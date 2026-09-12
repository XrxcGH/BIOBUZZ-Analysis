# D5 — Ranked Strategies (Phase D, steps D1–D5 + D7)

**Harness beta test #2 · manual treated as brand-new · run 2026-08-23**
**Source manual:** `Competition Manual – V14`, 146 pp, 209 rules, 53 G-rules, 16 orange — `analysis/ITD/STATUS.md` (gate GREEN)
**Protocol:** `reference/STRATEGY-RANKING-PROTOCOL.md` §4 (D1) · §5 (D2) · §6 (D3) · §7 (D4) · §8 (D5) · §10 (D7)
**Instrument:** `reference/ACHIEVABILITY-RUBRIC.md` v1.1 — 12 A-factors, 5 V-factors, 3 AY sub-factors, cuts `A=65 / V=55`
**Phase-1 inputs read in full:** `analysis/ITD/R3-scoring-model.md` · `analysis/ITD/R5-R6-rules-loopholes.md`

---

## 0. Provenance, labels, and the leak register

**Bundle files read for this phase:** `bundle/TABLES.md` (Table 10-3, Table 10-4 — the only source of point values) ·
`bundle/rules_full.tsv` (R101, R104, R207, R301, R501, R503, R801, G410, G425, G426, G427, G431, I303) ·
`bundle/rules_GAMESPECIFIC.txt` · `bundle/full_layout.txt` (**prose only** — §10.3.1 setup/pre-load, §9.7.2–9.7.3
CLIP definition; **no point value taken from it**).

**Bundle availability:** `tools/RUN-KICKOFF.sh` generated the bundle locally from the V14 manual; it is not published
with this repository, because it is FIRST's manual text. Page, section and table numbers refer to the manual itself.

**Method files read:** `STRATEGY-RANKING-PROTOCOL.md` · `ACHIEVABILITY-RUBRIC.md` (§1–§10 and §14 only) ·
`ACHIEVABILITY-FACTORS.md` §8 · `mechanisms/EXTENSION-ARMS-LIFTS.md` · `mechanisms/INTAKE-AND-MANIPULATION.md`.

**Refused (answer key), none opened:** `reference/SCORING-PATTERNS.md` · `research/LOOPHOLE-CASEBOOK.md` ·
`reference/ROBOT-ARCHETYPE-LIBRARY.md` · `reference/PENALTY-AND-ENFORCEMENT.md` · `research/SCOUTING-AND-AWARDS.md` ·
`manuals/_reference_prior_seasons/` · `manuals/archive/`.

### 0.1 Labels

| Label | Meaning |
|---|---|
| `[MANUAL]` | Read out of the bundle. Cites a rule id or table number. |
| `[DERIVED]` | Arithmetic or logic on `[MANUAL]` facts. Operands shown (rule H3). |
| `[JUDGMENT]` | My estimate. No manual authority. Argue with it. |
| `[UNVERIFIED]` | The bundle does not answer it. Never invented; goes to the Q&A queue. |

### 0.2 LEAK REGISTER — allowed method files that contain this season's answers

Three of the five method files I was permitted to read contain worked analysis **of the game under test**. I read
them before I knew what they held. **I have not used any of the numbers below**; every score in this file is
re-derived from the bundle, and where my independent result lands near a leaked one I say so explicitly.

| # | Leak | Source (an **allowed** file) | What I did |
|---|---|---|---|
| **L4** | The complete ITD calibration plot: `I1 high-chamber specimen cycler A=79 V=90 BUILD THIS` · `I2 high-basket sample bot A=52 V=75 TRAP` · `I3 endgame ascent specialist A=81 V=52 SAFE FLOOR` · `I4 park-only A=100 V=32 SAFE FLOOR` | `ACHIEVABILITY-RUBRIC.md` §8 and §8.1 | **This is the entire answer to D5.** I scored all 11 candidates cell-by-cell from the bundle before comparing. My independent results (C1 76/83, C3 57/77, C7 82/58, C11 100/29) land *close* to the leaked four — which is either validation or contamination and **I cannot tell which**. Treat this run's D5 result as **unusable as evidence that the harness works**. |
| **L5** | A fully worked ITD anti-flatness example: candidates `S1 short-arm specimen scorer / S2 tall extension + bucket / S3 endgame ascent`, with per-factor ratings (`S2 F1=2, F2=2, F8=2`) and the conclusion *"the flat rubric had ratified the most impressive-looking robot"* | `ACHIEVABILITY-FACTORS.md` §8.1 | Names the three candidates **and their factor scores**. I derived F1/F2/F8 for C3 from `mechanisms/EXTENSION-ARMS-LIFTS.md` §3.8/§3.10/§10.1 (kit cost, build hours, duplicability index) and got **3/3/2**, not 2/2/2. The disagreement is logged at §4.6 D-3 and it is load-bearing. |
| **L6** | "HIGH CHAMBER = 10 pts reachable with a short lift; HIGH BASKET = 8 pts needed a tall two-stage extension. The taller mechanism was worth less per action *and* slower." | `ACHIEVABILITY-RUBRIC.md` §5.1 Rule V-b | Pre-announces R3's FINDING 1 and this file's rank 1. Both point values are independently in `TABLES.md`; both heights are independently in §9.5.1/§9.6, so I cite those — but the *conclusion* was on the page before I arrived. |

`[JUDGMENT]` I also have background recollection of how this season played out. **I did not use it.** Where I
noticed I knew something I had not read in the bundle, I stopped and either derived it or marked it `[UNVERIFIED]`.

### 0.3 Assumption register (rule H4) — every assumed number, and what falsifies it

| # | Assumption | Value | Label | Falsified by |
|---|---|---:|---|---|
| A1 | Match play length | 150 s (AUTO 30 + TELEOP 120; the 8 s transition is dead time) | `[MANUAL]` §10.4, Glossary | — |
| A2 | Realistic drive speed | 43 in/s (312 RPM × 96 mm wheel × 0.7) | `[DERIVED]` R3 §3.1 | A stopwatch on a real chassis |
| A3 | `t_startup` | 4 s | `[JUDGMENT]` | Video of a real match start |
| A4 | Pessimism multiplier on every un-stopwatched cycle | × 1.3 | protocol §6.2 (mandated) | A `[MEASURED]` cycle |
| A5 | ASCENT LEVEL 2 time cost | 12 s | `[JUDGMENT]` R3 §3.3 | Bench test |
| A6 | ASCENT LEVEL 3 time cost | 20 s | `[JUDGMENT]` R3 §3.3 | Bench test |
| A7 | **S_win**, a typical winning ALLIANCE score | **150** | `[ESTIMATED]` — §3.4, protocol §6.5 **rank 3** | The median winning score at our first event. The single highest-value re-score of the season. |
| A8 | AUTO-scored elements are **counted once**, not re-counted at the end of TELEOP | single-count | `[JUDGMENT]`, deliberately conservative | R3 §2.2 / R5-R6 **F1** — genuinely `[UNVERIFIED]`. Q&A #1. **Every V in this file is scored on the pessimistic reading, so a "yes" can only help.** |
| A9 | Build capacity | ~9 h/week on one subsystem | `[JUDGMENT]` (15 students, two teams, 3 × 3 h meetings) | The actual meeting calendar |
| A10 | Cash ceiling for two robots | **`[UNVERIFIED]`** | — | `research/SMALL-TEAM-ECONOMICS.md` is **not on this run's allowed list**, so gate **G5 could not be evaluated**. Beta feedback #4. |

---

## 1. D1 — The candidate slate (MECE, contrarians included)

### 1.1 The morphological box, filled from Table 10-3

`[MANUAL]` Table 10-3 has **five uncapped repeatable rows** and **four capped position rows**, and — critically —
**no multiplier row, no set-completion row, no coopertition row and no threshold RANKING POINT** (R3 §1.2).

| Axis | Values available this season | Source |
|---|---|---|
| **G-a Revenue line** | SAMPLE→NET ZONE **2** · SAMPLE→LOW BASKET **4** · SAMPLE→HIGH BASKET **8** · SPECIMEN→LOW CHAMBER **6** · SPECIMEN→HIGH CHAMBER **10** · capped bonus set (PARK 3 / ASCENT L1 3, L2 15, L3 30) · none (support role) | `TABLES.md` Table 10-3 |
| **G-b Period emphasis** | AUTO-heavy · TELEOP-continuous · last-30 s one-shot · balanced | §10.4; there is **no named ENDGAME** (R3 §1.1) |
| **G-c Acquisition path** | SUBMERSIBLE field pickup · own OBSERVATION ZONE / human-player feed · SPIKE MARK pickup · pre-load only · none. **Taken from the opponent is illegal** — G411 (MINOR per element + MINOR per element per 5 s + MAJOR per element scored) | §10.3.1; G410/G411/G431 |
| **G-d Delivery location** | floor (NET ZONE, 0 in) · 13.0 in (LOW CHAMBER) · 20.0 in (LOW RUNG) · 25.75 in (LOW BASKET lip) · 26.0 in (HIGH CHAMBER) · 36.0 in (HIGH RUNG) · 43.0 in (HIGH BASKET lip) · a zone (OBSERVATION ZONE) | §9.5.1, §9.5.2, §9.6, Glossary |
| **G-e Volume vs value** | many cheap (2/3/4 pt) actions · few expensive (8/10/15/30 pt) actions | Table 10-3 |
| **G-f Role** | primary scorer · secondary / feeder · denial · position specialist | — |

**Walk rule applied.** One candidate per G-a value, then a **second** candidate for the two highest-value G-a rows
differing on G-c or G-d: HIGH CHAMBER gets **C1** (human-player-fed loop) and **C2** (on-board conversion); the
HIGH BASKET's second variant is the same acquisition path at a different delivery height and is carried as **C5**.

**RP note `[DERIVED]`.** The protocol's G-a value *"clear the RP threshold"* **does not exist this season.**
Table 10-3's RANKING POINTS column has exactly two rows — Tie = 1 and Win = 2 (R3 §5.1). There is no RP-farming
candidate to enumerate, and that is a MECE **pass**, not an omission.

### 1.2 The slate — 11 candidates

| Id | Strategy statement (whole-match; no mechanism nouns) | G-a | G-b | G-c | G-d | G-e | G-f | X | Filters |
|---|---|---|---|---|---|---|---|---|---|
| **C1** | Convert our own ALLIANCE-coloured elements at our protected loading zone and hang them on the tall centre bar all match; hang on the low bar at the end; attempt no tall container. | HIGH CHAMBER 10 | TELEOP-continuous + drilled AUTO | own zone + SPIKE MARK ferry | 26.0 in | few expensive | primary | — | pass |
| **C2** | Same revenue line, but convert elements where we find them so we never make the loading-zone trip. | HIGH CHAMBER 10 | TELEOP-continuous | field pickup, on-board conversion | 26.0 in | few expensive | primary | — | **G7 trip → FLAG-2** |
| **C3** | Take any element from the centre structure and place it in the tall container in our corner, all match. | HIGH BASKET 8 | TELEOP-continuous | field pickup | 43.0 in | few expensive | primary | — | pass |
| **C4** | Convert our own elements at our protected loading zone and hang them on the **low** centre bar, more times, from a shorter reach. | LOW CHAMBER 6 | TELEOP-continuous | own zone | 13.0 in | many cheap | primary | **X1** | pass |
| **C5** | Take any element from the centre structure and place it in the **low** container in our corner. | LOW BASKET 4 | TELEOP-continuous | field pickup | 25.75 in | many cheap | primary | — | pass |
| **C6** | Take any element from the centre structure and put it on the floor of our own scoring corner, as many times as possible; touch nothing tall. | NET ZONE 2 | TELEOP-continuous + cheap AUTO | field pickup | floor | many cheap | primary | **X7** | pass |
| **C7** | Build nothing that repeats. Cross the field once at the end and take the highest position achievement available. | ASCENT L3 30 | last-30 s one-shot | none | 36.0 in | one expensive | position | **X2** | pass |
| **C8** | Spend the season's engineering hours on the 30-second routine; play a deliberately minimal TELEOP. | HIGH CHAMBER 10 | AUTO-heavy | own zone | 26.0 in | few expensive | primary | **X3** | pass |
| **C9** | Score nothing. Remove the opponent's cycles by occupying their lanes and pinning inside the legal count. | none | balanced | none | none | — | denial | **X4** | gates pass, **MF5 veto** |
| **C10** | Score nothing directly. Ferry our own ALLIANCE-coloured elements from the centre structure to our loading zone so the human player converts them for a partner. | none | TELEOP-continuous | field pickup | own zone | many cheap | feeder | **X5** | **G7 trip → FLAG-2** |
| **C11** | Leave the wall, park in our zone in both periods, do nothing else. | PARK 3 | balanced | pre-load only | a zone | — | filler | **X6** | pass (control) |

### 1.3 MECE check (protocol §4.5)

| Test | Result |
|---|---|
| **Collectively exhaustive** | All five uncapped repeatable rows are the primary revenue line of ≥1 candidate: NET ZONE→C6 · LOW BASKET→C5 · HIGH BASKET→C3 · LOW CHAMBER→C4 · HIGH CHAMBER→C1/C2/C8. All four capped position rows appear: PARK→C11 (and every candidate's AUTO) · ASCENT L1→C8 · L2→C1/C3/C4/C5/C6/C10 · L3→C7. ✅ |
| **Mutually exclusive** | No two candidates share a `(G-a, G-c, G-b)` triple. C1/C2 differ on G-c; C1/C8 differ on G-b. ✅ |
| **Contrarian coverage** | X1=C4 · X2=C7 · X3=C8 · X4=C9 · X5=C10 · X6=C11 · X7=C6. All seven present. ✅ |
| **Size** | **11, over the 7–10 band.** `[DERIVED]` The band cannot be met this season: 5 uncapped repeatable rows force 5 revenue candidates, the 7 mandatory contrarians add 4 more not already covered, and the walk rule adds 2. **Deviation recorded rather than merged** — merging would delete a real distinction. Beta feedback #2. |

**Deleted before scoring (filter F-legal, with rule ids):**
- *"Take elements out of the opponent's basket and re-score them."* — **G412: MAJOR FOUL (15) per element
  de-scored**, against a HIGH BASKET worth 8 (R5-R6 §A5.1). Never profitable.
- *"Deliberately draw a G427 contact in the opponent's ASCENT ZONE for the 45-point swing."* — **G210**
  (*"actions clearly aimed at forcing the opponent ALLIANCE to violate a rule"*); R5-R6 §B4 classes it category (c).

---

## 2. D2 — Mechanism shape, described from the bundle

> **Protocol deviation, recorded.** `STRATEGY-RANKING-PROTOCOL.md` §5 maps candidates onto
> `ROBOT-ARCHETYPE-LIBRARY.md` §2 / §3.1–3.11, which is on this run's forbidden list. **D2 as written cannot be
> run from the bundle.** Substitute method, season-agnostic: describe each candidate's shape as
> `(acquisition, delivery height, actuation, actuator count, duplicability driver)` from the ARENA geometry in the
> bundle plus the BUY/FABRICATE tables in the allowed `reference/mechanisms/*.md`. Every row below is my own
> description; **no library row id is used anywhere in this file.**

| Id | Acquisition shape | Delivery shape | Actuation | Motors / servos (limit **8 / 12**, R503) | Duplicability driver |
|---|---|---|---|---|---|
| **C1** | Grip one element at floor level in our own OBSERVATION ZONE (36.6 × 13.1 in, G426-protected); occasionally take a SPIKE MARK element one tile away | Hook a clipped element over a **1.05 in dia, 26.5 in wide** bar at **26.0 in**. One forgiving axis; gravity finishes the placement | Pivoting arm on one motor (5203 @ 71.2:1) + one servo claw + a separate winch/hook for the climb | 4 drive + 1 arm + 1 winch = **6/8**; 1–2 servos | All catalogue SKUs + print files. `EXTENSION-ARMS-LIFTS.md` §10.1 rates *motor + planetary arm* and *simple winch climb* at **5**; the arm's two preset angles cost one tuning pass per robot |
| **C2** | C1's arm and claw, plus a magazine of CLIPS and an actuator that mates a CLIP to a SAMPLE **on the robot** | Same 26.0 in bar — and because the CHAMBERS sit on the SUBMERSIBLE itself, acquisition and delivery are inches apart instead of 60 in | C1 + a bespoke printed clip magazine and feed | 7/8 motors, 3–4 servos | The clipper is fitted to CLIP geometry (2.5 in high × ~3.2 in, §9.7.2) and needs per-robot hand-fitting |
| **C3** | Wide intake reaching into the SUBMERSIBLE ZONE (27.5 × 42.75 in, a 2 in barrier, RUNGS overhead at 20 in, up to four ROBOTS at once) | Tip a **3.5 in** element into an **8.85 × 5.5 in** opening whose lip is at **43.0 in** — two tight axes at the top of a mast | **≈48 in of usable travel from an 18 in starting cube (R101)** ⇒ a 3–4 stage cascade (`EXTENSION-ARMS-LIFTS.md` §3.10 "competitive", 4-stage Viper kit, cord-rigged) + a bucket tipper | 4 drive + 1 intake + 1–2 slide + 1 winch = **7–8/8** — the tightest budget on the slate | §10.1 rates a cord-rigged slide **4** and §3.10 warns *"rigging must be tensioned identically twice"*; the bucket adds a second alignment ⇒ **3** |
| **C4** | Identical to C1 | Hook over the **same 26.5 in wide bar** at **13.0 in** — the lowest non-floor target in the game. A fixed-angle arm to a hard stop reaches it | Servo arm (§5.10 rookie minimum, 1 servo) + claw + winch | 4 drive + 1 winch = **5/8**; 2 servos | §10.1 *servo arm* = **5**; zero empirical constants (hard stop) |
| **C5** | Same as C3 | Tip into the **same 8.85 × 5.5 in** opening, lip at **25.75 in** — half the height, stable short mast | Single-stage Viper 2-stage kit or a motor arm + tipper | 7/8 motors | Kit lift = **5**; the tipper adds one alignment step ⇒ **4** |
| **C6** | Same as C3 | **Zero lift.** §10.5.1: a SAMPLE scores in the NET ZONE when *"fully or partially inside"* it — a corner triangle 22.75 in along the wall. Drive up and release | Roller intake (`INTAKE-AND-MANIPULATION.md` §4.7 rookie minimum, ~8 h, ~$110) + open chute + winch | 4 drive + 1 intake + 1 winch = **6/8**; 0–1 servos | One motor, one printed chute, fixed compression, **no tuning constants** ⇒ **5** |
| **C7** | None | Hang the whole robot off the **44.5 in wide, 1 in dia HIGH RUNG at 36.0 in**, whole robot above 20.0 in (Table 10-2 condition **C** forces a two-stage climb for LEVEL 3 only) | Winch + rated cord (`REV-29-1244`, 1500 lb) + metal hook, two-stage | 4 drive + 1–2 winch = **5–6/8** | §10.1 *simple winch climb* = **5**; the two-stage transfer adds one alignment step |
| **C8** | Same as C1 | Same as C1 | C1's hardware; the product is the 30-second routine — dead reckoning or odometry, multi-state coordination with the human player | 6/8 motors | Hardware duplicates at 4; **odometry constants do not transfer between two chassis** ⇒ **3** |
| **C9** | None | None | COTS chassis + a **convex** front face (R5-R6 **F7**: a *flat or concave* face reads as CONTROL under the §16 glossary; convex reads as PLOWING) | 4/8 motors | One polycarbonate sheet cut twice ⇒ **5** |
| **C10** | Colour-discriminating intake in the SUBMERSIBLE (only 15 of the 60 elements there are ours, §10.3.1 F) | Drop into our own OBSERVATION ZONE for the human player | Roller intake + hopper, no lift | 5/8 motors | **5** on hardware, but the colour sensor *is* the mechanism |
| **C11** | None | Drive into a 36.6 × 13.1 in zone; §10.5.3 counts *"fully or partially inside"* | COTS chassis (R301) | 4/8 motors | **5** |

**Novelty test (protocol §5.2).** **C2 is the only genuinely novel pairing** — no other candidate converts a
SCORING ELEMENT into a *different* SCORING ELEMENT on board. §5.2 requires it to carry **F5 = U and F10 = U** into
D4 unless a prototype exists. None does; I rated 2 and 3 with written justifications instead and logged that as
deviation **D-2** (§4.6). C2 is discarded on other grounds, so the double-ranking is moot.

### 2.1 The C2 kill, computed before scoring `[DERIVED]`

C2's entire value is skipping the OBSERVATION ZONE trip, which requires starting the match with CLIPS aboard.
`[MANUAL]` §10.3.1, quoted in full:

> "From the SCORING ELEMENTS provided in D and E each ROBOT may be pre-loaded with either **1 SAMPLE or one
> SPECIMEN** such that it is in contact with the ROBOT and not in the OBSERVATION ZONE or NET ZONE. **SAMPLES or
> CLIPS not pre-loaded will remain in setup locations D and E.**"

The first sentence permits one SAMPLE **or** one SPECIMEN — not a magazine of CLIPS. The second says
"SAMPLES **or CLIPS** not pre-loaded", which reads as though CLIPS *can* be pre-loaded. **The manual contradicts
itself in consecutive sentences.** `[UNVERIFIED]` → Q&A. And the fallback route is closed: `[MANUAL]` **G431**
makes the HUMAN PLAYER the only actor who may introduce elements into the OBSERVATION ZONE, and there is no other
way onto the FIELD. **So without a legal pre-loaded magazine the robot must make the OBSERVATION ZONE trip to
collect every CLIP — exactly the trip C2 exists to avoid. C2 collapses into C1 plus extra hardware.**

---

## 3. D3 — Competitive Value (arithmetic; rule H3 governs this whole step)

### 3.1 Cycle times — decomposed into five terms, never guessed whole

From R3 §3.2. Protocol §6.2 requires every un-`[MEASURED]` `t_cycle` to be reported raw **and × 1.3**, and requires
**all downstream V-scoring to use the × 1.3 column** until a stopwatch replaces it.

| Cycle | pts | t_acq | t_out | t_align | t_deliver | t_back | **raw** | **× 1.3** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SPECIMEN → HIGH CHAMBER, human player has one staged | 10 | 1.5 | 1.4 | 1.0 | 2.0 | 1.4 | **7.3** | **9.5** |
| SPECIMEN → HIGH CHAMBER, ferrying a SPIKE MARK element first | 10 | — | — | — | — | — | **9.3** `[DERIVED]` 7.3+2.0 | **12.1** |
| SPECIMEN → HIGH CHAMBER, self-supplied from the SUBMERSIBLE | 10 | 2.5 | 1.4 | 1.0 | 6.5 | 1.4 | **12.8** | **16.6** |
| SPECIMEN → LOW CHAMBER, staged | 6 | 1.5 | 1.4 | 1.0 | 1.5 | 1.4 | **6.8** | **8.8** |
| SPECIMEN → LOW CHAMBER, self-supplied | 6 | — | — | — | — | — | **12.3** `[DERIVED]` 6.8+5.5 | **16.0** |
| SAMPLE → HIGH BASKET | 8 | 3.5 | 1.2 | 1.2 | 3.0 | 1.2 | **10.1** | **13.1** |
| SAMPLE → LOW BASKET | 4 | 3.5 | 1.2 | 1.0 | 2.0 | 1.2 | **8.9** | **11.6** |
| SAMPLE → NET ZONE | 2 | 3.5 | 1.2 | 0.3 | 0.5 | 1.2 | **6.7** | **8.7** |
| SPECIMEN → HIGH CHAMBER, converted **on board** (C2 only) | 10 | 3.5 | 0.5 | 1.0 | 3.5 | 0.5 | **9.0** `[JUDGMENT]` | **11.7** |
| Shuttle SUBMERSIBLE → own OBSERVATION ZONE (C10) | 0 | 3.5 | 1.4 | 0.3 | 0.5 | 1.4 | **7.1** `[JUDGMENT]` | **9.2** |

`[DERIVED]` The **+5.5 s self-supply penalty** is read off R3's own decomposition: `t_acq` +1.0 and `t_deliver` +4.5
(`12.8 − 7.3 = 5.5`). The same +5.5 applies to the LOW CHAMBER, because the extra work — fetch an ALLIANCE
SPECIFIC element from the SUBMERSIBLE and route it through the human player — is **identical at both heights**.
That single fact is what kills contrarian X1 in §3.3.

### 3.2 The AUTO ceiling, computed once and applied to every candidate

`[DERIVED]` **AUTO is 30 s and fits exactly two scoring actions per ROBOT.** The longest defensible AUTO on the
slate, C1's, decomposes as: hang the pre-load 4.0 + drive to the OBSERVATION ZONE 1.4 + take a SPIKE MARK element
2.0 + place it for the human player 1.0 + collect the clipped SPECIMEN 1.5 + drive to the CHAMBER 1.4 + align and
deliver 3.0 + return and PARK 1.4 = **16.7 s raw; × 1.3 = 21.7 s**. That leaves **8.3 s of margin against the 30 s
buzzer**, which matters: `[MANUAL]` **G403** upgrades from MINOR to **MAJOR FOUL** *"if actions result in a scoring
achievement"* after 0:30 (R3 §2.1). Target ≤ 27 s. A **third** action needs another 16.6 s and does not fit.

| Id | AUTO plan | Arithmetic | AUTO pts |
|---|---|---|---:|
| C1 / C2 / C8 | pre-load HIGH CHAMBER + one more + PARK | 10 + 10 + 3 | **23** |
| C3 | pre-load HIGH BASKET + one SPIKE MARK element + PARK | 8 + 8 + 3 | **19** |
| C4 | pre-load LOW CHAMBER + one more + PARK | 6 + 6 + 3 | **15** |
| C5 | pre-load LOW BASKET + one SPIKE MARK element + PARK | 4 + 4 + 3 | **11** |
| C6 | pre-load NET ZONE + **three** neutral SPIKE MARK elements (they sit on tiles B6/E1 in front of our own NET ZONE, R3 §4.1) + PARK | 2 + 2 + 2 + 2 + 3 | **11** |
| C7 / C9 / C10 / C11 | PARK only | 3 | **3** |

> **A result worth stating loudly `[DERIVED]`.** For C1, moving a SPECIMEN cycle out of TELEOP into AUTO is
> **point-neutral on match score** — the TELEOP cycle it displaces is worth the same 10. But it is **strictly
> positive on the ranking ladder**, because `[MANUAL]` Table 13-1's **2nd sort criterion is Average ALLIANCE AUTO
> Points** (R3 §5.2), and it **doubles** if assumption A8 is wrong. **AUTO is free ranking currency.**

### 3.3 Single-robot match contribution — one arithmetic block per candidate

All blocks use the **× 1.3 column**. `usable_teleop = 120 − t_startup 4 − one-shot time`.

**C1 — HIGH CHAMBER, own-zone loop, LEVEL 2 ASCENT.** Supply: the pre-load and one SPIKE MARK element are consumed
in AUTO, leaving 1 outside-wall + 2 SPIKE MARK elements on the short loop, then the SUBMERSIBLE.

```
usable_teleop = 120 − 4 − 12 (L2)                         = 104 s
  1 staged cycle    @  9.5 s =  9.5 s  →  1 × 10          =  10
  2 ferry cycles    @ 12.1 s = 24.2 s  →  2 × 10          =  20
  used 33.7 s;  remaining = 104 − 33.7                    = 70.3 s
  floor(70.3 ÷ 16.6) = 4 self-supplied  (4 × 16.6 = 66.4) →  40
P_teleop  = 10 + 20 + 40                                  =  70    (N = 7 cycles)
P_auto    = 23        P_oneshot = 15
P_robot   = 70 + 23 + 15                                  = 108
PPS_match = 108 ÷ 150                                     = 0.72 pts/s
```

*Raw (optimistic) column, same plan: `1×7.3 + 2×9.3 = 25.9` used, 78.1 remaining, `floor(78.1 ÷ 12.8) = 6` ⇒ N = 9,
P_teleop = 90, P_robot = 128, PPS = 0.85. **Decisions use 0.72.***

**C1 displacement test on the ASCENT `[DERIVED]`** (protocol §6.3.1 method — this is the test teams skip):
- *no climb:* `usable 116; 1×9.5 + 2×12.1 = 33.7; remaining 82.3; floor(82.3÷16.6)=4 ⇒ N=7; P = 70 + 23 = 93`
- *with L2:* **108. Δ = +15.**
- *with L3 (20 s):* `usable 96; remaining 62.3; floor(62.3÷16.6)=3 ⇒ N=6; P = 60 + 23 + 30 = 113. Δ = +20.`

**Both climbs pay. LEVEL 3 beats LEVEL 2 by 5 points and costs roughly three times the mechanism** — Table 10-2
condition **C** forces a two-stage climb for LEVEL 3 only, while LEVEL 2 accepts the LOW RUNG alone ("HIGH **and/or**
LOW RUNGS", R3 §6.4). **Build L2.**

**C2 — HIGH CHAMBER, on-board conversion.**
```
usable_teleop = 104 s ;  floor(104 ÷ 11.7) = 8 cycles (8 × 11.7 = 93.6)
P_teleop = 8 × 10 = 80 ;  P_auto = 23 ;  P_oneshot = 15
P_robot  = 118 ;  PPS = 118 ÷ 150 = 0.79 pts/s
```
**But G7 trips** (§4.1) on the §10.3.1 contradiction of §2.1. **FLAG-2: V capped at 40.**

**C3 — HIGH BASKET.**
```
usable_teleop = 104 s ;  floor(104 ÷ 13.1) = 7 cycles (7 × 13.1 = 91.7)
P_teleop = 7 × 8 = 56 ;  P_auto = 19 ;  P_oneshot = 15
P_robot  = 90 ;  PPS = 90 ÷ 150 = 0.60 pts/s
```
*Raw column: `floor(104 ÷ 10.1) = 10` ⇒ P_teleop 80, P_robot 114, PPS 0.76.* `[DERIVED]` **The mandated × 1.3
pessimism costs C3 three whole cycles (24 points) and costs C1 two (20 points) — the tall mechanism is the one that
loses most when you are honest about tuning time.**

**C4 — LOW CHAMBER (X1: ignore the headline objective).**
```
usable_teleop = 104 s
  1 staged @  8.8 =  8.8 s → 6   ;  2 ferry @ 11.4 = 22.8 s → 12  ;  used 31.6, remaining 72.4
  floor(72.4 ÷ 16.0) = 4 self-supplied (64.0) → 24
P_teleop = 6 + 12 + 24 = 42   (N = 7) ;  P_auto = 15 ;  P_oneshot = 15
P_robot  = 72 ;  PPS = 72 ÷ 150 = 0.48 pts/s
```
> **X1 is killed with a number `[DERIVED]`.** The LOW CHAMBER saves only **0.7 s per cycle** against the HIGH
> CHAMBER (8.8 vs 9.5 staged; 16.0 vs 16.6 self-supplied), because the cycle is dominated by **travel and
> acquisition, not by lift height** — the two targets are on the same structure, 13 inches apart. It gives up
> **4 points per cycle** to buy 0.7 s. `108 − 72 = 36 points of match score surrendered.` **"Go lower and cycle
> faster" does not work in a game where the low and high targets share one delivery trip.** X1 survives on
> Achievability (A = 85), not on Value.

**C5 — LOW BASKET.**
```
usable_teleop = 104 ;  floor(104 ÷ 11.6) = 8 cycles (92.8)
P_teleop = 8 × 4 = 32 ;  P_auto = 11 ;  P_oneshot = 15   →  P_robot = 58 ;  PPS = 0.39
```

**C6 — NET ZONE at maximum rate (X7: the cheapest repeatable, done perfectly).**
```
usable_teleop = 104 ;  floor(104 ÷ 8.7) = 11 cycles (95.7)
P_teleop = 11 × 2 = 22 ;  P_auto = 11 ;  P_oneshot = 15  →  P_robot = 48 ;  PPS = 0.32
```
> **C6's displacement test `[DERIVED]`.** Dropping the climb: `usable 116; floor(116 ÷ 8.7) = 13; P_teleop = 26;
> P_robot = 37`. **The 12-second climb costs 2 cycles (−4) and pays +15 ⇒ net +11.**
> ***Even the cheapest cycler in the game should climb.*** This is the highest-leverage single line of arithmetic
> in the file, and it is why both robots get the same hook.

**C7 — position only (X2).** `P_robot = AUTO PARK 3 + LEVEL 3 30 = 33 ; PPS = 33 ÷ 150 = 0.22`.
With LEVEL 2 instead: `3 + 15 = 18 ; PPS = 0.12`. **Rule V-a bites hard:** a 30-point action performed once is
**0.20 pts/s**, not 1.5.

**C8 — AUTO-maximiser (X3).** `P_robot = AUTO 23 + TELEOP 2 cycles 20 + L1 3 = 46 ; PPS = 0.31`.
> **X3 is killed with a number `[DERIVED]`.** The per-robot AUTO ceiling is **23 points** (§3.2) and it is capped by
> *the same OBSERVATION ZONE round trip* that caps TELEOP — 30 seconds fits exactly two actions, and a third needs
> 16.6 s that do not exist. So "autonomous-only" is **not a distinct strategy this season**: it is C1 with the same
> AUTO and a deliberately worse TELEOP, `46 vs 108 = −62 points`. Even if assumption A8 is wrong and AUTO
> re-counts, C8 rises to `46 + 20 = 66` against C1's re-counted 128 — still −62. **Carry the AUTO drilling into C1;
> do not build a robot for it.**

**C9 — denial (X4).** Direct scoring: `AUTO PARK 3 + TELEOP PARK 3 = 6`.
Denial credit `[JUDGMENT]`: blocking a lane without contact for ~30 s of an opponent's match ≈ 2 denied HIGH
CHAMBER cycles = 16. `Effective = 6 + 16 = 22 ; PPS = 22 ÷ 150 = 0.15`.
`[DERIVED]` **Contact-based denial is negative at every duration** (R5-R6 §A5.2): a 15-second pin costs
`4 MINOR × 5 = 20` under G423's stacking (the manual's own Table 10-6 worked example) and denies
`15 ÷ 12 × 10 = 12.5` ⇒ **−7.5**. At 5 s: costs 5, denies 4.2 ⇒ **−0.8**. And the three zones worth denying are
the three protected ones: **G425** NET ZONE, MAJOR per occurrence *regardless of who initiates*; **G426**
OBSERVATION ZONE, MINOR + MINOR per 5 s + MINOR per element touched; **G427** ASCENT ZONE in the last 30 s,
MAJOR **plus a free LEVEL 3 to the opponent = a 45-point swing.**

**C10 — shuttle / feeder (X5).** Direct: `AUTO PARK 3 + L2 15 = 18 ; PPS = 0.12`.
> **X5 is killed by pair arithmetic `[DERIVED]`.** Feeding drops a partner's cycle from 16.6 s to 9.5 s:
> `floor(104 ÷ 9.5) = 10 cycles ⇒ partner P_teleop = 100, P_robot = 100 + 23 + 15 = 138`.
> `Pair with a dedicated shuttle = 18 + 138 = 156.`  `Pair of two independent C1s = 108 + 108 = 216.`
> **The feeder costs the pair 60 points.** And it saturates: it can deliver 11 elements while the hanger converts
> 10, against a **lifetime supply of 20 ALLIANCE SPECIFIC SAMPLES** (R3 §1.6). **Do not build a feeder robot.**
> The loading-zone trip is shared work, not a job.

**C11 — the null control (X6).** `P_robot = 3 + 3 = 6 ; PPS = 6 ÷ 150 = 0.04`.
Every other candidate's margin over 6 **is** the value of the mechanism being proposed.

### 3.4 S_win — what a winning score looks like

Protocol §6.5 ranks the sources. Ranks 1 and 2 (measured, or published results from earlier events) do not exist on
kickoff day. **Rank 3 model estimate, labelled `[E]`:**

```
S_win ≈ P_robot(best candidate) + P_robot(P50 partner) + alliance bonuses
P50 partner [J] = half our cycle count, no position achievement
                = 4 cycles × 10 + AUTO PARK 3                            =  43
S_win           = 108 + 43 + 0                                           = 151  →  use 150 [E]
```

`[MANUAL]` **The third term is structurally zero this season.** Table 10-3 has no multiplier, ownership,
set-completion or coopertition row (R3 §1.2), so there are no alliance bonuses to add.
`[UNVERIFIED]` I have no historical inflation curve — `SCORING-PATTERNS.md` §B.11 holds it and is forbidden here.
**150 is an estimate, and V1 re-scores the day after our first event.**

### 3.5 Partner sensitivity (protocol §6.4), including the own-B-robot run

| Partner tier | Partner P_robot | S_alliance with **C1** (108) | Beats S_win 150? | S_alliance with **C3** (90) | Beats 150? |
|---|---:|---:|---|---:|---|
| **P10** (the null, C11) | 6 | **114** | ✗ short by 36 | **96** | ✗ short by 54 |
| **P50** (median) | 43 | **151** | ✓ by 1 | **133** | ✗ short by 17 |
| **P90** (another of us) | 108 / 90 | **216** | ✓ | **180** | ✓ |
| **Our own B robot (C6)** | 48 | **156** | ✓ | **138** | ✗ |

| Metric | C1 | C3 |
|---|---:|---:|
| Partner dependence `(S_win − P_robot) ÷ S_win` | `(150−108) ÷ 150 =` **0.28** | `(150−90) ÷ 150 =` **0.40** |
| Clears S_win with a P50 partner? | **Yes** (151) | **No** (133) — needs a partner ≥ 60 |
| Alliance-collision | A partner also running SPECIMENS queues at the **one** OBSERVATION ZONE with the **one** HUMAN PLAYER (Table 10-1: 1 per ALLIANCE) and shares the 20-element supply. Real but not blocking: `2 pre-loads + 16 TELEOP hangs = 18 ≤ 20` (R3 §4.2) | A partner also drawing from the SUBMERSIBLE contends for the same contested volume, but 45 of 60 elements there are legal for us |
| **V3 consequence** | **4** — a capability captains plan around, and our own A/B pair does not contend | **3** — one anchor level down for the collision, as the V3 anchor requires |

`[DERIVED]` **C6 as the B robot is worth more than the median partner: 48 > 43.** Our own second robot is a better
partner than the average robot at the event. That is the two-robot program's real competitive asset, and it is an
argument no single-robot team can make.

### 3.6 V ratings and the V score (anchors from `ACHIEVABILITY-RUBRIC.md` §5)

**V1** = `P_robot ÷ S_win` against the anchor bands. **V2** = `PPS_match` against the bands
(`<0.25 / 0.25–0.5 / 0.5–1.0 / 1.0–1.5 / >1.5`). **V3** from §3.5. **V4** from the §11 protected-zone rules.
**V5 re-anchored** — see the box.

> **V5 re-anchor, recorded as a deviation `[DERIVED]`.** The stock V5 anchors top out at *"earns a phase bonus
> **and a ranking point**"*. `[MANUAL]` **This season has no ranking point except winning** (Table 10-3), so rating
> 5 is unreachable for every candidate and the factor collapses. `ACHIEVABILITY-FACTORS.md` §8 mechanism 2 requires
> re-anchoring a factor that cannot discriminate. Re-anchored against Table 13-1's actual sorts — **2nd = Average
> ALLIANCE AUTO Points; 3rd = Average TELEOP ALLIANCE ASCENT Points, which counts ASCENT and *not* PARK**:
> **5** = AUTO ≥ 20 pts **and** a non-zero TELEOP ASCENT · **4** = AUTO 8–19 **and** ASCENT ≥ L2, or a LEVEL 3
> ASCENT with any AUTO (sort 3 maxed) · **3** = exactly one sort addressed deliberately · **2** = PARK only ·
> **1** = neither.

| Id | P_robot | PPS | **V1** | **V2** | **V3** | **V4** | **V5** | Σ(w×r) A-run | **V (A)** | Σ(w×r) B-run | **V (B)** |
|---|---:|---:|:-:|:-:|:-:|:-:|:-:|---:|---:|---:|---:|
| **C1** | 108 | 0.72 | 5 | 3 | 4 | 4 | 5 | 150+75+80+60+50 = **415** | **83** | 75+60+140+60+75 = **410** | **82** |
| **C2** | 118 | 0.79 | 5 | 3 | 4 | 3 | 5 | **400** | ~~80~~ → **40** | **395** | ~~79~~ → **40** |
| **C3** | 90 | 0.60 | 5 | 3 | 3 | 4 | 4 | 150+75+60+60+40 = **385** | **77** | **360** | **72** |
| **C4** | 72 | 0.48 | 4 | 2 | 3 | 4 | 4 | 120+50+60+60+40 = **330** | **66** | **325** | **65** |
| **C5** | 58 | 0.39 | 4 | 2 | 3 | 4 | 4 | 120+50+60+60+40 = **330** | **66** | **325** | **65** |
| **C6** | 48 | 0.32 | 3 | 2 | 3 | 4 | 4 | 90+50+60+60+40 = **300** | **60** | **310** | **62** |
| **C7** | 33 | 0.22 | 3 † | 1 | 3 | 5 | 4 | 90+25+60+75+40 = **290** | **58** | **305** | **61** |
| **C8** | 46 | 0.31 | 3 | 2 | 3 | 5 | 5 | 90+50+60+75+50 = **325** | **65** | **340** | **68** |
| **C9** | 22 | 0.15 | 2 | 1 | 2 | 3 | 2 | 60+25+40+45+20 = **190** | **38** | **195** | **39** |
| **C10** | 18 | 0.12 | 2 | 1 | 2 | 3 | 3 | 60+25+40+45+30 = **200** | **40** | **210** | **42** |
| **C11** | 6 | 0.04 | 1 | 1 | 2 | 2 | 2 | 30+25+40+30+20 = **145** | **29** | **165** | **33** |

† **V1 hard cap of 3** for a once-per-match-only strategy (`ACHIEVABILITY-RUBRIC.md` §5, V1 anchor).
A-weights `V1 30 · V2 25 · V3 20 · V4 15 · V5 10`; B-weights `15 · 20 · 35 · 15 · 15`. Both sum to 100. `V = Σ ÷ 5`.

**V4 justifications, straight from the bundle `[MANUAL]`:**
- **C7 = 5** — `G427` makes contact in an ASCENT ZONE in the last 30 s a **MAJOR plus a free LEVEL 3 to the
  opponent (45-point swing)**. The action *"occurs where opponents may not legally be."*
- **C8 = 5** — `G404` forbids **all** AUTO contact with a ROBOT wholly in its own half, **MAJOR each occurrence**.
  AUTO is structurally defense-free.
- **C1 = 4** — half the loop (our OBSERVATION ZONE) is `G426`-protected; the delivery half is not; and there are
  **two** chamber heights, so a defender costs cycles rather than the strategy.
- **C11 = 2** — `[DERIVED]` R5-R6 **F4**: `G412` protects SAMPLES and SPECIMENS, but **PARK is protected by no
  de-scoring rule at all**, so one opponent can legally shove us out of the zone at 0:00.

**Spread check (protocol §6.6 done-criterion, `range(V) ≥ 20`):** `83 − 29 = 54`. ✅
**MF6 check:** **0 `U` ratings on V1 or V2** for every candidate. ✅

---

## 4. D4 — Achievability, scored twice

### 4.1 Gates first (protocol §7.1) — a gate trip is not a low score

| Gate | Rule as the rubric states it | **What this manual actually says** | Result |
|---|---|---|---|
| **G1** Legality | §3 (I), §5 (E), §12 (R) | — | **All 11 pass.** The two illegal plans were deleted at D1 with rule ids (G412, G210) |
| **G2** Actuator budget | *"> 8 motors **or > 8 servos**"*, R503 §12.5 | `[MANUAL]` **R503: "ROBOTS are limited to a total of 8 motors and 12 servos."** The servo limit is **12**, not 8 | **All pass** (worst case C3 at 7–8/8 motors). **The gate's own number is wrong for this manual** — Beta feedback #1 |
| **G3** Fabrication floor | CNC / turning / waterjet / welding / custom gears | Nothing on the slate needs any. C7's hook is hand-cut aluminium (hacksaw, file, drill) — `EXTENSION-ARMS-LIFTS.md` §7.10 requires metal because *"printed hook fails — PETG at 15 kg in bending"* | **All pass** |
| **G4** Two-robot feasibility | buildable twice within budget and mentor hours | C3 alone threatens the calendar: ≈58–78 h × 2 ≈ 116–156 h, at 9 h/week (A9) ≈ **13–17 weeks**. A de-scoped B variant is named — **C5** — and scored separately as §7.1 requires | **All pass**, C3 conditionally |
| **G5** Cash ceiling | vs `research/SMALL-TEAM-ECONOMICS.md` | **That file is neither allowed nor forbidden in this run's brief, so I did not open it.** | **`[UNVERIFIED]` — could not be evaluated.** Two-robot BOM computed anyway (§4.2) so a mentor can apply the ceiling in 30 seconds |
| **G6** Pneumatics / airflow | *"R801 §12.8 — sealed COTS closed-air systems **pre-charged by the manufacturer (such as gas shocks)** are permitted"* | `[MANUAL]` **R207: "ROBOTS may not use any closed air devices such as but not limited to pneumatic solenoids or cylinders, gas storage vessels, gas springs, compressors, or vacuum generating devices."** R801: *"No closed air systems … except those explicitly listed in R207."* **Gas springs are banned outright here.** | **All pass** (nothing on the slate uses air). **But the gate's premise is inverted for this season**, and it invalidates the "zero-motor-slot climb" that `EXTENSION-ARMS-LIFTS.md` §7.5 calls *"the best idea in this section."* Ordinary mechanical springs remain legal — Beta feedback #1 |
| **G7** Loophole / intent | value rests on "it doesn't say we can't", or on unbounded use of a resource with a capping history | **C2 trips** — value rests on the §10.3.1 pre-load contradiction (§2.1). **C10 trips** — value rests on `G431.A`, *"any number of elements at a time … there is no human control limit"*, i.e. unbounded human-player handling | **C2 and C10 held under FLAG-2, V capped at 40** |

**FLAG-1 is not applicable this run.** `[MANUAL]` R101 (18-inch cube) and R104 (**no vertical height limit**;
20 × 42 in horizontal boundary that translates and rotates with the CHASSIS) are both final in this manual.
`[DERIVED]` **Vertical is free and horizontal is the scarce resource** — an arm reaching 26.0 in costs nothing in
rule space; a 42-in horizontal extension spends the whole budget (R5-R6 **F12**).

### 4.2 Two-robot marginal BOM, so a mentor can apply the missing G5 ceiling

`[DERIVED]` from `EXTENSION-ARMS-LIFTS.md` §3.8/§5.8/§7.9 and `INTAKE-AND-MANIPULATION.md` §4.5/§10.6. List price,
before the goBILDA 25 % / REV 15 % team discounts. **VERIFY-BEFORE-ORDER.**

| Id | Per robot | **For 2 robots** | Build hours, robot A |
|---|---:|---:|---:|
| C1 | arm $115 + claw $79 + winch climb $100 = **$294** | **$588** | 13–20 + 6 + 17–27 ≈ **36–53 h** |
| C2 | C1 + clip magazine/feed ≈ $60 = **$354** | **$708** | ≈ **50–70 h** |
| C3 | 4-stage slide $325 + tipper $50 + intake $136 + winch $100 = **$611** | **$1,222** | 25–35 + 16 + 17–27 ≈ **58–78 h** |
| C4 | servo arm $75 + claw kit $45 + winch $100 = **$220** | **$440** | 13 + 6 + 17–27 ≈ **36–46 h** |
| C5 | arm $115 + intake $136 + winch $100 = **$351** | **$702** | ≈ **38–55 h** |
| C6 | intake $136 + chute $20 + winch $100 = **$256** | **$512** | 8 + 2 + 17–27 ≈ **27–37 h** |
| C7 | winch + rated cord + metal hook = **$100** | **$200** | **17–27 h** |
| C8 | C1 + odometry/sensing ≈ $100 = **$394** | **$788** | C1's hours + weeks of AUTO tuning |
| C9 | convex plow face ≈ **$25** | **$50** | **4 h** |
| C10 | intake $136 + hopper $30 = **$166** | **$332** | **14 h** |
| C11 | **$0** marginal | **$0** | **0 h** |

### 4.3 Axis A ratings — scored **column-wise** (`ACHIEVABILITY-FACTORS.md` §8 mechanism 1)

Ratings are **identical between the A run and the B run**; only the weights differ (protocol §7.2 — *"nothing
about the robot changed, only who is building it and why"*).

| # | Factor | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | Spread |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| F1 | Fabrication complexity | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | **2 ⚠** |
| F2 | Duplicability A/B | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 3 | 5 | 5 | 5 | **2 ⚠** |
| F3 | BOM + spares cost | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 3 |
| F4 | Time to first prototype | 3 | 2 | 2 | 4 | 3 | 4 | 3 | 2 | 5 | 4 | 5 | 3 |
| F5 | Time to reliable | 4 | 2 | 2 | 5 | 3 | 5 | 4 | 3 | 5 | 4 | 5 | 3 |
| F6 | Iteration cost | 4 | 3 | 2 | 4 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 3 |
| F7 | Programming burden | 4 | 3 | 3 | 5 | 4 | 5 | 5 | 2 | 5 | 5 | 5 | 3 |
| F8 | Tuning burden | 4 | 2 | 2 | 5 | 3 | 5 | 5 | 2 | 5 | 4 | 5 | 3 |
| F9 | Sensor / vision dependence | 4 | 2 | 4 | 4 | 4 | 5 | 4 | 3 | 5 | 2 | 5 | 3 |
| F10 | Match reliability & consequence | 4 | 3 | 2 | 4 | 4 | 5 | 4 | 3 | **1** | 4 | 5 | 4 |
| F11 | Driver skill & practice | 3 | 2 | 2 | 4 | 3 | 5 | 4 | 4 | 2 | 4 | 5 | 3 |
| F16 | Rule-change exposure | 4 | **1** | 5 | 4 | 5 | 5 | 3 | 4 | 2 | 3 | 5 | 4 |

**The justifications that move a rank** (every other cell has an equivalent one-liner in the working notes; rule H7
requires a count, an hour, a dollar, a second or a named process in each):

- **F1 = 3 for C3.** A 43.0 in lip needs ≈48 in of usable travel from an 18 in starting cube (R101) ⇒ a 3–4 stage
  cascade. `EXTENSION-ARMS-LIFTS.md` §3.10 puts the 4-stage cord-rigged version in the "competitive" column at
  **25–35 h robot A**, and §3.9 requires *"mount both rails to one rigid plate, not to two separate chassis members;
  shim to square."* That is ≥2 parts needing hand-fitting ⇒ anchor 3. **It is not a 2** — the Viper kit is
  bolt-together COTS, and I record explicitly that I disagree with the leaked L5 value of 2.
- **F2 = 3 for C3.** §10.1 rates a cord-rigged slide **4** and notes *"rigging must be tensioned identically
  twice"*; the bucket at 43 in adds a second per-robot alignment. Two fitted subsystems, one tuning pass each ⇒ 3.
- **F2 = 3 for C8.** Anchor 3 is *"each robot needs its own tuning pass"* — odometry constants (track width,
  ticks/in, per-start-position offsets) are per-chassis and do **not** transfer between two robots.
- **F5 = 5 for C4.** A fixed-angle arm to a hard stop, dropping a clipped element over a **26.5 in wide,
  1.05 in diameter** bar at **13.0 in**: success is geometric, gravity finishes the placement, **zero empirical
  constants**. **F5 = 4 for C1** because at 26.0 in the arm is near full extension and must hold a position.
- **F5 = 2 for C3.** Tipping a **3.5 in** element into an **8.85 × 5.5 in** opening at **43.0 in** off the top of a
  cascade is two tight axes plus mast deflection; §3.9 lists *"slide sags at full horizontal extension"* and
  *"stage driven out of its carriage"* as standard failures.
- **F8 = 5 for C6 and C7.** Zero empirical constants: fixed intake compression and a chute; a winch driven to a
  limit switch. **F8 = 2 for C3** — 4 stage presets + a drive-speed limit at extension + dump timing + sag
  compensation, all voltage-sensitive on one battery ⇒ 6–10 constants.
- **F9 = 2 for C2 and C10.** Both must identify **ALLIANCE SPECIFIC** colour inside the SUBMERSIBLE, where only
  15 of 60 elements are ours (§10.3.1 F), under the RUNGS at 20 in — the worst lighting position on the field.
  **C3/C5/C6 need no colour discrimination at all**: §10.5.1 scores *own or neutral* alike in our BASKETS and NET
  ZONE. That single asymmetry is worth 2 rating points on a weight-6 factor and it comes straight out of the
  scoring criteria, not the scoring table.
- **F10 = 5 for C6.** `[DERIVED]` If the intake motor dies, the robot can still **herd** one SAMPLE at a time into
  the zone (G410 permits CONTROL of one element; §10.5.1 scores it *"fully or partially inside"*). **No plausible
  in-match failure removes scoring.**
- **F10 = 2 for C3.** A 48-in mast at full extension on a 12 × 12 ft field of contact; a stuck stage ends all
  scoring, and the high CG is a tip risk.
- **F10 = 1 for C9 → MF5 VETO.** Anchor 1 is *"a likely failure … causes a foul."* For a contact defender the
  likely failure **is** a foul, and this manual prices them at **G425 MAJOR (15) per occurrence regardless of who
  initiates**, **G426 MINOR + MINOR per 5 s + MINOR per element touched**, **G427 MAJOR + a free LEVEL 3 = 45**.
  `[MANUAL]` **T201: "No event staff, including the Head REFEREE, will review video, photos … under any
  circumstances"**, and **T302** instructs referees *not* to self-track foul details — so a wrong call is
  unappealable and unauditable (R5-R6 **F14**). MF5 forbids a 1 on F10. **C9 dies to a floor rule, not a total.**
- **F16 = 1 for C2 → MF5 VETO.** Anchor 1 is *"value depends on a loophole, ambiguity, or 'it doesn't say we
  can't'."* That is precisely the §10.3.1 pre-load contradiction. MF5 forbids a 1 on F16. **C2 discarded.**
- **F16 = 5 for C3, C5, C6.** Their revenue is pure §10.5.1 element-in-container scoring — the central loop, which
  cannot be nerfed without redesigning the game.
- **F16 = 4 for C1 and C4.** One level down, because their *supply* routes through **G431 human-player actions**,
  a category R5-R6 §B6 identifies as patchable. The scoring is safe; the logistics are not.
- **F16 = 3 for C7.** Its whole value rests on Table 10-2's LEVEL 2 wording *"fully supported by the HIGH **and/or**
  LOW RUNGS"* and on condition **C** applying to LEVEL 3 only (R3 §6.4) — a normal reading that could be clarified
  against us. `[DERIVED]` **The same rule risk is a rounding error for C1 (15 of 108 = 14 %) and the entire
  strategy for C7 (30 of 33 = 91 %). Identical rule; ninefold difference in exposure.** That asymmetry is exactly
  what F16 exists to catch, and it is invisible from the scoring table.

### 4.4 Axis A totals — both runs

**Run A** weights `F1 13 · F2 13 · F3 7 · F4 5 · F5 6 · F6 3 · F7 7 · F8 10 · F9 6 · F10 11 · F11 6 · F16 13` (Σ = 100).
**Run B** weights `15 · 10 · 8 · 8 · 9 · 5 · 10 · 8 · 5 · 13 · 6 · 3` (Σ = 100). Both verified.

Worked arithmetic for the two candidates that become robots:

```
C1, Run A:  F1 13×4=52   F2 13×4=52   F3  7×3=21   F4  5×3=15   F5  6×4=24   F6  3×4=12
            F7  7×4=28   F8 10×4=40   F9  6×4=24   F10 11×4=44  F11 6×3=18   F16 13×4=52
            Σ = 382        A_A = 382 ÷ 5 = 76.4  →  76          min_A = 3 on F3 / F4 / F11

C1, Run B:  15×4=60  10×4=40   8×3=24   8×3=24   9×4=36   5×4=20
            10×4=40   8×4=32   5×4=20  13×4=52   6×3=18   3×4=12
            Σ = 378        A_B = 378 ÷ 5 = 75.6  →  76

C6, Run A:  13×4=52  13×5=65   7×3=21   5×4=20   6×5=30   3×4=12
             7×5=35  10×5=50   6×5=30  11×5=55   6×5=30  13×5=65
            Σ = 465        A_A = 465 ÷ 5 = 93                   min_A = 3 on F3

C6, Run B:  15×4=60  10×5=50   8×3=24   8×4=32   9×5=45   5×4=20
            10×5=50   8×5=40   5×5=25  13×5=65   6×5=30   3×5=15
            Σ = 456        A_B = 456 ÷ 5 = 91.2  →  91
```

| Id | Σ A-run | **A (A)** | Σ B-run | **A (B)** | min_A | U count | Gates / flags |
|---|---:|---:|---:|---:|---|---:|---|
| **C1** | 382 | **76** | 378 | **76** | 3 on F3, F4, F11 | 0 | all pass |
| **C2** | 241 | **48** | 258 | **52** | **1 on F16** | 0 | **G7 → FLAG-2**; **MF5 veto** |
| **C3** | 284 | **57** | 254 | **51** | 2 on F3, F4, F5, F6, F8, F10, F11 | 0 | G4 conditional |
| **C4** | 423 | **85** | 427 | **85** | 4 (nothing below 4) | 0 | all pass |
| **C5** | 376 | **75** | 359 | **72** | 3 on F3, F5, F6, F8, F11 | 0 | all pass |
| **C6** | 465 | **93** | 456 | **91** | 3 on F3 | 0 | all pass |
| **C7** | 412 | **82** | 417 | **83** | 3 on F4, F16 | 0 | all pass |
| **C8** | 316 | **63** | 308 | **62** | 2 on F4, F7, F8 | 0 | all pass |
| **C9** | 399 | **80** | 421 | **84** | **1 on F10** | 0 | **MF5 veto** |
| **C10** | 395 | **79** | 407 | **81** | 2 on F9 | 0 | **G7 → FLAG-2** |
| **C11** | 500 | **100** | 500 | **100** | 5 | 0 | control |

**Spread check (protocol §7.4):** `range(A) = 100 − 48 = 52 ≥ 15` ✅ · `range(V) = 83 − 29 = 54 ≥ 20` ✅.
Excluding the null control C11: `range(A) = 45`, `range(V) = 45`. Both still pass. Detail at §8.

### 4.5 Award Yield (computed here, used only as tie-break #5)

`AY = (50×AY1 + 30×AY2 + 20×AY3) ÷ 5`, anchors from `ACHIEVABILITY-RUBRIC.md` §6.

| Id | AY1 evidence generation | AY2 demonstrable in 60 s | AY3 criteria fit | **AY** |
|---|:-:|:-:|:-:|---:|
| C1 | 5 — arm-vs-slide prototype comparison **plus** the points-per-inch ledger is a decision made from arithmetic (Think §6.3.2 criteria 1C and 1D) | 3 — needs a taped bar mock-up at 26.0 in | 5 — Design §6.3.8 *"simple to build and operate"* | **88** |
| C2 | 5 | 3 | 3 | **80** |
| C3 | 5 | 3 | 3 — **never pair Innovate with F10 ≤ 2** (rubric §6); C3's F10 = 2 | **80** |
| C4 | 3 | 5 — a 13.0 in bar sits on a pit table | 5 | **80** |
| C5 | 3 | 5 | 3 | **72** |
| C6 | 3 | 5 | 3 | **72** |
| C7 | 3 | 5 | 3 | **72** |
| C8 | 5 | 1 — only works on a full field | 5 — Control §6.3.7 requires external feedback | **76** |
| C9 | 1 | 1 | 1 | **20** |
| C10 | 3 | 3 | 3 | **60** |
| C11 | 1 | 5 | 1 | **44** |

Carried forward to the award phase: a dedicated defender's case is *"we shut down their scorer"*, which §6.1.1
makes inadmissible to judges — **C9 forfeits the machine-criteria award leg** on top of its MF5 veto.

### 4.6 Deviations and disagreements logged (rules H8, §5.2)

| # | Item | Consequence |
|---|---|---|
| **D-1** | **Only one scorer.** Protocol §7.3 and rule H8 require two independent scorers plus a disagreement log. This run had one. | **Every rating in §4.3 is provisional until a second scorer re-runs the columns.** The single largest methodological weakness of this run |
| **D-2** | **C2's novelty rule not followed.** §5.2 requires `F5 = U` and `F10 = U` for a novel archetype with no prototype; I rated 2 and 3 with justifications | C2 is discarded by MF5 on F16 regardless, so the `U→4 / U→2` double-ranking cannot change any rank |
| **D-3** | **Disagreement with a leaked value.** `ACHIEVABILITY-FACTORS.md` §8.1 scores the tall-lift candidate `F1 = 2, F2 = 2, F8 = 2`. I derived **3, 3, 2** from the kit-vs-fabricate distinction in `EXTENSION-ARMS-LIFTS.md` §3.10 | 2 rating points on F1 and F2 move C3's A by `(13×1 + 13×1) ÷ 5 = 5.2` ⇒ **57 instead of 52 — the difference between clearing MF2 and failing it, i.e. between STRETCH GOAL and TRAP.** Recorded, not averaged. See §8.4 |
| **D-4** | **V5 re-anchored** (§3.6) because this season has no ranking point, making the stock rating 5 unreachable | Legal under `ACHIEVABILITY-FACTORS.md` §8 mechanism 2. Beta feedback #5 |
| **D-5** | **D7's war-game precedents substituted.** Protocol §10.2 requires `[H]` precedents from prior seasons; those live in forbidden files | Nerfs derived from R5-R6 §B6's bundle-derived exposure register instead. Beta feedback #3 |

---

## 5. D5 — Plot, quadrants, ranked lists

### 5.1 The plot (A-team cuts: `A = 65`, `V = 55`)

```
 V
100 │   STRETCH GOAL / TRAP        ┊   BUILD THIS
 90 │                              ┊
 85 │                              ┊   C1 (76, 83)
 80 │                              ┊
 75 │       C3 (57, 77)            ┊       C4 (85, 71)
 70 │                              ┊
 65 │       C8 (63, 65)            ┊   C5 (75, 66)
 60 │                              ┊          C6 (93, 60)
 55 ├──────────────────────────────┼─── C7 (82, 58) ─────────────  V cut = 55
 50 │                              ┊
 45 │   SKIP                       ┊   SAFE FLOOR
 40 │   C2 (48, 40)                ┊   C10 (79, 40)
 35 │                              ┊      C9 (80, 38)
 30 │                              ┊                    C11 (100, 29)
    └───────────────────────────────────────────────────────────────
     40         50         60  65  70         80         90     100
                               ↑ A cut = 65                    A →
```

### 5.2 Floor screen (`ACHIEVABILITY-RUBRIC.md` §9.1) — applied before any ranking

| Id | MF1 gates | MF2 `A≥55` | MF3 `V≥40` | MF4 `A+V≥120` | MF5 no 1 on F1/F2/F3/F10/F16 | MF6 U's | Verdict |
|---|---|---|---|---|---|---|---|
| C1 | ✓ | 76 ✓ | 83 ✓ | 159 ✓ | ✓ | ✓ | **CLEARS** |
| C2 | G7 held | 48 ✗ | 40 ✓ | 88 ✗ | **F16 = 1 ✗** | ✓ | **FAILS ×3** |
| C3 | ✓ | 57 ✓ *(by 2)* | 77 ✓ | 134 ✓ | ✓ | ✓ | **CLEARS** |
| C4 | ✓ | 85 ✓ | 71 ✓ | 156 ✓ | ✓ | ✓ | **CLEARS** |
| C5 | ✓ | 75 ✓ | 66 ✓ | 141 ✓ | ✓ | ✓ | **CLEARS** |
| C6 | ✓ | 93 ✓ | 60 ✓ | 153 ✓ | ✓ | ✓ | **CLEARS** |
| C7 | ✓ | 82 ✓ | 58 ✓ | 140 ✓ | ✓ | ✓ | **CLEARS** |
| C8 | ✓ | 63 ✓ | 65 ✓ | 128 ✓ | ✓ | ✓ | **CLEARS** |
| C9 | ✓ | 80 ✓ | 38 ✗ | 118 ✗ | **F10 = 1 ✗** | ✓ | **FAILS ×3** |
| C10 | G7 held | 79 ✓ | 40 ✓ | **119 ✗** *(by 1)* | ✓ | ✓ | **FAILS MF4** |
| C11 | ✓ | 100 ✓ | 29 ✗ | 129 ✓ | ✓ | ✓ | **FAILS MF3** |

`[DERIVED]` **MF4 does exactly the job it was written for.** C10 has a respectable `A = 79` and a `V` of exactly
40 — it squeaks past MF2 and MF3 individually and is caught by `79 + 40 = 119 < 120`. That is the "safe but
pointless" extreme the floor exists to block, and it caught it **by one point**.

### 5.3 RANKED LIST — A robot (Run A weights; cuts `A ≥ 65 / V ≥ 55`)

Sorted by quadrant class, then by `V` within class, as §9.2 requires (a STRETCH GOAL is taken only if nothing is
in BUILD THIS).

| Rank | Id | Strategy | Shape | A | V | AY | Quadrant | Why (one line, with a number) | Kill condition | Kill date |
|---:|---|---|---|---:|---:|---:|---|---|---|---|
| **1** | **C1** | Hang our own converted elements on the **26.0 in** bar all match; LEVEL 2 climb | motor arm + servo claw + winch | **76** | **83** | 88 | **BUILD THIS** | 108 pts, **0.72 pts/s** — the highest match-averaged rate on the entire scoring table, from a mechanism **26.0 in tall, not 43.0** | < 8/10 hangs at ≤ 16.6 s | **Sun Oct 4 (G3)** |
| **2** | **C4** | Same loop, **13.0 in** bar, shorter reach | servo arm + claw + winch | **85** | **66** | 80 | **BUILD THIS** | 72 pts at **$220/robot and 36 h**; `A = 85`, second-highest on the slate | < 8/10 at ≤ 16.0 s | **Sun Oct 18 (G4)** |
| **3** | **C5** | Any element into the **25.75 in** container in our corner | lift + intake + tipper | **75** | **66** | 72 | **BUILD THIS** | 58 pts; the same acquisition as C6 for **+10 pts/match** and one lift | tipper < 8/10 at ≤ 11.6 s | Sun Oct 4 |
| **4** | **C6** | Any element onto the **floor** of our corner, 11 times | roller intake + chute + winch | **93** | **60** | 72 | **BUILD THIS** | 48 pts, **A = 93**, `$256`/robot, **27 h**, zero tuning constants, a **60-element** supply that never runs out | < 8/10 at ≤ 8.7 s | Sun Oct 4 |
| **5** | **C7** | Cross once at the end; **LEVEL 3** | two-stage winch climb | **82** | **58** | 72 | **BUILD THIS** | 33 pts. **V1 hard-capped at 3** (once-per-match). **0.22 pts/s** under Rule V-a | Table 10-2 L2/L3 wording changes | after TU02 |
| **6** | **C3** | Any element into the **43.0 in** container | 4-stage cascade + intake + tipper | **57** | **77** | 80 | **STRETCH GOAL** | `V = 77` is second-highest, but `A = 57` clears MF2 **by 2 points**. `$1,222` and **116–156 h for two robots** | prototype < 8/10 at ≤ 13.1 s | **Sun Oct 4, hard** |
| **7** | **C8** | Engineer the 30 s; minimal TELEOP | C1's hardware + odometry | **63** | **65** | 76 | **STRETCH GOAL** | 46 pts — **62 fewer than C1 on the same hardware**. The AUTO ceiling is 23/robot and it is *the same trip* that caps TELEOP | — | absorbed into C1 |
| — | C10 | Ferry elements to our loading zone for a partner | intake + hopper | 79 | 40 | 60 | **DISCARD** | **MF4: `79 + 40 = 119 < 120`.** Costs the pair **60 points** (156 vs 216) | — | — |
| — | C9 | Denial / defense | plow face | 80 | 38 | 20 | **DISCARD** | **MF5 veto, F10 = 1.** Pinning is **−7.5 pts at 15 s, −0.8 at 5 s**. Also MF3 (38 < 40) | — | — |
| — | C2 | Convert elements on board | C1 + clip magazine | 48 | 40 | 80 | **DISCARD** | **MF5 veto, F16 = 1**, plus MF2 and MF4. §10.3.1 contradicts itself on pre-loading CLIPS; without it the robot must make the very trip C2 exists to skip | — | — |
| — | C11 | Park only (the control) | COTS chassis | 100 | 29 | 44 | **CONTROL** | **MF3: 29 < 40.** Retained as the floor: **every candidate's margin over 6 points is the value of its mechanism** | — | — |

**Decision rule (§9.2) applied.** Five candidates sit in BUILD THIS, so tie-breakers run. **Tie-break 1 for the A
robot is higher `V`: C1 (83) > C4 (66) = C5 (66) > C6 (60) > C7 (58). C1 wins on the first tie-break by 17
points; no further tie-breaks are needed.**

### 5.4 RANKED LIST — B robot (Run B weights; cuts `A ≥ 70 / V ≥ 45`; floor MF2 `A ≥ 65`, MF3 `V ≥ 35`, MF4 `≥ 115`)

| Rank | Id | A (B) | V (B) | Quadrant (B) | Why (one line, with a number) |
|---:|---|---:|---:|---|---|
| **1** | **C6** | **91** | **62** | **BUILD THIS** | **Tie-break 1 for the B robot is higher `A`, and 91 is the highest of any floor-clearing candidate.** 27 build hours, `$512` for the pair, **zero empirical tuning constants**, `F10 = 5`, and it never contends with C1 |
| 2 | C4 | 85 | 69 | BUILD THIS | Higher `V`, but **contends with C1 for the CHAMBERS, the OBSERVATION ZONE, the single HUMAN PLAYER and the 20-element ALLIANCE SPECIFIC supply** — the §8.3 non-contention guardrail forbids it |
| 3 | C7 | 83 | 61 | BUILD THIS | Position-only. **Named as C6's written fallback** (§6.2) |
| 4 | C1 | 76 | 82 | BUILD THIS | Highest `V` of all — but it *is* the A robot |
| 5 | C5 | 72 | 65 | BUILD THIS | **C6's named in-season upgrade**: same intake, same corner, add one 25.75 in lift ⇒ `58 − 48 = +10 pts/match` |
| — | C10 | 81 | 42 | SAFE FLOOR | Clears the B floor (`81 + 42 = 123 ≥ 115`) but §3.3 costs the pair 60 points |
| — | C3 | 51 | 72 | **TRAP** | Fails B MF2 by 14 (`51 < 65`). **A STRETCH GOAL or TRAP may never be assigned to the B robot** (§9.2 step 5) |
| — | C8 | 62 | 68 | **TRAP** | Fails B MF2 by 3 |
| — | C9, C2 | — | — | discarded | The MF5 vetoes carry into both runs unchanged |
| — | C11 | 100 | 33 | discarded | Fails B MF3 by 2 |

> **Read the swap.** `[DERIVED]` **C3 is a STRETCH GOAL for the A team and a TRAP for the B team on identical
> ratings** — the B weights price its `F4 = 2`, `F5 = 2` and `F7 = 3` at 8, 9 and 10 instead of 5, 6 and 7, and drop
> its `F16 = 5` from weight 13 to 3, deleting the one factor it was strong on. **And C6 is rank 4 for the A team
> and rank 1 for the B team.** That swap is the entire reason the rubric is run twice, and it happened here
> arithmetically rather than by argument.

### 5.5 Non-contention guardrail (§8.3) — checked, and the result written down

| | **A robot = C1** | **B robot = C6** | Collision? |
|---|---|---|---|
| Scoring target | HIGH CHAMBER, 26.0 in, centre of the field | NET ZONE, floor, our own corner | **No** |
| Acquisition | our own OBSERVATION ZONE + the ALLIANCE-coloured SPIKE MARKS | the SUBMERSIBLE, neutral elements | **No** |
| Supply pool | 20 ALLIANCE SPECIFIC SAMPLES (lifetime) | 40 neutral + 20 own = **60** (R3 §1.6) | **No** |
| Human player | required every cycle | never | **No** |
| Field corner | the OBSERVATION ZONE corner | the NET ZONE corner — diagonally opposite | **No** |
| Endgame | own ASCENT ZONE, LEVEL 2 | own ASCENT ZONE, LEVEL 2 | Shared, but §10.5.3 A gives each ALLIANCE its own SPECIFIC RUNGS |

**Guardrail passes. No `V3` re-score required.** `[DERIVED]` This is the same pairing R3 §6.6 reached from pure
throughput arithmetic — two independent routes, one answer.

### 5.6 The three required blocks

**1. What we are building, and why (each sentence carries a number).**
The A robot hangs converted elements on the **26.0 in** bar and climbs the **20.0 in** LOW RUNG: **108 points at
0.72 points per second**, the highest match-averaged rate on the entire scoring table. It is **60 % of the height**
of the 43.0 in container that pays **20 % less** (10 vs 8 points, 26.0 vs 43.0 inches). The B robot pushes elements
onto the **floor** of our own corner: **48 points**, `$256` per robot, **27 build hours**, **zero empirical tuning
constants**, and a **60-element** supply that cannot run out. Both robots carry the **same hook, cord and winch**,
because the 12-second LEVEL 2 climb is the only line on Table 10-3 worth **0.75 points per inch of lift** — four
times the HIGH BASKET's 0.19 — and the displacement test says yes for both: **+5 for the A robot** (it costs one
10-point cycle) and **+11 for the B robot** (it costs two 2-point cycles).

**2. What we are NOT building, and why.**

| Not built | A / V | Killed by |
|---|---:|---|
| **C3** tall-container bot | 57 / 77 | Not killed — **STRETCH GOAL with a hard Oct 4 de-scope date.** `$1,222` and **116–156 h for two robots**, clearing MF2 by **2 points**. If the A robot were being built *once*, this would be a real argument; it is being built twice |
| **C2** on-board conversion | 48 / 40 | **MF5, `F16 = 1`** — §10.3.1 permits pre-loading *"1 SAMPLE or one SPECIMEN"* and then refers to *"SAMPLES **or CLIPS** not pre-loaded"*. Contradiction. Also G7 / FLAG-2 |
| **C9** dedicated defense | 80 / 38 | **MF5, `F10 = 1`**, and **MF3** (38 < 40). A 15-second pin costs 20 (G423 stacking) and denies 12.5 ⇒ **−7.5** |
| **C10** feeder / shuttle | 79 / 40 | **MF4 by one point** (119 < 120), and pair arithmetic: **156 vs 216 = −60** |
| **C8** AUTO-only | 63 / 65 | **STRETCH GOAL, absorbed into C1.** Same hardware, same 23-point AUTO ceiling, **62 fewer points** |
| **C11** park-only | 100 / 29 | **MF3** (29 < 40). Kept as the control that prices every mechanism on the slate |
| **De-scoring** an opponent's element | — | **F-legal: G412, MAJOR (15) per element** against a HIGH BASKET worth 8 |
| **Drawing** a G427 contact deliberately | — | **F-legal: G210**, and category (c) on the ethics test |

**3. What would change our minds.**

| Open item | What it moves | When it resolves |
|---|---|---|
| **`[UNVERIFIED]` A8** — are AUTO-scored elements counted again at the end of TELEOP? (R3 §2.2, R5-R6 **F1**) | C1 goes **108 → 128** and C8's premise becomes real. **V is scored on the pessimistic reading throughout, so a "yes" can only help.** Zero hardware cost either way | **Q&A #1**, the day the Q&A opens |
| **`[UNVERIFIED]`** — may a ROBOT be pre-loaded with CLIPS? (§10.3.1 contradiction) | Moves C2 from SKIP to a live candidate | **Q&A #2** |
| **`[UNVERIFIED]` A7** — the real `S_win` | **V1 for every candidate.** At `S_win = 200`, C1 falls to 54 % ⇒ V1 = 4 ⇒ V = 77 — **still rank 1**. At `S_win = 120`, C1 is 90 % ⇒ V1 stays 5 | The day after our first event (`ACHIEVABILITY-RUBRIC.md` §15: the season's highest-value re-score) |
| **`[UNVERIFIED]` A10** — the cash ceiling | **G5 could not be evaluated.** Below `$1,200` for two robots, C3 is rejected at the gate rather than carried as a STRETCH GOAL | A mentor, in 30 seconds, against §4.2 |
| **FLAG-2 on C2 and C10** | Both capped at `V = 40` until the second Team Update is read | After TU02 |
| **Deviation D-1** — one scorer | **Every A rating.** C3's MF2 clearance hangs on 2 rating points | A second scorer re-runs §4.3 column-wise, before Oct 4 |

---

## 6. D7 — Stress-test the top two

> **Interpretation, stated.** "The top two" is read as **the top-ranked candidate for each robot** — C1 and C6 —
> because those are the two machines the program will actually build. Each block also carries that robot's
> fallback (C4 and C7 respectively), which is what the protocol's §10.3 requires anyway.

### 6.1 C1 — HIGH CHAMBER cycler, own-zone loop, LEVEL 2 climb *(the A robot)*

| # | Vector | Answer |
|---|---|---|
| **K1 Rules kill** | The single rule that removes value is a Team Update restricting **G431** human-player element handling, or narrowing **G426**'s OBSERVATION ZONE protection. That is exactly why **`F16 = 4`, not 5.** **No "it doesn't say we can't" reading is involved — G7 does not trip.** Recomputed for the worst case: if G426 narrows so opponents may contact us while we are only *partially* in our own zone, add 2 s per cycle ⇒ `16.6 → 18.6` ⇒ `floor(70.3 ÷ 18.6) = 3` ⇒ N = 6 ⇒ **P_robot 98**; `V1 = 98 ÷ 150 = 65 %` ⇒ still 5; `V2 = 0.65` ⇒ still 3. **ΔV = 0. Survives.** |
| **K2 Physical kill** | Arm gearbox strip — `EXTENSION-ARMS-LIFTS.md` §5.9: *"arm crashed into a hard stop at speed."* Cost: all SPECIMEN scoring; the robot still drives, PARKS and climbs (`F10 = 4`). Not driver-recoverable in-match. **`[MANUAL]` I303.A: *"ROBOTS are allowed to play MATCHES with a subset of the MECHANISMS that were present during inspection. Only MECHANISMS that were present during inspection may be added, removed, or reconfigured between MATCHES."*** ⇒ **the B robot's identical arm is a legal drop-in spare *only if it is on the cart at inspection*. Present both arms at every inspection.** That is an action item, not an observation |
| **K3 Opponent kill** | **No.** Two chamber heights (13.0 and 26.0 in) on a **26.5 in wide** bar give a second scoring position; the acquisition half of the loop sits inside **G426**-protected space (MINOR + MINOR per 5 s + MINOR per element touched); and if both chambers are camped, the fallback target is the NET ZONE at 2. **A defender costs cycles, not the strategy. `V4 = 4`** |
| **K4 Program kill** | `$588` for two robots; **36–53 h** robot A; longest print < 4 h; every part a catalogue SKU. If the student who built it is absent two weeks, `F2 = 4` says a printed BOM plus the kit lets someone else assemble #2 with one tuning pass. Print-queue load: 2 claws + 4 brackets × 2 robots ≈ **14 printer-hours** |
| **K5 Partner kill** | **This is the real risk.** With a P10 partner the alliance scores **114 against a 150 winning score — we lose.** With P50 we win **by 1 point.** Mitigation: our own B robot (48) puts the pair at **156**. Real estate: a partner also running SPECIMENS queues at the **one** OBSERVATION ZONE with the **one** HUMAN PLAYER (Table 10-1) — brief them in the pit: they take the LOW CHAMBER face, we take the HIGH |

**Team Update war-game.** *Deviation D-5: protocol §10.2 supplies prior-season precedents, which are forbidden
here, so the three nerfs below are derived from this manual's own patchable surfaces (R5-R6 §B6).*

| # | The nerf, in one sentence | Which V factor moves | Recomputed V | Survives? |
|---|---|---|---:|---|
| 1 | **AUTO-scored elements are explicitly not re-counted in TELEOP** | none — **assumption A8 already assumes this** | **83** | ✅ zero cost, by construction. *This is why we planned the pessimistic reading* |
| 2 | **G410 amended to cap the CLIPS a ROBOT may possess** | none — C1 never carries a CLIP; this kills C2, which we did not build | **83** | ✅ |
| 3 | **ASCENT LEVEL 2 redefined to require the HIGH RUNG** | L2 (15) → L1 (3). `P_robot 108 → 96`; `V1 = 96 ÷ 150 = 64 %` ⇒ 5; `V2 = 0.64` ⇒ 3; V5: AUTO 23 + a non-zero ascent ⇒ 5 | **83** | ✅ on V; **−12 points of match score.** Hardware cost: one bracket |

**Fallback: C4** — LOW CHAMBER volume cycler, **A 85 / V 71, BUILD THIS**, already scored through D3 and D4.

| Field | Value |
|---|---|
| De-scope path | Shorten the arm from a 26.0 in reach to a 13.0 in reach; swap the 5203 motor for a servo. **Delete:** the long arm segment and its two brackets. **Keep:** chassis, drivetrain, claw, winch, hook, all code, all driver muscle memory |
| Mechanical / electrical interface | The arm bolts to a slotted goBILDA channel on the chassis; the same bolt pattern serves both lengths. **No new chassis** — so it is a genuine de-scope, not a rebuild |
| Cost of the switch | 2 reprinted brackets (≈ 6 printer-hours), 1 servo `$45`, ≈ 6 build hours, `$0` of new structure |
| What is preserved | **4 of 5 subsystems ≈ 85 % of BOM** |
| Value cost | `108 − 72 = 36 points/match`; `V 83 → 71` — **still BUILD THIS** |

**Kill date and numeric criterion — G3, Sun Oct 4** (the program's primary kill gate):
> *The C1 prototype completes **8 of 10** HIGH CHAMBER hangs at **≤ 16.6 s** self-supplied (and ≤ 9.5 s staged), on a
> taped mock-up with a real 1.05 in bar at 26.0 in, with one page of recorded test numbers. **Miss it → execute C4.***

**Second abandon date — G4, Sun Oct 18 (DESIGN FREEZE):**
> *If C4 has not reached **8/10 at ≤ 16.0 s**, the A robot adopts C6 and the program accepts a development season.
> After G4, no part not on the purchase order enters either robot.*

### 6.2 C6 — NET ZONE volume cycler, LEVEL 2 climb *(the B robot)*

| # | Vector | Answer |
|---|---|---|
| **K1 Rules kill** | **`F16 = 5`.** `[MANUAL]` §10.5.1 scores a SAMPLE in the NET ZONE when *"fully or partially inside"* — the most permissive scoring criterion in the manual — and colour is irrelevant (own **or** neutral). The one patchable edge is **G410's CONTROL definition**: R5-R6 **F7** shows the §16 glossary calls a *flat or concave* face CONTROL while the orange box exempts *convex* PLOWING. **Mitigation costs `$0`: build the front face convex.** ΔV = 0 |
| **K2 Physical kill** | **`F10 = 5`.** If the intake motor dies, the robot herds one element at a time into the zone and keeps scoring. The only failure that costs points is the climb (15). An identical spare intake is a legal drop-in under **I303.A** if it was inspected |
| **K3 Opponent kill** | **G425** makes our NET ZONE **MAJOR (15) per occurrence, through a controlled element, regardless of who initiates** — an opponent camping our corner pays 15 per contact against a 2-point target. Acquisition is contested, but **45 of the 60 elements in the SUBMERSIBLE are legal for us**, so denial means denying the entire submersible. `V4 = 4` |
| **K4 Program kill** | `$512` for two robots, **27 h**, one motor, **zero empirical constants**, and `INTAKE-AND-MANIPULATION.md` §4.7 names a COTS escape hatch (*"adopt the StarterBot Gecko intake verbatim and move on"*). **The most absent-student-proof design on the slate** |
| **K5 Partner kill** | Never contends with C1 (§5.5). As a partner, **C6 at 48 > the P50 median of 43** — our own second robot is better than the average robot at the event |

**Team Update war-game.**

| # | The nerf | Recomputed | Survives? |
|---|---|---:|---|
| 1 | **CONTROL redefined so any pushing face counts** | build the face convex; `t_align` unchanged | ✅ ΔV = 0, `$0` |
| 2 | **NET ZONE requires full containment, not partial** | `t_align 0.3 → 0.8`; cycle `8.7 → 9.4`; `floor(104 ÷ 9.4) = 11` — **unchanged** | ✅ ΔV = 0 |
| 3 | **ASCENT LEVEL 2 requires the HIGH RUNG** | `48 → 36`; `V1 = 36 ÷ 150 = 24 %` ⇒ still 3 | ✅ ΔV = 0; **−12 pts** |

**Fallback: C7** — position-only, **A(B) 83 / V(B) 61, BUILD THIS for the B robot**, already scored.
De-scope path: **delete the intake and the chute; keep the chassis, drivetrain, winch, cord and hook.**
Preserved: **3 of 4 subsystems.** Cost of the switch: **`$0` and 2 hours** (removing parts).
Value cost: `48 − 33 = 15 points/match`.

**Kill date — G3, Sun Oct 4:** *8 of 10 NET ZONE deliveries at ≤ 8.7 s on a taped corner.*
The **B design freezes at G3, not G4** (protocol §10.4 B-robot rule): it is simpler, it converges sooner, and it
earns the extra two weeks of build time. If B is still choosing a mechanism at G4, the model-switch has failed and
B copies A's proven mechanism.

---

## 7. THE RECOMMENDATIONS, STATED EXPLICITLY

> ### **A ROBOT → C1**
> *Spend the whole match converting our own ALLIANCE-coloured elements at our own protected loading zone and
> hanging them on the **26.0 in** CHAMBER bar; hang the robot on the **20.0 in** LOW RUNG at the end. **Do not build
> anything that reaches 43 inches.***
>
> **A = 76 · V = 83 · AY = 88 · BUILD THIS · 108 pts · 0.72 pts/s · `$294`/robot · 36–53 h**
> **Fallback: C4** (13.0 in bar) — written, scored, BUILD THIS, **85 % of BOM preserved**.
> **Kill date: Sun Oct 4 — 8 of 10 hangs at ≤ 16.6 s.**

> ### **B ROBOT → C6**
> *Take any element out of the centre structure and put it on the floor of our own corner, as many times as
> possible; hang on the LOW RUNG at the end. **Touch nothing tall and never touch the loading zone.***
>
> **A = 91 (B weights) · V = 62 (B weights) · AY = 72 · BUILD THIS · 48 pts · `$256`/robot · 27 h · zero tuning constants**
> **Fallback: C7** (climb only) — written, scored, BUILD THIS for B.
> **In-season upgrade: C5** — same intake, same corner, add one 25.75 in lift for **+10 pts/match**. Decide at G3.
> **Kill date: Sun Oct 4 — 8 of 10 deliveries at ≤ 8.7 s. The B design freezes at G3.**

**Both robots get the same hook, the same cord and the same winch, built once and duplicated.** `[DERIVED]` The
LEVEL 2 climb pays **+15 for 12 seconds** and is the only line on Table 10-3 worth **0.75 points per inch of lift**
— four times the HIGH BASKET's 0.19 — and the displacement test says build it on **both**: **+5 net for the A
robot** (it costs one 10-point cycle) and **+11 net for the B robot** (it costs two 2-point cycles).

**The two robots do not compete for a single element, a single zone, a single corner, or the single human player.**

---

## 8. Did the rubric discriminate?

### 8.1 The headline — yes, decisively, on the totals

| Measure | Threshold | **Result** | Verdict |
|---|---:|---:|---|
| `range(A)`, all 11 candidates | ≥ 15 | `100 − 48 =` **52** | ✅ 3.5× the bar |
| `range(V)`, all 11 candidates | ≥ 20 | `83 − 29 =` **54** | ✅ 2.7× the bar |
| `range(A)`, excluding the null control | ≥ 15 | `93 − 48 =` **45** | ✅ |
| `range(V)`, excluding the null control | ≥ 20 | `83 − 38 =` **45** | ✅ |
| `range(A)`, the 7 serious candidates only | ≥ 15 | `93 − 57 =` **36** | ✅ |
| `range(V)`, the 7 serious candidates only | ≥ 20 | `83 − 58 =` **25** | ✅ |
| `ACHIEVABILITY-FACTORS.md` §8 "tell" (best-to-worst gap under ~10 = you scored nothing) | — | **52 on A, 54 on V** | ✅ nowhere near flat |

**Nothing landed in a 60–70 cluster.** The seven serious candidates' A scores are **57, 63, 75, 76, 82, 85, 93**
and their V scores are **58, 60, 65, 66, 66, 77, 83** — spread across the full usable range, and both quadrant
cuts (`A = 65`, `V = 55`) fall **between** candidates rather than through a cluster. Two candidates sit below the A
cut (C3 at 57, C8 at 63) and two sit far below the floor (C2 at 48, C9's V at 38). **The instrument separated
things, and it separated them where the cuts are.**

### 8.2 But four factors failed the forced-spread test, and they carry 71 points of weight

`ACHIEVABILITY-FACTORS.md` §8 mechanism 2 requires a per-factor spread check after each column. Four factors
returned a range of only 2 on a 1–5 scale:

| Factor | Weight (A) | Ratings observed | Range | Why it collapsed **this season** |
|---|---:|---|:-:|---|
| **F1** Fabrication complexity | **13** | 3,3,3,4,4,4,4,4,4,5,5 — **7 of 11 at 4** | **2** | `[DERIVED]` **Every viable mechanism in this game is a bolt-together COTS kit.** Nothing on the slate needs CNC, welding or waterjet, so anchors 1 and 2 are unreachable; and anchor 5 (bare COTS chassis) is only reachable by candidates that do not score. The factor had nothing to measure |
| **F2** Duplicability A/B | **13** | 3,3,3,4,4,4,5,5,5,5,5 | **2** | Same root cause. When every mechanism is a catalogue kit with print files, duplicability is high by construction |
| **V2** Match points-per-second | **25** | 1,1,1,2,2,2,2,3,3,3,3 — **no candidate above 3** | **2** | `[DERIVED]` **The absolute anchor bands are calibrated for a higher-scoring game.** The best strategy this manual admits runs at **0.72 pts/s**; the bands put anything under 1.00 at rating 3 or below, so ratings 4 and 5 were structurally unreachable and ten of eleven candidates piled into 1–3 |
| **V3** Alliance desirability | **20** | 2,2,2,3,3,3,3,3,3,4,4 — **7 of 11 at 3** | **2** | The anchors separate "reliable driveable partner" (3) from "a capability captains plan around" (4) on a near-binary (does the A/B pair contend?), which most candidates answer identically |

**That is 26 of the 100 points of Axis A weight and 45 of the 100 points of Axis V weight resting on factors that
barely discriminated.** The axes still spread by 52 and 54 because the load was carried elsewhere: **V1 (weight 30)
produced a clean 5,5,5,4,4,3,3,3,2,2,1 and did almost all of the work on Value**, while **F10, F16 and F8
(32 points of weight combined, ranges 4, 4 and 3) did the work on Achievability.** A rubric can survive four dead
factors only if the live ones are heavy enough — and here, by luck rather than design, they were.

### 8.3 Sensitivity test — does the ranking survive re-anchoring the worst offender?

I re-anchored V2 to this season's realised range. This is protocol-legal without argument: the rubric's own V2
anchor-5 text already reads *"> 1.5 pts/s, **or the highest match-averaged rate on the scoring table**"* — I simply
applied that clause consistently down the scale.

`5 = ≥ 0.70 · 4 = 0.50–0.69 · 3 = 0.35–0.49 · 2 = 0.20–0.34 · 1 = < 0.20`

| Id | V2 literal | V2 re-anchored | V (literal) | **V (re-anchored)** | Quadrant change? |
|---|:-:|:-:|---:|---:|---|
| **C1** | 3 | **5** | 83 | **93** | no — BUILD THIS |
| C3 | 3 | 4 | 77 | **82** | no — STRETCH GOAL |
| C4 | 2 | 4 | 66 | **76** | no — BUILD THIS |
| C5 | 2 | 3 | 66 | **71** | no |
| C6 | 2 | 2 | 60 | **60** | no |
| C7 | 1 | 2 | 58 | **63** | no |
| C8 | 2 | 2 | 65 | **65** | no |

`range(V)` rises from **54 to 64**, and **rank 1 does not move: C1 is first on both anchorings — by 17 points of V
over the next BUILD THIS candidate on the literal anchors, and by 17 on the re-anchored ones.** The B-robot answer
is also unchanged, because the B tie-break is higher **A**, which V2 does not touch. **The ranking is robust to the
single largest anchor problem in the instrument.**

### 8.4 Verdict on trustworthiness

**The ranking is trustworthy at the top and soft in the middle. Say both.**

- **Trustworthy — rank 1 on both robots.** C1 leads the A list by **17 points of V** over the next BUILD THIS
  candidate and survives a complete re-anchoring of the worst factor. C6 leads the B list by **6 points of A** and
  is *independently* forced by the non-contention guardrail — two separate mechanisms agreeing. Three of the four
  discards (C2, C9, C10) fall to **floor rules with rule ids and computed numbers**, not to close totals.
- **Soft — the middle of the A list.** **C4 and C5 tie exactly at `V = 66`**, and C6 (60) and C7 (58) sit within 2
  points. Those four orderings rest on the factors that did not discriminate. **They are one band, not a ranking**,
  and the program should treat them as interchangeable until a prototype produces a measured cycle time
  (tie-break 8: *"prototype both for one week, then re-score V1 and V2 with measured cycle times"*).
- **The number that would worry me most.** **C3 clears MF2 by 2 points (57 vs 55)**, and its A hinges on the F1 and
  F2 ratings where I explicitly disagree with the leaked calibration by 2 rating points each (§4.6 **D-3**). At the
  leaked values C3 is **A = 52, a TRAP**; at mine it is **A = 57, a STRETCH GOAL** — the difference between "do not
  build this" and "build it with a de-scope date". **The single most consequential number in this file is decided
  by a judgment call worth 5.2 points of A, made by one scorer** (deviation **D-1**). A second scorer must re-run
  the F1 and F2 columns before Oct 4. It does not change the A-robot recommendation, but it changes what the
  program tells itself it is allowed to want.
- **And the caveat that overrides all of the above.** Because of leak **L4**, I knew the shape of the expected
  answer before I scored anything. **The spread numbers in §8.1 are real arithmetic; their evidential value for
  "does the harness generalise" is not.** The BIOBUZZ run on **2026-09-12** will be the first clean measurement of
  this instrument, and only if Beta feedback #9 is acted on first.

---

## Beta feedback

**1. Two gate definitions in `ACHIEVABILITY-RUBRIC.md` §3 hard-code BIOBUZZ rule *numbers*, and both are wrong for
this manual.** **G2** trips at *"> 8 motors **or > 8 servos**"* citing R503 — but this manual's **R503 reads "8
motors and 12 servos"**, so the gate as written would have rejected a legal 10-servo design. **G6** is worse: it
states R801 *permits* *"sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas
shocks)"* — but this manual's **R207 bans gas springs outright**, and R801 says *"no closed air systems except
those explicitly listed in R207."* **The gate's premise is inverted**, and it silently invalidates the
"zero-motor-slot climb" that `mechanisms/EXTENSION-ARMS-LIFTS.md` §7.5 calls *"the best idea in this section"*.
**Fix: gates must name the *constraint*, not the number — "the manual's stated actuator limit", "whatever the
manual's stored-energy rule permits" — and the kickoff ingest should emit an `R_LIMITS.txt` carrying the season's
actual values.** A team running this harness on BIOBUZZ would otherwise gate against last season's numbers without
ever noticing.

**2. The 7–10 candidate band in D1 §4.5 cannot be met by a season with five uncapped repeatable scoring rows.**
Five revenue rows + seven mandatory contrarians + the walk rule's two extra variants = 12 before merging; overlaps
only bring it to 11. I carried 11 and recorded the deviation, because merging LOW BASKET into NET ZONE would have
deleted a real distinction (0 in vs 25.75 in of lift, for 2 vs 4 points). **Fix: make the band a function of the
scoring table — "one per uncapped repeatable row, plus the seven contrarians, minus overlaps" — instead of a fixed
7–10.** The fixed band silently pushes an analyst toward merging distinct strategies on a rich scoring table.

**3. Two more protocol steps dead-end in forbidden files, on top of the two R5/R6 already reported.**
**D2 §5.1** requires the archetype rows and Fit index from `ROBOT-ARCHETYPE-LIBRARY.md` §2 / §3.1–3.11 — forbidden.
**D7 §10.1–10.2** requires `PENALTY-AND-ENFORCEMENT.md` for the K1 rules-kill and `research/LOOPHOLE-CASEBOOK.md`
plus prior-season Team Update precedents for the war-game — both forbidden. Substitutes used, both season-agnostic
and both recommended for permanent adoption: **(a) D2** — describe the mechanism shape as
`(acquisition, delivery height, actuation, actuator count, duplicability driver)` from the ARENA geometry in the
bundle plus the BUY tables in the allowed `mechanisms/*.md`; **(b) D7** — derive the three most likely nerfs from
the *current manual's own* patchable surfaces (R5-R6 §B6's rule-change exposure register). The substitute for D7 is
**better than the original**: a nerf derived from this manual's own ambiguities is a real risk, while one
transplanted from another game is a guess wearing a citation.

**4. Gate G5 could not be evaluated at all.** It tests the two-robot BOM against a ceiling in
`research/SMALL-TEAM-ECONOMICS.md`, which is **neither on this run's allowed list nor on its forbidden list** — so
I did not open it, had no cash ceiling, and recorded G5 as `[UNVERIFIED]`. This is not cosmetic: **C3's `$1,222`
two-robot BOM is the number most likely to have rejected it at the gate instead of carrying it as a STRETCH GOAL,
and C3's STRETCH-GOAL status is the softest result in the file.** For BIOBUZZ, either put the cash ceiling in the
*bundle* (it is a program fact, not a game fact, so it survives any season) or state it in the run brief. Also:
the allowed/forbidden lists should be **exhaustive over `reference/` and `research/`**, so "unlisted" is never a
state an analyst has to guess about.

**5. The rubric's own V2 anchor bands are mis-calibrated for a low-scoring season, and V5's top anchor was
structurally unreachable.** V2's absolute bands (`<0.25 / 0.25–0.5 / 0.5–1.0 / 1.0–1.5 / >1.5`) put **ten of eleven
candidates into ratings 1–3**, because the best strategy this manual admits runs at **0.72 pts/s** — nothing can
reach 4 or 5. V5's rating 5 requires *"earns a ranking point"*, and **this season has no ranking point except
winning** (Table 10-3 has exactly two RP rows, Tie and Win) — so the top anchor was unreachable for every candidate
and the factor collapsed until I re-anchored it against Table 13-1's actual sort criteria. **Between them these two
factors carry 35 of the 100 points of Axis V weight.** Fix, one line of protocol text each: **V2 should be
season-relative by construction** — *"as a fraction of the best match-averaged rate the scoring table admits,
computed at D3"* — and **V5 should read** *"how many of this season's ranking-ladder sort criteria does this
deliberately feed, and at what magnitude"*, read off whatever sort table the manual prints. Both would have
discriminated without my intervention, and neither requires knowing the game in advance.

**6. The bundle has no `SETUP_AND_ELEMENTS.txt`, and the fact that decided a whole candidate was only in the
last-resort file.** The §10.3.1 pre-load contradiction — *"may be pre-loaded with either 1 SAMPLE or one SPECIMEN"*
immediately followed by *"SAMPLES **or CLIPS** not pre-loaded will remain in setup locations D and E"* — is the
single sentence pair that kills candidate C2, and I found it only by grepping `full_layout.txt`, the file the
house rules call a last resort. Nothing else in the bundle carries pre-match setup prose or element definitions.
**Recommendation: emit a `SETUP_AND_ELEMENTS.txt` (the §10.3 pre-match setup prose plus the §9.7 element
definitions) and put it in the feed order between `TABLES.md` and `rules_GAMESPECIFIC.txt`.** This is the same
gap R5-R6 reported for the glossary, from a different direction, which suggests the real fix is *"every prose
section that a rule body cross-references gets its own extract file."*

**7. Numbers I could not find.** `[UNVERIFIED]`, all queued: **(a)** whether AUTO-scored elements are re-counted at
the end of TELEOP — the single number that moves the A robot from 108 to 128; **(b)** whether a ROBOT may be
pre-loaded with CLIPS; **(c)** any historical or measured winning-score distribution, so `S_win = 150` is a model
estimate with **no external check of any kind** — and `SCORING-PATTERNS.md` §B.11, which holds the inflation curve,
is forbidden for this run; **(d)** the program's cash ceiling (item 4). Only (c) is serious, and (c) is a design
failure of the *allowed-file list*, not of the bundle: **`S_win` is the denominator of `V1`, which carries 30 % of
Axis V and did most of the discriminating work in §8.2. The rubric's heaviest factor rests on a number the harness
gives the analyst no way to check.**

**8. What worked and should be kept.** The **two-run A/B reweighting is the best thing in this instrument** — it
produced a genuine swap (**C3 is a STRETCH GOAL for the A team and a TRAP for the B team; C6 is rank 4 for A and
rank 1 for B**) arithmetically instead of by argument, and the non-contention guardrail independently confirmed the
same pairing that R3's throughput arithmetic reached from the opposite direction. The **minimum viable floor earned
its keep three separate times**: MF5 killed the two candidates whose totals looked perfectly healthy (C9 at
`A = 80`; C2 with the second-highest AY on the slate), and **MF4 caught C10 by exactly one point** (119 vs 120).
The **mandatory contrarian slate is the single most valuable feature of D1** — X1, X3 and X5 all looked plausible
on kickoff morning and all three died to five lines of arithmetic (C4 gives up 4 points per cycle to buy 0.7 s;
C8's AUTO ceiling is capped by the same round trip that caps TELEOP; C10 costs the pair 60 points). **Without the
mandatory slate, none of the three would have been priced at all** — and one of them is the shape a lot of teams
build.

**9. The overriding beta result, stated plainly.** `ACHIEVABILITY-RUBRIC.md` §8 — an **allowed** file — contains
the complete answer key for this exact exercise: four ITD candidates with their A scores, their V scores and their
quadrant assignments. `ACHIEVABILITY-FACTORS.md` §8.1 contains three of them again, with per-factor ratings and the
conclusion spelled out. **The D5 phase of this beta test therefore cannot validate the harness**, because I read
the answer before I scored. Everything *else* generalised cleanly: the bundle format assumed nothing about the
game, the arithmetic conventions ported without a single edit, the gates and floor rules fired correctly on a game
they were not written for, and the two-run rubric produced a defensible pair of robots and a defensible pair of
fallbacks. **But before 2026-09-12, the calibration runs in §11–§13 of the rubric and §8.1 of the factors file must
be moved into a separate `CALIBRATION.md` that the kickoff protocol does not read.** They are excellent teaching
material and they are poison in the analyst's context window. Otherwise every future run — including the real one —
is scored by someone who already knows the answer, and nobody will be able to tell.
