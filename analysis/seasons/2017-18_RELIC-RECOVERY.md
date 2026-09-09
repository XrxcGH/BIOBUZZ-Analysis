# FIRST Tech Challenge 2017-18 — RELIC RECOVERY (presented by Qualcomm)

**Season dossier for the BIOBUZZ 2026-27 kickoff harness.**

| | |
|---|---|
| Sources | Game Manual **Part 2** (the game), Rev 1.4, 11.21.2017, 42 pp; Game Manual **Part 1** (game-independent), Rev 1.3, 10/25/2017, 58 pp |
| Q&A | `2017-18_RELICRECOVERY_Complete_QA.pdf` — official forum answers, threads dated 09-2017 through 03-2018 |
| Era | Two-part manual (Part 1 = robot/event/tournament, Part 2 = game). Angle-bracket rule tags. **No Traditional/Remote split** — that begins 2020-21. |
| Manual paths | `manuals/archive/wayback/2017-18_RELICRECOVERY_GameManual_Part2.pdf`, `..._Part1.pdf` |

Labels used throughout: **[MANUAL]** = the text says it · **[DERIVED]** = arithmetic, operands shown · **[JUDGMENT]** = my read · **[Q&A]** = official forum ruling · **UNVERIFIED** = not in the documents I read.

---

## 1. The game in five sentences

Two two-team Alliances play on a 12 ft x 12 ft field for 2:30, scoring 6-inch foam cubes called **Glyphs** into wall-mounted **Cryptoboxes** that are three Columns wide and four Rows tall. [MANUAL §1.2, §1.4] Each robot starts *Balanced on a 23 in x 23 in Balancing Stone raised about 2 in off the floor*, preloaded with one Glyph, facing a randomized **Jewel Set** (one red ball, one blue ball on an unattached platform) and a randomized **Pictograph** that encodes which Cryptobox Column is the **Cryptobox Key** for that match. [MANUAL §1.4, §1.5.1, Appendix G] In the 30-second Autonomous Period an Alliance scores by knocking the *opponent's* Jewel off its platform (30), scoring Glyphs (15 each), landing its first Glyph in the Key Column (+30), and Parking in a Safe Zone (10). [MANUAL §1.5.2] In the two-minute Driver-Controlled Period Glyphs are worth only 2 each, with cumulative bonuses for completed Rows (10), Columns (20), and a fully correct 12-Glyph brown/gray **Cipher** (30). [MANUAL §1.5.3] In the last 30 seconds — the End Game — robots reach *over* the audience-facing wall to place Alliance-specific **Relics** on a mat outside the field (10/20/40 by Zone, +15 upright) and climb back onto their Balancing Stone (20). [MANUAL §1.5.4]

---

## 2. Match structure

| Period | Length | What is live | Citation |
|---|---|---|---|
| Pre-Match | — | Robots placed Balanced on own-colour Balancing Stone, one per Stone; one Glyph pre-loaded per robot; field personnel randomize Jewels + Pictographs by die roll | [MANUAL §1.5.1, Appendix G] |
| **Autonomous** | **30 s** | Pre-programmed only. Driver Station hands-off; single start touch permitted. Jewels, Glyphs @15, Cryptobox Key, Park | [MANUAL §1.4 "Autonomous Period", §1.5.2] |
| *Transition* | **5 s** | Drive Teams pick up Driver Stations, then 3-2-1 countdown. Hands-off on robots; field personnel do not enter | [MANUAL §1.5.3, `<G11>`] |
| **Driver-Controlled** | **120 s** | Glyphs @2, Rows, Columns, Cipher | [MANUAL §1.5.3] |
| **End Game** | **final 30 s** of Driver-Controlled | Relics, Balancing. All teleop scoring continues | [MANUAL §1.4 "End Game", §1.5.4] |
| **Total** | **2:30** | | [MANUAL §1.4 "Match"] |

**Changed vs 2016-17 VELOCITY VORTEX** — checked directly against `2016-17_VELOCITYVORTEX_GameManual_Part1/2`:

- **Unchanged:** 30 s auto / 2 min teleop / final-30 s End Game; Minor Penalty = 10, Major = 40; QP/RP ranking formula; 18-inch starting cube; 8 DC motors, 12 servos. [MANUAL, both seasons]
- **Changed — the randomized objective became vision-decoded.** 2016-17 placed Vuforia Vision Targets under each Beacon, but they "remain in the same locations for every Match" — navigation aids, not a randomizer. 2017-18's Pictograph is *randomly chosen per match* and *encodes a scoring instruction* (which Column is the Key). This is the first time in this era that a camera read is worth points directly. [MANUAL: 2016-17 P2 §Appendix vs 2017-18 P2 §1.4 "Pictograph", Appendix B, Appendix G]
- **Changed — the REV Expansion Hub became legal.** "Expansion Hub" appears 0 times in the 2016-17 Part 1 and 48 times in the 2017-18 Part 1 (`<RE07>f` allows up to two). [DERIVED: grep counts on both Part 1 text layers]

---

## 3. Scoring table

Values below are read from the **§1.7 Scoring Summary table, Game Manual Part 2 p.27**, recovered by geometry (`tools/extract-tables.py`, table 1 of 2 on p.27) and cross-checked against the rendered page image and the §1.5 body text.

| Scoring achievement | AUTO | TELEOP | END GAME | Manual reference |
|---|---:|---:|---:|---|
| **Jewel** — one Jewel remains on the Platform (colour = scoring Alliance) | **30** | – | – | §1.5.2.1 |
| **Glyph** — Scored in a Cryptobox | **15** | **2** | – | §1.5.2, §1.5.3 |
| **Glyph** — bonus for first Glyph in the correct Cryptobox Key Column | **30** | – | – | §1.5.2.3 |
| **Row** — completed (a Scored Glyph in each of the 3 Columns) | – | **10 per Row** | – | §1.5.3.2 |
| **Column** — completed (4 Glyphs, one Scored in each of the 4 Rows) | – | **20 per Column** | – | §1.5.3.3 |
| **Cipher** — all 12 Glyphs in a valid arrangement | – | **30** | – | §1.5.3.4 |
| **Relic** — In Zone 1 | – | – | **10** | §1.5.4.1.a |
| **Relic** — In Zone 2 | – | – | **20** | §1.5.4.1.a |
| **Relic** — In Zone 3 | – | – | **40** | §1.5.4.1.a |
| **Relic** — Upright bonus (bottom surface is the only contact) | – | – | **+15** | §1.5.4.1.b |
| **Robot Parked** — In own Safe Zone | **10** | – | – | §1.5.2.4 |
| **Robot Balanced** — on own-colour Balancing Stone at end of Match | – | – | **20** | §1.5.4.2 |
| **Minor Penalty** (awarded to the *non*-offending Alliance) | 10 | 10 | 10 | §1.5.6 |
| **Major Penalty** (awarded to the *non*-offending Alliance) | 40 | 40 | 40 | §1.5.6 |

> **Table caveat (manual defect, not tooling).** In the printed §1.7 table, the `Robot Balanced` value `20` sits in a cell that visually straddles the *Driver-Controlled* and *End Game* columns, and the Glyph Row/Column/Cipher values straddle the same boundary. The table's own **Reference** column (`1.5.4.2`) and the §1.5.4 body text resolve `Robot Balanced` as an **End Game** achievement. Rows/Columns/Cipher are Driver-Controlled per §1.5.3. [MANUAL §1.7 vs §1.5.3/§1.5.4]

### Scoring mechanics that change the arithmetic

- **A Glyph scored in Autonomous is counted twice.** It earns 15 in Auto, and it is still a Scored Glyph at the end of the Match, so it also earns the 2-point teleop value and contributes to Rows/Columns/Cipher. Effective value **17**. [Q&A, *"Section 1.5.3 Driver-Controlled Period Scoring - Glyph previously Scored during the Autonomous Period"*: "Yes, a Glyph that is Scored in the Cryptobox during the Autonomous Period will contribute towards the Driver-Controlled Score."] [DERIVED: 15 + 2 = 17]
- **Two Cryptobox Key bonuses are available per Alliance, not one.** Each Alliance owns two Cryptoboxes; the first Glyph scored into *each* is eligible. [Q&A, *"Cryptobox Key Scoring Clarification"*: "Two Cryptobox Scoring achievements are possible for an Alliance; one opportunity for each Cryptobox."] It does not have to be the pre-loaded Glyph, and a vertical stack of two placed simultaneously earns a single 30. [Q&A, *"Cryptobox Key - Scoring a Glyph from the Glyph Pit"*]
- **Cryptobox capacity is 12.** A 13th Scored Glyph has zero value. [Q&A, *"Cryptobox Glyph capacity"*]
- **Cryptobox points are cumulative**, and the manual works the example: 12 Glyphs = 24 (2 each) + 40 (4 Rows x 10) + 60 (3 Columns x 20) = **124**; with a valid Cipher, **154**. [MANUAL §1.5.3.5]
- **Appendix D worked example (independent check):** 4 Rows x 10 = 40, 2 Columns x 20 = 40, 11 Glyphs x 2 = 22, Cipher 0 → **102**. [MANUAL Appendix D, p.35]
- **Scoring Elements touching an own-Alliance robot score zero** at the moment the Score Tracker records. [MANUAL `<G20>`]
- **The final state is what counts.** A Cipher completed mid-match and then broken before all elements come to rest earns nothing. [Q&A on `<G13>`: "The Alliance does not earn 30-points for the Cypher because it is not complete at the end of the Match."]
- **Relic Zone overlap** goes to the higher-value Zone, and "In" means breaking the Zone's infinite vertical plane — the Relic need not touch mat inside the border. [MANUAL §1.5.4.1.a, `<G23>`, Appendix H-2; Q&A *"Rule `<G23>` and Section 1.5.4"* accepted a team's correction that the sentence should read "If a Relic is **In** two (2) Zones".]
- **Parking**: any portion of a Parked robot inside the Safe Zone Area scores; wheels need not be inside. [Q&A, *"Parking in a Safe Zone - Robot drive-base Outside the Safe Zone"*]

---

## 4. Bonuses, randomization and ranking

### Randomized objectives — two of them, both revealed the same way

| | Jewel orientation | Pictograph / Cryptobox Key |
|---|---|---|
| What is randomized | Which side of the platform the red Jewel sits on (left or right, as seen from mid-field) | Which of Left / Center / Right is the Key Column |
| How chosen | **Roll of a die**, by field personnel, pre-match | **Roll of a die**, by field personnel, pre-match |
| Consistency | **All four Jewel Sets get the same orientation** | Three different Pictograph images exist |
| How revealed to the robot | Physical colour — robot must sense it on the field | Printed image on the outside wall, decoded by the phone camera via **Vuforia** |
| Placement | Platform in front of each Balancing Stone, not affixed to the field | On the Field Perimeter, **offset 3 in to the left of the centre of the Balancing Stone** as seen by a robot sitting on the Stone |
| Reward | 30 per platform left with a single Jewel of your colour | +30 on top of the 15 for the first Glyph in that Column, per Cryptobox |
| Citation | [MANUAL §1.4 "Jewel", §1.5.2.1, Appendix G] | [MANUAL §1.4 "Pictograph"/"Cryptobox Key", §1.5.2.3, Appendix B, Appendix F Fig F-6, Appendix G] |

The randomization is locked in before the match: once the **first** Jewel or Pictograph is placed, Drive Teams may not touch robots or Driver Stations. [MANUAL §1.5.1] Violating that is `<GS1>`: Minor Penalty per robot **plus that robot loses eligibility for both the Jewel and the Cryptobox Key achievements** — the partner robot keeps its eligibility. [MANUAL `<GS1>`]

### The Cipher

Six valid Ciphers exist: **three named patterns — Frog, Bird, Snake — each shown in two mirror variants**. [MANUAL Appendix E, p.36, read from the rendered figure] Each is a specific arrangement of the 12 brown and gray Glyphs; the Frog variants are a strict brown/gray checkerboard. Glyphs "do not have to be perfectly aligned horizontally but all twelve (12) Glyphs must be in the proper arrangement." [MANUAL Appendix E] The field carries 24 brown and 24 gray Glyphs. [MANUAL §1.4 "Glyph"]

A completed Cipher also unlocks **early Relic scoring**: one Relic may be scored before the End Game per completed Cipher, on a referee's signal. [MANUAL §1.5.4, `<GS14>`]

### Ownership / multipliers

There are **no ownership, control-zone, or multiplier mechanics this season.** Every achievement is a flat additive value. The only multiplicative language in the manual is on the *penalty* side (`<GS3>`, `<GS6>` "Double Major Penalty"). [MANUAL §1.5, §1.7] Cryptoboxes are Alliance-owned in the sense that only that Alliance's colour Rails score for them, and a Glyph placed by *either* Alliance into a Cryptobox scores for the Cryptobox's owner "regardless of its location or which Alliance placed it." [MANUAL §1.5.2.2]

### Ranking formula and tiebreakers — Game Manual **Part 1 §5.8**

| Element | Rule |
|---|---|
| **Qualifying Points (QP)** — primary rank | Win **2**, Tie **1**, Loss **0**, Disqualified **0** |
| **Ranking Points (RP)** — secondary rank | **The losing Alliance's PRE-PENALTY score, awarded to BOTH Alliances.** Tie → both get the lowest pre-penalized score. Disqualified team gets 0 RP. If both teams on one Alliance are disqualified, the winners get *their own* score as RP. |
| Tiebreak 1 | Total QP |
| Tiebreak 2 | Total RP |
| Tiebreak 3 | Highest single match score |
| Tiebreak 4 | Next-highest match score, repeating until broken |
| Tiebreak 5 | Random electronic draw |
| Surrogate matches | Marked with an asterisk; do not count toward standings |
| Credit without a working robot | Granted if the robot passed inspection and one Drive Team member is present in the Alliance Station |
| Score disputes | Referee Question Box, one student, within three matches of the disputed match |

[MANUAL Part 1 §5.8, all rows] The manual's own worked example Q-4 is the one to internalise: Red 15, Blue 45, Blue takes a Minor Penalty (+10 to Red = 25) — Blue still wins, and **both Alliances receive 15 RP**, the *pre-penalized* loser's score. [MANUAL Part 1 §5.8]

---

## 5. The rules that shaped play

Penalty currency: **Minor = 10 pts to the opponent, Major = 40 pts to the opponent, "Double Major" = 80.** [MANUAL §1.4 "Penalty", §1.5.6] Cards: two Yellow Cards convert to a Red; a Red Card means 0 points and a lost match; Yellows do not carry from qualification into eliminations; in eliminations cards attach to the whole Alliance. [MANUAL §1.4 "Yellow Cards and Red Cards"] Rule precedence: **Safety > Game-Specific > General**, and forum rulings override the manual. [MANUAL §1.6]

### Game-specific rules (`<GS#>`), Part 2 §1.6.3

| Rule | Threshold | Consequence tier |
|---|---|---|
| `<GS1>` Touching robot/DS after randomization begins | Any touch after the **first** Jewel or Pictograph is placed | Minor **per robot** + that robot ineligible for Jewel *and* Cryptobox Key in Auto |
| `<GS2>` Autonomous keep-out | Any entry into the opponent's half during Auto (tape line divides the field). **The Glyph Pit is open to all at any time.** | **Major** + no benefit from any scoring done in the opponent's Area |
| `<GS3>` Glyph Control/Possession limit | **2 Glyphs max.** Plowing legal; herding/directing for advantage not | Minor **per Glyph over the limit**, repeating **every 5 s per Glyph**; **Double Major (80) for each Glyph Scored while over the limit**; escalates to Yellow "quickly" |
| `<GS4>` Glyph Hoarding | Triggers **only after the Alliance has scored more than 20 Glyphs**; then the Alliance may not collectively hold/block more than it needs to fill its Cryptoboxes (12 per box) | **Major** + Minor per 5 s per excess Glyph; Yellow Cards to **all** Alliance members for intentional/repeated violation |
| `<GS5>` Relic Control/Possession limit | **1 Relic max per robot** | **Score wipe: no Relic is eligible to be Scored by *either* robot on that Alliance** — not a point penalty |
| `<GS6>` De-scoring Glyphs | Removing/re-positioning a Glyph from the **opponent's** Cryptobox. Own-Cryptobox de-scoring is explicitly legal | **Double Major (80) per Glyph** |
| `<GS7>` De-scoring Relics | Any re-positioning of a Relic In the opponent's Recovery Zone, **including accidental** — explicitly supersedes `<G28>` inadvertent/inconsequential | Opponent's Relic is awarded **maximum value (40 + 15 = 55)** |
| `<GS8>` Interfering with Cryptobox access | Opponent robot must be **In its own Safe Zone with a Glyph in Control** to be protected | **Major** + Minor per 5 s; escalates to Yellow |
| `<GS9>` Non-Glyph items in a Cryptobox | Any Jewel/Relic/etc. placed In an **opponent's** Cryptobox | **Major per item**; the owning Alliance must remove it |
| `<GS10>` Controlling/Blocking Relic access | Blocking = denying **ALL** access; requires the opponent to be attempting action | **Major** + Minor per 5 s; offender must retreat **3 ft (0.9 m)** |
| `<GS11>` Blocking Balancing Stone access | End Game only | **Warning**, then Major + Minor per 5 s; retreat **3 ft within 5 s** or it counts as a fresh violation |
| `<GS12>` Balancing Stone interference | Applies once the opponent robot is **in contact with** the Stone, End Game | **Warning**, then Major + Minor per 5 s |
| `<GS13>` Preventing Relic scoring | Protected state is defined precisely: opponent has a Relic **in Possession** *and* is **within 24 in (61 cm)** of the audience-facing wall | **Major** + Minor per 5 s; incidental Inadvertent + Inconsequential contact not penalised |
| `<GS14>` Relic Control / early scoring | May Control own Relics any time; may only **Score** in End Game, or earlier — **one Relic per completed Cipher**, on referee signal | Relics moved outside the wall before eligibility have **zero value** |
| `<GS15>` Outside contact during Relic scoring | Reaching over the audience wall and touching the floor outside is legal **only** while scoring or re-positioning a Relic | **Carve-out: exempts the robot from `<S2>` and `<G19>`.** `<S1>` still applies |
| `<GS16>` Scoring Relics | Placing/dropping only. No propelling "with any noticeable force" | Illegally launched Relics have **zero value**; missed Relics stay where they land and may be recovered |

### General rules that mattered most (Part 2 §1.6.2, §1.6.1)

| Rule | Threshold / consequence |
|---|---|
| `<G3>` Robot Starting Volume | **18 in x 18 in x 18 in**. Flag and pre-loaded Glyph may protrude. Offender is **Disabled and powered off for the match**, left in its starting location. Unlimited expansion after the start unless a `<GS#>` says otherwise |
| `<G4>` Setup alignment devices | Alignment aids must be **part of the robot and Completely Inside the 18-in cube**. Minor Penalty each offense. Humans across the field aligning the robot are banned |
| `<G17>` Pin / Trap / Block | **5-second** limit; Minor for **every 5 s** in violation |
| `<G19>` Removing Game Elements from the field | Minor **per element** — but `<GS15>` exempts Relic scoring |
| `<G20>` Scoring Elements touching own robot | **Zero value** at the moment the score is recorded |
| `<G22>` / `<G23>` | Controlled/Possessed elements are part of the robot; an object In two Scoring Areas earns **only the highest** achievement |
| `<G28>` Inadvertent + Inconsequential | Referee may decline to penalise — **except** where a game-specific rule overrides (see `<GS7>`) |
| `<S1>` Unsafe robot / field damage | Disable + optional Yellow; **re-inspection required** before the next match |
| `<S2>` Contact outside the Perimeter | **Immediate Yellow Card** + optional Disable — the single harshest general rule, and the reason `<GS15>`'s carve-out is load-bearing |

### The genuinely ambiguous rule: `<GS3>`

`<GS3>` is referenced **43 times** in the Q&A archive — nearly double the next rule (`<G27>`, 22) and triple `<G20>` (14). **Twelve separate posts** carry a `Subject: <GS3>` line, more than any other rule in the season. [DERIVED: tag-frequency and subject-line counts over `2017-18_RELICRECOVERY_Complete_QA.txt`] What the GDC had to clarify:

- **Scored Glyphs don't count.** Lifting a stack of already-Scored Glyphs inside your own Cryptobox to insert a new one is not a `<GS3>` violation. Glyphs *not* currently Scored do count if Controlled or Possessed. [Q&A, *"`<GS3>` Control/Possession Limits of Glyphs - Scored Glyphs in a Cryptobox"*]
- **Plowing vs herding.** The GDC's own worked example: driving straight through three-plus Glyphs on the way to your Balancing Stone in End Game is legal plowing; pushing them to a chosen location for advantage is herding. [Q&A, *"`<GS3>` ... Plowing versus directing multiple Glyphs"*]
- **Inconsequential pit disturbance is fine** — knocking Glyphs around, or off the pile and out of the pit, while grabbing one or two, does not violate `<GS3>`. [Q&A, *"`<GS3>` ... Inconsequential movement of Glyphs Inside the Glyph Pit"*]
- **But moving the pit toward a protected Area is not.** Intake mechanisms that consistently shove the Glyph Pit toward the Relic Recovery wall or a Cryptobox draw an escalation path: warn on `<GS3>` → penalise on `<GS3>` → warn on `<G27>` → apply `<G27>` egregious-behaviour consequences. [Q&A, *"`<GS3>` ... and `<G27>` use of Game Elements to amplify the difficulty of Scoring activities"*]
- **No warning is required.** Referees may assess the Minor Penalty immediately: "There is no requirement for Referees to issue a rule `<GS3>` warning." [Q&A, *"`<GS3>` ... When is a warning issued for violating rule `<GS3>`?"*]
- **Penalty counts per excess Glyph.** Holding 5 Glyphs = 2 allowed + **3 penalised** Glyphs, repeating every 5 s. [Q&A, *"`<GS3>` ... Penalty point application clarification"*]

**[JUDGMENT]** `<GS3>` is ambiguous because the rule regulates an *outcome* ("Control or Possess") using a definition built for *intent* ("to gain a strategic advantage"), applied to a 44-cube loose pile that any active intake necessarily disturbs. The referee is asked to infer intent from a scrum. That is the structural pattern to watch for in any future manual: **a possession limit imposed on a bulk pile of identical elements.**

---

## 6. Robot archetypes that season

**The build envelope (Game Manual Part 1 §8.3).** 18-in cube at start, expanding freely afterward (`<RG02>`, `<G3>`); **no weight limit is stated anywhere in Part 1**; max **8 DC motors** (`<RE09>`) and **12 servos** (`<RE10>`, VEX EDR 393 motors count as servos, max 2 per Servo Power Module); **one 12 V battery** (`<RE03>`); at most **two REV Expansion Hubs** (`<RE07>f`) — the REV Control Hub was *not* allowed (`<RE07>g`); Android phone as Robot Controller and a second phone as Driver Station with Logitech F310 or Xbox 360 gamepads (`<RE06>`, §1.4 "Driver Station"); 3D-printed parts legal (`<RM04>`), COTS mechanical parts limited to **a single degree of freedom** (`<RM02>`), holonomic wheels legal (`<RM03>`).

The season's central design tension: **8 motors and an 18-inch cube had to contain a drivetrain, a Glyph intake, a Glyph lift, a ~4-foot Relic extension, and a Jewel arm.** [JUDGMENT]

| Archetype | What it had to do | Build implications | Points it addresses |
|---|---|---|---|
| **Jewel arm (universal)** | Drop an arm past the wall-side of the Balancing Stone, read red-vs-blue, knock the opponent's Jewel off an unattached platform | 1 servo + 1 colour sensor. Must fold inside the 18-in cube at setup; the Q&A confirms a fallen jewel arm can be reset before the match with referee notification | 30 per platform |
| **Vuforia auto** | Decode the Pictograph from the phone camera, then deliver the pre-loaded Glyph to the named Column | Camera aim is fixed by geometry — the Pictograph sits **3 in left of the Stone's centreline** as seen from the Stone. Pure software after mounting | 15 + 30, twice per Alliance |
| **2-Glyph intake / scorer** | Collect exactly two Glyphs from a 44-cube pile, carry them, place them between Cryptobox Rails without touching them at rest | `<GS3>` makes **two** the natural carriage unit — a 1x2 or 2x1 holder that places a pair at once. Compliant-wheel or belt intakes dominate the Q&A discussion. `<G20>` means release must be clean | 2/Glyph + 10/Row + 20/Column |
| **Cipher scorer** | Everything the intake robot does, **plus** distinguish brown from gray and control placement order | Adds a colour sensor on the intake path and a way to *reject* or *re-order* Glyphs — a queue or a selectable dual path. This is the most expensive capability in the game for 30 marginal points | +30 |
| **Relic arm** | Extend roughly 4 ft horizontally over a 12-in wall, place a 10-in-tall Relic upright in Zone 3, then retract | Telescoping/cascading slides folding into 18 in, plus a gripper with wrist rotation for the upright bonus. Directly competes with the Glyph lift for the 8-motor budget. `<GS15>` legalises resting outside the field; the Q&A confirms the robot may be left extended into the Recovery Zone at the buzzer | 40 + 15, twice |
| **Balancer** | Climb a 2-in step onto a 23-in square Stone and stop Completely Supported, with no outer edge touching the floor | The drivetrain already has to *descend* the Stone at match start, so clearance and approach are constrained from the first second. A robot that never moves stays Balanced and still scores 20 [Q&A] | 20 per robot |

**Constraint worth carrying forward:** a robot unable to be Balanced at setup "is not eligible to earn points for their Alliance during the Autonomous Period however it still must start On the Balancing Stone." [MANUAL §1.5.1] The starting position was itself a scoring gate.

---

## 7. The strategic lesson

**The same physical act was worth 8.5x more in Autonomous than in Driver-Controlled, and almost nothing else in the game moved that far.**

| Comparison | Arithmetic | Label |
|---|---|---|
| One Glyph scored in Auto | 15 (Auto) + 2 (still Scored at end) = **17** | [DERIVED from §1.5.2.2 + Q&A confirmation] |
| One Glyph scored in Teleop | **2** | [MANUAL §1.5.3.1] |
| Ratio | 17 / 2 = **8.5x** | [DERIVED] |

**Where the points really were.** A "cheap" auto per robot — Jewel + one Key-Column Glyph + Park — is 30 + 15 + 30 + 10 = **85**. Two robots: **170**, plus the two Glyphs' 2 points each at the end = **174**. [DERIVED: (30+15+30+10) x 2 + (2 x 2)] A completely filled 12-Glyph Cryptobox *with* a valid Cipher is **154**. [MANUAL §1.5.3.5] **A two-robot clean Autonomous out-scored a perfect Cipher Cryptobox** — in 30 seconds, with four game elements, using a servo arm, a colour sensor and a camera, instead of two minutes of colour-selective cube handling.

**The underpriced objective: the Relic.** Zone 3 upright = 40 + 15 = **55 points for placing one object**. Two Relics = **110**, which is 89% of a full 12-Glyph Cryptobox (124) for **one-sixth the game elements** and no colour constraint. [DERIVED: 110/124 = 0.887; 2 objects vs 12] Per element: **55 pts/Relic vs 10.3 pts/Glyph** in a full Cryptobox (124/12). [DERIVED] And the Relic is the most rule-protected objective on the field — `<GS10>`, `<GS13>` and `<GS7>` all defend the scorer, with `<GS7>` awarding maximum value even when the opponent's interference is *accidental*.

**The "obvious" strategy that underperformed: chasing the Cipher.** It is the mechanic the game is named around, it is the Appendix that draws the eye, and it is worth **30 marginal points over the 124 the same 12 Glyphs already earn — 19.5% of the total for the hardest capability in the game.** [DERIVED: 30/154 = 0.195] Worse, it is *fragile*: the score is taken from the final at-rest state, so one Glyph de-scored at the buzzer erases it [Q&A on `<G13>`], and every Glyph handled toward it lives under `<GS3>`, the most-litigated rule of the season. The only structural reason to build for the Cipher is the **early-Relic unlock** in `<GS14>` — which buys time for an objective (the Relic) that a non-Cipher robot could simply have started on 30 seconds later anyway.

**Column-first beats Row-first, and the manual never says so.**

| Fill order | Glyphs | Glyph pts | Bonus | Total | Pts/Glyph |
|---|---:|---:|---:|---:|---:|
| Complete one **Column** | 4 | 8 | 20 | **28** | **7.00** |
| Complete one **Row** | 3 | 6 | 10 | **16** | **5.33** |

[DERIVED: Column = 4x2 + 20; Row = 3x2 + 10; §1.5.3.1-3] Stacking vertically pays 31% more per Glyph than spreading horizontally — and a vertical stack is also the natural output of a lift, which the Relic arm's slide hardware already resembles.

**The consequence class that dominates expected value: score wipes, not penalties.** `<GS5>` (holding two Relics) does not cost 40 points — it zeroes **every** Relic for the Alliance, up to **-110**. [DERIVED: 2 x 55] `<GS14>` zeroes a Relic scored early. `<GS16>` zeroes a launched Relic. `<G20>` zeroes anything your own robot is touching. Ranked by worst case, these outrank every Major Penalty in the manual.

---

## 8. Signals for BIOBUZZ

1. **On day one, compute the AUTO:TELEOP ratio for every action that appears in both columns.** Relic Recovery's 15:2 Glyph ratio is the single largest lever in the game, and the manual never presents the two numbers adjacent — they are in §1.5.2 and §1.5.3, and the §1.7 summary table splits them across columns without comment. If BIOBUZZ prices one action differently by period, that ratio is the strategy.
2. **Remember to re-count Auto-scored elements at the end.** Whether Auto-scored elements also earn their teleop value was left implicit and required a forum ruling. If the BIOBUZZ manual is similarly silent, submit that Q&A in week 1 — the answer moves every scoring model.
3. **A randomized objective revealed by a camera is a software problem with a hardware-sized payout.** The Pictograph was worth 30 (x2 per Alliance) for aiming a phone at a printed sheet at a fixed offset. Check the geometry note early: the target's position was specified *relative to the starting position* (3 in left of the Balancing Stone centreline), which is what made it cheap.
4. **Check the marginal value of the bonus the game is named after.** Cipher = 30 on top of 124. A signature mechanic that is only ~20% of its own subtotal, is fragile to end-state adjudication, and requires a whole extra sensing capability, is a trap. Compute *marginal* value, never headline value.
5. **Count objects, not points, when comparing objectives.** 55 points per Relic vs 10.3 points per Glyph is the number that predicts which robot wins. Rank every objective by points-per-game-element-handled before ranking by points.
6. **Enumerate every rule whose consequence is "zero score value" rather than "N points."** In 2017-18 those were `<GS5>`, `<GS14>`, `<GS16>`, `<GS2>`, `<G20>`, `<G24>` — collectively far more dangerous than the 40-point Majors, because they scale with how well you were doing.
7. **Find the carve-out rules.** `<GS15>` explicitly exempted Relic scoring from `<S2>` (immediate Yellow Card for contact outside the perimeter) and `<G19>`. When an objective lives outside the normal play space, the manual will contain exactly one rule that makes it legal — that rule defines the whole legal envelope of the mechanism.
8. **Watch for a possession limit imposed on a bulk pile.** `<GS3>` generated 43 Q&A references because it regulated an outcome using an intent-based definition against a 44-cube heap. If BIOBUZZ has a possession cap over a loose pile, expect the same litigation, design the intake to be *visibly* compliant (a fixed-capacity carriage), and read every plowing-vs-herding ruling as it lands.
9. **If RP is still the losing Alliance's pre-penalty score, defense costs you rank.** Under Part 1 §5.8, both Alliances receive the *loser's pre-penalized* score as RP. In a match you will comfortably win, suppressing the opponent's score directly suppresses your own RP, and penalties you draw from them do not raise it either (RP is pre-penalty). Verify this formula in the BIOBUZZ Part 1 equivalent before writing any defensive playbook — the sign of the incentive flips entirely depending on it.
10. **Two-part manuals hide the build constraints from the game analysis.** The 8-motor / 12-servo / 18-inch-cube ceiling is what made the Relic arm and the Glyph lift mutually exclusive for most teams, and none of that is in Part 2. Read the robot rules *before* ranking strategies by points.

---

## 9. Extraction notes

### Rule counts

| Manual | Pages | Rules found | By prefix | Tag occurrences |
|---|---:|---:|---|---:|
| **Part 2** (the game) | 42 | **47** | `S` 3, `G` 28, `GS` 16 | 95 |
| **Part 1** (game-independent) | 58 | **77** | `I` 8, `RG` 8, `RM` 7, `RE` 17, `RS` 9, `T` 28 | 167 |

Counts above are from a **patched** run (see tooling defects below). Independently verified for Part 2 by `grep -o "<[A-Z]\{1,3\}[0-9]\{1,3\}>" | sort -u | wc -l` = **47**, matching exactly.

### Violation lines

**Zero rules carry a structured `Violation:` line.** The literal string `Violation:` appears **0 times** in Part 2. This era encodes consequences two ways instead:

- **Inline prose** inside the rule body — 28 of 47 Part 2 rule bodies name an explicit consequence (Minor Penalty / Major Penalty / Yellow Card / Disabled / zero Score value).
- **The §1.8 Rule Summary table** (Part 2, pp.27-30), a matrix with `Warning/Disable | Minor Penalty | Major Penalty | Card Issued` columns. It covers **38 of the 47** rules. The 9 absent are `<G13>`, `<G18>`, `<G22>`, `<G23>`, `<G24>`, `<G25>`, `<G26>`, `<G28>`, `<GS16>` — all but `<GS16>` are definitional/adjudication rules with no penalty.

The parser reports `violations=23` for Part 2. **That number is not a violation-line count** — `parse-legacy-manual.py`'s `VIOLATION` regex matches the *words* "Violation" or "Penalty" anywhere in the first 400 characters of a body, so it is a prose keyword heuristic. Do not carry it into the harness-generalization report as comparable to a 2024-25 `Violation:` count.

### Tooling defects found (both in `tools/parse-legacy-manual.py`)

**Defect 1 — the tag regex drops every single-digit rule. Severity: high.**

```python
RULE_TAG = re.compile(r"<([A-Z]{1,3})(\d{2,3})>")   # requires TWO digits minimum
```

2017-18 numbers its rules `<S1>`, `<G1>`, `<GS1>`, `<I1>`, `<T1>` — single digit, no zero padding. Measured under-count:

| Manual | Parser as shipped | Actual | Missed | Error |
|---|---:|---:|---|---:|
| Part 2 | 26 (`G` 19, `GS` 7) | **47** | `G1`-`G9`, `GS1`-`GS9`, `S1`-`S3` | **-45%** |
| Part 1 | 60 (`RE` 17, `RG` 8, `RM` 7, `RS` 9, `T` 19) | **77** | `I1`-`I8`, `T1`-`T9` | **-22%** |

The whole `I` (inspection) prefix vanished from Part 1 — the parser reported the prefix vocabulary as `RE/RG/RM/RS/T` when it is actually `I/RE/RG/RM/RS/T`. Fix is one character: `\d{1,3}`. Note that Part 1 zero-pads its robot rules (`<RG02>`, `<RE09>`) but *not* its inspection or tournament rules (`<I1>`, `<T9>`) — the padding convention is inconsistent **within a single manual**, so `\d{1,3}` is required, not merely preferable.

**Defect 2 — `--tsv` / `--json` never write, and the output path is mis-parsed as an input PDF. Severity: medium (documented usage is broken).**

In `main()`, `pdfs` is built from `argv` *before* `take()` strips the flag values:

```python
pdfs = [a for a in argv if not a.startswith("-")]   # picks up the --tsv value too
...
tsv_out, json_out = take("--tsv"), take("--json")   # too late
```

So the exact invocation in the task brief and in the module docstring —
`python tools/parse-legacy-manual.py "<PART2.pdf>" --tsv /tmp/2017-18.tsv` —
produces `### MISSING C:/.../2017-18.tsv`, sets `rc=1`, and writes **no TSV at all**, because the guard `if tsv_out and len(pdfs) == 1` now sees `len(pdfs) == 2`. Fix: move the two `take()` calls above the `pdfs` assignment. Worked around here by importing the module and calling `parse()` directly.

### What the other tools got right

- **`tools/extract-tables.py` was necessary and correct.** The §1.7 Scoring Summary (p.27) and the §1.8 Rule Summary (pp.27-30) both came out with rows and values correctly paired. Flat `pdftotext -layout` mangles §1.8 severely — the `<G16>`/`<G17>`/`<G19>`/`<G20>`/`<G21>` block interleaves five rule labels, four consequence texts and the penalty-column marks into a scrambled 15-line paragraph with no recoverable row structure. The same failure hits the `<RE09>` motor/battery/controller compatibility matrix on Part 1 p.34, where the checkmarks and X marks float free of their rows. **Use geometry for both.**
- **Caveat on the index.** This manual contains **no `Table N-M:` captions**, so `INDEX.txt` labelled all 9 recovered tables `(no caption on page)`. The caption-matching logic is a 2024-25+ convention; for legacy manuals, identify tables by page and by the section heading above them instead.
- **`tools/render-pages.py`** was needed to resolve the §1.7 column ambiguity and to read Appendix E, whose six Ciphers exist only as images with three text labels (Frog / Bird / Snake) — the flat text gives no indication that each label covers two mirror variants.

### Manual defects (not tooling)

1. **§1.8 Rule Summary mis-numbers its last row.** It lists "Launching or Shooting Relics" as `<GS15>`. In the body text (§1.6.3) that is `<GS16>`; `<GS15>` is "Outside Contact during Relic Scoring." The summary table has no `<GS16>` row at all.
2. **§1.7 column straddle** on `Robot Balanced` and on the Row/Column/Cipher values — resolved by the table's own Reference column and the §1.5.3/§1.5.4 body text, as noted in section 3.
3. **§1.4 unit-conversion error on the Relic:** "approximately 4.72 ounces (214 gm)". 4.72 oz is ~134 g; 214 g is ~7.55 oz. The Glyph and Jewel conversions in the same section are internally consistent, so the Relic figure is the outlier and at least one of the two numbers is wrong. **UNVERIFIED** which; the official Field Setup Guide would settle it.
4. **§1.5.4.1.a wording** — "If a Relic is touching two (2) Zones" contradicts Appendix H-2's vertical-plane definition of *In*. The GDC accepted the correction on the forum: the sentence should read "If a Relic is **In** two (2) Zones."

### Q&A archive statistics

6,230 lines; ~200 answered threads across Robot Build, Game Rules, Tournament, Field Setup, Judging and Advancement. Rule-tag reference frequency (top of distribution):

| Rule | Refs | Rule | Refs | Rule | Refs |
|---|---:|---|---:|---|---:|
| `<GS3>` | **43** | `<G27>` | 22 | `<G20>` | 14 |
| `<G9>` | 13 | `<S2>` | 12 | `<G4>` | 10 |
| `<RE17>` | 9 | `<RE14>` | 9 | `<GS13>` | 9 |

By distinct `Subject:` lines: `<GS3>` **12 posts**, `<G20>` **5**, `<G3>`+`<G4>` (starting volume and pre-match alignment devices) **6**. [DERIVED: `grep -c 'Subject: <GS3>'` etc.]

`<GS3>` (2-Glyph Control/Possession limit) is the season's genuine ambiguity by a wide margin and is written up in section 5. The runner-up clusters are *adjudication-boundary* questions rather than strategy questions — `<G20>` (does a Scoring Element touching a robot count?) and `<G3>`/`<G4>` (what may extend from the robot during setup?) — and both classes recur every season, so a kickoff harness should expect them and not treat them as signal about the new game.

### Reproduction

```bash
# rules — NOTE: --tsv is broken as shipped (Defect 2); patch RULE_TAG to \d{1,3} (Defect 1)
python tools/parse-legacy-manual.py "manuals/archive/wayback/2017-18_RELICRECOVERY_GameManual_Part2.pdf"
python tools/parse-legacy-manual.py "manuals/archive/wayback/2017-18_RELICRECOVERY_GameManual_Part1.pdf"

# scoring + rule-summary tables (required — flat text is unusable for §1.8)
python tools/extract-tables.py "manuals/archive/wayback/2017-18_RELICRECOVERY_GameManual_Part2.pdf" --out <dir>

# §1.7 column check, Appendix E ciphers, Appendix F field geometry
python tools/render-pages.py "manuals/archive/wayback/2017-18_RELICRECOVERY_GameManual_Part2.pdf" --pages 27-30 --dpi 130 --out <dir>
python tools/render-pages.py "manuals/archive/wayback/2017-18_RELICRECOVERY_GameManual_Part2.pdf" --pages 36-37 --dpi 110 --out <dir>
```
