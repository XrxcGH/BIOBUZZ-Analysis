# FREIGHT FRENZY — FTC 2021-22 — Season Dossier

**Sources.** Game Manual Part 2 – Traditional Events, Rev 1.2 (10/19/2021), 46 pp — the game.
Game Manual Part 1 – Traditional Events, Rev 1.5 (2/23/2022), 70 pp — robot/tournament.
Official Q&A archive (Traditional), compiled 12/16/2021, 2,427 lines.
Point values below come from the geometry-extracted §4.7 Scoring Summary table (PDF p.28) and were
independently re-read in the §4.5.2 / §4.5.3 / §4.5.4 prose. Every value matched both ways.

Label key: **[MANUAL]** the text says it · **[DERIVED]** arithmetic, operands shown · **[JUDGMENT]** my read.

---

## 1. The game in five sentences

[MANUAL §4.2.2] Two two-team Alliances play on a 12 ft × 12 ft field, and the Alliance with the higher
Score wins. Robots collect *Freight* — 2 in. Boxes, 2.75 in. Cargo balls, and rubber Ducks — from two
Alliance-Neutral *Warehouses* in the far corners and score it on their own three-level *Alliance Shipping
Hub*, on the contested *Shared Shipping Hub* between the Warehouses, or in their *Storage Unit*
[MANUAL §4.4, §4.5.3]. In the 30-second Autonomous Period a randomization step places a Duck or the team's
own *Team Shipping Element* on one of three *Barcode* squares, and putting your Pre-Loaded Box on the
matching Hub level is worth a large bonus [MANUAL §4.5.2.4]. In the last 30 seconds — the *End Game* —
Alliances spin a corner *Carousel* to Deliver Ducks onto the floor, Cap their Hub with the Team Shipping
Element, and fight over which side of the Shared Shipping Hub is tipped down onto the tile
[MANUAL §4.5.4]. Because Ranking Points at a Traditional event are literally your Alliance's final score
[MANUAL Part 1 §4 "Ranking Points"], qualification ranking is a pure offence race with no win bonus at all.

---

## 2. Match structure

| Segment | Length | Notes |
|---|---|---|
| Pre-Match setup + randomization | untimed | Field randomized *after* the referee's set-up signal [MANUAL §4.5.1.3.c] |
| Autonomous Period | 0:30 | Pre-programmed only; built-in 30-s timer mandatory [MANUAL §4.4, §4.5.1.2.d.ii] |
| Transition | 0:08 | 5 s + a "3-2-1-go" countdown [MANUAL §4.4 "Match", §4.5.3] |
| Driver-Controlled Period | 2:00 | [MANUAL §4.4] |
| — of which End Game | last 0:30 | A sub-window of Driver-Controlled, not a separate period [MANUAL §4.4 "End Game"] |
| **Total** | **2:38 wall clock / 2:30 scored play** | See discrepancy note below |

- **Internal inconsistency [MANUAL].** §4.4 ("Match") states 30 s + 8 s + 2:00 = **2:38**. The §4.5
  Gameplay preamble states the periods total **2:30**. Both are literally in the manual. They reconcile only
  if 2:30 is read as scored play and 2:38 as wall clock [JUDGMENT].
- **vs. 2020-21 ULTIMATE GOAL: unchanged.** The prior manual carries the identical 30 s Auto / 2:00
  Driver-Controlled / last-30-s End Game structure [MANUAL 2020-21 Part 2 §4.4] and the identical
  score-as-Ranking-Points scheme with TBP1 = Auto and TBP2 = End Game [MANUAL 2020-21 Part 1 §4].
  2021-22 inherited the whole scaffolding and changed only the game inside it [DERIVED].
- **Traditional vs. Remote.** Remote fields had **one** Carousel and **one** Alliance Shipping Hub, no
  Shared Shipping Hub, and correspondingly no `<GS7>d/e` or `<GS10>` opponent-interaction clauses
  [MANUAL Remote Part 2 §4.4, §4.6.3]. Traditional is the primary reference throughout this dossier.

---

## 3. Scoring table

Source: §4.7 Scoring Summary table, PDF p.28, recovered by `tools/extract-tables.py` (geometry).
Cross-verified line-by-line against §4.5.2 / §4.5.3 / §4.5.4 prose. **All achievements are Scored at Rest**
[MANUAL §4.7 header]. This era's manuals do not number their tables — cite by section and page.

| Scoring achievement | AUTO | TELEOP | END GAME | Manual ref |
|---|---:|---:|---:|---|
| Carousel: Delivering a Duck | 10 | — | — | §4.5.2.1 |
| Parking: Robot **In** Storage Unit | 3 | — | — | §4.5.2.2a |
| Parking: Robot **Completely In** Storage Unit | 6 | — | — | §4.5.2.2b |
| Parking: Robot **In** Warehouse | 5 | — | — | §4.5.2.2c |
| Parking: Robot **Completely In** Warehouse | 10 | — | — | §4.5.2.2d |
| Freight Completely In Storage Unit | 2 | — | — | §4.5.2.3a |
| Freight Completely On Alliance Shipping Hub (**any level**) | 6 | — | — | §4.5.2.3b |
| Auto Bonus: Pre-Load Box on randomized Level, detected via **Duck** | 10 | — | — | §4.5.2.4a |
| Auto Bonus: Pre-Load Box on randomized Level, detected via **TSE** | 20 | — | — | §4.5.2.5 (table) / §4.5.2.4b |
| Freight Completely In Storage Unit | — | 1 | — | §4.5.3.1a |
| Freight On Alliance Shipping Hub — Level 1 | — | 2 | — | §4.5.3.1b |
| Freight On Alliance Shipping Hub — Level 2 | — | 4 | — | §4.5.3.1b |
| Freight On Alliance Shipping Hub — Level 3 | — | 6 | — | §4.5.3.1b |
| Freight On Shared Shipping Hub (your side) | — | 4 | — | §4.5.3.1c |
| Duck **or** Team Shipping Element Delivered | — | — | 6 | §4.5.4.1 |
| Alliance Shipping Hub: **Balanced** | — | — | 10 | §4.5.4.2a |
| Shared Shipping Hub: **Unbalanced in your favour** | — | — | 20 | §4.5.4.2b |
| Parking In a Warehouse | — | — | 3 | §4.5.4.3a |
| Parking Completely In a Warehouse | — | — | 6 | §4.5.4.3b |
| Capping: each Team Shipping Element (max 2 per Alliance) | — | — | 15 | §4.5.4.4 |
| **Minor Penalty** (to the offending Alliance) | −10 | −10 | −10 | §4.5.6 |
| **Major Penalty** (to the offending Alliance) | −30 | −30 | −30 | §4.5.6 |

**Notes that change the arithmetic**

- *Ducks are Freight.* "Freight consists of Cargo, Boxes, and Ducks" [MANUAL §4.4]. A Delivered Duck is
  therefore also scoreable on a Hub at 2/4/6 or the Shared Hub at 4. The Team Shipping Element is **not**
  Freight and has zero Score value anywhere except as a Cap [MANUAL §4.4; Q&A Q94].
- *Level does not matter in Auto.* Auto Freight on the Alliance Hub is 6 points regardless of level
  [MANUAL §4.5.2.3b]; the same placement on Level 1 in teleop is 2 [MANUAL §4.5.3.1b].
- *Both Warehouses count in End Game.* Auto Parking specifies the Warehouse **closest to your Alliance
  Station** [MANUAL §4.5.2.2c/d]; End Game Parking does not, and either Alliance-Neutral Warehouse scores
  [MANUAL §4.5.4.3; Q&A Q122].
- *Empty Hubs still balance.* An empty, Balanced Alliance Shipping Hub earns the 10 points [Q&A Q27].
- *Shared Hub scores by side, not by scorer.* Freight a red robot places on the blue semicircle scores for
  **blue** [MANUAL §4.5.3.1]. Freight spanning both semicircles is worth zero [MANUAL §4.5.3.1c].
- *Negative scores floor at zero* for ranking purposes [MANUAL Part 1 §5.2].
- **UNVERIFIED — does the Pre-Load earn both the 6-point Auto Hub row and the Auto Bonus?** The §4.7 table
  lists them as separate achievements and §4.5.2.3b / §4.5.2.4 are separate items, which reads as stacking
  (6 + 20 = 26) [JUDGMENT]. Q&A Q106 confirms only the adjacent case — that a bonus-earning Pre-Load plus a
  *second, different* Freight both score. I found no ruling on the Pre-Load itself double-counting. Treat
  26 as unconfirmed; the safe floor is 20.

---

## 4. Bonuses, randomization and ranking

### Randomization

| Item | Detail |
|---|---|
| Mechanism | After the referee signals set-up complete, field personnel randomize to one of **three** configurations, chosen by the scoring system or a **dice throw** [MANUAL §4.5.1.3.c] |
| Dice mapping | 1 or 4 → Scoring Level 1 · 2 or 5 → Level 2 · 3 or 6 → Level 3 [MANUAL Appendix D-1, rendered p.42] |
| Distribution | 2/6 = **1/3 each**, uniform [DERIVED from the dice mapping] |
| Reveal | Physical — the Duck (or TSE) is moved onto Barcode square #1, #2 or #3; the robot must see it with a camera or sensor [MANUAL §4.2.3.1, §4.5.2.4] |
| Numbering | From the corresponding Alliance Station's viewpoint the **leftmost** square is #1 [Q&A Q131] |
| Barcodes | Four locations, three taped squares each [MANUAL §4.4] — two per Alliance, one per starting spot [MANUAL Figure 4.3-2, p.8] |
| Lock-out | Once randomization begins, touching your Robot or Driver Station is a Minor Penalty **and forfeits the Auto Bonus for that robot only** [MANUAL `<GS11>`, added in Rev 1.2] |

**Which object goes on the Barcode is a team choice.** The TSE may be placed on your centre Barcode (the
Duck then moves to the Loading Dock) or kept in the Loading Dock, leaving the Duck on the Barcode
[MANUAL §4.5.1.2.c]. Detecting with the TSE pays 20; detecting with the Duck pays 10.

**Guessing is legal.** A robot that lands the Pre-Load on the correct level *by chance*, with no detection
attempt at all, still earns the Bonus [Q&A Q66].

> [DERIVED] Expected Auto Bonus with no vision, guessing one level at random:
> TSE on Barcode → 20 × (1/3) = **6.67**; Duck on Barcode → 10 × (1/3) = **3.33**.
> Putting the TSE on the Barcode **doubles the expected bonus for zero engineering effort**, and rises to a
> guaranteed 20 once detection works. Working TSE detection is worth 20 − 6.67 = **13.3 pts per robot**
> over guessing, i.e. **26.6 per Alliance**.

### Ownership / multiplier mechanics

There are no multipliers this season. The three flat terminal bonuses are:

| Bonus | Value | Contested? | Determination |
|---|---:|---|---|
| Alliance Shipping Hub **Balanced** | 10 | No (yours alone) | Only the dome base touching the floor; determined solely by the weight and position of the Hub, Scored Freight and Scored TSEs [MANUAL §4.4, `<GS3>`b] |
| Shared Shipping Hub **Unbalanced your way** | 20 | **Yes, zero-sum** | Your semicircle contacting the tile floor [MANUAL §4.5.4.2b] |
| **Capping** | 15 × up to 2 | Semi-protected | TSE fully Supported by the centre pole above Level 3 [MANUAL §4.5.4.4] |

Robot contact at the end of the Match flips these deterministically [MANUAL `<GS3>`b]: your robot touching
your own Hub → **Unbalanced** (you lose the 10); an opponent's interference with your Hub → **Balanced**
(you get the 10 anyway); a robot interfering with the Shared Hub → Unbalanced **in favour of its opponent**,
and if both Alliances interfere, **neither** scores the 20.

### Ranking

| Element | Definition |
|---|---|
| Ranking Points (RP) | Your **Alliance's final score** for the Match. Total RP = sum over all non-Surrogate Quals [MANUAL Part 1 §4] |
| TBP1 | Your Alliance's **Autonomous Period score** [MANUAL Part 1 §4] |
| TBP2 | Your Alliance's **End Game specific task score** [MANUAL Part 1 §4] |
| Sort order | Total RP → TBP1 → TBP2 → random electronic selection [MANUAL Part 1 §5.1] |
| Penalties | Subtracted at end of Match; a negative Match score is recorded as **zero** [MANUAL Part 1 §5.2] |
| League Tournaments | Top 10 league-meet Matches + top 5 league-Tournament Matches, sorted by §5.1 [MANUAL Part 1 §5.3] |
| Eliminations | No RP — win/loss/tie only; first Alliance to two wins advances, ties replayed [MANUAL Part 1 §4.10] |
| Alliance size | 2 teams in Quals; semi-finals and finals run 3-team Alliances at events with 21+ teams, 2 playing per Match [MANUAL §4.4 "Alliance"] |

**There is no win bonus.** [DERIVED] Beating the opponent 200–0 and losing 200–201 award the identical
200 RP. Qualification ranking in FREIGHT FRENZY is a scoring rate contest, full stop.

---

## 5. The rules that shaped play

### Penalty tiers

Minor = **−10**, Major = **−30**, Warning = 0 [MANUAL §4.5.6]. Yellow Cards are additive; a second Yellow
auto-converts to Red [MANUAL §4.4 "Penalty"].

> [DERIVED] Priced in cycles at teleop rates: a Minor Penalty = 2.5 Shared-Hub scores (4 pts) or
> 1.67 Level-3 scores (6 pts). A **Major Penalty = 5 Level-3 cycles**, or the entire Balance-plus-one-Cap
> package (10 + 15 = 25). Almost every rule that touches an opponent's Game Element is a Major.

### Game-specific rules (§4.6.3)

| Rule | What it constrains | Threshold | Penalty |
|---|---|---|---|
| `<GS1>` | Exceptions to `<G22>` (Loading Dock contact) and `<G12>` (TSE placement/retrieval) | — | none |
| `<GS2>`a/b | Descoring opponent's Storage Unit / Carousel | per Scoring Element | Minor |
| `<GS2>`c/d | Descoring opponent's Alliance Hub / their Shared Hub side | per Scoring Element | **Major** |
| `<GS3>`a | Intentionally relocating **your own** Alliance Hub | "affects gameplay" — deliberately unquantified | **Major** |
| `<GS3>`b | Balance determined by weight/position only; robot-contact flip rules | at End of Match | scoring flip, no points |
| `<GS3>`c | Interacting with Shared Hub during Autonomous | any interaction | Minor |
| `<GS3>`d | Relocating/rotating the Shared Hub | intentional + affects gameplay | **Major** |
| `<GS3>`e | Interfering with opponent's Alliance Hub or their Shared Hub side | each offence | **Major** |
| `<GS4>`a | Placing a TSE on the Shared Hub | each offence | **Major** |
| `<GS4>`b | Interfering with an opponent's Capping attempt | End Game only [Q&A Q96] | Cap awarded to them **+** Minor; does not stack past 2 caps [Q&A Q96] |
| `<GS4>`c | Controlling an opponent's TSE (incl. parking on top of it) | each offence [Q&A Q171] | **Major** |
| `<GS5>`a | Warehouse Operations sequence: Completely Out → Completely In → collect 1 → Completely Out | strict ordering | Minor |
| `<GS5>`b | Must be Completely Outside the Warehouse to Score | — | Minor |
| `<GS6>` | Launching Scoring Elements (Carousel-fall exempt) | each offence | Minor |
| `<GS7>`a/c | Placing items on the Carousel / contacting an element on it | each offence | Minor |
| `<GS7>`b | Contacting the top or bottom of the Carousel Platform — **Rim only** | immediate, **+ Minor every 5 s** | Minor+ |
| `<GS7>`d/e | Touching opponent's Carousel, or their robot while it contacts a Carousel | each offence | **Major** |
| `<GS8>` | **Possession limit: one (1) Freight + one (1) TSE** | Plowing OK, Herding is not | Minor per excess element, **+ Minor per element every 5 s** |
| `<GS8>`b | Scoring while over the limit | each element | **Major**, escalates to Yellow |
| `<GS8>`c/d | Already-Scored Freight exempt; Auto contact with your own floor-resting Barcode object = Plowing | — | none |
| `<GS9>`a | Must let a Delivered Duck/TSE touch the floor before Controlling it | each offence | Minor |
| `<GS9>`b/c/e/f/g/h | Delivery-sequence integrity: Carousel-only introduction, no Drive-Team Carousel contact in Auto, one object at a time, Sweeper-Plate contact required, hands off once spinning | each offence | **Major** |
| `<GS9>`d | Delivery only in Autonomous or End Game | each offence | Minor **and zero Delivery points** (Rev 1.2 downgraded this from Major) |
| `<GS10>` | Interfering with opponent's Scoring during Autonomous | each occurrence | **Major** |
| `<GS11>` | Touching Robot/Driver Station after randomization begins | — | Minor **+ that robot forfeits the Auto Bonus**; partner unaffected |

### General rules that mattered most

| Rule | Substance |
|---|---|
| `<G14>` / `<RG02>` | 18 × 18 × 18 in starting cube; **unlimited expansion after the start**; a Pre-Load may protrude [MANUAL; Q&A Q102 confirms nothing else may] |
| `<G21>` | Human control during Auto, or stopping Auto code early → **Major** and *all* achievements in that window score zero |
| `<G25>` | May not grab/grasp/attach to any Game Element other than Scoring Elements — Warning then **Major**. This is why the Hubs, Barriers and Carousel could not be gripped |
| `<G26>` | Destruction/damage/tipping — Major + Yellow for deliberate or chronic |
| `<G28>` | Pinning/Trapping/Blocking > 5 s → Minor **every 5 s**; must retreat ≥ 3 ft (~1.5 tiles). The 5 s is a grace period to withdraw, explicitly *not* licence to block for 5 s |
| `<G29>` | Using Game Elements to ease or amplify Scoring, or to amplify an opponent's difficulty — **Major**, then Yellow |
| `<G30>` | Egregious behaviour — Major + Yellow and/or Red, escalating to Team Disqualification |
| `<G3>` | Forcing an opponent to break a rule carries no penalty for the victim — this protected scoring robots being shoved into their own Hub [Q&A Q140] |

**Rev 1.2 changes shipped at Kickoff release** [MANUAL revision history, p.3]: Capping capped at two TSEs per
Alliance; `<GS9>`d downgraded Major → Minor with zero Delivery value; `<GS8>`d rewritten; `<GS11>` added.

---

## 6. Robot archetypes that season

### The build envelope [MANUAL Part 1]

| Constraint | Value | Rule |
|---|---|---|
| Starting size | 18 × 18 × 18 in, self-supporting in the sizing tool, power off or via an Init routine | `<RG02>` |
| Expansion | Unlimited after Match start | `<RG02>`, `<G14>` |
| Weight | **No robot weight limit found in Part 1** (grep for "weight" returns only unrelated hits); no TSE weight limit either [Q&A Q19] | — |
| DC motors | **Max 8**, from a closed list (TETRIX, AndyMark NeveRest, MR/MATRIX, REV HD Hex, REV Core Hex) | `<RE10>` |
| Servos | Max 12, ≤ 6 V, 3-wire | `<RE11>` |
| Control | Control Hub **or** allowed phone + Expansion Hub, **plus at most one more Expansion Hub**; any number of SPARK Minis and Servo Power Modules | `<RE08>`, `<RE09>` |
| TSE | 3×3×4 in min, 4×4×8 in max; no electronics; may not resemble this season's Freight | `<TE02>`, `<TE04>`, `<TE05>` |

**The eight-motor budget is the binding constraint** [DERIVED]: a holonomic drivetrain consumes 4, leaving 4
for intake, lift, carousel and cap. Every archetype below is really a claim about how to spend those four.

### Archetypes

| Archetype | Mechanism | Motor cost | Points it unlocks | Manual basis |
|---|---|---:|---|---|
| **Hub cycler** | Fast holonomic drive + active intake + linear/virtual-four-bar lift clearing **14.75 in** to Level 3 + dump servo | ~3 beyond drive | 6/cycle | §4.4 Hub Level 3 height; §4.5.3.1b |
| **Shared-Hub sprinter** | Same intake, **no lift** — the Shared Hub is a flat 18 in disc adjacent to the Warehouse border | ~1 beyond drive | 4/cycle + drives the 20-pt tip | §4.4 Shared Hub; Figure 4.3-2 |
| **Duck spinner** | One wheel pressed against the Carousel **Rim** — `<GS7>`b makes touching the top or bottom a Minor+ | **1** | up to 10 (Auto) + 54 (End Game) | `<GS7>`b; §4.5.2.1; §4.5.4.1 |
| **Capper** | Gripper reaching above Level 3 that leaves the TSE fully Supported by the pole — must "encompass and obscure" the pole tip | ~1–2 | 15 × 2 = 30 | §4.5.4.4; Q&A Q47, Q40 |
| **Auto vision** | USB webcam on the Control Hub + TensorFlow trained on the team's own TSE | 0 | +10/robot over the canned Duck model | §4.2.3.1; `<RE12>`; Q&A Q126 |
| **Barrier crosser** | Ground clearance / ramp geometry to cross the 1 in × 5.5 in Barrier | 0 | route flexibility; avoids `<GS5>`a traps | §4.4 Barrier; Q&A Q124 A3 |

### The rule that dictated the mechanical answer

`<GS5>`a forces **Completely Out → Completely In → collect one → Completely Out**. The Q&A closed the obvious
workaround: extending a linear-slide intake to grab Freight *before* the robot is fully inside breaks the
b→c ordering and earns a Minor [Q&A Q110]. Reach was therefore actively penalised and **full-body entry was
mandatory**, which prizes drivetrain speed, low profile and Barrier clearance over arm reach [JUDGMENT].

Two further Q&A rulings sharpened this into a real design tax:

- Freight that a robot accidentally knocks out of the Warehouse still earns a `<GS5>`a Minor if the robot
  then leaves with a different piece [Q&A Q101, Q74]. Sloppy intakes leak −10s.
- The Barrier "is considered an open path of travel for **all** Robots, even if the Robot is not capable of
  travelling over the Barrier" [Q&A Q124 A3]. A robot that could not cross the Barrier was still held to the
  standard of one that could — a pure penalty on low-clearance designs.

Meanwhile `<GS8>`'s one-Freight limit forbade the multi-element hopper that would otherwise be the obvious
answer to a Warehouse full of 38 loose pieces [DERIVED: 20 Cargo + 26 Light + 20 Medium + 10 Heavy = 76
pieces of non-Pre-Load, non-Duck Freight; "approximately half" per Warehouse ≈ 38; and Q&A Q159 confirms it
sits **evenly spread within a single corner tile**]. Single-piece cycling was the only legal mode.

---

## 7. The strategic lesson

**The lesson: when Ranking Points equal raw score, the terminal flat bonuses — not the cycle rate — decide
the season, and FREIGHT FRENZY priced its last 30 seconds higher than its middle 90.**

### Where the points actually were

[DERIVED] Per-Alliance End Game ceiling, all values from §4.5.4:

| End Game component | Points | Operands |
|---|---:|---|
| Duck Delivery | 54 | 9 Ducks × 6 — **the manual's own arithmetic**, Q&A Q114 states the 10 + 54 = 64 total |
| Capping | 30 | 2 TSE × 15 (§4.5.4.4 caps it at two) |
| Shared Hub Unbalanced | 20 | flat |
| Alliance Hub Balanced | 10 | flat |
| Parking | 12 | 2 robots × 6 Completely In |
| **Total** | **126** | |

*Duck accounting* [DERIVED, corroborated by Q&A Q114]: 10 Ducks per Alliance — 1 on the Carousel, 1 on each
of the Alliance's **two** Barcodes, 7 in the Loading Dock [MANUAL §4.5.1.1.d; Figure 4.3-2 shows two Barcodes
per Alliance]. If both robots put their TSE on their Barcode, both displaced Ducks join the Dock: 7 + 2 = **9
available for End Game Delivery**, plus the Carousel Duck already Delivered in Auto for 10. Q114 states this
exact total: 10 + 54 = 64.

Note also that these five components **contend for two robots and 30 seconds**: the Carousel robot cannot
also be Capping, and a robot Capping must release and clear its own Hub before the buzzer or `<GS3>`b flips
the Hub to Unbalanced and eats the 10 [MANUAL `<GS3>`b.i]. 126 is a ceiling, not a plan [JUDGMENT].

Compare a flawless 90-second teleop cycling run at a very good 6 s/cycle to Level 3: 90 ÷ 6 = 15 cycles ×
6 pts = **90 points** [DERIVED]. The End Game ceiling exceeds a perfect teleop run by 40%, and it double-counts
into TBP2. Auto's ceiling similarly feeds TBP1. **Both tiebreakers reward the two short periods and neither
rewards the long one.**

### The four underpriced objectives

1. **End Game Ducks, at 6 points for a one-motor mechanism.** Nine Ducks is 54 points from a wheel pressed
   against a plastic rim, gated only by how fast a human can reload the Carousel — and `<GS9>`e allows one
   Duck at a time, `<GS7>`b restricts contact to the Rim, and Q&A Q31 confirms the robot need not separate
   between Ducks. The engineering cost is the lowest of any 50-point block in the game [JUDGMENT].
2. **The TSE on the Barcode, even with no vision.** 20 × 1/3 = 6.67 expected vs 10 × 1/3 = 3.33 [DERIVED],
   free, and Q&A Q66 explicitly blesses lucky guesses. A rookie team with no camera should still have put
   the TSE out there. There is no evidence in the manual that this was widely understood [JUDGMENT].
3. **Auto Freight on Level 1.** Auto pays **6 points regardless of level** [MANUAL §4.5.2.3b]; the same
   3-inch-high placement in teleop pays 2 [MANUAL §4.5.3.1b]. A lift-less robot could bank 6-point Freight in
   Auto and 4-point Freight on the Shared Hub in teleop, never once reaching 14.75 inches [DERIVED].
4. **Box weight as the Shared Hub lever.** Heavy Boxes are 4.78 oz vs Light 1.79 oz — **2.67×** [DERIVED
   from §4.4 Freight masses]. The 20-point Unbalance is decided purely by "the weight and position of the
   Hub, the Scored Freight, and the Scored Team Shipping Elements" [MANUAL `<GS3>`b]. §4.2.3.3a names
   weight-sensing as an explicit season technology challenge. Sorting Heavy Boxes onto your Shared-Hub side
   was a directly rules-endorsed path to a flat 20 that appears to have gone largely unexploited [JUDGMENT].

### The two overrated strategies

1. **The Storage Unit is dominated on every axis** [DERIVED]. Teleop Freight there is **1 point** vs 4 on the
   Shared Hub and 6 on Level 3. Auto Navigation Completely In the Storage Unit is **6** vs **10** Completely
   In the Warehouse — and the Warehouse park also leaves you parked on top of the Freight pile when teleop
   starts. There is no configuration in which the Storage Unit is the right target.
2. **Defence has strictly negative expected value in qualification** [DERIVED + JUDGMENT]. RP is your own
   Alliance's score [MANUAL Part 1 §4]; suppressing the opponent moves your RP by exactly zero while costing
   you cycle time. And the Q&A converged on defence being legal-on-paper but punished in practice: an
   eight-question chain (Q133 → Q140 → Q151 → Q175, plus Q171, Q137, Q177, Q178) answers "no rule broken"
   and then adds *"Referees will likely escalate this type of repeated defensive activity to a violation of
   rule G30 for egregious behavior. There is also a potential for violating rule G26"* [Q&A Q137, Q140].
   That is an unstable equilibrium: zero ranking upside, unbounded card downside.

### The genuine ambiguity of the season

Q&A density by rule (mentions across the compiled archive): **`<GS3>` 22 · `<GS5>` 21 · `<GS4>` 9 ·
`<GS9>` 8 · `<GS8>` 7 · `<GS2>` 5**. The two hot spots are the two rules every scoring robot touched on
every cycle.

The marquee case is `<GS3>`a, "Inadvertent and Inconsequential" Alliance Hub movement. Asked to quantify the
threshold, the Game Design Committee **refused on purpose**: the answer states the Committee "deliberately
does not quantify" it, because the same displacement toward a Warehouse is a strategic advantage while the
same displacement away from it may be Inconsequential — and then twice offers the Pro Tip that "the Drivers
Meeting is a good opportunity to discuss how rule `<GS3>` will be applied at the tournament" [Q&A Q104, Q177,
Q178]. A **Major Penalty (−30, five Level-3 cycles)** hung on a threshold the manual explicitly declined to
define, on the one Game Element every robot must approach ~15 times a match. That is the season's real
ambiguity, and the per-event variance it created is the thing worth remembering [JUDGMENT].

The second is `<GS5>` Warehouse Operations, where the crucial economic ruling is Q117: improperly-removed
Freight **remains eligible to be Scored**, and the Q&A says outright that the penalty "offsets the future
Scoring potential." So `<GS5>` is a **tax, not a nullification** — but at −10 against a 4-to-6-point cycle it
is a tax you can never profitably pay [DERIVED].

---

## 8. Signals for BIOBUZZ

1. **Read the ranking formula before reading the scoring table.** FREIGHT FRENZY's entire strategic shape
   follows from RP = your Alliance's final score, with TBP1 = Auto and TBP2 = End Game. If BIOBUZZ ranks on
   score, defence is worthless in Quals and the tiebreaker periods are worth double. If BIOBUZZ has returned
   to a win-based RP (as 2024-25 and 2025-26 did), that inverts and defence becomes purchasable.
2. **Compute the terminal-bonus ceiling against a perfect cycling run on day one.** Here it was 126 vs 90
   [DERIVED]. Any season where flat End Game bonuses beat a flawless teleop run is a season where the
   low-mechanism, high-value endgame device out-earns the cycling machine.
3. **Hunt for the level-flattening clause.** "6 points regardless of Level" in Auto vs 2/4/6 in teleop was a
   free 3× for lift-less robots. Every manual has at least one place where a period-specific rule collapses a
   difficulty gradient. Grep the Auto section against the teleop section, row by row.
4. **Price every penalty tier in cycles immediately.** Minor −10 = 1.67 top-goal cycles; Major −30 = 5. Once
   penalties are denominated in cycles, "is this strategy worth the risk" becomes arithmetic instead of vibes.
5. **Compute the expected value of the randomized bonus under pure guessing.** 6.67 vs 20 here. It tells you
   how much the vision work is actually worth and whether a no-vision fallback is viable.
6. **Q&A density is the ambiguity map.** Sort the Q&A archive by rule-tag frequency in the first six weeks.
   The top two tags are where your referees will disagree with the next event's referees, and they are the
   rules to raise at the Drivers Meeting — the Q&A itself said so, twice.
7. **Watch for a physical property of the game pieces that a flat bonus depends on.** Three Box weights
   feeding a 20-point tip contest was a fully-specified, rules-endorsed edge sitting in plain sight
   [MANUAL §4.4, §4.2.3.3a, `<GS3>`b]. Read the Game Element mass and dimension table as a strategy document,
   not as reference data.
8. **A possession limit of one is a mechanical mandate, not a footnote.** `<GS8>`'s one-Freight cap plus
   `<GS5>`'s full-body-entry sequence together forbade the hopper-and-reach robot and forced fast, compact,
   low chassis. Find the possession limit and the collection-sequence rule early; between them they specify
   most of the drivetrain.

---

## 9. Extraction notes

### Rule counts

| Manual | Pages | Distinct tags present | Parser found | Recall | With a Violation line |
|---|---:|---:|---:|---:|---:|
| Part 2 Traditional | 46 | **44** — G:30, GS:11, S:3 | **23** — G:21, GS:2, S:0 | **52%** | 16 of 23 |
| Part 1 Traditional | 70 | **90** | **90** — C:28, DS:9, I:7, RE:17, RG:8, RM:6, RS:10, TE:5 | **100%** | 2 of 90 |

Tag **occurrences** in the raw text: Part 2 = **118** (parser saw 53, missing 55%); Part 1 = **196**
(parser saw 196). Part 1's occurrence spread by prefix: RE 54, C 35, RS 33, RG 25, DS 19, I 11, TE 10, RM 9.

The 2-of-90 Violation rate on Part 1 is expected, not a defect: Part 1 rules are construction and inspection
rules that state consequences in prose without a "Violation:" or "Penalty:" lead-in. The `VIOLATION` regex
matches `(Violation|VIOLATION|PENALTY|Penalty)`, so it has almost nothing to hit. Part 2's 16-of-23 is the
meaningful figure. One Part 1 rule, `C10`, extracted with **no body** and was flagged by the tool itself.

### Tooling defects found on this manual

1. **`tools/parse-legacy-manual.py` silently drops every single-digit rule tag.** The regex is
   `RULE_TAG = re.compile(r"<([A-Z]{1,3})(\d{2,3})>")` — it requires **two or more** digits. FREIGHT FRENZY
   Part 2 numbers its rules `<G1>`…`<G30>`, `<GS1>`…`<GS11>`, `<S1>`…`<S3>`, so **21 of 44 distinct tags
   were never seen**: G1–G9, GS1–GS9, S1–S3. This is silent — the tool reported a clean
   `rules=23 (G:21 GS:2)` with no warning. Note that the missing rules include `<GS1>`–`<GS9>`, i.e. **nine
   of the eleven game-specific rules**, which are the most strategically important rules in the manual.
   The docstring itself advertises `<S01>` / `<RS01>` two-digit forms, so the assumption is baked in at the
   design level. **Fix: `(\d{1,3})`.** Part 1 is unaffected (it zero-pads: `RG02`, `RE10`, `TE01`), so a
   `--all` sweep would show healthy numbers and hide the defect. Expect the same failure on any season that
   does not zero-pad — worth re-sweeping the 2017-24 corpus after the fix.
2. **`--tsv` and `--json` never write, and report a phantom missing file.** In `main()`, `pdfs` is built as
   `[a for a in argv if not a.startswith("-")]` **before** `take()` strips the flag values out of `argv`, so
   the output path is collected as a second positional PDF. Result: the tool prints
   `### MISSING <your-tsv-path>`, `len(pdfs)` becomes 2, and the `if tsv_out and len(pdfs) == 1` guard is
   false, so nothing is written and the exit code is 1. Reproduced on both Part 1 and Part 2. This is
   order-independent — moving the flag does not help. Worked around by importing the module and calling
   `parse()` directly. **Fix: run `take()` before building `pdfs`.**
3. **`tools/extract-tables.py` worked correctly but every table came back "(no caption on page)".** The
   caption heuristic looks for a nearby `Table N-M:` string; this era's manuals **do not number their
   tables** — the Scoring Summary is just "4.7 Scoring Summary" and the Rule Summary is "4.8 Rule Summary".
   Not a data error, but it means legacy tables must be cited by section and PDF page. Recovered 10 tables
   from 46 pages, including the full Scoring Summary (p.28) and the six-page Rule Summary (pp.29–34), with
   **no row/value mis-pairing** — every row label kept its number. Verified independently against §4.5 prose.
4. **Geometry extraction emits phantom empty columns.** The Scoring Summary came back as 21 × **15** for a
   logically 5-column table, and the p.29 Rule Summary as 20 × **18** for a 6-column table. Values are
   correct and correctly paired; the extra columns are empty spacers from the PDF's cell geometry. Any
   downstream consumer must drop all-empty columns before parsing.
5. `pymupdf` prints an advisory on every run — *"Consider using the pymupdf_layout package for a greatly
   improved page layout analysis."* Cosmetic; it appears on stdout ahead of the result line, so a script
   parsing the first line of output would break.
6. `tools/render-pages.py` worked with no issues (pages 8 and 42 at 130 dpi). Appendix D is an
   **image-only** page — the dice-roll → Scoring-Level mapping exists nowhere in the extracted text and was
   recoverable only by rendering. Any legacy season's randomization scheme should be assumed to be
   image-only until a render proves otherwise.

### Manual-content defects

7. **The Match length is stated two different ways.** §4.4 "Match": 30 s + 8 s transition + 2:00 = **2:38**.
   §4.5 Gameplay preamble: periods "totaling two minutes and thirty seconds (**2:30**)". Both in Rev 1.2.
8. **Section-reference drift in the Scoring Summary.** The §4.7 table cites the TSE Auto Bonus row as
   **4.5.2.5**, but §4.5.2 has no item 5 — the TSE bonus is item **4)b** of §4.5.2. The Duck row correctly
   cites 4.5.2.4. Flagged because the table's Reference column is otherwise reliable and a harness that
   trusts it would follow a dead link.
9. The extracted plain text mangles the `<G15>`/`<G16>` region: the §4.8 Rule Summary table's cell text is
   interleaved into the §4.6.2 rule bodies in the flat `.txt`. The geometry-extracted table is clean; the
   flat text is not. Another reason to use `extract-tables.py` for anything tabular in this era.

### Files produced

- `...\scratchpad\ff_p2.tsv` (+ `.json`) — 23 Part 2 rules
- `...\scratchpad\ff_p1.tsv` (+ `.json`) — 90 Part 1 rules
- `...\scratchpad\ff_tables\TABLES.md` / `tables.tsv` / `INDEX.txt` — 10 geometry-recovered tables
- `...\scratchpad\ff_fig\p008_page.png` (field top view), `p042_page.png` (Appendix D randomization)
