# FTC Season Dossiers — Cross-Season Index, 2017-18 → 2025-26

**Purpose.** Nine seasons of FTC games, read end to end, so that on **2026-09-12** the BIOBUZZ kickoff
analysis starts from what recurs instead of from scratch. Section 4 is the engineering finding: how much of
the 2026-27 analysis harness actually generalises backwards, measured rather than assumed.

**How to read the citations.** Seasons 2017-18 → 2023-24 are cited by dossier filename in this directory.
Seasons 2024-25 and 2025-26 are cited to `../ITD/` and `../kickoff/`, which are **beta-test outputs of the
2026-27 harness run backwards against a known season**, not dossiers in the same shape — see §5.

Every number in this file is either quoted from a dossier or re-measured in this session against the PDFs
and text dumps in `manuals/archive/`. Measurements taken here are marked **[measured]**.

---

## 1. The index

| Season | Game | Scoring element(s) | The core loop, in a few words | Endgame mechanic | Dossier |
|---|---|---|---|---|---|
| **2017-18** | RELIC RECOVERY | **Glyphs** (6 in foam cubes); Jewels; Relics | Two Glyphs at a time out of a 44-cube pit into a wall-mounted 3-wide × 4-tall Cryptobox; Rows / Columns / Cipher pay cumulative bonuses | Reach *over* the audience wall to place Relics on the outside mat (10 / 20 / 40 by Zone, **+15 upright**), then climb back onto your own Balancing Stone (20) | [`2017-18_RELIC-RECOVERY.md`](2017-18_RELIC-RECOVERY.md) |
| **2018-19** | ROVER RUCKUS | **Minerals** — 90 Gold cubes, 60 Silver balls; Team Marker | Harvest Minerals out of a Crater and either sort them into the *matching* Cargo Hold on the central Lander (5) or dump either type in the Depot (2) | Exactly **one** of: Latch back onto the Lander (**50**) / In a Crater (15) / Completely In a Crater (25) — mutually exclusive via `<G24>` | [`2018-19_ROVER-RUCKUS.md`](2018-19_ROVER-RUCKUS.md) |
| **2019-20** | SKYSTONE | **Stones** (56) + 4 **Skystones**; Foundation; team-built Capstone | Carry **one** Stone, with the robot itself passing under its own **14 in** Skybridge, into the Building Zone and Interlock it onto the Foundation | Drop a Capstone on the tower (5 + 1/Level), drag the Foundation **Completely Out** of the Building Site (15), Park (5 each) | [`2019-20_SKYSTONE.md`](2019-20_SKYSTONE.md) |
| **2020-21** | ULTIMATE GOAL | 20 **Rings**; 4 **Wobble Goals** | Launch Rings **from inside the Launch Zone** into the Low / Mid / High Tower Goals (2/4/6 teleop), or knock over three 1-inch Power Shot targets | Wobble Goal over the front wall into the Drop Zone (**20**) or onto the Start Line (5); Power Shots reset and re-score (15 each); Rings stacked on a Wobble Goal (5) | [`2020-21_ULTIMATE-GOAL.md`](2020-21_ULTIMATE-GOAL.md) |
| **2021-22** | FREIGHT FRENZY | **Freight** — Boxes, Cargo, Ducks; Team Shipping Element | **One** piece of Freight at a time, with full-body entry into a Warehouse, onto the 3-level Alliance Shipping Hub (2/4/6) or the contested Shared Hub (4) | Spin the Carousel to Deliver Ducks (6 each, 9 available), Cap with the TSE (15 × 2), tip the Shared Hub your way (**20**), keep your own Hub Balanced (10), Park (3/6) | [`2021-22_FREIGHT-FRENZY.md`](2021-22_FREIGHT-FRENZY.md) |
| **2022-23** | POWER PLAY | 60 **Cones**; team-built **Beacons** | Cone from your Substation onto one of 25 Junctions — 2/3/4/5 by height — where the **top** Cone owns the Junction | Everything is scored at rest: Junction Ownership (3 each), Beacon Cap (10, permanent), and a **Circuit** linking your two diagonally-opposite Terminals (**20**); Terminal park (2) | [`2022-23_POWER-PLAY.md`](2022-23_POWER-PLAY.md) |
| **2023-24** | CENTERSTAGE | **Pixels** (hex); paper **Drone**; Team Prop | Two Pixels at a time on a full cross-field diagonal, under a ~14 in Stage Door, onto the inclined Backdrop (3) or flat In the Backstage (1); Mosaic and Set Line bonuses stack on top | **Suspend** from the Rigging (20) or Park In the Backstage (5), plus one paper Drone launched over the Truss into Landing Zone 1/2/3 (**30** / 20 / 10) | [`2023-24_CENTERSTAGE.md`](2023-24_CENTERSTAGE.md) |
| **2024-25** | INTO THE DEEP | **SAMPLES** and **SPECIMENS** (a SAMPLE + a CLIP) | **One element per trip** out of the SUBMERSIBLE: SAMPLE → NET ZONE (2) or BASKET (4/8); or clip a SAMPLE into a SPECIMEN → CHAMBER (6/10) | **No named ENDGAME.** In the last 30 s, ASCENT on your own RUNGS: LEVEL 1 = 3, **LEVEL 2 = 15**, LEVEL 3 = 30 | [`../ITD/R3-scoring-model.md`](../ITD/R3-scoring-model.md), [`../ITD/STATUS.md`](../ITD/STATUS.md) |
| **2025-26** | DECODE | **ARTIFACTS** — 24 purple, 12 green | Collect ARTIFACTS, **LAUNCH** from inside a LAUNCH ZONE through the SQUARE into the GOAL; they queue on a 9-index RAMP as CLASSIFIED (3) and pay again if the colour order matches the randomised **MOTIF** (PATTERN, 2/index) | **No named ENDGAME.** Return to BASE at the end of TELEOP: partially 5, fully 10, **+10 alliance bonus for both robots**; the 38 in height exception opens only in the final 20 s | [`../kickoff/R3-scoring-model.md`](../kickoff/R3-scoring-model.md), [`../kickoff/STATUS.md`](../kickoff/STATUS.md) |

---

## 2. What changed over nine seasons

### 2.1 Match structure and period naming

**The clock has not moved in nine years.** 30-second autonomous period + 2:00 driver-controlled = **2:30**,
every season, 2017-18 through 2025-26. The only structural drift is the transition and the vocabulary.

| | 2017-18 | 2018-19 | 2019-20 | 2020-21 | 2021-22 | 2022-23 | 2023-24 | 2024-25 | 2025-26 |
|---|---|---|---|---|---|---|---|---|---|
| Auto | 0:30 | 0:30 | 0:30 | 0:30 | 0:30 | 0:30 | 0:30 | 0:30 | 0:30 |
| Transition | 5 s | 5 s + countdown | 0:05 + countdown | ~0:05 + countdown | **0:08** | 0:08 | 0:08 | 8 s | 8 s |
| Teleop | 2:00 | 2:00 | 2:00 | 2:00 | 2:00 | 2:00 | 2:00 | 2:00 | 2:00 |
| Named final window | End Game 0:30 | End Game 0:30 | End Game 0:30 | End Game 0:30 | End Game 0:30 | End Game 0:30 | End Game 0:30 | **none** | **none** |

**The End Game was abolished in 2024-25.** [measured] The string `end ?game` (case-insensitive) occurs
**19 / 15 / 14 / 22 / 11 / 14 / 13** times in the seven legacy Part 2 manuals and **0** times in
`2024-25_INTO_THE_DEEP_Competition_Manual_V14.txt`, `2025-26_DECODE_Competition_Manual_TU32.txt` **and**
`2026-27_BIOBUZZ_Competition_Manual_V0.txt`. It survives only as a *protection window* defined by a rule:
the last 30 seconds in 2024-25 (**G427**, ASCENT ZONE protection) and the final **20** seconds in 2025-26
(**G415.A**, **G427**), each with its own audio cue. Plan against a de-facto endgame; never cite one.

Naming also changed: "Autonomous Period" / "Driver-Controlled Period" (legacy, Title Case) became
**AUTO** / **TELEOP** (2024-25+, ALL CAPS). 2021-22's manual states the match length two different ways in
the same revision — §4.4 says 2:38 wall clock, §4.5 says 2:30 of scored play
([`2021-22_FREIGHT-FRENZY.md`](2021-22_FREIGHT-FRENZY.md) §2, §9 defect 7).

### 2.2 Point inflation — the numbers went *down*, not up

The headline story is **deflation of per-element value and compression of the penalty scale**.

| Season | Per-element headline (best repeatable) | Biggest single achievement | Minor / Major penalty |
|---|---|---|---|
| 2017-18 | Glyph **15** in auto, 2 in teleop | Relic Zone 3 upright **55** | **10 / 40** |
| 2018-19 | Mineral sorted into Cargo Hold **5** | Latching **50** | **10 / 40** |
| 2019-20 | Skystone delivery **10** (first two only) | Foundation Moved 15 | **5 / 20** |
| 2020-21 | High Goal Ring **12** auto / 6 teleop | Wobble Goal in Drop Zone 20; Power Shot 15 | 10 / **30** |
| 2021-22 | Level-3 Freight **6** | Shared Hub Unbalanced 20; TSE Auto Bonus 20 | 10 / 30 |
| 2022-23 | High Junction Cone **5** | Circuit 20; Signal Sleeve 20 | 10 / 30 |
| 2023-24 | Backdrop Pixel **5** auto / 3 teleop | Drone into LZ1 **30**; Suspend 20 | 10 / 30 |
| 2024-25 | HIGH CHAMBER SPECIMEN **10**; HIGH BASKET 8 | ASCENT LEVEL 3 **30** | **5 / 15** |
| 2025-26 | CLASSIFIED ARTIFACT **3** (+2 PATTERN) | BASE 10 (+10 alliance bonus) | **5 / 15** |

Two clean lines fall out:

- **A Major Penalty has fallen from 40 points to 15** — 40 (2017-18, 2018-19) → 20 (2019-20) → 30
  (2020-21 → 2023-24) → 15 (2024-25, 2025-26). Priced in the season's own currency, that is 8 sorted
  Minerals in 2018-19 vs 5 CLASSIFIED ARTIFACTS in 2025-26, so the *relative* cost has fallen less than
  the absolute number, but the direction is unambiguous.
- **The rulebook grew as the point values shrank.** Part 2 rule counts are flat across the legacy era —
  **47 / 44 / 45 / 46 / 44 / 47 / 47** [measured, patched parser, §4.1] — but the whole-season totals climb:
  124 (2017-18, 47 + 77) → 145 (2023-24, 47 + 98) → **209** (2024-25, single manual) → **214** (2025-26).
  Pages: 100 → 133 → 146 → 188.

### 2.3 The AUTO reward mechanism — four distinct generations

This is the trend with the most strategic consequence, and it inverts entirely across the nine years.

1. **Generation 1 — a raw price differential (2017-18).** The identical physical act was worth **15** in
   auto and **2** in teleop, an **8.5×** ratio once the auto Glyph's re-count is included (15 + 2 = 17).
   Nothing else in the game moved that far ([`2017-18_RELIC-RECOVERY.md`](2017-18_RELIC-RECOVERY.md) §7).
2. **Generation 2 — an auto-only achievement list (2018-19).** Landing 30, Sampling 25, Claiming 15,
   Parking 10, none of which exist in teleop at all: a **160-point auto robot ceiling** per alliance with no
   teleop analogue ([`2018-19_ROVER-RUCKUS.md`](2018-19_ROVER-RUCKUS.md) §3).
3. **Generation 3 — a shrinking differential plus a randomised-task bonus (2019-20 → 2023-24).** The
   multiplier decays every year: Skystone 10 vs 2 but only for the *first two* deliveries (2019-20); Rings
   3/6/12 vs 2/4/6, a flat **2×** (2020-21); Freight worth **6 regardless of level** in auto against 2/4/6
   in teleop (2021-22); placement values **identical** in both periods (2022-23); Backdrop 5 vs 3 (2023-24).
   As the differential shrank, the *randomised task* took over as the auto payload — and for three
   consecutive seasons FIRST let the team supply its own detection target and **doubled** the award for it:
   TSE 20 vs Duck 10 (2021-22), Signal Sleeve 20 vs field Signal 10 (2022-23), Team Prop 20 vs white Pixel
   10 on **two** tasks (2023-24). That lever then disappeared.
4. **Generation 4 — no price differential at all (2024-25, 2025-26).** Table 10-3 in INTO THE DEEP carries
   **identical AUTO and TELEOP values** on every row (2/4/8, 6/10, PARK 3); DECODE's Table 10-2 likewise
   (CLASSIFIED 3/3, OVERFLOW 1/1, PATTERN 2/2). AUTO's premium is now entirely indirect: (a) elements or
   assessments **counted twice**, and (b) **the ranking tiebreaker**. DECODE's R3 model puts a single
   MOTIF-matching auto shot at **3 + 2 + 2 = 7 points from one trigger pull** and rates it the best
   points-per-second action in the game.

### 2.4 Randomization mechanics

| Season | What is randomised | Configs | How revealed | Value at stake |
|---|---|---|---|---|
| 2017-18 | **Two** things: which side the red Jewel sits on, **and** which Cryptobox Column is the Key | 2 × 3 | Die roll; the Jewel is physical colour, the Pictograph is a printed image decoded by **Vuforia** — the first camera read worth points directly | 30 per Jewel platform; +30 per Cryptobox |
| 2018-19 | Which of 3 positions holds the single Gold in a 2-Silver + 1-Gold group | 3 | **Physical only.** No beacon, no signal, no coded marker; same grouping in front of every robot | 25 per Sample Field; blind-guess EV ≈ 8.33 |
| 2019-20 | Position of the 2 Skystones in a 6-Stone Quarry | 3 | Die roll (1/4→A, 2/5→B, 3/6→C). **The mapping exists nowhere in the text layer** — only in the Appendix D figure on p.37 | 10 per Skystone; the two are always 3 apart, so one detection unlocks both |
| 2020-21 | Which Target Zone (A/B/C) the Wobble Goal must reach | 3 | The **Starter Stack** in front of the robot is set to 0 / 1 / 4 Rings — the indicator is *also* a Ring supply, and the farthest zone carries the biggest bounty | 15 per robot |
| 2021-22 | Which of 3 Barcode squares holds the marker | 3 | Dice (1/4→L1, 2/5→L2, 3/6→L3), image-only Appendix D. Marker is a Duck (10) **or your own TSE (20)** — team's choice | 10 or **20** per robot |
| 2022-23 | Which of 3 images faces you on the Signal cone (120° apart) | 3 | Scoring system or die throw; **global** — all four robots see the same image; revealed pre-match, never re-rolled | 10 field image / **20** Signal Sleeve |
| 2023-24 | Which Spike Mark (left / center / right) | 3 | Scoring System selects; field personnel physically move the object. White Pixel (10) or **Team Prop (20)**, on **two** tasks | up to 40 per robot |
| **2024-25** | **Nothing.** | — | [measured] `randomiz` appears **once** in `..._V14.txt`, and it refers to the *match-scheduling* "brute force randomizer". The first season in nine with **no randomised field objective** | 0 |
| 2025-26 | Which of 3 **MOTIFs** (GPP / PGP / PPG) the RAMP must be filled to match | 3 | An **OBELISK** carrying an **AprilTag** (21 / 22 / 23) — the first machine-readable randomiser since 2017-18's Pictograph, and the first that specifies a **firing sequence** rather than a location | PATTERN 2/index, 9 indices, assessed twice → up to 36, plus the PATTERN RP |

**The invariant nobody should forget.** Every season 2017-18 → 2023-24 carries the *same* lock-out rule
under a different number: touch your robot or Driver Station once randomization has begun and you take a
Minor **and that robot alone** forfeits the randomization award, with the partner robot unaffected.
`<GS1>` (2017-18, 2018-19), `<GS12>` (2019-20), `<GS5>` (2020-21), `<GS11>` (2021-22), `<GS2>` (2022-23),
`<GS02>` (2023-24). **Seven seasons, six rule numbers, one rule** — and it is what converts a three-way
dice roll into a mandatory on-robot vision project, because you may not pick an opmode after seeing the
answer ([`2019-20_SKYSTONE.md`](2019-20_SKYSTONE.md) §4).

### 2.5 Endgame value

| Season | What the last 30 s was worth per alliance | Against what |
|---|---|---|
| 2017-18 | **150** — 2 × (Relic 40+15) + 2 × Balance 20 | A full 12-Glyph Cryptobox with a valid Cipher = 154 |
| 2018-19 | **100** — 2 × Latch 50, mutually exclusive with parking | 20 sorted Minerals |
| 2019-20 | **35** for the whole Foundation package (10 auto + 15 + 2 × 5) | A 6-level capped Skyscraper (5N+5 = 35) — exact break-even |
| 2020-21 | **70** Ring-free Wobble Goal programme (2 × 15 auto + 2 × 20) | An entire disciplined teleop High Goal run |
| 2021-22 | **126** ceiling (54 Ducks + 30 Capping + 20 + 10 + 12 park) | A flawless 90 s teleop run at 6 s/cycle = **90**. The endgame beat perfect teleop by **40 %** |
| 2022-23 | State-scored: 3/Junction + 10/Beacon + 20 Circuit, all resolved at rest | A 20-Junction spread plan (136) beat stacking one High Junction 20 times (103) |
| 2023-24 | **50 per robot** (Suspend 20 + Drone LZ1 30) | **8.3** perfect two-Pixel teleop cycles (50 ÷ 6) |
| 2024-25 | **30 per robot** (ASCENT L3), or 15 for L2 at 20 in off the floor | L2 is named the best points-per-effort row in the game: one motor, one hook, no sensor |
| 2025-26 | **30 per alliance** (10 + 10 + 10 bonus) | The smallest endgame in nine years — and it is a *drivetrain* task with no mechanism at all |

**Trend:** the endgame drifted from a bespoke mechanism (a 4-ft Relic arm, a 42-lb latch winch, a paper
drone launcher) to, in 2025-26, driving back into an 18 in × 18 in square. What did **not** change is that
in seven of nine seasons the endgame was underpriced relative to its build cost, and that both ranking
tiebreakers pointed at it.

### 2.6 Ranking-system era — six regimes in nine seasons

| Era | Seasons | Primary rank | Tiebreakers | Aggregation |
|---|---|---|---|---|
| **I** | 2017-18, 2018-19 | QP/RP: Win 2 · Tie 1 · Loss 0 | **TBP = the *losing* alliance's *pre-penalty* score, awarded to BOTH alliances** → highest match score → next-highest → random | **Totals** |
| **II** | 2019-20 | same | same TBP formula | **Averages**, with a drop rule: drop the 1 lowest TBP match at 5-6 matches, the **2 lowest** at 7+ |
| **III** | 2020-21, 2021-22 | **RP = your alliance's own raw final score** | TBP1 = auto score · TBP2 = end-game task score → random | Totals |
| **IV** | 2022-23, 2023-24 | back to Win 2 · Tie 1 · Loss 0 | Avg TBP1 (auto) → Avg TBP2 (endgame) → **Highest Match Score incl. Penalties** (a 5th sort that did not exist before) → random | **Averages** |
| **V** | 2024-25 | RS = average RP; Win 2 · Tie 1 only | Avg ALLIANCE **AUTO** points → Avg TELEOP **ASCENT** points → highest match score → random | Averages |
| **VI** | 2025-26 | RS = average RP; **Win 3** · Tie 1 **plus three threshold RPs** (MOVEMENT, GOAL, PATTERN, 1 each; max **6** in a match) | Avg match points **excluding FOULS** → Avg **BASE** points → Avg **AUTO** points → random | Averages |

Three things a strategy memo must re-derive every year, because the sign flips:

- **Era I/II:** TBP is the *loser's* score handed to both sides, so **playing defence lowers your own
  tiebreaker** and running up the score adds nothing.
- **Era III:** RP is your own raw score, so suppressing the opponent contributes **exactly zero** to your
  rank while costing you cycle time. Both the 2020-21 and 2021-22 dossiers conclude defence is strictly
  negative-EV in qualification.
- **Era VI:** 2025-26 is the first season in the set where you can earn ranking credit **without winning** —
  and where the three bonus RPs are not equally priced. MOVEMENT RP needs 16 points of the two cheapest
  achievements (a drivetrain and nothing else); GOAL RP needs **36 ARTIFACTS through the SQUARE**, the
  entire field's supply.

The through-line worth carrying into BIOBUZZ: for **seven of nine seasons** the tiebreakers measured the
two 30-second windows, never the two-minute one.

### 2.7 Penalty vocabulary

[measured] Occurrences of each term in the game manual:

| Manual | `Minor Penalty` \| `Major Penalty` | `MINOR FOUL` \| `MAJOR FOUL` |
|---|---:|---:|
| 2017-18 Part 2 | **69** | 0 |
| 2018-19 Part 2 | **70** | 0 |
| 2019-20 Part 2 | **77** | 0 |
| 2020-21 Part 2 (Trad) | **86** | 0 |
| 2021-22 Part 2 (Trad) | **115** | 0 |
| 2022-23 Part 2 (Trad) | **106** | 0 |
| 2023-24 Part 2 (Trad) | **117** | 0 |
| 2024-25 Competition Manual V14 | **0** | **67** |
| 2025-26 Competition Manual TU32 | **0** | **93** |

A clean, total substitution at the 2024-25 boundary. Three further shifts:

- **Semantics.** Legacy: "a Minor Penalty will be assessed". Modern: a MINOR FOUL is *"a credit of 5 points
  towards the opponent's MATCH point total"* — the penalty never appears in your own score, which the
  2024-25 model flags as easy for a drive team to under-weight.
- **Direction flipped three times.** Added to the non-offending alliance (2017-18 → 2019-20) → **subtracted
  from the offender** (2020-21, 2021-22) → added back to the non-offender (2022-23, 2023-24) → credited to
  the opponent (2024-25 →). The 2022-23 dossier names the consequence: in an *additive* season your
  opponents' fouls inflate **your** final score, so OPR/EPA built on final scores attributes their
  discipline problems to your robot. Prefer penalty-free scores for scouting, and confirm the direction first.
- **Extinct vocabulary.** "**Double Major**" — 80 points in 2017-18 (`<GS3>` scoring over the possession
  limit, `<GS6>` de-scoring an opponent's Cryptobox), 40 points in 2019-20 (`<GS3>`). Gone after 2019-20.
  Surviving unchanged across all nine seasons: Warning, Yellow Card, Red Card (a second Yellow auto-converts),
  Disqualified.

### 2.8 The 2024-25 consolidation of Part 1 + Part 2 into one Competition Manual

Through 2023-24 a season shipped **at least two** documents:

- **Game Manual Part 1** — game-independent: robot construction, inspection, tournament, awards.
  73-98 rules, prefixes `I`, `T`, `C`, `RE`, `RG`, `RM`, `RS`, `TE`, `DS`, `DR`, `SS`, `TM`.
- **Game Manual Part 2** — the game. 44-47 rules [measured], prefixes `S`, `G`, `GS`.

…and from **2020-21 through 2023-24** each of those forked into **Traditional** and **Remote** editions, so
a season could carry **four** manuals. The Remote editions were not cosmetic: 2020-21 Remote *omits six
rules*, every one that presupposes an opponent on the field, and 2022-23 Remote replaces the discovered
Circuit with a **predefined** path published per match in Appendix H.

2024-25 collapsed all of it into a single **Competition Manual** — 146 pp / 209 rules / 16 sections; 2025-26
is 188 pp / 214 rules. The corpus shows six concrete consequences, all of which the harness depends on:

| | Legacy (2017-18 → 2023-24) | Consolidated (2024-25 →) |
|---|---|---|
| Rule ID form | `<G14>`, `<GS05>`, `<S01>` — angle-bracket delimited, prefix inconsistently zero-padded *within one manual* | `G410`, `R503`, `T705`, `C501` — bare, one namespace `[IEAGRTLC]\d{3}`, always 3 digits |
| Rule namespace | split across two documents | single |
| Game-specific marking | a `<GS>` prefix | an **orange headline colour** (`#ED7D31`) vs evergreen green (`#06844B`) |
| Defined terms | **Title Case** — "Scoring Element" appears 23 / 27 / 37 / 31 / 43 / 54 / 42 times across the seven Part 2s [measured] | **ALL CAPS** — ROBOT 602, MATCH 377, ALLIANCE 247 in ITD V14 [measured] |
| Per-section version stamps | **0** in every legacy manual [measured] | **132** in ITD V14; a changed section announces itself |
| PDF outline (TOC) | **0 entries** in all seven legacy Part 2 PDFs [measured] | 130 (ITD) / 157 (DECODE) / 88 (BIOBUZZ V0) |
| Numbered table captions | **0** `Table N-M` strings in all seven [measured] | 51 / 68 / 30 |

The 2026-27 pre-season release confirms the consolidated shape continues: `BIOBUZZ_Competition_Manual_V0`
is **93 pp, 16 sections, 109 rules, 0 G-rules**, ALL-CAPS defined terms, per-section version stamps and a
full outline.

---

## 3. The recurring lessons

Each is anchored to at least two seasons that demonstrate it. These are the patterns most likely to repeat
in BIOBUZZ.

**1. Read the ranking formula before you read the scoring table.**
2020-21 and 2021-22 both rank on your alliance's own raw score, which makes defence worthless and turns the
season into a solo throughput problem. 2017-18, 2018-19 and 2019-20 all award **the loser's pre-penalty
score to both alliances**, which makes defence actively lower your own tiebreaker. Same game shape, opposite
incentive, and the difference lives in a document most teams never open.

**2. Both tiebreakers usually point at the two 30-second windows.**
2020-21 → 2023-24: TBP1 = auto score, TBP2 = endgame task score. 2024-25: sorts 2 and 3 are avg AUTO and
avg TELEOP ASCENT. 2025-26: sorts 3 and 4 are avg BASE and avg AUTO. As the CENTERSTAGE dossier puts it, a
team that maxes auto and endgame and does nothing else outranks a teleop cycling machine at equal RP.

**3. Find the objective that consumes zero scoring elements.**
2020-21's Wobble Goal programme is **70 points per alliance with no Rings at all**. 2019-20's Foundation
shuffle is **35 points without ever delivering a Stone**. 2022-23's Signal Sleeve is 20 points per alliance
for a printed sheet of paper. 2025-26's MOVEMENT RP needs a drivetrain and nothing else. There is usually
exactly one of these and it is usually mispriced.

**4. Compute *marginal* value, never headline value.**
2017-18's Cipher — the mechanic the game is named around — pays **30 on top of the 124 the same 12 Glyphs
already earn**, 19.5 % of its own subtotal, for the hardest capability in the game. 2022-23: a cone on a
bare Ground Junction (2 + 3 Ownership = 5) is worth **exactly as much** as a cone stacked on your own High
Junction (5), and a bare Low Junction (6) is worth more. 2024-25: the HIGH BASKET pays 8 at 43 in while the
HIGH CHAMBER pays 10 at 26 in — the price ladder is literally inverted.

**5. Rank objectives by points per game element handled, not by points.**
2017-18: 55 points per Relic vs 10.3 per Glyph in a full Cryptobox. 2020-21: Power Shots return **15.0
points per Ring** vs the High Goal's 6.0 in teleop — a 36-point swing off six Rings. 2021-22: nine endgame
Ducks at 6 each is 54 points from one wheel pressed against a plastic rim.

**6. Every single season has a possession limit, and it is always the most-litigated rule.**
`<GS3>` 2 Glyphs (**43 Q&A references, 12 subject lines — nearly triple the next rule**); `<GS3>` 2 Minerals
(21); `<GS3>` 1 Stone (22 mentions / 9 threads, the season's top); `<GS6>` 3 Rings (16, the season's top);
`<GS8>` 1 Freight; `<GS6>` 1 Cone + 1 Beacon; `<GS05>` 2 Pixels (**22 threads, the season's top**);
**G410** 1 SAMPLE or 1 SPECIMEN; **G408** 3 ARTIFACTS. **Nine seasons, nine possession limits.** The failure
mode is identical every time: an *intent-based* definition ("to gain a strategic advantage", plowing vs
herding) applied to a dense pile that any working intake necessarily disturbs, refereed in real time. Build
a fixed-capacity carriage that is **visibly** compliant, and expect regional enforcement variance.

**7. Enumerate the rules whose consequence is "zero score value", not "N points".**
2017-18's `<GS5>` does not cost 40 for holding two Relics — it **zeroes every Relic for the alliance, up to
−110**; `<GS14>`, `<GS16>`, `<GS2>` and `<G20>` do the same class of thing. 2018-19's `<GS7>` costs nothing
in points and simply makes the 50-point Latch ineligible. 2024-25 hides one in the scoring criteria: a
neutral SAMPLE **with a CLIP attached** dropped in your own HIGH BASKET scores 0 instead of 8. These scale
with how well you were doing, which is why they outrank every Major Penalty in the manual.

**8. The load-bearing field geometry lives in figures, not text.**
2019-20's Appendix D — the entire dice-roll → Skystone-pattern mapping — exists **nowhere in the text
layer**. 2020-21's Appendices B-F are figure-only with no text layer at all. 2021-22's Appendix D is
image-only. 2023-24: *"a text-only pipeline recovers zero field geometry for this season."* And in 2025-26
the analyst had to measure the field off PNGs by eye and called it *"the least reliable step in the whole
analysis, and it feeds everything."* Render the appendix pages on day one; it is a five-minute job.

**9. The manual's own revision history is a free list of the season's exploits.**
2018-19 Rev 1.2 (10/3/2018) added `<GS10>` and `<GS11>` — and a Q&A thread dated **the same day** shows a
team assembling exactly the Crater-camping combination those two rules killed. 2020-21 Rev 1.1 added
`<GS13>` and Rev 1.2 added "**Completely** In the Launch Zone". 2021-22 Rev 1.2 capped Capping at two TSEs.
2023-24 Rev 1.2 added `<GS03>`c and `<GS11>`h. Diff the revision table at kickoff; it is a dated, official
confession of which strategy the GDC does not want.

**10. Forum rulings outrank the manual and reshape the meta in weeks 4-10.**
2022-23's Q&A closed two live loopholes (`<G29>` on the upside-down-cone blocker, `<G25>` on V-shaped pole
guides) and **opened** the substation-camp meta by blessing it — the dossier's verdict is that *"any strategy
memo written from the V0 manual alone has a shelf life of about six weeks."* 2017-18's single largest lever,
the 8.5× auto Glyph, existed only as a Q&A answer. 2018-19's `<G24>` End Game exclusivity — Latch 50 and
Crater 15 do **not** stack to 65 — took a December ruling to establish, after teams had built around a
number that never existed.

**11. Look for the achievement that is paid twice, and ask about it on day one.**
2017-18: an auto Glyph earns 15, then earns its 2-point teleop value again (Q&A-only). 2020-21: Power Shots
are priced 15 in auto and **15 again in the endgame** off the same hardware — build cost paid once,
collected twice. 2022-23: auto cones are re-counted in the final field state. 2023-24: *"Pixels Scored in
the Autonomous Period will earn additional points at the end of the Driver-Controlled Period."* And **both**
modern seasons flag the re-count as the single most consequential open question in the whole analysis:
2024-25 says it moves the ceiling **266 → 306** and AUTO's value from 13 points to 26; 2025-26 says it moves
AUTO's share of a realistic winning score from **41 % to 27 %**. File that Q&A the minute the forum opens.

**12. The build envelope is where the strategy actually dies.**
**8 DC motors and 12 servos** held from 2017-18 straight through 2023-24, with a holonomic drivetrain
consuming 4 of the 8. 2017-18: an 18-in cube and 8 motors had to contain a drivetrain, a Glyph intake, a
Glyph lift, a ~4-ft Relic extension **and** a Jewel arm — mutually exclusive for most teams. 2020-21: 4
drive + 2 flywheel leaves **two** motors for intake, transfer *and* the wobble arm that pays 70 Ring-free
points. 2021-22: *"every archetype is really a claim about how to spend those four."* Read the robot rules
before ranking strategies by points. Note also that the envelope **does** change: 2018-19 introduced a 42-lb
weight cap in the exact season robots had to hoist themselves off a bracket.

**13. The binding dimension is usually a dynamic clearance, not the starting cube.**
2019-20: the Alliance Skybridge is **14 in** and `<G26>` allows ±1.0 in tolerance, so worst-case usable
clearance is **13.0 in** — and every Delivery point in both periods required the whole robot to fit through
it. The 18-in cube never bound. 2023-24: the Stage Door's lowest pipe at ~14 in decides whether you cross
the field on the short diagonal. 2025-26: **R105.B** caps the robot at 18 in for 130 of the 150 seconds of
play against a GOAL lip at 38.75 in. Ask on day one: is there a gate, tunnel, bar or door every scoring
path must pass?

**14. Penalty income is an under-modelled offensive strategy — but re-derive the sign every year.**
2019-20: Major = 20 with five separate rules charging Major-plus-Minor-every-5-s made the protected zones
worth more per second than the scoring zones. 2018-19: a sustained Lander block ran 70+ points. But the
modern manuals reversed it: 2024-25's **G412** costs you 15 to deny the opponent 8 (never profitable), and
2025-26's **G427** makes a single BASE-defence contact cost **15 + up to 20 handed over + the opponent's
MOVEMENT RP**. The one asymmetry that survived is 2023-24's `<GS03>`: one Major (30) against 45+ points of
denied auto, which the GDC was asked about in Q353 and **declined to fix**, noting only that egregious-
behaviour cards, not the score sheet, are what deter it.

---

## 4. HARNESS GENERALIZATION REPORT

The honest engineering finding, re-measured this session rather than quoted.

### 4.1 The two parsers, measured

**`reference/ftc_parse.py` returns `rules=0` on every manual 2017-18 → 2023-24.** Re-run in this session:

```
### 2017-18_RELICRECOVERY_GameManual_Part2:  42pp rules=0   ... unpaired=0  orange-box lines=0  penalty lines=0
### 2023-24_CENTERSTAGE_GameManual_Part2:    57pp rules=0   ... unpaired=0  orange-box lines=0  penalty lines=0
### 2024-25_INTO_THE_DEEP_Competition_Manual_V14: 146pp rules=209 evergreen=193 game-specific=16 unpaired=0
```

**The dangerous part is `unpaired=0`.** That field is the parser's own self-check, and it reads 0 both when
the parser understood 209 rules perfectly and when it understood nothing at all. The failure is not an
error — it is silence that looks like success. Only `RUN-KICKOFF.sh` catches it, because it independently
tests `NRULES == 0` and exits 4 with the right diagnosis ("the layout was not recognised").

**`tools/parse-legacy-manual.py` was written to cover that era.** Measured this session, as shipped, on the
seven Part 2 manuals:

| Season | As shipped (`\d{2,3}`) | Patched (`\d{1,3}`) | Missed | Error |
|---|---:|---:|---|---:|
| 2017-18 RELIC RECOVERY | 26 (G:19 GS:7) | **47** (G:28 GS:16 S:3) | `<G1>`-`<G9>`, `<GS1>`-`<GS9>`, `<S1>`-`<S3>` | −45 % |
| 2018-19 ROVER RUCKUS | 23 (G:21 GS:2) | **44** (G:30 GS:11 S:3) | same shape | −48 % |
| 2019-20 SKYSTONE | 24 (G:21 GS:3) | **45** (G:30 GS:12 S:3) | same shape | −47 % |
| 2020-21 ULTIMATE GOAL | 25 (G:21 GS:4) | **46** (G:30 GS:13 S:3) | same shape | −46 % |
| 2021-22 FREIGHT FRENZY | 23 (G:21 GS:2) | **44** (G:30 GS:11 S:3) | same shape | −48 % |
| 2022-23 POWER PLAY | 26 (G:21 GS:5) | **47** (G:30 GS:14 S:3) | same shape | −45 % |
| 2023-24 CENTERSTAGE | **47** (G:30 GS:13 S:4) | 47 | — | 0 % |

Three things this table says:

- **The "23-47 rules per season" range is the bug's own signature.** Six seasons land in a tight 23-26 band
  and one — CENTERSTAGE, the only legacy manual that **zero-pads** (`<G01>`, `<GS01>`, `<S01>`) — reports
  the truth. The true spread is 44-47, and it reconciles exactly with all seven dossiers' independently
  hand-verified counts.
- **The undercount is silent.** No warning is emitted, the tool's own `empty_body` check passes, and
  `rules=23` looks entirely plausible. The 2018-19 dossier calls it *"a silent 48 % undercount on Part 2
  with no warning."*
- **The missing rules are the ones that matter.** `<GS1>`-`<GS9>` is nine of eleven game-specific rules in
  2021-22, and the whole `<S>` safety prefix vanishes every time. As the 2022-23 dossier records: *"a
  dossier built on the parser's output alone would have omitted the descoring and possession rules
  entirely."*

**The fix is one character** and it is **still unapplied** — `tools/parse-legacy-manual.py` line 46 still
reads `RULE_TAG = re.compile(r"<([A-Z]{1,3})(\d{2,3})>")` as of this run. Note that the padding convention
is inconsistent *within a single manual*: 2018-19 Part 1 pads `<RS01>`-`<RS08>` and `<RS10>` but **not
`<RS9>`**, so `\d{1,3}` is required, not merely preferable.

A second, separate defect is documented independently by all seven dossiers: `--tsv` / `--json` never write,
because `main()` builds `pdfs = [a for a in argv if not a.startswith("-")]` **before** `take()` strips the
flag values, so the output path is collected as a second input PDF. The run prints `### MISSING <path>`,
returns exit 1, and writes nothing.

### 4.2 What is FORMAT-DEPENDENT and what is FORMAT-INDEPENDENT

| Component | Verdict | What it keys on | Measured behaviour on 2017-18 → 2023-24 |
|---|---|---|---|
| `reference/ftc_parse.py` | **Format-dependent (severe)** | font name, point size band, **four** hex colours, left margin, `[IEAGRTLC]\d{3}`, `n of N` footer | `rules=0` on all 7 — **with `unpaired=0`** |
| `tools/parse-legacy-manual.py` | **Format-independent**, except its digit regex | the literal `<TAG>` delimiter in flat text | 23-26 on 6 of 7 as shipped; 44-47 patched |
| `extract-tables.py` — the geometry | **Format-independent** | pymupdf ruling lines and cell rectangles | 8-11 tables recovered per season, rows correctly paired |
| `extract-tables.py` — captions, `--sections` | **Format-dependent** | `Table\s+\d+-\d+` regex; the PDF outline | **0** captions and **0** TOC entries on all 7 |
| `extract-tables.py` — the `SPLIT?` gate | Format-independent but **too weak** | an empty first cell | missed the 2019-20 page-break row; false-positives on merged headers |
| `render-pages.py` — the rasteriser | **Format-independent** | page number → PNG | worked on all 7 at 110-130 dpi, no issues reported |
| `render-pages.py` — the `--sections` default | **Format-dependent** | PDF outline + 2024-25 section numbering | inoperative on all 7 |
| ALL-CAPS novelty detector | **Format-dependent (severe)** | ALL-CAPS defined terms + a stoplist | names **no** scoring element, zone or goal |
| Tripwire greps — 4 of 5 categories | **Format-independent** | ordinary English, case-insensitive | 17-55 hits per category per manual |
| Tripwire greps — counting words; `penalty_mentions` | **Vocabulary-dependent** | `per MATCH`; `MINOR FOUL\|MAJOR FOUL` | **0** FOUL hits; the failure is partial and therefore invisible |
| Ingest gates (rule-count range, orange count, page count) | **Format-dependent** | the 2024-26 document shape | 180-230 rules / ~16-17 orange vs a legacy reality of 44-47 and **0** orange |

**The rule parser.** `ftc_parse.py` identifies a rule as: font normalised to `Roboto-Bold`, **and** size in
9.5-12.5 pt, **and** colour `#000000`, **and** `x0 < 70`, **and** text matching `^[IEAGRTLC]\d{3}$` — then
pairs it with a headline whose colour must be `#06844B` (evergreen) or `#ED7D31` (game-specific) on the same
baseline within ±3 pt, while suppressing commentary sitting inside a `#F4B083` fill and anchoring the footer
on a `^\d+ of \d+$` block. That is **seven independent presentation assumptions**. Its own source comments
record two near-misses *already inside the 2024-26 corpus*: a hyphen-style font name (`Roboto-Bold`)
hard-coded against a comma-style export (`Roboto,Bold`) returned **zero rules on both kickoff-day
releases**; and an exact `== 11.0` size test *"silently dropped all 39 E-rules and all 72 R-rules"* from the
2024-25 ITD kickoff export. Both were caught by hand and hard-coded around.

`parse-legacy-manual.py` is the opposite design: `pdftotext -layout` flat text, keyed only on an unambiguous
`<PREFIX###>` delimiter. No font, no colour, no geometry, no outline. That is exactly why it survives eleven
years of layout churn. **The delimiter is the format-independent thing; the parser's assumption about how
FIRST numbers *inside* the delimiter is not.**

**The geometric table extractor** splits cleanly down the middle. The extraction itself is
format-independent and was the single most valuable tool in the legacy corpus — the 2018-19 dossier verified
the §1.7 Scoring Summary **cell-by-cell against a 130-dpi render** and got an exact match, on a manual with
no outline and no captions. And the *reason* it exists is confirmed independently by all nine seasons: flat
`pdftotext -layout` mis-pairs the scoring table every time. 2022-23's flat text renders the Junction ladder
**off by one row** — a reader builds a model where a Ground Junction is worth 3 and a High Junction is worth
nothing. 2023-24's floats `20, 5, 30, 20, 10` into the Reference column with no numbers beside the Drone or
Suspend rows.

What is format-dependent is everything *around* the extraction: (a) the caption regex `Table\s+\d+-\d+`
matches **0** strings in all seven legacy Part 2 manuals against 51/68/30 in ITD/DECODE/BIOBUZZ V0
[measured], so every table comes back "(no caption on page)" and must be cited by page; (b) `--sections`
reads `doc.get_toc()`, which returns **0 entries** for all seven legacy PDFs against 130/157/88 for the
modern ones [measured] — every dossier's reproduction line uses `--pages` for this reason; (c) the `SPLIT?`
heuristic both false-positives (flagged the p.3 revision history as split in four seasons — it is a merged
header) and, worse, **false-negatives on the case that matters**: 2019-20's Scoring Summary lost its
`Parking | – | – | 5` row across a p.25→p.26 page break with **no flag at all**, a 10-point-per-alliance
endgame objective invisible from `INDEX.txt`; (d) phantom empty columns are routine (a logically 5-column
table returned as 21×15 in 2021-22; 9-11 columns for a printed 7 in 2023-24).

**The figure renderer** is format-independent in its core — rasterising page N to a PNG cannot break, and
every dossier reports it worked at 110-130 dpi — and format-dependent only in its **default**, which is
`--sections 8,9,10,11`. Those section numbers are a 2024-25 convention (legacy game content is §1 in
2017-18/2018-19 and §4 from 2019-20 on) and they resolve through the PDF outline, which legacy manuals do
not have. Keep the tool; never trust the default.

**The ALL-CAPS novelty detector is the most era-locked component in the harness, and the era it is locked to
is two seasons old.** `ingest-manual.sh` step 5 greps `[A-Z]{3,}('S)?`, subtracts
`reference/known_caps_stoplist.txt` and ranks by frequency, resting on its own comment: *"FTC sets every
defined term in ALL CAPS, so an ALL-CAPS token NOT already known … is almost certainly a NEW GAME NOUN."*
**That convention began in 2024-25.** [measured] Top ALL-CAPS tokens by frequency:

| Manual | Top 6 ALL-CAPS tokens |
|---|---|
| 2020-21 Part 2 | FIRST(84) ULTIMATE(5) GOAL(5) NOT(1) GAME(1) FTC(1) |
| 2021-22 Part 2 | FIRST(110) FREIGHT(5) FRENZYSM(3) FRENZY(2) NOT(1) FTC(1) |
| 2022-23 Part 2 | FIRST(126) POWERPLAYSM(5) NOT(1) FTC(1) ALL(1) |
| 2023-24 Part 2 | FIRST(135) CENTERSTAGESM(5) RTX(2) NOT(1) FTC(1) CAD(1) |
| **2024-25 CM V14** | **ROBOT(602) MATCH(377) ALLIANCE(247) FIRST(237) FIELD(221) ROBOTS(133)** |
| **2025-26 CM TU32** | **ROBOT(631) MATCH(439) FIELD(298) ALLIANCE(284) FIRST(282) MATCHES(161)** |

**Earlier seasons used Title Case.** [measured] "Scoring Element" (Title Case) appears **23 / 27 / 37 / 31 /
43 / 54 / 42** times across the seven legacy Part 2 manuals; "SCORING ELEMENT" appears **zero** times in any
of them. Run against any manual 2017-18 → 2023-24 the detector returns the brand name, the trademarked game
title and OCR noise — it names **no scoring element, no zone and no goal**. It is not degraded on legacy
manuals; it is inoperative.

Two further cautions the beta runs recorded. `known_caps_stoplist.txt` was itself built from BIOBUZZ V0 +
DECODE TU32 + ITD V14, so the 2024-25 run was **train-on-test and cannot measure novelty-detection
generalization at all**. And even on the season it was tuned for, the ranked output leaks vendor names,
materials and OCR fragments (`VEX 6`, `HIPS 4`, `BILDA 4`, `JST 1`, `NZS 1`, `ARTFACTS`, `DECODETM`) into
the top of the list an analyst trusts first.

**The tripwire greps generalise, with two vocabulary leaks.** Four of the five categories — hedge words,
timers/thresholds, exceptions and carve-outs, and scored-live-vs-scored-at-end — are `grep -i` over ordinary
English and fire on every era. [measured] Hedge words: 50 (2017-18) / 55 (2023-24) / 163 (ITD) / 179
(DECODE). Carve-outs: 18 / 33 / 58 / 64. Counting words: 26 / 17 / 59 / 66. The 2024-25 beta run measured
**312 tripwire hits against DECODE's 318**, across five categories on a season they were not written for,
with all five producing findings. Both leaks are vocabulary rather than layout:

- The **counting-words** category includes the literal phrase `per MATCH|each MATCH`. `grep -i` rescues it,
  but the phrase shape is a 2024-25 assumption.
- Step 6's `penalty_mentions` grep is `MINOR FOUL|MAJOR FOUL|YELLOW CARD|RED CARD|DISQUALIF|VERBAL WARNING`.
  On legacy manuals the two FOUL terms match **0 lines** while `Minor Penalty|Major Penalty` matches 69-117
  occurrences. The grep still returns 46-53 lines because the *card* terms survive — **so the failure is
  partial and therefore invisible**. You get a penalty file that has quietly omitted the entire penalty
  currency.

One more, for completeness: the `section_versions` grep (`^Section [0-9]+ .*  V[0-9]+`) measures 132 stamps
on ITD V14 and **0** on every legacy manual. That is correct behaviour — legacy manuals do not version
sections — but the harness prints an empty list rather than saying so.

### 4.3 What this implies for 2026-09-12, and the contingency

**The corpus already contains two documented format changes and two near-misses.** 2023-24 → 2024-25 changed
the document count, the rule-ID syntax, the game-specific marker, the defined-term case, the penalty
vocabulary, the period names, and added an outline, table captions and per-section version stamps — all at
once. Within the 2024-26 window, FIRST shipped the *same* manual through two PDF export paths
(`Roboto,Bold` vs `Roboto-Bold`), and shrank rule-ID text to 10.56 pt in a kickoff export. **Both near-misses
were on kickoff-day releases, and the BIOBUZZ manual arriving 2026-09-12 is a kickoff-day release.**

So the honest finding is this: **the harness is not robust to a format change; it is robust to the format
changes someone has already found and hard-coded around.** Split by what a component reads:

- **What survived eleven years:** components that read *text* (the flat-text `<TAG>` scan, four of five
  tripwire categories) and *physical geometry* (pymupdf's cell-rectangle table finder, the page rasteriser).
- **What will break:** components that read *presentation* — font name, point size, four hex colours, left
  margin, table caption strings, the PDF outline, and letter case.

If FIRST changes the format on 2026-09-12, the failure modes rank like this:

1. **Total change → clean stop.** `ftc_parse.py` returns `rules=0` with `unpaired=0`, and `RUN-KICKOFF.sh`
   exits **4** before ingest runs, correctly distinguishing "no rules at all — the layout was not
   recognised" (exit 4) from "rules parsed cleanly but none are G-rules — wrong file" (exit 3). Nothing is
   written and nothing downstream is poisoned. This guard is the single best feature of the harness.
2. **Partial change → silent wrong answer.** This is the likelier and far worse case: the orange hex shifts,
   or the ID pattern gains a letter, or a rule table indents on a page break, and the parser returns a
   plausible count with `unpaired=0`. **There is no check for that today.** The 2024-25 beta run already
   produced one instance of this class at a different layer: ingest gate G-d passed (it requires only
   "a `Table 10-x` row with 8 or more rows") **while Table 10-2 was entirely missing from `TABLES.md`**, with
   a glossary block masquerading under its heading. The analyst recovered it only by reading a rendered PNG.

**The contingency, in the order to run it on the day:**

1. **Trust exit 4; do not paste around it.** `rules=0` means the layout, not the file.
2. **Patch `parse-legacy-manual.py` now, before kickoff, not on the day.** `\d{2,3}` → `\d{1,3}`, plus
   moving the two `take()` calls above the `pdfs` assignment so `--tsv`/`--json` write. One character and
   two lines, both measured, and leaving them means every historical re-run stays 45-48 % short.
3. **Build the missing bare-ID fallback.** Neither parser can read a bare `G410`-style ID out of flat text:
   `ftc_parse.py` needs geometry, `parse-legacy-manual.py` needs angle brackets. A
   `grep -oE '^[A-Z]{1,2}[0-9]{3}' full_layout.txt | sort -u` recovers the rule-ID inventory from **any**
   layout with zero font, colour or geometry assumptions. Reconciling that flat-text count against
   `ftc_parse.py`'s geometric count is the check that would have caught **both** 2024-26 near-misses
   automatically. It is an hour of work and it is the highest-value thing to add before 2026-09-12.
4. **Run everything downstream anyway — it degrades gracefully.** `extract-tables.py --pages`,
   `render-pages.py --pages` and the tripwire greps all work with **zero** rule parsing. In the worst case
   the entire R3 scoring model can be rebuilt from a geometry-extracted table plus rendered pages — which is
   exactly how all seven legacy dossiers were built.
5. **Verify the ALL-CAPS convention before trusting the novelty detector.** One command answers it:
   `grep -oE '\b[A-Z]{3,}\b' full_layout.txt | sort | uniq -c | sort -rn | head`. If the top of the list is
   `FIRST` and the trademarked game name, the convention changed and the detector is returning pure noise.
   Fall back to the Section 16 glossary and the Section 9/10 figure captions.
6. **Add the two reconciliation gates the beta runs asked for.** (a) Every `Table 10-x` referenced in
   Section 10 prose must have a matching heading in `TABLES.md` — this catches the missing-Table-10-2 class.
   (b) The summary table's row count must reconcile against the achievements enumerated in the gameplay
   prose — this catches the 2019-20 page-break class. Both are cheap and both have already failed once.

**Blast radius if the format changes and nothing is prepared:** R1 ingest stops at the guard (good); **R3 is
recoverable by hand in a few hours** from geometry tables plus rendered figures; R5 and R6 lose their
structured rule bodies and violation strings entirely and would have to be read by hand off the PDF. The
rule-dependent phases are the ones at risk. The scoring model is not.

---

## 5. Coverage gaps

### 5.1 Seasons with manuals in the corpus but no dossier

`manuals/archive/wayback/` holds complete game manuals for **twelve seasons before 2017-18** — 2005-06
HALF PIPE HUSTLE (FVC), 2006-07 HANGIN'-A-ROUND, 2007-08 QUAD QUANDARY, 2008-09 FACE OFF, 2009-10 HOT SHOT!,
2010-11 GET OVER IT!, 2011-12 BOWLED OVER!, 2012-13 RING IT UP!, 2013-14 BLOCK PARTY!, 2014-15 CASCADE
EFFECT, 2015-16 RES-Q, 2016-17 VELOCITY VORTEX — **none of them dossiered**. Q&A archives exist for 2011-12,
2012-13, 2013-14, 2015-16 and 2016-17 with no analysis attached to any of them.

**2016-17 VELOCITY VORTEX is the highest-value single addition.** The 2017-18 dossier already diffs against
it and found the transition worth recording: unchanged were the 30 s / 2 min / final-30 s structure, Minor 10
/ Major 40, the QP/RP formula, the 18-in cube and the 8-motor / 12-servo cap; changed were the vision target
(2016-17's Vuforia targets "remain in the same locations for every Match" — navigation aids, not a
randomiser) and the control system (the string "Expansion Hub" appears **0** times in the 2016-17 Part 1 and
**48** times in the 2017-18 Part 1). One more dossier extends this index to ten seasons at low cost.

### 5.2 2024-25 and 2025-26 are not dossiers

Those two rows are assembled from **harness beta-test outputs** — `STATUS.md`, `R3-scoring-model.md`,
`R5*`/`R6*`, `D5-ranked-strategies.md`, `BETA-TEST-VERDICT-ITD.md` — not from season dossiers in this
directory's format. They therefore have **no §6 robot-archetype section, no §7 strategic-lesson section
written in the same shape, and no §9 extraction notes**. Every trend in §2 for those two seasons rests on
the scoring model and the ingest STATUS alone. Writing 2024-25 and 2025-26 up as proper dossiers is the
cheapest way to make this index internally consistent, and it would also test the §3 lessons against the two
seasons closest to BIOBUZZ.

### 5.3 Documents in the corpus that no analysis has read

- **Q&A archives for 2024-25 and 2025-26 exist and were never opened.**
  `manuals/archive/supplemental/2024-25_ITD_Complete_QA.html` and `2025-26_DECODE_Complete_QA.html` are both
  present; neither beta run cites either (grep for "Complete_QA" across `analysis/ITD/` and
  `analysis/kickoff/` returns **0** hits). This matters because the 2024-25 run left **the AUTO re-count
  question — worth 40 points of ceiling — marked UNVERIFIED and "queued for Game Q&A"** while a Q&A archive
  for that exact season sat unread in the corpus. Every legacy dossier used its Q&A archive heavily and
  ranked Q&A density as the ambiguity map; the modern-era runs did not.
- **2022-23's Q&A exists only as `.html`** (388 KB, 375 items) and was missed by an inventory keyed on file
  extension — the harness brief asserted no archive existed for that season. The 2022-23 dossier's fix
  stands: index `supplemental/` by **filename stem**, not extension, and add an HTML branch to the Q&A
  ingestion path. The 2024-25 and 2025-26 archives are HTML too, so this is not a legacy-only problem.
- **No Field Setup Guide for any legacy season.** They exist for 2024-25 (`ITD_FieldGuide.pdf`) and 2025-26
  (`DECODE_EventFieldSetupGuide.pdf`, plus field CAD and the AprilTag sheet) but for none of 2017-18 →
  2023-24 — which is precisely the document the 2017-18 dossier needed to resolve its unit-conversion
  ambiguity (below).
- **No historical score-inflation curve is available to the analysis.** The 2024-25 run could not
  sanity-check "a realistic winning score" against anything and left it at `[JUDGMENT] ≈ 150-200`.

### 5.4 Everything a dossier had to mark UNVERIFIED

| Season | UNVERIFIED item | Why it matters |
|---|---|---|
| 2017-18 | The Relic's mass: §1.4 says *"approximately 4.72 ounces (214 gm)"* — 4.72 oz is ~134 g, 214 g is ~7.55 oz. **Which figure is correct is unknown.** | The other conversions in the same section are internally consistent, so one of the two is simply wrong. The official Field Setup Guide would settle it; there is none for this season |
| 2018-19 | **Cargo Hold capacity** — the manual never states a Mineral limit per hold. Also, the vision toolchain used for Sampling is not described in either manual | Caps the sorted-Mineral branch of any scoring model |
| 2019-20 | Whether a single Stone can earn **both** Autonomous Delivery (§4.5.2.2) **and** Autonomous Placing (§4.5.2.4). The two rows carry different "When Scored" semantics, which reads as independent, but `<G24>` (highest-value-only) is a plausible counter-reading. **Not resolved in the manual or the Q&A archive.** Separately, the 2018-19 comparison was never done — the prior manual was not read | Changes the auto ceiling |
| 2020-21 | Period-length comparison to 2019-20 — not stated in the documents read | Cosmetic |
| 2021-22 | Whether the Pre-Load earns **both** the 6-point Auto Hub row **and** the 20-point Auto Bonus. The §4.7 table and §4.5.2.3b/§4.5.2.4 read as separate achievements (26 total); Q&A Q106 confirms only the adjacent case. **Safe floor is 20** | 6 points per robot |
| 2022-23 | — none substantive | |
| 2023-24 | — none substantive | |
| **2024-25** | **Whether elements scored in AUTO are counted again at the end.** Moves the ceiling **266 → 306** and AUTO's value from 13 points to 26. The bundle does not answer it and nothing in the harness flags it as open — `TRIPWIRES.txt` holds the relevant sentences but is gated to phase R6 | The single largest open number in the season |
| **2025-26** | **Four:** whether an ARTIFACT re-scored through the SQUARE counts twice toward GOAL RP (decides whether GOAL RP is reachable at all); whether ARTIFACTS still on the RAMP at 0:00 with the GATE open are "retained by the GATE"; whether the DEPOT has any capacity ("over the DEPOT" is given no volume); whether "All Other Events" RP thresholds apply to League play. **And the PATTERN double-assessment — worth 18 of a 36-point ceiling — is `[DERIVED]`, not `[MANUAL]`: the manual never states additivity in words** | If PATTERN is scored once, the ceiling halves, both RP thresholds become unreachable-to-marginal, and AUTO's share of a realistic score drops from 41 % to 27 % |

### 5.5 Where the dossiers disagree with each other

**1. How many seasons the single-digit tag bug affects.** The 2022-23 dossier scopes it to *"three of the
seven legacy seasons"* (2020-21, 2021-22, 2022-23). The 2017-18, 2018-19 and 2019-20 dossiers each
independently document the same defect on their own manuals. The re-measurement in §4.1 confirms **six of
seven** are affected; only 2023-24 CENTERSTAGE is clean. Both claims are in the corpus; six-of-seven is the
measured figure.

**2. The 2020-21 violation-line count.** The ULTIMATE GOAL dossier's rule inventory reports **25 of 46**
Part 2 rules as carrying a Violation/Penalty line — while the *same dossier* prints a list of the rules
carrying **no** such line containing exactly **21** entries (`G1`-`G10`, `G12`, `G13`, `G16`, `G27`, `GS1`,
`GS2`, `GS3`, `GS7`, `S1`-`S3`). A re-run of the parser measures **`violations=21`** on that manual. The
headline number and the enumerated list appear **transposed**; the list is the correct one.

**3. What `violations=N` means at all.** The 2017-18, 2018-19, 2019-20 and 2023-24 dossiers each warn —
independently and correctly — that `parse-legacy-manual.py`'s `with_violation` field is a **prose keyword
match** on `Violation|Penalty` inside a 400-character body window, not a parsed field, and that legacy
manuals contain **zero** structured `Violation:` lines (the literal string appears 0 times in 2017-18 Part
2). The 2020-21 and 2021-22 dossiers nonetheless tabulate the number as if it were a coverage metric.
**It is not comparable to a 2024-25+ `Violation:` count and must never be charted against one.** The
authoritative consequence source for the whole legacy era is the **Rule Summary table** — §1.8 (2017-18,
2018-19), §4.8 (2019-20 → 2021-22), §4.7 (2022-23, 2023-24) — recovered by geometry, which carries explicit
Warning / Disable / Minor / Major / Card columns. Note that it is **not** a rule inventory either: 2018-19's
lists 35 rows against 44 tagged rules, and the 9 omitted G-rules include `<G24>`, which is exactly why the
End Game exclusivity was non-obvious enough to need a Q&A ruling.
