# FTC Scoring Architecture: Cross-Season Study (2005-06 - 2025-26)

**Purpose.** The analytical backbone for the BIOBUZZ (2026-27) kickoff strategy review. Every number below was
pulled from the actual manual text in this corpus. Use Part C on kickoff day.

**Built:** 2026-08-21 | **Extended to the full 21-season corpus 2026-08-22 (Part D)** | **Corpus root:** ``

**Layout.** **Part A** = season-by-season architecture, 2015-16 → 2025-26. **Part B** = the synthesis.
**Part C** = the kickoff-day question list. **Part D** = the pre-2015 era (2005-06 → 2014-15), which corrects
the left edge of several Part B trend tables. Companions: `FIELD-AND-ARENA.md` (the geometry those points sit
on) and `TOURNAMENT-AND-RANKING.md` (what a match score is worth in ranking and advancement).

## Evidence labels used throughout

| Label | Meaning |
|---|---|
| **[C]** CONFIRMED-FOR-BIOBUZZ | Present in the BIOBUZZ V0 pre-season manual (already-final sections) |
| **[H]** HISTORICAL-PATTERN | Read directly out of one or more prior-season manuals; a *pattern*, not a BIOBUZZ fact |
| **[D]** DERIVED | My arithmetic on manual-stated point values. Inputs are cited; the total is mine |
| **[S]** SPECULATION | Reasoned guess. Never treat as fact |
| **UNVERIFIED** | Could not be established from this corpus |

> **Hard rule for kickoff day:** no number in Part A or B is a BIOBUZZ number. BIOBUZZ point values do not exist
> until 2026-09-12. Sections 8, 9, 10, 11, 13 and 15 of the V0 manual are placeholders reading "This section will
> be updated with the Kickoff Competition Manual release on September 12, 2026"
> (`manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` lines 2285-2306, 3516, 3557).

---

# PART A - Season-by-season scoring architecture

## A.0 Source map

| Season | Primary source in corpus | Scoring section |
|---|---|---|
| 2015-16 RES-Q | `manuals/archive/wayback/2015-16_RESQ_GameManual_PartII.txt` | 1.5.2-1.5.6, 1.7 |
| 2016-17 VELOCITY VORTEX | `.../wayback/2016-17_VELOCITYVORTEX_GameManual_Part2.txt` | 1.5.2-1.5.6 |
| 2017-18 RELIC RECOVERY | `.../wayback/2017-18_RELICRECOVERY_GameManual_Part2.txt` | 1.5.2-1.5.6 |
| 2018-19 ROVER RUCKUS | `.../wayback/2018-19_ROVERRUCKUS_GameManual_Part2.txt` | 1.5.2-1.5.6 |
| 2019-20 SKYSTONE | `.../wayback/2019-20_SKYSTONE_GameManual_Part2.txt` | 4.5.2-4.5.6 |
| 2020-21 ULTIMATE GOAL | `manuals/archive/2020-21_ULTIMATEGOAL_GameManual_Part2_Traditional.pdf` | 4.5.2-4.5.6 |
| 2021-22 FREIGHT FRENZY | `manuals/archive/2021-22_FREIGHTFRENZY_GameManual_Part2_Traditional.txt` | 4.5.2-4.5.6 |
| 2022-23 POWERPLAY | `manuals/archive/2022-23_POWERPLAY_GameManual_Part2_Traditional.txt` | 4.4.2-4.4.6 |
| 2023-24 CENTERSTAGE | `manuals/archive/2023-24_CENTERSTAGE_GameManual_Part2_Traditional.txt` | 4.4.2-4.4.6 |
| 2024-25 INTO THE DEEP | `manuals/archive/2024-25_INTO_THE_DEEP_Competition_Manual_V14.txt` | 10.4-10.6, Table 10-3 |
| 2025-26 DECODE | `manuals/archive/2025-26_DECODE_Competition_Manual_TU32.txt` | 10.4-10.6, Tables 10-2/10-3 |
| Q&A rulings | `manuals/archive/supplemental/*_Complete_QA.html` | cited by Q number |

Ranking-system citations come from the matching Part 1 manual (pre-2024) or Section 13 (2024+).

---

## A.1 2015-16 RES-Q - *traverse / climb archetype*

**Match structure [H]:** 30 s Autonomous + 2:00 Driver-Controlled; final 0:30 of DC = End Game. Total 2:30.
(PartII 1.5.2, 1.5.4)

| Achievement | AUTO | Driver-Ctrl | End Game | Notes |
|---|---|---|---|---|
| Rescue Beacon triggered (per trigger) | 20 | - | - | 1 beacon/alliance, up to 2 triggers (1 per robot) = 40 max |
| Climber In Shelter (each) | 10 | 10 | - | **Re-counted at end of DC** -> auto climber = 20 total |
| Zip Line Climber (each) | - | 20 | - | |
| Debris - Floor Goal | - | 1 | - | |
| Debris - Low Zone Goal | - | 5 | - | |
| Debris - Mid Zone Goal | - | 10 | - | |
| Debris - High Zone Goal | - | 15 | - | Top cycle value |
| Robot Parked - tile floor + Mountain | 5 | 5 | - | |
| Robot Parked - Low Zone | 10 | 10 | - | |
| Robot Parked - Mid Zone | 20 | 20 | - | |
| Robot Parked - High Zone | 40 | 40 | - | |
| Rescue Beacon Repair Zone / Floor Goal park | 5 | - | - | AUTO only |
| Cliff Pull-up Bar (hanging, per robot) | - | - | **80** | Largest single-robot award in the corpus |
| All Clear Signal (per Mountain) | - | - | 20 | Max 2/alliance = 40 |

**Bonus / risk mechanics [H]**
- **Randomized objective:** Rescue Beacon LED randomization; pressing the wrong button awards **20 points to the
  opposing alliance** (1.5.2.1). Earliest example of *randomized target with a wrong-answer gift to the opponent*.
- Only the highest-value robot position scores (`<G22>`).
- De-scoring Debris from Mountain Goals prohibited (`<GS15>`); de-scoring a Climber zeroes both Zip Line
  achievements (`<GS16>`).
- **Penalties:** Minor = **+10 to opponent**, Major = **+40 to opponent** (1.5.6).

**AUTO fixed ceiling [D]** approx. 140 (40 beacon + 20 climbers + 80 two-robot High Zone park).
**End Game fixed ceiling [D]** = 200 (2x80 cliff + 2x20 signal).

**Ranking [H]:** QP/RP era. QP = 2 win / 1 tie / 0 loss. RP = *the losing alliance's pre-penalty score*, awarded to
both alliances. Ladder: QP -> RP -> highest match score -> next-highest -> random.
(`2015-16_RESQ_GameManual_PartI.txt` L506-535)

**Typical winning score:** UNVERIFIED (not stated in manual or corpus).

---

## A.2 2016-17 VELOCITY VORTEX - *cycle-the-element + randomized beacon*

**Match structure [H]:** 30 s AUTO + 2:00 DC, last 0:30 = End Game (Part2 1.5, L530-532).

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Beacon claimed (per beacon) | 30 | 10 (end-state) | - |
| Cap Ball knocked to floor | 5 | - | - |
| Particle -> Center Vortex | **15** | **5** | - |
| Particle -> Corner Vortex | 5 | 1 | - |
| Park On Center Vortex Base | 5 | - | - |
| Park **Completely** On Center Vortex Base | 10 | - | - |
| Park On / Completely On Corner Vortex | 5 / 10 | - | - |
| Cap Ball raised, low (< 76 cm) | - | - | 10 |
| Cap Ball raised, high (> 76 cm) | - | - | 20 |
| Capping (Cap Ball supported by Center Vortex) | - | - | 40 |

**Bonus / risk mechanics [H]**
- **Randomized objective:** Beacons. The alliance whose colour shows at the end of AUTO gets 30 **regardless of
  which robot pressed it** - pressing wrong gives the opponent 30.
- **Auto -> teleop carry:** each claimed Beacon released a **bonus Particle** onto the field for the DC period
  (max 2). A rare *resource* bonus rather than a point bonus.
- Teleop beacons **toggle** on every press - over-pressing hands the beacon to the opponent.
- Pre-load: alliance must stage 3 alliance-specific Particles; each robot may pre-load up to 2 (1.5.1 L549-557).
- **Penalties:** Minor +10 / Major +40 to opponent.

**AUTO fixed ceiling [D]** approx. 85 (2 beacons 60 + cap ball 5 + 2 robots parked completely 20), plus up to 45
from 3 pre-loaded Particles into the Center Vortex -> ~130.
**End Game ceiling [D]** = 40 (one Cap Ball per alliance).
**AUTO premium:** Center-Vortex particle is **3x teleop value** (15 vs 5).

**Ranking [H]:** identical QP/RP scheme to RES-Q (`Part1.txt` L716-768).
**Typical winning score:** UNVERIFIED.

---

## A.3 2017-18 RELIC RECOVERY - *stack/build + set completion*

**Match structure [H]:** 30 s AUTO + 2:00 DC (5 s hand-off), last 0:30 = End Game (1.5.2-1.5.4).

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Jewel - correct one removed (per platform) | 30 | - | - |
| Glyph In Cryptobox | **15** | **2** | - |
| Cryptobox Key column bonus (first glyph, correct column) | 30 | - | - |
| Robot Parked In Safe Zone | 10 | - | - |
| Completed Row (3 glyphs across) | - | 10 | - |
| Completed Column (4 glyphs) | - | 20 | - |
| Completed Cipher (all 12, correct arrangement) | - | 30 | - |
| Relic In Recovery Zone 1 / 2 / 3 | - | - | 10 / 20 / **40** |
| Relic upright bonus | - | - | +15 |
| Robot Balanced on Balancing Stone | - | - | 20 |

**Bonus / risk mechanics [H]**
- **Two randomized objectives:** the **Pictograph / VuMark** selects the Key Column; the **Jewel** order is
  randomized. Removing the wrong Jewel hands 30 to the opponent.
- **Set completion, compounding:** manual worked example - 12 glyphs = 24 (glyphs) + 40 (rows) + 60 (columns)
  = **124**, and a valid Cipher adds 30 -> **154** per Cryptobox (1.5.3 item 5). The marginal value of the 12th
  glyph is far higher than the 1st.
- **Early-unlock mechanic:** completing a Cipher before End Game lets you score one Relic *early* - a rare
  "set completion unlocks the endgame" reward.
- **Penalties:** Minor +10 / Major +40 to opponent.

**AUTO fixed ceiling [D]** = 170 (2x30 jewel + 2x30 key + 2x15 pre-load glyph + 2x10 park).
**End Game ceiling [D]** = 150 (2 relics x 55 + 2 robots x 20).
**AUTO premium: 7.5x** - the largest in the corpus (glyph 15 in AUTO vs 2 in teleop), and the AUTO glyph *also*
feeds the row/column/cipher bonuses at the end. Pre-load: exactly 1 glyph per robot (1.5.1 L545).

**Ranking [H]:** QP/RP era, unchanged.
**Typical winning score:** UNVERIFIED.

---

## A.4 2018-19 ROVER RUCKUS - *traverse/hang + randomized vision sample*

**Match structure [H]:** 30 s AUTO + 2:00 DC, last 0:30 = End Game (1.5.2-1.5.4).

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Landing (lowering from the Lander) | **30** / robot | - | - |
| Claiming (Team Marker In Depot) | 15 / robot | - | - |
| Sampling (correct Gold Mineral displaced) | 25 / Sample Field | - | - |
| Parking In a Crater | 10 / robot | - | - |
| Mineral Scored into Depot | - | 2 (-2 if removed) | - |
| Gold -> Gold Cargo Hold / Silver -> Silver | - | 5 | - |
| Wrong Cargo Hold ("Contaminant") | - | 0 | - |
| Robot **Latched** on Lander bracket | - | - | **50** / robot |
| Robot Parked In any Crater | - | - | 15 / robot |
| Robot Parked **Completely** In any Crater | - | - | 25 / robot |

**Bonus / risk mechanics [H]**
- **Randomized objective:** Sampling - the Gold Mineral's position among 3 is randomized; the TensorFlow/vision
  era begins. Displacing the wrong mineral simply forfeits the 25 (no gift to the opponent - a softening vs 2015-17).
- **Proto-ownership:** a **Completely Claimed Depot** becomes permanent and blocks opponent de-scoring from it
  for the rest of the match - the first "lock it and it is yours" mechanic.
- **Risk:** Latching (50) is all-or-nothing and physically fragile; failing it usually forfeits the crater park too.
- **Penalties:** Minor +10 / Major +40 to opponent.

**AUTO fixed ceiling [D]** = 160 (2x30 land + 2x15 claim + 2x25 sample + 2x10 park).
**End Game ceiling [D]** = 100 (2x latch).
**AUTO premium:** no per-element multiplier; AUTO is entirely a **fixed-task bounty** (160 pts, approx. 32 teleop
minerals). Pre-load: Team Marker only, no minerals (1.5.1 L527).

**Ranking [H] - ERA CHANGE.** RES-Q through Relic Recovery used QP/RP. **Rover Ruckus renamed them Ranking
Points (2 win / 1 tie / 0 loss) and TieBreaker Points (losing alliance's pre-penalty score)** - same math, new
names. Ladder: RP -> TBP -> highest match score -> next-highest -> random draw.
(`2018-19_ROVERRUCKUS_GameManual_Part1.txt` L651-705)
**Typical winning score:** UNVERIFIED.

---

## A.5 2019-20 SKYSTONE - *stack/build; the deflation season*

**Match structure [H]:** 30 s AUTO + 2:00 DC, last 0:30 = End Game (4.5.2-4.5.4).

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Repositioning (Foundation In Building Site) | 10 | - | - |
| First two Stones Delivered - if **Skystones** | **10** each | - | - |
| First two Stones Delivered - if plain Stones | 2 each | - | - |
| Remaining Stones Delivered | 2 each | 1 each | - |
| Stone Returned (de-delivered) | -2 (-10 if first is a Skystone) | -1 | - |
| Navigating (Parked on Loading/Building tape) | 5 / robot | - | - |
| Placing (Stone In the Foundation) | 4 each | 1 each | - |
| Skyscraper Bonus (tallest tower, per Level) | - | 2 / level | - |
| Capping - Capstone Supported | - | - | 5 each |
| Capping - per Level supporting a Capstone | - | - | 1 / level |
| Foundation Moved Completely Out of Building Site | - | - | 15 |
| Parking In Building Site | - | - | 5 / robot |

**Bonus / risk mechanics [H]**
- **Randomized objective:** Skystone identification (vision) - 10 vs 2 for the first two deliveries, a **5x premium**
  for getting the vision task right, but only on 2 stones.
- **Negative scoring:** the only season in the corpus with explicit **point deduction for undoing your own work**
  (Stone Returned -2 / -10 in AUTO, -1 in teleop).
- **Risk:** Foundation Moved (15) at End Game frequently topples the Skyscraper you just built - the manual even
  calls this out and defers Skyscraper/Placing/Capstone scoring until the field comes to rest (4.5.4 note).
- **Penalties halved:** Minor **+5** / Major **+20** (4.5.6) - half of every other season, consistent with a deflated
  point economy.

**AUTO fixed ceiling [D]** approx. 40 + deliveries. **End Game ceiling [D]** approx. 50.
**Point economy:** by far the lowest in the corpus - a teleop stone is worth **1 point**.

**Ranking [H]:** RP/TBP, now **averaged**, with low-score drops: "Average TieBreaker Points ... subtracting the
lowest scoring Match (5-6 Matches, one Match is subtracted; 7 or more, two are subtracted)".
Ladder: Avg RP -> Avg TBP -> highest match score -> random.
(`2019-20_SKYSTONE_GameManual_Part1.txt` L735-800)
**Typical winning score:** UNVERIFIED.

---

## A.6 2020-21 ULTIMATE GOAL - *cycle/launch + repeatable precision target*

**Match structure [H]:** 30 s AUTO + 2:00 DC, last 0:30 = End Game (4.5.2-4.5.4). COVID season: Remote and
Traditional manuals both exist; values below are the **Traditional** manual.

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Wobble Goal Completely In its Target Zone | 15 each | - | - |
| Robot Navigating (In the Launch Line) | 5 / robot | - | - |
| Ring -> Low Goal | 3 | 2 | - |
| Ring -> Mid Goal | 6 | 4 | - |
| Ring -> High Goal | **12** | **6** | - |
| Power Shot Target knocked Back | **15** each (x3) | - | **15** each (x3) |
| Wobble Goal In the Start Line | - | - | 5 |
| Wobble Goal Supported by the Drop Zone | - | - | 20 |
| Ring Completely Supported by a Wobble Goal | - | - | 5 each |

**Bonus / risk mechanics [H]**
- **Randomized objective:** the **Starter Stack** (0, 1 or 4 Rings) selects Target Zone A/B/C for Wobble Goal
  delivery - a vision task cued by a *variable-height stack* (Appendix D).
- **Repeatable one-time target:** Power Shots pay 15 in AUTO **and again** 15 in End Game after the Human Player
  resets them - 90 points/alliance available from three static targets. The best points-per-second in the corpus if
  you can land three shots in a few seconds.
- **Anti-defense clause:** "A Power Shot Target knocked Down by an Opposing Alliance Robot by any means counts
  as Scored" for the *owning* alliance. Defending a Power Shot is strictly self-harming.
- Illegally Scored Rings / Power Shots **still score** but carry an offsetting penalty (`<GS12>`, `<GS13>`).
- **Penalties flip sign:** Minor **-10 / Major -30 subtracted from the offender** (4.5.6) - first season of
  subtract-from-offender.

**AUTO fixed ceiling [D]** = 85, plus up to 72 from 6 pre-loaded Rings into the High Goal (3/robot, 4.5.1 L529)
-> approx. 157. **End Game ceiling [D]** approx. 85 + wobble rings.
**AUTO premium: 2x** on every ring.

**Ranking [H] - THE OUTLIER SEASON.** RP = **your own alliance's final match score**, not win/loss. TBP1 = your
AUTO score; TBP2 = your End Game task score. Ladder: Total RP -> TBP1 -> TBP2 -> random. This was done so
remote (solo) and traditional play were comparable.
(`2020-21_ULTIMATEGOAL_GameManual_Part1_Traditional.pdf` 3.4 + 5.1)
**Typical winning score:** UNVERIFIED.

---

## A.7 2021-22 FREIGHT FRENZY - *cycle + tug-of-war ownership*

**Match structure [H]:** 30 s AUTO + 120 s DC, last 0:30 = End Game (4.5.2-4.5.4).

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Carousel - deliver the pre-placed Duck | 10 | - | - |
| Navigating - In / Completely In Storage Unit | 3 / 6 | - | - |
| Navigating - In / Completely In Warehouse | 5 / 10 | - | - |
| Freight Completely In Alliance Storage Unit | 2 | 1 | - |
| Freight Completely On Alliance Shipping Hub (any level) | 6 | - | - |
| Freight On ASH Level 1 / 2 / 3 | - | 2 / 4 / **6** | - |
| Freight Completely On Shared Shipping Hub | - | 4 | - |
| Autonomous Bonus - pre-load box on Barcode level, **Duck** cue | **10** | - | - |
| Autonomous Bonus - same, **Team Shipping Element** cue | **20** | - | - |
| Duck / TSE Delivered to the floor | - | - | 6 each |
| Alliance Shipping Hub **Balanced** | - | - | 10 |
| Shared Shipping Hub tipped in your favour | - | - | **20** |
| Parked In / Completely In a Warehouse | - | - | 3 / 6 |
| Capping (TSE above Level 3) | - | - | 15 each, max 2 |

**Bonus / risk mechanics [H]**
- **Randomized objective:** the **Barcode** selects ASH level #1/#2/#3. **First appearance of the "bring your own
  randomization object" doubler**: 10 points using the field-supplied Duck, **20** using your custom Team Shipping
  Element. This doubler then repeated in 2022-23 and 2023-24.
- **Contested ownership:** the Shared Shipping Hub is a physical tug-of-war - 20 to whichever alliance has it
  tipped onto their tile at the end; the neutral "Balanced" state pays only 10 to each ASH owner.
- **Risk:** capping a TSE (15) requires reaching above Level 3, competing directly with cycle time.
- **Penalties:** Minor **-10** / Major **-30** subtracted from offender (4.5.6).

**AUTO fixed ceiling [D]** = 70 (carousel 10 + 2x10 warehouse + 2x20 auto bonus) + 12 pre-load freight = ~82.
**End Game ceiling [D]** approx. 10 + 20 + 12 + 30 + ducks.
**AUTO premium:** identical per-freight value in AUTO and teleop on the ASH (6 vs 6) - the premium lives entirely
in the fixed bounties. Pre-load: **exactly one** Pre-Load Box per robot (4.5.1 L612).

**Ranking [H]:** still score-based. RP = alliance's final score; TBP1 = AUTO score; TBP2 = End Game task score.
Ladder: Total RP -> TBP1 -> TBP2 -> random.
(`2021-22_FREIGHTFRENZY_GameManual_Part1_Traditional.txt` L397-437, L963-972)
**Typical winning score:** UNVERIFIED.

---

## A.8 2022-23 POWERPLAY - *pure cycle game; ownership + circuit*

**Match structure [H]:** 30 s AUTO + 120 s DC, last 0:30 = End Game (4.4.2-4.4.4).

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Navigating - Parked In Substation or nearest Terminal | 2 / robot | - | - |
| Cone In matching-colour Terminal | 1 | 1 | - |
| Cone Secured on **Ground** Junction | 2 | 2 | - |
| Cone Secured on **Low** Junction | 3 | 3 | - |
| Cone Secured on **Medium** Junction | 4 | 4 | - |
| Cone Secured on **High** Junction | **5** | **5** | - |
| Signal Bonus - field-supplied Signal | 10 / robot | - | - |
| Signal Bonus - **Team Signal Sleeve** | **20** / robot | - | - |
| Junction Ownership via top Scored Cone | - | - | 3 / junction |
| Junction Ownership via **Beacon** (Capping) | - | - | 10 / junction |
| Circuit (continuous Owned path, Terminal to Terminal) | - | - | 20 (once) |
| Navigating - Parked In either Terminal | - | - | 2 / robot |

Field has 25 Junctions: 9 Ground, 8 Low, 4 Medium, 4 High (4.3 L361-373).

**Bonus / risk mechanics [H]**
- **Randomized objective:** Signal image 1/2/3 -> Signal Zone. Custom Sleeve doubles the bonus (10 -> 20).
- **Ownership is contested until the buzzer:** whoever's cone is *on top* owns the junction - an opponent stacking
  one cone flips 3 points. A **Beacon Cap** (10) makes ownership **permanent and un-flippable**; subsequent cones
  on a capped junction score zero.
- **Circuit** is the season's set-completion mechanic: 20 points for a connected chain of owned junctions linking
  your two Terminals. A single flipped junction destroys it.
- **Penalties revert:** Minor **+10** / Major **+30 credited to the non-offender** (4.4.6).

**AUTO fixed ceiling [D]** = **50** (2x20 Signal Bonus + 10 for 2 pre-load cones on High).
*Correction (verified 2026-08-22 against Part 2 Traditional 4.4.1):* Navigating and the Signal Bonus are
**mutually exclusive per robot** - Navigating pays for Parking In the Substation/Terminal, the Signal Bonus for
Parking **Completely In** a Signal Zone, so one robot cannot earn both. The nav 2s do **not** add to the signal 20s.
**End Game realistic [D]** approx. 30-45 ownership + 20 circuit + 20 beacons + 4 nav.
**AUTO premium: zero on the nominal table** - cone values are identical in AUTO and teleop (5/5) - **but auto
cones re-score at the end of the DC period**: "Cones that are Scored in the Autonomous Period will earn
additional points at the end of the Driver-Controlled Period if they remain in place" (4.4.2). So an AUTO
high-junction cone is worth 10. Pre-load: **exactly one** Cone per robot (4.4.1 L598).

**Ranking [H] - the win/loss revert.** Traditional events: RP = 2 win / 1 tie / 0 loss (remote events kept
score-as-RP). TBP1 = AUTO score, TBP2 = End Game score, everything **averaged**.
Ladder: Avg RP -> Avg TBP1 -> Avg TBP2 -> random.
(`2022-23_POWERPLAY_GameManual_Part1_Traditional.txt` L409-461, L1032-1036)
**Typical winning score:** UNVERIFIED.

---

## A.9 2023-24 CENTERSTAGE - *cycle + set completion + AprilTag randomization*

**Match structure [H]:** 30 s AUTO + 120 s DC, last 0:30 = End Game (4.4.2-4.4.4).

| Achievement | AUTO | Driver-Ctrl | End Game |
|---|---|---|---|
| Navigating (Park In Backstage) | 5 / robot | - | 5 / robot |
| Randomization - purple Pixel on designated Spike Mark, white-Pixel cue | 10 | - | - |
| Randomization - same, **Team Prop** cue | **20** | - | - |
| Randomization - yellow Pixel on Backdrop at matching location, white-Pixel cue | 10 | - | - |
| Randomization - same, **Team Prop** cue | **20** | - | - |
| Pixel On the Backdrop | **5** | **3** | - |
| Pixel In the Backstage | **3** | **1** | - |
| Mosaic (cluster of 3 non-white Pixels) - Artist Bonus | - | 10 each | - |
| Set Bonus (Pixels crossing a horizontal Set Line) | - | 10 / line, **max 30** | - |
| Robot **Suspended** from the Rigging | - | - | 20 (1 robot per Rigging) |
| Drone Launched -> Landing Zone 1 / 2 / 3 | - | - | **30** / 20 / 10 |

**Bonus / risk mechanics [H]**
- **Randomized objective:** first season using **AprilTags for the randomization task** - 3 tags on each Backdrop
  identify target columns, plus wall tags for localization (4.3 L216-220). Team Prop doubler (10 -> 20), the third
  consecutive season of the custom-object doubler.
- **Two stacked set-completion mechanics:** Mosaics (spatial clusters, uncapped) and Set Bonus (height
  thresholds, capped at 30). Both reward *arrangement*, not just count.
- **Risk:** Suspension (20) is all-or-nothing; a failed hang forfeits the 5-point park as well. Drone launch (30) must
  clear the Truss / Stage Door and land in the far zone.
- **AUTO carries over:** "Pixels that are Scored in the Autonomous Period will earn additional points at the end of
  the Driver-Controlled Period if they remain in place" (4.4.2) -> an AUTO Backdrop pixel is worth 5 + 3 = **8**.
- **Penalties:** Minor +10 / Major +30 to non-offender (4.4.6).

**AUTO fixed ceiling [D]** approx. 90-100 (2x5 park + 2x40 randomization + the pixel values of those same pixels).
**End Game ceiling [D]** = 100 (2x20 suspend + 2x30 drone).
Pre-load: exactly one yellow Pixel and/or one purple Pixel per robot, plus one Drone (4.4.1 L613-617).

**Ranking [H]:** unchanged from POWERPLAY - Avg RP (2/1/0) -> Avg TBP1 (AUTO) -> Avg TBP2 (End Game) -> random.
(`2023-24_CENTERSTAGE_GameManual_Part1_Traditional.txt` L465-517, L1122-1126)
**Typical winning score:** UNVERIFIED.

---

## A.10 2024-25 INTO THE DEEP - *the architecture reset*

**Match structure [H]:** 30 s **AUTO** + **8-second transition** + 2:00 **TELEOP**. **There is no End Game period.**
MATCH cycle time 6-10 min/field (10.1, 10.4). This is the season FTC adopted the FRC-style manual: ALL-CAPS
defined terms, `G`/`R`/`T` rule numbering, MINOR/MAJOR FOUL, RANKING SCORE.

**Table 10-3 point values** (extracted from the PDF table, `2024-25_INTO_THE_DEEP_Competition_Manual_V14.pdf` p.66):

| Achievement | AUTO | TELEOP | RP |
|---|---|---|---|
| PARK - OBSERVATION ZONE | 3 | 3 | |
| SAMPLE - NET ZONE | 2 | 2 | |
| SAMPLE - LOW BASKET | 4 | 4 | |
| SAMPLE - **HIGH BASKET** | **8** | **8** | |
| SPECIMEN - LOW CHAMBER | 6 | 6 | |
| SPECIMEN - **HIGH CHAMBER** | **10** | **10** | |
| ASCENT LEVEL 1 (contact LOW RUNG) | 3 | 3 | |
| ASCENT LEVEL 2 (fully supported by RUNGS) | - | **15** | |
| ASCENT LEVEL 3 (above the LOW RUNG on the HIGH RUNG) | - | **30** | |
| Tie | | | 1 |
| Win | | | 2 |

**Bonus / risk mechanics [H]**
- **NO randomized objective at all.** AprilTags (36h11, IDs 11-16) sit outside the FIELD perimeter for
  *localization only* (9.8). First season since 2015-16 with no vision-selected target. This matters for BIOBUZZ
  forecasting - see B.6.
- **No multipliers, no set completion, no ownership.** The flattest scoring table in the corpus.
- **The AUTO premium is entirely double-counting.** Q&A **Q21** (`2024-25_ITD_Complete_QA.html`): *"A SCORING
  ELEMENT which meets the scoring criteria at the end of the AUTO period and still meets scoring criteria at the
  end of the TELEOP period will be counted in both MATCH periods."* -> an AUTO HIGH CHAMBER specimen is worth
  **20**, an AUTO HIGH BASKET sample **16**.
- **Risk:** LEVEL 3 ASCENT (30) is all-or-nothing but **retryable** - a failed ascent may disengage and re-attempt.
  A robot eligible for both ASCENT and PARK earns only the higher (10.5.3.D).
- **Penalties:** MINOR FOUL = **+5** to opponent, MAJOR FOUL = **+15** to opponent (Table 10-4) - halved vs the
  10/30 of the prior three seasons.
- Pre-load: **1 SAMPLE or 1 SPECIMEN** per robot (10.3.1). Field stock: 15 red + 15 blue + 30 neutral SAMPLES in
  the SUBMERSIBLE, 20 CLIPS per alliance outside the wall.

**AUTO fixed ceiling [D]** = 6 (2 robots parking or L1 ascent) - the smallest fixed auto bounty in the corpus. All
other AUTO value is cycle-derived and doubled.
**"End Game" ceiling [D]** = 60 (2 x LEVEL 3), available at any point in TELEOP.

**Ranking [H]:** **RANKING SCORE (RS) = average RP**, RP = 2 win / 1 tie. Ladder (Table 13-1):
RS -> Avg ALLIANCE AUTO points -> Avg TELEOP ALLIANCE ASCENT points -> highest MATCH score (including FOULS)
-> random.
**Typical winning score:** UNVERIFIED (no RP thresholds published this season).

---

## A.11 2025-26 DECODE - *cycle + AprilTag pattern + bonus RPs*

**Match structure [H]:** 30 s AUTO + 8 s transition + 2:00 TELEOP; **no End Game period**, but Table 9-1 audio
cues include a **"Final 20 seconds" train whistle at 0:20** - a soft endgame marker with no scoring meaning
(Section 9 Table 9-1, 10.4).

**Table 10-2 point values** (extracted from `2025-26_DECODE_Competition_Manual_TU32.pdf` p.88):

| Achievement | AUTO | TELEOP | RP |
|---|---|---|---|
| **LEAVE** (no longer over any LAUNCH LINE at end of AUTO) | **3** / robot | - | |
| ARTIFACT - **CLASSIFIED** | 3 | 3 | |
| ARTIFACT - OVERFLOW | 1 | 1 | |
| ARTIFACT - DEPOT | - | 1 | |
| **PATTERN** - ARTIFACT matches MOTIF at its index | 2 | 2 | |
| BASE - partially returned | - | 5 | |
| BASE - fully returned | - | 10 | |
| BASE - bonus, **both** ROBOTS fully returned | - | 10 | |
| MOVEMENT RP - LEAVE + BASE points at/above threshold | | | 1 |
| GOAL RP - ARTIFACTS through the SQUARE at/above threshold | | | 1 |
| PATTERN RP - PATTERN points at/above threshold | | | 1 |
| WIN | | | **3** |
| TIE | | | 1 |

**Table 10-3 RP thresholds** - the closest thing in the corpus to a manual-stated expected-performance figure:

| RP Type | FIRST Championship | Regional Championships | All Other Events |
|---|---|---|---|
| MOVEMENT RP | 21 | 21 | 16 |
| GOAL RP | 67 | 42 | 36 |
| PATTERN RP | 22 | 22 | 18 |

**Bonus / risk mechanics [H]**
- **Randomized objective:** the **OBELISK** AprilTag (IDs 21/22/23) selects a 3-colour MOTIF (GPP / PGP / PPG),
  repeated 3x across the 9 RAMP indices (10.5.2).
- **Live vs end-of-period scoring is the whole game.** Q&A **Q27**: CLASSIFIED/OVERFLOW are assessed **as the
  artifact passes through the SQUARE** and are *not* recounted, so AUTO artifacts do **not** double. But Q&A
  **Q129**: an ARTIFACT "is eligible for PATTERN points at the end of AUTO **and/or** end of TELEOP" - so PATTERN
  **does** double. AUTO's exclusive value = LEAVE (6) + a doubled PATTERN (up to 18).
- **Risk mechanic - the GATE:** the RAMP holds roughly 9 CLASSIFIED artifacts; after that everything is OVERFLOW
  at 1 point instead of 3. Opening the GATE dumps the ramp into the **opponent's SECRET TUNNEL ZONE** to restore
  3-point classification - but destroys the PATTERN you built. Cycle rate vs pattern retention is a designed-in
  tension, not an accident.
- 36 ARTIFACTS on the field (24 purple, 12 green) (9.9). Pre-load **up to 3 per robot** (10.3); G408 caps
  simultaneous CONTROL at 3.
- **Penalties:** MINOR FOUL +5 / MAJOR FOUL +15 to opponent. **New penalty type: "ALLIANCE is ineligible for RP"**
  - a rule violation can strip a specific Ranking Point independently of match points (Table 10-4).
- **RP thresholds are recalibrated mid-season from live data.** Team Update (Nov 2025): *"FIRST staff members
  closely evaluated the data from every DECODE match played each week. We then compared scoring trends with
  historical patterns."* (`2025-26_DECODE_TeamUpdates_Combined.pdf`)

**AUTO exclusive ceiling [D]** = 24 (6 LEAVE + 18 doubled PATTERN).
**"End Game" ceiling [D]** = 30 (2x10 BASE + 10 both-robots bonus).

**Ranking [H]:** RS = average RP, where RP is a **sum of up to 6** (3 for a win + 3 bonus RPs). Ladder (Table 13-1):
RS -> Avg MATCH points **excluding FOULS** -> Avg BASE points -> Avg AUTO points -> random.
**Typical winning score:** UNVERIFIED as a stated number. The GOAL RP threshold of **36 artifacts through the
SQUARE at ordinary events** is the manual's own statement of a strong-but-achievable alliance performance.

---

# PART B - Synthesis: the patterns that matter

## B.1 Match clock evolution [H]

| Seasons | AUTO | Transition | Driver / TELEOP | Named End Game | Total |
|---|---|---|---|---|---|
| 2015-16 -> 2023-24 (9 seasons) | 0:30 | 0-5 s + countdown | 2:00 | **last 0:30 of teleop** | 2:30 |
| 2024-25 INTO THE DEEP | 0:30 | **8 s** | 2:00 | **none** | 2:38 clock, 2:30 of play |
| 2025-26 DECODE | 0:30 | **8 s** | 2:00 | **none** (0:20 audio cue only) | 2:38 clock, 2:30 of play |

**Nine consecutive seasons of an identical 30/120/30 clock, then two consecutive seasons with the End Game
period deleted.** The 8-second transition exists "for scoring purposes" (ITD 10.4) - it is the window in which
end-of-AUTO field state is certified.

**[S] Forecast for BIOBUZZ:** 30 s AUTO + 8 s transition + 2:00 TELEOP with no named ENDGAME is the most likely
structure - but verify at kickoff. The V0 manual contains **zero occurrences of "ENDGAME" or "END GAME"**
(`BIOBUZZ_V0_layout.txt`), which is consistent with but not proof of the ITD/DECODE structure, since all game
sections are placeholders.

## B.2 Ranking-system eras [H]

| Seasons | 1st sort | 2nd sort | 3rd sort | 4th sort |
|---|---|---|---|---|
| 2015-16 - 2017-18 | QP (2/1/0) | RP = losing alliance's pre-penalty score | Highest match score | Next-highest, then random |
| 2018-19 | RP (2/1/0) | TBP = losing alliance's score | Highest match score | Next-highest, then random |
| 2019-20 | **Avg** RP (2/1/0) | **Avg** TBP, lowest 1-2 matches dropped | Highest match score | Random |
| 2020-21 | Total RP = **your own score** | TBP1 = AUTO score | TBP2 = End Game score | Random |
| 2021-22 | Total RP = **your own score** | TBP1 = AUTO score | TBP2 = End Game score | Random |
| 2022-23 - 2023-24 | Avg RP (2/1/0) | Avg TBP1 = AUTO | Avg TBP2 = End Game | Random |
| 2024-25 | RS = avg RP (2/1) | Avg **AUTO** points | Avg **ASCENT** points | Highest match score (incl. FOULS), random |
| 2025-26 | RS = avg RP (**3** win / 1 tie **+ 3 bonus RPs**) | Avg match points **excl. FOULS** | Avg **BASE** points | Avg **AUTO** points, random |

**Three durable truths:**
1. **AUTO has been an explicit tiebreaker in every season since 2020-21** (as TBP1, then as a named sort). It is
   the single most reliably rank-relevant sub-score. **[C] This continues into BIOBUZZ:** V0 Table 4-2 Advancement
   Sorting Criteria lists *"7th - Average Qualification AUTO Points"* (`BIOBUZZ_V0_layout.txt` L1026).
2. **The endgame sub-score has been the second tiebreaker in every season since 2020-21** (TBP2, then ASCENT,
   then BASE). Expect a BIOBUZZ endgame-equivalent sub-score to be a named sort criterion.
3. FIRST oscillates between score-as-RP (2020-22, remote-era) and win-as-RP (everything else). The 2025-26
   bonus-RP model (win worth 3, three task RPs worth 1 each) is FRC's model and is the newest.

**[C] BIOBUZZ facts already in V0:** Section 13.6.3 "Qualification Ranking" is referenced by name from Section 4
(L1037) and Table 13-1 is referenced from Section 14 (L3543), so the RS/Table 13-1 architecture survives. Table
4-2's 6th/8th/9th sorts reference *"Qualification MATCH Points (excluding FOULS)"*, matching DECODE's
FOUL-excluding sort rather than ITD's FOUL-including one.

## B.3 Penalty architecture [H]

| Seasons | Minor | Major | Direction |
|---|---|---|---|
| 2015-16 - 2018-19 | 10 | 40 | Added to non-offender |
| 2019-20 | 5 | 20 | Added to non-offender |
| 2020-21 - 2021-22 | 10 | 30 | **Subtracted from offender** |
| 2022-23 - 2023-24 | 10 | 30 | Added to non-offender |
| 2024-25 - 2025-26 | **5** | **15** | Added to non-offender (MINOR/MAJOR FOUL) |

Fouls are worth *less* than ever in absolute terms, but DECODE added a much sharper weapon: **RP ineligibility**,
which can cost a full ranking point regardless of the scoreboard. **[S]** Expect BIOBUZZ to keep 5/15 FOULs plus
RP-stripping violations.

## B.4 Point availability by period [D]

Fixed/capped opportunities only (park, climb, randomization bonuses, one-time set bonuses). Cycle scoring is
unbounded by definition, so it is shown separately as the top per-element value.

| Season | AUTO fixed ceiling (alliance) | Top teleop element value | "Endgame" fixed ceiling (alliance) | AUTO : ENDGAME (fixed) |
|---|---:|---:|---:|---|
| 2015-16 RES-Q | ~140 | 15 (High Zone Debris) | 200 | 41 : 59 |
| 2016-17 VELOCITY VORTEX | ~130 | 5 (Center Vortex) | 40 | 76 : 24 |
| 2017-18 RELIC RECOVERY | 170 | 2 + set bonuses | 150 | 53 : 47 |
| 2018-19 ROVER RUCKUS | 160 | 5 (Cargo Hold) | 100 | 62 : 38 |
| 2019-20 SKYSTONE | ~40 | 1-2 (Stone) | ~50 | 44 : 56 |
| 2020-21 ULTIMATE GOAL | ~157 | 6 (High Goal Ring) | ~85 | 65 : 35 |
| 2021-22 FREIGHT FRENZY | ~82 | 6 (ASH Level 3) | ~72 | 53 : 47 |
| 2022-23 POWERPLAY | 50 | 5 (High Junction Cone) | ~85 | 37 : 63 |
| 2023-24 CENTERSTAGE | ~95 | 3 (Backdrop Pixel) | 100 | 49 : 51 |
| 2024-25 INTO THE DEEP | **6** | 10 (HIGH CHAMBER) | 60 | 9 : 91 |
| 2025-26 DECODE | **24** (LEAVE + doubled PATTERN) | 3 (CLASSIFIED) | 30 | 44 : 56 |

**Read this table as a trend, not as arithmetic precision.** The dominant signal: **fixed AUTO bounties collapsed
after 2020-21.** From 2015-2021 the AUTO period paid 130-170 points of guaranteed, non-cycle work. Since 2022-23
it pays 6-50. FIRST moved the AUTO reward out of "task bounties" and into "your cycles count twice."

## B.5 How FIRST actually pays for autonomous [H] - the single most important pattern

There are exactly **three mechanisms** FIRST has ever used, and knowing which one BIOBUZZ uses changes your
entire robot architecture.

| Mechanism | How it works | Seasons | Size of the prize |
|---|---|---|---|
| **1. Higher per-element AUTO value** | Same action, bigger number in AUTO | Velocity Vortex (3x), Relic Recovery (**7.5x**), Skystone (5x on 2 stones), Ultimate Goal (2x), CENTERSTAGE (1.67x) | Multiplier on the element |
| **2. Fixed AUTO task bounty** | Discrete one-time achievements only available in AUTO | RES-Q, Rover Ruckus (**160 pts**), Freight Frenzy, POWERPLAY (Signal 40), CENTERSTAGE (Randomization 80), DECODE (LEAVE 6) | Flat per-alliance total |
| **3. Double-counting** | AUTO-scored elements are counted again at end of TELEOP | RES-Q Climbers, POWERPLAY Cones, CENTERSTAGE Pixels, **INTO THE DEEP everything** (Q&A Q21), **DECODE PATTERN only** (Q&A Q129) | Effectively **2x** the element |

**Historical size of the AUTO prize, expressed in teleop cycles** [D]:

| Season | AUTO exclusive value | = how many top teleop cycles |
|---|---:|---:|
| 2017-18 RELIC RECOVERY | 170 | ~85 glyphs (absurd - AUTO dominated) |
| 2018-19 ROVER RUCKUS | 160 | 32 minerals |
| 2020-21 ULTIMATE GOAL | ~157 | 26 rings |
| 2015-16 RES-Q | ~140 | 9 high-zone debris |
| 2023-24 CENTERSTAGE | ~95 | 32 pixels |
| 2021-22 FREIGHT FRENZY | ~82 | 14 freight |
| 2022-23 POWERPLAY | 50 (+ auto cones double) | 10 cones |
| 2024-25 INTO THE DEEP | 6 fixed, but every AUTO cycle doubles | a 4-specimen AUTO = 80 pts = 8 teleop cycles |
| 2025-26 DECODE | 24 | 8 artifacts |

**The rule of thumb that has held for 11 seasons:** a competent AUTO is worth **8-30 teleop cycles**, i.e. roughly
**one-quarter to one-half of a whole match's teleop output**, and the trend since 2022 is toward the low end of
that range *unless* double-counting is in play, in which case AUTO cycle rate becomes as valuable as teleop cycle
rate.

## B.6 Randomized-objective mechanics [H]

| Season | Cue | Sensor era | Doubler for team-supplied object? | Wrong answer costs |
|---|---|---|---|---|
| 2015-16 RES-Q | Beacon LEDs | Colour sensor | No | **+20 to opponent** |
| 2016-17 VELOCITY VORTEX | Beacon LEDs | Colour sensor | No | **+30 to opponent** |
| 2017-18 RELIC RECOVERY | Pictograph (VuMark) + Jewel order | VuMark / colour | No | **+30 to opponent** (jewel) |
| 2018-19 ROVER RUCKUS | Gold Mineral position (1 of 3) | TensorFlow object detection | No | Forfeit 25 only |
| 2019-20 SKYSTONE | Skystone position | TensorFlow / VuMark | No | Forfeit 8/stone only |
| 2020-21 ULTIMATE GOAL | Starter Stack height (0/1/4 rings) | Vision | No | Forfeit 15/wobble |
| 2021-22 FREIGHT FRENZY | Barcode position | Vision | **Yes: Duck 10 -> TSE 20** | Forfeit only |
| 2022-23 POWERPLAY | Signal image (1 of 3) | Vision | **Yes: Signal 10 -> Sleeve 20** | Forfeit only |
| 2023-24 CENTERSTAGE | Spike Mark (1 of 3), **AprilTags on Backdrop** | AprilTag | **Yes: white Pixel 10 -> Team Prop 20** | Forfeit only |
| 2024-25 INTO THE DEEP | **NONE** | AprilTags for localization only | n/a | n/a |
| 2025-26 DECODE | **OBELISK AprilTag** (IDs 21/22/23) -> MOTIF | AprilTag | No | Wrong pattern = 0 PATTERN pts |

**Patterns worth knowing:**
- The **punitive** randomization era (wrong answer gifts the opponent points) ran 2015-2018 and has not returned.
  Since 2018 a wrong answer only costs you the bonus.
- The **custom-object doubler** ran three straight seasons (2021-2024) and then stopped for two straight seasons.
- **AprilTags are now the standard randomization carrier.** DECODE used a dedicated OBELISK element with tags
  21/22/23; CENTERSTAGE embedded them in the Backdrop.
- **The randomization payload has migrated from AUTO-only to whole-match.** RES-Q through CENTERSTAGE:
  randomization decided a one-time AUTO bonus. DECODE: the MOTIF defines a **PATTERN that pays in both AUTO
  and TELEOP** and shapes your entire cycle strategy. **[S]** If BIOBUZZ has a randomized element, expect it to
  govern teleop scoring, not just an auto bonus.

## B.7 Season archetypes - what recurs [H]

| Archetype | Seasons | Defining trait |
|---|---|---|
| **Cycle-the-element** | VELOCITY VORTEX, ULTIMATE GOAL, FREIGHT FRENZY, **POWERPLAY**, CENTERSTAGE, INTO THE DEEP, **DECODE** | Uncapped repeat scoring; winner = highest cycle rate |
| **Stack / build / arrange** | RELIC RECOVERY, SKYSTONE, (CENTERSTAGE Mosaics, POWERPLAY Circuit, DECODE PATTERN as sub-mechanics) | Points depend on *arrangement*, not just count |
| **Traverse / park / climb** | RES-Q, ROVER RUCKUS | Field geometry is the challenge; scoring elements are secondary |
| **Randomized-target** | Every season 2015-2024 and 2025-26 as a sub-mechanic; **absent only in 2024-25** | Vision task gates a bonus |

**The trend is unambiguous: 7 of the last 7 seasons have been cycle games**, with arrangement mechanics layered
on top rather than replacing the cycle. Pure traverse/park games have not appeared since 2018-19.

**[S] Prior for BIOBUZZ:** a cycle game with an arrangement/pattern sub-mechanic and a robot-position endgame is
the highest-probability shape. The "BIOBUZZ" name (bio/hive/pollination imagery) is consistent with a
collect-and-deposit cycle game. **Do not commit to this before reading the kickoff manual.**

## B.8 Where the points-per-second has actually lived [D]

Estimates below are DERIVED and use commonly observed cycle times, not manual-stated ones. Treat the ranking
as directional.

| Season | Best sustained teleop rate | Best one-shot / endgame rate | Which won matches |
|---|---|---|---|
| 2015-16 RES-Q | 15 pts / debris cycle | **Cliff hang 80 pts in ~10 s = 8 pts/s** | Endgame. Two cliff hangs (160) outweighed most debris totals |
| 2016-17 VELOCITY VORTEX | 5 pts / particle, fast launcher | Cap 40 in ~15 s = 2.7 pts/s | Cycle rate, with cap as a tiebreaker |
| 2017-18 RELIC RECOVERY | 2 pts / glyph raw, but ~13 pts / glyph marginal at cipher completion | Relic 55 in ~20 s | **Set completion** - a full cipher (154) beat raw stacking |
| 2018-19 ROVER RUCKUS | 5 pts / mineral | **Latch 50 in ~5 s = 10 pts/s** | AUTO (160) + double latch (100) = 260 before a single mineral |
| 2019-20 SKYSTONE | 1-3 pts / stone | Foundation 15 | Cycle rate; the game was so low-value that consistency dominated |
| 2020-21 ULTIMATE GOAL | 6 pts / ring, ~3 rings per cycle | **3 Power Shots = 45 in ~5 s = 9 pts/s** | Power Shots twice (90) rivalled a whole teleop of high goals |
| 2021-22 FREIGHT FRENZY | 6 pts / freight | Shared hub tip 20 | Cycle rate + shared-hub contest |
| 2022-23 POWERPLAY | **5 pts / cone, ~5 s per cycle = 1 pt/s sustained** | Circuit 20, beacons 20 | **Pure cycle rate.** 25-30 cones dwarfed all bonuses |
| 2023-24 CENTERSTAGE | 3 pts / pixel + 10 / mosaic | **Drone 30 in ~2 s = 15 pts/s** | Cycle + mosaic; the drone was the best pts/s in FTC history |
| 2024-25 INTO THE DEEP | **10 pts / specimen, ~5 s = 2 pts/s**; doubled in AUTO | L3 ascent 30 in ~10 s = 3 pts/s | **Cycle rate.** High-chamber specimen cycling beat basket play outright |
| 2025-26 DECODE | 3 pts / artifact, 3 at a time | BASE 30 alliance-wide in ~5 s | Cycle rate; PATTERN as an RP gate rather than a points driver |

**How often did the "obvious" strategy lose to cycle rate?** In the corpus, the pattern is remarkably consistent:

- **The flashy high-value task loses when it is capped and the cycle is not.** POWERPLAY is the cleanest case:
  the entire endgame ownership + circuit + beacon package caps around 80-100 points, while a top cycler put up
  125-150 from cones alone. Teams that built beacon-capping mechanisms at the cost of cycle time lost.
- **INTO THE DEEP is the textbook case.** The HIGH BASKET (8) looked like the premium goal and required a tall
  vertical lift; the HIGH CHAMBER specimen (10) was faster, closer to the human player, and mechanically simpler.
  The "obvious" basket strategy lost to specimen cycling almost everywhere.
- **The exception is when the high-value task is repeatable and cheap.** Ultimate Goal Power Shots (45, twice)
  and CENTERSTAGE drones (30 for a ~2 s action) were correctly-priced and worth building for.
- **Set-completion mechanics beat raw cycling only when the bonus is a large multiple of the element.** Relic
  Recovery (2 pts/glyph raw vs 154 for a full cipher) rewarded arrangement; CENTERSTAGE Set Bonus (capped at 30)
  and DECODE PATTERN (2/artifact) did not change the cycle-first conclusion.

**The generalizable test:** *divide the endgame/bonus ceiling by the time it costs you, and compare with your
cycle rate over that same time.* If the bonus is worth fewer than ~1.5x the cycles it displaces, skip it.

## B.9 Endgame archetypes and their premium [H]

| Archetype | Seasons | Top value | In "top teleop cycles" |
|---|---|---|---|
| **Hang / suspend from a bar** | RES-Q (Cliff 80), Rover Ruckus (Latch 50), CENTERSTAGE (Suspend 20), ITD (L3 Ascent 30) | 20-80 | 3-10 |
| **Climb / ascend a structure** | ITD ASCENT L1/L2/L3 (3/15/30) | 30 | 3 |
| **Park in a zone** | Every season | 3-40 | 1-8 |
| **Cap / place an object at height** | VELOCITY VORTEX (40), SKYSTONE (5+levels), FREIGHT FRENZY (15), POWERPLAY (Beacon 10) | 10-40 | 2-8 |
| **Launch / projectile** | ULTIMATE GOAL Power Shot (15x3), CENTERSTAGE Drone (30) | 30-45 | 5-10 |
| **Ownership / territory** | POWERPLAY (3 or 10 per junction, Circuit 20), FREIGHT FRENZY (Shared Hub 20) | 20-75 | 4-15 |
| **Return to base** | DECODE (10 + 10 bonus) | 30 | 10 |

**Endgame premium over time [D]:** expressed as the endgame ceiling divided by the top teleop element value:

| Season | Endgame ceiling / top element |
|---|---:|
| 2015-16 | 200 / 15 = **13.3** |
| 2018-19 | 100 / 5 = **20.0** |
| 2020-21 | 85 / 6 = 14.2 |
| 2022-23 | 85 / 5 = 17.0 |
| 2023-24 | 100 / 3 = **33.3** |
| 2024-25 | 60 / 10 = 6.0 |
| 2025-26 | 30 / 3 = **10.0** |

**Two conclusions.** (1) The endgame is *always* worth building for - never less than ~6 cycles, usually 10-20.
(2) But in absolute alliance points the endgame has shrunk hard: 200 in RES-Q, 100 in CENTERSTAGE, 60 in ITD,
30 in DECODE. **The 2020s design language treats the endgame as a tiebreaker and a "both robots must
participate" cooperation gate, not as a match-winner.**

**A durable design cue:** every season since 2021-22 has an endgame that **rewards both alliance robots doing the
same thing** (FREIGHT FRENZY dual warehouse park, POWERPLAY dual terminal, CENTERSTAGE one-robot-per-rigging,
ITD two alliance-specific RUNGS, DECODE explicit "both ROBOTS fully returned" +10 bonus). Design your endgame
mechanism assuming your alliance partner also needs the same real estate.

## B.10 Pre-load allowance trend [H] - a direct constraint on the AUTO ceiling

| Season | Pre-load per robot | Source |
|---|---|---|
| 2015-16 RES-Q | 1 Climber | PartII 1.5.1 |
| 2016-17 VELOCITY VORTEX | up to 2 Particles (alliance stages 3) | Part2 1.5.1 L549-557 |
| 2017-18 RELIC RECOVERY | exactly 1 Glyph | Part2 1.5.1 L545 |
| 2018-19 ROVER RUCKUS | 1 Team Marker (no minerals) | Part2 1.5.1 L527 |
| 2019-20 SKYSTONE | 1 Capstone (optional) | Part2 4.5.1 L512 |
| 2020-21 ULTIMATE GOAL | 1 Wobble Goal (required) + up to 3 Rings | Part2 4.5.1 L524-529 |
| 2021-22 FREIGHT FRENZY | exactly 1 Pre-Load Box | Part2 4.5.1 L612 |
| 2022-23 POWERPLAY | exactly 1 Cone | Part2 4.4.1 L598 |
| 2023-24 CENTERSTAGE | 1 yellow and/or 1 purple Pixel + 1 Drone | Part2 4.4.1 L613-617 |
| 2024-25 INTO THE DEEP | 1 SAMPLE **or** 1 SPECIMEN | 10.3.1 |
| 2025-26 DECODE | **up to 3 ARTIFACTS** | 10.3 |

DECODE tripled the pre-load allowance and simultaneously capped in-match CONTROL at 3 (G408) - i.e. the
pre-load was set equal to the robot's carrying capacity. **[S]** Watch for BIOBUZZ to set pre-load = carry capacity
again; if so, AUTO opens with a full magazine and the first cycle is free.

## B.11 Point inflation over time [D]

There is no clean monotonic inflation. Instead there are three distinct economies:

| Era | Typical top element | Typical fixed-task award | Character |
|---|---|---|---|
| **2015-2018 "big numbers"** | 15-30 | 30-80 | Few, expensive achievements. High variance |
| **2019-2022 "deflation and rebuild"** | 1-6 | 10-20 | SKYSTONE bottoms out at 1 pt/stone; UG/FF rebuild to ~6 |
| **2022-2026 "flat and fast"** | 3-10 | 3-30 | Small numbers, high volume. Score comes from cycle count |

**The strategically useful reading:** absolute point *values* have deflated, but *scores* have not, because
element counts and cycle rates rose. A 2016 winning score and a 2026 winning score may look similar while
representing completely different robot capabilities. **Never calibrate your BIOBUZZ expectations from a
prior-season score number.** Calibrate from cycle count.

## B.12 The scored-live vs scored-at-end distinction [H] - the highest-leverage rule in any manual

This determines whether AUTO work compounds, and it is buried in a definitions paragraph, not in the point table.

| Season | Mechanism | Effect on AUTO |
|---|---|---|
| RES-Q | Climbers counted at end of AUTO **and** end of DC | AUTO climber = 20, not 10 |
| POWERPLAY | Explicit: auto Cones "earn additional points at the end of the Driver-Controlled Period" | AUTO high cone = 10, not 5 |
| CENTERSTAGE | Explicit: auto Pixels re-score at end of DC | AUTO Backdrop pixel = 8, not 5 |
| INTO THE DEEP | "scored at the end of each period based on the status of the FIELD" + Q&A Q21 | **Every** AUTO element doubles. AUTO high chamber = 20 |
| DECODE | ARTIFACTS scored **live** at the SQUARE (Q27, no double); PATTERN scored at end of AUTO **and** end of TELEOP (Q129) | Only PATTERN doubles |
| ULTIMATE GOAL | Rings "Scored Live... the moment the Rings are Completely In the Tower Goal" | No double; AUTO premium is the 2x value instead |

**On kickoff day, find the sentence that says when each achievement is assessed before you build your AUTO
routine.** In INTO THE DEEP this one paragraph made AUTO worth double; in DECODE the same-looking paragraph
made it worth nothing extra. Most students will read the point table and stop.

---

# PART C - Kickoff-day scoring-table questions

## C.1 What is already CONFIRMED for BIOBUZZ [C]

| Fact | Source |
|---|---|
| AUTO and TELEOP are the two named MATCH periods; "ENDGAME" appears zero times in V0 | `BIOBUZZ_V0_layout.txt` L2142 (Control Award: "during the AUTO period, the TELEOP period, or both"); zero-hit grep for ENDGAME |
| AUTO points are tracked as a separate, rank-relevant sub-score | Table 4-2 Advancement Sorting, 7th sort: "Average Qualification AUTO Points" (L1026) |
| Match points are reported **excluding FOULS** for sorting | Table 4-2, 6th/8th/9th sorts (L1025-1029) |
| Qualification Ranking lives in Section 13.6.3 and uses a Table 13-1 sort order | Cross-references at L1037, L3543 |
| League Tournament ranking = top 10 League Meet matches + League Tournament matches | Section 14 (L3540-3548) |
| STARTING CONFIGURATION is an 18 in. cube; pre-loaded SCORING ELEMENTS may extend outside it | R102, R104 note (L2475-2484) |
| Expansion limits exist but the numbers are **not yet published** | R105: "Sizing Constraints and more details will be released at Kickoff" (L2521) |
| VERBAL WARNING is a defined penalty tier (carried over from DECODE) | Glossary (L3560+) |
| ROBOT SIGN is a required, defined field-identification element | Glossary; `supplemental/2026-27_BIOBUZZ_RobotSign_USLetter.pdf` |
| The Glossary contains **no** game terms - no HUMAN PLAYER, no SCORING ELEMENT definition, no period lengths | Section 16, 92-93 of 93 |

## C.2 The 18 questions to answer in the first hour after the manual drops

Ordered by strategic leverage.

**Clock and structure**
1. What are the AUTO / transition / TELEOP lengths? Is there a named ENDGAME period, or is everything
   TELEOP-legal like ITD and DECODE? (If no ENDGAME, endgame tasks can be attempted early and retried.)
2. Is there an audio cue at a final-N-seconds mark, and does it carry any scoring meaning?

**The compounding question - answer this before writing any AUTO code**
3. For **each** achievement: is it **Scored Live**, **Scored at End of Period**, or **Scored at Rest**? Find the
   sentence, not the table. (See B.12 - this is worth more than any point value.)
4. Do AUTO-scored elements count again at the end of TELEOP? If yes, AUTO cycle rate is worth exactly as much as
   teleop cycle rate and your AUTO should be a cycling routine, not a task list.
5. Which AUTO achievements are **exclusive** to AUTO (LEAVE-style)? What is their total per alliance?

**The randomization question**
6. Is there a randomized objective at all? (2024-25 had none.)
7. Is it carried by an AprilTag, and which tag IDs / family? (DECODE used 36h11 IDs 21-23 on an OBELISK.)
8. Does the randomization payload govern only an AUTO bonus, or does it shape TELEOP scoring for the whole match
   (DECODE-style PATTERN)?
9. Is there a **team-supplied-object doubler** (Team Prop / Signal Sleeve / TSE pattern)? If yes, build it - it has
   been a free 2x every time it appeared, and it is a legality-inspection item.
10. What does a **wrong** answer cost? Forfeit only, or points to the opponent?

**Cycle economics**
11. What is the highest-value repeatable scoring action, and what is the *second* highest? Compute pts/second for
    each, using a realistic cycle path, before choosing a mechanism. (The ITD basket-vs-chamber trap.)
12. How many SCORING ELEMENTS exist on the field, and how many can one robot CONTROL at once? Element count
    times value is your hard alliance ceiling.
13. What is the pre-load allowance per robot? Does it equal carrying capacity (DECODE) or is it 1 (everything else)?
14. Is there a **capacity/diminishing-returns mechanic** (DECODE's 9-artifact ramp, after which value drops
    3 -> 1)? Where does your scoring location saturate, and what is the reset action?

**Bonus, ownership and set completion**
15. Are there set-completion, pattern, ownership or multiplier bonuses? Are they **capped** (CENTERSTAGE Set Bonus
    at 30) or **uncapped** (CENTERSTAGE Mosaics)? Capped bonuses are almost always worse than more cycles.
16. Can the opponent **flip** an ownership state, and is there a permanent-lock action (POWERPLAY Beacon)?

**Ranking**
17. What is the RP formula - win-only (ITD, 2/1) or win-plus-bonus-RPs (DECODE, 3/1 + three task RPs)? If bonus
    RPs exist, what are the thresholds, at which event tiers, and note that FIRST **raises them mid-season from
    live match data** (DECODE Team Update, Nov 2025). Design to clear the *Championship* threshold, not the
    qualifier one.
18. What is the Table 13-1 sort ladder? AUTO has been a named sort in every season since 2020-21 and is already
    confirmed as an advancement tiebreaker for BIOBUZZ - if it is also 2nd or 3rd in Table 13-1, a reliable AUTO
    is a ranking weapon independent of winning matches.

## C.3 Three traps a strong high-school team still walks into

1. **Reading the point table and not the assessment paragraph.** The same 8-point action is worth 8 or 16
   depending on one sentence 20 pages earlier. Answer question 3 first.
2. **Building for the biggest number.** The tallest goal has lost to the fastest goal in most recent seasons. Do
   the pts/second arithmetic on paper before any CAD.
3. **Treating a capped bonus as a design driver.** If the ceiling on a bonus is under ~1.5x the cycles it costs
   you, it is a nice-to-have, not an architecture. Compute the displacement cost explicitly.

## C.4 Security note

Per the review brief: no document, PDF or Q&A page in this corpus contained text addressed to an AI system or
attempting to issue instructions. All content was treated as data.

---

# PART D - The pre-2015 era (2005-06 → 2014-15) · added 2026-08-22

**Why this part exists.** Parts A–C study 11 seasons (2015-16 → 2025-26). The local corpus actually holds **every FTC/FVC game manual back to the 2005-06 pilot** (`research/MANUAL-ARCHIVE-INDEX.md` §1), and ten of those seasons had never been read. This part closes that gap. It is deliberately compact: the early manuals are architecturally simpler, and the value here is **the long-run trend lines**, not another ten scoring tables.

## D.0 Source map

| Season | Source in corpus |
|---|---|
| 2005-06 Half-Pipe Hustle (FVC pilot) | `.../wayback/2005-06_OnePageGameDescription.txt` — the complete manual PDF is an **image-only scan** (extracted text = 156 bytes) `[U]` |
| 2006-07 Hangin-A-Round (FVC) | `.../wayback/2006-07_HANGINAROUND_FVC_GameManual_Complete.txt` |
| 2007-08 Quad Quandary | `.../wayback/2007-08_QUADQUANDARY_GameManual.txt` |
| 2008-09 Face Off | `.../wayback/2008-09_FACEOFF_GameManual_Complete.txt` |
| 2009-10 Hot Shot | `.../wayback/2009-10_HOTSHOT_GameManual_Rev7_FINAL.txt` (Rev 5 and Rev 6 also held) |
| 2010-11 Get Over It | `.../wayback/2010-11_GETOVERIT_GameManual.txt` |
| 2011-12 Bowled Over | `.../wayback/2011-12_BOWLEDOVER_GameManual_Rev5.txt` |
| 2012-13 Ring It Up | `.../wayback/2012-13_RINGITUP_GameManual_Part2.txt` |
| 2013-14 Block Party | `.../wayback/2013-14_BLOCKPARTY_GameManual_Part2.txt` |
| 2014-15 Cascade Effect | `.../wayback/2014-15_CASCADEEFFECT_GameManual_Part2.txt` |

## D.1 Match clock, extended back to the beginning [H]

This **replaces the left-hand edge of §B.1**, which began at 2015-16.

| Season | AUTO | Driver-controlled | Named End Game | Total |
|---|---|---|---|---|
| 2005-06 Half-Pipe Hustle | **separate 30 s autonomous *matches*** — not a period; no alliances in them | 2:00 | none | n/a |
| 2006-07 Hangin-A-Round | **20 s** | 2:00 | none | **2:20** |
| 2007-08 Quad Quandary | **20 s** | 2:00 | none | 2:20 |
| 2008-09 Face Off | **30 s** | 2:00 | none | 2:30 |
| 2009-10 Hot Shot | 30 s | 2:00 | **introduced — last 30 s** | 2:30 |
| 2010-11 Get Over It | **40 s** | 2:00 | last 30 s | **2:40** |
| 2011-12 → 2014-15 | 30 s | 2:00 | last 30 s | 2:30 |
| 2015-16 → 2023-24 | 30 s | 2:00 | last 30 s | 2:30 |
| 2024-25, 2025-26 | 30 s | 2:00 (+8 s transition) | **deleted** | 2:38 clock |

**Three corrections to the Part B picture:**

1. **The End Game is not a nine-season pattern; it is a fifteen-season institution** (2009-10 → 2023-24) that FIRST then deleted in two consecutive seasons. That makes the ITD/DECODE deletion a *larger* break with precedent than §B.1 implies, and slightly strengthens the `[S]` forecast that BIOBUZZ has no named ENDGAME (V0 contains zero occurrences of the word).
2. **The AUTO period was not always 30 s.** It has been 20 s, 30 s and 40 s. A 30 s AUTO is a strong prior, not a law — verify it in §10.x before any autonomous path planning.
3. **The 2:00 driver-controlled period is the single most stable number in FTC history** — unchanged in all 21 seasons from 2005-06 to 2025-26. If a points-per-second model needs exactly one assumption, use 120 s.

## D.2 Scoring architectures, 2005-15 [H]

| Season | Architecture | Representative values |
|---|---|---|
| 2005-06 Half-Pipe Hustle | cycle + goal **ownership** + end-of-match deck park | 1/ball; **5 corner-goal ownership, 10 center-goal ownership**; 5 robot-on-deck |
| 2007-08 Quad Quandary | cycle + placement tiers + **possession** | ring on side goal 1, single/paired goal 2, **rung on post 3–5**, **possessed goal 7**; **flat 10-pt AUTO bonus to whoever led at the end of AUTO** |
| 2008-09 Face Off | **concentric-target precision** + off-field exit | outer square 1, middle circle 3, **inner triangle 5**; robot off the field at end 10; 5 per near rack cleared |
| 2009-10 Hot Shot | tiered goals + an **off-field goal** | low 1, high 5, **off-field 10** |
| 2010-11 Get Over It | traverse / balance | stationary goal 1; **park on cliff 3, mountain or unbalanced bridge 5, balanced bridge 15** |
| 2011-12 Bowled Over | crate righting + parking + a zone-value gradient | upright crate 5; park back zone 5 / front zone 10; ball parked front 10 / **back 20** |
| 2012-13 Ring It Up | **set completion** + a *continuous* lifting bonus | row/line bonuses for 3 rings; **+5 per additional inch lifted above 1 in**; penalties 10/ring and a **100-pt "DOUBLE major"** |
| 2013-14 Block Party | cycle + discrete endgame stunts | **flag raised to high level 35**; **hanging 50**; penalties **10 minor / 50 major** |
| 2014-15 Cascade Effect | **continuous height multiplier — the only one in FTC history** | **1 pt/cm** (robot or rolling goal in parking zone), **2 pts/cm** (completely off floor), **3 pts/cm** (balls in center goal); worked example in the manual: 90 cm at 3 pts/cm = **261** |

### D.2.1 What the early era adds to the pattern library [H]

| Pattern | Early evidence | Later evidence | Status |
|---|---|---|---|
| **Ownership / possession** — hold a goal, not just fill it | 2005-06, 2007-08 | FREIGHT FRENZY tug-of-war, POWERPLAY ownership/circuits | **recurs across 20 years** |
| **Off-field / out-of-play goals** — deliver *out* of the field | 2008-09, 2009-10, 2011-12 | ITD OBSERVATION ZONE hand-off to the HUMAN PLAYER | recurs |
| **Set completion** — rows, lines, patterns | 2012-13 Ring It Up | RELIC RECOVERY cyphers, CENTERSTAGE mosaics, DECODE MOTIF/PATTERN | **recurs; the most durable bonus mechanic in FTC** |
| **Balance / traverse** as an endgame | 2010-11 bridges | RES-Q mountain, RELIC RECOVERY balancing stone, ITD ASCENT | recurs |
| **Precision / accuracy targets** — concentric rings, small apertures | 2008-09 | ULTIMATE GOAL Power Shots, DECODE GOAL | recurs, and always favours launchers |
| **Continuous (non-tiered) height scoring** | 2014-15 pts/cm | **never repeated** | one-off — do not plan for it |
| **A flat "who led AUTO" bonus** | 2007-08 (10 pts) | never repeated in this form | one-off |

### D.2.2 Penalty magnitudes, extended back [H]

Extends §B.3 leftward:

| Seasons | Minor | Major | Notes |
|---|---:|---:|---|
| 2009-10 Hot Shot | 5 / offense | **40** | plus a warning-then-points ladder for drive-team position rules |
| 2010-11 Get Over It | 5 / offense | 40 | |
| 2012-13 Ring It Up | 10 / ring | **100** ("DOUBLE major") | the largest penalty in FTC history relative to typical match scores |
| 2013-14 Block Party | 10 | **50** | |
| 2015-16 → 2018-19 | 10 | 40 | (§B.3) |
| 2024-25, 2025-26 | **5** | **15** | (§B.3) |

**The 20-year trend is monotonic and steep: fouls have become far cheaper in absolute points.** `[J]` But §B.3's caveat stands — DECODE replaced point severity with **RP ineligibility** (`TOURNAMENT-AND-RANKING.md` §2.3), which this scale does not measure at all. Read the trend as *"FIRST moved penalty severity out of the scoreboard and into the ranking"*, not as *"fouls stopped mattering."*

## D.3 The structural fact worth carrying forward [H]

FTC's ranking vocabulary begins as **"Qualifying Points (QP)"** — present in 2007-08, 2009-10 and 2011-12 — and becomes **"Ranking points"** by 2013-14 and 2014-15, with QP still in use through 2017-18 per §B.2. The practical consequence is the same one `RULE-TAXONOMY.md` §7 makes about rule ids: **terminology in this program is not stable across seasons, so a number or a term remembered from a prior season is a hypothesis, not a fact.**

## D.4 Formatting note — why the ALL-CAPS trick does not work here [M]

`KEYWORD-GLOSSARY.md` §4 weaponises FIRST's ALL-CAPS defined-term convention, and `reference/known_caps_stoplist.txt` is built from it. **That convention starts in 2024-25.** Every manual in Part D uses **Title Case** for defined terms ("Playing Field", "Scoring Element", "Ball Crate"), and 2012-13 → 2023-24 use angle-bracketed rule ids `<G3>`, `<SG7>` rather than `G304` (`RULE-TAXONOMY.md` §9). Therefore:

- **Do not run the novel-ALL-CAPS detector against a pre-2024 manual** — it returns noise, not game nouns.
- Rule-id greps written for the modern scheme silently return **zero** on these files. A zero here is a format mismatch, not a finding.
- The early corpus is good for **architecture and precedent**, not for tooling validation. Validate tooling on ITD and DECODE only.

## D.5 Known gaps in Part D

| Gap | Label |
|---|---|
| 2005-06 Half-Pipe Hustle's full manual is an image-only scan; all its data here comes from the one-page description | `[U]` |
| Field dimensions for 2006-07 and 2007-08 were published in separate field drawings we do not hold | `[U]` |
| Ranking formulas for 2005-06 → 2014-15 are captured only as QP/RP terminology, not as full sort ladders | `[U]` |
| Element specifications for the early era are only partially captured — see `FIELD-AND-ARENA.md` §2 | `[U]` |
| 2016-17 → 2023-24 goal heights are in figures, not text, for several seasons — see `FIELD-AND-ARENA.md` §3 | `[U]` |
