#!/usr/bin/env bash
# kickoff-fetch.sh -- BIOBUZZ kickoff-day bulk download.  Run after the 2026-09-12 broadcast.
#
# WHY THIS FILE EXISTS
#   research/SOURCES.md section 9.3 said "save as tools/kickoff-fetch.sh" but the file was never
#   created, so on kickoff morning you would be copy-pasting a script out of a markdown document
#   under time pressure. This is that script, made real and hardened:
#     * every slug that 404s is REPORTED and retried, never silently skipped
#     * every downloaded PDF gets a page count and a size, so the V0 placeholder (93 pp, 1.7 MB)
#       cannot be mistaken for the real manual
#     * a MANIFEST.txt is written so R0's done-criterion is satisfiable without extra work
#     * --retry re-runs only the misses from the previous run
#
# USAGE
#   bash tools/kickoff-fetch.sh              # full run
#   bash tools/kickoff-fetch.sh --retry      # only the slugs that missed last time
#   bash tools/kickoff-fetch.sh --tier 0     # tier 0 only (the manual and TU00)
#   YEAR=2028 bash tools/kickoff-fetch.sh    # next season; FIRST's archive path is the END year
#
# NOTE ON SLUGS
#   The full slug vocabulary and the reasoning behind these URLs is in research/SOURCES.md
#   sections 9.1-9.2. Two are known to move between seasons:
#     * DECODE's event/travel-letter is event/transport-letter in 2027
#     * the game-element CAD slug is NAMED AFTER THE ELEMENT (DECODE: field/artifact-cad-step).
#       BIOBUZZ's element is POLLEN, so field/pollen-cad-step is a GUESS. Both are tried; if
#       both miss, open the live field page and read the real link. Do not invent one.
set -uo pipefail

YEAR="${YEAR:-2027}"
BASE="https://ftc-resources.firstinspires.org/ftc/archive/${YEAR}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/manuals/2026-27_BIOBUZZ/kickoff"
MISSES="$OUT/_misses.txt"
MANIFEST="$OUT/MANIFEST.txt"
RETRY=0
TIER="all"

while [ $# -gt 0 ]; do
  case "$1" in
    --retry) RETRY=1 ;;
    --tier)  shift; TIER="${1:-all}" ;;
    -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
    *) echo "unknown option: $1"; exit 2 ;;
  esac
  shift
done

mkdir -p "$OUT"
PREV_MISSES=""
if [ "$RETRY" = "1" ] && [ -f "$MISSES" ]; then
  PREV_MISSES="$(cat "$MISSES")"
  echo "== retry mode: only re-fetching $(wc -l < "$MISSES") slug(s) that missed last run"
fi
: > "$MISSES.new"

pagecount() {  # pagecount <pdf> -> page count, or "?" if pymupdf cannot read it
  python -c "import pymupdf,sys; print(pymupdf.open(sys.argv[1]).page_count)" "$1" 2>/dev/null || echo "?"
}

fetch() {  # fetch <category/slug> <output-name> [note]
  local slug="$1" name="$2" note="${3:-}"
  if [ "$RETRY" = "1" ] && ! printf '%s\n' "$PREV_MISSES" | grep -qxF "$slug"; then
    return 0
  fi
  local code
  code=$(curl -sL --max-time 180 -w '%{http_code}' -o "$OUT/$name" "$BASE/$slug" 2>/dev/null || echo 000)
  if [ "$code" = "200" ] && [ -s "$OUT/$name" ]; then
    local sz pp extra=""
    sz=$(stat -c%s "$OUT/$name" 2>/dev/null || echo 0)
    case "$name" in
      *.pdf) pp=$(pagecount "$OUT/$name"); extra=" ${pp}pp" ;;
    esac
    printf '  OK    %-34s -> %-42s %8s bytes%s %s\n' "$slug" "$name" "$sz" "$extra" "$note"
    printf 'OK\t%s\t%s\t%s\t%s\n' "$slug" "$name" "$sz" "${pp:-}" >> "$MANIFEST.new"
  else
    printf '  MISS  %-34s (HTTP %s) %s\n' "$slug" "$code" "$note"
    rm -f "$OUT/$name"
    echo "$slug" >> "$MISSES.new"
    printf 'MISS\t%s\t%s\t\t\n' "$slug" "$name" >> "$MANIFEST.new"
  fi
}

: > "$MANIFEST.new"
echo "== BIOBUZZ kickoff fetch  base=$BASE  out=$OUT"
echo

if [ "$TIER" = "all" ] || [ "$TIER" = "0" ]; then
echo "== Tier 0: the manual, the game sections, Team Update 00 =="
fetch game/manual      BIOBUZZ_Manual_KICKOFF.pdf  "<- THE ONE THAT MATTERS"
fetch game/cm-html     BIOBUZZ_Manual_KICKOFF.html "<- best for diffing"
for n in 08 09 10 11; do fetch "game/manual-$n" "BIOBUZZ_Section_$n.pdf" "<- game sections"; done
fetch game/tu-00       BIOBUZZ_TeamUpdate00.pdf    "<- read BEFORE the manual"
fetch game/tu-combined BIOBUZZ_TeamUpdates_Combined.pdf
for n in 13 14 15; do fetch "game/manual-$n" "BIOBUZZ_Section_$n.pdf"; done
for n in 01 02 03 04 05 06 07 12 16; do fetch "game/manual-$n" "BIOBUZZ_Section_$n.pdf"; done
fi

if [ "$TIER" = "all" ] || [ "$TIER" = "1" ]; then
echo
echo "== Tier 1: field, inspection, judging =="
fetch field/field-cad-step         BIOBUZZ_FieldCAD_STEP.zip
fetch field/pollen-cad-step        BIOBUZZ_ElementCAD_STEP.zip  "<- slug is a GUESS"
fetch field/artifact-cad-step      BIOBUZZ_ElementCAD_alt.zip   "<- fallback slug"
fetch field/initialfieldguide      BIOBUZZ_InitialFieldAssembly.pdf
fetch field/eventfieldguide        BIOBUZZ_EventFieldSetup.pdf
fetch field/field-check            BIOBUZZ_FieldAcceptanceChecklist.pdf
fetch field/field-mitigation-guide BIOBUZZ_FieldMitigation.pdf
fetch field/apriltag-us            BIOBUZZ_AprilTags_USLetter.pdf
fetch field/apriltag-art           BIOBUZZ_AprilTag_ProductionArt.pdf
fetch event/inspection-check       BIOBUZZ_InspectionChecklist.pdf
fetch event/inspection-reference   BIOBUZZ_InspectionQuickRef.pdf
fetch event/question-bank          BIOBUZZ_JudgingQuestionBank.pdf
fetch event/award-summary          BIOBUZZ_JudgeSummarySheets.pdf
fetch event/interview-feedback     BIOBUZZ_InterviewFeedback.pdf
fetch event/judging-guide          BIOBUZZ_JudgingProcessGuide.pdf
fi

if [ "$TIER" = "all" ] || [ "$TIER" = "2" ]; then
echo
echo "== Tier 2: tournament, league, advancement, StarterBots =="
fetch event/tournament-guide       BIOBUZZ_TournamentGuide.pdf
fetch event/league                 BIOBUZZ_LeagueGuide.pdf
fetch event/advancement            BIOBUZZ_AutomatedAdvancement.pdf
fetch event/season-dates           BIOBUZZ_SeasonDates.pdf
fetch volunteer/annotated-checklist BIOBUZZ_AnnotatedInspection.pptx
fetch team/am-starterbot           BIOBUZZ_StarterBot_AndyMark.pdf
fetch team/gobilda-starterbot      BIOBUZZ_StarterBot_goBILDA.pdf
fetch team/rev-starterbot          BIOBUZZ_StarterBot_REV.pdf
fetch team/studica-starterbot      BIOBUZZ_StarterBot_Studica.pdf
fi

mv -f "$MANIFEST.new" "$MANIFEST"
mv -f "$MISSES.new" "$MISSES"

echo
echo "=========================================================="
MAN="$OUT/BIOBUZZ_Manual_KICKOFF.pdf"
if [ -f "$MAN" ]; then
  PP=$(pagecount "$MAN"); SZ=$(stat -c%s "$MAN")
  echo " Competition Manual: ${PP} pages, ${SZ} bytes"
  # The pre-season V0 placeholder is 93 pp / 1,704,884 bytes. Prior KICKOFF releases were
  # 161 pp (DECODE) and 142 pp (ITD). A short file means the CDN is still serving V0.
  if [ "$PP" != "?" ] && [ "$PP" -lt 120 ] 2>/dev/null; then
    echo " !! WARNING: only ${PP} pages. That looks like the V0 PRE-SEASON placeholder,"
    echo " !! not the Kickoff manual. Wait and re-run:  bash tools/kickoff-fetch.sh --retry"
  fi
else
  echo " !! The Competition Manual did not download. Re-run in a few minutes:"
  echo " !!   bash tools/kickoff-fetch.sh --retry"
fi
NMISS=$(wc -l < "$MISSES" 2>/dev/null || echo 0)
echo " Misses: $NMISS  (list: $MISSES)"
echo " Manifest: $MANIFEST"
echo "=========================================================="
echo " Next:  bash tools/ingest-manual.sh \"$MAN\" V1"
echo "        then reference/ANALYSIS-PROTOCOL.md phase R1."
