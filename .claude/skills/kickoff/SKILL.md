---
name: kickoff
description: Run the complete BIOBUZZ kickoff-day game manual review end to end — ingest the new FTC Competition Manual, build the scoring model, rank design and scoring strategies by achievability for this two-robot program, assign target awards, hunt rule loopholes, generate bills of materials, and write the decision brief. Use when the user uploads or points at the 2026-27 FTC game manual, says the manual is out, says kickoff happened, or asks to run the game review. Also triggered by /kickoff.
---

# BIOBUZZ KICKOFF — full automatic review

The user has one job: get the manual to this machine. **Everything else is yours.** Do not ask
permission between phases. Do not ask which phase to run. Run the whole chain and report at the end.
Only stop early if a hard gate fails (§2) — in that case say exactly what broke and what to check.

Workspace root: `C:\Users\ericj\Documents\BIOBUZZ Analysis`

---

## 0. Standing rules for every phase

Apply these to everything you write in this run. They are not optional.

1. **CITE.** Every claim about the game carries a rule ID (`G414`) or table reference (`Table 10-2`).
   No citation means you are guessing — say so.
2. **LABEL.** Mark each statement `[MANUAL]` (the text says it), `[DERIVED]` (arithmetic — show the
   operands), or `[JUDGMENT]` (your opinion). Never blur them.
3. **NO PRIOR SEASONS.** This is BIOBUZZ. Any fact from DECODE / INTO THE DEEP / earlier is
   `[HISTORICAL]` and needs a note on why it might not hold. **A prior-season number presented as a
   BIOBUZZ number is the worst error available here.**
4. **SHOW ARITHMETIC.** Every points-per-second or cycle estimate shows its operands and states each
   time assumption. A bare number is rejected.
5. **UNVERIFIED, not invented.** If the manual doesn't say, write `UNVERIFIED` and add it to the Q&A
   list. Never fill a gap with plausible inference.
6. **Never read point values from `full_layout.txt`.** Flat text mis-pairs labels and numbers
   (measured on DECODE p.88). Use `bundle/TABLES.md`.
7. **Orange boxes are not binding.** They look identical to rule text once flattened. If a finding
   rests on one, say so.
8. **Rule IDs come from the parser, never from grepping flat text** — flat text mis-pairs IDs with
   bodies (this produced a real R304/R305 error in this workspace).

---

## 1. Ingest

Run:

```bash
bash tools/RUN-KICKOFF.sh
```

If the user gave you a path to the PDF (attached it, pasted a path, or named a file), pass it:
`bash tools/RUN-KICKOFF.sh "<path>"`.

The script locates the manual, refuses the pre-season V0, ingests everything, runs the gates, and
writes `analysis/kickoff/STATUS.md` plus `analysis/kickoff/bundle/`.

## 2. Gate check — the only place you may stop

Read `analysis/kickoff/STATUS.md`.

- **GREEN** → continue to §3 immediately, without asking.
- **RED** → stop. Report which gate failed and what it implies:
  - *unpaired ≠ 0* → FIRST changed the rule layout; the evergreen/game-specific split is untrustworthy.
    Read the PDF directly and see `reference/MANUAL-ANATOMY.md`.
  - *no tables* → do not build a scoring model from flat text. Try `tools/parse-html-manual.py` on the
    HTML edition instead.
  - *page count small* → wrong file.
  - *zero G-rules* → the script's guard exits **before** it writes `STATUS.md` (exit 3) and prints the
    reason to the terminal, so if there is no `STATUS.md` at all, read the script's output: it means the
    file was the pre-season V0 or an unrelated PDF.

## 3. The review — run all of these, in order

Write each output to `analysis/kickoff/`. Keep each file self-contained.

| # | Phase | Read | Write |
|---|---|---|---|
| R1 | Ingest sanity | `STATUS.md` | fold into R8 |
| R2 | Diff vs pre-season | `bundle/section_versions.txt`, `rules_ADDED/REMOVED.txt`, ingest `DIFF_vs_V0.patch` | `R2-changes.md` |
| R3 | **Scoring model** | `bundle/TABLES.md` | `R3-scoring-model.md` |
| R4 | ARENA & geometry | `bundle/figures/*.png` + Section 9 text | `R4-arena.md` |
| R5 | G-rules & penalties | `bundle/rules_full.tsv`, `VIOLATIONS.tsv` | `R5-rules.md` |
| R6 | Loophole hunt | `reference/LOOPHOLE-PLAYBOOK.md` + `bundle/TRIPWIRES.txt`, `ORANGE_BOXES.md`, `caps_NOVEL_ranked.txt` | `R6-loopholes.md` |
| R7 | Pitfall register | R1–R6 | `R7-pitfalls.md` |

**R3 is the critical path — do it first and get it right.** Everything downstream is arithmetic on it.
It must contain: the complete scoring table with citations; an explicit answer to *"is AUTO evaluated
live or at end of period, and are AUTO elements re-counted?"* (quote the text, or mark `UNVERIFIED` and
make it Q&A question #1 — this single sentence inverted AUTO strategy between ITD and DECODE); a
points-per-second estimate per action with operands shown; the AUTO/TELEOP/endgame budget; and the
ranking-point and tiebreaker conditions.

For R6, follow the playbook's seven passes and output its §7 table format. Apply the two-robot filter
and the ethics test in §5 before calling anything an opportunity.

## 3.5 The Trellis season file (PHASE S)

**Run this as soon as R3 and R4 are written, before §4.** It is transcription, not analysis, and it
takes about an hour. Everything it needs is already in `R3-scoring-model.md`, `D0-scoring-table.md`
and `R4-arena.md`.

Follow `reference/SEASON-FILE-PROTOCOL.md` steps S1 to S9. The worksheet is
`tools/trellis/2026-biobuzz.json`, already filled in as far as the pre-season V0 allowed and marked
unverified everywhere it could not be.

The output is one JSON file that makes the Trellis suite describe BIOBUZZ: the scouting form, the
picklist, the simulator, Cycle Economics and the printed brief all read it. Without it, Trellis is
configured for an FRC game the team is not playing.

Three things that bite if they are not read first:

- **S4 is the whole step.** `scoringLocations` is a row-for-row transcription of
  `D0-scoring-table.md`. An action paid for in AUTO and nowhere else gets an `auto` value and no
  other; a structure with levels gets one entry per level; per-what and caps go in a `_note`,
  because the schema has nowhere else for them.
- **FTC ranking columns arrive positionally.** There is no published header to copy. Claim
  `sortOrder: 3` only and leave positions 1 and 2 alone. Trellis prints a warning telling you to
  claim them; §5.1 of the protocol says why the warning is wrong and what obeying it breaks.
- **Do not delete the `field` block** if Section 9.2 gives you nothing. A missing field block makes
  the simulator fall back to the FRC carpet, measured at 16.46 by 8.23 m. An `[H]` number with a
  note is loud; an omission is silent and wrong.

Then run S9, which is one command and is not optional:

```bash
bash tools/trellis/validate-season.sh
```

It runs Trellis's own validator against the file, and checks that the file says which program it is
for. A file written under time pressure has to fail at 12:30, not silently at an event.

Two outcomes, and they are not the same. "Year clash, and it is handled" means the file carries
`"program": "ftc"`, so Trellis picks it on an FTC install and refuses it on an FRC one whatever the
glob returns; nothing to do. "FIREWALL WARNING: this file does not say which program it is for"
means the key was lost while editing, and the fix is to put it back next to `gameName`. Measured
2026-09-04: without that key, both programs loaded the FRC season file.

Report the file path and the validator's verdict in §8. If validation failed and you could not fix
it, say so plainly rather than reporting the file as done.

## 4. Strategy ranking — the part the user specifically wants

Follow `reference/STRATEGY-RANKING-PROTOCOL.md` steps D1–D8, scoring with
`reference/ACHIEVABILITY-RUBRIC.md`.

- **D1** Generate a MECE candidate slate — include the deliberately contrarian ones (ignore the
  headline objective, endgame-only, autonomous-only, defense). Not just the three obvious.
- **D2** Map each onto `reference/ROBOT-ARCHETYPE-LIBRARY.md`; flag genuinely novel shapes.
- **D3** Competitive Value (V) from the R3 model.
- **D4** Achievability (A) from the rubric — **scored twice, once for the A robot and once for the B
  robot.** Fill the rubric cell by cell with justifications; do not hand-wave a total.
- **D5** Plot A against V, assign quadrants, produce the **ranked list**.
- **D7** Stress-test the top two: what kills this, what a Team Update could do to it, the fallback, and
  the decision deadline for abandoning it.

Write `D5-ranked-strategies.md`.

**Calibration that must hold:** ~15 students, two registered teams, two robots, modest budget, hand
tools + 3D printing, no CNC. **Duplicability is a first-class factor** — every mechanism gets built
twice, and a design needing hand-tuning does not scale to a second robot.

## 5. Awards — ~2 per strategy

Using `reference/AWARD-ALIGNMENT-MATRIX.md` and `reference/AWARD-CATALOG-BIOBUZZ.md`, assign each
surviving strategy its **top 2 target awards** with the materials checklist, and split targets across
the A and B teams so they do not compete in the same judged category.

Remember the structural constraint: **only Innovate, Control and Design respond to what you build.**
Inspire (60 advancement points, vs 40 for winning the event) needs an MCI award *and* a Team Attributes
award *and* Think simultaneously — so the TA leg runs on a separate track.

Write `D6-awards.md`.

## 6. Bills of materials

For the top-ranked strategy (and the B-team recommendation if different), follow
`reference/BOM-PROTOCOL.md` steps B1–B5 using the six catalogs in `reference/mechanisms/`.

Decompose into major mechanisms; per mechanism give BUY vs FABRICATE, quantity per robot **and for
two**, and check every part against `reference/LEGAL-PARTS-CONSTRAINTS.md` with rule IDs — especially
the **R503 8-motor/8-servo budget**, which must be shown to fit.

Write `B-bom.md` and fill `tools/bom/BOM.template.csv` into `analysis/kickoff/BOM-A.csv` (and `-B` if
divergent).

**Do not state a SKU or price you have not loaded from the vendor page this session.** Tag every row
`VERIFIED` / `FAMILY-ONLY` / `UNVERIFIED`. A wrong part number costs real money and real weeks.

## 7. Q&A submissions

Collect every `UNVERIFIED` and every ambiguity from R6 into `Q-A-SUBMISSIONS.md`, each drafted as a
filable question: cite the rule, quote the ambiguous phrase, give both readings neutrally, and one
match scenario that distinguishes them. Under 150 words each. Do not argue for a preferred answer.

The Q&A opens **28 September 2026, 12:00 p.m. ET**, Lead Coach 1 or 2 account only.

## 8. The brief

Write `analysis/kickoff/BRIEF.md` — one page, for students who have read the manual once and a mentor
who has not:

- The game in five sentences
- Simplified scoring table with points-per-second alongside
- The ranked strategies, one line each
- **The recommendation, with its 2 target awards and its headline BOM cost for two robots**
- Top three pitfalls
- The Q&A questions being filed
- What must be decided this week vs what can wait

Then **report to the user in chat**: the recommendation, the ranking, the award targets, the top
loophole findings, the cost, the season file's path and validator verdict from §3.5, and anything
`UNVERIFIED` that matters. Link the files.

## 9. Afterwards

Tell the user that each Thursday Team Update should be re-run with:

```bash
bash tools/ingest-manual.sh <new-manual.pdf> TU<n>
```

then the `U1` prompt in `reference/REVIEW-PROMPTS.md` to diff it — and that the only question that
matters is whether the update invalidates the chosen strategy, the design, or a loophole finding.

---

## Reference map

**Method:** `ANALYSIS-PROTOCOL.md` (R0–R8) · `STRATEGY-RANKING-PROTOCOL.md` (D1–D8) ·
`LOOPHOLE-PLAYBOOK.md` · `BOM-PROTOCOL.md` · `SEASON-FILE-PROTOCOL.md` (S1–S9)
**Data:** `SCORING-PATTERNS.md` (21 seasons, 2005-06 through 2025-26) · `PENALTY-AND-ENFORCEMENT.md` · `ROBOT-ARCHETYPE-LIBRARY.md`
· `AWARD-CATALOG-BIOBUZZ.md` · `LEGAL-PARTS-CONSTRAINTS.md` · `mechanisms/*.md` · `KEYWORD-GLOSSARY.md`
**Context:** `research/LOOPHOLE-CASEBOOK.md` · `research/BIOBUZZ-PRESEASON.md` ·
`playbook/TWO-ROBOT-PROGRAM.md` · `research/TWO-TEAM-PROGRAM-RULES.md`

**Known before kickoff:** POLLEN was named in FIRST's Game Preview (2 May 2026). Its stated size,
**2.8 in ± 0.1 in yellow sphere, 0.055 lb**, comes from the **AndyMark product listing**, a vendor
page and not a FIRST primary source, so treat it as `UNVERIFIED` until the Kickoff manual confirms it
(`research/BIOBUZZ-PRESEASON.md` §6, where it carries `[C-web]`). Either way it is *not* the ~5 in
DECODE ball. **Sections 1 through 7, 12, 14 and 16 were already final in the pre-season V0**, and the
six placeholders are 8, 9, 10, 11, 13 and 15 (`research/BIOBUZZ-V0-STRUCTURE.md` §2). Section 14
League Play is the one most often miscounted as a placeholder; it is full text, verbatim from DECODE
§14. **R304** permits pre-Kickoff fabrication; **R503** caps 8 motors + 8 servos; **R801** allows only
manufacturer-sealed closed-air systems and bans generating pressure or vacuum; **R102** is an 18-inch
starting cube; **R104** sets no weight limit.

*Any output that reaches a team PORTFOLIO must carry the A201 AI credit.*
