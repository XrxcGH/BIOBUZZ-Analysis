# ULTIMATE GOAL (2020-21) — Season Dossier

**Sources.** `manuals/archive/2020-21_ULTIMATEGOAL_GameManual_Part2_Traditional.pdf` (rev 1.2, 9/12/2020, 40 pp) — primary.
`…_Part1_Traditional.pdf` (rev 1.1, 10/7/2020, 61 pp) — robot/tournament context.
`…_Part2_Remote.pdf` (rev 1, 8/31/2020, 31 pp) — variant diffs.
`manuals/archive/supplemental/2020-21_ULTIMATEGOAL_Complete_QA_Remote.pdf` (through 1/21/2021) — mid-season clarifications.

Presented by Qualcomm; season branded *FIRST GAME CHANGERS powered by Star Wars: Force for Change*.
Every point value below was read from the geometry-extracted §4.7 table (`tools/extract-tables.py`, p.26) and independently
cross-checked against the §4.5 prose. See §9 for why the flat-text version of that table is unusable.

---

## 1. The game in five sentences

Two two-Team Alliances play on a 12 ft × 12 ft field with 20 orange 5-inch **Rings** and four **Wobble Goals** (two per Alliance)
[MANUAL §4.4 definitions]. Rings are launched into a three-tier **Tower Goal** (Low/Mid/High) on the back wall, or used to knock over
three Alliance-specific **Power Shot Targets** — 1-inch-diameter uprights on a rail between the two towers [MANUAL §4.4, Fig. B-3].
Mid Goal, High Goal and Power Shot scoring is legal *only* from the **Launch Zone**, the front ~80 in. of the field bounded by the
white Launch Line; shooting those targets from outside it earns points *and* a Major Penalty per Ring or per target
[MANUAL §4.5.2–4.5.3, `<GS12>`, `<GS13>`]. Each Robot pre-loads exactly one Wobble Goal and delivers it in Autonomous to a
**Target Zone** chosen at random and announced by the size of a pre-placed **Starter Stack** — 0, 1 or 4 Rings meaning Zone A, B or C
[MANUAL §4.5.1]. In the last 30 seconds the Wobble Goals are worth far more if pushed *over the front wall* into the Drop Zone, and
the Power Shots reset and become scorable a second time [MANUAL §4.5.4].

**The one structural fact that drives everything else:** a Team's Ranking Points are its Alliance's **raw final score**, not a win/loss
record [MANUAL Part 1 §3 definitions, §5.1]. See §4 and §7.

---

## 2. Match structure

| Period | Length | Notes |
|---|---|---|
| Pre-Match setup | untimed | Robots Parked In their Alliance Start Line, touching the front (audience) wall, Completely Inside the Perimeter. Exactly one Wobble Goal pre-loaded per Robot; up to three Rings pre-loaded per Robot; Rings may not be loaded onto the Wobble Goal [MANUAL §4.5.1] |
| **Field randomization** | untimed | Happens *after* setup is complete. Starter Stack set to 0/1/4 Rings; excess Rings dropped into that Alliance's Low Goal [MANUAL §4.5.1] |
| **Autonomous** | 0:30 | Pre-programmed only; Driver Station in a hands-off location. Teams must use the built-in 30-second timer [MANUAL §4.4 *Autonomous Period*, §4.5.2] |
| Transition | ~0:05 + "3-2-1-go" | Hands-off; field personnel do not enter or touch Robots [MANUAL `<G1>`] |
| **Driver-Controlled** | 2:00 | [MANUAL §4.4 *Driver-Controlled Period*] |
| ↳ **End Game** | final 0:30 of Driver-Controlled | Teleop scoring continues *in addition to* End Game tasks. Tasks "started and/or completed prior to the start of the End Game earn zero points" [MANUAL §4.5.4] |
| **Total** | **2:30** | [MANUAL §4.4 *Match*] |

**Changes evident from within the manuals.**

- 2020-21 is the first season shipping a **Remote** variant alongside **Traditional**: single-Team Matches on a full or official half field, developed "to mimic traditional FIRST Tech Challenge events, while practicing social distancing" [MANUAL Part 2 Remote §3.0]. Remote differences are catalogued at the end of §5.
- Part 1 defines **Sports Start** — Teams start their Robot after the 3-2-1 countdown [MANUAL Part 1 §3 definitions].
- Comparison to 2019-20 SKYSTONE period lengths: **UNVERIFIED** — not stated in these documents; the revision history covers only in-season changes.

**In-season revisions worth knowing** [MANUAL Part 2 revision table, p.3]: rev 1.1 (8/31) added `<GS13>` Illegal Power Shot Scoring
and added the End Game Power Shot point value to §4.7 (i.e. the End Game Power Shot was *missing a printed value* at kickoff);
rev 1.2 (9/12) added the requirement that the Robot be **Completely** In the Launch Zone to score a Power Shot.

---

## 3. Scoring table

All values from the §4.7 Scoring Summary, recovered by geometry from p.26 (6 rows × 6 cols); §4.5 references are the manual's own.

| Scoring achievement | AUTO | TELEOP | END GAME | When Scored | Cite |
|---|---:|---:|---:|---|---|
| Wobble Goal Completely In its Alliance Target Zone (each) | **15** | – | – | End of Period | §4.7 / §4.5.2.1 |
| Wobble Goal In its Alliance Start Line (each) | – | – | **5** | End of Period | §4.7 / §4.5.4.1a |
| Wobble Goal Supported by the Drop Zone (each) | – | – | **20** | End of Period | §4.7 / §4.5.4.1b |
| Robot Navigating — Parked with any part In the Launch Line (each Robot) | **5** | – | – | End of Period | §4.7 / §4.5.2.2 |
| Ring in **Low** Goal (each) | **3** | **2** | 2 † | Scored Live | §4.7 / §4.5.2.3a, §4.5.3.1 |
| Ring in **Mid** Goal (each) | **6** | **4** | 4 † | Scored Live | §4.7 / §4.5.2.3b, §4.5.3.2 |
| Ring in **High** Goal (each) | **12** | **6** | 6 † | Scored Live | §4.7 / §4.5.2.3c, §4.5.3.3 |
| Power Shot Target moved Forward → Back (each) | **15** | – | **15** | Scored at Rest | §4.7 / §4.5.2.4, §4.5.4.3 |
| Ring Completely Supported by a Wobble Goal, or by a Ring Completely Supported by one (each) | – | – | **5** | End of Period | §4.7 / §4.5.4.2 |
| Minor Penalty | −10 | −10 | −10 | subtracted from the **offending** Alliance | §4.4 *Penalty*, §4.5.6 |
| Major Penalty | −30 | −30 | −30 | subtracted from the **offending** Alliance | §4.4 *Penalty*, §4.5.6 |

† [MANUAL §4.5.4] The §4.7 table leaves the End Game column blank for Tower Goal Rings. §4.5.4 states "Driver-Controlled Period
Scoring can still take place during the End Game", so teleop Ring values simply continue through the last 30 seconds. The blank cell
is not a zero.

**Location and eligibility gates on the above** (these are conditions, not modifiers):

| Achievement | Gate | Cite |
|---|---|---|
| Low Goal | Scoring Robot may be anywhere Inside the Playing Field | §4.5.2.3a, §4.5.3.1 |
| Mid / High Goal | Scoring Robot must be **Completely In** the Launch Zone (small Inconsequential extension allowed) | §4.5.2.3b/c, §4.5.3, orange boxes |
| Power Shot | Scoring Robot must be **Completely In** the Launch Zone | §4.5.2.4, §4.5.4.3 |
| Power Shot (End Game) | Targets already Back at the start of End Game are ineligible; Human Player has a 10-second grace period to reset them | §4.5.4.3b |
| Wobble Goal (End Game) | Must be In a Target Zone **or not located in the Launch Zone** at the *start* of End Game | §4.5.4.1 |
| Any Scoring Element | Zero value while in contact with / Controlled by a Robot of the corresponding Alliance | `<G10>` |
| Robot or element in two Scoring Areas | Only the highest-value achievement counts; if equal, only one counts | `<G5>` |

**Field geometry that prices these** (read from rendered figures; Appendices B–F of Part 2 are images with no text layer):

| Dimension | Value | Cite |
|---|---|---|
| Playing Field | 12 ft × 12 ft (144 in.), 36 Tiles of 24 in. | §4.4 *Playing Field*, *Tile* |
| Launch Line, from the front (audience) wall | ≈ 80 in. | Fig. B-4 (caption: "approximate") |
| ⇒ horizontal shot distance, Launch Line to Tower wall | ≈ 64 in. (5.3 ft) | [DERIVED: 144 − 80] |
| Starter Stack Area | 47 in. from front wall, 34 in. from side wall | Fig. B-4 |
| Start Line | 22.75 in. long × 2 in. wide, at 22.75 in. and 47 in. from the side wall | §4.4 *Start Line*, Fig. B-4 |
| Target Zone Goal | ≈ 22.75 in. square; three per Alliance, A nearest the Launch Line → C nearest the Tower wall | §4.4 *Target Zone Goal*, Fig. 4.3-2 |
| Tower Goal opening heights above the floor (stacked datum) | 13.0 / 21.0 / 33.0 in., + a 5.0 in. increment above 33.0 | Fig. B-2 |
| Tower Goal opening widths | 16.0 in. (upper) and 23.0 in. (Mid) | Fig. B-2 |
| Power Shot Target | 1.0 in. diameter uprights; rail at 21.0 in., tops at 26.0 in. | Fig. B-3 |
| Power Shot Target spacing | 7.5 in. apart, innermost 3.5 in. from centre | [DERIVED: 11.0 − 3.5 = 7.5; 18.5 − 11.0 = 7.5, Fig. B-3] |
| Rings in play | 20 | §4.4 *Ring* |
| Wobble Goals | 4 total, 2 per Alliance | §4.4 *Wobble Goal* |

[JUDGMENT] Fig. B-2 dimensions the goal boundaries as a stack from the floor but does not label which number belongs to which goal;
the natural reading is Low ≤13 in., Mid 13–21 in., High 21–33 in. Treat the mapping, not the numbers, as inferred.

**Which goal belongs to whom.** The two Tower Goals split ownership so that an Alliance's Mid Goal is on the *opposite* tower from
its Low and High Goals [MANUAL §4.4 *Tower Goal* table]:

| | Tower nearest the **Blue** Alliance Station | Tower nearest the **Red** Alliance Station |
|---|---|---|
| Low | Blue | Red |
| Mid | **Red** | **Blue** |
| High | Blue | Red |

---

## 4. Bonuses, randomization and ranking

**There are no bonuses, multipliers or ownership mechanics in ULTIMATE GOAL.** Every point in the game is a flat per-element or
per-achievement award. The only "bonus-shaped" thing is that the Power Shot objective is **priced twice in one Match** (Autonomous
and again in End Game) off the same physical targets.

### Randomization

| Property | Value | Cite |
|---|---|---|
| What is randomized | One of three field configurations, selecting Target Zone **A**, **B** or **C** | §4.5.1 |
| When | **After** Robot setup is complete and referees have given the setup-complete signal | §4.5.1 |
| How it is revealed | The physical **Starter Stack** in front of the Robot is adjusted to **0 / 1 / 4** Rings ⇒ Zone **A / B / C**. Excess Rings are dropped into that Alliance's Low Goal | §4.5.1, §4.4 *Starter Stack* |
| Sensing required | Vision on a stack of 0/1/4 Rings — no fiducial marker. Five Navigation Images (letter/A4) on the walls are available for localisation | §4.4 *Navigation Image*, Appx. F |
| Consequence of touching the Robot or Driver Station once randomization has begun | Minor Penalty **and** that Robot is ineligible for the Autonomous Wobble Goal Delivery score. Penalty is Team-only; the partner Robot stays eligible | `<GS5>` |
| Value at stake per Robot | 15 points | §4.7 |

[JUDGMENT] The randomization is self-balancing in a way worth naming: the *farthest* Target Zone (C) comes with the *largest* Ring
bounty (4 free Rings sitting 47 in. from the wall), and the nearest zone (A) comes with none. The random draw therefore trades drive
time against Ring supply rather than simply being harder or easier. Starter Stack Rings are explicitly legal to shoot in Autonomous
[Q&A, Autonomous Period: "Yes. Keep in mind that the Ring Control/Possession limits described in rule `<GS6>` apply to all periods"].

### Ranking

| Sort key | Definition | Cite |
|---|---|---|
| 1. Total Ranking Points | **The Alliance's final score for the Match**, summed over all non-Surrogate Qualification Matches. (Remote: the single Team's own final score.) | Part 1 §3 *Ranking Points*, §5.1 |
| 2. Total TBP1 | The Alliance's **Autonomous Period score**, summed | Part 1 §3 *TieBreaker Points* |
| 3. Total TBP2 | The Alliance's **End Game specific task score**, summed | Part 1 §3 *TieBreaker Points* |
| 4. | Random electronic selection | Part 1 §5.1 |

- Surrogate Matches earn no RP or TBP [Part 1 §3 *Surrogate Match*].
- League Tournament ranking = top ten league-meet Matches + top five League Tournament Matches [Part 1 §5.2].
- Elimination Matches award win/loss/tie, not RP [Part 1 §4].
- Penalties subtract from the **offending** Alliance's own score [§4.5.6] — so under a score-based RP formula, a Penalty is a direct
  Ranking Point loss, and there is no mechanism by which harming the opponent improves your rank.
- [JUDGMENT] TBP2 is "End Game **specific task** score", which reads as the three End-Game-only achievements (Wobble Goal Start
  Line / Drop Zone / Wobble Goal Rings, plus End Game Power Shots) and *not* the Tower Goal Rings that merely happen to land in the
  last 30 seconds. The manual does not enumerate it.

---

## 5. The rules that shaped play

Penalty currency: **Minor = 10 points, Major = 30 points**, deducted from the offender's own score [§4.4 *Penalty*, §4.5.6].
Rule-summary key [§4.8]: `1x` = single cost, `1x+` = single cost **every 5 seconds**, `2x` = double cost, `*` = optional.

### Game-specific rules (§4.6.3)

| Rule | Threshold / trigger | Consequence |
|---|---|---|
| `<GS1>` | Extension outside the Playing Field Perimeter allowed **only** for Low Goal scoring (back wall) and, during End Game, Drop Zone Wobble Goal delivery (front wall) | Anything else falls to `<S2>`: **Yellow Card** + optional Disable |
| `<GS2>` | Human Player may move within the Human Player Station while collecting/returning Rings and resetting Power Shots | — |
| `<GS3>` | Robots **may** grasp Rings and Wobble Goals (overrides `<G25>`) | — |
| `<GS4>` | Human Player Ring handling: (a) no Rings before teleop; (b) only via own Return Rack, no tools; (c) no storing a supply of Rings; (d) may not extend inside the Perimeter; (e) may reach into a Tower Goal for stuck Rings only when all Robots are ≥1 Tile away; (f) may hold more than one Ring | Referee warning, then **Minor per occurrence**; (c) is per Ring **plus per Ring every 5 s** |
| `<GS5>` | Touching Robot or Driver Station once randomization has begun | **Minor** + that Robot forfeits the Autonomous Wobble Goal Delivery score (offender only) |
| `<GS6>` | **Rings: max 3 Controlled/Possessed. Wobble Goals: max 1.** A Launched Ring counts as Controlled until it contacts something else | Rings: **Minor per excess Ring immediately, + Minor per excess Ring every 5 s, + an additional Minor per Ring Scored while over the limit**; escalates to Yellow. Wobble Goals: Minor per excess + Minor per 5 s, **Major** per excess Wobble Goal Scored while over |
| `<GS6>(1)a` | Plowing through Rings is fine; **Herding** or directing Rings above the limit for advantage is not | as above |
| `<GS6>(1)b` | Controlling a Ring **before it has been Supported by the Playing Field Floor** | **Minor per occurrence**, escalating to **Major + Yellow** on recurrence |
| `<GS6>(1)c` | Rings Supported by a Wobble Goal are **exempt** from the 3-Ring limit | — |
| `<GS7>(1)` | Rings may be Launched in any period. A Ring launched over any wall **other than the Tower Goal wall** | **Minor per Ring** |
| `<GS7>(2)` | Launching a Wobble Goal | **Major** + that Wobble Goal scores nothing for the period |
| `<GS8>` | Interfering with the opponent's scoring attempts or their Starter Stack Area **during Autonomous** | **Major each** |
| `<GS9>a–d` | Interfering with / Controlling an opposing Wobble Goal Completely In its Target Zone; de-scoring an opposing Wobble Goal in End Game; Blocking access to one in End Game; interfering with an opponent's Drop Zone delivery while their Robot is within 1 Tile of the Front Wall in End Game | **Major each** |
| `<GS9>e–f` | De-scoring Rings off an opposing Wobble Goal in End Game (per Ring); placing Rings onto Wobble Goals **outside** End Game (per Ring) | **Minor each**; hoarding strategies escalate via `<G30>` |
| `<GS10>` | Interfering with an opponent's Launched Ring **≥18 in. above the floor** that was launched with intent to Score | **Major each**, escalating to Yellow (anti-goaltending, in the air) |
| `<GS11>` | Preventing access to the opponent's Tower **Low** Goal | **Immediate Major each**, escalating to Yellow (anti-goaltending, on the ground) |
| `<GS12>` | Placing or Launching a Ring into a **Mid or High** Goal from **outside** the Launch Zone | **Major per Ring** |
| `<GS13>` | Scoring a **Power Shot** Target from outside the Launch Zone, by any means | **Major per Target** |

> **Manual defect.** In §4.6.3 the last rule is printed as `<G13>`, not `<GS13>`, colliding with the real `<G13>` *Pre-Match Robot
> Placement*. The §4.8 rule-summary table and the revision history both call it `<GS13>`, and the Remote manual labels it correctly.
> Verified with two independent text engines — see §9.

**The compounding trap.** §4.5.2 and §4.5.3 both state that illegally Scored Rings and Power Shot Targets **earn points for the
Alliance *and* an offsetting Penalty**. Net effect [DERIVED, operands from §4.7 and §4.5.6]:

| Illegal act | Points gained | Penalty | **Net** |
|---|---:|---:|---:|
| High Goal Ring from outside the Launch Zone (teleop) | +6 | −30 | **−24 per Ring** |
| High Goal Ring from outside the Launch Zone (auto) | +12 | −30 | **−18 per Ring** |
| Power Shot from outside the Launch Zone | +15 | −30 | **−15 per Target** |
| A 3-Ring burst fired while drifting outside the Launch Zone (teleop) | +18 | −90 | **−72** |

The manual's own mitigation is the orange box under §4.5.2.4 and §4.5.3: *small, Inconsequential* extension outside the Launch Zone
while Launching is allowed. Everything beyond that is per-element Majors.

### General game rules that mattered most (§4.6.2)

| Rule | Threshold | Consequence |
|---|---|---|
| `<G14>` | Starting volume 18 × 18 × 18 in.; a Pre-Loaded Scoring Element may extend outside it | delay-of-game Penalty in place of delay |
| `<G20>` | Robots must be **Parked** at the End of both Autonomous and Driver-Controlled | **Minor**, *and the Robot's actions do not count toward the Alliance's Score* |
| `<G21>` | No Drive Team control or interaction during Autonomous; early stopping not allowed except for safety | **Major** |
| `<G18>` | Starting gameplay before a period starts | Minor, escalating to Major if it produced advantage |
| `<G24>` | Deliberately detaching parts / leaving mechanisms on the field | Minor; Major if it Blocks an opponent |
| `<G25>` | Grasping/attaching to anything other than Scoring Elements | warning, then **Major** |
| `<G27>` | Deliberately removing Game Elements from the field — **but elements removed in an attempt to Score are exempt** | Minor per element |
| `<G28>` | Pinning / Trapping / Blocking; offender must retreat **3 ft (≈1.5 Tiles)** | **Minor every 5 seconds** |
| `<G29>` | Using Game Elements to ease or amplify a Scoring or game activity | **Major**, escalates to Yellow quickly |
| `<G26>` | Destruction, damage, tipping, entanglement — but "Robot-to-Robot contact and defensive gameplay should be expected" | referee discretion |
| `<S2>` | Any Robot contact outside the Perimeter not permitted by `<GS1>` | **Yellow Card** + optional Disable |
| `<S1>` | Unsafe operation or Playing Field damage | Disable + optional Yellow; significant damage → Red |

Yellow Cards are additive: a second Yellow becomes a **Red** [§4.4 *Yellow Cards and Red Cards*].

### Traditional vs. Remote (Part 2 Remote, rev 1)

- **Point values are identical** across both variants (verified line-by-line against §4.5 of the Remote manual).
- One Team, one Robot per Match; the Team's own score is its Ranking Points [Part 1 §3].
- The Remote manual **omits six rules — every one that presupposes an opponent on the field**: `<G3>` (forcing an opponent to break a
  rule), `<G28>` (pinning/trapping/blocking), `<GS8>` (Autonomous interference), `<GS10>` (Ring interference), `<GS11>` (Tower Goal
  interference). `<G30>` (Egregious Behavior) is also absent from Remote Part 2 entirely. Remaining rules keep their Traditional
  numbers, so `<GS9>` shrinks to just the "no Rings on Wobble Goals outside End Game" clause.
- Remote introduces a **Barrier** — an ≈12 in. tall structure separating the field from the Drop Zone. A Team using a taped field
  boundary **must build a physical Barrier** or the 20-point Drop Zone achievement is unavailable to it [Remote §4.4 *Barrier*; Q&A,
  End Game: "A Team using a taped Playing Field Boundary must add a physical Barrier … if the Wobble Goal Delivery to the Drop Zone
  task is part of the Team's Scoring strategy"].
- Remote inspection was on the honour system: "There will be no checks of Robots that compete in Remote events. We are relying on
  Teams to be honest… At traditional events, Rule `<RG08>`, along with all the other rules will be strictly enforced" [Q&A, General
  Robot Rules].

---

## 6. Robot archetypes that season

Build envelope from Part 1 (Traditional, rev 1.1):

| Constraint | Value | Cite |
|---|---|---|
| Starting size | 18 × 18 × 18 in.; must self-support in the Sizing Tool powered-off, or via an initialization routine | `<RG02>` |
| **Expansion after Match start** | **Unlimited** — "Robots may expand beyond the starting size constraint after the start of the Match" | `<RG02>` |
| DC motors | **max 8**, from a closed list (TETRIX, AndyMark NeveRest, Modern Robotics/MATRIX, REV HD Hex, REV Core Hex) | `<RE10>` |
| Servos | max 12; VEX EDR 393 counts as a servo (max 2 per REV Servo Power Module) | `<RE11>` |
| Control system | REV Expansion Hub or REV Control Hub; ≤1 additional Expansion Hub | `<RE07>`–`<RE09>` |
| Stored energy | battery, change in centre of gravity, **or deformation of Robot parts** — springs and elastics are legal launchers | `<RG06>` |
| Launching Robot parts | prohibited, even if tethered | `<RG07>` |
| **Launcher energy cap** | a launched Scoring Element must not travel **>16 ft (4.88 m) horizontally or >5 ft (1.52 m) in elevation** | `<RG08>` |
| Weight limit | none stated in Part 1 §7 | `<RG01>`–`<RG08>` (absent) |

`<RG08>` is the single most under-appreciated build rule of the season, and the Q&A hammered it (9 hits, second only to `<GS6>`):

- The "or" is **conjunctive in effect**: "A Launched Ring that travels in the air more than 16 feet violates rule `<RG08>`. A Launched
  Ring that travels more than 5 feet in elevation violates rule `<RG08>`" [Q&A, Gameplay — All Match Periods]. Both caps bind.
- Enforcement is a *demonstration on demand*: "If a Referee feels the Robot is Launching rings in excess of the requirement, then
  Teams must demonstrate that the Robot **as configured** cannot Launch Rings exceeding the limits" [Q&A, General Robot Rules].
- **A software limit is acceptable** [Q&A, General Robot Rules] — so a velocity-capped flywheel controller satisfied the rule without
  mechanical de-rating.

### The archetypes

| Archetype | What it had to be | Motor/servo budget [DERIVED against `<RE10>`] | Notes |
|---|---|---|---|
| **Flywheel shooter** (the default build) | Floor intake for 5-in. Rings, a ≤3-Ring magazine, a transfer, and a flywheel aimed ~64 in. horizontally at a goal opening 21–33 in. up | 4 drive + 1–2 flywheel + 1 intake + 1 transfer = **7–8 of 8** | The 8-motor cap is the binding constraint of the whole season. A 4-motor drive + 2-motor flywheel leaves **two** motors for intake, transfer *and* wobble arm — one of those had to become a servo |
| **Wobble Goal manipulator** | Gripper + arm able to lift a Wobble Goal and reach **over the front wall** into the Drop Zone (legal under `<GS1>`) | 0–1 motor + 1–2 servos | Teams that spent a motor here paid for it in the shooter. Unlimited expansion (`<RG02>`) made long servo-driven arms viable |
| **Power Shot specialist** | A **tunable, lower-energy** launch and heading precision good enough to hit a 1.0-in. rod at ~64 in., with targets 7.5 in. apart | shares the shooter | Requires either a turret or a repeatable Robot heading. This is a *different tune* from the High Goal — see §7 |
| **Autonomous Ring runner** | Vision on a 0/1/4 Ring stack, odometry or Navigation Image localisation, plus the ability to intake the 4-Ring stack and feed the High Goal at 12/Ring | shares the drivetrain | Five wall-mounted Navigation Images were the only fiducials [§4.4, Appx. F] |
| **Defender / blocker** | Almost nothing to build | — | And almost nothing to gain: see §7 |

[JUDGMENT] The combination of *unlimited expansion after start* + *no weight limit* + *8 motors* pushed this season toward tall,
light, single-purpose Robots. The 18-in. cube was a packing problem, not a play constraint.

---

## 7. The strategic lesson

**When Ranking Points are the raw score, the game stops being a contest and becomes a solo throughput optimisation — and the right
question is points *per Ring*, not points per shot.**

### Where the points actually were

The Ring supply was hard-capped three ways: **20 Rings on the field** [§4.4], a **3-Ring possession limit** [`<GS6>`], and **one Human
Player per Alliance** feeding **one Return Rack per Alliance** for two Robots [§4.4 *Drive Team*, *Return Rack*, `<GS4>`]. Teleop was
therefore **supply-limited, not shooter-limited**. Under that constraint, price the objectives per Ring [DERIVED, all operands from §4.7]:

| Objective | Rings consumed | Points | **Points per Ring** |
|---|---:|---:|---:|
| Power Shots, Autonomous (3 targets) | 3 | 45 | **15.0** |
| Power Shots, End Game (3 targets, after reset) | 3 | 45 | **15.0** |
| High Goal, Autonomous | 1 | 12 | 12.0 |
| High Goal, teleop | 1 | 6 | 6.0 |
| Ring stacked on a Wobble Goal, End Game | 1 | 5 | 5.0 |
| Mid Goal, teleop | 1 | 4 | 4.0 |
| Low Goal, teleop | 1 | 2 | 2.0 |
| **Wobble Goal program** (2 × 15 auto Target Zone + 2 × 20 End Game Drop Zone) | **0** | **70** | **∞** |

Six Rings spent on Power Shots return **90 points**. The same six Rings put through the High Goal (three in auto at 12, three in
teleop at 6) return **54** [DERIVED: 36 + 18]. That is a **36-point swing off six Rings**, and the Power Shot version needs no
sustained cycle at all — it is six aimed shots in a 2:30 Match.

The complete no-Ring program is worth **70 points** per Alliance [DERIVED: 2×15 + 2×20], plus up to **5 per Ring** stacked on each
Wobble Goal in End Game. A Wobble Goal parked in the Drop Zone carrying three Rings is worth **35 points** [DERIVED: 20 + 3×5], and
two of them is **70 points in the last 30 seconds** — matching an entire disciplined teleop High Goal run for a fraction of the build.

### The "obvious" strategy that underperformed

**The High Goal flywheel.** It is the loudest, most visible objective, it has the biggest single number in Autonomous (12), and it is
the thing every promotional animation shows. It underperformed for three compounding reasons:

1. **It is priced last per Ring** of the launch objectives once teleop starts (6 vs. the Power Shot's 15).
2. **It consumed the entire motor budget** (`<RE10>`, 8 motors), crowding out the Wobble Goal arm that pays 70 Ring-free points.
3. **It is the wrong tune for the Power Shot.** This is the sharpest lesson of the season. A Power Shot is **Scored at Rest**
   [§4.5.2.4c], and the GDC ruled that a target knocked Back which then bounces Forward **does not count** — followed by an explicit
   design note: *"Reducing the Robot's Ring Launch energy is likely to prevent the scenario described in the question"* [Q&A,
   Autonomous Period and End Game, "Power Shot Scoring"]. A launcher tuned to reliably clear a 33-in. goal at 64 in. is over-energised
   for a 1-in. pivoting rod. A single fixed-power flywheel could not do both well, and the Teams that only tuned for the High Goal
   quietly forfeited 90 points a Match.

Two supporting rulings from the same thread: a target only needs to be **beyond vertical away from the field** to count, not fully
Back; and a "stiff" target is a field-maintenance fault, not a scoring condition [Q&A, "Power Shot Scoring"].

### The eligibility gate that ate 40 points

§4.5.4.1: at the **start** of End Game, a Wobble Goal is eligible for the Start Line and Drop Zone achievements only if it is
**In a Target Zone or not located in the Launch Zone**. The Launch Zone is exactly where a shooter Robot lives for the whole Match.
A Team that kept its second Wobble Goal beside the shooter — the natural, tidy thing to do — made 20 points per goal unreachable at
0:30 with no way to recover. The Q&A was asked about this twice in different words:

- Pre-positioning a Wobble Goal outside the Launch Zone and lunging for the Barrier the instant End Game begins is **not** starting
  the task early [Q&A, End Game, 10/23/2020].
- The second Wobble Goal may be moved into a Target Zone or across the Launch Line **at any time**, including during Autonomous and
  during teleop before End Game [Q&A, End Game, 10/24/2020: "Yes to all three questions"].

This is a pure bookkeeping objective — a 40-point-per-Alliance swing available to anyone who read §4.5.4.1 carefully, and invisible to
anyone who didn't.

### The rule that was genuinely ambiguous

`<GS6>` drew **16 Q&A references — more than any other rule that season**, and every one of them is the same collision: a shooter
parked in the Launch Zone holding its maximum three Rings, while the Human Player keeps feeding fresh Rings out of the Return Rack
into that same space. The line the GDC eventually drew:

- Inadvertent contact from a returned Ring while already holding three is **not** a violation; deliberately moving to block a
  returning Ring while holding three **is** [Q&A, Driver-Controlled Period, 12/15 and 12/16/2020].
- Momentary fourth-Ring possession with automatic ejection is fine "provided that the fourth Ring Possession is brief, Inadvertent,
  and Inconsequential"; but scoring while over the limit stacks a **second** Minor on top of the possession Minor [Q&A, 12/23/2020].
- `<GS6>(1)b` requires the Ring to be **directly** Supported by the Playing Field Floor before a Robot may Control it. **There is no
  transitive support**: a Ring that falls from the Return Rack onto a Wobble Goal without ever touching the floor is illegal to
  Control, per Ring [Q&A, End Game, 11/16/2020].

[JUDGMENT] The design flaw is structural, not editorial: the game put the Ring re-entry point and the mandatory shooting position in
the same region of the field, then imposed a hard possession cap there. Any season that re-injects Scoring Elements into the zone
where Robots must stand will generate this exact class of question.

### Where defence went to die

Defence was close to strictly negative-EV in 2020-21, and this is unusually clean-cut:

- Ranking is on **your own score** [Part 1 §5.1], so suppressing the opponent contributes **nothing** to your rank.
- Every second spent defending is a second not cycling — a direct RP loss.
- Penalties come off **your** score [§4.5.6], so a failed defensive play is doubly costly.
- The aggressive plays were fenced off anyway: `<GS10>` (Major for touching an airborne Ring ≥18 in.), `<GS11>` (immediate Major for
  camping the opponent's Low Goal), `<GS8>` (Major for Autonomous interference), `<GS9>a–d` (Majors around opposing Wobble Goals),
  `<G28>` (Minor every 5 s for pinning).

The only defence with a positive expectation was the *legal* kind: occupying the best Launch Zone shooting lane first.

---

## 8. Signals for BIOBUZZ (2026-27)

1. **Read the ranking formula before the scoring table.** RP = raw score turns the game into a solo throughput problem and makes
   defence worthless; RP = win/loss makes defence a weapon. ULTIMATE GOAL is the archive's cleanest score-based-RP case, and every
   strategic conclusion above flows from it. Establish which regime BIOBUZZ is in on day one.
2. **When the Scoring Element supply is capped, price everything in points *per element*, not per action.** UG's cap was triple
   (20 Rings, 3-Ring possession, one Human Player and one Return Rack per Alliance). Build the points-per-element and
   points-per-second tables *before* choosing a mechanism.
3. **Find the objective that consumes zero Scoring Elements.** UG's Wobble Goal program was worth 70 points per Alliance with no
   Rings, no launcher and no competition for field resources. There is usually one of these and it is usually mispriced.
4. **Find the objective that is priced twice in one Match.** Power Shots paid 15 each in Autonomous and 15 again in End Game off the
   same hardware — the build cost is paid once and collected twice. Always the best return on engineering.
5. **Hunt for eligibility gates keyed to a state at a period boundary.** UG §4.5.4.1 required the Wobble Goal to be outside the
   Launch Zone *at the instant End Game started*. These gates are free points for careful readers and silent 20-point losses for
   everyone else. Grep the new manual for "at the start of", "at the End of the Period", and "eligible".
6. **Look for two objectives that demand opposite tunings of the same mechanism.** High Goal wanted power; Power Shot wanted
   finesse, and an over-energised shot scored zero because the target bounced back. A single-tune mechanism silently forfeits one of
   them. Ask early: does any pair of targets want different exit velocities, angles or precisions?
7. **Cost the motor/actuator budget against the strategy list in week one.** UG's 8-motor cap (`<RE10>`) was what actually forced the
   choice between "good shooter" and "shooter plus Wobble arm". Whatever BIOBUZZ's limit is, enumerate mechanisms against it before
   committing to a strategy.
8. **Per-element penalty tiers can exceed the value of an entire scoring run.** `<GS12>`/`<GS13>` charged a **Major per Ring / per
   target** for firing from outside a zone, netting −24 per Ring. Identify every per-element Major in the new manual and build a hard
   localisation interlock — do not fire unless the Robot knows it is inside the zone.
9. **Read the build rules for a *demonstrable* cap, not just a dimensional one.** `<RG08>`'s 16 ft / 5 ft launch limit was enforced by
   on-demand demonstration and satisfiable in **software**. Caps of that shape are cheap to comply with and expensive to discover at
   inspection.
10. **Use Q&A density as the ambiguity map.** `<GS6>` (16 hits) and `<RG08>` (9 hits) were the two genuine ambiguities of the season,
    and both were predictable from the manual text alone: a possession cap in the same space where elements re-enter the field, and
    an "or" between two numeric limits. Scan the new manual for those two shapes at kickoff.
11. **Watch for randomization that doubles as a resource.** UG's Starter Stack *was* the randomization signal *and* a Ring supply,
    with the farthest zone carrying the biggest bounty. If BIOBUZZ randomizes, check whether the indicator has independent value.
12. **Expect manual defects and cross-check every rule tag against the rule-summary table.** UG shipped a rule printed as `<G13>`
    that collides with a different `<G13>` — see §9. A parse that trusts inline tags alone will silently lose a rule.

---

## 9. Extraction notes

### Rule inventory (corrected)

**Part 2 Traditional, rev 1.2 — 40 pp, 46 rule definitions, 108 tag occurrences**

| Prefix | Meaning | Count | Range | Carried a Violation/Penalty line |
|---|---|---:|---|---:|
| `S` | Safety rules (§4.6.1) | 3 | S1–S3 | 0 |
| `G` | General game rules (§4.6.2) | 30 | G1–G30 | 16 |
| `GS` | Game-specific rules (§4.6.3) | 13 | GS1–GS13 | 9 |
| **Total** | | **46** | | **25 (54%)** |

Rules with no Violation/Penalty line: G1–G10, G12, G13, G16, G27, GS1, GS2, GS3, GS7, S1, S2, S3. G1–G9 are definitional by design —
§4.8 groups them under "General Rules – Further definitions, no Penalties earned". The `S` rules state consequences in prose
(Disable / Yellow Card) without the word "Penalty", so the violation regex misses all three.

**Part 1 Traditional, rev 1.1 — 61 pp, 73 real rule definitions + 1 false positive, 158 tag occurrences**

| Prefix | Meaning | Count | Range |
|---|---|---:|---|
| `C` | Competition rules | 26 | C01–C26 |
| `I` | Inspection | 7 | I01–I07 |
| `RE` | Robot electrical | 18 | RE01–RE18 |
| `RG` | Robot general | 8 | RG01–RG08 |
| `RM` | Robot mechanical / materials | 5 | RM01–RM05 |
| `RS` | Robot software | 9 | RS01–RS09 |
| **Total** | | **73** | |

Only **1** Part 1 rule carried a Violation/Penalty line — Part 1 states consequences narratively rather than with a keyed
"Violation:" clause. Any harness metric that uses "has a Violation line" as a completeness check will read Part 1 as broken.

**Part 2 Remote, rev 1 — 31 pp, 40 rules** (G 27, GS 10, S 3; 21 with a violation line). Omits `<G3>`, `<G28>`, `<G30>`, `<GS8>`,
`<GS10>`, `<GS11>`; retains Traditional numbering for everything else.

### What the tooling got wrong on this manual

1. **`--tsv` and `--json` are broken in `tools/parse-legacy-manual.py`.** `pdfs = [a for a in argv if not a.startswith("-")]`
   executes *before* `take("--tsv")` strips the flag and its value, so the output path is parsed as a second input PDF. The tool
   printed `### MISSING …/ug_p2.tsv` and wrote nothing (the `len(pdfs) == 1` guard also suppressed the write). **Fix:** move the two
   `take()` calls above the `pdfs = [...]` assignment. **Workaround used here:** import `parse()` and serialise the result directly.

2. **The tag regex silently drops every single-digit rule — this is the serious one.**
   `RULE_TAG = re.compile(r"<([A-Z]{1,3})(\d{2,3})>")` requires **two or more** digits. ULTIMATE GOAL numbers its rules without
   zero-padding: `<G1>`…`<G9>`, `<GS1>`…`<GS9>`, `<S1>`–`<S3>`. The tool reported **`rules=25 (G:21 GS:4)`** for Part 2; the true
   count is **46 (S:3 G:30 GS:13)**. All three safety rules and the first nine general game rules were invisible, including `<G5>`
   (highest-value-only scoring) and `<G9>` (Inadvertent / Inconsequential) — both load-bearing for scoring analysis. Changing the
   quantifier to `\d{1,3}` recovers them. **This is not UG-specific:** any legacy manual using un-padded numbering is under-counted,
   so the docstring's per-season rule counts should be re-measured after the fix.

3. **Revision-history cross-references win the deduplication.** The parser keeps whichever occurrence of a tag has the longest
   trailing text. The Part 2 revision-history table on p.3 flattens into one long run-on line, so `<GS13>`'s extracted "body" came
   from the changelog — *"to rule summary table Updated Sponsor lockup • Section 4 – Various – Changed Ultimate Goal…"* — instead of
   §4.6.3. **Fix:** skip lines before the start of §4 (or before the Contents block) when deduplicating.

4. **A genuine defect in the manual, confirmed with two independent text engines.** In §4.6.3 (PDF p.26) of Part 2 Traditional
   rev 1.2, the final game-specific rule is printed as `<G13> Illegal Power Shot Scoring`. Both `pdftotext -layout` and
   `pymupdf.get_text()` return the same string, so it is not an extraction artifact. The §4.8 rule-summary table lists it as
   `<GS13> Illegal Power Shot Scoring`, the revision history says "Added rule `<GS13>`", and the Remote manual labels it `<GS13>`
   correctly. `<G13>` is already *Pre-Match Robot Placement*, so a naive tag-keyed parse overwrites one rule with the other. **Any
   legacy-manual harness needs a duplicate-tag check that reconciles inline tags against the rule-summary table.**

5. **`<I7>` in Part 1 is a false positive.** It originates in the Robot Inspection Checklist appendix, which cross-references rules
   with un-padded numbers (`<I7>`, `<I7>a`). The same appendix's column wrapping also produces truncated fragments such as `RG02>`
   with the opening bracket lost. Multi-column checklist tables are the main source of tag noise in Part 1; the appendix should be
   excluded from definition extraction.

6. **`<C10>` extracts with an empty body** (correctly flagged by the tool). It is a heading — `<C10> Time-Outs` — whose content sits
   in indented sub-bullets after a blank line, and the body-accumulation loop stops at the first blank line. Real content, not a
   defect in the manual.

7. **Flat text mis-pairs the scoring table exactly as the house rules warn.** `pdftotext -layout` on §4.7 produced rows where the
   label and its values are on different lines: `Wobble Goals Delivered (each)` appears with no number, `Robot Navigating (each)` is
   printed beside `5 / – / 20` (the 20 belongs to Drop Zone), and `• High` lands beside `12 / 2 / 5`. Building a scoring model from
   that text would have mis-priced at least four rows. `tools/extract-tables.py` recovered the 6 × 6 table on p.26 correctly, and
   every value in §3 above was then re-verified against the §4.5 prose independently.

8. **`extract-tables.py` found no captions on any page** ("no caption on page" for all 11 tables). This era's manual captions figures
   as `B-4 Playing Field Tape Dimensions` and does not caption tables at all, so `INDEX.txt` is page-number-only. Not a bug — but the
   harness must not rely on `Table N-M:` captions for pre-2024 manuals. Page 3's revision-history table was also flagged `SPLIT?`
   (empty first cell), a false alarm caused by a merged header.

9. **All field geometry had to be read from rendered images.** Appendices B–F of Part 2 are figure-only with no text layer, so the
   Launch Line position, Tower Goal heights, Power Shot dimensions and Starter Stack randomization layout came from
   `tools/render-pages.py` output plus clipped high-DPI re-renders. **Caution:** Figure B-4 is not to scale vertically (the square
   field is drawn wider than tall), so pixel measurement is unreliable; its dimensions are a stacked datum from the front wall and
   must be read as such. The 80 in. Launch Line position was confirmed by cross-checking against the tile grid in Figure 4.3-2.

10. **Scratchpad filename collision (harness-level).** Generic intermediate names (`p2.txt`, `p2_rules.txt`) collide when sibling
    per-season agents share one scratchpad directory. My first Part 2 text extraction was silently overwritten with a different
    season's manual between two tool calls, and the only reason it was caught was a sanity grep for the season name. **Season-scoped
    output paths and a post-extraction identity check (`grep -c '<game name>'`) should be mandatory in the harness.**
