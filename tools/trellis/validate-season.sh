#!/usr/bin/env bash
# validate-season.sh: run Trellis's own validator against the BIOBUZZ season file.
#
#   bash tools/trellis/validate-season.sh          # analysis/kickoff/ if written, else the worksheet
#   bash tools/trellis/validate-season.sh path/to/2026-biobuzz.json
#   bash tools/trellis/validate-season.sh path/to/season.json /path/to/Trellis
#   TRELLIS_ROOT=/path/to/Trellis bash tools/trellis/validate-season.sh
#
# Step S9 of reference/SEASON-FILE-PROTOCOL.md. Run it on kickoff day the moment the file is
# written, so a file authored under time pressure fails at 12:30 rather than silently at an event.
#
# It calls the validator in place and copies nothing. The season file stays in this workspace and
# the Trellis checkout is not modified, which matters: config/season/ is what the app loads, and a
# half-written file left there is a live configuration rather than a draft.
#
# What the validator checks is the SHAPE. It does not check your reading of the manual. See
# reference/SEASON-FILE-PROTOCOL.md §3 for the two lists, and do not skip the read-it-on-a-phone
# step just because this printed ok.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# With no argument, prefer the file kickoff day writes and fall back to the pre-season worksheet.
# So the same command means "check today's file" on 12 September and "check the skeleton" today,
# and nobody has to remember a path while three people are waiting on the answer.
DEFAULT_SEASON="$ROOT/tools/trellis/2026-biobuzz.json"
if [ -f "$ROOT/analysis/kickoff/2026-biobuzz.json" ]; then
  DEFAULT_SEASON="$ROOT/analysis/kickoff/2026-biobuzz.json"
fi
SEASON="${1:-$DEFAULT_SEASON}"

# Made absolute before it goes anywhere. The validator runs with the Trellis checkout as its working
# directory, so a relative path typed here resolves against the wrong root and comes back as "No
# file at that path" for a file that is plainly sitting right there. The usage block above documents
# relative paths, so this is the common way to hit it, and kickoff day is the worst time to lose ten
# minutes to a path. Measured 2026-09-04: without this, `validate-season.sh _workfiles/x.json`
# failed while the firewall check in the same run read the same file without trouble.
case "$SEASON" in
  /* | [A-Za-z]:[/\]*) ;;
  *) SEASON="$(cd "$(dirname "$SEASON")" 2>/dev/null && pwd)/$(basename "$SEASON")" ;;
esac
# Where Trellis is checked out. Argument two wins, then TRELLIS_ROOT, then a sibling checkout
# beside this repository, which is what somebody who cloned both from github.com/XrxcGH gets.
# The default used to be one machine's absolute path, which is no use to anybody else and put a
# home directory into a public repository.
DEFAULT_TRELLIS="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." 2>/dev/null && pwd)/Trellis"
TRELLIS="${2:-${TRELLIS_ROOT:-$DEFAULT_TRELLIS}}"

say(){ printf '%s\n' "$*"; }
rule(){ printf '%s\n' "------------------------------------------------------------"; }

say ""; rule
say " BIOBUZZ season file: Trellis validation     $(date '+%Y-%m-%d %H:%M')"
rule
say " season file  : $SEASON"
say " trellis root : $TRELLIS"
say ""

# ---------------------------------------------------------------- guards
if [ ! -f "$SEASON" ]; then
  say "!! No season file at: $SEASON"
  say "   Pass the path as the first argument, or write the file first."
  exit 2
fi

if [ ! -f "$TRELLIS/tools/validate-config.ts" ]; then
  say "!! That does not look like a Trellis checkout: $TRELLIS"
  say "   tools/validate-config.ts is missing. Pass the checkout path as the second"
  say "   argument, or set TRELLIS_ROOT."
  exit 2
fi

if [ ! -d "$TRELLIS/node_modules" ]; then
  say "!! Trellis dependencies are not installed."
  say "   Run 'npm install' in $TRELLIS first. Do this BEFORE kickoff day:"
  say "   npm install on a venue network is not a five-minute problem."
  exit 2
fi

# ---------------------------------------------------------------- the check
say "Running Trellis's validator against the season schema..."
say ""
( cd "$TRELLIS" && npm run validate --silent -- --season "$SEASON" )
STATUS=$?
say ""

# --------------------------------------------------- the collision the validator cannot see
# pickSeason in src/lib/config/bundled.ts takes the highest `year` and breaks a tie by whichever
# the glob yields first. BIOBUZZ is year 2026 and so is FRC REBUILT, so two 2026 files in one
# config/season/ means one program silently loads the other program's game. The validator has no
# view of this: it checks one file at a time and a tie is not a schema error.
YEAR="$(grep -o '"year"[[:space:]]*:[[:space:]]*[0-9]\+' "$SEASON" | grep -o '[0-9]\+$' | head -1)"
if [ -n "${YEAR:-}" ] && [ -d "$TRELLIS/config/season" ]; then
  CLASH=""
  for f in "$TRELLIS"/config/season/*.json; do
    [ -e "$f" ] || continue
    case "$(basename "$f")" in example*) continue ;; esac
    OTHER="$(grep -o '"year"[[:space:]]*:[[:space:]]*[0-9]\+' "$f" | grep -o '[0-9]\+$' | head -1)"
    if [ "${OTHER:-}" = "$YEAR" ]; then CLASH="$CLASH  $(basename "$f")"; fi
  done
  # Whether THIS file names the program it belongs to. Trellis gained an optional `program` key on
  # the season schema, and chooseSeason now scores that claim ahead of the year: claims this program
  # scores 2, claims nothing scores 1, claims another program is ineligible. So a year clash is only
  # dangerous when the file is silent about which program it is for. Measured against the real
  # chooseSeason on 2026-09-04, both glob orders: with the key, ftc gets BIOBUZZ and frc gets
  # REBUILT; without it, BOTH programs got REBUILT.
  CLAIM="$(grep -o '"program"[[:space:]]*:[[:space:]]*"[^"]*"' "$SEASON" | head -1 | awk -F'"' '{print $4}')"
  if [ -n "$CLASH" ] && [ -z "${CLAIM:-}" ]; then
    rule
    say " FIREWALL WARNING: this file does not say which program it is for"
    rule
    say " That Trellis checkout already ships a season file for year $YEAR:"
    say "$CLASH"
    say ""
    say " This file has no \"program\" key, so chooseSeason cannot tell the two apart and falls"
    say " back to the year, which is a tie, and then to glob order. Measured on 2026-09-04:"
    say " with no claim BOTH programs loaded the FRC file, so the FTC install silently gets the"
    say " wrong game."
    say ""
    say " FIX: add  \"program\": \"ftc\"  next to gameName. One line, and the clash stops"
    say " mattering. reference/SEASON-FILE-PROTOCOL.md §0.2 and step S1."
    say ""
  elif [ -n "$CLASH" ]; then
    rule
    say " Year clash, and it is handled"
    rule
    say " That Trellis checkout also ships a season file for year $YEAR:"
    say "$CLASH"
    say ""
    say " This file claims program \"$CLAIM\", so chooseSeason picks it on a matching install and"
    say " refuses it outright on any other, whatever order the glob returns. The two files can"
    say " sit in one config/season/ directory. A separate FTC checkout is still fine and is no"
    say " longer required. reference/SEASON-FILE-PROTOCOL.md §0.2."
    say ""
    say " This says nothing about whether the file is FILLED IN. See the _notLoadable note in it."
    say ""
  fi
fi

# ---------------------------------------------------------------- report
rule
if [ "$STATUS" -eq 0 ]; then
  say " SHAPE OK. The validator has no complaints about this file."
  say ""
  say " It cannot see: a point value off the wrong row, a phase length copied from"
  say " DECODE, a counter whose points disagree with its scoring location, or an"
  say " option string using last season's noun. Next step is S9's second half:"
  say " open the scouting form on a phone-sized window and read every label."
else
  say " FAILED. Fix what is listed above and run this again."
  say " The message names the key. reference/SEASON-FILE-PROTOCOL.md maps each key"
  say " back to the manual section that fills it."
fi
rule
say ""
exit "$STATUS"
