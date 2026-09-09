#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_events.py -- pull FTC event / team / match data into CSV.

Two data sources, one CLI:

  --source ftc     Official FIRST FTC-Events API v2.0.  REQUIRES free credentials.
                   Base URL : https://ftc-api.firstinspires.org
                   Auth     : HTTP Basic  (username : AuthorizationKey)
                   Register : https://ftc-events.firstinspires.org/services/API/register
                   Docs     : https://ftc-events.firstinspires.org/api-docs
                   Spec     : https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json

  --source scout   Community FTCScout REST API v1.  NO credentials needed.
                   Base URL : https://api.ftcscout.org/rest/v1
                   GraphQL  : https://api.ftcscout.org/graphql
                   Docs     : https://ftcscout.org/api

Everything here is Python standard library.  No pip install.  This matters:
the laptop you run this on at an event will not have working Wi-Fi to install
anything, and often will not have working Wi-Fi at all -- so run this the night
BEFORE and print the output.

--------------------------------------------------------------------------------
VERIFICATION STATUS OF THE ENDPOINTS BELOW
--------------------------------------------------------------------------------
Every FTC-Events path in ENDPOINTS_FTC was extracted programmatically from the
official OpenAPI 3.0.1 document at
https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json on 2026-08-22.
Every FTCScout path in ENDPOINTS_SCOUT was exercised live against the real
server on 2026-08-22 and returned HTTP 200 with the documented shape.

If FIRST renumbers the API (a v3.0 path, a changed base host), you do NOT need
to hunt through this file: change API_BASE_FTC / API_VERSION_FTC / the one
ENDPOINTS_FTC entry, at the top of this file.  They are deliberately isolated
constants for exactly that reason.  Re-verify by running:

    python fetch_events.py check --source ftc
    curl -s https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json | python -m json.tool | less

--------------------------------------------------------------------------------
USAGE POLICY (quoted from the sources, 2026-08-22)
--------------------------------------------------------------------------------
FTC-Events: free, but "The data from this API may not be used for commercial
purposes."  FIRST asks that you "include a link back to this page" when you
display API-derived data.  Also: "Publicly distributing an application, code
snippet, etc, that has your username and token in it, encoded or not, WILL
result in your token being blocked from the API.  Each user should apply for
their own token."  ==> This script NEVER writes your token to disk or to any
output file, and never echoes it.  Do not commit your credentials file.

Rate limits are NOT documented.  Be polite: this script sends
If-Modified-Since when --cache-dir is set, sleeps between paged requests, and
retries with backoff rather than hammering.
"""

from __future__ import annotations

import argparse
import base64
import csv
import datetime as _dt
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

__version__ = "1.0.0"

# ==============================================================================
# CONFIGURABLE CONSTANTS -- change these if an API moves.  Nothing else needs to.
# ==============================================================================

# --- Official FIRST FTC-Events API ------------------------------------------
# VERIFIED 2026-08-22 against the OpenAPI document (servers[0].url is listed as
# http://; https works and is what we use).
API_BASE_FTC = "https://ftc-api.firstinspires.org"
API_VERSION_FTC = "v2.0"
FTC_REGISTER_URL = "https://ftc-events.firstinspires.org/services/API/register"
FTC_DOCS_URL = "https://ftc-events.firstinspires.org/api-docs"
FTC_SPEC_URL = "https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json"

# Path templates, relative to f"{API_BASE_FTC}/{API_VERSION_FTC}".
# VERIFIED 2026-08-22.  {season} is the STARTING year of the season:
#   BIOBUZZ 2026-27 -> 2026        DECODE 2025-26 -> 2025
ENDPOINTS_FTC = {
    "index":     "",                                        # API index; no auth needed
    "season":    "/{season}",
    "events":    "/{season}/events",                        # ?eventCode= | ?teamNumber=
    "teams":     "/{season}/teams",                         # ?teamNumber= ?eventCode= ?state= ?page=
    "schedule":  "/{season}/schedule/{eventCode}",          # ?tournamentLevel= ?teamNumber=
    "hybrid":    "/{season}/schedule/{eventCode}/{tournamentLevel}/hybrid",
    "matches":   "/{season}/matches/{eventCode}",           # ?tournamentLevel= ?teamNumber=
    "scores":    "/{season}/scores/{eventCode}/{tournamentLevel}",
    "rankings":  "/{season}/rankings/{eventCode}",          # ?teamNumber= ?top=
    "alliances": "/{season}/alliances/{eventCode}",
    "selection": "/{season}/alliances/{eventCode}/selection",
    "awards":    "/{season}/awards/{eventCode}",            # ?teamNumber=
    "awardlist": "/{season}/awards/list",
    "advance":   "/{season}/advancement/{eventCode}",       # ?excludeSkipped=
    "advpoints": "/{season}/advancement/{eventCode}/points",
}

# The JSON key holding the array, per FTC endpoint. VERIFIED 2026-08-22 from the
# OpenAPI component schemas (e.g. SeasonEventListingsModel_Version2.events).
FTC_ARRAY_KEY = {
    "events": "events",
    "teams": "teams",
    "schedule": "schedule",
    "hybrid": "schedule",
    "matches": "matches",
    "scores": "matchScores",
    "rankings": "rankings",
    "alliances": "alliances",
    "selection": "alliances",
    "awards": "awards",
    "awardlist": "awards",
}

# --- Community FTCScout API --------------------------------------------------
# VERIFIED 2026-08-22 by live request.  No authentication.
API_BASE_SCOUT = "https://api.ftcscout.org/rest/v1"
API_GRAPHQL_SCOUT = "https://api.ftcscout.org/graphql"
SCOUT_DOCS_URL = "https://ftcscout.org/api"

ENDPOINTS_SCOUT = {
    "team":       "/teams/{teamNumber}",
    "teamevents": "/teams/{teamNumber}/events/{season}",
    "quickstats": "/teams/{teamNumber}/quick-stats?season={season}",
    "event":      "/events/{season}/{eventCode}",
    "matches":    "/events/{season}/{eventCode}/matches",
    "teams":      "/events/{season}/{eventCode}/teams",
    "awards":     "/events/{season}/{eventCode}/awards",
}

# Identify ourselves. Replace the contact address with your team's.
USER_AGENT = (
    "BIOBUZZ-fetch-events/%s (FTC team scouting tool; "
    "set FTC_API_CONTACT env var to your email)" % __version__
)

HTTP_TIMEOUT = 30          # seconds
HTTP_RETRIES = 3
PAGE_SLEEP = 0.35          # seconds between paged requests -- be polite

# Exit codes
EXIT_OK = 0
EXIT_ERROR = 1
EXIT_NO_CREDENTIALS = 2
EXIT_HTTP = 3
EXIT_NO_DATA = 4


# ==============================================================================
# Small helpers
# ==============================================================================

class ApiError(RuntimeError):
    """Any non-recoverable API problem, carrying an exit code."""

    def __init__(self, message: str, code: int = EXIT_HTTP) -> None:
        super().__init__(message)
        self.code = code


def eprint(*a) -> None:
    print(*a, file=sys.stderr)


def default_season(today: _dt.date | None = None) -> int:
    """FTC seasons are named by their STARTING year and kick off in September.

    Anything from August onward belongs to the new season (kickoff for BIOBUZZ
    is 2026-09-12; pre-season manuals post in July/August).  Override with
    --season whenever you want last season's data.
    """
    d = today or _dt.date.today()
    return d.year if d.month >= 8 else d.year - 1


def flatten(obj, prefix: str = "", out: dict | None = None) -> dict:
    """Flatten nested dicts to dot.notation. Lists become compact JSON strings.

    Score-detail payloads are SEASON-SPECIFIC (the spec has a separate
    ScoreDetailModel_2019 ... ScoreDetailModel_2025, and BIOBUZZ will add a
    _2026).  Flattening generically means this script keeps working at kickoff
    without anybody editing it.
    """
    out = {} if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = "%s.%s" % (prefix, k) if prefix else str(k)
            if isinstance(v, dict):
                flatten(v, key, out)
            elif isinstance(v, list):
                if v and all(isinstance(x, (int, float, str, bool)) or x is None for x in v):
                    out[key] = "|".join("" if x is None else str(x) for x in v)
                else:
                    out[key] = json.dumps(v, separators=(",", ":"))
            else:
                out[key] = v
    else:
        out[prefix or "value"] = obj
    return out


def union_fieldnames(rows: list[dict]) -> list[str]:
    """Stable union of keys across rows: first-seen order, nothing dropped."""
    seen, order = set(), []
    for r in rows:
        for k in r:
            if k not in seen:
                seen.add(k)
                order.append(k)
    return order


def write_csv(rows: list[dict], out_path: str | None) -> int:
    if not rows:
        eprint("[warn] no rows to write.")
        return 0
    fields = union_fieldnames(rows)
    if out_path in (None, "-"):
        w = csv.DictWriter(sys.stdout, fieldnames=fields, extrasaction="ignore",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    else:
        p = Path(out_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        # utf-8-sig so Excel on Windows opens accented team names correctly.
        with p.open("w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        eprint("[ok] wrote %d rows x %d columns -> %s" % (len(rows), len(fields), p))
    return len(rows)


def write_raw_json(payload, out_path: str) -> None:
    p = Path(out_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    eprint("[ok] wrote raw JSON -> %s" % p)


# ==============================================================================
# Credentials
# ==============================================================================

CRED_FILENAMES = (".ftc-api-credentials", "ftc-api-credentials.txt")
CRED_HELP = """
No FTC-Events API credentials found.

The official API is free but requires a username + AuthorizationKey.
  1. Register (takes about a minute):  %s
     FIRST emails you a username and a UUID-looking AuthorizationKey.
  2. Give them to this script by ANY ONE of these:

     (a) Environment variables (recommended):
           Windows PowerShell:  $env:FTC_API_USER="you"; $env:FTC_API_TOKEN="uuid"
           bash/zsh:            export FTC_API_USER=you FTC_API_TOKEN=uuid

     (b) A credentials file, one 'key=value' per line, in this directory,
         your home directory, or a path given with --credentials:
           %s
         containing:
           user=yourusername
           token=7eaa6338-a097-4221-ac04-b6120fcc4d49

     (c) --user / --token on the command line (visible in shell history --
         least good option).

  3. ADD THE CREDENTIALS FILE TO .gitignore.  FIRST blocks tokens that get
     published, and each person is supposed to apply for their own.

You do NOT need credentials to use the community mirror:
     python fetch_events.py <command> --source scout ...
FTCScout carries the same match/team/award data, plus precomputed OPR, with no
signup at all.  It is a volunteer-run service; the official API is the source
of truth.
""" % (FTC_REGISTER_URL, " or ".join(CRED_FILENAMES))


def _parse_cred_file(path: Path) -> tuple[str | None, str | None]:
    user = token = None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None, None
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip().lower(), v.strip().strip('"').strip("'")
        if k in ("user", "username", "ftc_api_user"):
            user = v
        elif k in ("token", "key", "authorizationkey", "ftc_api_token"):
            token = v
    return user, token


def load_credentials(args) -> tuple[str, str]:
    """Resolve credentials or raise ApiError(EXIT_NO_CREDENTIALS) with real help."""
    user = getattr(args, "user", None) or os.environ.get("FTC_API_USER")
    token = getattr(args, "token", None) or os.environ.get("FTC_API_TOKEN")

    candidates: list[Path] = []
    if getattr(args, "credentials", None):
        candidates.append(Path(args.credentials).expanduser())
    for name in CRED_FILENAMES:
        candidates.append(Path.cwd() / name)
        candidates.append(Path(__file__).resolve().parent / name)
        candidates.append(Path.home() / name)

    for c in candidates:
        if user and token:
            break
        if c.is_file():
            fu, ft = _parse_cred_file(c)
            user = user or fu
            token = token or ft
            if fu or ft:
                eprint("[info] read credentials from %s" % c)

    if not user or not token:
        raise ApiError(CRED_HELP, EXIT_NO_CREDENTIALS)
    return user, token


# ==============================================================================
# HTTP
# ==============================================================================

def _cache_paths(cache_dir: str | None, url: str) -> tuple[Path, Path] | None:
    if not cache_dir:
        return None
    d = Path(cache_dir)
    d.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:20]
    return d / ("%s.json" % h), d / ("%s.meta" % h)


def http_get_json(url: str, headers: dict | None = None,
                  cache_dir: str | None = None, verbose: bool = False):
    """GET a URL, return parsed JSON. Retries on 5xx/timeouts with backoff.

    Honours the FTC-Events Last-Modified / If-Modified-Since contract when
    --cache-dir is set: a 304 means "nothing changed", and we serve the cached
    body.  This is the documented, polite way to poll the API.
    """
    hdrs = {"Accept": "application/json",
            "User-Agent": os.environ.get("FTC_API_CONTACT_UA", USER_AGENT)}
    if headers:
        hdrs.update(headers)

    cp = _cache_paths(cache_dir, url)
    if cp and cp[1].is_file():
        try:
            lm = json.loads(cp[1].read_text(encoding="utf-8")).get("lastModified")
            if lm:
                hdrs["If-Modified-Since"] = lm
        except Exception:
            pass

    last_err = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = urllib.request.Request(url, headers=hdrs, method="GET")
        try:
            if verbose:
                eprint("[http] GET %s (attempt %d)" % (url, attempt))
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                if cp:
                    lm = resp.headers.get("Last-Modified")
                    cp[0].write_text(body, encoding="utf-8")
                    cp[1].write_text(json.dumps({"lastModified": lm, "url": url}),
                                     encoding="utf-8")
                if not body.strip():
                    return None
                return json.loads(body)
        except urllib.error.HTTPError as e:
            if e.code == 304 and cp and cp[0].is_file():
                if verbose:
                    eprint("[http] 304 Not Modified -- using cache")
                return json.loads(cp[0].read_text(encoding="utf-8"))
            detail = ""
            try:
                detail = e.read().decode("utf-8", errors="replace")[:400]
            except Exception:
                pass
            if e.code == 401:
                raise ApiError(
                    "HTTP 401 Unauthorized from the FTC-Events API.\n"
                    "Your username/AuthorizationKey pair was rejected. Check for a\n"
                    "trailing space, a swapped user/token, or an expired key.\n"
                    "Re-register at %s\nServer said: %s" % (FTC_REGISTER_URL, detail),
                    EXIT_NO_CREDENTIALS)
            if e.code == 404:
                raise ApiError(
                    "HTTP 404. For this API a 404 means the SEASON was valid and the\n"
                    "eventCode looked well-formed, but no event matched that combination.\n"
                    "Event codes change year to year. Check the code at\n"
                    "https://ftc-events.firstinspires.org/ or run:  fetch_events.py events\n"
                    "Server said: %s" % detail, EXIT_NO_DATA)
            if e.code == 400:
                raise ApiError("HTTP 400 -- malformed parameter (bad season, bad event "
                               "code, non-numeric team). Server said: %s" % detail, EXIT_HTTP)
            if e.code == 501:
                raise ApiError("HTTP 501 -- this API rejects that COMBINATION of optional\n"
                               "parameters (e.g. teamNumber together with eventCode on "
                               "/teams).\nServer said: %s" % detail, EXIT_HTTP)
            if 500 <= e.code < 600 and attempt < HTTP_RETRIES:
                last_err = e
                time.sleep(2 ** attempt)
                continue
            raise ApiError("HTTP %s from %s\n%s" % (e.code, url, detail), EXIT_HTTP)
        except urllib.error.URLError as e:
            last_err = e
            if attempt < HTTP_RETRIES:
                time.sleep(2 ** attempt)
                continue
            raise ApiError(
                "Network error reaching %s\n  %s\n"
                "If you are at a venue: venue Wi-Fi is why you print this data the "
                "night before." % (url, e), EXIT_HTTP)
        except json.JSONDecodeError as e:
            raise ApiError("Response was not JSON (%s). URL: %s" % (e, url), EXIT_HTTP)
    raise ApiError("Giving up after %d attempts: %s" % (HTTP_RETRIES, last_err), EXIT_HTTP)


def ftc_get(key: str, path_params: dict, query: dict | None, creds: tuple[str, str],
            cache_dir: str | None, verbose: bool):
    template = ENDPOINTS_FTC[key]
    path = template.format(**path_params) if path_params else template
    url = "%s/%s%s" % (API_BASE_FTC, API_VERSION_FTC, path)
    q = {k: v for k, v in (query or {}).items() if v is not None and v != ""}
    if q:
        url += "?" + urllib.parse.urlencode(q)
    user, token = creds
    blob = base64.b64encode(("%s:%s" % (user, token)).encode("utf-8")).decode("ascii")
    return http_get_json(url, {"Authorization": "Basic " + blob}, cache_dir, verbose)


def scout_get(key: str, path_params: dict, cache_dir: str | None, verbose: bool):
    path = ENDPOINTS_SCOUT[key].format(**path_params)
    return http_get_json(API_BASE_SCOUT + path, None, cache_dir, verbose)


def scout_graphql(query: str, variables: dict | None, verbose: bool):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = urllib.request.Request(
        API_GRAPHQL_SCOUT, data=payload, method="POST",
        headers={"Content-Type": "application/json", "Accept": "application/json",
                 "User-Agent": USER_AGENT})
    if verbose:
        eprint("[http] POST %s" % API_GRAPHQL_SCOUT)
    try:
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise ApiError("Network error reaching FTCScout GraphQL: %s" % e, EXIT_HTTP)
    if "errors" in data:
        raise ApiError("FTCScout GraphQL error: %s" %
                       json.dumps(data["errors"])[:600], EXIT_HTTP)
    return data.get("data") or {}


# ==============================================================================
# Row shaping
# ==============================================================================

def _station_key(team_row: dict) -> str | None:
    """Normalise a match-team entry to a column name like 'Red1' / 'Blue2'.

    FTC-Events puts the whole thing in `station` ("Red1").
    FTCScout splits it into `alliance` ("Red") + `station` ("One").
    """
    st = team_row.get("station")
    if isinstance(st, str) and st[:3].lower() in ("red", "blu"):
        return st.replace(" ", "")
    alliance = team_row.get("alliance")
    ordinal = {"one": "1", "two": "2", "three": "3"}.get(str(st).lower(), str(st))
    if alliance:
        return "%s%s" % (alliance, ordinal)
    return None


def expand_match_rows(matches: list[dict]) -> list[dict]:
    """One row per match, with Red1/Red2/Blue1/Blue2 team-number columns."""
    rows = []
    for m in matches or []:
        base = {k: v for k, v in m.items() if k not in ("teams", "scores")}
        row = flatten(base)
        for t in m.get("teams") or []:
            col = _station_key(t)
            if not col:
                continue
            row[col] = t.get("teamNumber")
            if t.get("surrogate"):
                row[col + "_surrogate"] = True
            if t.get("noShow"):
                row[col + "_noShow"] = True
            if t.get("dq"):
                row[col + "_dq"] = True
            if t.get("onField") is False:
                row[col + "_onField"] = False
        # FTCScout nests full score breakdowns under scores.red / scores.blue
        if isinstance(m.get("scores"), dict):
            row.update(flatten(m["scores"], "score"))
        rows.append(row)
    return rows


def rows_from_array(payload, array_key: str) -> list[dict]:
    if payload is None:
        return []
    if isinstance(payload, list):
        items = payload
    elif isinstance(payload, dict):
        items = payload.get(array_key)
        if items is None:
            # Single-object endpoints (FTCScout /events/{season}/{code}).
            return [flatten(payload)]
    else:
        return []
    return [flatten(i) for i in (items or [])]


# ==============================================================================
# Commands
# ==============================================================================

def cmd_check(args) -> int:
    """Connectivity + credential + season sanity check. Run this FIRST."""
    print("fetch_events.py %s" % __version__)
    print("python %s on %s" % (sys.version.split()[0], sys.platform))
    print("default season if --season omitted: %d "
          "(FTC seasons are named by their starting year)" % default_season())
    print("")
    print("-- FTCScout (no credentials required) ------------------------------")
    try:
        t = scout_get("team", {"teamNumber": 16321}, None, args.verbose)
        print("  OK  %s -> team 16321 = %r" % (API_BASE_SCOUT, t.get("name")))
    except ApiError as e:
        print("  FAIL  %s" % e)
    print("")
    print("-- FTC-Events official API ----------------------------------------")
    try:
        idx = http_get_json("%s/%s" % (API_BASE_FTC, API_VERSION_FTC),
                            None, None, args.verbose)
        print("  index reachable (no auth needed for the index):")
        print("    apiVersion=%s status=%s currentSeason=%s maxSeason=%s"
              % (idx.get("apiVersion"), idx.get("status"),
                 idx.get("currentSeason"), idx.get("maxSeason")))
    except ApiError as e:
        print("  index FAIL: %s" % e)
    try:
        creds = load_credentials(args)
        print("  credentials found for user %r (token not shown)" % creds[0])
        data = ftc_get("season", {"season": args.season}, None, creds, None, args.verbose)
        if data:
            print("  OK  authenticated call succeeded: season %s gameName=%r "
                  "teamCount=%s eventCount=%s"
                  % (args.season, data.get("gameName"), data.get("teamCount"),
                     data.get("eventCount")))
        else:
            print("  authenticated call returned an empty body for season %s "
                  "(season may not have started)" % args.season)
    except ApiError as e:
        if e.code == EXIT_NO_CREDENTIALS:
            print("  NO CREDENTIALS -- the official API is unavailable to this "
                  "machine right now.")
            print("  Use --source scout for everything, or set credentials up:")
            print(str(e))
        else:
            print("  authenticated call FAILED: %s" % e)
    print("")
    print("Docs: %s\n      %s" % (FTC_DOCS_URL, SCOUT_DOCS_URL))
    return EXIT_OK


def cmd_endpoints(args) -> int:
    print("FTC-Events API   base: %s/%s   (HTTP Basic auth REQUIRED)"
          % (API_BASE_FTC, API_VERSION_FTC))
    print("  verified 2026-08-22 against %s" % FTC_SPEC_URL)
    for k, v in ENDPOINTS_FTC.items():
        print("    %-10s GET %s" % (k, v or "/"))
    print("")
    print("FTCScout REST    base: %s   (no auth)" % API_BASE_SCOUT)
    print("  verified 2026-08-22 by live request")
    for k, v in ENDPOINTS_SCOUT.items():
        print("    %-10s GET %s" % (k, v))
    print("")
    print("FTCScout GraphQL      : %s" % API_GRAPHQL_SCOUT)
    return EXIT_OK


def _emit(rows, args) -> int:
    if args.raw_json:
        write_raw_json(rows, args.raw_json)
    n = write_csv(rows, args.out)
    return EXIT_OK if n else EXIT_NO_DATA


def cmd_events(args) -> int:
    if args.source == "scout":
        if args.event_code:
            payload = scout_get("event", {"season": args.season,
                                          "eventCode": args.event_code},
                                args.cache_dir, args.verbose)
            return _emit([flatten(payload)], args)
        if args.team:
            # "Every event OUR team attended this season", with the per-event
            # stats block attached.  VERIFIED 2026-08-22 against
            # GET /rest/v1/teams/{n}/events/{season}.  This is what
            # PROMPTS-scouting.md SC12 (season trend report) needs.
            payload = scout_get("teamevents", {"teamNumber": args.team,
                                               "season": args.season},
                                args.cache_dir, args.verbose)
            return _emit([flatten(e) for e in payload or []], args)
        # VERIFIED 2026-08-22 by GraphQL introspection of api.ftcscout.org:
        # Event has NO flat venue/city/state/country -- they live under
        # location { venue city state country }.  Re-introspect with:
        #   curl -s -X POST https://api.ftcscout.org/graphql         #     -H 'Content-Type: application/json'         #     -d '{"query":"{__type(name:\"Event\"){fields{name}}}"}'
        q = """query($season: Int!, $limit: Int, $region: RegionOption) {
                 eventsSearch(season: $season, limit: $limit, region: $region) {
                   season code divisionCode name start end type
                   regionCode leagueCode districtCode
                   remote hybrid published fieldCount timezone
                   hasMatches started ongoing finished website
                   location { venue city state country }
                 } }"""
        data = scout_graphql(q, {"season": args.season, "limit": args.limit,
                                 "region": getattr(args, "region", None)},
                             args.verbose)
        return _emit([flatten(e) for e in data.get("eventsSearch") or []], args)

    creds = load_credentials(args)
    payload = ftc_get("events", {"season": args.season},
                      {"eventCode": args.event_code, "teamNumber": args.team},
                      creds, args.cache_dir, args.verbose)
    return _emit(rows_from_array(payload, FTC_ARRAY_KEY["events"]), args)


def cmd_teams(args) -> int:
    if args.source == "scout":
        if args.event_code:
            payload = scout_get("teams", {"season": args.season,
                                          "eventCode": args.event_code},
                                args.cache_dir, args.verbose)
            return _emit([flatten(t) for t in payload or []], args)
        if args.team:
            info = scout_get("team", {"teamNumber": args.team},
                             args.cache_dir, args.verbose)
            row = flatten(info)
            try:
                qs = scout_get("quickstats", {"teamNumber": args.team,
                                              "season": args.season},
                               args.cache_dir, args.verbose)
                row.update(flatten(qs, "quickStats"))
            except ApiError as e:
                eprint("[warn] quick-stats unavailable: %s" % e)
            return _emit([row], args)
        raise ApiError("--source scout needs either --event-code or --team for "
                       "'teams'.  FTCScout has no whole-season team dump.", EXIT_ERROR)

    creds = load_credentials(args)
    rows, page, total = [], 1, 1
    while page <= total:
        payload = ftc_get(
            "teams", {"season": args.season},
            {"teamNumber": args.team, "eventCode": args.event_code,
             "state": args.state, "page": page,
             "excludeNonCompeting": "true" if args.exclude_non_competing else None},
            creds, args.cache_dir, args.verbose)
        if not payload:
            break
        rows.extend(flatten(t) for t in payload.get("teams") or [])
        total = int(payload.get("pageTotal") or 1)
        if args.verbose:
            eprint("[info] page %d/%d (%d rows so far)" % (page, total, len(rows)))
        page += 1
        if page <= total:
            time.sleep(PAGE_SLEEP)
    return _emit(rows, args)


def cmd_matches(args) -> int:
    if args.source == "scout":
        payload = scout_get("matches", {"season": args.season,
                                        "eventCode": args.event_code},
                            args.cache_dir, args.verbose)
        return _emit(expand_match_rows(payload or []), args)

    creds = load_credentials(args)
    payload = ftc_get("matches", {"season": args.season, "eventCode": args.event_code},
                      {"tournamentLevel": args.level, "teamNumber": args.team},
                      creds, args.cache_dir, args.verbose)
    return _emit(expand_match_rows(
        (payload or {}).get(FTC_ARRAY_KEY["matches"]) or []), args)


def cmd_schedule(args) -> int:
    if args.source == "scout":
        raise ApiError("FTCScout REST does not expose a pre-match schedule "
                       "endpoint. Use --source ftc for 'schedule'.", EXIT_ERROR)
    creds = load_credentials(args)
    payload = ftc_get("schedule", {"season": args.season, "eventCode": args.event_code},
                      {"tournamentLevel": args.level, "teamNumber": args.team},
                      creds, args.cache_dir, args.verbose)
    return _emit(expand_match_rows(
        (payload or {}).get(FTC_ARRAY_KEY["schedule"]) or []), args)


def cmd_rankings(args) -> int:
    if args.source == "scout":
        payload = scout_get("teams", {"season": args.season,
                                      "eventCode": args.event_code},
                            args.cache_dir, args.verbose)
        rows = []
        for t in payload or []:
            r = flatten(t)
            if t.get("stats"):
                rows.append(r)
        rows.sort(key=lambda r: (r.get("stats.rank") is None, r.get("stats.rank")))
        return _emit(rows, args)

    creds = load_credentials(args)
    payload = ftc_get("rankings", {"season": args.season, "eventCode": args.event_code},
                      {"teamNumber": args.team, "top": args.top},
                      creds, args.cache_dir, args.verbose)
    return _emit(rows_from_array(payload, FTC_ARRAY_KEY["rankings"]), args)


def cmd_awards(args) -> int:
    if args.source == "scout":
        payload = scout_get("awards", {"season": args.season,
                                       "eventCode": args.event_code},
                            args.cache_dir, args.verbose)
        return _emit([flatten(a) for a in payload or []], args)
    creds = load_credentials(args)
    payload = ftc_get("awards", {"season": args.season, "eventCode": args.event_code},
                      {"teamNumber": args.team}, creds, args.cache_dir, args.verbose)
    return _emit(rows_from_array(payload, FTC_ARRAY_KEY["awards"]), args)


def cmd_alliances(args) -> int:
    if args.source == "scout":
        raise ApiError("FTCScout REST does not expose alliance selection. "
                       "Use --source ftc for 'alliances'.", EXIT_ERROR)
    creds = load_credentials(args)
    key = "selection" if args.selection else "alliances"
    payload = ftc_get(key, {"season": args.season, "eventCode": args.event_code},
                      None, creds, args.cache_dir, args.verbose)
    return _emit(rows_from_array(payload, FTC_ARRAY_KEY[key]), args)


def cmd_scores(args) -> int:
    """Score BREAKDOWN. The columns are season-specific and change at kickoff."""
    if args.source == "scout":
        payload = scout_get("matches", {"season": args.season,
                                        "eventCode": args.event_code},
                            args.cache_dir, args.verbose)
        rows = []
        for m in payload or []:
            sc = m.get("scores") or {}
            for side in ("red", "blue"):
                if isinstance(sc.get(side), dict):
                    r = {"matchId": m.get("id"),
                         "tournamentLevel": m.get("tournamentLevel"),
                         "hasBeenPlayed": m.get("hasBeenPlayed")}
                    r.update(flatten(sc[side]))
                    rows.append(r)
        return _emit(rows, args)

    creds = load_credentials(args)
    payload = ftc_get("scores",
                      {"season": args.season, "eventCode": args.event_code,
                       "tournamentLevel": args.level or "qual"},
                      {"teamNumber": args.team}, creds, args.cache_dir, args.verbose)
    raw = (payload or {}).get(FTC_ARRAY_KEY["scores"]) or []
    rows = []
    for m in raw:
        base = {k: v for k, v in m.items() if k != "alliances"}
        for a in m.get("alliances") or []:
            r = flatten(base)
            r.update(flatten(a))
            rows.append(r)
        if not m.get("alliances"):
            rows.append(flatten(m))
    return _emit(rows, args)


def cmd_dossier(args) -> int:
    """One row per team at an event: identity + season quick stats + event stats.

    This is the pre-event artefact you actually print.  FTCScout only -- it is
    the source that serves precomputed OPR, which the official API does not.
    """
    at_event = scout_get("teams", {"season": args.season, "eventCode": args.event_code},
                         args.cache_dir, args.verbose) or []
    if not at_event:
        eprint("[warn] no teams registered for %s in season %d yet."
               % (args.event_code, args.season))
        return EXIT_NO_DATA
    rows = []
    for i, entry in enumerate(at_event, 1):
        num = entry.get("teamNumber")
        # Seed the identity columns so the CSV column ORDER is stable even when
        # an individual lookup fails -- a printed sheet with shifting columns is
        # worse than useless in a pit.
        row = {"teamNumber": num, "name": "", "city": "", "state": "",
               "country": "", "rookieYear": "", "opr_tot": "", "rank_tot": "",
               "opr_auto": "", "rank_auto": "", "opr_dc": "", "rank_dc": "",
               "opr_eg": "", "rank_eg": "", "opr_pool": ""}
        try:
            info = scout_get("team", {"teamNumber": num}, args.cache_dir, args.verbose)
            row.update({"name": info.get("name"), "city": info.get("city"),
                        "state": info.get("state"), "country": info.get("country"),
                        "rookieYear": info.get("rookieYear")})
        except ApiError as e:
            eprint("[warn] team %s info: %s" % (num, e))
        try:
            qs = scout_get("quickstats", {"teamNumber": num, "season": args.season},
                           args.cache_dir, args.verbose)
            if qs:
                for band in ("tot", "auto", "dc", "eg"):
                    if isinstance(qs.get(band), dict):
                        row["opr_%s" % band] = round(qs[band].get("value") or 0.0, 2)
                        row["rank_%s" % band] = qs[band].get("rank")
                row["opr_pool"] = qs.get("count")
        except ApiError as e:
            eprint("[warn] team %s quick-stats: %s" % (num, e))
        if isinstance(entry.get("stats"), dict):
            st = entry["stats"]
            row.update({"event_rank": st.get("rank"), "event_rp": st.get("rp"),
                        "event_w": st.get("wins"), "event_l": st.get("losses"),
                        "event_t": st.get("ties"),
                        "event_qm": st.get("qualMatchesPlayed")})
        # Blank human-observation columns -- the scout fills these in by hand.
        for col in ("auto_start_position", "auto_reliability_1to5", "cycle_time_s",
                    "downtime_seen", "downtime_cause", "driver_1to5",
                    "defense_1to5", "endgame_capability", "pit_notes", "verdict"):
            row.setdefault(col, "")
        rows.append(row)
        if i % 10 == 0:
            eprint("[info] %d/%d teams" % (i, len(at_event)))
        time.sleep(PAGE_SLEEP)
    rows.sort(key=lambda r: -(r.get("opr_tot") if isinstance(r.get("opr_tot"),
                                                             (int, float)) else 0.0))
    return _emit(rows, args)


# ==============================================================================
# CLI
# ==============================================================================

EPILOG = """\
EXAMPLES
  # 0. Always run this first on a new machine.
  python fetch_events.py check

  # 1. No credentials at all -- community mirror. Works today.
  python fetch_events.py events    --source scout --season 2025 --limit 50 --out events.csv
  python fetch_events.py events    --source scout --season 2025 --region USTXHO
  python fetch_events.py events    --source scout --season 2025 --team 16321   # our season
  python fetch_events.py matches   --source scout --season 2025 --event-code USTXHOCMP --out m.csv
  python fetch_events.py awards    --source scout --season 2024 --event-code FTCCMP1   --out a.csv
  # (those three event codes were run live on 2026-08-22 and returned real rows;
  #  the USTXHOQ1 below is a PLACEHOLDER -- substitute your own event code.)

  # 2. The pre-event artefact you print the night before.
  python fetch_events.py dossier   --season 2026 --event-code USTXHOQ1 --out dossier.csv

  # 3. With official credentials.
  python fetch_events.py events    --season 2026 --out events-2026.csv
  python fetch_events.py teams     --season 2026 --event-code USTXHOQ1 --out roster.csv
  python fetch_events.py schedule  --season 2026 --event-code USTXHOQ1 --level qual
  python fetch_events.py rankings  --season 2026 --event-code USTXHOQ1 --out rank.csv
  python fetch_events.py alliances --season 2026 --event-code USTXHOQ1 --selection
  python fetch_events.py scores    --season 2026 --event-code USTXHOQ1 --level qual --out sc.csv

  # 4. Answer "what did it take to advance out of my region last year?"
  python fetch_events.py events --season 2025 --out e25.csv
  #   then look up your regional championship code and pull its rankings + awards.

SEASON NUMBERS
  BIOBUZZ 2026-27 = 2026     DECODE 2025-26 = 2025     INTO THE DEEP 2024-25 = 2024

EXIT CODES
  0 ok   1 usage/logic error   2 missing or rejected credentials
  3 HTTP/network error         4 request succeeded but returned no rows

ATTRIBUTION
  FTC-Events data may not be used commercially; FIRST asks for a link back to
  https://ftc-events.firstinspires.org/services/API .  FTCScout is a
  volunteer-run community service -- credit https://ftcscout.org .
"""


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="fetch_events.py",
        description="Pull FTC event / team / match / award data into CSV from the "
                    "official FTC-Events API or the FTCScout community mirror.",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version="fetch_events.py " + __version__)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--source", choices=("ftc", "scout"), default="ftc",
                        help="ftc = official API (needs credentials); "
                             "scout = FTCScout community mirror (no credentials). "
                             "Default: ftc")
    common.add_argument("--season", type=int, default=default_season(),
                        help="Starting year of the season. BIOBUZZ 2026-27 = 2026. "
                             "Default: %d" % default_season())
    common.add_argument("--event-code", "-e", default=None,
                        help="Event code, e.g. USTXHOQ1. Case-insensitive.")
    common.add_argument("--team", "-t", type=int, default=None, help="Team number filter.")
    common.add_argument("--out", "-o", default=None,
                        help="CSV output path. Omit or '-' for stdout.")
    common.add_argument("--raw-json", default=None,
                        help="Also dump the shaped rows as JSON to this path.")
    common.add_argument("--cache-dir", default=None,
                        help="Cache responses here and send If-Modified-Since on "
                             "later runs (the API's documented polite-polling "
                             "mechanism).")
    common.add_argument("--user", default=None,
                        help="FTC-Events username (prefer FTC_API_USER env var).")
    common.add_argument("--token", default=None,
                        help="FTC-Events AuthorizationKey (prefer FTC_API_TOKEN "
                             "env var; --token lands in your shell history).")
    common.add_argument("--credentials", default=None,
                        help="Path to a key=value credentials file.")
    common.add_argument("--verbose", "-v", action="store_true", help="Log every request.")

    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("check", parents=[common],
                       help="Connectivity, credential and season sanity check.")
    s.set_defaults(func=cmd_check)

    s = sub.add_parser("endpoints", parents=[common],
                       help="Print every endpoint this script knows about.")
    s.set_defaults(func=cmd_endpoints)

    s = sub.add_parser("events", parents=[common],
                       help="Event listings for a season, a region, one event, "
                            "or every event ONE TEAM attended.")
    s.add_argument("--limit", type=int, default=200,
                   help="scout source only: max events to return. Default 200.")
    s.add_argument("--region", default=None,
                   help="scout source only: FTCScout RegionOption enum value, "
                        "e.g. USTXHO, USNYLI, USCHS, CAON, All. Run "
                        "'fetch_events.py endpoints' for the full list. "
                        "VERIFIED 2026-08-22; re-check by introspecting "
                        "RegionOption on the GraphQL endpoint.")
    s.set_defaults(func=cmd_events)

    s = sub.add_parser("teams", parents=[common],
                       help="Team listings for a season, an event, or one team.")
    s.add_argument("--state", default=None,
                   help="ftc source only: full legal state/province name, "
                        "e.g. 'New Hampshire'.")
    s.add_argument("--exclude-non-competing", action="store_true",
                   help="ftc source only: valid only with --event-code.")
    s.set_defaults(func=cmd_teams)

    s = sub.add_parser("matches", parents=[common],
                       help="Played match results for an event.")
    s.add_argument("--level", choices=("qual", "playoff"), default=None,
                   help="tournamentLevel filter.")
    s.set_defaults(func=cmd_matches)

    s = sub.add_parser("schedule", parents=[common],
                       help="Scheduled (including future) matches. ftc source only.")
    s.add_argument("--level", choices=("qual", "playoff"), default=None)
    s.set_defaults(func=cmd_schedule)

    s = sub.add_parser("rankings", parents=[common], help="Event rankings.")
    s.add_argument("--top", type=int, default=None,
                   help="ftc source only: return only the top N.")
    s.set_defaults(func=cmd_rankings)

    s = sub.add_parser("awards", parents=[common], help="Awards given at an event.")
    s.set_defaults(func=cmd_awards)

    s = sub.add_parser("alliances", parents=[common],
                       help="Playoff alliances. ftc source only.")
    s.add_argument("--selection", action="store_true",
                   help="Use the /selection variant: the actual draft order and "
                        "declines. This is the single most under-used endpoint in "
                        "the API.")
    s.set_defaults(func=cmd_alliances)

    s = sub.add_parser("scores", parents=[common],
                       help="Per-alliance score BREAKDOWN. Columns are "
                            "season-specific and change at kickoff.")
    s.add_argument("--level", choices=("qual", "playoff"), default="qual")
    s.set_defaults(func=cmd_scores)

    s = sub.add_parser("dossier", parents=[common],
                       help="Pre-event scouting sheet: every team at an event with "
                            "season OPR plus blank human-observation columns. "
                            "Uses FTCScout; no credentials needed.")
    s.set_defaults(func=cmd_dossier)

    return p


def main(argv=None) -> int:
    # Line-buffer stdout. Python block-buffers stdout whenever it is not a TTY (piped to
    # a file, into `head`, or captured by a CI job), so on a slow or dead network this
    # tool printed NOTHING AT ALL until it exited -- not even the banner it writes before
    # its first request. Measured 2026-08-22: `check` piped to a file produced 0 bytes
    # after 90s and had to be killed. A diagnostic command that looks frozen is worse
    # than one that fails, so flush as we go.
    try:
        sys.stdout.reconfigure(line_buffering=True)
        sys.stderr.reconfigure(line_buffering=True)
    except Exception:
        pass

    args = build_parser().parse_args(argv)

    needs_event = ("matches", "schedule", "rankings", "awards", "alliances",
                   "scores", "dossier")
    if args.command in needs_event and not args.event_code:
        eprint("error: %s requires --event-code (e.g. --event-code USTXHOQ1).\n"
               "       Find codes with:  python fetch_events.py events --source scout "
               "--season %d" % (args.command, args.season))
        return EXIT_ERROR
    if args.command == "dossier":
        args.source = "scout"   # dossier is defined against FTCScout's OPR data

    try:
        return args.func(args)
    except ApiError as e:
        eprint("")
        eprint(str(e))
        return e.code
    except KeyboardInterrupt:
        eprint("\ninterrupted.")
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
