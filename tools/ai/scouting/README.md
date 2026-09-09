# Scouting data toolkit

Everything here is **Python standard library only**. No `pip install`. That is
deliberate: the laptop you use at a venue often has no working network, and you
cannot install anything when you need this most.

| File | What it is |
|---|---|
| `fetch_events.py` | Pulls event / team / match / ranking / award / score data into CSV from the official FTC-Events API **or** the FTCScout community mirror. `python fetch_events.py --help` |
| `README.md` | This file — API access, verification status, the 45-minute event pipeline |

**Related**
- Prompt library for this workstream: `../PROMPTS-scouting.md`
- Strategy, OPR's real limits, alliance-selection negotiation: `../../../research/SCOUTING-AND-AWARDS.md` §1–§6
- A ready-to-run OPR/pick-list script (pure stdlib, Cholesky solve): `../../../research/SCOUTING-AND-AWARDS.md` §5.3a

---

## 1. Quick start (60 seconds, no signup)

```bash
cd "tools/ai/scouting"

# Does anything work at all?
python fetch_events.py check

# No credentials needed — community mirror, last season's data:
python fetch_events.py events  --source scout --season 2025 --region USTXHO --limit 20
python fetch_events.py matches --source scout --season 2025 -e USTXHOCMP -o m.csv
python fetch_events.py awards  --source scout --season 2024 -e FTCCMP1   -o a.csv

# The one you will actually run before every event:
python fetch_events.py dossier --season 2026 -e <YOUR-EVENT-CODE> -o dossier.csv
```

`--help` on the top level and on every subcommand carries real examples.
`python fetch_events.py endpoints` prints every URL the script knows about.

---

## 2. The two data sources

### 2.1 Official FTC-Events API — FIRST

**[FACT — verified 2026-08-22]**

| Property | Value |
|---|---|
| Base URL | `https://ftc-api.firstinspires.org` (the OpenAPI `servers` entry lists `http://`; HTTPS works and is what the script uses) |
| Version path | `/v2.0/…` |
| Auth | **HTTP Basic.** `Authorization: Basic <base64(username:AuthorizationKey)>` |
| Register | <https://ftc-events.firstinspires.org/services/API/register> |
| Docs | <https://ftc-events.firstinspires.org/api-docs> · interactive: <https://ftc-events.firstinspires.org/try-it-out> |
| OpenAPI spec | <https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json> |
| Cost | Free |
| Restriction | *"The data from this API may not be used for commercial purposes."* |
| Attribution | The API page asks you to *"include a link back to this page"* when you display API-derived data |
| Rate limits | **Not documented anywhere.** UNVERIFIED. Be polite: cache, and use `--cache-dir`. |
| Caching | `Last-Modified` / `If-Modified-Since` → HTTP 304 when unchanged. Also a custom `FMS-OnlyModifiedSince` header for partial updates. |
| Freshness | *"Information is currently made available after the conclusion of the tournament. The API will provide data as soon as it has synced, and we do not add any artificial delays."* |

**Verification method:** the endpoint list in `fetch_events.py` (`ENDPOINTS_FTC`)
was extracted **programmatically** from the OpenAPI 3.0.1 document on
2026-08-22, not written from memory. A live unauthenticated request to
`/v2.0/2025/events?eventCode=…` returned **HTTP 401**, confirming auth is
mandatory; a request to the index `/v2.0` returned **HTTP 200** with
`"currentSeason": 2026`, confirming the season number for BIOBUZZ.

**Every endpoint** (all of these are in the script):

| Path | Gives you |
|---|---|
| `/v2.0` | API index — `currentSeason`, `maxSeason`, status. **No auth needed.** |
| `/v2.0/{season}` | Season summary: `gameName`, `kickoff`, `teamCount`, `eventCount` |
| `/v2.0/{season}/events` | Every official event. `?eventCode=` or `?teamNumber=` |
| `/v2.0/{season}/teams` | Team listings. `?teamNumber= ?eventCode= ?state= ?page=` (paged) |
| `/v2.0/{season}/schedule/{eventCode}` | Scheduled matches, **including future ones** |
| `/v2.0/{season}/schedule/{eventCode}/{level}/hybrid` | Played + upcoming in one call |
| `/v2.0/{season}/matches/{eventCode}` | Played match results |
| `/v2.0/{season}/scores/{eventCode}/{level}` | Per-alliance score **breakdown** |
| `/v2.0/{season}/rankings/{eventCode}` | Rankings, RP, tiebreakers, W-L-T |
| `/v2.0/{season}/alliances/{eventCode}` | Playoff alliances |
| `/v2.0/{season}/alliances/{eventCode}/selection` | **The actual draft order and declines** |
| `/v2.0/{season}/awards/{eventCode}` | Awards given at an event |
| `/v2.0/{season}/awards/{teamNumber}` | Everything one team has won this season |
| `/v2.0/{season}/awards/list` | The season's award catalogue |
| `/v2.0/{season}/advancement/{eventCode}` | Who advanced from an event |
| `/v2.0/{season}/advancement/{eventCode}/points` | **Official advancement point totals** |
| `/v2.0/{season}/leagues…` | League listings, membership, rankings |

**[JUDGMENT] The two endpoints nobody uses and everybody should:**
`/alliances/{eventCode}/selection` gives you the real draft order and declines at
past events, and `/advancement/{eventCode}/points` gives you the official
advancement totals. Together they answer *"what did it actually take to advance
out of my region last year?"* with data instead of folklore. See
`../PROMPTS-scouting.md` SC8.

### 2.2 FTCScout — community

**[FACT — verified by live request 2026-08-22]**

| Property | Value |
|---|---|
| REST base | `https://api.ftcscout.org/rest/v1` |
| GraphQL | `https://api.ftcscout.org/graphql` |
| Docs | <https://ftcscout.org/api> |
| Auth | **None.** |
| Why you want it | It serves **precomputed OPR** (total, auto, driver-controlled, endgame — each with a value and a global rank), which the official API does not. |

Endpoints the script uses, all confirmed returning HTTP 200:

| Path | Gives you |
|---|---|
| `/teams/{number}` | Team identity: name, school, city, rookie year |
| `/teams/{number}/events/{season}` | Every event the team attended, with full per-event stats. Reached by `events --source scout --team <n> --season <yyyy>` — this is the input to the season-trend report, `../PROMPTS-scouting.md` SC12 |
| `/teams/{number}/quick-stats?season={season}` | OPR bands `tot` / `auto` / `dc` / `eg`, each `{value, rank}`, plus the size of the comparison pool |
| `/events/{season}/{code}` | Event details |
| `/events/{season}/{code}/matches` | Matches with the **full score breakdown nested under `scores.red` / `scores.blue`** |
| `/events/{season}/{code}/teams` | Teams at the event, each with rank, RP, W-L-T and component totals |
| `/events/{season}/{code}/awards` | Awards |

GraphQL `eventsSearch(season:, limit:, region:)` is used for the season-wide
event list, because REST has no "all events in a season" route. Two things that
cost us an hour on 2026-08-22 and will cost you the same if you edit the query:

1. **`Event` has no flat `venue` / `city` / `state` / `country` fields.** They
   live under `location { venue city state country }`. Asking for them at the
   top level returns a bare **HTTP 400**, with no useful message. The script's
   `flatten()` turns them into `location.venue`, `location.city`, … columns.
2. **`region` is an enum (`RegionOption`), not a free string.** 97 values as of
   2026-08-22, and Texas is split four ways — `USTXHO`, `USTXCE`, `USTXNO`,
   `USTXSO`, plus `USTXWP`. `USTX` also exists. Others you may want: `USCHS`,
   `USNYLI`, `USNYNY`, `USNYEX`, `USCALA`, `USCALS`, `USCANO`, `USCASD`,
   `CAON`, `All`, `UnitedStates`, `International`.

Re-introspect either of those any time, no auth needed:

```bash
curl -s -X POST https://api.ftcscout.org/graphql -H 'Content-Type: application/json'   -d '{"query":"{__type(name:\"Event\"){fields{name}}}"}'
curl -s -X POST https://api.ftcscout.org/graphql -H 'Content-Type: application/json'   -d '{"query":"{__type(name:\"RegionOption\"){enumValues{name}}}"}'
```

**It is a volunteer-run service.** The official API is the source of truth. Use
FTCScout for OPR and for getting started without credentials; verify anything
that matters against FIRST.

**Do not scrape the website.** The HTML source of
`ftc-events.firstinspires.org` literally opens with
`<!-- PLEASE DO NOT SCRAPE WEBPAGES FOR EVENT DATA! We have an API… -->`.

---

## 3. Getting official credentials

1. Go to <https://ftc-events.firstinspires.org/services/API/register>.
   Takes about a minute. FIRST emails you a **username** and a UUID-looking
   **AuthorizationKey**.
2. Give them to the script in **one** of these ways:

   **(a) Environment variables — recommended**
   ```powershell
   # Windows PowerShell (this session only)
   $env:FTC_API_USER  = "yourusername"
   $env:FTC_API_TOKEN = "7eaa6338-a097-4221-ac04-b6120fcc4d49"
   ```
   ```bash
   # bash / zsh
   export FTC_API_USER=yourusername
   export FTC_API_TOKEN=7eaa6338-a097-4221-ac04-b6120fcc4d49
   ```

   **(b) A credentials file** named `.ftc-api-credentials` in this directory,
   your home directory, or a path passed with `--credentials`:
   ```
   user=yourusername
   token=7eaa6338-a097-4221-ac04-b6120fcc4d49
   ```

   **(c) `--user` / `--token` on the command line.** Works, but the token lands
   in your shell history. Least good option.

3. **Add `.ftc-api-credentials` to `.gitignore`.** This is not optional:

   > **[FACT — FTC-Events API docs]** *"Publicly distributing an application,
   > code snippet, etc, that has your username and token in it, encoded or not,
   > WILL result in your token being blocked from the API. Each user should
   > apply for their own token."*

   `fetch_events.py` never writes your token to disk, never puts it in an output
   file, and never echoes it — but a credentials file you commit is on you.

4. Verify: `python fetch_events.py check`

**If you skip all of this,** the script still works: every command supports
`--source scout`, and `dossier` uses FTCScout regardless. You lose the schedule,
alliance-selection and advancement endpoints, which FTCScout does not expose.

---

## 4. Season numbers

`{season}` is the **starting year**:

| Season | Number |
|---|---|
| BIOBUZZ 2026-27 | **2026** |
| DECODE 2025-26 | 2025 |
| INTO THE DEEP 2024-25 | 2024 |

The script defaults to the current season (year if the month is August or later,
otherwise year − 1). `check` prints the API's own `currentSeason` so you can
confirm.

**As of 2026-08-22 there is no BIOBUZZ event data yet.** Kickoff is
**12 September 2026**; the first events are months later. Practise the whole
pipeline on `--season 2025` now, so that in December you are running a tool you
already know rather than debugging one.

---

## 5. The score-breakdown warning

Score-detail columns are **season-specific**. The OpenAPI spec carries a
separate schema per season (`ScoreDetailModel_2019` … `ScoreDetailModel_2025`),
and BIOBUZZ will add a `_2026` with **column names that do not exist today**.

For scale, the DECODE (2025) breakdown from FTCScout has fields like
`autoLeavePoints`, `autoArtifactClassifiedPoints`, `dcPatternPoints`,
`movementRp`, `goalRp`, `penaltyPointsByOpp`, `totalPointsNp`. **None of those
names will necessarily survive into BIOBUZZ.**

`fetch_events.py` therefore **flattens score payloads generically** rather than
hardcoding field names, so it keeps working on Kickoff day with nobody editing
it. When you write analysis on top of it, do the same: read the actual column
headers out of the CSV at runtime.

---

## 6. The 45-minute-per-event pipeline

Full reasoning and the three sustainability tiers are in
`../../../research/SCOUTING-AND-AWARDS.md` §5. The short version for a team with
no scouting squad:

| When | Time | Do this |
|---|---|---|
| **T−3 days** | 10 min | `fetch_events.py dossier --season 2026 -e <CODE> -o dossier.csv` → run `../PROMPTS-scouting.md` SC2 → **print it on paper** |
| **T−1 day** | 10 min | Watch list: top 20% by season OPR, plus anyone who has won Inspire or Control this season |
| **Event morning** | ~25 min walking | Pit-scout cards, 90 s each. Priority: top-20% teams, then teams you play, then everyone else |
| **Quals 1–3** | passive | Watch. Fill only downtime / auto-conflict / driver columns. **Do no arithmetic yet** — OPR is not stable before round 3 |
| **Lunch** | ~10 min | Pull matches, compute OPR + component OPR + last-3 trend, merge the human columns, emit tiered lists (SC4 → SC5) |
| **Quals 4–5** | ~15 min | Re-run after each round. Spend the rest of the time **negotiating in the pits** (SC10) |
| **After** | 10 min | Pull final results, file the debrief (SC7) |

**Print everything.** Venue Wi-Fi fails. Plan for it rather than being surprised
by it.

---

## 7. What the script does and does not do

**Does:** fetch, page, retry with backoff, honour `If-Modified-Since` caching,
flatten nested JSON to dot-notation columns, expand match team arrays into
`Red1`/`Red2`/`Blue1`/`Blue2` columns (handling both APIs' different station
encodings), write Excel-friendly UTF-8 CSV, fail with a message that tells you
what to do next, and exit with a meaningful code (`0` ok, `1` usage, `2`
credentials, `3` HTTP, `4` no data).

**Does not:** compute OPR (see `SCOUTING-AND-AWARDS.md` §5.3a for a stdlib
Cholesky solver), rank teams, or build a pick list. Those are deliberate
omissions — see the fact/judgement box at the top of `../PROMPTS-scouting.md`.

---

## 8. If an endpoint stops working

The API constants are isolated at the top of `fetch_events.py` precisely so this
is a two-minute fix, not an archaeology project:

```python
API_BASE_FTC     = "https://ftc-api.firstinspires.org"
API_VERSION_FTC  = "v2.0"
ENDPOINTS_FTC    = { ... }          # one entry per path template
API_BASE_SCOUT   = "https://api.ftcscout.org/rest/v1"
ENDPOINTS_SCOUT  = { ... }
```

To re-verify against the source of truth:

```bash
python fetch_events.py check
python fetch_events.py endpoints
curl -s https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json | python -m json.tool > spec.json
```

Then diff the `paths` object in `spec.json` against `ENDPOINTS_FTC`.
`../PROMPTS-scouting.md` SC9 is the prompt for having Claude do the repair, with
the constraints (stdlib only, constants at the top, graceful failure) already
written into it.

---

## 9. Verification log

| Date | What was verified | How |
|---|---|---|
| 2026-08-22 | Every FTC-Events v2.0 path and parameter | Parsed `swagger/v2.0/swagger.json` (OpenAPI 3.0.1) programmatically |
| 2026-08-22 | Auth is HTTP Basic and mandatory | `components.securitySchemes.basic = {type: http, scheme: basic}`; unauthenticated call → HTTP 401 |
| 2026-08-22 | `currentSeason = 2026` | `GET /v2.0` → HTTP 200 |
| 2026-08-22 | All 7 FTCScout REST paths used here | Live requests, HTTP 200, shapes recorded |
| 2026-08-22 | FTCScout has **no** 2026-season events yet | `eventsSearch(season: 2026)` → `[]` |
| 2026-08-22 | `fetch_events.py` compiles and every subcommand runs | `python -m py_compile`, plus an offline harness driving all 11 subcommands against captured real payloads |
| 2026-08-22 (2nd pass) | **BUG FOUND AND FIXED** — `events --source scout` returned HTTP 400 | The GraphQL query asked for `venue city state country` as top-level `Event` fields. They are under `location {}`. Query rewritten; `--region` added |
| 2026-08-22 (2nd pass) | `events --source scout --season 2025 --region USTXHO --limit 8` | Live. 8 rows x 24 cols, e.g. `USTXHOCMP, Texas - Houston Championship, 2026-02-21, San Jacinto College` |
| 2026-08-22 (2nd pass) | `matches --source scout --season 2025 -e USTXHOCMP` | Live. **56 rows x 88 cols** — full DECODE score breakdown nested under `score.red.*` / `score.blue.*` |
| 2026-08-22 (2nd pass) | `teams` and `rankings`, same event | Live. **36 rows x 183 cols** each |
| 2026-08-22 (2nd pass) | `awards --source scout --season 2024 -e FTCCMP1` | Live. 18 rows x 9 cols, incl. `DeansListWinner` rows with `personName` |
| 2026-08-22 (2nd pass) | `dossier --season 2025 -e USTXHOCMP` | Live. **36 rows x 31 cols** — OPR bands + ranks + event W-L-T + blank human-observation columns. Took ~3 min (one quick-stats call per team, politely rate-limited) |
| 2026-08-22 (2nd pass) | Graceful failure on a bad event code | `matches -e USTXCMPENER` → *"eventCode looked well-formed, but no event matched that combination"*, exit 4. No traceback |
| 2026-08-22 (2nd pass) | Graceful failure with no credentials | `check` prints the full registration walkthrough and exits 2. Never echoes a token |
| 2026-08-22 (2nd pass) | **Gap closed** — the `teamevents` endpoint was declared but no subcommand reached it | Wired to `events --source scout --team <n>`. Live-tested: team 16321, season 2025 → 3 events (`FPEWE`, `FPEWESND`, `USCALACMP`) with per-event stats |
| 2026-08-22 (2nd pass) | Empty-but-valid responses are not treated as errors | `awards` for `USTXHOCMP` (2025 and 2024) genuinely returns `[]` from the API; the script says `[warn] no rows to write` rather than inventing rows |

**Re-verify at Kickoff (12 Sep 2026)** and again when the first BIOBUZZ events
post: the score-breakdown columns will be new, and the season number rolls.
