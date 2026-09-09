# ROVER RUCKUS (2018-19) — Season Dossier

**Sources.** Game Manual **Part 2** (the game), Revision **1.4, 1/22/2019**, 35 pp — `manuals/archive/wayback/2018-19_ROVERRUCKUS_GameManual_Part2.pdf`. Game Manual **Part 1** (game-independent), Revision **1, 7/11/2018**, 48 pp — `manuals/archive/wayback/2018-19_ROVERRUCKUS_GameManual_Part1.pdf`. Official Q&A archive — `manuals/archive/supplemental/2018-19_ROVERRUCKUS_Complete_QA.pdf`.

**Label key.** `[MANUAL]` the text says it · `[DERIVED]` arithmetic, operands shown · `[JUDGMENT]` my read · `UNVERIFIED` not found in the manual.

> Note on Part 1: it was published at Revision 1 on 7/11/2018 and **never revised**. Every 2018-19 rule change landed in Part 2 (four revisions). Section 9 records what that implies for the harness.

---

## 1. The game in five sentences

Two two-team Alliances play on a 12 ft × 12 ft field holding a central **Lander**, two Alliance-neutral **Craters** in opposite corners, and one Alliance-specific **Depot** in each of the other two corners `[MANUAL §1.2, §1.3 Fig 1.3-1]`. Robots begin either **Latched** to their Alliance's Lander Support Bracket — hanging with their lowest point at least 4 in (102 mm) off the floor — or already **Deployed** on the floor, and only a robot that starts Latched can earn the 30-point Landing award for lowering itself down `[MANUAL §1.5.1]`. In the 30-second Autonomous Period an Alliance can Land, **Sample** (knock the one randomly-placed Gold out of a three-mineral group without disturbing the two Silvers), **Claim** a Depot by dropping a team-built Team Marker in it, and Park in a Crater `[MANUAL §1.5.2]`. Through the two-minute Driver-Controlled Period robots harvest **Minerals** — 90 Gold cubes and 60 Silver balls — from the Craters and either sort them into the matching Gold or Silver **Cargo Hold** on the Lander for 5 points each, or dump either type into the Depot for 2 `[MANUAL §1.5.3, §1.7]`. In the final 30 seconds — the End Game — each robot chooses exactly one of Latching back onto the Lander (50), Parking In a Crater (15), or Parking Completely In a Crater (25) `[MANUAL §1.5.4; §1.6.2 <G24>; Q&A "End Game" #5]`.

---

## 2. Match structure

| Segment | Length | Notes |
|---|---|---|
| Pre-Match setup | untimed | Robot placed Latched **or** Deployed; one Team Marker may be Pre-Loaded; **no Minerals may be Pre-Loaded** `[MANUAL §1.5.1]` |
| Sample randomization | untimed | Referees arrange 2 Silver + 1 Gold per Sample Field; robots and Driver Stations become hands-off `[MANUAL §1.5.1-3; <GS1>]` |
| **Autonomous Period** | **0:30** | Pre-programmed only; single start touch on the Driver Station Android device using the built-in 30-second timer `[MANUAL §1.5.2]` |
| Transition | 5 s + "3-2-1-go" | Hands-off; field personnel do not enter or touch robots `[MANUAL §1.5.3, <G12>]` |
| **Driver-Controlled Period** | **2:00** | Includes the End Game `[MANUAL §1.5.3]` |
| ↳ **End Game** | final **0:30** | Driver-Controlled scoring continues throughout `[MANUAL §1.5.4]` |
| **Total** | **2:30** | `[MANUAL §1.5]` |

**Versus 2017-18 (Relic Recovery)** — verified by extracting the prior manual, not from memory:

| Dimension | 2017-18 | 2018-19 | Source |
|---|---|---|---|
| Period structure | 30 s auto + 2:00 teleop, last 0:30 = End Game | **identical** | `[MANUAL]` RELIC RECOVERY Part 2 §1.5 / ROVER RUCKUS Part 2 §1.5 |
| Minor / Major Penalty | 10 / 40 pts | **10 / 40 pts, unchanged** | `[MANUAL]` both Part 2 §1.5.6 |
| Robot starting volume | 18 in cube | **18 in cube, unchanged** | `[MANUAL]` both `<RG02>` |
| DC motors / servos | 8 / 12 | **8 / 12, unchanged** | `[MANUAL]` `<RE09>`, `<RE10>` |
| **Robot weight limit** | **none exists** | **42 lb + 0.5 lb allowance** | `[MANUAL]` 2017-18 Part 1 has no weight rule (`<RG04>` there is Alliance Flag Holder); 2018-19 `<RG04>` |
| Game rule count (Part 2) | G:28 GS:16 S:3 = 47 | G:30 GS:11 S:3 = **44** | `[DERIVED]` legacy parser, single-digit regex repaired |

The 42-pound cap is the one structural change to what teams were allowed to build, and it arrived in the same season that asked robots to hang their entire mass from a bracket. `[JUDGMENT]`

---

## 3. Scoring table

Verbatim from the Scoring Summary table, §1.7 (Part 2 p. 24), recovered by `tools/extract-tables.py` geometry and **confirmed cell-by-cell against a 130-dpi render of the same page**.

| Scoring Achievement | AUTO | TELEOP | END GAME | Manual ref |
|---|---:|---:|---:|---|
| **Robot** | | | | |
| Landing | **30** | – | – | §1.5.2-1 |
| Claiming | **15** | – | – | §1.5.2-2 |
| Parking (In a Crater at end of Auto) | **10** | – | – | §1.5.2-3 |
| Sampling | **25** | – | – | §1.5.2-4 |
| Latching | – | – | **50** | §1.5.4-1 |
| Robot In any Crater | – | – | **15** | §1.5.4-2 |
| Robot Completely In any Crater | – | – | **25** | §1.5.4-3 |
| **Mineral** | | | | |
| Any Mineral in Depot | **2** | **2** | **2** | §1.5.3-1 |
| Gold in **Gold** Cargo Hold | **5** | **5** | **5** | §1.5.3-2 |
| Silver in **Silver** Cargo Hold | **5** | **5** | **5** | §1.5.3-3 |
| Gold in Silver Cargo Hold *(Contaminant)* | **0** | **0** | **0** | §1.5.3-4 |
| Silver in Gold Cargo Hold *(Contaminant)* | **0** | **0** | **0** | §1.5.3-4 |

Additional scoring mechanics not on the table:

| Mechanic | Value | Source |
|---|---|---|
| Mineral **removed from a Depot** | **−2 each** | `[MANUAL §1.5.3-1]` |
| Minor Penalty (awarded to the non-offending Alliance) | **+10** each occurrence | `[MANUAL §1.5.6]` |
| Major Penalty (awarded to the non-offending Alliance) | **+40** each occurrence | `[MANUAL §1.5.6]` |
| Scoring Element still touching / Controlled by a same-Alliance robot | **0** | `[MANUAL <G21>]` |
| Robot qualifying for two achievements | **highest only**; if equal, one counts | `[MANUAL <G24>]` |

**Scored volumes** `[MANUAL §1.5.3-5]`: a Depot is the outer edge of its tape extended infinitely upward; a Cargo Hold is its 5 inner surfaces plus the horizontal extension of the upper edge of the outside clear panel. **Cargo Hold capacity is UNVERIFIED** — the manual never states a mineral limit per hold.

### Derived ceilings

| Quantity | Value | Operands |
|---|---:|---|
| Landing, both robots | 60 | 30 × 2 `[DERIVED]` |
| Claiming, both robots (= Completely Claimed) | 30 | 15 × 2 `[DERIVED]` |
| Sampling, both Sample Fields | 50 | 25 × 2 `[DERIVED]` |
| Parking, both robots | 20 | 10 × 2 `[DERIVED]` |
| **Autonomous robot-achievement ceiling** | **160** | 60 + 30 + 50 + 20 `[DERIVED]` |
| **End Game ceiling** | **100** | 50 × 2 — only one End Game task per robot `[DERIVED from <G24> + Q&A]` |
| **Non-mineral ceiling, per alliance** | **260** | 160 + 100 `[DERIVED]` |
| …expressed in sorted Cargo Hold minerals | **52 minerals** | 260 ÷ 5 `[DERIVED]` |
| Total Minerals on field | **150** | 90 Gold + 60 Silver `[MANUAL §1.2]` |
| Cross-check of the element count | **150** | Craters 86 G + 52 S = 138 `[MANUAL §1.5.1]`; Sample Fields 4 × (1 G + 2 S) = 12; 138 + 12 = 150 `[DERIVED]` |
| Gold : Silver ratio | **3 : 2** | 90 : 60 `[DERIVED]` — both score 5, so Gold-only collectors had 1.5× the supply |

---

## 4. Bonuses, randomization and ranking

### Claiming → the season's ownership mechanic

Rover Ruckus had no multipliers. Its one ownership mechanic was **Completely Claimed**:

| State | Definition | Effect |
|---|---|---|
| **Claimed** | One robot placed and released a Team Marker in its Alliance's Depot during Autonomous. The Marker need not stay there. | 15 points `[MANUAL §1.4, §1.5.2-2]` |
| **Completely Claimed** | **Both** robots on the Alliance did so during Autonomous — not necessarily simultaneously. | 30 points **and the Depot becomes permanently immune to opponent de-scoring for the rest of the Match** `[MANUAL §1.4, §1.5.2-2, <GS4>]` |

`[MANUAL §1.5.2-2]` states Completely Claimed Depots are permanent for the Match. `<GS4>` sets the matching prohibition: robots may de-score an opponent's Depot **only** if it was not Completely Claimed in Autonomous, and may always de-score their own Depot; each illegal removal is a Minor Penalty. So a second Team Marker in Autonomous bought 15 points *plus* an insurance policy on every Depot mineral scored thereafter. `[JUDGMENT]`

### Randomization

| Property | Detail |
|---|---|
| What is randomized | Referees arrange **2 Silver + 1 Gold** into a grouping; each of the three positions is a red or blue taped Area `[MANUAL §1.4 "Sample Field"/"Samples", §1.5.1-3]` |
| Positions | **Three** per Sample Field, in front of each robot starting location `[MANUAL §1.4]` |
| Count | **One Sample Field per robot starting location** → 4 total, **2 per Alliance** `[MANUAL §1.5.1-3]` |
| Is it the same for everyone? | **Yes** — "This grouping will be repeated in front of each Robot starting location." `[MANUAL §1.5.1-3]` |
| How revealed | **Physically only.** No beacon, signal, or coded marker. Robots had to see it or feel it. `[MANUAL]` — the manual describes no electronic reveal anywhere. The vision toolchain teams used lived in the SDK, **UNVERIFIED in either manual** |
| Lock-in | Once randomization begins, touching your robot or Driver Station is a Minor Penalty **and forfeits that robot's Sample Score**; the penalty hits only the offender, not the Alliance partner `[MANUAL <GS1>]` |
| Scoring condition | Gold **Out** of its taped Area **and both** Silvers **remaining In** theirs `[MANUAL §1.5.2-4]` |
| When evaluated | At the **end** of the Autonomous Period, on final positions — not at the instant it happens `[Q&A, "Autonomous Period" #12, Answer 1]` |
| Blind-guess expected value | **≈ 8.33 pts** — 25 × ⅓ `[DERIVED]` |

The evaluation-at-end rule has a sharp edge the Q&A had to spell out: knocking the Gold out and then letting *either* Silver drift off its mark scores **zero**, "regardless of how the Silver Minerals are removed" — including by an opponent's stray mineral `[Q&A, "Autonomous Period" #12, Answers 2–3]`. Sampling was all-or-nothing and could be destroyed after it was earned. `[JUDGMENT]`

### Ranking

| Element | Rule |
|---|---|
| **Ranking Points (RP)** | Win **2**, tie **1**, loss **0**; DQ or no-show **0** `[MANUAL Part 1 §5.8]` |
| **TieBreaker Points (TBP)** | **The losing Alliance's pre-penalty score — awarded to BOTH Alliances.** On a tie, both get the lowest pre-penalty score. `[MANUAL Part 1 §5.8]` |
| DQ handling | A disqualified Team gets 0 TBP; if both Teams on an Alliance are DQ'd, the winners receive **their own** score as TBP `[MANUAL Part 1 §5.8]` |
| Sort order | RP → TBP → highest single Match score → next-highest → random electronic draw `[MANUAL Part 1 §5.8]` |
| Surrogate Match | Marked with an asterisk; does not count toward standings `[MANUAL Part 1 §5.8, §4.2]` |
| Score dispute window | One student, referee question box, within **3 Matches** of the disputed Match `[MANUAL Part 1 §5.8]` |
| Alliances | 4 Alliances; **3 Teams each if ≥21 Teams**, 2 each if ≤20 `[MANUAL Part 1 §5.9]` |
| Elimination bracket | 1 v 4, 2 v 3; higher seed is red; lower seed places robots first `[MANUAL Part 1 §5.10, <G3>b]` |

**The TBP formula is the single most exploitable fact in this table.** TBP is the *loser's* score, given to both sides — Part 1's own Q-1 example has a 30-15 win awarding **15 TBP to all four Teams**. Two consequences `[DERIVED]`: (a) running up your own score adds **zero** TBP, and (b) **playing defense lowers your own tiebreaker**, because suppressing the opponent below their natural output shrinks the number you bank. The penalty note matters too — Q-4 in Part 1 §5.8 shows an Alliance losing on penalties while TBP still uses the **pre-penalized** floor of 15.

---

## 5. The rules that shaped play

**44 tagged rules in Part 2** — 30 `<G>`, 11 `<GS>`, 3 `<S>`. The `<GS>` block is where this season lives.

### Game-specific rules (§1.6.3), with thresholds

| Rule | Threshold / trigger | Consequence |
|---|---|---|
| `<GS1>` Touching after randomization | Any contact with robot or Driver Station once randomization starts | Minor + **that robot forfeits the Sample Score**; offender only, partner unaffected |
| `<GS2>` Autonomous interference | Interfering with opponent Scoring attempts **or their Sample Field** during Auto. **Exemption:** robots attempting to Score in a Crater | **Major** |
| `<GS3>` Mineral Control/Possession | **Max 2 Minerals.** May *temporarily* exceed while collecting inside a Crater; must shed before any other gameplay. Plowing through any quantity inside the Crater is legal; Herding beyond the max for advantage is not | Minor **per Mineral over**, **plus another Minor per Mineral per 5 s**; **Major per Mineral Scored** while over; escalates to Yellow Card |
| `<GS4>` De-scoring | Never from a Cargo Hold. Opponent's Depot only if **not Completely Claimed**. Own Depot always allowed | Minor **per Mineral** |
| `<GS5>` Blocking Lander access | Blocking an opponent's Cargo Hold or Lander Support Bracket; must retreat **3 ft (0.9 m) ≈ 1.5 tiles** from their Landing Zone | **Major immediately + Minor per 5 s**; escalates to Yellow "quickly" |
| `<GS6>` Interfering at the Lander | Interfering with an opponent that is **In their own Landing Zone** scoring or Latching | **Major immediately + Minor per 5 s**; escalates to Yellow |
| `<GS7>` Latching before End Game | A Deployed robot intentionally Supporting **any portion** of its weight on the Bracket before End Game | **Ineligible for the 50-point Latch.** No penalty — pure forfeiture |
| `<GS8>` Wrong bracket | Latching to an opposing Alliance's Lander Support Bracket | **Major** |
| `<GS9>` Launching | Launching is legal **only from inside your own Landing Zone** | Minor **per illegally launched element** — but the element **still scores** `[MANUAL orange box]`; escalates to Yellow |
| `<GS10>` Scoring from in a Crater | A robot **In a Crater** may not Score Minerals | Minor per occurrence; escalates to Yellow |
| `<GS11>` Obstructing Lander↔Crater travel | Obstructing another robot's path between Lander and Crater **> 5 s**. Driver-Controlled Period only | Minor **per 5 s** |

### General rules that bit hardest

| Rule | Substance |
|---|---|
| `<G4>` | 18 in cube at start; Alliance flag and Pre-Loads may protrude; **after the start the robot may extend in any dimension** — no expansion limit this season |
| `<G16>` | May not grasp/attach to any Game Element **other than Scoring Elements** — this is what made the Lander a hands-off structure. Warning, then **Major** |
| `<G18>` | Pin / Trap / Block > **5 s**; Minor **per 5 s**; must retreat **3 ft**. Applies in Auto only if the referee judges it deliberate strategy |
| `<G21>` | A Scoring Element touching or Controlled by a same-Alliance robot is worth **zero** — you must let go |
| `<G23>` | Controlled Scoring Elements count as part of the robot **except** when locating the robot; a possessed mineral breaking a plane does not put the robot there |
| `<G24>` | Two or more Scoring Areas → **highest value only**. Confirmed by Q&A to bind the three End Game tasks together |
| `<G29>` | Using Game Elements to ease or amplify a Scoring activity → **Major** |
| `<G30>` | Referee discretion to excuse Inadvertent **and** Inconsequential violations — the release valve `<GS2>` explicitly leans on |
| `<S2>` | Any contact outside the Playing Field Perimeter → **immediate Yellow Card**, optional Disable |

### Penalty economics `[DERIVED]`

| Infraction | Points | Equivalent in sorted Cargo Hold minerals |
|---|---:|---:|
| Minor | 10 | 2 (10 ÷ 5) |
| Major | 40 | 8 (40 ÷ 5) |
| `<GS3>` over-possession, 2 extra minerals held 10 s | 60 | 12 — 2 Minors immediate + 2 Minors per 5 s × 2 intervals = 6 × 10 |
| `<GS5>`/`<GS6>` block held 15 s | 70 | 14 — 40 + (10 × 3) |

A single Major costs more than a Landing (30) and more than a Sampling (25). A sustained Lander block could out-cost the Latch it was trying to prevent. `[DERIVED]`

---

## 6. Robot archetypes that season

Build envelope, from Part 1 (all `[MANUAL]`):

| Constraint | Value | Rule |
|---|---|---|
| Starting volume | 18 × 18 × 18 in (45.7 cm cube), self-supporting in the Sizing Tool, power-OFF or via an Initialization Routine | `<RG02>`, `<G4>` |
| Post-start expansion | **Unlimited** | `<G4>` |
| **Weight** | **42 lb incl. battery, +0.5 lb scale allowance**; excludes Alliance Flag and Team Marker; swappable mechanisms all weighed together | `<RG04>` |
| DC motors | **8 max** (TETRIX / AndyMark NeveRest / MR-MATRIX / REV HD Hex / REV Core Hex) | `<RE09>` |
| Servos | **12 max**, ≤6 V; VEX EDR 393 counts against this total | `<RE10>` |
| Launching robot parts | Prohibited, tethered included | `<RG08>` |
| Launching Scoring Elements | Allowed, but must demonstrate < 16 ft (4.88 m) range and < 6 ft (1.83 m) elevation if challenged | `<RG09>` |
| Team Marker | Min 3 × 3 × 4 in, max 4 × 4 × 8 in; team number legible at 12 in; **no electronics**; inspected | `<TM01>`–`<TM04>`, `<I9>` |
| Init-move warning label | Required near the main power switch if servos move on init, ≥ 1 × 2.63 in | `<RG02>`b(i) |

What that envelope forced teams to build `[JUDGMENT, grounded in the cited rules]`:

| Archetype | Must have | Rules that constrain it |
|---|---|---|
| **Hanger / Lander robot** | A lift or winch that supports the robot's **full 42 lb** off a bracket, twice per match (start descent + End Game re-latch), and holds the whole robot in the 18 in cube while hanging with 4 in of floor clearance | `<RG04>` 42 lb; `<RG02>`/`§1.5.1-1c` 18 in cube while Latched; `§1.5.1-1b` 4 in clearance; `<GS7>` no early weight-bearing |
| **Crater harvester** | Intake that reaches over the 3 in Crater Rim, tolerates a dense pile, and **sheds down to 2 minerals before leaving** — plus visible mineral storage, because obscured storage invites penalties | `<GS3>` limit and its orange box; `§1.4` Crater Rim ≈ 7.6 × 9 × 3 in; `<GS10>` cannot score from in the Crater |
| **Sorter** | Gold-cube vs Silver-sphere discrimination, since a wrong hold scores **0** | `§1.5.3-4` Contaminant |
| **Depot dumper** | The low-tech path: no sorting needed, 2 pts/mineral, either type | `§1.5.3-1` |
| **Auto vision robot** | Camera + compute to find 1 Gold among 3 positions, then a manipulator precise enough to move **only** the Gold | `§1.5.2-4`; toolchain **UNVERIFIED** in the manuals |
| **Full-auto traveller** | Land → Sample → cross to the Depot corner → drop Marker → return to a Crater, in 30 s | `§1.5.2` 1–4; Depot and Crater sit in **different corners** per Fig 1.3-1 |
| **Launcher** | Rarely worth it: legal only from inside your own Landing Zone | `<GS9>`, `<RG09>` |

The binding tension: **8 motors** had to cover drivetrain + lift + intake + delivery, and **42 lb** had to include a mechanism strong enough to hoist that same 42 lb. `[DERIVED from <RE09>, <RG04>]`

---

## 7. The strategic lesson

**The points were in the 60 seconds when nobody was cycling minerals.**

Non-mineral achievements ceiling at **260 per alliance** (160 Auto + 100 End Game) `[DERIVED §3]`. That equals **52 perfectly-sorted Cargo Hold minerals**, or **130 Depot minerals**, and it is available in 30 seconds of Autonomous plus 30 seconds of End Game — during which teleop scoring also continues uninterrupted `[MANUAL §1.5.4]`. Mineral cycling was the *visible* game and the *underpriced-looking* one; the checklist tasks were where the scoreboard actually moved. `[JUDGMENT]`

**What was underpriced.** *Claiming.* At 15 points it reads like the smallest Autonomous award, below Sampling's 25 and Landing's 30 — so it looks like the one to skip when the 30-second budget gets tight. But the **second** Team Marker is not worth 15 points; it is worth 15 points **plus permanent de-score immunity for every Depot mineral banked for the rest of the match** `[MANUAL §1.5.2-2, <GS4>]`. Nothing else in the season converted a one-time Autonomous action into a match-long defensive property. An alliance dumping into an unprotected Depot was scoring at 2 points a mineral against an opponent legally removing them at −2 `[MANUAL §1.5.3-1]`; the same alliance behind a Completely Claimed Depot was scoring at 2 with the removals **illegal at a Minor each**. Same mineral, opposite sign, decided by a 15-point Autonomous task the manual buries in a numbered list. `[JUDGMENT]`

**Where the "obvious" strategy underperformed.** *Camping the Crater.* The Crater is where 138 of 150 minerals sit `[MANUAL §1.5.1]`, `<GS3>` explicitly relaxes the 2-mineral limit inside it, and the Crater is Alliance-neutral so both alliances share it. The apparent play — park in the Crater, hold a large pile under the relaxed limit, and feed from there while denying the opponent — was killed by rule, mid-season. Revision **1.2 (10/3/2018)** added `<GS10>` (robots **In a Crater** cannot Score) and `<GS11>` (no obstructing Lander↔Crater travel > 5 s) `[MANUAL, Part 2 revision history table, p. 3]`. The Q&A entry dated the **same day** shows a team assembling exactly that combination — extend from the Crater into the Landing Zone for `<GS6>` protection while holding unlimited minerals under `<GS3>` — and the GDC answering that it violates `<GS11>`, and `<GS10>` too if it tries to score `[Q&A "Game Play — All Match Periods" #6]`. Anyone who built a Crater-camper in September owned a penalty generator by October. `[JUDGMENT]`

**The genuine ambiguities**, ranked by how hard the Q&A had to work — count of references to each rule token across the full archive, bracketed and bare forms combined `[DERIVED]`:

| Rule | Refs | What was actually unclear |
|---|---:|---|
| `<GS2>` Auto interference | **27** | Whether the "attempting to Score in a Crater" exemption covers a robot that disturbs an opponent's Sample Field *on the way*. GDC: **no** — the violation attaches when the Silver moves, and a later Crater attempt does not retroactively excuse it |
| `<GS3>` Possession limit | **21** | Where "temporarily exceed while collecting in the Crater" ends. GDC: Herding ends when the minerals **stop moving**; referees warn, then the Drive Team has **5 s** to comply; sweeping **3+ extra** minerals out per exit will likely be penalized |
| `<GS7>` Early latching | **13** | Whether *incidental* bracket contact while scoring kills the 50. GDC: contact is fine, **any weight-bearing is not** — a robot tethered to the bracket by hook and string is "partially supported" and loses eligibility |
| `<GS6>` Lander interference | **12** | Where legitimate defense ends and Major-penalty interference begins at the Landing Zone |
| `<GS5>` Blocking | **8** | Same boundary from the access side |
| `<GS11>` Obstructing | **7** | Added mid-season; how "5 seconds" is counted |

Three of the top four are the same question: **`<GS3>`, `<GS5>`, `<GS6>`, `<GS7>` and `<GS11>` all turn on referee reading of intent** — "planned strategy" vs `<G30>` Inadvertent, "intentionally Support," "to gain a strategic advantage." A season whose most-contested rules are intent-based is a season where identical robot behaviour scores differently in different brackets. `[JUDGMENT]`

**One more trap.** `<G24>` makes the three End Game tasks mutually exclusive, but the manual never says so in §1.5.4 — the three achievements are simply listed, and it takes `<G24>` plus a December Q&A ruling to learn that Latching (50) and Parking In a Crater (15) do **not** stack to 65 `[Q&A "End Game" #5]`. A team that budgeted 65 built its End Game around a number that never existed. `[JUDGMENT]`

---

## 8. Signals for BIOBUZZ

| # | Signal | Grounding |
|---|---|---|
| 1 | **Price the checklist tasks before the cycle tasks.** Compute the non-cycling ceiling (auto + endgame) in units of one cycled scoring element on day one. Here it was 260 pts = 52 minerals. | `[DERIVED §3]` |
| 2 | **Hunt for the task that buys a property, not points.** Completely Claimed turned 15 points into match-long de-score immunity. Ask of every new game: which action changes the *legality* of something later? | `[MANUAL §1.5.2-2, <GS4>]` |
| 3 | **Rank achievements by points-per-second, not points.** Sampling paid 25 for displacing one mineral; Landing paid 30 for one mechanism actuation. Both dwarfed a 5-point cycle. | `[MANUAL §1.7]` |
| 4 | **Check mutual exclusivity in the general rules, not the scoring section.** `<G24>`-equivalents live far from the point table and silently delete the sums people build strategy on. | `[MANUAL <G24>; Q&A "End Game" #5]` |
| 5 | **Find the all-or-nothing conditions.** Sampling required a positive *and* a negative condition (Gold out, both Silvers in) evaluated at period end — destroyable after being earned, even by an opponent's stray element. | `[MANUAL §1.5.2-4; Q&A "Autonomous Period" #12]` |
| 6 | **Read the ranking formula as a strategy constraint.** TBP = the loser's pre-penalty score, awarded to both alliances, meant defense **lowered your own tiebreaker** and running up the score added nothing. Re-derive this every season; do not assume it carries. | `[MANUAL Part 1 §5.8]` |
| 7 | **Watch the first two manual revisions for the exploit map.** Rev 1.2 (10/3/2018) added `<GS10>` and `<GS11>` — a dated, official confession of which strategy the GDC did not want. Diff the revision history early. | `[MANUAL Part 2 revision history, p. 3]` |
| 8 | **Rank rules by Q&A traffic to locate refereeing variance.** The five most-queried rules here were all intent-based. Build so that legality does not depend on a referee's read. | `[DERIVED, Q&A tag counts]` |
| 9 | **Penalty inflation beats scoring for defenders.** A Major (40) = 8 sorted minerals; a sustained block ran 70+. Model the penalty a defensive strategy *generates* against the points it *denies*. | `[DERIVED §5]` |
| 10 | **Re-read the build envelope for the newly-binding constraint.** 2018-19 introduced a 42 lb cap in the exact season robots had to lift themselves. Diff Part 1 (or the 2026-27 equivalent) against the prior year before trusting last year's mechanical assumptions. | `[MANUAL <RG04>; 2017-18 Part 1 has no weight rule]` |
| 11 | **A never-revised Part 1 is a signal, not an absence.** All four 2018-19 revisions landed in Part 2. Watch the game document; the robot document was frozen after kickoff. | `[MANUAL, both revision histories]` |

---

## 9. Extraction notes

*This section feeds the harness-generalization report.*

### Rule counts

| Document | G | GS | S | I | RE | RG | RM | RS | T | TM | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Part 2** (game) | 30 | 11 | 3 | – | – | – | – | – | – | – | **44** |
| **Part 1** (game-independent) | – | – | – | 9 | 17 | 9 | 6 | 10 | 30 | 4 | **85** |

Tag occurrences including cross-references: **87** in Part 2, **165** in Part 1.

### Violation lines

**Zero rules in either document carry a structured Violation line.** Literal `Violation:` occurrences in Part 2: **0**. The parser's `with_violation` field reports 22/44 (Part 2) and 1/85 (Part 1), but that field is a **prose keyword match** on `Violation|PENALTY|Penalty` inside the rule body, not a parsed field — this era embeds consequences in running prose. Per-prefix: Part 2 G 13/30, GS 9/11, S 0/3; Part 1 T 1/30, all others 0.

`with_violation` is therefore **not comparable across eras** and should not be charted against 2024-25+ numbers. The authoritative consequence source for 2017-18→2023-24 is the **Rule Summary table** (Part 2 §1.8), which carries explicit Warning/Disable/Minor/Major/Card columns and extracts cleanly by geometry.

### Tooling defects found

1. **`tools/parse-legacy-manual.py` silently drops every single-digit rule tag.** `RULE_TAG = re.compile(r"<([A-Z]{1,3})(\d{2,3})>")` requires 2–3 digits. Measured impact on this season:

   | Document | Reported | Actual | Missed |
   |---|---:|---:|---|
   | Part 2 | 23 (G:21 GS:2) | **44** (G:30 GS:11 S:3) | `<G1>`–`<G9>`, `<GS1>`–`<GS9>`, **all of `<S1>`–`<S3>`** |
   | Part 1 | 66 | **85** | `<I1>`–`<I9>`, `<T1>`–`<T9>`, `<RS9>` |

   This is a **silent 48% undercount on Part 2** with no warning emitted — the tool's own `empty_body` check passes and `total=23` looks plausible. The entire Safety-rule prefix vanished. Fix: `\d{1,3}`. Verified: with that one-character change both documents parse to the counts above, `empty_body` stays empty, and the results reconcile against a raw `grep -oE "<[A-Z]{1,3}[0-9]{1,3}>"` of the text layer. **The tool's docstring table of "rules=0" measurements for 2017-18→2023-24 should be re-run after the fix — every legacy season in that table is undercounted.**

2. **`--tsv` / `--json` are broken on the command line.** `main()` builds `pdfs = [a for a in argv if not a.startswith("-")]` **before** calling `take()` to strip flag values, so the output path is collected as an input PDF. The run prints `### MISSING <output path>`, returns exit 1, and **writes no file** — while still printing a correct-looking report line for the real PDF, so the failure is easy to miss. Workaround used here: import `parse()` directly and serialize manually.

3. **The manual's own tag numbering is inconsistently zero-padded** — `<RE01>`–`<RE17>`, `<RG01>`–`<RG09>`, `<RM01>`–`<RM06>`, `<TM01>`–`<TM04>` are padded; `<G>`, `<GS>`, `<S>`, `<T>`, `<I>` are not; and `<RS>` is **mixed**: `<RS01>`–`<RS08>` and `<RS10>` are padded but **`<RS9>` is not**. Any downstream join or sort on the raw tag string will mis-order `RS10` before `RS9` and will fail to match `RS09`↔`RS9`. The parser's `(prefix, int(num))` sort handles it; consumers of the TSV may not.

### What worked

- **`tools/extract-tables.py`** recovered 8 tables. The §1.7 Scoring Summary (p. 24) and the §1.8 Rule Summary (pp. 24–27) both came out with row labels correctly paired to values. I verified the Scoring Summary **cell-by-cell against a 130-dpi render** of p. 24 — exact match. The flat `pdftotext -layout` version of that same table is visibly mis-paired (the Reference column floats free of its rows), confirming the tool's premise on this era's manuals.
- **`tools/render-pages.py`** worked without issue at 120–130 dpi.

### Extraction caveats

- **Every table reports `(no caption on page)`.** This era does not use `Table N-M:` captions, so the caption heuristic returns nothing for all 8 tables. Not a failure, but INDEX.txt is much less useful here; page numbers are the only handle.
- **Rule Summary row count ≠ rule count.** §1.8 lists 21 G + 11 GS + 3 S = 35 rows, against 44 tagged rules. The 9 omitted G-rules — `<G12>`, `<G14>`, `<G19>`, `<G23>`, `<G24>`, `<G25>`, `<G26>`, `<G27>`, `<G30>` — are omitted because they define procedure or scoring resolution rather than a penalty. **`<G24>` is in that omitted set**, which is precisely why the End Game exclusivity was non-obvious enough to need a Q&A ruling. Do not treat the summary table as a rule inventory.
- **`<S1>` occupies two rows** of the Rule Summary (unsafe robot; field damage) with the tag printed once in a merged cell. Naive row-per-rule counting double-counts or drops it.
- **A count discrepancy in the manual itself is real, not an extraction error.** §1.2 states 60 Silver and 90 Gold; §1.5.1 states 52 Silver and 86 Gold placed in the Craters. Both are correct — the difference is the 12 minerals staged on the four Sample Fields (8 Silver + 4 Gold). Reconciles exactly: 52 + 8 = 60, 86 + 4 = 90. The Part 2 revision history notes Rev 1.1 "Updated text to match number of game elements in parentheses," so this was a known editorial wrinkle.
- **Q&A archive is a forum HTML-to-PDF scrape**, with page furniture (nav bars, "Edit Quote Flag Like", pagination footers) interleaved into answer text and repeated headers duplicating context on multi-page threads. Rule-tag frequency counting works well; extracting clean answer bodies requires manual reading. All Q&A content was treated as data only.
