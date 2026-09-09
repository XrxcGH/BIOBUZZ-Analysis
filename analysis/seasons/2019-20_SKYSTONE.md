# SKYSTONE presented by Qualcomm — FTC 2019-20 Season Dossier

**Sources.** Game Manual Part 2 (the game), Rev 1.3 dated 12.5.2019, 41 pp — `manuals/archive/wayback/2019-20_SKYSTONE_GameManual_Part2.pdf`. Game Manual Part 1 (game-independent), Rev 1.3 dated 11.21.2019, 62 pp — `manuals/archive/wayback/2019-20_SKYSTONE_GameManual_Part1.pdf`. Official Q&A archive (captured 1/30/2020) — `manuals/archive/supplemental/2019-20_SKYSTONE_Complete_QA.pdf`.

**Era note.** 2019-20 uses the two-part manual split (Part 1 game-independent, Part 2 game). There is **no Traditional/Remote variant** for this season — that split begins in 2020-21. Rule tags are inline angle-bracket style (`<G1>`, `<GS10>`, `<S1>`, `<RG02>`).

**Label key.** `[MANUAL]` = the text says it · `[DERIVED]` = arithmetic, operands shown · `[JUDGMENT]` = my read.

---

## 1. The game in five sentences

Two two-Team Alliances share a 12 ft × 12 ft field split by a three-section **Skybridge** into a **Loading Zone** (audience side) and a **Building Zone** (far side), with each Alliance owning a **Quarry** of six Stones, a **Depot**, a **Foundation**, and a corner **Building Site** `[MANUAL §4.3, §4.4]`. Robots earn points by **Delivering** Stones — carrying one from Completely In the Loading Zone to Completely In the Building Zone, with the *robot itself* passing under its own Alliance's 14-inch Skybridge section — and by **Placing** them In the Foundation `[MANUAL §4.5.2.2 Note, §4.5.3.1-2, §4.4 "Deliver"]`. Two of the six Stones in each Quarry are **Skystones**, marked with an image, arranged in one of three randomized patterns; delivering a Skystone as one of your first two Autonomous deliveries is worth 10 points against 2 for a plain Stone `[MANUAL §4.5.2.2a, Appendix D]`. Stones Interlocked into a vertical **Skyscraper** on the Foundation pay a per-level bonus, and a Team-built **Capstone** dropped on top in the End Game pays again per supporting level `[MANUAL §4.5.3.3, §4.5.4.1]`. The End Game inverts the Autonomous objective: you get 10 points for pulling the Foundation **into** your Building Site during Autonomous, then 15 more for dragging it **back out** during the last 30 seconds so both robots can Park in that same corner `[MANUAL §4.5.2.1, §4.5.4.2, §4.5.4.3; confirmed by Q&A thread "Section 4.5.4 End Game Foundation Moved Task"]`.

---

## 2. Match structure

| Period | Length | Notes |
|---|---|---|
| Pre-Match setup | untimed | Field crew loads 24 Stones per Stone Supply; referees then place 6 Stones (4 Stones + 2 Skystones) per Quarry in one of three random patterns `[MANUAL §4.5.1]` |
| **Autonomous** | 0:30 | Pre-programmed only; Driver Station in a hands-off location; start command issued from the DS Android device `[MANUAL §4.5.2]` |
| Transition | 0:05 + "3-2-1-go" | Hands-off; field personnel do not touch robots `[MANUAL §4.5.3, `<G12>`]` |
| **Driver-Controlled** | 2:00 | Includes the End Game `[MANUAL §4.5, §4.5.3]` |
| ↳ **End Game** | last 0:30 of Driver-Controlled | Not a separate period; Driver-Controlled scoring continues throughout `[MANUAL §4.5.4]` |
| **Total** | **2:30** | `[MANUAL §4.5]` |

**Timing gotchas** `[MANUAL]`

- Except for Parking, an End Game task completed *before* the End Game starts earns **zero** for that task (§4.5.4).
- Robots must **Park** (be motionless) at the end of both periods; a robot still moving after roughly a one-second grace period takes a Minor Penalty *and* forfeits the actions taken after the sound (`<G10>`).
- Skyscraper, Placing and Capstone achievements are scored only **after all Scoring Elements come to rest** following the Match — an explicit concession that towers fall when the Foundation gets dragged (§4.5.4 Note).

**Versus 2018-19 ROVER RUCKUS:** not assessed — the prior-season manual was not read for this dossier. **UNVERIFIED.**

---

## 3. Scoring table

All values below are read from the **§4.7 Scoring Summary** table recovered by geometry (`tools/extract-tables.py`, PDF p.25) and independently confirmed against the §4.5 gameplay prose. The 2019-20 manual does **not** number its tables, so it is cited as "§4.7" throughout.

| # | Scoring achievement | AUTO | TELEOP | END GAME | Manual ref | When scored |
|---|---|---:|---:|---:|---|---|
| 1 | Repositioning — Foundation In your Building Site at end of Auto, not touching your robot | **10** | — | — | §4.5.2.1 | End of Period |
| 2 | Stone Delivery — **initial two**, if a **Skystone** | **10** ea | — | — | §4.5.2.2a | As it occurs |
| 3 | Stone Delivery — **initial two**, if a plain **Stone** | **2** ea | — | — | §4.5.2.2a | As it occurs |
| 4 | Stone Delivery — **third and higher** (Stone or Skystone) | **2** ea | — | — | §4.5.2.2b | As it occurs |
| 5 | Navigating — robot Parked over the Loading/Building tape *and* under its own Skybridge | **5** ea | — | — | §4.5.2.3 | End of Period |
| 6 | Placing — each Stone In the Foundation | **4** ea | **1** ea | — | §4.5.2.4 / §4.5.3.2 | End of Period |
| 7 | Stone Delivery (Driver-Controlled) | — | **1** ea | — | §4.5.3.1 | As it occurs |
| 8 | Tallest Skyscraper Bonus — per Skyscraper Level, **tallest tower only** | — | **2** / Level | — | §4.5.3.3 | End of Match |
| 9 | Capping — Capstone fully Supported On a Skyscraper or Foundation | — | — | **5** ea | §4.5.4.1a | End of Match |
| 10 | Capping Bonus — per **Level that Supports** the Capstone | — | — | **1** / Level | §4.5.4.1b | End of Match |
| 11 | Foundation Moved — Completely **Out** of the Building Site by end of Match (must have been In at start of End Game) | — | — | **15** | §4.5.4.2 | End of Match |
| 12 | Parking — robot Parked In your Building Site at T=0:00 | — | — | **5** ea | §4.5.4.3 | End of Match |

> Row 12 (`Parking`) is **not** in the geometry-extracted table — it fell across a page break and had to be recovered from §4.5.4.3 prose. See Extraction Notes defect 4.

### Negative and zero-value actions `[MANUAL]`

| Action | Value | Ref |
|---|---:|---|
| Stone **Returned** during Autonomous (Building Zone → Loading Zone) | **−2** ea | §4.5.2.2c |
| **First** Stone Returned during Autonomous **if it is a Skystone** | **−10** | §4.5.2.2c |
| Stone Returned during Driver-Controlled | **−1** ea | §4.5.3.1 |
| Stone Returned as a result of a **falling Skyscraper** | **no deduction** | §4.4 "Return" |
| Stone Delivered under the **Alliance-neutral** Skybridge | **0** | §4.5.3.1 |
| Scoring Element in contact with / Controlled by a robot of the corresponding Alliance | **0** | `<G21>` |
| **Minor Penalty** — awarded to the non-offending Alliance | **+5** | §4.5.6, §4.4 "Penalty" |
| **Major Penalty** — awarded to the non-offending Alliance | **+20** | §4.5.6, §4.4 "Penalty" |

### Scoring edge cases resolved by Q&A

`[MANUAL — official forum ruling; forum rulings take precedence over the manual per §4.1]`

| Question | Ruling |
|---|---|
| Auto: one Skystone only | 10 |
| Auto: Skystone then Stone | 12 (10 + 2) |
| Auto: Stone then Skystone | 12 (2 + 10) |
| Navigating: must the drivetrain be over the tape? | **No** — any portion of a Parked robot over the tape and under its own Skybridge qualifies; an extended arm counts |
| Parking: is an extended tape measure into the Building Site legal? | **Yes**, and it counts as Parked, provided `<G17>` entanglement is not violated |
| Capping: may the Capstone overhang and touch the side walls of lower Stones? | **Yes** — does not reduce effective height |
| Foundation Moved: must the Foundation enter the Building Site during Auto? | **No** — it may be moved In at any time before the End Game starts; it need only be In when End Game begins |

> **Interaction not resolved in the manual or the Q&A archive:** whether a single Stone can earn both Autonomous Delivery (§4.5.2.2) *and* Autonomous Placing (§4.5.2.4). The two rows carry different "When Scored" semantics ("As it occurs" vs "End of Period"), which reads as independent, but `<G24>` (highest-value achievement only, when In two or more Scoring Areas) is a plausible counter-reading. **UNVERIFIED.**

---

## 4. Bonuses, randomization and ranking

### Randomized objective — the Quarry

| Property | Detail | Ref |
|---|---|---|
| What is randomized | Position of the **2 Skystones** among the 6 Stones in each Quarry | `[MANUAL §4.4 "Quarry", §4.5.1]` |
| Number of configurations | **3** (Pattern A / B / C) | `[MANUAL §4.5.1, Appendix D]` |
| Skystone spacing | The two Skystones sit **3 positions apart** in the 6-Stone row (A = 1 & 4, B = 2 & 5, C = 3 & 6) | `[MANUAL Appendix D figure]` |
| How revealed | **Physical dice roll** by field personnel — 1 or 4 → A, 2 or 5 → B, 3 or 6 → C | `[MANUAL Appendix D figure]` |
| When revealed | During pre-Match setup, *after* robots are staged | `[MANUAL §4.5.1]` |
| **Can teams react to it?** | **No.** `<GS12>` forbids touching the robot or Driver Station once randomization begins; violation is a Minor Penalty **and** the offending robot loses all Autonomous Stone Delivery credit (partner robot unaffected) | `[MANUAL <GS12>]` |

> `[JUDGMENT]` `<GS12>` is the decisive design choice of the season. Because you may not select an opmode after seeing the pattern, the 10-point Skystone is reachable only through **on-robot vision**. The 3-position spacing then makes the problem cheaper than it looks: detect **one** Skystone and the second is deterministically at +3, so a single successful detection unlocks both 10-point deliveries.

### Bonus / multiplier mechanics `[MANUAL]`

- **Tallest Skyscraper Bonus** (§4.5.3.3): 2 points per Level of your **tallest** Skyscraper only. Ties in height among your own towers score once. A Skyscraper requires (a) its lowest Level Interlocked with the Foundation, all higher Stones Interlocked with the Stone below, and (b) **no contact from an Alliance robot** (§4.4 "Skyscraper", "Skyscraper Level"). This is a height bonus, not a volume bonus — a second tower is worth nothing beyond its Delivery + Placing points.
- **Capping Bonus** (§4.5.4.1b): 1 point per Level Supporting the Capstone. A Capstone may sit on another legally scored Capstone, but the lower Capstone does **not** count as a Level. Multiple Capstones on one Skyscraper each score, but **a robot may only Score one Capstone** (§4.5.4.1c-d).
- **Ownership-style mechanics: none.** There is no zone control, no possession multiplier, no Alliance-specific stone. All 56 Stones and all 4 Skystones are Alliance-**neutral** (§4.4) — the only Alliance-specific Scoring Elements are the two Foundations and the Team-built Capstones.

### Ranking formula (Qualification Matches) `[MANUAL Part 1 §4.8.1, §3.2 definitions]`

Ranked in order:

1. **Average Ranking Points** — 2 for a win, 1 for a tie, 0 for a loss / disqualification / no-show, divided by matches played.
2. **Average TieBreaker Points** — see below.
3. Highest Match Score.
4. Random electronic draw.

**TieBreaker Points (TBP):** each match awards **both** Alliances the **losing** Alliance's **pre-penalized** score. Ties award both the lowest pre-penalized score. A disqualified/no-show Team gets 0 TBP and that match is **not** eligible to be dropped. If both Teams on an Alliance are disqualified, the winners receive their **own** pre-penalized score.

**Drop rule:** with 5-6 matches, the single lowest TBP match is dropped; with 7 or more, the **two** lowest are dropped. The divisor is matches played minus the dropped matches. The manual's worked example: RP 2,2,0,1,2 over 5 matches → Avg RP 1.4; TBP 15,65,125,200,78 → drop 15 → (65+125+200+78)/4 = **117**.

**League play** (Part 1 §4.8.2): match data carries across Meets; after the second Meet a Team is ranked on its **top 10** matches; at the League Tournament all 15 (best 10 Meet + 5 LT) are pooled and the **two lowest TBP** dropped, with all League Tournament matches counting. Match precedence for "top": more RP first, then higher TBP, then higher score.

> `[DERIVED]` Because TBP is the **loser's pre-penalized** score, penalties move wins but never move TBP. A blowout is worth less in the tiebreaker than a close win against a strong opponent — your TBP is bounded above by your opponent's output, not your own.

---

## 5. The rules that shaped play

**Rule inventory (Part 2):** 45 tagged rules — `<S1>`–`<S3>` (3 safety), `<G1>`–`<G30>` (30 general), `<GS1>`–`<GS12>` (12 game-specific). Precedence, per §4.6: **Safety > Game-Specific > General**, and **official Q&A forum rulings take precedence over everything in the manuals** (§4.1, §4.6).

### The twelve game-specific rules

| Rule | Threshold / trigger | Consequence tier | Ref |
|---|---|---|---|
| `<GS1>` Human Player supplied Stones/Capstones | Driver-Controlled only; **one element at a time**; hand-delivered only; may not break the wall plane or deliver while a robot **or** element is already In the Depot; elements must be In the Depot and Completely On the floor before a robot Controls them; Auto hand-deliveries score **nothing** | Minor per occurrence | §4.6.3 |
| `<GS2>` Autonomous interference | May not interfere with the opponent's scoring attempts or contact/disrupt the **opposing Quarry** during Auto | **Major** per violation + offender's scoring using opponent elements is voided | §4.6.3 |
| `<GS3>` Control/Possession limits | Max **1 Stone and/or 1 Capstone**. Plowing legal; herding/directing multiple for advantage illegal. Foundation-resident Stones exempt. Controlling an **opposing** Capstone = Major | Minor per element over limit, **+1 Minor per element per 5 s**; **double Major** per excess element **Scored** while over the limit; escalates to Yellow Card | §4.6.3 |
| `<GS4>` Launching | No Launching by robot or Human Player | Minor per element Launched | §4.6.3 |
| `<GS5>` Foundation scoring interference | Robots may not be In the **opponent's** Foundation, nor interfere with an opposing robot that is In its own Foundation | **Major** immediately, **+1 Minor per 5 s**, escalates to Yellow | §4.6.3 |
| `<GS6>` Blocking the Depot | May not be In or Block access to the opponent's Depot. Must retreat **3 ft (0.9 m) ≈ 1.5 tiles within 5 s** of a warning | Warning, then **Major + 1 Minor per 5 s**; explicit exception to `<G25>` — a **Disabled** robot in the opposing Depot still earns these penalties and a Yellow Card | §4.6.3 |
| `<GS7>` Skybridge penalties | (a) no grabbing/hanging on Skybridge pipes; (b) no crossing zones via the **opponent's** Skybridge section; (c) no blocking the **Neutral** Skybridge | (a) Major, (b) Major, (c) penalized per `<G18>` | §4.6.3 |
| `<GS8>` Controlling the opponent's Foundation | Illegal when their Foundation is In their Building Site, **or at any time during End Game** | **Major + 1 Minor per 5 s**, escalates to Yellow | §4.6.3 |
| `<GS9>` De-scoring | May not remove/reposition Stones or Capstones from the opponent's Foundation when it is In their Building Site or at any time during End Game | **Double Minor per Stone**; **+ Major** if a Capstone is de-scored | §4.6.3 |
| `<GS10>` Foundation movement | Foundations must remain **Completely In the Building Zone** | Minor per 5 s out of the Zone — charged to the Alliance that **moved** it (Q&A) | §4.6.3 |
| `<GS11>` Skybridge safety | Never step or jump over any Skybridge section (Q&A extends this to crawling/sliding **under** it) | Warning → Minor → Major → treated as Egregious `<G28>` | §4.6.3 |
| `<GS12>` Touching after randomization | No touching robot or Driver Station once randomization begins | Minor **+ that robot forfeits Autonomous Stone Delivery scoring**; partner unaffected | §4.6.3 |

### General rules that mattered most `[MANUAL]`

- `<G4>` / `<RG02>` — **18 in × 18 in × 18 in** starting volume; the pre-loaded Scoring Element may protrude. **After the start of the Match the robot may extend in any dimension** — and no `<GS>` rule restricts expansion this season. Violation: robot removed, counted a no-show, zero RP/TBP.
- `<G16>` — robots may not grab, grasp or attach to any Game Element **other than Scoring Elements**. Because the **Foundation is defined as a Scoring Element** (§4.4), a Foundation grabber is legal; a Skybridge grabber is not (`<GS7>`a). Warning, then Major.
- `<G18>` — Pinning / Trapping / Blocking: **Minor per 5 seconds**, and on a referee warning the offender must retreat **3 ft**. Not penalized in Auto unless a deliberate strategy; if it does occur in Auto, the offender's **first** Driver-Controlled action must be to move away.
- `<G21>` — a Scoring Element touching or Controlled by a robot of the corresponding Alliance is worth **zero**. This is what forces you to let go of the tower before the buzzer.
- `<G24>` — an element or robot In two or more Scoring Areas earns only the **highest** achievement.
- `<G29>` — no using Game Elements to ease or amplify scoring difficulty. Major, escalating quickly to Yellow. This was the catch-all the Game Design Committee reached for repeatedly (14 Q&A mentions).
- `<G19>` — forced rule violations are excused, no penalty assigned.
- `<G30>` — Inadvertent **and** Inconsequential violations may be waived at referee discretion.
- `<G26>` — field and Game Element tolerances of **±1.0 in (25.4 mm)**; Q&A confirms this **includes the Skybridge height**.

### Penalty economics `[DERIVED]`

Minor = 5, Major = 20 (§4.5.6). Operands from §4.5.2.2a and §4.5.3.3:

- One **Major Penalty** (20) = **two Autonomous Skystones** (10 + 10) = a **10-Level** Skyscraper's height bonus (2 × 10).
- The `<GS3>` **double Major** for scoring an over-limit element = **40** points — the single largest swing available to a referee's whistle in this game.
- A `<GS5>` / `<GS6>` / `<GS8>` violation held for 15 seconds = 20 + 5 + 5 + 5 = **35** — equal to the entire Foundation-plus-Parking package below.

---

## 6. Robot archetypes that season

### Hard constraints teams built against `[MANUAL]`

| Constraint | Value | Ref |
|---|---|---|
| Starting volume | 18 × 18 × 18 in (45.72 cm cube), self-supporting in the sizing tool with power OFF or via an init routine | `<RG02>`, `<G4>` |
| Expansion after start | **Unlimited** in every dimension — no game-specific restriction this season | `<RG02>`, `<G4>` |
| Weight | **42 lb (19.05 kg)** including battery | `<RG04>` |
| DC motors | **max 8**, from a closed list (TETRIX, AndyMark NeveRest, MR/MATRIX, REV HD Hex, REV Core Hex) | `<RE09>` |
| Servos | **max 12** (a VEX EDR 393 counts as a servo), 6 V or less, 3-wire connector | `<RE10>` |
| Battery | **single 12 V** main battery | `<RE03>` |
| **Alliance Skybridge clearance** | **14 in (355.6 mm)** — the robot must pass *completely* under it to score a Delivery | §4.4 "Skybridge", §4.5.2.2 Note |
| Neutral Skybridge clearance | 20 in (508 mm), but Stones delivered there are worth **0** | §4.4, §4.5.3.1 |
| Stone | 8 × 4 × 5 in tall; 56 neutral Stones + 4 Skystones | §4.4 |
| Foundation | 18.5 × 34.5 × 2 in | §4.4 |
| Building Site | right triangle, 22.75 in (57.8 cm) legs | §4.4 |
| Depot | ≈ 24 × 24 in | §4.4 |
| Capstone (Team Scoring Element) | max 4 × 4 × 8 in, min 3 × 3 × 4 in; no electronics; may not be built from this season's Scoring Elements; must carry the Team number legibly from 12 in | `<TE02>`, `<TE04>`, `<TE05>`, `<TE03>` |

> `[DERIVED]` **The 14-inch rule is the season's real size limit.** Alliance Skybridge clearance is 14 in and `<G26>` plus the Q&A "Skybridge Tolerance" ruling put field elements at ±1.0 in — so worst-case usable clearance is **13.0 in**. Every Delivery point in the game, in both periods, requires the whole robot to fit through that gap. The 18-inch starting cube was never the binding constraint; a 13-inch **dynamic** height ceiling was.

### Archetypes `[JUDGMENT, constrained by the cited rules]`

| Archetype | What it must do | Rule pressure it lives under |
|---|---|---|
| **Sub-13-inch delivery chassis** (mandatory floor for any Stone strategy) | Cross under its own Skybridge with a Stone Controlled, both robot and Stone Completely crossing the zone boundary | 14 in − 1.0 in tolerance; §4.5.2.2 Note explicitly bans kickers, push-through arms and any method that avoids the robot passing under |
| **Collapsing stacker** | Intake one Stone, transit under 13 in, then extend vertically without limit to Interlock a Level onto the Foundation, and **release** before the buzzer | Unlimited expansion (`<RG02>`); `<G21>` zeroes anything the robot is still touching; `<GS3>` caps it at one Stone at a time; the 8-motor budget (`<RE09>`) must cover drivetrain + intake + lift |
| **Foundation grabber** | Hooks or a claw that grabs the 18.5 × 34.5 in Foundation, drags it into the Building Site in Auto and back out in the End Game, then parks | Legal because the Foundation is a **Scoring Element** (§4.4) and `<G16>` only bans grasping non-Scoring Elements; `<GS10>` penalizes leaving the Building Zone; `<GS8>` makes the opponent's Foundation untouchable in End Game |
| **Vision Autonomous** | Detect one Skystone from the staged position and infer the second at +3; deliver both as the initial two deliveries | `<GS12>` bans post-randomization opmode selection, forcing real detection; Appendix D's 3-apart spacing halves the detection problem |
| **Depot / defense specialist** | Contest the Loading Zone without tripping the 5-second timers | `<GS6>` (Depot), `<GS5>` (Foundation), `<GS7>`c / `<G18>` (Skybridge, pinning) all charge **Major + Minor-per-5-s** — the field is heavily protected |

> `[JUDGMENT]` The 8-motor cap (`<RE09>`) is the quiet budget constraint. A holonomic drivetrain (`<RM03>`) spends 4 of 8; a lift spends 1-2; an intake spends 1-2. A robot that wants to drive omnidirectionally, stack tall, **and** drag the Foundation sits at the ceiling — which pushed many designs toward passive or servo-actuated Foundation hooks rather than a motorized mechanism.

---

## 7. The strategic lesson

**The one thing SKYSTONE teaches: when a game pays for a *state* rather than for *repetitions*, the state is almost always underpriced — and the repetition strategy is usually the fragile one.**

### The arithmetic

**Package A — the "obvious" strategy: build a tall capped Skyscraper.** For a tower of N Stones `[DERIVED, operands from §4.5.3.1, §4.5.3.2, §4.5.3.3, §4.5.4.1a, §4.5.4.1b]`:

```
Delivery        1 × N
Placing         1 × N
Skyscraper      2 × N   (tallest tower only)
Capping         5       (one Capstone)
Capping Bonus   1 × N
                -----
TOTAL       =   5N + 5
```

| N (Levels) | Approx. height (N × 5 in) | Points |
|---:|---:|---:|
| 3 | 15 in | 20 |
| 4 | 20 in | 25 |
| 5 | 25 in | 30 |
| **6** | **30 in** | **35** |
| 8 | 40 in | 45 |
| 10 | 50 in | 55 |

**Package B — the Foundation shuffle** `[DERIVED, operands from §4.5.2.1, §4.5.4.2, §4.5.4.3]`:

```
Repositioning (Auto, Foundation In Building Site)     10
Foundation Moved (End Game, Completely Out)           15
Parking × 2 robots                                5 + 5 = 10
                                                      -----
TOTAL                                             =    35
```

**Break-even:** `5N + 5 = 35 → N = 6`. `[DERIVED]`

> A six-level, roughly 30-inch tower — built one Stone at a time by a robot that has to duck under 13 inches between every single Stone — buys exactly what a drivetrain with a hook buys by dragging a plastic tray twice and sitting in a corner.

### Where the points really were

1. **The Autonomous Skystone was the highest-value single action in the game.** 10 points for one Delivery `[MANUAL §4.5.2.2a]`. Two of them = 20 = a **three-level capped tower** (5·3+5) built over the entire two-minute Driver-Controlled Period `[DERIVED]`. And the 10-point rate applies only to the **first two** deliveries — the third Stone drops to 2 `[MANUAL §4.5.2.2b]` — so the entire premium is front-loaded into the first ~15 seconds of the match.
2. **The Foundation was underpriced relative to its build cost.** 35 points `[DERIVED above]` for a mechanism with no height requirement, no vision requirement, no Interlocking precision requirement, and no dependence on the 13-inch gap. It is the only major scoring package in SKYSTONE that a robot can execute **without ever delivering a Stone**.
3. **The "obvious" strategy — tall towers — underperformed because the game actively destroys them.** The lowest Level of a Skyscraper must be Interlocked **with the Foundation** (§4.4 "Skyscraper"). The End Game requires dragging that same Foundation Completely Out of the Building Site (§4.5.4.2). The manual says the quiet part out loud: *"Due to the possibility that Skyscrapers may fall when Robots try to move the Foundation, the Skyscraper, Placing, and Capstone achievements will be Scored once all Scoring Elements have come to rest"* (§4.5.4 Note). A tower is not banked when built — it is banked only after your own partner finishes yanking its base across the floor. `[MANUAL + JUDGMENT]` The one mercy: Stones knocked into the Loading Zone by a **falling** Skyscraper do not incur the −1 Return deduction (§4.4 "Return").
4. **Height paid only once.** The Skyscraper Bonus is for the **tallest** tower only (§4.5.3.3). A second tower earns Delivery + Placing (2/Stone) and nothing else. The game rewarded one tall stack, not throughput — while simultaneously making that one tall stack the most fragile object on the field. `[MANUAL + JUDGMENT]`
5. **Penalties dwarfed offense in a protected-field game.** With Major = 20 (§4.5.6) and five separate rules charging Major-plus-Minor-per-5-seconds (`<GS3>`, `<GS5>`, `<GS6>`, `<GS8>`, plus `<GS3>`'s double-Major-on-score at 40), the cheapest way to score 35+ points was frequently to let a confused opponent linger near your Foundation or Depot. `[DERIVED from the §4.8 penalty table + §4.5.6]`

### The genuine ambiguity worth recording

**`<GS3>` Control/Possession Limits was the most-clarified rule of the season — 22 mentions across 9 distinct Q&A threads** (counting subject lines that name the rule), nearly double the next-highest: `<GS2>` 16 mentions / 5 threads, `<G29>` 14 / 4, `<GS5>` 12 / 1, `<GS6>` 11 / 4, `<GS8>` 11 / 3. The ambiguity is the boundary between legal **Plowing** ("inadvertent contact with Game Elements while in the path of the Robot", §4.4) and illegal **Herding** ("pushing or impelling one or more Game Elements to a desired location... that gains a strategic advantage beyond moving the Robot around the Playing Field", §4.4). Because the Quarry is a tight row of six Stones and the target Skystone is buried in it, essentially every intake geometry displaces neighbours on the way in. The Committee ultimately ruled broadly in favour of the builder:

- A U-shaped drivetrain that shoves the Stones on **both** sides of a Skystone aside while acquiring it — **legal Plowing**.
- The same, shoving two Stones on **one** side only — **legal Plowing**.
- Pushing a Stone out of the way when it blocks access to your own Foundation — **legal**, characterised as "removing a disadvantage caused by a Scoring Element."

> `[JUDGMENT]` The pattern: the rule's *text* is written around intent and advantage, which is unrefereeable in real time, so the rulings converged on a mechanical test instead — did the robot *retain* the extra elements, or merely displace them in passing? Any future season with a possession limit plus a densely packed source of elements will reproduce this exact argument. `<GS5>` shows the mirror-image failure: the Committee had to state explicitly that "a Robot that is attempting to Score does **not** have an automatic exemption from rule `<GS5>`" — i.e. offensive intent is not a defence against an interference rule.

---

## 8. Signals for BIOBUZZ (2026-27 kickoff)

| # | Signal | Why it generalizes |
|---|---|---|
| 1 | **Find the clearance number before the size limit.** Compute the season's binding *dynamic* dimension, not the starting cube. In SKYSTONE that was 14 in − 1.0 in tolerance = 13.0 in, and it gated 100% of Delivery scoring in both periods. Ask on day one: is there a gate, tunnel, bar or door that every scoring path must pass? | The starting-volume rule is loud and printed in bold; the real constraint is usually a field geometry buried in the definitions section |
| 2 | **Price every scoring package as points-per-mechanism, then find the break-even.** Foundation package = 35 for a hook + drivetrain; tower = 5N+5 for a vision system, intake, lift and precision Interlocking; `5N+5 = 35 → N = 6`. Run this arithmetic in the first 48 hours of kickoff. | Every FTC game has one objective whose point total is decoupled from its build difficulty. Identifying it early is the highest-leverage analysis of the season |
| 3 | **Check whether the game destroys its own scoring at the end.** Look for two objectives that share a physical object with opposite requirements. SKYSTONE: Repositioning wants the Foundation In, Foundation Moved wants it Out, and towers Interlock to it. When scoring is deferred until "all Scoring Elements come to rest," fragile accumulation is discounted. | Any endgame that moves a structure the whole match was built on converts stored points into a coin flip |
| 4 | **Read the randomization-*reaction* rule, not just the randomization.** `<GS12>` — no touching the robot or DS after randomization — is what turned a 3-way dice roll into a mandatory vision project. Also look for redundancy in the pattern (Skystones 3 apart ⇒ detect one, get both). | Whether a randomized objective is expensive depends entirely on whether you may react to it manually, and on how much of the pattern one observation reveals |
| 5 | **Count Q&A threads per rule to locate genuine ambiguity.** `<GS3>` drew 9 threads. Concentration of clarifications marks the rule your referees will call inconsistently — a scouting variable, not just a rules variable. | A heavily-clarified rule is one the drafters could not make refereeable; expect regional variance in enforcement |
| 6 | **Model penalty income as an offensive strategy.** With Major = 20, five rules charging Major + Minor-per-5-s, and one double-Major worth 40, SKYSTONE's protected zones were worth more per second than its scoring zones. Compute "penalty points per second of opponent error" alongside your own scoring rate. | Protected-zone rules with per-interval escalation are a recurring FTC pattern; their expected value is routinely underestimated at kickoff |
| 7 | **TBP is bounded by your opponent, not by you.** SKYSTONE's TieBreaker Point = the **losing** Alliance's **pre-penalized** score. Penalties decide wins but never TBP. Check each season whether the tiebreaker rewards your output or your opponent's. | Ranking-formula shape changes which matches matter and whether running up the score helps at all |
| 8 | **Look for "tallest only" / "best only" bonuses.** The Skyscraper Bonus paid for one tower. That converts a throughput game into a precision game and changes which archetype wins. | Max-of vs sum-of bonus structures are the single biggest determinant of whether cycle speed or reliability dominates |
| 9 | **Verify the motor/servo budget against the strategy list.** 8 motors (`<RE09>`) forced drivetrain-vs-lift-vs-Foundation tradeoffs. Build the motor-budget spreadsheet before committing to a three-objective robot. | The electrical rules cap how many objectives one robot can physically pursue |

---

## 9. Extraction notes

### Rule count by prefix

| Manual | Prefix | Rules | Range |
|---|---|---:|---|
| **Part 2** | `S` | 3 | S1-S3 |
| | `G` | 30 | G1-G30 |
| | `GS` | 12 | GS1-GS12 |
| | **subtotal** | **45** | 99 tag occurrences |
| **Part 1** | `I` | 9 | I1-I9 |
| | `RE` | 17 | RE01-RE17 |
| | `RG` | 9 | RG01-RG09 |
| | `RM` | 6 | RM01-RM06 |
| | `RS` | 10 | RS01-RS10 |
| | `T` | 31 | T1-T31 |
| | `TE` | 5 | TE01-TE05 |
| | **subtotal** | **87** | 179 tag occurrences |
| | **TOTAL** | **132** | |

### Violation-line coverage

| Manual | Rules with a violation/penalty phrase captured | Breakdown |
|---|---:|---|
| Part 2 | **21 / 45** | G: 12, GS: 9, S: 0 |
| Part 1 | **2 / 87** | both `T` |

**Important caveat — this is not "rules that carry a consequence."** SKYSTONE has **no `Violation:` lines at all**; consequences are written in running prose ("A Minor Penalty will be assessed..."). The parser's `VIOLATION` regex matches the words *Violation/Penalty* only within its **400-character body truncation**, so long rules whose penalty sentence falls past that window are scored as having none — `<GS1>` (penalty stated after sub-clauses a-g), `<GS3>` and `<GS6>` are all false negatives. **The authoritative consequence source for this season is the §4.8 Rule Summary table**, which the geometry extractor recovered cleanly across PDF pages 26-28: **37 rows** with explicit Warning / Disable / Minor / Major / Card columns, plus a Column Key on p.29.

`[DERIVED]` The 8 Part-2 rules **absent** from the §4.8 summary (45 − 37) are `<G14>`, `<G19>`, `<G23>`, `<G24>`, `<G25>`, `<G26>`, `<G27>`, `<G30>` — all interpretive or procedural (score certification, forced violations, element-as-robot, multi-area scoring, disabled eligibility, field tolerances, match replay, inadvertent/inconsequential). Their absence from the summary is correct, not an extraction gap.

### Tooling defects found on this manual

1. **`tools/parse-legacy-manual.py` silently drops every single-digit rule tag.** `RULE_TAG = re.compile(r"<([A-Z]{1,3})(\d{2,3})>")` requires **two or three** digits. SKYSTONE numbers its game rules without zero-padding (`<G1>`, `<GS1>`, `<S1>`), so the tool reported **rules=24** on Part 2 when the true count is **45** — losing `G1`-`G9`, `GS1`-`GS9` and `S1`-`S3` (21 of 45, **47%**). On Part 1 it reported 69 instead of 87, losing `I1`-`I9` and `T1`-`T9` (18 of 87, **21%**). Critically, the tool **does not warn**: it prints a confident `rules=24` and its `empty_body` check passes. Patching the quantifier to `\d{1,3}` recovers all of them with no false positives on either manual. **This is the highest-priority harness fix** — any 2017-18 to 2023-24 manual using unpadded low rule numbers is affected, and a downstream analyst has no way to detect the loss from the tool's output.
2. **`--tsv` / `--json` output paths are consumed as input PDFs.** In `main()`, `pdfs = [a for a in argv if not a.startswith("-")]` executes **before** `take("--tsv")` strips the flag/value pair, so the TSV destination is treated as a second input file. The invocation documented in the harness instructions produces `cannot extract text: Failed to open file '...tsv' as type tsv`, a spurious `### <out>.tsv: 0pp rules=0` line, the alarming-but-wrong `!! NO <TAG> RULES FOUND` banner, and **exit code 1** — while still writing the TSV correctly. Fix: move the two `take()` calls above the `pdfs` list comprehension.
3. **Rule-body mis-attribution from the "longest body wins" heuristic.** The parser keeps whichever occurrence of a tag is followed by the most text. For tags that also appear in the revision-history table (Part 2 p.3) or the inspection-checklist appendices (Part 1), the wrong occurrence wins. Confirmed mis-attributed bodies: **`<TE03>`, `<TE05>`, `<RS02>`, `<RS03>`, `<RS07>`** — all returned checklist or revision-log prose instead of rule text. All five were corrected by hand against the Part 1 source. A section-aware guard ("prefer the occurrence inside the rules section") would fix this.
4. **`tools/extract-tables.py` dropped the `Parking` row of the §4.7 Scoring Summary — and did not flag it.** The Scoring Summary breaks across PDF pages 25→26; the extractor returned a clean 9-row table on p.25 and never picked up the orphaned tenth row (`Parking | - | - | 5 | 4.5.4.3 | End of Match`) sitting above the §4.8 heading on p.26. `INDEX.txt` marked p.3 and p.29 with `SPLIT?` but **not** p.25/p.26, so the omission was invisible from the index. It was caught only by cross-reading the §4.5.4.3 prose. **A scoring model built from the geometry output alone would have been missing a 10-point-per-alliance End Game objective.** Lesson for the harness: always reconcile the summary table's row count against the gameplay section's enumerated achievements.
5. **The flat-text failure mode is confirmed on this manual, exactly as the harness warns.** `pdftotext -layout` renders §4.7 with labels and values on different lines — e.g. `Navigating 5 | 2 per Skyscraper Level` collapsed onto one row, and the Placing "4 / 1" pair split across three non-adjacent lines. Reading the scoring model from flat text here would pair *Navigating* with the *Skyscraper* bonus value. The geometry extractor got all 9 rows it captured correct.
6. **No table captions exist in this manual.** All 6 extracted tables report `(no caption on page)` — the 2019-20 manual does not number its tables. Citations in this dossier are therefore by **section** (§4.7 Scoring Summary, §4.8 Rule Summary), never by table number. The harness should not assume `Table N-M:` captions on pre-2024 manuals.
7. **`tools/render-pages.py` worked correctly** at 130 dpi on pages 7, 8 and 37. Appendix D (Quarry Randomization) is **figure-only** — the dice-roll mapping (1/4→A, 2/5→B, 3/6→C) and the three Skystone patterns exist nowhere in the text layer and are recoverable **only** by rendering p.37. Any text-only pipeline would miss the entire randomization-reveal mechanism, which is the season's central Autonomous design constraint.

### Reproduction

```bash
# rule extraction (requires the \d{1,3} patch from defect 1, and the defect 2 workaround)
python tools/parse-legacy-manual.py "manuals/archive/wayback/2019-20_SKYSTONE_GameManual_Part2.pdf"
python tools/parse-legacy-manual.py "manuals/archive/wayback/2019-20_SKYSTONE_GameManual_Part1.pdf"

# scoring + rule-summary tables by geometry (authoritative for all point values in this dossier)
python tools/extract-tables.py "manuals/archive/wayback/2019-20_SKYSTONE_GameManual_Part2.pdf" --out <dir>

# field illustration (p.7), definitions (p.8), Quarry randomization (p.37 - figure only)
python tools/render-pages.py "manuals/archive/wayback/2019-20_SKYSTONE_GameManual_Part2.pdf" --pages 7,8,37 --dpi 130 --out <dir>
```
