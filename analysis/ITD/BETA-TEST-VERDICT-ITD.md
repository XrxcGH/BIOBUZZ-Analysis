# BETA TEST VERDICT — INTO THE DEEP (harness run #2)

**Run under test:** 2026-08-23, `analysis/ITD/` — V14 INTO THE DEEP Competition Manual (146 pp, 209 rules,
53 G-rules, 16 orange) fed to the kickoff harness as an unseen game.
**Verdict written:** 2026-08-23. **Answer key opened:** only after reading all four blind outputs in full.
**Purpose:** decide whether this harness can be trusted on BIOBUZZ on 2026-09-12.

**Files read for this verdict**
`analysis/ITD/R3-scoring-model.md` · `analysis/ITD/R5-R6-rules-loopholes.md` · `analysis/ITD/D5-ranked-strategies.md` ·
`analysis/ITD/STATUS.md` · every `## Beta feedback` section (24 numbered items across three files) ·
**answer key:** `reference/SCORING-PATTERNS.md` §A.10, §B.1–B.12, §C.2–C.3 ·
**re-verified against the bundle:** `bundle/TABLES.md`, `bundle/rules_full.tsv`, `bundle/TRIPWIRES.txt`,
`bundle/caps_NOVEL_ranked.txt`, `bundle/full_layout.txt` (geometry prose only) ·
**method files audited for contamination:** `reference/ANALYSIS-PROTOCOL.md`, `reference/STRATEGY-RANKING-PROTOCOL.md`,
`reference/LOOPHOLE-PLAYBOOK.md`, `reference/ACHIEVABILITY-RUBRIC.md`, `reference/ACHIEVABILITY-FACTORS.md`,
`reference/mechanisms/*.md`, `reference/known_caps_stoplist.txt`.

**Bundle availability:** `tools/RUN-KICKOFF.sh` generated the bundle locally from the V14 manual; it is not published
with this repository, because it is FIRST's manual text. Line numbers this verdict cites in bundle files refer to that generated
copy; page and table numbers refer to the manual itself.

> **Headline.** The transcription is near-perfect and the strategic conclusion is right. **Neither result is
> admissible evidence**, because an *allowed* method file reprints this season's point values and its defining
> insight. Underneath that, three substantive things went wrong that would have gone wrong on BIOBUZZ too:
> the harness never asked whether the game had a randomised objective, its cycle model was ~2.6× pessimistic
> and cascaded into every value rating, and one mechanism catalogue recommended an illegal actuator.

---

## 1. ACCURACY SCORE

### 1.1 Table 10-3 point values — 18 cells

Answer key: `SCORING-PATTERNS.md` §A.10 (extracted from p.66 of the source PDF).
Harness: `R3-scoring-model.md` §1.2. Independently re-verified against `bundle/TABLES.md` line 162–177.

| Scoring item | Key AUTO | Key TELEOP | Harness AUTO | Harness TELEOP | Match? |
|---|---:|---:|---:|---:|:--:|
| PARK — OBSERVATION ZONE | 3 | 3 | 3 | 3 | ✅ |
| SAMPLE — NET ZONE | 2 | 2 | 2 | 2 | ✅ |
| SAMPLE — LOW BASKET | 4 | 4 | 4 | 4 | ✅ |
| SAMPLE — HIGH BASKET | 8 | 8 | 8 | 8 | ✅ |
| SPECIMEN — LOW CHAMBER | 6 | 6 | 6 | 6 | ✅ |
| SPECIMEN — HIGH CHAMBER | 10 | 10 | 10 | 10 | ✅ |
| ASCENT LEVEL 1 | 3 | 3 | 3 | 3 | ✅ |
| ASCENT LEVEL 2 | — (blank) | 15 | — (blank) | 15 | ✅ |
| ASCENT LEVEL 3 | — (blank) | 30 | — (blank) | 30 | ✅ |

**Point-value hit rate: 18 / 18 = 1.000.**

Two things deserve credit beyond the raw score, because both are the kind of error this harness exists to catch:

- The harness **flagged the two blank AUTO cells as load-bearing** and derived "there is no AUTO climb in this
  game" from them, rather than silently reading 15/15 and 30/30. The key confirms the blanks.
- **Table 10-2 (ASCENT LEVEL criteria) is missing from `bundle/TABLES.md`** — verified: the only `Table 10-2`
  heading in that file is at line 710, `## p.143 - Table 10-2`, and it is the **glossary**, a false positive
  produced by the phrase *"as defined in Table 10-2"* inside a glossary cell (line 724). In `full_layout.txt`
  the real table is scrambled **off by one** — line 2273 reads `LEVEL 2 · ROBOT is in contact with the LOW
  RUNG`, which is LEVEL 1's definition. The harness detected the scramble, went to
  `figures/p065_s10-game-details.png`, and recovered LEVEL 1/2/3 correctly (contact LOW RUNG / fully supported
  by RUNGS / on HIGH RUNG and above the LOW RUNG top). **That matches the key exactly.** This is the single
  best behaviour in the whole run and the reason the "never take point values from flat text" house rule must
  survive to BIOBUZZ.

### 1.2 Ranking-point conditions — 5 items

| Condition | Answer key | Harness | Match? |
|---|---|---|:--:|
| Win | 2 RP | 2 RP | ✅ |
| Tie | 1 RP | 1 RP | ✅ |
| Loss | (no row) | 0 RP `[DERIVED]` — "the table lists no loss row" | ✅ |
| RANKING SCORE | RS = average RP | RS = average RP across qualification MATCHES, excluding SURROGATES (§13.5.3) | ✅ |
| Bonus / threshold RPs | none this season | "**There are no RP thresholds, no bonus RP, and no per-tier RP variation… RP-farming is not a strategy this season**" | ✅ |

**RP hit rate: 5 / 5 = 1.000.** The harness also drew the correct downstream inference the key does not state —
that with RP ∈ {0,1,2} a 10-point win ranks identically to a 200-point win, so sorts 2 and 3 decide most seeding.

### 1.3 Tiebreakers — Table 13-1, 5 sorts

| Sort | Answer key | Harness | Match? |
|---:|---|---|:--:|
| 1st | RANKING SCORE (RS) | RANKING SCORE (RS) | ✅ |
| 2nd | Average ALLIANCE AUTO Points | Average ALLIANCE AUTO Points | ✅ |
| 3rd | Average TELEOP ALLIANCE ASCENT Points | Average TELEOP ALLIANCE ASCENT Points | ✅ |
| 4th | Highest MATCH Score (including FOULS) | Highest MATCH Score (including FOULS) | ✅ |
| 5th | Random sort by FIRST event management software | Random sort by FIRST event management software | ✅ |

**Tiebreaker hit rate: 5 / 5 = 1.000.** The harness additionally noticed that sort 3 counts **ASCENT only, not
PARK**, and used it to rescue ASCENT LEVEL 1 ("3 = 3 in MATCH points, but 3 > 0 on the ranking ladder"). The key
does not record that inference. It is correct and it is original to this run.

### 1.4 Everything else the key records — 13 structural items

| # | Item | Answer key value | Harness value | Match? |
|---:|---|---|---|:--:|
| 1 | Match clock | 30 s AUTO + 8 s transition + 2:00 TELEOP | identical | ✅ |
| 2 | Named ENDGAME | **none** | none — plus `grep -ci endgame` = 0, and 0:30 identified as a *de facto* boundary via Table 9-1 + G427 | ✅ |
| 3 | MATCH cycle time | 6–10 min per field (§10.1, 10.4) | not reported | ❌ |
| 4 | **Randomised objective** | **NONE.** AprilTags 36h11 IDs 11–16, outside the perimeter, **localization only** (§9.8) | **not reported anywhere in R3, R5-R6 or D5** — zero occurrences of "AprilTag" or "randomis/randomiz" | ❌ |
| 5 | Multipliers / sets / ownership | none — "the flattest scoring table in the corpus" | "no multiplier row, no ownership row, no set-completion row, no coopertition row… this season has no multiplier or set mechanic at all" | ✅ |
| 6 | AUTO double-counting | **Confirmed** (Q&A Q21): every AUTO element doubles; AUTO HIGH CHAMBER = **20**, AUTO HIGH BASKET = **16** | derived as the plain reading, computed 20 and 16 exactly, then left `[UNVERIFIED]` and queued for Q&A; **D5 then planned on the single-count reading (assumption A8)** | ⚠ partial |
| 7 | LEVEL 3 risk profile | all-or-nothing but **retryable** — a failed ascent may disengage and re-attempt (10.5.3) | not reported — although the text is in `TRIPWIRES.txt` (lines 2323–2327) and `full_layout.txt` | ❌ |
| 8 | ASCENT vs PARK stacking | earns only the higher (10.5.3.D) | "earns only the highest… per ROBOT per period you bank `max(PARK 3, L1 3, L2 15, L3 30)`" | ✅ |
| 9 | Penalties | MINOR +5 / MAJOR +15, credited to opponent (Table 10-4) | identical, plus the exchange rate 1 MAJOR = 1 ASCENT L2 = 1.5 HIGH CHAMBER | ✅ |
| 10 | Pre-load | 1 SAMPLE **or** 1 SPECIMEN per ROBOT (10.3.1) | identical, plus the derived "both robots pre-load SPECIMENS ⇒ HP holds 18 CLIPS and nothing legal to clip" trap | ✅ |
| 11 | Field stock | 15 red + 15 blue + 30 neutral in SUBMERSIBLE; 20 CLIPS per alliance | full inventory 20/20/40/40 with SPIKE MARK and outside-wall breakdown, arithmetic closing exactly | ✅ |
| 12 | AUTO **fixed** ceiling | **6** (2 robots parking or L1) — smallest in the corpus | never stated as a fixed/non-cycle ceiling; R3's AUTO table reports 46 (cycle-inclusive) | ⚠ partial |
| 13 | "Endgame" ceiling | **60** (2 × LEVEL 3) | **60** (2 × LEVEL 3), stated exactly | ✅ |

Two key entries are **not scoreable**: *typical winning score* (key = UNVERIFIED; harness = `[JUDGMENT]`
150–200, correctly labelled and correctly flagged as uncheckable), and *"the season FIRST adopted the FRC-style
manual"* (a cross-season claim no single-season bundle can produce).

**Structural hit rate: 8 / 13 clean, 2 partial, 3 missed.** Strict: **8 / 13 = 0.615**.

### 1.5 The headline number

| Block | Items | Hits | Partial | Miss | Strict hit rate |
|---|---:|---:|---:|---:|---:|
| Table 10-3 point values | 18 | 18 | 0 | 0 | **1.000** |
| Ranking-point conditions | 5 | 5 | 0 | 0 | **1.000** |
| Tiebreakers | 5 | 5 | 0 | 0 | **1.000** |
| Other structural facts | 13 | 8 | 2 | 3 | **0.615** |
| **TOTAL** | **41** | **36** | **2** | **3** | **36 / 41 = 0.878** |

**ACCURACY SCORE: 36/41 = 87.8 % strict** (90.2 % if partials score half). No rounding in the harness's favour:
items 6 and 12 are counted as misses in the strict figure, and item 6 is a miss with real consequences — see §1.7.

### 1.6 …but 11 of those 41 items were not blind

This is the finding that governs the whole verdict.

`reference/STRATEGY-RANKING-PROTOCOL.md` is on the **allowed** list. R3 cites it in its own header
(*"arithmetic conventions from `STRATEGY-RANKING-PROTOCOL.md` §6.2–6.3"*). Section **§6.3.1** of that file reads:

> *"All point values `[H]` from 2024-25 INTO THE DEEP (`SCORING-PATTERNS.md` §A.10, Table 10-3): HIGH CHAMBER
> specimen **10**, HIGH BASKET sample **8**, LEAVE **3**, ASCENT L1 **3**, ASCENT L3 **30**. AUTO 30 s, TELEOP
> 120 s, 150 s of play."*

— followed by a fully worked chamber-vs-basket cycle model. **R3 did not declare this leak.** Its leak register
flags only a background recollection about AUTO double-counting. So:

| Contaminated item | Where it was pre-printed | In an allowed file? |
|---|---|:--:|
| HIGH CHAMBER 10 (2 cells) | `STRATEGY-RANKING-PROTOCOL.md` §4 X1, §6.3.1; `ACHIEVABILITY-RUBRIC.md` §5.1, §11 | yes |
| HIGH BASKET 8 (2 cells) | same | yes |
| ASCENT L1 3 (2 cells) | §6.3.1 | yes |
| ASCENT L3 30 (1 cell) | §6.3.1; `ACHIEVABILITY-RUBRIC.md` §11.3 | yes |
| PARK 3 (2 cells) | §6.3.1, mislabelled "LEAVE 3" | yes |
| Match clock 30/120/150 s | §6.3 | yes |
| AUTO double-counting (item 6) | `LOOPHOLE-PLAYBOOK.md` §2 Pass 5 — *"ITD Q&A Q21 confirmed every AUTO element doubled"* | yes (R5-R6 **did** declare this one, as leak L1) |

**Blind-certified hit rate: 26 / 30 = 0.867.** The 41-item score stands as an accuracy measurement; it does not
stand as a *blindness* measurement. And D5 says the same about itself, correctly and at length (leak L4:
`ACHIEVABILITY-RUBRIC.md` §8 contains the four ITD calibration candidates **with their A and V scores and
quadrant assignments** — I1 79/90 BUILD THIS, I2 52/75 TRAP, I3 81/52, I4 100/32; the blind run produced
C1 76/83, C3 57/77, C7 82/58, C11 100/29).

### 1.7 The two partials, and why item 6 is worse than it looks

**Item 6 (AUTO double-counting).** R3 §2.2 reasoned to the right answer, gave the right arithmetic (20 and 16),
gave the right structural evidence (identical AUTO/TELEOP columns; PARK unambiguously assessed twice; G412 only
has teeth if presence keeps earning), stated the counter-reading fairly, and queued it as Q&A #1. That is
**exactly the behaviour the protocol asks for**, and the key confirms the primary reading was right.

But the pipeline then **acted on the wrong branch**. D5 assumption A8 fixes the model to single-count
"deliberately conservative", which halves the AUTO period's value. The key says AUTO was worth double —
"a 4-specimen AUTO = 80 pts = 8 teleop cycles" (§B.5), the largest phase leverage on the table. In the blind run
AUTO contributes 13 of C1's 108 points (12 %); on the true reading it contributes 26 of 128 (20 %), and the
AUTO-only contrarian C8 stops being a 62-point loser. **Correct reasoning, wrong number carried forward.** The
harness has no mechanism that forces the model to be *carried both ways* into D3/D4 when R3 flags a
value-moving ambiguity — it just picks the pessimistic branch and moves on.

**Item 12 (AUTO fixed ceiling = 6).** The key's "AUTO fixed ceiling" is a *cross-season comparison metric*:
non-cycle bounties only. The harness never computed it. On this season it is trivially 2 × PARK = 6, and its
value is the ratio it produces — AUTO : ENDGAME = **9 : 91**, the most endgame-weighted season in the corpus.
The blind run never noticed that this season's fixed AUTO bounty is essentially zero.

---

## 2. DID IT FIND THE SEASON'S DEFINING INSIGHT?

**Yes — stated more sharply than the answer key states it — but it cannot be credited as a discovery, and its
supporting arithmetic is wrong in a way that mattered downstream.**

### What R3 actually concluded

> **§6.2 FINDING 1 — YES. The price ladder is inverted. Both CHAMBERS outprice the BASKET above them in
> difficulty.**
>
> *"HIGH CHAMBER pays 25% MORE than HIGH BASKET for 60% of the lift. … Per inch of required lift:
> 0.385 ÷ 0.186 = **2.07× better.**"*
>
> *"**Stated loudly, because this is the kind of finding that decides a season: the cheapest tall mechanism in
> INTO THE DEEP is also the highest-paying one. The LOW CHAMBER — a 13-inch lift, the lowest scoring height of
> any non-floor objective in the game — pays 6, half again what a 25.75-inch LOW BASKET lift pays.**"*
>
> **§6.3 FINDING 2 — the trap: HIGH BASKET is the most expensive mechanism in the game and it is not the
> best-paying objective.**
>
> *"**If your team builds exactly one tall mechanism this season, build it 26 inches tall, not 43.**"*

And D5 turned it into a build order: *"**A ROBOT → C1** … **Do not build anything that reaches 43 inches.**"*

The answer key's version (§B.8):

> *"INTO THE DEEP is the textbook case. The HIGH BASKET (8) looked like the premium goal and required a tall
> vertical lift; the HIGH CHAMBER specimen (10) was faster, closer to the human player, and mechanically
> simpler."*

### Three things to say about that, in order of importance

**(a) It was pre-announced in an allowed file, twice.** `STRATEGY-RANKING-PROTOCOL.md` §4, contrarian **X1**,
which the analyst is *required* to instantiate:

> *"`[H]` INTO THE DEEP: HIGH CHAMBER (10 pts, short lift) beat HIGH BASKET (8 pts, tall two-stage lift). The
> 'premium' goal was worth **less per action and slower**. Teams that built for the big number lost."*

and `ACHIEVABILITY-RUBRIC.md` §5.1 Rule V-b (declared by D5 as leak L6). The blind run was told the answer and
then asked the question. **This item cannot be scored as insight.**

**(b) What *is* original is the derivation, and it is better than the key's.** The **points-per-inch-of-lift
ledger** (R3 §6.1) appears in no method file and in no answer-key file. It produces a falsifiable ratio
(2.07× on the HIGH pair, 2.98× on the LOW pair) instead of a narrative, and it **extends the finding to the LOW
CHAMBER / LOW BASKET pair, which the answer key does not record at all**. It also independently produced the
ASCENT LEVEL 2 finding — 15 points at 0.75 pts/inch, four times the HIGH BASKET's 0.19, from one hook and one
motor, off the *LOW* RUNG because Table 10-2 says "HIGH **and/or** LOW RUNGS" and condition C binds LEVEL 3 only.
That reading of "and/or" is a genuine, checkable, unleaked find. If the method files are decontaminated and the
harness still produces §6.1, that is real insight.

**(c) The supporting speed claim is backwards, and it poisoned the value axis.** The key says the chamber was
**faster** (10 pts / ~5 s ≈ 2 pts/s sustained). R3 §3.4 concluded the opposite:

> *"**They tie.** 0.72 vs 0.71."*

and §6.6:

> *"Per-cycle, once you charge the SPECIMEN branch for the CLIP round trip, **HIGH CHAMBER (0.78 pts/s) and
> HIGH BASKET (0.79 pts/s) are throughput-identical.** The CHAMBER's advantage is **not** speed."*

R3's best match-averaged rate for the whole game is **0.72 pts/s**; the key's is ~**2.0 pts/s** — the harness is
**2.6–2.8× pessimistic**. The cause is compounding pessimism: a ×0.7 realism factor on drive speed *and* a
mandated ×1.3 multiplier on every un-stopwatched cycle (≈1.86× total), plus charging every specimen cycle a full
SUBMERSIBLE fetch. It got the right verdict for a partly wrong reason — it attributed the chamber's win entirely
to mechanism cost when speed was also on its side.

**And this is where the error became expensive.** D5 §8.2 reports that factor **V2 (match points-per-second,
weight 25)** collapsed — ten of eleven candidates scored 1–3, ratings 4 and 5 structurally unreachable — and
blamed the rubric's anchor bands for being "calibrated for a higher-scoring game". **That diagnosis is probably
wrong.** The bands put >1.0 pts/s at rating 4; the protocol's own worked example (§6.3.1) reaches 1.22 pts/s on
this same season, and the rubric's own calibration puts the real strategy at 2.0. The anchors were fine. **The
input was 2.6× low.** D5 then "fixed" the instrument by re-anchoring V2 to the harness's own depressed range —
which is exactly the wrong correction, and it happened to leave rank 1 unchanged only by luck. A harness that
mis-measures its inputs and then re-calibrates its instrument to match will produce confident, self-consistent,
wrong answers on BIOBUZZ. **This is the most dangerous single behaviour in the run.**

---

## 3. CROSS-SEASON GENERALIZATION

DECODE: 188 pp / 214 rules / 17 orange. INTO THE DEEP: 146 pp / 209 rules / 16 orange. Five components checked.

### 3.1 Ingest gates and tripwires — **PASSED, with one masked failure and one gating error**

The four R1 gates (`ANALYSIS-PROTOCOL.md` §2) are written as ranges, not constants — "expect roughly 180–230
rules", "~16–17 orange" — and all four went green on a season they were not written for. `TRIPWIRES.txt` fired
**312 hits** against the DECODE dress run's 318, across five game-agnostic categories (hedge words, counting
words, timers, carve-outs, scored-live/at-end). All five categories produced findings. **No DECODE shape
assumed.**

Two defects, both season-independent:

- **Gate G-d is too weak and masked a real extraction failure.** It requires only *"a `Table 10-x` row with 8 or
  more rows"*. Table 10-3 satisfied it, so the gate went green while **Table 10-2 was entirely missing** and a
  glossary block was masquerading under its name. Verified above. On BIOBUZZ this fails silently again.
- **The scored-live/at-end tripwire category is gated to R6, but R3 is the phase that needs it.** `STATUS.md`
  feed order says *"`TRIPWIRES.txt` — loophole candidates (phase R6 only)"*. The single highest-leverage
  sentence in the manual (§10.5, tripwire lines 2218–2226) is in that file, and R3 had to find it by hand.

### 3.2 The caps-novelty detector — **WORKED, but this run cannot prove it generalizes**

Top of `caps_NOVEL_ranked.txt`: SUBMERSIBLE 63 · SAMPLES 56 · OBSERVATION 47 · ASCENT 45 · SAMPLE 39 ·
SPECIMEN 35 · NET 26. Every real game noun surfaced in the top ten. Gate G-c green. The stoplist design is
genuinely season-agnostic: Tier 1 = BIOBUZZ V0 caps, **Tier 2 = caps present in *both* DECODE and ITD but absent
from V0** (i.e. evergreen-by-intersection), Tier 3 = generic noise. Verified that SUBMERSIBLE/SAMPLE/SPECIMEN/
CHAMBER/RUNG/BASKET/ASCENT/CLIP are all **absent** from the stoplist, as intended.

But: **`known_caps_stoplist.txt` line 2 says it was built from "BIOBUZZ V0, DECODE TU32, INTO THE DEEP V14."**
The detector was tuned on the manual it is being tested against. This run is train-on-test and cannot measure
novelty-detection generalization at all.

And Tier 3 is too thin — **VEX 6, HIPS 4, BILDA 4, EDR 3, SPARK 2, IEC 2, JST 1, NZS 1, DEEPSM 2, NADO 1, FOR 2,
PER 1** all leaked into the ranked list. On an unseen game the top-20 of this file is the first thing an analyst
trusts. Section 12 vendor tables must be excluded before ranking.

### 3.3 Archetype vocabulary — **NOT TESTED, because both archetype sources are forbidden files**

`ANALYSIS-PROTOCOL.md` R5 step 2 routes to `PENALTY-AND-ENFORCEMENT.md` §3; `STRATEGY-RANKING-PROTOCOL.md` D2
§5.1 routes to `ROBOT-ARCHETYPE-LIBRARY.md` §2/§3.1–3.11/§5; the R6 taxonomy routes to
`research/LOOPHOLE-CASEBOOK.md` Parts C and F. **All three are on the forbidden list.** The archetype layer of
this harness was never exercised this run — it was routed around.

The substitutes the analyst improvised are better than the originals and should be adopted:
- **R5:** the manual's own §11 subsection headings *are* the penalty archetype list (Personal Safety / Conduct /
  Pre-MATCH / AUTO / TELEOP / SCORING ELEMENT / ROBOT / Opponent Interaction / Human & DRIVE TEAM / Post-MATCH).
  Season-agnostic, derivable at ingest.
- **D2:** describe mechanism shape as `(acquisition, delivery height, actuation, actuator count, duplicability
  driver)` from ARENA geometry — no library needed.
- **D7:** derive Team-Update nerfs from *this* manual's own patchable surfaces rather than transplanting
  prior-season precedents. D5's own note is right: *"a nerf derived from this manual's own ambiguities is a real
  risk, while one transplanted from another game is a guess wearing a citation."*

**One concrete instance of DECODE vocabulary bleeding into this season's own analysis:**
`STRATEGY-RANKING-PROTOCOL.md` §6.3.1 lists this season's row as **"LEAVE 3"**. INTO THE DEEP has no LEAVE.
It has PARK. The allowed method file mislabels the season it is describing, using the *next* season's noun.

### 3.4 Rubric anchors and gates — **PARTIALLY FAILED. This is where DECODE shape is baked in.**

| Component | Result | Evidence |
|---|---|---|
| **Gate G2 (actuators)** | **FAILS on this season** | Rubric §3 hard-codes *"> 8 motors **or > 8 servos**"* citing R503. This manual's **R503 reads "8 motors and 12 servos"** (verified, `rules_full.tsv` line 141). The gate would reject a legal 10-servo design. |
| **Gate G6 / R801 (stored energy)** | **INVERTED on this season** | Rubric §3 and `mechanisms/EXTENSION-ARMS-LIFTS.md` §7.5 assert R801 permits *"sealed, COTS closed-air systems… (such as gas shocks)"* and label it **CONFIRMED-BIOBUZZ**. This manual's **R207 bans gas springs outright** and **R801 permits nothing except R207's list** (verified, `rules_full.tsv` lines 128, 182). |
| **Gate G5 (cash ceiling)** | **UNEVALUABLE** | Sourced from `research/SMALL-TEAM-ECONOMICS.md`, which is on **neither** the allowed nor the forbidden list. Gate never ran. The candidate it would most likely have killed (C3, `$1,222` two-robot BOM) is the softest result in D5. |
| **V2 anchor bands** | **held; the input was wrong** | See §2(c). D5 blamed the anchors; the anchors were fine at 1.22 pts/s from the protocol's own example. |
| **V5 top anchor** | **FAILS on this season** | V5 rating 5 requires *"earns a ranking point"*. This season has **no RP except winning** — verified, Table 10-3 has exactly two RP rows. The top anchor is unreachable by construction. This anchor is written for DECODE, which has three bonus RPs. |
| **Rubric §11 calibration** | **internally inconsistent** | §11.3 justifies `I1 V2 = 5` with *"10 pts / ~5 s cycle = 2.0 pts/s"* — an **action** rate, in direct violation of the rubric's own **Rule V-a** (points ÷ full match length). The instrument's calibration example breaks the instrument's own rule. D5 did not catch this. |
| **D1 candidate band (7–10)** | **too narrow for this season** | 5 uncapped repeatable rows + 7 mandatory contrarians = 12 before merging. D5 carried 11 and logged the deviation. |
| **Rubric §6 worked example** | **DECODE-shaped** | *"4 drive + 2 flywheel + 1 intake + 1 index = 8 motors… only if the turret is a servo."* A shooter robot. Nothing in INTO THE DEEP shoots; G417 penalises it. |

### 3.5 Mechanism catalogues — **FAILED on a checkable legality fact**

`reference/mechanisms/` carries **119 `CONFIRMED-BIOBUZZ` labels** across six files, all asserted against the V0
placeholder manual and **none re-verified against the ingested manual**. The failure above is not cosmetic:
`EXTENSION-ARMS-LIFTS.md` builds its self-described *"best idea in this section"* — the zero-motor-slot
gas-spring climb (§7.5, §8, and BOM rows at lines 1006 and 1120) — on an actuator this manual bans. A team
running the harness would have carried an illegal mechanism into D2 and only discovered it at inspection.
**Ordinary mechanical springs remain legal** (they are not closed-air systems), so the idea survives; the part
number does not. Nothing in the harness cross-checks a catalogue legality claim against the season's R-rules.

Coverage is also skewed: `LAUNCHERS-AND-FEEDING.md` has **8 DECODE references and 0 relevant to this season** —
an entire catalogue with no application here and no mechanism to notice that.

### 3.6 Generalization verdict

| Layer | Generalizes? |
|---|---|
| Ingest, gates, bundle format, feed order | **Yes** — nothing assumed a season's shape |
| Tripwire categories | **Yes** — all five fired; gating is wrong, categories are right |
| Caps-novelty detector | **Probably** — design is sound; untestable here (trained on this manual) |
| Arithmetic conventions (Rule V-a, ×1.3, displacement test) | **Yes** — ported without an edit |
| Floor rules and quadrant machinery | **Yes** — MF4 caught C10 by one point; MF5 killed two healthy-looking totals |
| Two-run A/B reweighting | **Yes** — produced a genuine swap arithmetically (C3 STRETCH for A, TRAP for B; C6 rank 4 for A, rank 1 for B) |
| Archetype vocabulary | **Untested** — both sources forbidden |
| Rubric gates and anchors | **No** — G2, G6 and V5 all carry DECODE/V0 numbers |
| Mechanism catalogues | **No** — season-specific legality labels never re-verified |
| **Method-file independence from the season under test** | **No** — the answer key is distributed across five allowed files |

---

## 4. WHAT BROKE — consolidated from all 24 beta-feedback items

### 4.1 Contamination (the run-invalidating class)

| # | Allowed file | What it gives away |
|---|---|---|
| C1 | `STRATEGY-RANKING-PROTOCOL.md` §4 X1 | The defining insight, verbatim, as a mandatory contrarian |
| C2 | `STRATEGY-RANKING-PROTOCOL.md` §6.3.1 | Five of nine Table 10-3 rows + the match clock + a worked chamber-vs-basket cycle model. **Not declared by R3.** |
| C3 | `ACHIEVABILITY-RUBRIC.md` §8, §11 | The complete D5 answer: four ITD candidates with A, V and quadrant |
| C4 | `ACHIEVABILITY-RUBRIC.md` §5.1 Rule V-b | HIGH CHAMBER 10 / short lift vs HIGH BASKET 8 / tall lift |
| C5 | `ACHIEVABILITY-FACTORS.md` §8.1 | Three ITD candidates with per-factor ratings |
| C6 | `LOOPHOLE-PLAYBOOK.md` §2 Pass 5, §3 | Q&A Q21 (the AUTO-recount answer); G427 as "the canonical case"; G423's 5 s pin limit |

### 4.2 Protocol steps that dead-end in forbidden files — six of them

`ANALYSIS-PROTOCOL.md` §3.3 (the 18 questions → `SCORING-PATTERNS.md` §C.2) · §3.4 (inflation curve →
`SCORING-PATTERNS.md` §B.11) · R5 step 2 (archetypes → `PENALTY-AND-ENFORCEMENT.md` §3) · R6 (taxonomy →
`LOOPHOLE-CASEBOOK.md` Parts C/F) · `STRATEGY-RANKING-PROTOCOL.md` D2 §5.1 (→ `ROBOT-ARCHETYPE-LIBRARY.md`) ·
D7 §10.1–10.2 (→ `PENALTY-AND-ENFORCEMENT.md` + `LOOPHOLE-CASEBOOK.md`).

**This is not a bookkeeping problem — it caused the run's biggest content miss.** The 18 questions the analyst
skipped are §C.2 Q6–Q10, *all five of which are about randomisation*. That is precisely the block that went
unanswered (§1.4 item 4). On a season where the answer is "none", skipping them is harmless. On DECODE or on
BIOBUZZ it is fatal.

### 4.3 Bundle gaps

| Missing | Consequence |
|---|---|
| **Table 10-2** absent from `TABLES.md`; glossary false-positives under its heading | Recovered only from a page image. Gate G-d green anyway. |
| **No `GLOSSARY.tsv`** | §16 is a two-column table that `pdftotext -layout` collapses; CONTROL / PIN / LAUNCH / PLOWING recovered **by counting positions**. Two of six Q&A questions depend on that recovery. |
| **No `SETUP_AND_ELEMENTS.txt`** | The §10.3.1 pre-load contradiction — the sentence pair that kills candidate C2 — exists only in `full_layout.txt`, the last-resort file. |
| **No `SCORING_TIMING.txt` at R3** | The scored-live/at-end sentences are gated to R6. |
| **No `SECTION_MAP.txt`** | The §11 heading map (the archetype substitute) has to be reconstructed by hand. |
| **No `R_LIMITS.txt`** | Nothing carries this season's actual actuator / stored-energy / expansion numbers, so the rubric gates ran on last season's. |
| **Figures stop at p.70** | Figures **11-1/11-2/11-3** (pp. 86–87, the G427 protected-vs-not illustrations — 45-point rule, "~7 in" threshold **defined by those pictures**) and **12-1/12-2** (p. 94, R104 expansion) were never rendered. F5 and F12 are under-confident as a result. |
| **`TRIPWIRES.txt` line numbers index `full_layout.txt`** | The honest workflow is "read tripwire, then open the file the house rules call last resort." |
| **`rules_GAMESPECIFIC.txt` is headline-only** | 16 bare `id + headline` lines; must be re-joined to `rules_full.tsv` by hand. |
| **`rules_ADDED` / `rules_REMOVED` / `section_versions` not in the feed order** | `section_versions.txt` (Section 11 at V12, Section 10 at V9, Section 8 at V1) is a direct "which rules are already patched" signal for R6 Pass 2. |
| **`caps_NOVEL_ranked.txt` noise** | Vendor and OCR fragments in the top-40. |
| **MANIFEST advice contradicts the house rule** | *"Read the scoring PROSE in the text extract, not off the image"* — but the §10.5.3 prose is the part that was scrambled and the image was correct. |

### 4.4 Numbers that could not be found

- Whether AUTO-scored elements re-count in TELEOP — **the absence *is* the finding**, correctly queued. Moves
  the ceiling 266 → 306 and the A robot 108 → 128. *(Key: they do.)*
- Whether a ROBOT may be pre-loaded with CLIPS — §10.3.1 contradicts itself. Correctly queued.
- Any winning-score distribution. `S_win = 150` is the denominator of V1, which carries 30 % of Axis V and did
  most of the discriminating work — **and the harness gave the analyst no way to check it.** *(Key: UNVERIFIED
  too. Nobody has this number. It must come from event data.)*
- The program's cash ceiling — Gate G5 never ran.
- Binding thresholds for "excessive", "egregious", "short distance"; the G419/G432 priority. Genuine manual
  weaknesses, not ingest failures.

### 4.5 Things that worked and must be preserved

`rules_full.tsv` (headline + body + violation in one row) — the most useful file in the bundle · `VIOLATIONS.tsv`
as a standalone · `ORANGE_BOXES.md` labelling non-binding text, which held all run · the four R1 gates as ranges
· the mandatory contrarian slate (X1/X3/X5 all looked plausible and all three died to five lines of arithmetic)
· the minimum-viable floor (MF4 caught C10 by exactly one point; MF5 killed the two candidates whose totals
looked healthiest) · the two-run A/B reweighting · **and above all the "never take point values from flat text"
rule, which this run proves is load-bearing**: `full_layout.txt` rendered Table 10-3 as
`PARK OBSERVATION ZONE 3 3 2` and mislabelled Table 10-2's LEVEL rows off by one.

---

## 5. FIX LIST BEFORE 2026-09-12

### P0 — without these the BIOBUZZ run is not a measurement

| # | File | Change |
|---|---|---|
| **1** | `reference/ACHIEVABILITY-RUBRIC.md` §8, §11–§13 · `reference/ACHIEVABILITY-FACTORS.md` §8.1 | **Move every worked calibration into `reference/CALIBRATION.md`** and remove it from the kickoff read path. These sections contain the D5 answer with scores and quadrants. Excellent teaching material; poison in the analyst's context. |
| **2** | `reference/STRATEGY-RANKING-PROTOCOL.md` §4 X1–X5, §6.3.1 | **Replace every ITD/DECODE numeric example with a synthetic game.** §6.3.1 currently hands over five point values, the clock and a worked chamber-vs-basket model; X1 hands over the season's defining insight. Use fictional values (e.g. "GOAL A 7 pts at 15 in, GOAL B 5 pts at 40 in"). Also fix **"LEAVE 3" → the season's own term**. |
| **3** | `reference/LOOPHOLE-PLAYBOOK.md` §2 Pass 5, §3 | Strip the Q&A Q21 answer and the named G-rule examples. Keep the *pass structure*, delete the worked seasons. |
| **4** | `reference/ANALYSIS-PROTOCOL.md` §3.3, §3.4; `STRATEGY-RANKING-PROTOCOL.md` D2 §5.1, D7 §10.1–10.2; R5 step 2; R6 | **Inline the method these steps need** so no step dereferences a corpus file. Specifically: copy the 18 kickoff questions into `ANALYSIS-PROTOCOL.md` itself (they are game-agnostic); adopt the three substitutes from §3.3 above. **Q6–Q10 (randomisation) are non-negotiable** — their absence cost this run item 4. |
| **5** | run brief + `reference/` index | Make the allowed/forbidden lists **exhaustive over `reference/` and `research/`**. "Unlisted" must not be a state an analyst has to guess about (`SMALL-TEAM-ECONOMICS.md` cost Gate G5 entirely). |

### P1 — correctness bugs that would produce wrong answers on any season

| # | File | Change |
|---|---|---|
| **6** | `reference/ACHIEVABILITY-RUBRIC.md` §3 gates G2, G6 | **Gates must name the constraint, not the number.** G2 → "the manual's stated actuator limit (motors, servos)". G6 → "whatever the manual's stored-energy rule permits". Both currently carry numbers wrong for this manual (R503 is 8 **and 12**; R207 **bans** gas springs). |
| **7** | ingest (`tools/`) → bundle | **Emit `R_LIMITS.txt`** at ingest: actuator counts, battery count, expansion envelope, stored-energy permissions, quoted with rule ids. Feed the gates from it. |
| **8** | `reference/mechanisms/*.md` | **Every `CONFIRMED-BIOBUZZ` legality claim (119 of them) must be re-verified against `R_LIMITS.txt` at kickoff** before any BOM row is used. Add a required verification pass to D2. Fix `EXTENSION-ARMS-LIFTS.md` §7.5/§8 today — its flagship idea rests on a banned actuator in this manual. |
| **9** | `reference/ACHIEVABILITY-RUBRIC.md` §5 V2 and V5 | **V2 → season-relative:** *"as a fraction of the best match-averaged rate the scoring table admits, computed at D3."* **V5 → ladder-relative:** *"how many of this season's ranking-ladder sort criteria does this deliberately feed, and at what magnitude."* V5's current top anchor ("earns a ranking point") is unreachable in any season without bonus RPs. |
| **10** | `reference/STRATEGY-RANKING-PROTOCOL.md` §6.2 + `ANALYSIS-PROTOCOL.md` §3 | **Add a cycle-model sanity check.** The ×0.7 speed factor and the ×1.3 cycle multiplier compound to ≈1.86× pessimism and produced a top rate 2.6× below reality. Require R3 to state its best match-averaged rate **and** cross-check it against the theoretical floor (fastest legal traverse + minimum manipulation time). **Add the standing rule: if the model's top rate lands below the rubric's own rating-4 band, suspect the model before re-anchoring the rubric.** |
| **11** | `reference/ANALYSIS-PROTOCOL.md` §3 + `STRATEGY-RANKING-PROTOCOL.md` §6 | **Any `[UNVERIFIED]` that moves the ceiling by >10 % must be carried through D3/D4 as a two-branch model, not collapsed to the pessimistic branch.** The AUTO-recount question was reasoned correctly at R3 and then silently halved at D5. |
| **12** | ingest gate G-d | **Verify that every `Table N-x` referenced in Section 9/10 prose has a matching heading in `TABLES.md`**, and that the heading's page number is inside that section. Table 10-2 was missing while the gate reported PASS, and a glossary block sat under its name. |

### P2 — bundle completeness

| # | File | Change |
|---|---|---|
| **13** | ingest → bundle | **Render figures for the G-rule and R-rule sections**, or at minimum any page whose rule body contains the string "Figure". Figures 11-1/11-2/11-3 define the 45-point rule's threshold. |
| **14** | ingest → bundle | **Emit `GLOSSARY.tsv` (term, definition).** The two-column §16 collapses under `pdftotext -layout`; two Q&A questions rested on recovery-by-counting. |
| **15** | ingest → bundle | **Emit `SETUP_AND_ELEMENTS.txt`** (§10.3 pre-match setup prose + §9.x element definitions) and put it in the feed order between `TABLES.md` and `rules_GAMESPECIFIC.txt`. Generalise: *every prose section a rule body cross-references gets its own extract file.* |
| **16** | ingest → bundle · `STATUS.md` | **Emit `SCORING_TIMING.txt`** (the scored-live / at-end / at-rest sentences) and make it available at **R3**, not R6. Un-gate the scored-live tripwire category from R6. |
| **17** | ingest → bundle | **Emit `SECTION_MAP.txt`** (the §11 subsection headings) — the season-agnostic penalty-archetype list. |
| **18** | ingest | **Add `rule_id` to every `TRIPWIRES.txt` line** (the mapping is already in `rules_full.tsv`) so no tripwire requires opening `full_layout.txt`. |
| **19** | ingest | **Add `page` and `violation` columns to `rules_GAMESPECIFIC.txt`.** A 16-line orange-rule list should be usable standalone on kickoff morning. |
| **20** | `reference/known_caps_stoplist.txt` + ingest | **Exclude Section 12 vendor tables before ranking** `caps_NOVEL`. Expand Tier 3 to catch vendor names, material codes and standards acronyms. Note in the header that the list was built from ITD V14 and therefore cannot self-validate on that manual. |
| **21** | `STATUS.md` feed order | **Promote `section_versions.txt` into the feed order** as the "what has already been patched" input to R6. On BIOBUZZ kickoff everything reads V0/V1, which is itself the correct signal. |
| **22** | `bundle/figures/MANIFEST.txt` | **Fix the contradictory advice.** "Read the scoring prose in the text extract, not off the image" is the opposite of what this run needed and conflicts with the house rule. Correct wording: *"read the table from `TABLES.md`; if a table is missing or a row looks off by one, the rendered page is authoritative."* |

### P3 — protocol shape

| # | File | Change |
|---|---|---|
| **23** | `STRATEGY-RANKING-PROTOCOL.md` D1 §4.5 | Make the candidate band a **function of the scoring table** — "one per uncapped repeatable row, plus the seven contrarians, minus overlaps" — not a fixed 7–10. |
| **24** | `LOOPHOLE-PLAYBOOK.md` Pass 6 | Reword the stored-energy prompt to *"which stored-energy sources does the R-section permit, and what does the G-section say about propelling elements with them?"* The current version presumes a permission this manual does not grant. |
| **25** | `ACHIEVABILITY-RUBRIC.md` §11.3 | Fix the internal contradiction: `I1 V2 = 5` is justified with an **action** rate (2.0 pts/s over a 5 s cycle) in violation of the file's own **Rule V-a**. Recompute the calibration match-averaged, or the instrument teaches analysts to break its own rule. |

---

## 6. THE VERDICT

**On accuracy: 36 / 41 = 87.8 % strict; 26 / 30 = 86.7 % on the blind-certified subset.** Perfect on the point
table, the RP conditions and the tiebreaker ladder. It also recovered a table the bundle did not contain, caught
an off-by-one in the flat text, and closed the element inventory arithmetically as a self-check.

**On insight: it produced the right answer and cannot be credited for it.** The finding was pre-printed in two
allowed files. What is genuinely original — the points-per-inch-of-lift ledger, its extension to the LOW pair,
the "and/or" reading that makes LEVEL 2 a low-rung hang, and the observation that Table 13-1 sort 3 counts ASCENT
but not PARK — is real work and is not in the answer key. But its supporting throughput claim is backwards, by a
factor of 2.6, and that error propagated into the value axis and was then mistaken for an instrument fault.

**On generalization: the *plumbing* generalizes and the *judgment layer* does not.** Ingest, gates, tripwires,
arithmetic conventions, floor rules and the two-run rubric all ran clean on a game they were not written for.
The rubric's gates and anchors, and the mechanism catalogues, carry hard-coded numbers from DECODE and from the
BIOBUZZ V0 placeholder — three of which are **wrong for this manual and would have been applied without anyone
noticing**. The archetype layer was never tested because both of its sources are forbidden files.

**Is it ready for 2026-09-12? No — but the gap is 25 specific edits, not a redesign.** Items 1–5 must land or the
BIOBUZZ run will be graded by an analyst who has already read the answer. Items 6–12 must land or the harness
will confidently apply last season's rules to this season's robot. Everything else is completeness.

**The single sentence I would put on the wall:** *the harness's worst failure this run was not getting a number
wrong — it was getting a number wrong, noticing that its instrument disagreed, and re-calibrating the instrument.*

---

## Beta feedback

**On this verdict task specifically.**

1. **"Compare it line by line against the answer key" is not well-defined, because the two documents are not the
   same kind of artifact.** `SCORING-PATTERNS.md` §A.10 is a **cross-season comparison record** — it carries
   "AUTO fixed ceiling = 6", "AUTO : ENDGAME = 9 : 91", "endgame ceiling / top element = 6.0". `R3-scoring-model.md`
   is a **single-season decision document**. Roughly a third of the key's ITD entries are only meaningful against
   the other ten seasons and are unanswerable from one bundle by construction. I scored 13 structural items and
   excluded two as unscoreable, and I have said exactly which — but another reviewer would draw that line
   somewhere else and get a different hit rate. **For BIOBUZZ, define the scoreable item list *before* the run**,
   as a checklist in `ANALYSIS-PROTOCOL.md`, so the accuracy number is reproducible rather than negotiated.

2. **The task told me the defining insight before I read R3.** *"The answer key records that INTO THE DEEP priced
   the HIGH CHAMBER above the HIGH BASKET…"* — I read that in the brief, then went looking for it in R3 and found
   it. I could not have judged "did it find this independently" cleanly even if the method files had been clean.
   **The grader's brief needs the same contamination discipline as the analyst's.** Ask "what is the season's
   defining insight, and did the run find it?" without naming it.

3. **There is no measurement of *how long* any of this took.** Every beta-feedback item is about correctness;
   none is about the kickoff-day clock. `ANALYSIS-PROTOCOL.md` §3 says "budget the full hour" for R3, and R3
   ended up recovering a table from a page image, counting glossary columns by position, and grepping the
   last-resort file. **A harness that produces 87.8 % accuracy in nine hours fails on kickoff day.** Instrument
   the BIOBUZZ run with wall-clock timestamps per phase.

4. **Nothing in the harness cross-checks one blind output against another.** R3 concluded HIGH CHAMBER and HIGH
   BASKET were throughput-identical; D5's V2 column then collapsed for exactly that reason and D5 re-anchored
   the rubric to fix it. Two documents, one root cause, no step that connects them. **A cheap fix with real
   value: a D3 gate that reads R3's top match-averaged rate and refuses to proceed if it falls below the
   rubric's rating-4 band without a written justification.**

5. **The forbidden-file list is enforced on the analyst and not on the harness.** Five allowed method files
   contain this season's answers; the analysts found and declared six leaks between them (R5-R6's L1–L3, D5's
   L4–L6) and **missed the largest one** (`STRATEGY-RANKING-PROTOCOL.md` §6.3.1, which R3 cites in its own
   header). Self-reported leak registers are a good practice and an inadequate control. **Before BIOBUZZ, grep
   every allowed file for the game's own nouns and point values and treat any hit as a blocking defect** — the
   check takes seconds and would have caught all six.

6. **What worked in this task and should be kept:** having the blind outputs carry their own labelled
   `[MANUAL]`/`[DERIVED]`/`[JUDGMENT]`/`[UNVERIFIED]` provenance made line-by-line comparison mechanical rather
   than interpretive; the leak registers, even incomplete, made contamination visible instead of invisible; and
   requiring a `## Beta feedback` section on every phase output produced 24 concrete, actionable defects, of
   which I was able to independently verify every one I checked.
