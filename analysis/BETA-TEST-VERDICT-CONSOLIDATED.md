# BETA TEST VERDICT — consolidated

### Two blind runs of the kickoff harness: DECODE (2025-26) and INTO THE DEEP (2024-25). Written 2026-08-23.

**What was tested.** Each manual was fed through `tools/RUN-KICKOFF.sh` and analysed **blind** — agents
worked only from the ingest bundle and the game-agnostic method files, and were forbidden from reading
this workspace's own analysis of those seasons (`SCORING-PATTERNS.md`, `LOOPHOLE-CASEBOOK.md`, the
archetype library, the raw prior-season corpus). Then the answer key was opened and the output scored.

**Why two seasons.** DECODE is 188 pp / 214 rules / 17 orange. INTO THE DEEP is 146 pp / 209 rules / 16
orange. If a component only worked on one, it is season-shaped and will mislead on BIOBUZZ.

**Status.** The INTO THE DEEP chain completed end to end (`analysis/ITD/BETA-TEST-VERDICT-ITD.md`, 541
lines). The DECODE chain completed its Review phase (R3/R5/R6) and then lost its Decide phase and verdict
agent to repeated **HTTP 529 Overloaded** — a server-side outage, not a harness failure. The DECODE
accuracy scoring below was therefore done by hand against the answer key.

---

## 1. THE HEADLINE NUMBERS

### 1.1 DECODE — scoring model, scored by hand

Blind `analysis/kickoff/R3-scoring-model.md` vs `reference/SCORING-PATTERNS.md` §A.11.

| Item | Answer key | Blind run | ✓ |
|---|---|---|:--:|
| LEAVE (AUTO) | 3 / robot | 3 per ROBOT | ✓ |
| ARTIFACT — CLASSIFIED | 3 / 3 | 3 / 3 | ✓ |
| ARTIFACT — OVERFLOW | 1 / 1 | 1 / 1 | ✓ |
| ARTIFACT — DEPOT | — / 1 | — / 1 | ✓ |
| PATTERN matches MOTIF | 2 / 2 | 2 / 2 | ✓ |
| BASE — partial | — / 5 | — / 5 | ✓ |
| BASE — full | — / 10 | — / 10 | ✓ |
| BASE — both-robots bonus | — / 10 | — / 10, per ALLIANCE, once | ✓ |
| MOVEMENT / GOAL / PATTERN RP | 1 each | 1 each | ✓ |
| WIN / TIE | 3 / 1 | 3 / 1 | ✓ |
| MOVEMENT RP thresholds | 21 / 21 / 16 | 21 / 21 / 16 | ✓ |
| GOAL RP thresholds | 67 / 42 / 36 | 67 / 42 / 36 | ✓ |
| PATTERN RP thresholds | 22 / 22 / 18 | 22 / 22 / 18 | ✓ |
| Match structure | 30 s + 8 s + 2:00, no End Game period, 0:20 whistle | identical, plus `grep -c -i endgame → 0` as evidence | ✓ |

**26 / 26 point-value and threshold cells correct. Zero errors.**

### 1.2 INTO THE DEEP — scored by its own verdict agent

**36 / 41 = 87.8% strict** (26 / 30 = 86.7% blind-certified after discounting leaked items).

| Category | Score |
|---|---|
| Table 10-3 point values (18 cells) | **18 / 18** |
| Ranking-point conditions | **5 / 5** |
| Tiebreakers | **5 / 5** |
| Structural facts | **8 / 13** |

### 1.3 What that means

Across two seasons the harness reproduced **44 of 44 point values, thresholds and ranking conditions**
without error. The scoring table — the artifact every downstream decision is arithmetic on — is
**reliable**. Everything the harness got wrong was *structural*, not numeric.

---

## 2. THE BEST RESULT: IT DERIVED THE HARDEST FACT IN DECODE WITHOUT THE ANSWER

The answer key's own words: *"Live vs end-of-period scoring is the whole game."* Establishing it required
**two official Q&A rulings**:

- **Q27** — CLASSIFIED/OVERFLOW are assessed as the artifact passes the SQUARE and are *not* recounted, so
  AUTO artifacts do **not** double.
- **Q129** — an ARTIFACT is eligible for PATTERN points at the end of AUTO **and/or** end of TELEOP, so
  PATTERN **does** double.

The blind run reached both conclusions **from the manual alone, with no Q&A access**:

> ARTIFACT scoring is live and counted once (§10.5.A), but PATTERN is assessed **twice** — end of AUTO and
> end of MATCH (§10.5.B/C) — so a matching AUTO shot pays 3+2+2 = 7. Never stated in words; `[DERIVED]`
> because the 22-point PATTERN RP threshold **exceeds the 18-point single-assessment ceiling**.

It found a contradiction between a ranking threshold and a scoring ceiling, and reasoned backwards to the
only structure that resolves it. Then it filed the question as Q&A #1 and wrote down what to recompute if
the answer came back no.

Two further marks of rigour: the realistic alliance score was computed **124 bottom-up and 124 top-down**
from the RP thresholds — independent methods agreeing. And R6 found that **LAUNCH and CONTROL are defined
with identical wording**, making herding literally LAUNCHING, saved only by a *non-binding orange box*.

**This is the behaviour that justifies the harness.** It is not transcription.

---

## 3. THE WORST RESULTS

### 3.1 Contamination — the harness leaks its own answers *(P0, confirmed independently by both runs)*

The method files an analyst is *told to read* contain the answers:

| File | What it leaks |
|---|---|
| `STRATEGY-RANKING-PROTOCOL.md` §4 X1, §6.3.1 | ITD's defining insight **verbatim**, plus five point values and the clock |
| `ACHIEVABILITY-RUBRIC.md` §8, §11–13 | the worked D5 answer, with scores and quadrants |
| `ACHIEVABILITY-FACTORS.md` §8.1 | same calibration |
| `ANALYSIS-PROTOCOL.md` §3.3–3.4 | DECODE AprilTags and duration thresholds; routes through the forbidden `SCORING-PATTERNS.md` **five times**, including in a mandatory done-criterion |
| `LOOPHOLE-PLAYBOOK.md` §2 Pass 5, §3 | the Q27/Q129 rulings and G422's pin count |

Consequence: ITD's "defining insight" find was **uncreditable** — the answer was pre-printed in an allowed
file. Excellent teaching material; poison in the analyst's context. On BIOBUZZ nothing is leaked because
no analysis exists yet — but the *protocol steps that dereference those files* will dead-end, and six of
them do.

### 3.2 Both runs missed the randomized objective — the one systematic blind spot

- **DECODE:** the OBELISK AprilTag (IDs 21/22/23) selecting a GPP/PGP/PPG MOTIF — **absent** from R3.
- **INTO THE DEEP:** the randomisation question **not asked at all**; cost the run one accuracy item.

Two for two. This is the clearest actionable defect in the whole exercise, and it matters disproportionately
because FIRST has paid **double** for a team-supplied vision marker in three consecutive seasons.
**Fix: make the randomisation questions a non-skippable step in R3, not a bullet in an appendix.**

### 3.3 A gate reported PASS while the data was missing

**ITD's `TABLES.md` was missing Table 10-2 entirely** — with a glossary block sitting under its heading —
while the ingest gate said PASS. R3 recovered it only from a rendered figure. Silent, and it looks like
success. **Fix: verify every `Table N-x` referenced in Section 9/10 prose has a matching heading, on the
right page.**

### 3.4 The judgment layer is BIOBUZZ-shaped and wrong elsewhere

| Item | Baked-in | True in ITD |
|---|---|---|
| Rubric gate **G2** | 8 motors / 8 servos | 8 motors / **12 servos** |
| Rubric gate **G6** | presumes gas springs permitted | **R207 bans them** — premise inverted |
| Mechanism catalogs | **119 `CONFIRMED-BIOBUZZ` legality labels** | unverified against any other manual |

`EXTENSION-ARMS-LIFTS.md`'s flagship idea rests on an actuator **banned** in that season. **Fix: gates name
the *constraint*, never the number; emit `R_LIMITS.txt` at ingest and feed the gates from it.**

### 3.5 Compounding pessimism, then trusting it over the instrument

ITD's R3 applied a ×0.7 speed factor **and** a ×1.3 cycle multiplier — **1.86× compounded** — producing a
top rate **2.6× below reality**. D5 then saw scores fall below the rubric's bands and **re-anchored the
rubric instead of suspecting its input.** Its own verdict calls this the worst behaviour in the run.

**Fix, as a standing rule:** *if the model's top rate lands below the rubric's rating-4 band, suspect the
model before re-anchoring the instrument.*

### 3.6 Bundle gaps that forced guesswork

- **No glossary file.** §16 is a two-column table that collapses under `pdftotext`; both runs did Pass 1 by hand.
- **No geometry file.** DECODE's field was measured **off PNGs by eye** — and every points-per-second figure
  divides by that.
- **Rule bodies overrun.** `G434` and `C501` each swallowed the entire glossary; Violation strings truncate
  mid-sentence (`G402`, `G419`).
- **§10.5's assessment list exists only in `full_layout.txt`** — the file the house rules say not to trust,
  yet it holds the single highest-leverage fact in the game.
- **Figures render only pp. 58–94**, omitting Figures 11-2/11-3/11-4 and 12-1/12-2 that govern five findings.
- `ORANGE_BOXES.md` mislabels twelve §9–§10 boxes as "after A215"; three different manual filenames appear
  inside one bundle.

---

## 4. WHAT GENERALIZED, AND WHAT DID NOT

| Component | Verdict |
|---|---|
| Rule parser (`ftc_parse.py`) on 2024-25+ | **Works.** 0 unpaired on both, 214 and 209 rules |
| Rule parser on 2017-18 → 2023-24 | **Fails silently — `rules=0` on all seven seasons.** Needs `tools/parse-legacy-manual.py` |
| Geometric table extractor | **Works, but can silently omit a table** (§3.3) |
| Figure renderer | Works; **page range too narrow** |
| ALL-CAPS novelty detector | **Works on both.** Reconstructed each game cold. Caveat: the convention only began in 2024-25, so it cannot work pre-2024 |
| Tripwires, gates, arithmetic, two-run rubric | **Ran clean on both** |
| Rubric gates and anchors | **Partially failed** — season numbers hard-coded |
| Mechanism catalogs | **Failed a checkable legality fact** |
| Archetype layer | **Untested** — both sources were forbidden files |

ITD's verdict summarises it exactly: **"plumbing yes, judgment layer no."**

---

## 5. THE VERDICT

**Would this review have been good enough to commit a season to? For the scoring model, yes — 44/44 with a
derived insight the answer key needed two Q&A rulings to establish. For the strategy decision, not yet:**
the rubric's gates carry the wrong season's numbers, its calibration sits in the analyst's read path, and a
compounding-pessimism bug moved a top candidate's rate 2.6×.

All of it is fixable, and none of it is architectural. The mechanical pipeline — locate, guard, ingest,
gate, bundle — worked on two structurally different manuals without modification, and the guard correctly
refused the pre-season V0 when pointed at it.

**Blocking fixes before 2026-09-12** (full 25-item list in `analysis/ITD/BETA-TEST-VERDICT-ITD.md` §5):

1. Move every worked calibration to `reference/CALIBRATION.md`, outside the kickoff read path.
2. Replace all ITD/DECODE examples in the protocols with a **synthetic** game.
3. Inline the method that six protocol steps currently fetch from forbidden files.
4. Make randomisation questions non-skippable in R3.
5. Gates name the constraint, not the number; emit `R_LIMITS.txt` and feed them from it.
6. Add the cycle-model sanity check and the suspect-the-model rule.
7. Add the `Table N-x` cross-check gate.
8. Emit `GLOSSARY.tsv`, `GEOMETRY`/`SETUP_AND_ELEMENTS.txt`, `SCORING_TIMING.txt`, `PENALTY_LADDER.tsv`;
   fix rule-body overrun and Violation truncation; widen the figure range.

---

*Sources: `analysis/ITD/BETA-TEST-VERDICT-ITD.md` (agent-written, 541 lines) · `analysis/kickoff/R3-scoring-model.md`,
`R5-rules.md`, `R6-loopholes.md` (blind DECODE outputs) · `reference/SCORING-PATTERNS.md` §A.11 (answer key).
DECODE accuracy scored by hand after its verdict agent was lost to an API outage. Produced with AI
assistance; per BIOBUZZ A201 anything reaching a PORTFOLIO carries the credit.*
