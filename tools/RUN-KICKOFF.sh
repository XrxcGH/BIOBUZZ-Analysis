#!/usr/bin/env bash
# RUN-KICKOFF.sh — ONE COMMAND. Everything mechanical, kickoff day.
#
#   bash tools/RUN-KICKOFF.sh                       # find the manual automatically
#   bash tools/RUN-KICKOFF.sh /path/to/manual.pdf   # or point at it
#   bash tools/RUN-KICKOFF.sh manual.pdf TU03       # a later release, kept side by side
#
# What it does, in order:
#   1. LOCATE  the kickoff manual (argument → kickoff/ → Downloads → download it)
#   2. GUARD   refuse to proceed on the pre-season V0 (zero G-rules = wrong file)
#   3. INGEST  text, rules, tables, rule bodies, figures, tripwires, novel vocabulary
#   4. GATE    four hard checks; any red is reported loudly, not swallowed
#   5. BUNDLE  assemble analysis/kickoff/ with the exact files to feed Claude, in order
#   6. REPORT  write STATUS.md and print the single next step
#
# Everything after this is the .claude/skills/kickoff skill, which reads STATUS.md and runs
# the analysis phases itself. You should not need to paste prompts by hand.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
LABEL="${2:-KICKOFF}"
OUT="$ROOT/manuals/2026-27_BIOBUZZ"
WORK="$OUT/ingest_$LABEL"
if [ "$LABEL" = "KICKOFF" ]; then AN="$ROOT/analysis/kickoff"; else AN="$ROOT/analysis/$LABEL"; fi
V0PDF="$OUT/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf"
mkdir -p "$AN"

say(){ printf '%s\n' "$*"; }
rule(){ printf '%s\n' "------------------------------------------------------------"; }

say ""; rule
say " BIOBUZZ KICKOFF — automatic run     $(date '+%Y-%m-%d %H:%M')"
rule

# ---------------------------------------------------------------- 1. LOCATE
PDF="${1:-}"
if [ -n "$PDF" ] && [ ! -f "$PDF" ]; then
  say "!! Path given but not found: $PDF"; exit 2
fi

if [ -z "$PDF" ]; then
  say "== 1. Locating the manual"
  # a) anything the fetch script already pulled
  for c in "$OUT/kickoff/BIOBUZZ_Manual_KICKOFF.pdf"; do
    [ -f "$c" ] && PDF="$c" && say "   found from kickoff-fetch: $c" && break
  done
  # b) newest plausible PDF in the usual download spots
  if [ -z "$PDF" ]; then
    for d in "$HOME/Downloads" "$HOME/Desktop" "/c/Users/$USER/Downloads"; do
      [ -d "$d" ] || continue
      cand=$(find "$d" -maxdepth 1 -iname '*.pdf' \
             \( -iname '*biobuzz*' -o -iname '*competition*manual*' -o -iname '*game*manual*' \) \
             -newermt '2026-09-01' -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
      if [ -n "${cand:-}" ]; then PDF="$cand"; say "   found in $d: $(basename "$cand")"; break; fi
    done
  fi
  # c) go get it
  if [ -z "$PDF" ]; then
    say "   nothing local — running tools/kickoff-fetch.sh"
    bash "$ROOT/tools/kickoff-fetch.sh" >"$AN/fetch.log" 2>&1 || true
    [ -f "$OUT/kickoff/BIOBUZZ_Manual_KICKOFF.pdf" ] && PDF="$OUT/kickoff/BIOBUZZ_Manual_KICKOFF.pdf"
    say "   fetch log: ${AN#$ROOT/}/fetch.log"
  fi
fi

if [ -z "${PDF:-}" ] || [ ! -f "$PDF" ]; then
  say ""
  say "!! Could not find the manual."
  say "!! Download it from firstinspires.org and re-run:"
  say "!!     bash tools/RUN-KICKOFF.sh ~/Downloads/<the-file>.pdf"
  exit 2
fi
say "   using: $PDF"

# ---------------------------------------------------------------- 2. GUARD
say ""
say "== 2. Verifying this is the KICKOFF manual, not the pre-season V0"
PARSE="$AN/_guard.txt"
python "$ROOT/reference/ftc_parse.py" "$PDF" --tsv "$AN/_guard.tsv" >"$PARSE" 2>&1 || true
GRULES=$(awk -F'\t' 'NR>1 && $1 ~ /^G/' "$AN/_guard.tsv" 2>/dev/null | wc -l | tr -d ' ')
NRULES=$(awk -F'\t' 'NR>1' "$AN/_guard.tsv" 2>/dev/null | wc -l | tr -d ' ')
say "   rules found: ${NRULES:-0}   G-rules: ${GRULES:-0}"

# Two very different causes of "no G-rules", and conflating them would mislead on kickoff day:
#   NRULES == 0  -> the parser did not understand this document AT ALL. Either a pre-2024 manual
#                   (those use <G10>-style tags and need tools/parse-legacy-manual.py) or FIRST
#                   changed the 2026-27 layout, which is a genuine emergency worth knowing instantly.
#   NRULES  > 0  -> the parser worked fine and the document really has no game rules: the pre-season
#                   V0, or a Part-1-style/non-game document.
if [ "${NRULES:-0}" -eq 0 ]; then
  say ""
  say "!! STOP — the parser found NO RULES AT ALL in this document."
  say "!! This is NOT the 'wrong file' case. It means the layout was not recognised. Either:"
  say "!!   (a) this is a pre-2024 manual (rule IDs look like <G10>) -> use:"
  say "!!         python tools/parse-legacy-manual.py \"$PDF\""
  say "!!   (b) FIRST changed the 2026-27 rule layout -> the harness needs updating TODAY."
  say "!!       Read the PDF by hand and see reference/MANUAL-ANATOMY.md section 13."
  say "!! Nothing was changed."
  exit 4
fi

if [ "${GRULES:-0}" -eq 0 ]; then
  say ""
  say "!! STOP — parsed $NRULES rules cleanly, but ZERO of them are G-rules."
  say "!! The parser works, so this really is a document with no game rules in it:"
  say "!! the PRE-SEASON V0 (109 rules, 0 G-rules), or a non-game document."
  say "!! The real kickoff manual has ~50 G-rules. See manuals/2026-27_BIOBUZZ/kickoff/README-DRY-RUN.txt"
  say "!! Nothing was changed. Point me at the right file:"
  say "!!     bash tools/RUN-KICKOFF.sh <correct.pdf>"
  exit 3
fi
say "   OK — G-rules present, this is the real thing."

# ---------------------------------------------------------------- 3. INGEST
say ""
say "== 3. Ingesting (text, rules, tables, rule bodies, figures, tripwires)"
bash "$ROOT/tools/ingest-manual.sh" "$PDF" "$LABEL" >"$AN/ingest.log" 2>&1
IRC=$?
tail -3 "$AN/ingest.log" | sed 's/^/   /'
if [ $IRC -ne 0 ]; then
  say "   !! ingest returned $IRC — see ${AN#$ROOT/}/ingest.log (continuing to gates)"
fi

# ---------------------------------------------------------------- 4. GATES
say ""
say "== 4. Gates"
g(){ printf '   [%s] %s\n' "$1" "$2"; }
GATES_OK=1
UNP=$(wc -l < "$WORK/rules_UNPAIRED.txt" 2>/dev/null | tr -d ' '); UNP=${UNP:-999}
PAGES=$(python -c "import pymupdf,sys;print(pymupdf.open(sys.argv[1]).page_count)" "$PDF" 2>/dev/null || echo 0)
NTAB=$(ls "$WORK/tables"/*.md 2>/dev/null | wc -l | tr -d ' ')
NFIG=$(ls "$WORK/figures"/*.png 2>/dev/null | wc -l | tr -d ' ')

if [ "$UNP" -eq 0 ]; then g OK "parser paired every rule id (unpaired=0)"
else g "!!" "UNPAIRED=$UNP — FIRST changed the rule layout. Verify by hand before trusting the split."; GATES_OK=0; fi

if [ "$PAGES" -gt 100 ]; then g OK "page count $PAGES (kickoff manuals are larger than V0's 93)"
else g "!!" "page count $PAGES looks small for a kickoff manual"; GATES_OK=0; fi

if [ "$NTAB" -gt 0 ]; then g OK "scoring tables recovered by geometry ($NTAB file(s))"
else g "!!" "no tables extracted — do NOT read point values from the flat text"; GATES_OK=0; fi

if [ "$NFIG" -gt 0 ]; then g OK "$NFIG ARENA/Game-Details page images rendered"
else g "!!" "no figures rendered — zone geometry will be guesswork"; fi

# ---------------------------------------------------------------- 5. BUNDLE
say ""
say "== 5. Assembling the upload bundle"
B="$AN/bundle"; rm -rf "$B"; mkdir -p "$B"
cp_if(){ [ -e "$1" ] && cp -r "$1" "$B/" 2>/dev/null && printf '   + %s\n' "$(basename "$1")"; }
cp_if "$WORK/tables/TABLES.md"
cp_if "$WORK/rules_GAMESPECIFIC.txt"
cp_if "$WORK/rulebodies/rules_full.tsv"
cp_if "$WORK/rulebodies/VIOLATIONS.tsv"
cp_if "$WORK/rulebodies/ORANGE_BOXES.md"
cp_if "$WORK/caps_NOVEL_ranked.txt"
cp_if "$WORK/rules_ADDED.txt"
cp_if "$WORK/rules_REMOVED.txt"
cp_if "$WORK/section_versions.txt"
cp_if "$WORK/TRIPWIRES.txt"
cp_if "$WORK/figures"
[ -f "$WORK/full_layout.txt" ] && cp "$WORK/full_layout.txt" "$B/" && printf '   + full_layout.txt (last resort only)\n'

# ---------------------------------------------------------------- 6. REPORT
NEW_G=$(grep -c '^G' "$WORK/rules_new.txt" 2>/dev/null || echo 0)
NGS=$(wc -l < "$WORK/rules_GAMESPECIFIC.txt" 2>/dev/null | tr -d ' ')
NOVEL=$(head -12 "$WORK/caps_NOVEL_ranked.txt" 2>/dev/null | awk '{printf "%s ", $2}')

cat > "$AN/STATUS.md" <<EOF
# KICKOFF INGEST STATUS

**Run:** $(date '+%Y-%m-%d %H:%M')
**Manual:** \`$PDF\`
**Pages:** $PAGES  ·  **Rules:** $NRULES  ·  **G-rules:** $NEW_G  ·  **Game-specific (orange):** $NGS

## Gates
| Gate | Result |
|---|---|
| Rule IDs all paired | $( [ "$UNP" -eq 0 ] && echo "PASS" || echo "**FAIL — unpaired=$UNP**" ) |
| Page count plausible | $( [ "$PAGES" -gt 100 ] && echo "PASS ($PAGES)" || echo "**FAIL ($PAGES)**" ) |
| Scoring tables recovered | $( [ "$NTAB" -gt 0 ] && echo "PASS" || echo "**FAIL**" ) |
| Figures rendered | $( [ "$NFIG" -gt 0 ] && echo "PASS ($NFIG)" || echo "WARN (0)" ) |

**Overall: $( [ $GATES_OK -eq 1 ] && echo "GREEN — proceed to analysis" || echo "RED — read the failing gate before trusting anything downstream" )**

## New game vocabulary (most frequent first)
$NOVEL

## Where things are
| What | Path |
|---|---|
| Upload bundle (feed Claude in this order) | \`${AN#$ROOT/}/bundle/\` |
| Full ingest output | \`manuals/2026-27_BIOBUZZ/ingest_$LABEL/\` |
| Ingest log | \`${AN#$ROOT/}/ingest.log\` |

## Feed order
1. \`bundle/TABLES.md\` — the scoring table. **Never read point values from flat text**
2. \`bundle/rules_GAMESPECIFIC.txt\` — the orange rules; read these first
3. \`bundle/rules_full.tsv\` — full rule bodies + Violation lines
4. \`bundle/figures/*.png\` — ARENA geometry
5. \`bundle/TRIPWIRES.txt\` — loophole candidates (phase R6 only)
6. \`bundle/full_layout.txt\` — last resort
EOF

rm -f "$AN/_guard.txt" "$AN/_guard.tsv"

say ""; rule
say " DONE — gates: $( [ $GATES_OK -eq 1 ] && echo GREEN || echo RED )"
rule
say " Pages $PAGES · Rules $NRULES · G-rules $NEW_G · game-specific $NGS"
say " New vocabulary: $NOVEL"
say ""
say " Status:  ${AN#$ROOT/}/STATUS.md"
say " Bundle:  ${AN#$ROOT/}/bundle/"
say ""
say " NEXT — say this to Claude:      /kickoff"
say " (or just: \"the manual is in, run the review\")"
rule
exit 0
