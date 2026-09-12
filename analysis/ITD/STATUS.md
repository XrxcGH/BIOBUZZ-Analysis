# KICKOFF INGEST STATUS

**Run:** 2026-08-23 20:32
**Manual:** `Competition Manual - V14.pdf`
**Pages:** 146  ·  **Rules:** 209  ·  **G-rules:** 53  ·  **Game-specific (orange):** 16

## Gates
| Gate | Result |
|---|---|
| Rule IDs all paired | PASS |
| Page count plausible | PASS (146) |
| Scoring tables recovered | PASS |
| Figures rendered | PASS (28) |

**Overall: GREEN — proceed to analysis**

## New game vocabulary (most frequent first)
SUBMERSIBLE SAMPLES OBSERVATION ASCENT SAMPLE SPECIMEN NET SPECIMENS CHAMBERS DEEP RUNGS CLIP 

## Where things are
| What | Path |
|---|---|
| Upload bundle (feed Claude in this order) | `analysis/ITD/bundle/` |
| Full ingest output | `manuals/2026-27_BIOBUZZ/ingest_ITD/` |
| Ingest log | `analysis/ITD/ingest.log` |

The bundle is generated on this machine by tools/RUN-KICKOFF.sh and is not published with the repository, because it is FIRST's manual text. To rebuild it, run bash tools/RUN-KICKOFF.sh with the manual PDF.

## Feed order
1. `bundle/TABLES.md` — the scoring table. **Never read point values from flat text**
2. `bundle/rules_GAMESPECIFIC.txt` — the orange rules; read these first
3. `bundle/rules_full.tsv` — full rule bodies + Violation lines
4. `bundle/figures/*.png` — ARENA geometry
5. `bundle/TRIPWIRES.txt` — loophole candidates (phase R6 only)
6. `bundle/full_layout.txt` — last resort
