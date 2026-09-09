# KICKOFF INGEST STATUS

**Run:** 2026-08-23 20:27
**Manual:** `/c/Users/ericj/Downloads/DECODE_Competition_Manual_TU32.pdf`
**Pages:** 188  ·  **Rules:** 214  ·  **G-rules:** 53  ·  **Game-specific (orange):** 17

## Gates
| Gate | Result |
|---|---|
| Rule IDs all paired | PASS |
| Page count plausible | PASS (188) |
| Scoring tables recovered | PASS |
| Figures rendered | PASS (37) |

**Overall: GREEN — proceed to analysis**

## New game vocabulary (most frequent first)
ARTIFACTS ARTIFACT GATE GOAL RAMP BASE LAUNCH PATTERN DECODE OBELISK LOADING SQUARE 

## Where things are
| What | Path |
|---|---|
| Upload bundle (feed Claude in this order) | `analysis/kickoff/bundle/` |
| Full ingest output | `manuals/2026-27_BIOBUZZ/ingest_KICKOFF/` |
| Ingest log | `analysis/kickoff/ingest.log` |

## Feed order
1. `bundle/TABLES.md` — the scoring table. **Never read point values from flat text**
2. `bundle/rules_GAMESPECIFIC.txt` — the orange rules; read these first
3. `bundle/rules_full.tsv` — full rule bodies + Violation lines
4. `bundle/figures/*.png` — ARENA geometry
5. `bundle/TRIPWIRES.txt` — loophole candidates (phase R6 only)
6. `bundle/full_layout.txt` — last resort
