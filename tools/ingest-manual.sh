#!/usr/bin/env bash
# ingest-manual.sh — Kickoff-day manual ingest + diff harness (FTC BIOBUZZ 2026-27)
# Usage:  bash tools/ingest-manual.sh <path-to-new-manual.pdf> [label]
# Example: bash tools/ingest-manual.sh ~/Downloads/BIOBUZZ-Manual-V1.pdf V1
#
# Rev 2 (2026-08-22) changes, all driven by measured failures of Rev 1:
#   * Rule inventory now uses reference/ftc_parse.py (font+colour+position) instead of a
#     regex. The old grep found 68/108 rules and produced 26 false "game-specific" hits,
#     because `pdftotext -layout` mis-pairs rule IDs with rule text, and because a regex
#     cannot tell rule "C270" from the Logitech C270 webcam named in R708.
#   * Evergreen/game-specific split now keys on the real marker: a GREEN #06844B headline
#     (evergreen) vs an ORANGE #ED7D31 headline (new/changed this game).
#   * Text extraction forced to UTF-8; the default Latin-1 turns "FIRST®" into mojibake.
#   * pdfinfo replaced with pymupdf — poppler's pdfinfo is not installed here.
#   * Rev 3 (2026-08-22): added steps 9-11 - geometric table extraction (pdftotext -layout
#     mangles the point-values table; measured on DECODE p.88), full rule bodies with the
#     orange boxes separated out, and page rendering for the ARENA figures.
#   * New: novel-ALL-CAPS detection against reference/known_caps_stoplist.txt, which
#     enumerates the new game nouns (scoring element, goals, zones) in one step.
#   * Rev 4 (2026-08-22): added step 12 - the HTML edition of the manual (.../game/cm-html)
#     parsed by class name via tools/parse-html-manual.py, plus a cross-pipeline gate. The
#     HTML carries Word's style names, so rule-id pairing, the orange-box split and the
#     scoring table come out exactly right. Validated: identical rule-id sets and identical
#     evergreen/season splits vs the PDF pipeline on both DECODE and ITD.
#     See reference/HTML-MANUAL-PARSING.md.  Pass HTML=<file> to override the search.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PDF="${1:?usage: ingest-manual.sh <manual.pdf> [label]}"
LABEL="${2:-V1}"
OUT="$ROOT/manuals/2026-27_BIOBUZZ"
WORK="$OUT/ingest_$LABEL"
V0PDF="$OUT/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf"
STOPLIST="$ROOT/reference/known_caps_stoplist.txt"

mkdir -p "$WORK/sections"
DEST="$OUT/BIOBUZZ_Competition_Manual_${LABEL}.pdf"
# Tolerate re-ingesting a PDF that already lives at the destination path (cp errors on
# same-file), so the harness can be re-run idempotently.
if [ "$(cd "$(dirname "$PDF")" && pwd)/$(basename "$PDF")" != "$DEST" ]; then
  cp -f "$PDF" "$DEST"
fi
PDF="$DEST"

echo "== 1. Extracting text =="
pdftotext -enc UTF-8 -layout "$PDF" "$WORK/full_layout.txt"
pdftotext -enc UTF-8         "$PDF" "$WORK/full_raw.txt"
# Regenerate the V0 baseline the SAME way so the step-4 diff compares like with like; the
# checked-in BIOBUZZ_V0_layout.txt was extracted as Latin-1 and carries mojibake.
# manuals/ is not published with the repository, so a fresh clone has no V0 PDF. The ingest
# still runs without it; only the V0 comparisons (rules_v0, ADDED/REMOVED, step 4) are skipped.
BASE="$WORK/baseline_layout.txt"
HAVE_V0=0
if [ -f "$V0PDF" ]; then
  HAVE_V0=1
  pdftotext -enc UTF-8 -layout "$V0PDF" "$BASE"
else
  echo "   !! WARNING: no V0 baseline at ${V0PDF#$ROOT/}"
  echo "   !! Download the pre-season V0 Competition Manual from FIRST and save it at that path"
  echo "   !! to get the V0 comparisons. Skipping rules_v0, rules_ADDED/REMOVED and the step-4 diff."
fi
PAGES=$(python -c "import pymupdf,sys; print(pymupdf.open(sys.argv[1]).page_count)" "$PDF" 2>/dev/null || echo "?")
echo "   pages=$PAGES  lines=$(wc -l < "$WORK/full_layout.txt")"

echo "== 2. Rule inventory (validated PDF parser, not regex) =="
python "$ROOT/reference/ftc_parse.py" "$PDF"   --tsv "$WORK/rules_new.tsv" >"$WORK/parse_new.log" 2>&1 || true
sed 's/^/   /' "$WORK/parse_new.log"
sed -n '2,$p' "$WORK/rules_new.tsv" | cut -f1 | sort -u > "$WORK/rules_new.txt"
if [ "$HAVE_V0" -eq 1 ]; then
  python "$ROOT/reference/ftc_parse.py" "$V0PDF" --tsv "$WORK/rules_v0.tsv"  >"$WORK/parse_v0.log"  2>&1 || true
  sed -n '2,$p' "$WORK/rules_v0.tsv"  | cut -f1 | sort -u > "$WORK/rules_v0.txt"
  comm -13 "$WORK/rules_v0.txt" "$WORK/rules_new.txt" > "$WORK/rules_ADDED.txt"
  comm -23 "$WORK/rules_v0.txt" "$WORK/rules_new.txt" > "$WORK/rules_REMOVED.txt"
  echo "   V0=$(wc -l < "$WORK/rules_v0.txt")  NEW=$(wc -l < "$WORK/rules_new.txt")"
  echo "   ADDED=$(wc -l < "$WORK/rules_ADDED.txt")  REMOVED=$(wc -l < "$WORK/rules_REMOVED.txt")"
else
  echo "   NEW=$(wc -l < "$WORK/rules_new.txt")  (no V0 baseline: ADDED/REMOVED not computed)"
fi
echo "   --- G-rules (the new game rules) ---"
{ grep -E "^G" "$WORK/rules_new.txt" || echo "(none - game rules section not present)"; } \
  | tr '\n' ' ' | fold -w 100 -s | sed 's/^/   /'
echo

UNPAIRED=$(awk -F'\t' 'NR>1 && $3=="UNPAIRED"' "$WORK/rules_new.tsv" | wc -l)
if [ "${UNPAIRED:-0}" -gt 0 ]; then
  echo
  echo "   !! WARNING: $UNPAIRED rule ids could not be paired with a headline."
  echo "   !! FIRST CHANGED THE RULE LAYOUT. Do not trust the evergreen split below."
  echo "   !! Inspect the PDF and read reference/MANUAL-ANATOMY.md before proceeding."
fi

echo "== 3. Evergreen vs game-specific split =="
# Evergreen = GREEN #06844B headline (carries over year to year -> low review priority)
# Gamespec  = ORANGE #ED7D31 headline (new/changed for this game -> HIGHEST review priority)
awk -F'\t' 'NR>1 && $3=="EVERGREEN" {print $1"  "$4}' "$WORK/rules_new.tsv" > "$WORK/rules_EVERGREEN.txt"
awk -F'\t' 'NR>1 && $3=="GAMESPEC"  {print $1"  "$4}' "$WORK/rules_new.tsv" > "$WORK/rules_GAMESPECIFIC.txt"
awk -F'\t' 'NR>1 && $3=="UNPAIRED"  {print $1}'       "$WORK/rules_new.tsv" > "$WORK/rules_UNPAIRED.txt"
echo "   evergreen=$(wc -l < "$WORK/rules_EVERGREEN.txt")  game-specific=$(wc -l < "$WORK/rules_GAMESPECIFIC.txt")  unpaired=$(wc -l < "$WORK/rules_UNPAIRED.txt")"
echo "   --- READ THESE FIRST (game-specific) ---"
cut -c1-96 "$WORK/rules_GAMESPECIFIC.txt" | sed 's/^/   /' | head -40

echo "== 4. Text diff vs V0 (carried-over sections) =="
if [ "$HAVE_V0" -eq 1 ]; then
  diff -u "$BASE" "$WORK/full_layout.txt" > "$WORK/DIFF_vs_V0.patch" 2>/dev/null || true
  echo "   diff lines: $(wc -l < "$WORK/DIFF_vs_V0.patch")"
else
  echo "   skipped: no V0 baseline (see step 1)"
fi

echo "== 5. Glossary terms + NOVEL game nouns =="
# NOTE: the flat text extraction mis-pairs glossary TERM with DEFINITION (they live in a
# two-column table). Use this list only as a term index; for real definitions read the
# reconstructed glossary in reference/KEYWORD-GLOSSARY.md, or parse the PDF by geometry.
awk '/^16 +Glossary/,0' "$WORK/full_layout.txt" \
  | grep -oE '^[A-Z][A-Z '"'"'-]{2,30}$' | sed 's/[[:space:]]*$//' | sort -u > "$WORK/glossary_terms.txt" || true
# Multi-word phrase frequency, for context when reading the new vocabulary.
grep -oE '\b[A-Z]{3,}([[:space:]][A-Z]{2,})*\b' "$WORK/full_layout.txt" \
  | sort | uniq -c | sort -rn > "$WORK/allcaps_frequency.txt"
# FTC sets every defined term in ALL CAPS, so an ALL-CAPS token NOT already known from V0 /
# DECODE / ITD is almost certainly a NEW GAME NOUN: the scoring element, a goal, a zone.
# The stoplist is SINGLE-TOKEN by construction, so tokenise the same way it was built
# (see reference/KEYWORD-GLOSSARY.md §0) — matching phrases against it silently matches
# nothing and reports every known term as novel.
if [ -f "$STOPLIST" ]; then
  grep -oE "[A-Z]{3,}('S)?" "$WORK/full_layout.txt" | sort -u > "$WORK/allcaps_terms.txt"
  grep -vxF -f "$STOPLIST" "$WORK/allcaps_terms.txt" > "$WORK/caps_NOVEL.txt" || true
  grep -oE "[A-Z]{3,}('S)?" "$WORK/full_layout.txt" | grep -vxF -f "$STOPLIST" \
    | sort | uniq -c | sort -rn > "$WORK/caps_NOVEL_ranked.txt" || true
  echo "   glossary terms: $(wc -l < "$WORK/glossary_terms.txt")   NOVEL all-caps: $(wc -l < "$WORK/caps_NOVEL.txt")"
  echo "   --- NEW GAME VOCABULARY, most frequent first (these name the game) ---"
  head -30 "$WORK/caps_NOVEL_ranked.txt" | awk '{printf "%s(%s) ", $2, $1}' | fold -w 100 -s | sed 's/^/   /'
  echo
else
  echo "   glossary terms: $(wc -l < "$WORK/glossary_terms.txt")  (stoplist missing; skipped novelty check)"
fi

echo "== 6. Scoring / numeric harvest =="
grep -inE '[0-9]+[[:space:]]*(point|pt)s?\b' "$WORK/full_layout.txt" > "$WORK/scoring_mentions.txt" || true
grep -inE 'MINOR FOUL|MAJOR FOUL|YELLOW CARD|RED CARD|DISQUALIF|VERBAL WARNING' "$WORK/full_layout.txt" > "$WORK/penalty_mentions.txt" || true
grep -inE '[0-9]+[[:space:]]*(second|minute)s?\b' "$WORK/full_layout.txt" > "$WORK/timing_mentions.txt" || true
echo "   scoring=$(wc -l < "$WORK/scoring_mentions.txt")  penalty=$(wc -l < "$WORK/penalty_mentions.txt")  timing=$(wc -l < "$WORK/timing_mentions.txt")"

echo "== 7. Section splits =="
grep -nE '^[0-9]{1,2}(\.[0-9]+)*[[:space:]]+[A-Z]' "$WORK/full_layout.txt" | head -80 > "$WORK/section_map.txt"
echo "   section headings captured: $(wc -l < "$WORK/section_map.txt")"
# Per-section version stamps: FIRST versions each section independently, so a changed
# section announces itself here. Anything not V0 changed since the pre-season release.
grep -oE '^Section [0-9]+ .*  V[0-9]+' "$WORK/full_layout.txt" | sed 's/  */ /g' | sort -u > "$WORK/section_versions.txt" || true
echo "   --- per-section version stamps (non-V0 = changed since pre-season) ---"
sed 's/^/   /' "$WORK/section_versions.txt" | head -20

echo "== 8. Loophole tripwires =="
{
  echo "### Hedge / vagueness words (ambiguity = loophole surface)"
  grep -inE '\b(generally|typically|usually|intended|attempt|reasonabl|egregious|excessive|repeated|momentar|inadvertent|deliberate|strateg|sole purpose|at the discretion)\w*' "$WORK/full_layout.txt" || true
  echo
  echo "### Counting words (per-MATCH vs per-instance ambiguity)"
  grep -inE '\b(per MATCH|each MATCH|at a time|simultaneous|at any (given )?time|more than|no more than|at most|up to|maximum of|limit of)\b' "$WORK/full_layout.txt" || true
  echo
  echo "### Timers / thresholds"
  grep -inE '\b(within|after|before|for more than|continuous|cumulative)\b.*[0-9]+[[:space:]]*(second|minute)' "$WORK/full_layout.txt" || true
  echo
  echo "### Exceptions and carve-outs"
  grep -inE '\b(unless|except|other than|does not apply|is exempt|notwithstanding|provided that)\b' "$WORK/full_layout.txt" || true
  echo
  echo "### Scored-live vs scored-at-end (decides whether AUTO work compounds)"
  grep -inE '(at the end of|end of the (MATCH|AUTO|period)|continuously|at the conclusion|when the (MATCH|period) ends)' "$WORK/full_layout.txt" || true
} > "$WORK/TRIPWIRES.txt"
echo "   tripwire hits: $(wc -l < "$WORK/TRIPWIRES.txt")"

echo "== 9. Tables by geometry (the scoring table is NOT readable in the flat text) =="
# MEASURED, not theoretical: on DECODE TU32 p.88, `pdftotext -layout` put the row labels and
# the point values of Table 10-2 on different lines -- "Fully returned to BASE" lost its 10,
# and 5/10/10 floated free at the bottom of the block. Anything built on that text is wrong.
# pymupdf's table finder recovers the same table correctly.
python "$ROOT/tools/extract-tables.py" "$PDF" --out "$WORK/tables" >"$WORK/tables.log" 2>&1 || true
sed 's/^/   /' "$WORK/tables.log" | grep -v "pymupdf_layout" || true
if [ -f "$WORK/tables/INDEX.txt" ]; then
  echo "   --- tables that carry numbers you will build a strategy on ---"
  grep -inE 'point value|scoring|ranking|threshold|RP |motor|servo' "$WORK/tables/INDEX.txt" \
    | head -12 | sed 's/^/   /' || true
fi

echo "== 10. Full rule bodies + orange boxes (loophole-hunting input) =="
# ftc_parse.py gives the rule INVENTORY. This gives the complete body of each rule, its
# Violation: line, and -- separately -- the non-binding orange-box commentary, which is
# typographically invisible in flat text and is otherwise quoted as if it were binding.
python "$ROOT/tools/rule-bodies.py" "$PDF" --out "$WORK/rulebodies" --min-words 8 \
  >"$WORK/rulebodies.log" 2>&1 || true
sed 's/^/   /' "$WORK/rulebodies.log" || true
if [ -f "$WORK/rulebodies/rules_full.tsv" ]; then
  awk -F'\t' 'NR>1 && $1 ~ /^G/ {print}' "$WORK/rulebodies/rules_full.tsv" \
    > "$WORK/rulebodies/G_rules_full.tsv" || true
  echo "   G-rule bodies: $(wc -l < "$WORK/rulebodies/G_rules_full.tsv") rules"
fi

echo "== 11. Rendering the pages text cannot carry (ARENA figures + scoring table) =="
# Figures do not survive text extraction at all. Upload these images alongside the text.
python "$ROOT/tools/render-pages.py" "$PDF" --sections 8,9,10 --dpi 130 \
  --out "$WORK/figures" >"$WORK/figures.log" 2>&1 \
  && grep -E "^==" "$WORK/figures.log" | sed 's/^/   /' \
  || { echo "   ! render failed or sections 8/9/10 not in the outline; see figures.log"; \
       echo "   ! fall back to: python tools/render-pages.py \"$PDF\" --pages <range>"; }

echo "== 12. HTML edition (the second, independent pipeline) =="
# FIRST publishes the SAME manual as a Word-filtered HTML export at .../game/cm-html, and
# that export carries Word's paragraph STYLE NAMES in class= attributes: RuleNumber-Game,
# Headline-Evergreen, Headline-SeasonSpecific, Violation, OrangeBox. That removes the four
# hardest problems in the PDF path (rule-id pairing, orange boxes, evergreen split, tables).
# Measured on DECODE + ITD: the two pipelines return IDENTICAL rule-id sets and IDENTICAL
# evergreen/season classifications. See reference/HTML-MANUAL-PARSING.md.
# It does NOT carry footers (no per-section version stamps) or figures - keep using the PDF.
HTML_IN="${HTML:-}"
if [ -z "$HTML_IN" ]; then
  # default: the file kickoff-fetch.sh saves next to the manual
  for cand in "$OUT/kickoff/BIOBUZZ_Manual_KICKOFF.html" "${PDF%.pdf}.html"; do
    [ -f "$cand" ] && HTML_IN="$cand" && break
  done
fi
if [ -n "$HTML_IN" ] && [ -f "$HTML_IN" ]; then
  python "$ROOT/tools/parse-html-manual.py" "$HTML_IN" --out "$WORK/html" >"$WORK/html.log" 2>&1 || true
  sed 's/^/   /' "$WORK/html.log" | head -20
  # GATE: the two pipelines must agree on the rule-id set. A diff is not a tie-break.
  if [ -f "$WORK/html/rules_html.tsv" ] && [ -s "$WORK/rules_new.txt" ]; then
    sed -n '2,$p' "$WORK/html/rules_html.tsv" | cut -f1 | sort -u > "$WORK/html/ids_html.txt"
    if diff -q "$WORK/rules_new.txt" "$WORK/html/ids_html.txt" >/dev/null 2>&1; then
      echo "   [ok ] PDF and HTML pipelines agree on all $(wc -l < "$WORK/rules_new.txt") rule ids"
    else
      echo "   !! WARNING: PDF and HTML rule-id sets DIFFER. Do not proceed on either until"
      echo "   !! you know why. Diff:"
      diff "$WORK/rules_new.txt" "$WORK/html/ids_html.txt" | head -20 | sed 's/^/   !! /'
    fi
  fi
else
  echo "   (no HTML edition found - fetch .../game/cm-html, or pass HTML=<file>. Optional,"
  echo "    but it is the cleanest source for the scoring table and the orange-box split.)"
fi

echo
echo "=========================================================="
echo " INGEST COMPLETE -> $WORK"
echo "=========================================================="
echo " Key files to hand to Claude:"
echo "   html/tables_html.md     ** THE SCORING TABLE, cleanest source ** (if the HTML was found)"
echo "   html/rules_full_html.md every rule + Violation + orange boxes tagged NON-BINDING"
echo "   tables/TABLES.md        ** THE SCORING TABLE ** - use this, never the flat text"
echo "   figures/*.png           ARENA + Game Details pages as images (upload with the text)"
echo "   rulebodies/rules_full.md   complete text of every rule, orange boxes separated"
echo "   rulebodies/VIOLATIONS.tsv  every penalty sentence, by rule id"
echo "   full_layout.txt         full manual text (UTF-8)"
echo "   rules_GAMESPECIFIC.txt  ** START HERE ** orange-headline rules = new/changed this game"
echo "   rules_ADDED.txt         every NEW rule id vs V0"
echo "   rules_EVERGREEN.txt     rules that carry over (low review priority)"
echo "   rules_UNPAIRED.txt      if non-empty the parser broke — layout changed, verify by hand"
echo "   caps_NOVEL.txt          NEW ALL-CAPS game vocabulary (names the scoring elements/zones)"
echo "   section_versions.txt    per-section version stamps; non-V0 = changed"
echo "   DIFF_vs_V0.patch        exactly what FIRST changed in carried-over text"
echo "   TRIPWIRES.txt           ambiguity/loophole candidate lines"
echo "   scoring_mentions.txt / penalty_mentions.txt / timing_mentions.txt"
echo
echo " Next: open reference/ANALYSIS-PROTOCOL.md and run phases R0-R8."
echo "       Copy-paste prompts: reference/REVIEW-PROMPTS-STRATEGY.md"
