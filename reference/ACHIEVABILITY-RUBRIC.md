# ACHIEVABILITY RUBRIC — the scoring instrument

**What this file is:** the fillable, arithmetic-complete instrument that ranks candidate BIOBUZZ strategies
and designs for **this** program. `ACHIEVABILITY-FACTORS.md` argues *why* the factors are the factors; this
file is the thing you actually print, fill in, and total on Kickoff morning.

**Status:** game-agnostic scaffolding, written 2026-08-21, **22 days before BIOBUZZ Kickoff (2026-09-12)**.
Sections 8–11, 13 and 15 of the BIOBUZZ V0 manual are placeholders (§14 League Play is *not*). Nothing here assumes a game task.

| Attribute | Value |
|---|---|
| Students | ~15 total |
| Registered teams | 2 (A team + B team), **two robots** |
| Budget | Modest — 2 × `$350` registration + events + 2 robots |
| Fabrication | COTS kits, 3D printing, hand tools. **No CNC mill, no lathe, no waterjet, no welding** |
| Mentor hours | Limited — cannot supervise two independent design programs |
| Practice field | Assume partial (tiles + some elements), not a full dedicated field |

**Companion files — read, do not duplicate:**

| File | What it supplies to this rubric |
|---|---|
| `reference/ACHIEVABILITY-FACTORS.md` | Factor definitions, full prose anchors, per-factor evidence, exemplars E1–E8 |
| `reference/AWARD-CATALOG-BIOBUZZ.md` | The real BIOBUZZ award set, A201–A215, Table 6-1 |
| `reference/AWARD-ALIGNMENT-MATRIX.md` | Strategy → award pairing detail (this rubric only produces the *input*) |
| `reference/ROBOT-ARCHETYPE-LIBRARY.md` | The candidate archetypes this rubric scores |
| `reference/SCORING-PATTERNS.md` | Verified per-season scoring tables and points-per-second history (§A.10, §A.11, §B.8, §B.9) |
| `reference/CONSTRUCTION-RULES-R.md`, `reference/PENALTY-AND-ENFORCEMENT.md` | Gate G1 / G6 source text |
| `research/TWO-TEAM-PROGRAM-RULES.md`, `research/SMALL-TEAM-ECONOMICS.md` | The A/B split and the cash ceiling behind Gates G4/G5 |

**Evidence labels used here** (same convention as the companion files):
**CONFIRMED-BIOBUZZ** = read from the 2026-27 V0 manual we hold · **CONFIRMED-PRESEASON** = published by FIRST
for 2026-27 outside the manual · **HISTORICAL** = prior-season fact, never a BIOBUZZ fact ·
**VERIFIED-WEB** = fetched from a named URL on 2026-08-21 · **JUDGMENT** = synthesis, not a rule or a measurement.

---

## Contents

| § | Section |
|---|---|
| [1](#1-the-five-minute-version) | The five-minute version |
| [2](#2-why-two-axes-and-not-one-number) | Why two axes and not one number |
| [3](#3-gates--run-before-any-scoring) | Gates — run **before** any scoring |
| [4](#4-axis-a--achievability-12-factors) | Axis A — Achievability (12 factors, anchors, weights) |
| [5](#5-axis-v--competitive-value-5-factors) | Axis V — Competitive Value (5 factors, anchors, weights) |
| [6](#6-third-number-award-yield-ay) | Third number — Award Yield (AY) |
| [7](#7-the-arithmetic) | The arithmetic |
| [8](#8-the-2x2-quadrants-cut-lines-and-the-trap-overlay) | The 2×2: quadrants, cut lines, TRAP overlay |
| [9](#9-minimum-viable-floor-decision-rule-and-tie-breakers) | Minimum viable floor, decision rule, tie-breakers |
| [10](#10-blank-scoring-sheet-copy-this) | **Blank scoring sheet (copy this)** |
| [11](#11-calibration-run-1--2024-25-into-the-deep) | Calibration run 1 — 2024-25 INTO THE DEEP |
| [12](#12-calibration-run-2--2025-26-decode) | Calibration run 2 — 2025-26 DECODE |
| [13](#13-what-calibration-changed-and-what-it-refused-to-change) | What calibration changed (and refused to change) |
| [14](#14-a-team-vs-b-team-variant) | A-team vs B-team variant |
| [15](#15-re-run-triggers) | Re-run triggers |
| [16](#16-machine-readable-model) | Machine-readable model |
| [17](#17-divergences-from-achievability-factorsmd-and-known-gaps) | Divergences and known gaps |

---

## 1. The five-minute version

1. **Write down 4–6 candidate whole-match strategies.** Not mechanisms — *strategies*. "A claw on a slide" is
   not a candidate; "score the highest-value repeatable target from the near wall, park at the end" is.
2. **Run the seven gates (§3).** A gate trip rejects or re-scopes. Gates are not averaged.
3. **Score column-wise** (all candidates on F1, then all on F2, …) — never one candidate at a time.
4. Compute **A** (Achievability, 0–100) and **V** (Competitive Value, 0–100) and **AY** (Award Yield, 0–100).
5. **Plot each candidate on the 2×2 (§8).** Read off the quadrant.
6. **Apply the minimum viable floor and the decision rule (§9).** Break ties in the stated order.
7. **Hand the top 2–3 to the award-pairing and BOM stages** with their AY sub-scores attached.

Budget: **45 minutes** for a full first run with 5 candidates and two scorers. **10 minutes** for a delta
re-score after a Team Update.

---

## 2. Why two axes and not one number

`ACHIEVABILITY-FACTORS.md` produces a single weighted composite out of 16 factors. That is the right model for
answering "which one strategy should we pick", and it is wrong for everything else this program needs to decide,
because **a composite silently trades payoff against buildability at a fixed exchange rate you never agreed to.**

Two concrete failures of the single number, both demonstrated in §11–§12 below:

| Failure | What a composite does | What the 2×2 does |
|---|---|---|
| A trivially-buildable, near-worthless strategy | Ranks high on build factors, mid overall, looks acceptable | Lands in **SAFE FLOOR** — visibly the fallback, never the plan |
| A high-payoff strategy this program cannot finish | Ranks mid overall, looks like a reasonable compromise | Lands in **TRAP** — visibly out of reach, and its de-scoped variant is forced to be scored separately |

The 2×2 also matches the actual decision, which is not one decision but three: *what does the A robot build*,
*what does the B robot build*, and *what is the fallback if the A robot's mechanism is not working by the
de-scope date*. Those three answers usually live in three different quadrants.

### 2.1 The axis-independence rule (read this before scoring)

> **Axis V is scored at design intent. Axis A carries all of the execution risk.**

Score **V** as if the robot works exactly as drawn, every time. Score **A** as the probability-and-cost of
getting there with 15 students and hand tools. Never discount a V rating for "but we probably can't hit that" —
that discount is F5, F8, F10 and F11 on the other axis, and applying it twice collapses every candidate onto
the diagonal and destroys the whole point of the plot.

This is a **deliberate divergence** from `ACHIEVABILITY-FACTORS.md` F12, whose anchor says "at realistic success
rate". Under this rubric, F12's realism discount moves wholesale to Axis A. See §17.

### 2.2 Factor mapping to the companion file

| `ACHIEVABILITY-FACTORS.md` | Here |
|---|---|
| F1–F11, F16 (weights 9,9,5,4,4,3,5,7,4,8,4,8 = 70) | **Axis A**, renormalised to 100, then two calibration adjustments (§13) |
| F12 Scoring Ceiling & PPS (12) | **Split** into V1 Scoring Ceiling + V2 Match Points-Per-Second |
| F13 Defense Resistance (5) | **V4** |
| F14 Alliance Value (5) | **V3** Alliance Desirability |
| F15 Award-Generation Potential (8) | **AY**, a third reported number — *not* a ranking term. See §6 and §17 |
| Gates G1–G6, FLAG-1 | Carried unchanged; **G7 and FLAG-2 added** by calibration (§13) |
| Exemplars E1–E8 | Still the pre-registered scale anchors. Every live rating must be defensible against them |

---

## 3. Gates — run **before** any scoring

A gate trip is not a low score. It is a **reject or re-scope**, decided before anyone writes a number, so that
four 5s cannot outvote one fatal 1.

| Gate | Trip condition | Source | Action on trip |
|---|---|---|---|
| **G1 Legality** | Violates any final BIOBUZZ rule in §3 (I), §5 (E) or §12 (R) | CONFIRMED-BIOBUZZ | **Reject.** Not a scoring matter |
| **G2 Actuator budget** | > 8 motors **or** > 8 servos summed across **all** configurations for one robot | **R503** §12.5, reinforced by **I302** §3.3.1 | **Reject or re-scope.** Count drivetrain first (typically 4 motors), then what remains |
| **G3 Fabrication floor** | Requires CNC milling/turning, welding, waterjet or custom gears, with no *named, priced, lead-time-verified* vendor in the plan | JUDGMENT on program capability | **Reject.** If a vendor is named, the candidate survives but **F1 = 1** |
| **G4 Two-robot feasibility** | Cannot be built twice within budget *and* mentor hours | JUDGMENT; CD t/406178 HISTORICAL | **Reject unless** a de-scoped B variant is named — and that variant is then **scored as its own candidate** |
| **G5 Cash ceiling** | BOM + season spares for **two** robots exceeds the stated cash ceiling | `research/SMALL-TEAM-ECONOMICS.md` | **Reject or re-scope.** Price both robots, never one |
| **G6 Pneumatics / airflow** | Pneumatic actuation, generated pressure/vacuum, or a high-speed airflow device | **R801** §12.8 (flywheels and rollers are explicitly *not* airflow devices) | **Reject** |
| **G7 Loophole / intent test** *(added by calibration — §13)* | The strategy's value depends on (a) an "it doesn't say we can't" reading, or (b) unbounded use of a resource FIRST has capped in ≥ 2 prior seasons (human-player handling, off-field element storage, descoring, expansion, protected zones) | HISTORICAL: DECODE TU01/TU02; ITD TU03/TU05/TU10 | **Do not reject.** Cap **V ≤ 40** and hold the candidate under **FLAG-2** until TU02 has been read |

| Flag | Condition | Action |
|---|---|---|
| **FLAG-1** | Depends on the still-unpublished **R105** sizing constraints, or on any Section 8–11 / 13 / 15 text | Score anyway, mark, re-score after Kickoff and after TU01/TU02 |
| **FLAG-2** *(new)* | Tripped G7 | Report **V as a range**: pre-TU value and post-nerf worst case. The decision rule uses the **worst case** until TU02 lands |

---

## 4. Axis A — Achievability (12 factors)

**Polarity is uniform: 5 is always favourable.** Cost-shaped factors are inverted, so 5 means *little* of that cost.
Full definitions, evidence and scoring traps: `ACHIEVABILITY-FACTORS.md` §4.

| # | Factor | Pol. | **w(A)** | w(B) | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---:|---:|---|---|---|---|---|
| **F1** | Fabrication complexity | inv | **13** | 15 | ≥1 CNC/turned/waterjet structural part, welding, or custom gears | Outsourced flat-plate cutting for ≥2 load-bearing parts, never done before | Bolt-together kit, but ≥3 printed parts load-bearing in multiple axes **or** ≥2 need hand-fitting | Kit extrusion + plate + printed brackets, each loaded in one axis; longest print < 4 h; drill/hacksaw/file/tap only | COTS chassis (**R301.A**) or StarterBot mechanism (**R301.B**) + bolt-ons; printed parts non-structural; no hand-fitting |
| **F2** | Duplicability A/B | dir | **13** | 10 | Copy #2 needs the same student and ~the same mentor hours; hand-fitted or one-off machined | Orderable but > 60% of original BOM **and** needs re-tuning; no CAD/print files | Reproducible from files, but 2–4 parts need per-robot fitting and each robot needs its own tuning pass | 100% catalogue + print-file defined; a student who did not build #1 can assemble #2 from a printed BOM; one short tuning pass | Entire parts list is a shopping cart; copy #2 = purchase order + assembly session; A/B mechanisms interchangeable as drop-in spares under **I303.F** |
| **F3** | BOM + season spares cost | inv | **7** | 8 | > `$800`/robot marginal, or a single-source part > 2-week lead time with no spare budgeted | `$500–800`/robot, spares unbudgeted | `$250–500`/robot, partial spares kit | `$100–250`/robot; full spare set of printed parts + all wear items in the pit bin | < `$100`/robot marginal; reuses parts already owned (**R304**) or is a StarterBot/COTS-chassis derivative. Spares *are* the other robot's identical parts |
| **F4** | Time to first working prototype | inv | **5** | 8 | > 6 weeks, or a lead time landing after your first event | 4–6 weeks | 2–4 weeks | 1–2 weeks with materials already in the shop | ≤ 1 week, or **already proven pre-Kickoff** (POLLEN and the StarterBot Base are purchasable/published now — CONFIRMED-PRESEASON) |
| **F5** | Time to reliable | inv | **6** | 9 | Still improving at the first event; < 60% success in practice | > 6 weeks past prototype; plateaus ~70% | 3–6 weeks; ~80%, sensitive to battery state or field position | 1–3 weeks; ≥ 90% across battery states and start positions | Reliable on first assembly — success is geometric, not tuned (funnel, hook, fixed-height deposit) |
| **F6** | Iteration cost (week-6 reversibility) | inv | **3** | 5 | Re-order outsourced plates or scrap the chassis; > 50% of original cost | Scraps the mechanism not the chassis; 2+ weeks, > 30% of BOM | Re-print several parts and re-drill structure; ~1 week | Re-print 1–2 brackets, move bolts on existing extrusion; < 3 days | Reposition on slotted/gridded structure with existing hardware; hours. Subsystem swaps at a defined interface |
| **F7** | Programming burden | inv | **7** | 10 | Motion profiling + path following + multi-state coordination + a custom control loop before it scores at all | Closed-loop position/velocity on ≥2 subsystems plus a state machine | Encoder positioning with PID on one subsystem plus a simple sequence | Run-to-position on a motor + a few servo presets; stock SDK throughout | Direct operator control; AUTO is drive-forward-and-deposit |
| **F8** | Tuning burden | inv | **10** | 8 | > 10 empirical constants; a function of pose and battery voltage; constants do **not** transfer between the two robots and must be re-found at each venue | 6–10 constants with real drift (velocity-controlled launch, variable-distance aiming) | 3–5 constants, mildly drift-sensitive | 1–2 constants, stable across batteries and venues | Zero empirical constants — hard stops, funnels, gravity, a fixed hook |
| **F9** | Sensor & vision dependence | inv | **6** | 5 | Primary scoring fails without vision/tag localisation; no fallback | Vision-dependent for high-value scoring; manual fallback much slower | Vision/odometry for AUTO only; TELEOP fully manual | Proprioceptive only — encoders, limit switches, IMU; failures detectable and recoverable in-match | No sensor required to score |
| **F10** | Match reliability & failure consequence | dir | **11** | 13 | A likely failure immobilises the robot, causes a foul, or risks ARENA damage (**R201**) / un-removable robot (**R203**) | Failure ends all scoring; not driver-recoverable; no spare | Failure ends scoring but the robot still drives, parks, defends | Failure costs 1–2 cycles and the driver can clear it | No plausible in-match failure removes scoring; degrades gracefully; identical spare is a legal drop-in under **I303.F** |
| **F11** | Driver skill ceiling & practice demand | inv | **6** | 6 | Precise positioning at speed under defense; > 40 h to reach claimed rate; a novice gets < 40% | Consistent alignment; 20–40 h | 10–20 h; novice reaches ~70% | < 10 h; forgiving alignment (funnels, wide capture, driver-assist presets) | Near-zero skill floor; novice matches expert within a session; **both** drive teams run it in week 1 |
| **F16** | Rule-change exposure | inv | **13** | 3 | Value depends on a loophole, ambiguity, or "it doesn't say we can't" | Depends on the edge of one rule, or a rule with a tightening history (protected zones, human-player actions, descoring, expansion) | Depends on a normal reading of one G-rule that could be clarified against you | Depends only on core scoring as written; a nerf costs efficiency, not the strategy | Depends on the central scoring loop, which cannot be nerfed without redesigning the game; or uses only §12 (R) rules, **already final** for BIOBUZZ |

**w(A) sums to 100. w(B) sums to 100.** Derivation of w(A) in §13.1; the B column is explained in §14.

**Scoring discipline (from `ACHIEVABILITY-FACTORS.md` §8 — apply all of it):** score column-wise; every 3 needs
a one-sentence written observable or it becomes **U**; **U** is legal and costs you (the candidate is ranked
twice, U→4 and U→2, and if the two rankings disagree on rank 1 you are not ready to decide); ban the words
*moderate, reasonable, somewhat, fairly* from justifications; two scorers, log every disagreement of ≥ 2.

---

## 5. Axis V — Competitive Value (5 factors)

Scored **at design intent** (§2.1). All five anchors are game-agnostic shapes; §15 tells you when to replace
the shapes with measured numbers.

> **"Typical winning score"** = the median winning alliance score at events of the type you attend. Before
> your first event, estimate it from the published scoring table × plausible cycle counts. After your first
> event, **replace the estimate with the measured number** — this is the single highest-value re-score.

| # | Factor | **w(A)** | w(B) | 1 | 2 | 3 | 4 | 5 |
|---|---|---:|---:|---|---|---|---|---|
| **V1** | **Scoring ceiling** — one robot's peak contribution as a share of a typical winning score | **30** | 15 | < 10% | 10–20% (a parking/support role) | 20–35% (a credible third robot). **Hard cap for any once-per-match-only strategy** | 35–55% (a solid second pick) | > 55%, or the single highest-value repeatable action available to a robot of this class |
| **V2** | **Match points-per-second** — points contributed ÷ **whole match length**, not ÷ the action | **25** | 20 | < 0.25 pts/s match-averaged | 0.25–0.5 | 0.5–1.0 | 1.0–1.5 | > 1.5, or the highest match-averaged rate on the scoring table |
| **V3** | **Alliance desirability** — what a captain writes next to your number | **20** | **35** | Actively harms an alliance: hogs a shared resource, causes fouls, unpredictable | Neutral filler, picked late if at all | Reliable driveable partner: parks, plays clean defense, causes no fouls | A capability captains plan around; **and** the A/B pair does not contend for the same resource | Captain-grade or first-pick-grade; **and** A and B are deliberately complementary so both are individually pickable |
| **V4** | **Defense resistance** | **15** | 15 | Requires occupying one specific spot, or depends on a resource an opponent can deny. One parked robot zeroes you | Single scoring location; a defender halves the rate; no alternate path | Contestable location with a slower fallback | Multiple scoring positions, or scores on the move; defense costs cycles, not the strategy | Position-independent, or occurs where opponents may not legally be, or is an action defense cannot reach |
| **V5** | **Phase & ranking leverage** — AUTO, endgame, and any ranking-point structure | **10** | 15 | Contributes nothing outside ordinary TELEOP cycling | Contributes to one phase incidentally (e.g. a park) | Deliberately earns one bounded phase bonus | Earns a phase bonus **and** a ranking criterion, or exploits a double-counted AUTO achievement | Earns the top phase bonus *and* a ranking point *and* is compatible with the alliance partner needing the same real estate |

**w(A) sums to 100. w(B) sums to 100.**

### 5.1 Two anchor rules that exist because the rubric got them wrong (§13)

> **Rule V-a — match-averaged, always.** V2 is `points ÷ 150 s` (or whatever the real match length is), **not**
> `points ÷ seconds the action took`. A 30-point action performed once in a match is **0.2 pts/s**, not 3 pts/s.
> HISTORICAL: `SCORING-PATTERNS.md` §B.9 shows the endgame ceiling has shrunk from 200 (2015-16 RES-Q) to 60
> (2024-25 ITD) to 30 (2025-26 DECODE). A one-shot mechanism is an add-on, never a strategy.

> **Rule V-b — value does not track difficulty.** If action X is worth **more** points **and** takes **less**
> time than action Y, then Y may not out-score X on V1 or V2, no matter how impressive Y's mechanism is.
> HISTORICAL (verified, `SCORING-PATTERNS.md` §A.10, ITD Table 10-3): HIGH CHAMBER = **10 pts** and reachable
> with a short lift; HIGH BASKET = **8 pts** and needed a tall two-stage extension. The taller mechanism was
> worth less per action *and* slower. Teams that scored the basket higher on payoff were scoring the mechanism,
> not the game.

---

## 6. Third number: Award Yield (AY)

Awards are this program's highest-yield advancement currency — **§4.1 Table 4-1 (CONFIRMED-BIOBUZZ)**: Inspire
1st = **60** advancement points versus **40** for winning the event, and any other 1st place judged award = **12**,
comparable to the ~16 points of the top qualification seed. But award potential must **not** be a ranking term:
a robot chosen for its award story over its ability to work fails the award criteria anyway (Innovate §6.3.6
criterion 3 requires the design be stable and reliable *most of the time*; Design §6.3.8 asks for "elegant,
efficient … simple to build and operate"). So AY is reported, used as tie-break #5, and handed to the pairing
stage — never added into A or V.

| # | Sub-factor | w | 1 | 3 | 5 |
|---|---|---:|---|---|---|
| **AY1** | **Evidence generation** — does *building it* manufacture the artifacts judges reward? | **50** | One design, no alternatives considered, no numbers | Two alternatives compared informally; some measurements | ≥2 prototypes built and compared with recorded data, and ≥1 decision made from arithmetic (Think §6.3.2 criteria 1C "comparing choices" and 1D "math choices") |
| **AY2** | **Demonstrability** — can a judge watch it work, in the pit, in 60 seconds? | **30** | Only works on a full field with a partner | Works on a tile with setup | Bench-demonstrable, repeatable on demand, and its failure mode is explainable |
| **AY3** | **Criteria fit** — does it map onto a named award's own words? | **20** | No award's text describes it | Fits one award weakly | Fits ≥1 award's literal criteria, and that award is on **Table 6-1** for your event size |

`AY = Σ(w × rating) / 5`, 0–100. Hand the pairing stage the **AY sub-scores**, not just the total —
`AWARD-ALIGNMENT-MATRIX.md` keys off which sub-factor is strong.

**Hard pairing constraints (all CONFIRMED-BIOBUZZ):** **A215** one judged award or runner-up per team per event
→ deliberately split A and B targets · **A211/Table 6-1** the award set shrinks at small events and only listed
awards are points-eligible · **A201** 15 content pages + 1 cover, content from 2026-01-01 only, judges will not
click links, **AI use permitted with a footnote/endnote credit** · **A203** Initial Interview mandatory ·
**§6.1** no awards at League Meets · **never pair Innovate with F10 ≤ 2**.

---

## 7. The arithmetic

```
A  = Σ ( wA_i × rating_i ) / 5        over F1…F11, F16    ΣwA = 100   →  A  ∈ [20, 100]
V  = Σ ( wV_j × rating_j ) / 5        over V1…V5          ΣwV = 100   →  V  ∈ [20, 100]
AY = Σ ( wAY_k × rating_k ) / 5       over AY1…AY3        ΣwAY = 100  →  AY ∈ [20, 100]
```

Dividing by 5 puts an all-5s candidate at exactly 100 and an all-1s candidate at 20. **There is no
composite of A and V. Do not compute one.**

**Always report eight things per candidate:**

| Output | Meaning |
|---|---|
| `A` | Achievability 0–100 |
| `V` | Competitive Value 0–100 (a **range** if FLAG-2) |
| `AY` | Award Yield 0–100 |
| `quadrant` | From §8 |
| `gates` | Pass / trip list from §3 |
| `min_A`, `min_V` | Lowest single rating on each axis, with the factor id |
| `flags` | FLAG-1 / FLAG-2 items and every `U` |
| `spread` | Range of `A` and range of `V` across all candidates |

**Spread check.** If the range of `A` across candidates is **< 15**, or the range of `V` is **< 20**, the rubric
has not discriminated. Re-run `ACHIEVABILITY-FACTORS.md` §8 mechanisms 1, 2 and 5 (column-wise scoring,
forced-spread check, countable anchors) before believing any ranking. *(The parent file's threshold is 10 on a
single composite; two axes of 12 and 5 factors should spread further, so the bar here is higher.)*

**Worked arithmetic, one factor at a time — ITD-A "high-chamber specimen cycler", Axis A:**

```
F1 13×4=52  F2 13×4=52  F3 7×4=28  F4 5×4=20  F5 6×4=24  F6 3×4=12
F7  7×4=28  F8 10×4=40  F9 6×4=24  F10 11×4=44 F11 6×3=18 F16 13×4=52
Σ = 394        A = 394 / 5 = 78.8 → 79
```

---

## 8. The 2×2: quadrants, cut lines, and the TRAP overlay

**Cut lines: `A = 65`, `V = 55`.** Both are set from the calibration runs in §11–§12, not chosen a priori —
see §13.3 for how they were placed and what they separate.

```
  100 │  STRETCH GOAL / TRAP       ┊  BUILD THIS
   95 │       D2                   ┊
   90 │                            ┊          I1
   85 │                            ┊
   80 │                            ┊
   75 │                  I2        ┊ D1
   70 │                            ┊
   65 │                            ┊
   60 │                            ┊
   55 │                            ┊
      ├────────────────────────────┼────────────────────────────  V cut = 55
   50 │                            ┊            I3 D3
   45 │                            ┊                      D4
   40 │  SKIP                      ┊  SAFE FLOOR
   35 │                            ┊             D3'
   30 │                            ┊                           I4
      └─────────────────────────────────────────────────────────
       30              50          65          80              100
                                   ↑ A cut = 65         ACHIEVABILITY →
```

| Code | Candidate | A | V | Quadrant |
|---|---|---:|---:|---|
| **I1** | ITD high-chamber specimen cycler | 79 | 90 | **BUILD THIS** |
| **I2** | ITD high-basket sample bot (tall two-stage) | 52 | 75 | **TRAP** (below floor) |
| **I3** | ITD endgame ascent specialist | 81 | 52 | SAFE FLOOR |
| **I4** | ITD COTS chassis, park + AUTO leave only | 100 | 32 | SAFE FLOOR (fallback only) |
| **D1** | DECODE fixed-angle single-flywheel launcher | 67 | 77 | **BUILD THIS** |
| **D2** | DECODE turret + vision auto-aim launcher | 39 | 97 | **TRAP** (below floor) |
| **D3 / D3'** | DECODE intake+hopper, feed human player | 82 | 52 → **37** post-TU02 | SAFE FLOOR, **G7 + FLAG-2** |
| **D4** | DECODE BASE-return + LEAVE + defense | 94 | 43 | SAFE FLOOR (**BUILD THIS for the B team** — §14) |

### 8.1 Quadrant definitions

| Quadrant | Condition | What it means | What you do |
|---|---|---|---|
| **BUILD THIS** | `A ≥ 65` and `V ≥ 55` | Worth winning with, and this program can finish it twice | The A robot's primary design. Aim for exactly **one** of these |
| **STRETCH GOAL** | `A < 65`, `V ≥ 55`, **clears the minimum viable floor (§9.1)** | Genuinely valuable and genuinely hard. Reachable only with a written de-scope and a kill date | A-team only, never the B robot. Requires a named fallback candidate that is itself in BUILD THIS or SAFE FLOOR, and a **de-scope date** on the calendar before it is started |
| **TRAP** *(overlay)* | `V ≥ 55` but **fails the floor** (`A < 55`, or a min-factor veto, or an untripped-but-uncleared gate) | Looks like the winning robot, is not a robot you will finish | **Do not build.** Write down *why* — the disagreement log is Think §6.3.2 evidence — and build its de-scoped sibling instead |
| **SAFE FLOOR** | `A ≥ 65`, `V < 55` | Cannot lose you a season, cannot win you one | The **B robot's** default, and the A robot's fallback if the primary mechanism misses its de-scope date. Never the A robot's plan |
| **SKIP** | `A < 65` and `V < 55` | Hard *and* worthless | Delete from the list. Do not spend meeting time arguing about it |

**Why "SAFE FLOOR" and not "Skip" in the high-A/low-V corner.** A two-robot program *needs* a stocked
high-achievability/low-value quadrant: it is where the B robot lives, and it is where the A robot retreats to on
the de-scope date. Labelling it "Skip" would delete the fallback plan, which for a 15-student program is the
most load-bearing plan there is. Calibration bears this out — **D4** is a SAFE FLOOR candidate for the A team
and a **BUILD THIS** candidate for the B team on the same ratings (§14.3).

---

## 9. Minimum viable floor, decision rule, and tie-breakers

### 9.1 Minimum viable floor — every candidate must clear **all** of it

| # | Floor condition | Rationale |
|---|---|---|
| **MF1** | All seven gates pass (G7 may be *tripped-and-held* under FLAG-2, but not ignored) | §3 |
| **MF2** | `A ≥ 55` | Below 55 this program does not finish it. Calibration: both TRAP candidates sit at 52 and 39 |
| **MF3** | `V ≥ 40` | Below 40 it is a fallback, not a candidate. Calibration: park-only sits at 32 |
| **MF4** | `A + V ≥ 120` | Blocks the "safe but pointless" and "brilliant but impossible" extremes that individually squeak past MF2/MF3 |
| **MF5** | No rating of **1** on **F1, F2, F3, F10 or F16** | Fabrication, duplicability, cash, failure consequence, rule exposure. A 1 on any of these is a season-ender, not a deduction. *(F16 added by calibration — §13.2)* |
| **MF6** | ≤ 2 `U` ratings on Axis A, and **0** `U` on V1 or V2 | You may be ignorant about the edges. You may not be ignorant about the payoff |
| **MF7** | Optimistic (`U→4`) and pessimistic (`U→2`) substitutions **agree on rank 1** | If they disagree, you are not ready to decide — prototype first |
| **MF8** | A named, de-scoped **B variant** exists and has been scored as its own candidate | **G4**; and the B robot is a second independent A215 award slot and a second 60-point Inspire lottery ticket (§4.1) |
| **MF9** | The robot can perform **at least one scoring action without a partner** | Alliance-dependent strategies fail in qualification matches with a weak partner |
| **MF10** | Fits the inspection envelope with margin: 18-in. cube start (**R102**), ≤ 8 motors / 8 servos (**R503**), exactly 1 approved battery (**R601**), no pneumatics (**R801**) | Re-check after R105's sizing constraints publish at Kickoff (**FLAG-1**) |

A candidate failing the floor is **not scored out of the running — it is out of the running.** Record the failed
condition next to it and move on.

### 9.2 Decision rule

```
1. Discard every candidate that fails the minimum viable floor (§9.1).
2. If exactly one candidate is in BUILD THIS  → that is the A robot. Go to 6.
3. If more than one is in BUILD THIS          → apply tie-breakers (§9.3).
4. If none is in BUILD THIS:
      4a. If a STRETCH GOAL exists that clears the floor → take it,
          AND adopt the highest-V SAFE FLOOR candidate as the written fallback,
          AND put a de-scope date on the calendar before build starts.
      4b. Otherwise → take the highest-V SAFE FLOOR candidate. Accept that this
          is a development season, and spend the freed hours on AY and on driver practice.
5. The B robot is chosen by re-running steps 1-4 with the B-team weights (§14).
   It may be the same architecture de-scoped, or a complementary SAFE FLOOR candidate.
   It may NOT be a STRETCH GOAL or a TRAP.
6. Hand the chosen pair, with AY sub-scores, to the award-pairing stage and the BOM stage.
```

**Guardrail:** if the A and B robots both land on the same scoring resource, **V3 for both must be re-scored**
downward (the anchor says so explicitly) and step 5 re-run. Two identical robots contending for one target are
worth less than the sum of their parts.

### 9.3 Tie-breakers, in order

Apply strictly in sequence; stop at the first one that separates.

| # | Tie-break | Why this order |
|---|---|---|
| **1** | **A robot: higher `V`. B robot: higher `A`.** | The two robots have different jobs; the tie-break should say so |
| **2** | Fewer `U` ratings | Certainty is worth more than an optimistic estimate |
| **3** | Higher **F2** (duplicability) | The program-defining factor. Backed by rule text: **I303.F** makes identical mechanisms legal drop-in spares; **R304** makes the work compound across seasons |
| **4** | Higher **F16** (rule-change exposure) | The candidate that survives Thursday |
| **5** | Higher **AY** | Only now does the award story break a tie |
| **6** | Higher **F4** (fastest to first prototype) | Get on the field; measured data beats argument |
| **7** | The one whose written fallback de-scope already exists | Reward the team that did the contingency work |
| **8** | **Still tied → prototype both for one week, then re-score V1 and V2 with measured cycle times.** A coin flip is not a tie-break | The tie means your anchors are not yet grounded in seconds |

---

## 10. Blank scoring sheet (copy this)

> One sheet per candidate. Score **column-wise across candidates**, not down a single sheet — fill the F1 row on
> every sheet, then the F2 row, and so on. Two scorers, independently, then reconcile.

**Candidate:** ____________________  **Scorer:** __________  **Date:** __________
**One-line description (whole-match strategy, not a mechanism):** ______________________________________
**Robot this is being scored for:** ☐ A team  ☐ B team  *(use the matching weight column)*

### Gate checklist

| Gate | Pass? | Evidence / rule id |
|---|---|---|
| G1 Legality (I / E / R rules) | ☐ pass ☐ trip | |
| G2 Actuator budget — motors ____ /8, servos ____ /8 (**R503**, **I302**) | ☐ pass ☐ trip | |
| G3 Fabrication floor | ☐ pass ☐ trip | vendor / price / lead time: |
| G4 Two-robot feasibility | ☐ pass ☐ trip | named B variant: |
| G5 Cash ceiling — 2-robot BOM + spares `$` ______ | ☐ pass ☐ trip | |
| G6 Pneumatics / airflow (**R801**) | ☐ pass ☐ trip | |
| G7 Loophole / intent test | ☐ pass ☐ **hold (FLAG-2)** | rule leaned on: |
| FLAG-1 Depends on R105 / Sections 8–11 | ☐ no ☐ yes | |

### Axis A — Achievability

| # | Factor | w(A) | w(B) | Rating (1–5 or U) | Observable justification (one sentence, must contain a count / hour / dollar / named process) | w × r |
|---|---|---:|---:|:---:|---|---:|
| F1 | Fabrication complexity | 13 | 15 | | | |
| F2 | Duplicability A/B | 13 | 10 | | | |
| F3 | BOM + spares cost | 7 | 8 | | | |
| F4 | Time to first prototype | 5 | 8 | | | |
| F5 | Time to reliable | 6 | 9 | | | |
| F6 | Iteration cost | 3 | 5 | | | |
| F7 | Programming burden | 7 | 10 | | | |
| F8 | Tuning burden | 10 | 8 | | | |
| F9 | Sensor / vision dependence | 6 | 5 | | | |
| F10 | Match reliability & consequence | 11 | 13 | | | |
| F11 | Driver skill & practice | 6 | 6 | | | |
| F16 | Rule-change exposure | 13 | 3 | | | |
| | **Σ** | 100 | 100 | | | |

**A = Σ ÷ 5 = ______**   **min_A = ____ on F____**

### Axis V — Competitive Value *(score at design intent — see §2.1)*

| # | Factor | w(A) | w(B) | Rating | Observable justification | w × r |
|---|---|---:|---:|:---:|---|---:|
| V1 | Scoring ceiling (% of typical winning score) | 30 | 15 | | | |
| V2 | Match points-per-second (÷ full match length) | 25 | 20 | | | |
| V3 | Alliance desirability | 20 | 35 | | | |
| V4 | Defense resistance | 15 | 15 | | | |
| V5 | Phase & ranking leverage | 10 | 15 | | | |
| | **Σ** | 100 | 100 | | | |

**V = Σ ÷ 5 = ______**  (FLAG-2? report as ______ pre-TU → ______ worst case)   **min_V = ____ on V____**

### Award Yield

| # | Sub-factor | w | Rating | Justification (cite the award section, e.g. §6.3.2) | w × r |
|---|---|---:|:---:|---|---:|
| AY1 | Evidence generation | 50 | | | |
| AY2 | Demonstrability | 30 | | | |
| AY3 | Criteria fit | 20 | | | |
| | **Σ** | 100 | | | |

**AY = Σ ÷ 5 = ______**   **Award targets (2):** ______________ and ______________

### Result

| Field | Value |
|---|---|
| A / V / AY | ____ / ____ / ____ |
| Quadrant (§8.1) | ☐ BUILD THIS ☐ STRETCH GOAL ☐ TRAP ☐ SAFE FLOOR ☐ SKIP |
| Minimum viable floor (§9.1) | ☐ clears all 10 ☐ fails: MF____ |
| Flags / `U` ratings | |
| De-scope fallback candidate | |
| De-scope kill date | |
| Scorer disagreements ≥ 2 (record — Think §6.3.2 evidence) | |

---

## 11. Calibration run 1 — 2024-25 INTO THE DEEP

**Purpose.** A rubric written before the game is knowable is worth nothing unless it reproduces known answers.
This run scores four real ITD strategy families with the instrument above, then checks the ranking against what
the season actually rewarded.

**Scoring facts used (HISTORICAL, verified in `SCORING-PATTERNS.md` §A.10 from
`2024-25_INTO_THE_DEEP_Competition_Manual.pdf` Table 10-3):** PARK 3 · SAMPLE NET ZONE 2 · LOW BASKET 4 ·
**HIGH BASKET 8** · LOW CHAMBER 6 · **HIGH CHAMBER 10** · ASCENT L1 3 · **L2 15** · **L3 30**. Match = 30 s AUTO +
8 s transition + 2:00 TELEOP, **no End Game period**. AUTO achievements that still meet criteria at the end of
TELEOP are **counted in both periods** (ITD Q&A Q21) — an AUTO high-chamber specimen is worth **20**.
G410 capped CONTROL at 1 SAMPLE or 1 SPECIMEN.

**Rule-change history used for F16 (HISTORICAL, read from `2024-25_ITD_TeamUpdates_Combined.pdf`):**
TU03 (2024-10-17) introduced **G420** "No climbing on the inside — ROBOTS must start their ASCENT with their
CHASSIS completely outside the SUBMERSIBLE ZONE", corrected in TU04 (2024-10-17) and revised again in TU05
(2024-10-31). TU10 (2025-01-16) **narrowed G427** "Climbing ROBOTS are protected", adding an exception because
the original protection "is not working as intended". Chamber and basket scoring were not narrowed.

### 11.1 Candidates

| Code | Whole-match strategy |
|---|---|
| **I1** | **High-chamber specimen cycler.** COTS chassis + single-stage vertical lift + claw/wrist. Human player clips samples into specimens; robot cycles the HIGH CHAMBER (10). AUTO: preload specimen (doubles to 20) + more. Ends with L1 ascent |
| **I2** | **High-basket sample bot.** Two-stage vertical extension + bucket, ground intake, HIGH BASKET (8). Ends with L2/L3 ascent |
| **I3** | **Endgame ascent specialist.** Winch + hooks, LEVEL 3 (30). Minimal teleop scoring; drives, defends, ascends |
| **I4** | **COTS chassis, AUTO leave + PARK only.** The floor baseline (exemplar E1) |

### 11.2 Axis A

| # | w | **I1** | **I2** | **I3** | **I4** |
|---|---:|:---:|:---:|:---:|:---:|
| F1 Fabrication | 13 | 4 | 2 | 4 | 5 |
| F2 Duplicability | 13 | 4 | 2 | 5 | 5 |
| F3 Cost | 7 | 4 | 3 | 4 | 5 |
| F4 Time-to-prototype | 5 | 4 | 3 | 4 | 5 |
| F5 Time-to-reliable | 6 | 4 | 2 | 4 | 5 |
| F6 Iteration cost | 3 | 4 | 2 | 3 | 5 |
| F7 Programming | 7 | 4 | 3 | 5 | 5 |
| F8 Tuning | 10 | 4 | 2 | 5 | 5 |
| F9 Sensors | 6 | 4 | 3 | 4 | 5 |
| F10 Reliability | 11 | 4 | 3 | 3 | 5 |
| F11 Driver skill | 6 | 3 | 2 | 4 | 5 |
| F16 Rule exposure | 13 | 4 | 4 | 3 | 5 |
| **Σ (w×r)** | | **394** | **262** | **403** | **500** |
| **A** | | **79** | **52** | **81** | **100** |

Key justifications (the ones that carry the ranking):

- **I2 F1 = 2, F2 = 2, F8 = 2.** A two-stage vertical extension needs per-robot alignment shimming, its printed
  mounts are loaded in bending, and its constants (height presets, tip-sensitive drive-speed limits, bucket
  release timing) are voltage-sensitive on a single battery (**R601**). ~6 constants → F8 = 2.
- **I3 F16 = 3.** Ascent geometry was directly re-cut by **G420** six weeks into the season and the ascent
  *protection* rule **G427** was narrowed in January. A robot whose entire value is one endgame action carried
  real exposure — and this is a rule-change that landed in **January**, not in the first fortnight.
- **I3 F10 = 3.** All-or-nothing, but retryable (ITD 10.5.3), and the robot still drives if it fails.
- **I1 F11 = 3.** The cycle rate is driver-limited: aligning to the chamber bar at speed is a 10–20 h skill.

### 11.3 Axis V (design intent)

| # | w | **I1** | **I2** | **I3** | **I4** |
|---|---:|:---:|:---:|:---:|:---:|
| V1 Scoring ceiling | 30 | 5 | 4 | 2 | 1 |
| V2 Match PPS | 25 | 5 | 3 | 1 | 1 |
| V3 Alliance desirability | 20 | 4 | 4 | 3 | 2 |
| V4 Defense resistance | 15 | 3 | 4 | 5 | 3 |
| V5 Phase & ranking leverage | 10 | 5 | 4 | 4 | 2 |
| **Σ (w×r)** | | **450** | **375** | **260** | **160** |
| **V** | | **90** | **75** | **52** | **32** |

- **I1 V2 = 5.** 10 pts / ~5 s cycle = **2.0 pts/s** — the top sustained rate in the corpus for that season
  (`SCORING-PATTERNS.md` §B.8, [D]).
- **I2 V2 = 3.** 8 pts / ~8–10 s = ~0.9 pts/s. **Rule V-b fires**: fewer points, longer cycle, taller mechanism.
- **I2 V4 = 4.** The NET ZONE had explicit protection (**G425 NET ZONE Protection**, ITD) — basket play was
  harder to defend than chamber play, which is I2's one genuine advantage over I1.
- **I3 V1 = 2, V2 = 1.** 30 points against a winning score in the low hundreds is ~15%. Match-averaged
  (**Rule V-a**): 30 / 150 s = **0.2 pts/s**.
- **I3 V4 = 5.** Ascending robots were explicitly protected by **G427** — defense literally could not reach it.
- **I1 V5 = 5.** AUTO double-counting (Q&A Q21) makes an AUTO high-chamber specimen worth **20**, the largest
  phase leverage on the table.

### 11.4 Result vs what actually happened

| | I1 | I2 | I3 | I4 |
|---|---:|---:|---:|---:|
| A | 79 | 52 | 81 | 100 |
| V | 90 | 75 | 52 | 32 |
| Floor (§9.1) | clears | **fails MF2** (A 52 < 55) | clears | **fails MF3** (V 32 < 40) |
| Quadrant | **BUILD THIS** | **TRAP** | SAFE FLOOR | SAFE FLOOR (fallback) |

**What actually happened.**

- **HISTORICAL / [D] (`SCORING-PATTERNS.md` §B.8):** *"High-chamber specimen cycling beat basket play outright"*,
  and ITD is named there as the textbook case of the flashy tall mechanism losing to the shorter faster one.
- **VERIFIED-WEB (fetched 2026-08-21, `team11260.org/robots/Into-the-Deep-robot`):** the 2025 FIRST Championship
  **Winning Alliance Captain** ran a specimen/clip robot — *"scoring specimens in the high chamber, not samples
  in the basket"* — with a **10-specimen autonomous** at Worlds and *"sub 2.3 second cycles"*. It also took the
  **Think Award** in its division.

**Verdict: the rubric's V ranking matches the season.** I1 > I2 > I3 > I4 on Competitive Value, and I1 is the
sole BUILD THIS. The tall basket bot — the one that *looks* like the serious robot — is correctly a TRAP for this
program, on two independent grounds (it fails MF2 at A = 52, and Rule V-b docks its payoff).

**An honest caveat about I1.** The world-championship version of I1 used a 120° webcam for sample selection, an
automated clipper, and a belt-driven lift — that build would score **F1 = 2, F2 = 1, F9 = 1** here and land in
TRAP. The rubric does not claim our program could have won Worlds. It claims that the *family* I1 belongs to was
the right family, and that its hand-tool variant was buildable twice. **That is exactly the claim the rubric is
supposed to make**, and it is why V is scored at design intent and A separately.

---

## 12. Calibration run 2 — 2025-26 DECODE

**Scoring facts used (HISTORICAL, verified in `SCORING-PATTERNS.md` §A.11 from
`2025-26_DECODE_Competition_Manual_TU32.pdf` Table 10-2):** LEAVE 3/robot (AUTO) · ARTIFACT **CLASSIFIED 3** ·
OVERFLOW 1 · DEPOT 1 · PATTERN 2/index · BASE partially returned 5 · **fully returned 10** · **both robots
returned +10**. Three bonus RPs (MOVEMENT / GOAL / PATTERN), WIN = 3 RP. **Table 10-3 GOAL RP threshold = 36
artifacts through the SQUARE at ordinary events** — the manual's own statement of a strong alliance performance.
G408 capped simultaneous CONTROL at 3 ARTIFACTS; pre-load up to 3.

**Rule-change history used for F16 and G7 (HISTORICAL, read from `2025-26_DECODE_TeamUpdates_Combined.pdf`):**

| When | Update | Change |
|---|---|---|
| Kickoff + 5 d (2025-09-11) | **TU01** | **G419** retitled *"ROBOTS only ~~score~~ LAUNCH into their own GOAL"* and rewritten to prohibit intentionally **placing** artifacts on your own RAMP; **G418** tightened. **R105 expansion limits published** — 18 × 18 in. horizontal, 18 in. vertical (38 in. under G415), **mechanically constrained, not in software**, demonstrated at inspection |
| Kickoff + 12 d (2025-09-18) | **TU02** | **G433** humans may enter artifacts only during TELEOP, only via the LOADING ZONE, **without LAUNCHING or rolling**; **G432** humans may only retrieve from the LOADING ZONE; **G434** an ALLIANCE may not store **more than 6 ARTIFACTS off the FIELD**, MINOR FOUL per artifact over the limit *plus another every 3 seconds* |

Both of the strategies a low-fabrication team would naturally pick — "place the ball instead of launching it"
and "feed the human players" — were narrowed **within 12 days of Kickoff**.

### 12.1 Candidates

| Code | Whole-match strategy |
|---|---|
| **D1** | **Fixed-angle single-flywheel launcher.** COTS chassis + roller intake + 3-artifact hopper + one fixed-angle flywheel; drive to a repeatable spot in the LAUNCH ZONE and shoot. LEAVE in AUTO, BASE return at the end |
| **D2** | **Full launcher.** Variable-velocity flywheel + servo turret + vision auto-aim + indexed hopper; shoot from anywhere |
| **D3** | **Intake + hopper, no launcher.** Collect artifacts, deliver to the human player / DEPOT; no scoring mechanism |
| **D4** | **BASE-return + LEAVE + defense.** COTS chassis, no scoring mechanism. Guarantees LEAVE (3/robot), the BASE bonus (10 + 10), and the MOVEMENT RP; plays clean defense in between |

**Gate note on D2:** 4 drive + 2 flywheel + 1 intake + 1 index = **8 motors, exactly at the R503 limit**, only
if the turret is a **servo**. Put a motor on the turret and **G2 trips** and the candidate is rejected before it
is scored. This is what gates are for.

### 12.2 Axis A

| # | w | **D1** | **D2** | **D3** | **D4** |
|---|---:|:---:|:---:|:---:|:---:|
| F1 Fabrication | 13 | 4 | 2 | 5 | 5 |
| F2 Duplicability | 13 | 3 | **1** | 5 | 5 |
| F3 Cost | 7 | 4 | 2 | 5 | 5 |
| F4 Time-to-prototype | 5 | 4 | 2 | 5 | 5 |
| F5 Time-to-reliable | 6 | 2 | 1 | 4 | 5 |
| F6 Iteration cost | 3 | 3 | 2 | 4 | 5 |
| F7 Programming | 7 | 3 | 1 | 5 | 4 |
| F8 Tuning | 10 | 2 | 1 | 4 | 5 |
| F9 Sensors | 6 | 3 | 1 | 5 | 4 |
| F10 Reliability | 11 | 4 | 2 | 4 | 5 |
| F11 Driver skill | 6 | 3 | 4 | 4 | 4 |
| F16 Rule exposure | 13 | 4 | 4 | **1** | 4 |
| **Σ (w×r)** | | **333** | **196** | **412** | **468** |
| **A** | | **67** | **39** | **82** | **94** |

- **D1 F5 = 2, F8 = 2.** HISTORICAL (Chief Delphi FTC 23511 DECODE OA thread, t/506155): first launcher
  prototypes were *"very inconsistent"*, and flexible gecko wheels performed **worse** than rigid ones. A
  fixed-angle launcher still has ~6 constants (flywheel RPM, compression, hood angle, feed dwell, spin-up time,
  voltage compensation) and they drift on a single battery (**R601**).
- **D2 F2 = 1.** Turret + auto-aim constants do not transfer between two robots; copy #2 is a full re-tune.
  **This alone vetoes D2 under MF5.**
- **D2 F11 = 4** — a genuinely non-obvious 4: auto-aim *reduces* driver burden. High ratings on the wrong axis
  do not save a candidate, which is the point of the min-factor veto.
- **D3 F16 = 1.** Its value depended on unbounded human-player handling and off-field storage — exactly the
  "resource FIRST has capped before" pattern. **G434 capped it 12 days after Kickoff.**

### 12.3 Axis V (design intent)

| # | w | **D1** | **D2** | **D3** pre-TU02 | **D3′** post-TU02 | **D4** |
|---|---:|:---:|:---:|:---:|:---:|:---:|
| V1 Scoring ceiling | 30 | 4 | 5 | 3 | 2 | 1 |
| V2 Match PPS | 25 | 4 | 5 | 3 | 2 | 1 |
| V3 Alliance desirability | 20 | 4 | 5 | 3 | 2 | 3 |
| V4 Defense resistance | 15 | 3 | 4 | **1** | **1** | 4 |
| V5 Phase & ranking leverage | 10 | 4 | 5 | 2 | 2 | 4 |
| **Σ (w×r)** | | **385** | **485** | **260** | **185** | **215** |
| **V** | | **77** | **97** | **52** | **37** | **43** |

- **D1 V1 = 4.** 3 pts × 30–40 artifacts ≈ 90–120 for one robot; the manual's own GOAL RP bar is **36 artifacts
  for an alliance** at ordinary events, so a robot that can put up 30+ alone is a solid second pick, not a star.
- **D2 V4 = 4.** A turret means you shoot from wherever you are — the clearest example in the corpus of
  fabrication complexity actually *buying* defense resistance.
- **D3 V4 = 1.** One opponent robot parks in the loading corner and zeroes it. HISTORICAL analogue, Chief Delphi
  t/519884 (FRC 2026): the identical argument against feeding human players — *the cheapest strategy to build was
  the cheapest strategy to defend.*
- **D4 V5 = 4.** This strategy is *entirely* phase leverage: LEAVE + BASE + the MOVEMENT RP, and DECODE's BASE
  bonus explicitly requires **both** alliance robots, which makes a guaranteed BASE-returner genuinely wanted.

### 12.4 Result vs what actually happened

| | D1 | D2 | D3 | D4 |
|---|---:|---:|---:|---:|
| A | 67 | 39 | 82 | 94 |
| V | 77 | 97 | 52 → **37** | 43 |
| Gates | pass (8 motors exactly) | pass **only** with a servo turret | **G7 trip → FLAG-2** | pass |
| Floor | clears | **fails MF2 (39) and MF5 (F2 = 1)** | **fails MF5 (F16 = 1)**; post-TU also fails MF3 | clears |
| Quadrant | **BUILD THIS** | **TRAP** | SAFE FLOOR (held) | SAFE FLOOR |

**What actually happened.**

- **VERIFIED-WEB (fetched 2026-08-21, `community.firstinspires.org/congratulations-to-our-decode-first-championship-teams`):**
  the DECODE FIRST Championship **Winning Alliance** was **30030 Exodus**, **21087 Velocity**, **11228 OverClucked
  Bots**; the **Finalist Alliance** was **18270 RoboPlayers**, **20265 Heart of RoBots**, **7172 Technical
  Difficulties**; the Championship **Inspire Award** went to **17792 Amigos Droids**.
- **CONFIRMED from the manual itself:** the GOAL RP threshold of **36 CLASSIFIED artifacts at ordinary events**
  makes launching effectively mandatory to be competitive. A non-launcher alliance cannot reach it.
- **HISTORICAL, verified from the Team Updates:** the non-launcher strategy D3 was directly constrained by
  **G432/G433/G434** twelve days after Kickoff.

**Verdict: the rubric's V ranking matches the season.** D2 > D1 > D3 > D4 on Competitive Value — launcher over
non-launcher, exactly as the game's own RP threshold implies. And the rubric makes the *right recommendation for
this program*: **build a launcher, but the simple fixed-angle one** (D1, the sole BUILD THIS), not the turret
(D2, a TRAP at A = 39 with an F2 = 1 veto).

---

## 13. What calibration changed (and what it refused to change)

### 13.1 Where the Axis A weights came from

`ACHIEVABILITY-FACTORS.md` §6 weights over F1–F11 + F16 sum to **70** (the remaining 30 is the payoff cluster
that became Axis V). Renormalising ×100/70 and rounding gives a set that happens to sum to exactly 100, with a
maximum distortion of 0.4 weight points. Then two calibration adjustments:

| Factor | Parent w | ×100/70 | v1.0 | **v1.1 (this file)** | Change and why |
|---|---:|---:|---:|---:|---|
| F1 | 9 | 12.86 | 13 | **13** | — |
| F2 | 9 | 12.86 | 13 | **13** | — |
| F3 | 5 | 7.14 | 7 | **7** | — |
| F4 | 4 | 5.71 | 6 | **5** | **−1.** The parent file itself notes F4 is "partly buyable now" — POLLEN and the StarterBot Base are already published (CONFIRMED-PRESEASON), and **R304** makes pre-Kickoff fabrication legal |
| F5 | 4 | 5.71 | 6 | **6** | — |
| F6 | 3 | 4.29 | 4 | **3** | **−1.** The parent file already calls F6 the lowest-value factor for a program that lacks the hours to execute a reversal |
| F7 | 5 | 7.14 | 7 | **7** | — |
| F8 | 7 | 10.00 | 10 | **10** | — |
| F9 | 4 | 5.71 | 6 | **6** | — |
| F10 | 8 | 11.43 | 11 | **11** | — |
| F11 | 4 | 5.71 | 6 | **6** | — |
| F16 | 8 | 11.43 | 11 | **13** | **+2.** See §13.2 |
| | **70** | 100.0 | **100** | **100** | |

### 13.2 Mis-rank 1 (DECODE) — and why a weight change was **not** the fix

**The mis-rank.** On Kickoff day 2025, scoring **D3** (intake + hopper, feed the human player) with v1.0 weights
gives **A = 84** — the **highest achievability score of any DECODE candidate**, higher than the eventual correct
answer D1 (67) by 17 points. A team ranking on achievability alone, or on a composite dominated by build
factors, commits to D3 on Kickoff weekend. **Twelve days later G434 caps off-field storage at 6 artifacts and
the strategy is gone.**

**What did not work.** Raising F16 from 11 to 13 moves D3 from **84 to 82**. That is not a fix. No defensible
weight on a single factor can beat eleven other factors all scoring 4–5, and inflating F16 until it does would
make the rubric useless for every candidate that *isn't* a loophole.

**What did work — three structural changes:**

| Change | Effect on D3 |
|---|---|
| **Gate G7 (loophole / intent test)** — trips on unbounded use of a resource FIRST has capped in ≥2 prior seasons | Caps `V ≤ 40` and holds the candidate under FLAG-2 until TU02 is read |
| **FLAG-2 — report V as a range and decide on the worst case** | D3 is evaluated at V = 37, not V = 52 |
| **MF5 extended to include `F16 = 1`** | D3 fails the minimum viable floor outright, regardless of its A score |
| *(supporting)* **F16 weight 11 → 13** | Widens the gap between exposed and unexposed candidates for the *ordinary* case where F16 is 2 or 3 rather than 1 |

**Recorded honestly:** the weight change alone was insufficient and is retained only as a secondary effect. The
real lesson is that **rule-change exposure is a gate-shaped risk, not a deduction-shaped one** — the same reason
`ACHIEVABILITY-FACTORS.md` §8 mechanism 8 says fatal flaws must not be averageable.

### 13.3 Mis-rank 2 (INTO THE DEEP) — the anchor that was wrong

**The mis-rank.** With Axis V's original V2 anchor inherited from F12 — "points per second of match time consumed
by the action" — the **I3 endgame ascent specialist** scores V2 = 5 (30 points in ~10 seconds = 3 pts/s) and
V1 = 4 (the parent file's exemplar E4 is F12 = 4). That gives:

| | A | V (v1.0 anchors) | Quadrant (v1.0) |
|---|---:|---:|---|
| I3 ascent specialist | 81 | **84** | **BUILD THIS** |
| I1 specimen cycler | 79 | 90 | BUILD THIS |

Two BUILD THIS candidates, with I3 close behind I1 on value and *ahead* on achievability — so tie-break #1 for
the B robot ("higher A") hands the B team a robot that scores **30 points a match**. That is a bad recommendation
and the season says so: `SCORING-PATTERNS.md` §B.9 records ITD's endgame ceiling / top element ratio as **6.0**,
the second-lowest in the corpus, and the general finding that the 2020s endgame is *"a tiebreaker and a
'both robots must participate' cooperation gate, not a match-winner."*

**The fix — two anchor rules, no weight change (§5.1):**

| Rule | Effect on I3 |
|---|---|
| **V-a: V2 is match-averaged** (`points ÷ full match length`) | 30 / 150 s = 0.2 pts/s → **V2 = 1**, not 5 |
| **V1's 3-cap for once-per-match-only strategies** | V1 = 2 by the percentage anchor anyway; the cap makes it structural |
| *(also adopted)* **candidates must be whole-match strategies, not mechanisms** (§1 step 1) | An ascent mechanism can only appear as *part* of a candidate that fills the match |

Result: I3 drops from **V = 84 → V = 52**, out of BUILD THIS and into SAFE FLOOR. Correct.

**Rule V-b** (value does not track difficulty) came out of the same run: with a naive "impressive mechanism =
high payoff" instinct the I2 basket bot out-scores the I1 specimen bot on V1, contradicting the verified point
values (10 vs 8) and the verified cycle times.

### 13.4 Where the cut lines came from

The cuts were placed **after** the eight calibration candidates were scored, by looking for the gaps in the data.

| Cut | Value | What it separates | Gap in the data |
|---|---:|---|---|
| **A cut** | **65** | Candidates this program finishes twice, from candidates it does not | 52 / 67 — a 15-point gap with nothing in it |
| **V cut** | **55** | Strategies that can win a match, from strategies that cannot | 52 / 75 — a 23-point gap with nothing in it |
| **MF2 floor** | `A ≥ 55` | Below this, no candidate in either calibration season was buildable by this program | Both TRAPs sit at 52 and 39 |
| **MF3 floor** | `V ≥ 40` | Below this it is a fallback, not a candidate | Park-only = 32; the lowest surviving candidate = 43 |

**A caveat, stated plainly (JUDGMENT).** Cut lines fitted to eight retrospective candidates from two seasons are
a *calibration*, not a validation on held-out data. They should be re-checked against BIOBUZZ candidates after
the first qualifier (§15) and moved if the BIOBUZZ candidate set clusters differently.

### 13.5 Validation summary

| Check | Result |
|---|---|
| Does V rank the archetype families the way the seasons ranked them? | **Yes.** ITD: specimen 90 > basket 75 > ascent 52 > park 32 — matches §B.8 and the verified Worlds outcome. DECODE: turret launcher 97 > fixed launcher 77 > human-feed 52 > base/defense 43 — matches the manual's own 36-artifact GOAL RP bar |
| Does exactly one BUILD THIS emerge per season? | **Yes**, both times, and both times it is the **simplified variant of the family that actually won** |
| Does the rubric catch the classic small-team over-scope? | **Yes.** ITD tall basket bot → TRAP; DECODE turret launcher → TRAP |
| Does it catch the classic small-team under-scope trap (the "free" no-mechanism strategy)? | **Only after the §13.2 structural fix.** Before it, D3 topped the achievability axis |
| Does it catch the one-shot endgame trap? | **Only after the §13.3 anchor fix.** Before it, a 30-point-per-match robot was BUILD THIS |
| Spread achieved? | A range 39–100 (**61**), V range 32–97 (**65**). Both far above the §7 thresholds of 15 and 20 |
| Weakest link | The "what actually won" claims. Scoring tables and Team Update text are verified from the local corpus; the *meta* claims are one fetched team page, one fetched FIRST results page, and a sibling document's derived analysis. Treat outcome attribution as **JUDGMENT** |

---

## 14. A-team vs B-team variant

### 14.1 What changes and why

The B team is a registered team with its own robot, its own **A215** award slot and its own shot at a 60-point
Inspire (§4.1, CONFIRMED-BIOBUZZ). Its objective function is different: **finish a working robot, teach the
newer half of the program, and be the partner nobody regrets picking.** Peak scoring is not on the list.

| Factor | w(A) | **w(B)** | Δ | Why |
|---|---:|---:|---:|---|
| F1 Fabrication | 13 | **15** | +2 | The B build crew is the less experienced half of a 15-student program |
| F2 Duplicability | 13 | **10** | −3 | The B robot *is* copy #2 — much of this factor is already realised. It still counts, because A/B mechanisms are each other's drop-in spares (**I303.F**) |
| F3 Cost | 7 | **8** | +1 | The B robot is funded last and gets whatever is left |
| F4 Time-to-prototype | 5 | **8** | +3 | If the B robot is not driving early, the newer students disengage. This is the retention factor |
| F5 Time-to-reliable | 6 | **9** | +3 | Reliability *is* the B objective |
| F6 Iteration cost | 3 | **5** | +2 | B is the program's learning platform; being able to change your mind is the pedagogy |
| F7 Programming | 7 | **10** | +3 | The novice programmers are here. **I303.D** makes code the cheapest thing to change at an event |
| F8 Tuning | 10 | **8** | −2 | Still high, but B's targets should be chosen to be lower-precision in the first place |
| F9 Sensors | 6 | **5** | −1 | B should still touch sensors — Control §6.3.7 *requires* external feedback, and it is a realistic B-team award |
| F10 Reliability | 11 | **13** | +2 | The B objective, again |
| F11 Driver skill | 6 | **6** | 0 | B's drivers are novices, but practice is the point; free Skill Builders (CONFIRMED-PRESEASON) buy this down for both teams |
| F16 Rule exposure | 13 | **3** | **−10** | **The B robot should never be the one carrying rule risk.** If A is running an exposed strategy, B is the hedge. Nearly all of F16's weight is redistributed to F4/F5/F7 |
| **Σ** | 100 | **100** | | |

| Factor | w(A) | **w(B)** | Δ | Why |
|---|---:|---:|---:|---|
| V1 Scoring ceiling | 30 | **15** | −15 | B is not chasing the ceiling |
| V2 Match PPS | 25 | **20** | −5 | Still matters — a slow robot is still a bad partner |
| V3 Alliance desirability | 20 | **35** | **+15** | **B's entire competitive value is being picked and costing the alliance nothing.** §4.1 pays `21 − draft position` for accepting a draft slot |
| V4 Defense resistance | 15 | **15** | 0 | Unchanged: a B robot that one defender can zero is still worthless |
| V5 Phase & ranking leverage | 10 | **15** | +5 | AUTO leave, endgame position and ranking criteria are **bounded, practiceable, cheap** — the best value-per-hour available to a B team |
| **Σ** | 100 | **100** | | |

### 14.2 B-team-specific cuts, floor and tie-break

| Setting | A team | **B team** | Why |
|---|---|---|---|
| Quadrant cuts | `A ≥ 65`, `V ≥ 55` | **`A ≥ 70`, `V ≥ 45`** | B needs more achievability headroom and is allowed less competitive value |
| Minimum viable floor | MF2 `A ≥ 55`, MF3 `V ≥ 40`, MF4 `A+V ≥ 120` | **MF2 `A ≥ 65`, MF3 `V ≥ 35`, MF4 `A+V ≥ 115`** | Same shape, different balance |
| Quadrants permitted | BUILD THIS, or STRETCH GOAL with a written de-scope | **BUILD THIS or SAFE FLOOR only.** A STRETCH GOAL or TRAP is never assigned to the B robot | Decision rule §9.2 step 5 |
| Extra tie-break | — | Insert **Learning Yield (L)** at position 5, ahead of AY | See below |

**Learning Yield (L), B-team tie-break only** — score 1–5 on each, take the mean:

| Sub-question | 1 | 5 |
|---|---|---|
| How many students get a subsystem of their own? | One student owns everything | ≥ 4 distinct student-owned subsystems |
| Does it teach a skill that transfers to next season (**R304**: custom designs and parts carry over)? | Single-use novelty | Drivetrain / intake / sensor / state-machine skills that carry forward |
| Can a student explain the whole robot to a judge in 2 minutes? | No one understands all of it | Any team member can |

### 14.3 The same strategy, ranked for both robots

Re-scoring the DECODE candidates with the B column, on **identical ratings** — nothing about the robot changed,
only who is building it and why:

| Candidate | A-team A / V | A-team quadrant | **B-team A / V** | **B-team quadrant** |
|---|---:|---|---:|---|
| **D1** fixed-angle launcher | 67 / 77 | **BUILD THIS** | **66 / 77** | **STRETCH GOAL** (clears B floor: A 66 ≥ 65) |
| **D2** turret + auto-aim launcher | 39 / 97 | **TRAP** | **35 / 97** | **TRAP** (fails B MF2 by 30 points) |
| **D4** BASE-return + LEAVE + defense | 94 / 43 | SAFE FLOOR | **95 / 52** | **BUILD THIS** |

**Read the swap.** D1 and D4 trade places. The same fixed-angle launcher that is the A robot's primary design is
a *stretch* for the B robot, because B's weights price its `F5 = 2` and `F7 = 3` much more heavily. The same
BASE-return/defense robot that is merely the A team's fallback is the B team's **best available design**, because
`V3` — the only thing B's competitive value really consists of — is weighted 35 instead of 20, lifting it from
V = 43 to V = 52 and across the B cut.

**And this is the correct answer for the program**, for reasons outside the robot: it satisfies **G4/MF8** (two
robots, differentiated), it satisfies the `V3` anchor's requirement that A and B not contend for the same
resource (D1 shoots, D4 returns and defends), and it lets the two teams target **different awards** so they do
not compete for the same **A215** slot at the same event — the split `AWARD-CATALOG-BIOBUZZ.md` §6.4 and
`ACHIEVABILITY-FACTORS.md` §10 both recommend.

**HISTORICAL support (Chief Delphi t/406178, FRC):** the mentors of a two-team program reported they lacked the
bandwidth to supervise two separate designs, and the pattern that worked was the second team building a
**simplified variant of the same architecture** with a differentiated role. That is what a B-team reweighting is
for — it produces that answer arithmetically instead of by argument.

---

## 15. Re-run triggers

**Re-scoring is cheap; being wrong for six weeks is not.** A **delta re-score** touches only the affected factors
(10 min). A **full re-score** re-runs every column (45 min).

| Trigger | When | Scope | What to re-score |
|---|---|---|---|
| **Kickoff manual read** | 2026-09-12 | **Full** | Everything. Instantiate V1/V2 anchors from the real scoring table; instantiate V4 from the real protected-zone G-rules; resolve **FLAG-1** against the published **R105** |
| **Every Team Update, all season** | Every **Thursday** from Kickoff to two weeks before Championship (**CONFIRMED-BIOBUZZ §2**) | Delta | **F16** always; plus any gate or factor the changed rule touches. If a scoring value or a G-rule changed, escalate to full |
| **TU01 and TU02 specifically** | Expected Thu **2026-09-17** and **2026-09-24** | **Full** | HISTORICAL: DECODE published R105's expansion limits in TU01 (K+5) and capped off-field storage in TU02 (K+12). Every **FLAG-2** candidate is resolved here — this is the moment the held V range collapses to a number |
| **Mid-season nerfs are real too** | Any TU | Delta | HISTORICAL: ITD changed **G420** (ascent geometry) in TU03/TU04/TU05, six to eight weeks in, and narrowed **G427** (climbing protection) in **TU10, January 2025**. Do not stop re-scoring F16 in November |
| **Q&A opens** | **2026-09-28, 12:00 p.m. ET**; moderators answer Mon–Thu 17:00 ET | Delta | Log answers against your assumptions. **Q&A does not supersede the manual — REFEREES and INSPECTORS are the final authority (CONFIRMED-BIOBUZZ §2)**, so an answer is a hint, never a gate clearance |
| **First cycle-time measurement on a real field** | Whenever the field element exists | Delta | **V1 and V2** — replace estimated seconds with measured seconds. This is the single highest-value re-score in the season |
| **After the first qualifier / League Meet** | Same day | **Full** | Replace every estimate with a measurement: measured cycle times (V1/V2), observed success rate (F5, F10), observed driver rate (F11), observed match-winning score (the V1 denominator). Re-check the §13.4 cut lines against the BIOBUZZ candidate spread |
| **After seeing the regional meta** | After 2 events, or after any scouting data dump | Delta | **V3** (what are captains actually picking here?) and **V4** (is anyone playing defense at this level?). `research/SCOUTING-AND-AWARDS.md` supplies the data collection |
| **Any mid-season ranking-criterion recalibration by FIRST** | If announced | Delta | **V5.** HISTORICAL: FIRST recalibrated DECODE's RP thresholds mid-season from live match data |
| **A mechanism misses its build deadline by > 2 weeks** | Immediately | Delta | **F4, F5** — then execute the de-scope. This is what the kill date is for |
| **Any inspection failure or referee ruling against you** | Same event | Delta | The relevant **gate**, plus **F16**. A ruling is evidence your reading of a rule was wrong |
| **Award feedback from judges** | After each event | Delta | **AY1–AY3** only. Never let award feedback move an A or V rating |

**Freeze rule.** Stop re-scoring **two weeks before your first qualifier** and execute. After the freeze, Team
Updates are read for *compliance* (does the robot still pass inspection? does a G-rule now penalise what we do?)
and **not** for re-ranking. A rubric consulted during the last two weeks of build is a procrastination device.

**Version the sheet.** Every re-score gets a date and a one-line reason. The set of dated sheets is directly
usable as Think §6.3.2 "comparing choices" evidence and Innovate §6.3.6 "how design risks were reduced" evidence
— and **A201** permits AI assistance in the portfolio **provided a footnote or endnote credit is included**
(CONFIRMED-BIOBUZZ, Section 6). If this rubric shaped a portfolio decision, credit it.

---

## 16. Machine-readable model

```yaml
model: BIOBUZZ-ACHIEVABILITY-RUBRIC
version: 1.1
authored: 2026-08-21
derives_from: reference/ACHIEVABILITY-FACTORS.md v1.0
calibrated_on: [2024-25_INTO_THE_DEEP, 2025-26_DECODE]
calibrated_for: {students: 15, robots: 2, teams: [A, B],
                 fabrication: [cots, 3d_printing, hand_tools],
                 excluded_fabrication: [cnc_mill, lathe, waterjet, welding],
                 budget: modest, mentor_hours: limited}
scale: {min: 1, max: 5, unknown: U, direction: "5 is always favorable"}
axis_independence: "V is scored at design intent; A carries all execution risk. Never discount V for reliability."
formulas:
  A:  "sum(wA_i  * rating_i) / 5"      # F1..F11, F16
  V:  "sum(wV_j  * rating_j) / 5"      # V1..V5
  AY: "sum(wAY_k * rating_k) / 5"      # AY1..AY3
  composite: null                      # deliberately absent

gates:
  - {id: G1, name: legality,             action: reject}
  - {id: G2, name: actuator_budget_R503, action: reject_or_rescope, limit: {motors: 8, servos: 8}}
  - {id: G3, name: fabrication_floor,    action: reject_unless_named_vendor, on_survive: {F1: 1}}
  - {id: G4, name: two_robot_feasibility,action: reject_unless_descoped_B_variant_scored_separately}
  - {id: G5, name: cash_ceiling,         action: reject_or_rescope, price: both_robots}
  - {id: G6, name: pneumatics_R801,      action: reject}
  - {id: G7, name: loophole_intent_test, action: cap_V_at_40_and_flag2, added_by: calibration_DECODE}
flags:
  FLAG1: {on: "depends on R105 sizing or Sections 8-11/13/15", action: score_and_rescore_after_kickoff}
  FLAG2: {on: "G7 tripped", action: "report V as range; decide on worst case until TU02"}

axis_A:   # weights sum to 100 in each column
  - {id: F1,  name: fabrication_complexity,   polarity: inverted, wA: 13, wB: 15}
  - {id: F2,  name: duplicability_A_B,        polarity: direct,   wA: 13, wB: 10}
  - {id: F3,  name: bom_and_spares_cost,      polarity: inverted, wA:  7, wB:  8}
  - {id: F4,  name: time_to_first_prototype,  polarity: inverted, wA:  5, wB:  8}
  - {id: F5,  name: time_to_reliable,         polarity: inverted, wA:  6, wB:  9}
  - {id: F6,  name: iteration_cost,           polarity: inverted, wA:  3, wB:  5}
  - {id: F7,  name: programming_burden,       polarity: inverted, wA:  7, wB: 10}
  - {id: F8,  name: tuning_burden,            polarity: inverted, wA: 10, wB:  8}
  - {id: F9,  name: sensor_vision_dependence, polarity: inverted, wA:  6, wB:  5}
  - {id: F10, name: match_reliability,        polarity: direct,   wA: 11, wB: 13}
  - {id: F11, name: driver_skill_practice,    polarity: inverted, wA:  6, wB:  6}
  - {id: F16, name: rule_change_exposure,     polarity: inverted, wA: 13, wB:  3}

axis_V:
  - {id: V1, name: scoring_ceiling,        wA: 30, wB: 15, cap_if_once_per_match: 3}
  - {id: V2, name: match_points_per_second,wA: 25, wB: 20, denominator: full_match_length}
  - {id: V3, name: alliance_desirability,  wA: 20, wB: 35}
  - {id: V4, name: defense_resistance,     wA: 15, wB: 15}
  - {id: V5, name: phase_ranking_leverage, wA: 10, wB: 15}

award_yield:
  - {id: AY1, name: evidence_generation, w: 50}
  - {id: AY2, name: demonstrability,     w: 30}
  - {id: AY3, name: criteria_fit,        w: 20}
  usage: "tie-break #5 and input to AWARD-ALIGNMENT-MATRIX.md; never a ranking term"

quadrants:
  A_team: {cut_A: 65, cut_V: 55}
  B_team: {cut_A: 70, cut_V: 45}
  names: {high_A_high_V: BUILD_THIS, low_A_high_V: STRETCH_GOAL,
          high_A_low_V: SAFE_FLOOR,  low_A_low_V: SKIP}
  trap_overlay: "any candidate with V >= cut_V that fails the minimum viable floor"

minimum_viable_floor:
  A_team: {MF2_min_A: 55, MF3_min_V: 40, MF4_min_sum: 120}
  B_team: {MF2_min_A: 65, MF3_min_V: 35, MF4_min_sum: 115}
  MF1: "all gates pass (G7 may be held under FLAG-2)"
  MF5_veto_rating_1_on: [F1, F2, F3, F10, F16]
  MF6: {max_U_on_A: 2, max_U_on_V1_V2: 0}
  MF7: "optimistic (U->4) and pessimistic (U->2) rankings agree on rank 1"
  MF8: "a de-scoped B variant exists and is scored as its own candidate"
  MF9: "at least one scoring action is performable without an alliance partner"
  MF10: [R102_18in_cube, R503_8_motors_8_servos, R601_one_battery, R801_no_pneumatics]

tie_breakers: [higher_V_for_A_robot__higher_A_for_B_robot, fewer_U, higher_F2, higher_F16,
               higher_AY, higher_F4, has_written_fallback, prototype_one_week_and_remeasure]
b_team_extra_tiebreak: {position: 5, name: learning_yield_L}

spread_warning: {A_range_min: 15, V_range_min: 20}
freeze: "stop re-scoring 2 weeks before the first qualifier"

calibration_results:
  ITD_2024_25:
    - {code: I1, name: high_chamber_specimen_cycler, A: 79, V: 90, quadrant: BUILD_THIS}
    - {code: I2, name: high_basket_two_stage,        A: 52, V: 75, quadrant: TRAP, fails: [MF2]}
    - {code: I3, name: endgame_ascent_specialist,    A: 81, V: 52, quadrant: SAFE_FLOOR}
    - {code: I4, name: cots_park_only,               A: 100, V: 32, quadrant: SAFE_FLOOR, fails: [MF3]}
  DECODE_2025_26:
    - {code: D1, name: fixed_angle_flywheel_launcher, A: 67, V: 77, quadrant: BUILD_THIS}
    - {code: D2, name: turret_vision_launcher,        A: 39, V: 97, quadrant: TRAP, fails: [MF2, MF5_F2]}
    - {code: D3, name: intake_hopper_human_feed,      A: 82, V: [52, 37], quadrant: SAFE_FLOOR,
       gates_tripped: [G7], flags: [FLAG2], fails: [MF5_F16]}
    - {code: D4, name: base_return_leave_defense,     A: 94, V: 43, quadrant: SAFE_FLOOR,
       b_team: {A: 95, V: 52, quadrant: BUILD_THIS}}

rerun_triggers: [kickoff, every_thursday_team_update, TU01, TU02, qa_open_2026_09_28,
                 first_measured_cycle_time, after_first_qualifier, after_regional_meta_scouting,
                 rp_threshold_recalibration, build_deadline_slip_2wk, inspection_or_referee_ruling,
                 judge_award_feedback_AY_only]
```

---

## 17. Divergences from `ACHIEVABILITY-FACTORS.md`, and known gaps

### 17.1 Deliberate divergences

| # | Divergence | Justification |
|---|---|---|
| **1** | **No single composite score.** The parent file's `score = Σ(w×r)/5` over 16 factors is replaced by two independent axes | §2. The composite fixes an exchange rate between payoff and buildability that the team never agreed to, and hides the three-way decision (A robot / B robot / fallback) |
| **2** | **F12 is split** into V1 (ceiling) and V2 (match PPS), and **V2 is match-averaged** | §5.1 Rule V-a. Calibration §13.3: the un-split, action-averaged version ranks a 30-point-per-match ascent specialist as BUILD THIS |
| **3** | **V is scored at design intent**, not "at realistic success rate" as the parent F12 anchor says | §2.1. The realism discount is F5/F8/F10/F11 on Axis A; applying it twice collapses the plot onto its diagonal |
| **4** | **F15 (award generation) is removed from the ranking** and reported as AY | §6. A strategy must never out-rank a better one because it tells a better story; the award criteria themselves (Innovate §6.3.6 criterion 3, Design §6.3.8) presuppose a working robot |
| **5** | **Gate G7 and FLAG-2 added**; **MF5 extended to F16 = 1** | §13.2, forced by the DECODE calibration |
| **6** | **F4 6→5, F6 4→3, F16 11→13** (post-renormalisation) | §13.1–13.2. Reported honestly as *insufficient on its own* |
| **7** | **Spread threshold raised** from 10 (one composite) to 15 on A and 20 on V | §7. Two axes of 12 and 5 factors should separate further than one of 16 |
| **8** | High-A/low-V quadrant named **SAFE FLOOR**, not "Skip" | §8.1. A two-robot program's B robot and fallback plan both live there |

### 17.2 Known gaps

| Item | Status |
|---|---|
| BIOBUZZ scoring values, field layout, G-rules, AUTO/endgame structure | **Deferred to Kickoff** (V0 §8–11, 13 and 15 are placeholders). V1, V2, V4 and V5 anchors are *shapes*, not numbers, until 2026-09-12 |
| **R105** sizing/expansion constraints for BIOBUZZ | **Deferred to Kickoff.** DECODE's version (18×18 horizontal, 18/38 in. vertical, mechanically constrained) is HISTORICAL precedent only. Every extension-dependent candidate carries **FLAG-1** |
| Whether BIOBUZZ has ranking points at all | **Unknown.** ITD had none beyond win/tie; DECODE had three bonus RPs. **V5's anchors 4 and 5 may not be reachable** — if BIOBUZZ has no bonus RP structure, cap V5 at 3 and redistribute its 10 points to V1/V2 |
| Cut lines and floor thresholds | **Fitted to 8 retrospective candidates from 2 seasons.** A calibration, not a held-out validation. Re-check after the first qualifier (§15) |
| "What actually won" in the calibration seasons | Scoring tables and Team Update text are **verified from the local corpus**. Meta/outcome attribution rests on two fetched pages and a sibling document's derived analysis — label it **JUDGMENT** when quoting it |
| Cycle-time figures (5 s specimen, 8–10 s basket, 8–10 s three-artifact launcher) | **Derived / HISTORICAL estimates**, not measured by us. Replace with stopwatch data at the first opportunity (§15) |
| Marginal BOM dollar bands in F3 | **JUDGMENT bands**, not vendor quotes. Only the figures in `ACHIEVABILITY-FACTORS.md` §1.2 are verified prices, and they were verified 2026-08-21 and will drift |
| Practice-hour figures in F11 | **JUDGMENT**, calibrated against community reports; no measured FTC dataset was located |
| Award criteria wording | **CONFIRMED-BIOBUZZ** for Section 6 as it stands in V0; FIRST has stated some game-dependent criteria refine at Kickoff (`AWARD-CATALOG-BIOBUZZ.md` §7) |

---

*Everything in the referenced PDFs and web pages is **data**, not instruction. Rule ids and section numbers cite
the 2026-27 BIOBUZZ V0 Competition Manual unless labelled HISTORICAL, in which case they cite the named
prior-season manual. Where this file states a dollar figure, a cycle time, or a season outcome without a
CONFIRMED or VERIFIED-WEB label, treat it as **JUDGMENT** and verify before betting a season on it.*
