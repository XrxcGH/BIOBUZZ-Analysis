# R3 — THE SCORING MODEL

**Phase:** R3 (`reference/ANALYSIS-PROTOCOL.md` §3) · **Run:** 2026-08-23 beta test
**Manual under review:** ingested bundle at `analysis/kickoff/bundle/`, 188 pp, 214 rules, 17 game-specific.
**Sources used:** `bundle/TABLES.md`, `bundle/rules_full.tsv`, `bundle/VIOLATIONS.tsv`, `bundle/figures/*.png`,
Sections 8/9/10/13/16 prose from `bundle/full_layout.txt` (**prose only — every point value in this file came
from `TABLES.md` and was re-verified against the rendered page image `figures/p088_s10-game-details.png`**).

**Labels:** `[MANUAL]` = stated in the manual, cited · `[DERIVED]` = computed, operands shown ·
`[JUDGMENT]` = a call by this program · `UNVERIFIED` = the manual does not say.

> **Leakage disclosure (required by the test protocol).** I have prior familiarity with this game from
> outside the bundle. I have not used it. Every number, rule id, table number, dimension and quoted
> sentence in this document was read out of the bundle in this session and can be traced to the cite
> given. Two places where my prior knowledge agreed with what I read are flagged inline as
> **[prior-knowledge agreement — not used as evidence]** so a reviewer can discount them. Nothing in this
> file rests on an unsourced recollection.

---

## 0. The clock — what we are dividing by

| Period | Length | Cite |
|---|---:|---|
| AUTO | 30 s | §10.4 `[MANUAL]` "The first period of each MATCH is 30 seconds (0:30) long and called the Autonomous Period (AUTO)." |
| AUTO→TELEOP transition | 8 s | §10.4 `[MANUAL]` "There is an 8-second delay between AUTO and TELEOP for scoring purposes" |
| TELEOP | 120 s | §10.4 `[MANUAL]` |
| **Named ENDGAME** | **NONE** | `[DERIVED]` `grep -c -i endgame full_layout.txt` → **0**. Two rules key off "the final 20 seconds" (**G415.A**, **G427**) and Table 9-1 fires a "Train Whistle" audio cue at 0:20, but there is no separate scoring period. |

`T_match_play = 30 + 120 = 150 s` of robot-controlled time. The 8-second transition is dead time —
**G403** `[MANUAL]`: "Any powered movement of the ROBOT or any of its MECHANISMS is not allowed during the
transition period between AUTO and TELEOP." Violation: MAJOR FOUL.

Table 9-1 (`TABLES.md` p.77) is a countdown display, not a second clock: MATCH start 2:30 → AUTO ends 2:00
→ transition 0:07–0:01 → TELEOP begins 2:00 → 0:20 → 0:00. `[MANUAL]` "If there is a discrepancy between an
audio cue and the visual FIELD timers, the visual FIELD timers are the authority."

---

## 1. THE COMPLETE SCORING TABLE

### 1.1 Table 10-2 — DECODE point values (`TABLES.md` p.88, verified against `figures/p088_s10-game-details.png`)

| Achievement | Sub-condition | AUTO | TELEOP | RP | Per what | Cap | Assessment (§10.5) |
|---|---|---:|---:|---:|---|---|---|
| **LEAVE** | — | **3** | — | — | per ROBOT | 6/alliance (2 robots) | **AT END OF AUTO** — §10.5.E |
| **ARTIFACT** | **CLASSIFIED** | **3** | **3** | — | per ARTIFACT | uncapped; RAMP holds 9 at a time | **LIVE / AT REST** — §10.5.A |
| | **OVERFLOW** | **1** | **1** | — | per ARTIFACT | uncapped | **LIVE / AT REST** — §10.5.A |
| | **DEPOT** | — | **1** | — | per ARTIFACT | UNVERIFIED (physical) | **AT END OF TELEOP** — §10.5.D |
| **PATTERN** | ARTIFACT matches MOTIF | **2** | **2** | — | per matching ARTIFACT | 9 indices → 18/assessment | **AT END OF EACH PERIOD** — §10.5.B, §10.5.C |
| **BASE** | Partially returned to BASE | — | **5** | — | per ROBOT | — | **AT END OF TELEOP** — §10.5.F |
| | Fully returned to BASE | — | **10** | — | per ROBOT | — | **AT END OF TELEOP** — §10.5.F |
| | **Additional Bonus:** 2 ROBOTS fully returned to BASE | — | **10** | — | per ALLIANCE | once | **AT END OF TELEOP** — §10.5.F |
| **MOVEMENT RP** | Combined LEAVE + BASE points ≥ threshold | — | — | **1** | per ALLIANCE | 1 | end of MATCH |
| **GOAL RP** | Number of ARTIFACTS scored through the SQUARE ≥ threshold | — | — | **1** | per ALLIANCE | 1 | end of MATCH |
| **PATTERN RP** | PATTERN points earned ≥ threshold | — | — | **1** | per ALLIANCE | 1 | end of MATCH |
| **WIN** | More MATCH points than your opponent | — | — | **3** | per ALLIANCE | 1 | end of MATCH |
| **TIE** | Same MATCH points as your opponent | — | — | **1** | per ALLIANCE | 1 | end of MATCH |

**Maximum RP available in one Qualification MATCH = 3 + 1 + 1 + 1 = 6** `[DERIVED]` (WIN 3, plus the three
achievement RPs; WIN and TIE are mutually exclusive).

### 1.2 Table 10-3 — RP thresholds (`TABLES.md` p.88)

| RP Type | *FIRST* Championship | Regional Championships | All Other Events\* |
|---|---:|---:|---:|
| MOVEMENT RP | 21 | 21 | **16** |
| GOAL RP | 67 | 42 | **36** |
| PATTERN RP | 22 | 22 | **18** |

\*`[MANUAL]` orange box, non-binding commentary: "RP thresholds for Regional Championships and *FIRST*
Championship will be announced in Team Updates" and "Premier Events will be able to set their own
thresholds." **Plan against the "All Other Events" column** — that is what a Qualifier uses. `[JUDGMENT]`

### 1.3 Table 10-4 — the penalty currency (`TABLES.md` p.89)

| Penalty | Value |
|---|---|
| MINOR FOUL | `[MANUAL]` "a credit of 5 points towards the opponent's MATCH point total" |
| MAJOR FOUL | `[MANUAL]` "a credit of 15 points towards the opponent's MATCH point total" |
| ALLIANCE is ineligible for RP | `[MANUAL]` "This overrides any RP awarded through normal MATCH play or other rule violations." |
| DISQUALIFIED | `[MANUAL]` "0 MATCH points and 0 RANKING POINTS in a Qualification MATCH" |

**Exchange rate `[DERIVED]`:** 1 MAJOR FOUL = 15 pts = **5 CLASSIFIED ARTIFACTS** (15 ÷ 3). 1 MINOR FOUL =
5 pts = 1.67 CLASSIFIED ARTIFACTS. A single MAJOR FOUL erases roughly one-third of a realistic TELEOP
cycling output (see §4).

### 1.4 The rows that pay in RP, not points — un-priceable by any points model

These come from `bundle/VIOLATIONS.tsv` and `rules_full.tsv`. They matter to the scoring model because
**no amount of scoring recovers them.**

| Rule | Headline | Violation |
|---|---|---|
| **G206** | Don't violate rules for RPs | `[MANUAL]` "YELLOW CARD and the ALLIANCE is ineligible for PATTERN and GOAL RPs" |
| **G417** | ROBOTS only operate GATES as directed | `[MANUAL]` "MAJOR FOUL and the opposing ALLIANCE is awarded the PATTERN RP if G417.A" (contacting the **opponent's** GATE) |
| **G418** | ROBOTS may not meddle with ARTIFACTS on RAMPS | `[MANUAL]` "MAJOR FOUL per ARTIFACT, and the ALLIANCE is ineligible for the PATTERN RP if G418.A, or the opposing ALLIANCE is awarded the PATTERN RP if G418.B" |
| **G419** | ROBOTS LAUNCH into their own GOAL | `[MANUAL]` "MAJOR FOUL per ARTIFACT and the opposing ALLIANCE is awarded the PATTERN RP if [G419.B]" |
| **G431** | DRIVE TEAMS, watch your reach | `[MANUAL]` "RED CARD and the opposing ALLIANCE is awarded the PATTERN RP if G431.C" (a DRIVE TEAM member disrupting SCORING ELEMENT scoring) |
| **G427** | BASE ZONE protection | `[MANUAL]` "MAJOR FOUL and opponent ROBOT and any ROBOT fully supported by the contacted ROBOT are awarded fully returned to BASE points" |

`[DERIVED]` **G427 makes late-match BASE defence strictly self-harming:** the cost is 15 (MAJOR FOUL) + up to
20 (two ROBOTS' fully-returned points handed over) + the opponent then likely clears the MOVEMENT RP =
**35 points and an RP for one contact.** Do not defend the BASE ZONE. Ever.

`[DERIVED]` **G418 is the sharpest own-goal in the manual for a shooter team:** "MAJOR FOUL **per ARTIFACT**"
for contacting ARTIFACTS on a RAMP — *including your own RAMP*. A robot that bumps its own loaded ramp
while reaching for the GATE pays 15 points per ball touched **and** forfeits the PATTERN RP.

### 1.5 The scoring geometry that constrains the table

| Fact | Value | Cite |
|---|---|---|
| ARTIFACTS on the FIELD | 36 total — **24 purple, 12 green** | §9.9 `[MANUAL]` |
| Staging | 3 on each of 6 SPIKE MARKS (18) + 3 in each LOADING ZONE (6) + 6 in each ALLIANCE AREA (12) = **36** `[DERIVED]` | §10.3.1 |
| Pre-load allowance | **up to 3 ARTIFACTS per ROBOT**, drawn from your own ALLIANCE AREA stock | §10.3.1 `[MANUAL]` |
| CONTROL limit | **3 at a time** — **G408** `[MANUAL]` "A ROBOT may not simultaneously CONTROL more than 3 ARTIFACTS." MINOR FOUL per SCORING ELEMENT over the limit | G408 |
| RAMP capacity | **9 CLASSIFIED ARTIFACTS**, then newly entered ARTIFACTS OVERFLOW | §9.8.2 `[MANUAL]` |
| PATTERN indices | **9**, ordered GATE→SQUARE as 1…9; the 3-ARTIFACT MOTIF repeats 3× | §10.5.2 + Figure 10-4 `[MANUAL]` |
| MOTIF set | 3 MOTIFS: **GPP (tag 21), PGP (tag 22), PPG (tag 23)**, each 2 purple + 1 green | §9.6, §9.10 `[MANUAL]` |
| GOAL top lip | **38.75 in** above the TILE; opening 26.5 in × 18.3 in | §9.7 `[MANUAL]` |
| ROBOT height limit | **18 in**; **38 in** only during the final 20 s and when not in any LAUNCH ZONE — **R105.B/C**, **G415** | `[MANUAL]` |
| BASE ZONE | **one 18 in × 18 in zone per ALLIANCE** | §9.3 `[MANUAL]` |
| ALLIANCE AREA storage cap | **6 ARTIFACTS out of play** during TELEOP — **G434** | `[MANUAL]` |
| Human player scope | **LOADING ZONE only, TELEOP only, no tools** — **G432**; **G433** ARTIFACTS only | `[MANUAL]` |

`[DERIVED]` **This is a launcher game, not a placer game.** The GOAL lip is 38.75 in. R105.B caps a ROBOT at
18 in for 130 of the 150 seconds of play, and R105.C's 38 in exception is both time-limited (final 20 s) and
still 0.75 in short of the lip. Over-the-top placement is marginal at best; **G416** independently requires
"ROBOTS may only LAUNCH SCORING ELEMENTS when inside a LAUNCH ZONE or overlapping a LAUNCH LINE," with
"MAJOR FOUL per LAUNCHED SCORING ELEMENT if the SCORING ELEMENT enters the open top of the GOAL" from
outside. Everything is shot, from a defined zone.

`[DERIVED]` **The shot order is fully determined and the field supply ratio matches it.** Figure 10-4 lays the
RAMP out `GATE | 1 2 3 4 5 6 7 8 9 | SQUARE` — ARTIFACTS enter at the SQUARE and roll down toward the GATE,
so the **first** ARTIFACT scored occupies index 1 and the ninth occupies index 9. For MOTIF GPP the required
firing sequence is therefore **G,P,P,G,P,P,G,P,P** — 3 green and 6 purple, and the field holds 12 G and 24 P,
exactly 1:2. The robot must be able to *choose which colour it fires next*. That is the whole PATTERN
challenge and it is a sorting problem, not a mechanism problem.

`[DERIVED]` **Scoring resupplies your opponent.** §9.8.3: "The GATE is an ALLIANCE specific FIELD element that
prevents CLASSIFIED ARTIFACTS from exiting the RAMP into **the opposing ALLIANCE'S SECRET TUNNEL ZONE** …
OVERFLOW ARTIFACTS can pass over the top of the GATE to exit the RAMP into the opposing ALLIANCE'S SECRET
TUNNEL ZONE." Figure 9-3 confirms the left wall runs GATE ZONE-**BLUE** (top, at the blue GOAL in A6) →
SECRET TUNNEL ZONE-**RED** → LOADING ZONE-**RED** (A1). So blue's scored ARTIFACTS roll down into red's
LOADING ZONE, where red's HUMAN PLAYER re-enters them. **Every ARTIFACT you score is delivered to your
opponent's human player.** This closed loop is why GOAL RP can exceed the 36 ARTIFACTS on the field.

---

## 2. THE HIGHEST-LEVERAGE QUESTION — is AUTO scored live or at the end, and is it re-counted?

### 2.1 The governing text, quoted in full

`[MANUAL]` §10.5 Scoring, p.83: "All achievements are updated by FIELD STAFF throughout the MATCH. Scoring
achievements are assessed as follows:

> **A.** Assessment of ARTIFACTS as either CLASSIFIED or OVERFLOW occurs throughout the MATCH and continues
> until all ARTIFACTS have come to rest following the conclusion of the MATCH. ARTIFACTS that meet scoring
> criteria prior to the start of TELEOP are assessed as part of AUTO
>
> **B.** Assessment of AUTO PATTERN scoring occurs at when all ARTIFACTS have come to rest following the
> conclusion of AUTO or the start of TELEOP, whichever comes first.
>
> **C.** Assessment of TELEOP PATTERN scoring occurs when all ROBOTS and ARTIFACTS have come to rest
> following the conclusion of the MATCH.
>
> **D.** Assessment of DEPOT scoring occurs at the end of TELEOP when all ROBOTS and ARTIFACTS have come to
> rest following the conclusion of the MATCH.
>
> **E.** Assessment of LEAVE scoring occurs at the end of AUTO.
>
> **F.** Assessment of BASE scoring occurs at the end of the TELEOP."

And §10.5.2, p.86 `[MANUAL]`: "**At the end of AUTO and TELEOP**, ARTIFACTS that are directly on the RAMP
score for PATTERN points if the color of the ARTIFACT in order matches the MOTIF color for that index, and
the ARTIFACTS **are retained by the GATE**."

### 2.2 The answer, row by row

| Achievement | Live or end-of-period? | Re-counted at the end of the MATCH? |
|---|---|---|
| CLASSIFIED / OVERFLOW | **Live**, continuously (§10.5.A), with the AUTO/TELEOP split decided by whether the ARTIFACT met criteria *before the start of TELEOP* | **No.** Each ARTIFACT is counted **once**. (Moot for value: AUTO and TELEOP both pay 3 and 1.) |
| LEAVE | **End of AUTO** (§10.5.E) | No |
| **PATTERN** | **End of AUTO** *and* **end of TELEOP** — **two separate assessments** (§10.5.B, §10.5.C), with **separate AUTO and TELEOP columns in Table 10-2** | **YES — this is the re-count.** |
| DEPOT | End of TELEOP, at rest (§10.5.D) | No |
| BASE | End of TELEOP (§10.5.F) | No |

### 2.3 The one answer that changes the season — `[DERIVED]`, and it must be Q&A'd

**Claim:** an ARTIFACT that is CLASSIFIED onto a MOTIF-matching index during AUTO and is still there at
0:00 scores **3 + 2 + 2 = 7 points from a single shot**: 3 for CLASSIFIED (once), 2 for the AUTO PATTERN
assessment, and 2 again for the TELEOP PATTERN assessment.

**Evidence chain:**
1. `[MANUAL]` Table 10-2 gives PATTERN a value in the **AUTO column (2)** *and* the **TELEOP column (2)**. No
   other row in the table has that shape without the two being genuinely separate events (LEAVE is AUTO-only;
   BASE and DEPOT are TELEOP-only; CLASSIFIED/OVERFLOW pay the same either way, so their two columns are a
   labelling convenience, not a double count — §10.5.A says explicitly that each ARTIFACT is assessed once).
2. `[MANUAL]` §10.5.B and §10.5.C define **two assessments at two different instants**, with different
   at-rest conditions.
3. `[DERIVED] — the decisive arithmetic.` A single PATTERN assessment cannot exceed
   **9 indices × 2 pts = 18 points**. The *FIRST* Championship **PATTERN RP threshold is 22** (Table 10-3).
   **22 > 18.** A threshold that no alliance could ever reach would be meaningless, so PATTERN points must
   accumulate across the two assessments. Maximum PATTERN = 18 + 18 = **36**, and 22 ÷ 36 = 61 % — a sane
   threshold. The "All Other Events" threshold of 18 is likewise 18 ÷ 36 = 50 %; under a single-assessment
   reading it would demand a **perfect 9-of-9 ramp**, which is not how FIRST sets a base-tier threshold.
4. `[MANUAL]` corroboration that the *end-of-match* state is what is scored, from the **G203/G204** worked
   examples (p.96): "Team C requests Team A to **open the GATE at the end of the MATCH** in order resulting
   in teams A and B **not earning the PATTERN RP**." Opening the GATE at 0:00 destroys the TELEOP PATTERN —
   which is only possible if the TELEOP PATTERN is a live, separately-earned quantity.

**Confidence:** high, but **the manual never states additivity in words.** Under house rule 4 this is
`[DERIVED]`, not `[MANUAL]`.

> **Q&A QUESTION #1 (file the minute the Game Q&A opens).** *"Table 10-2 lists PATTERN with a value of 2 in
> both the AUTO and TELEOP columns, and §10.5 B and C describe two separate assessments. If an ARTIFACT is
> on a MOTIF-matching RAMP index at the end of AUTO and is still on that index at the end of TELEOP, does the
> ALLIANCE earn 2 points at the AUTO assessment **and** a further 2 points at the TELEOP assessment, for 4
> PATTERN points from that one ARTIFACT?"*
>
> **Everything below is arithmetic on the answer.** If the answer is "no, PATTERN is scored once," the
> PATTERN ceiling halves from 36 to 18, the PATTERN RP thresholds of 18/22 become unreachable-to-marginal,
> and AUTO's share of the point budget drops from 41 % to 27 % of a realistic winning score. Re-run §3–§6.

### 2.4 Two second-order assessment traps

`[MANUAL]` §10.5 orange box (**non-binding commentary, not quoted as a rule**): "Achievements scored before
the MATCH starts, during the AUTO-to-TELEOP transition, and after the MATCH ends at 0:00 are subject to
penalties." Read with **G404** `[MANUAL]`: "MAJOR FOUL **per ARTIFACT** if ROBOT LAUNCHES an ARTIFACT such
that it enters the open top of a GOAL after the end of TELEOP. MAJOR FOUL if ROBOT contacts a GATE after the
end of TELEOP." `[DERIVED]` A shot fired at 0:00 that lands at 0:01 is not worth 3 points, it is worth
**−15**. Programme a hard cutoff at ~0:01.

`[MANUAL]` §10.5 orange box: "LEAVING the LAUNCH LINE, ARTIFACT scoring, and return to BASE points are all
evaluated and scored by **human volunteers**." `[JUDGMENT]` Design for legibility: a robot that is
*obviously* fully inside the BASE ZONE beats one that is technically inside it.

---

## 3. POINTS PER SECOND, PER SCORING ACTION

Protocol: `reference/STRATEGY-RANKING-PROTOCOL.md` §6.2 — decompose into
`t_acq + t_out + t_align + t_deliver + t_back`, never estimate the cycle whole. House rule 3 — show the
division. Every `t` below is `[JUDGMENT]` for a 15-student, hand-tools-plus-3D-printing, two-robot program,
and every un-measured cycle is also reported **×1.3** per the protocol's pessimism rule.

### 3.1 Geometry inputs (measured off the figures, tiles are 24 in)

Coordinates in inches from the bottom-left (audience-left) corner. Column A…F left→right, row 1…6
bottom→top (Figure 9-5, `figures/p063_s9-arena.png`). Red ALLIANCE AREA is on the left (§9.5); the **blue**
GOAL is at A6 and the **red** GOAL is at F6 (Figures 9-2, 9-5) — **each ALLIANCE's GOAL is diagonally
opposite its own LOADING ZONE.**

| Landmark (red ALLIANCE) | Position | Source |
|---|---|---|
| LOADING ZONE (supply) | A1 corner, 23 in × 23 in, centre ≈ **(11.5, 11.5)** | §9.3 |
| GOAL mouth | F6 corner, centre of the 27 in × 27 in footprint ≈ **(130, 130)** | §9.7 |
| BASE ZONE | B2, 18 in × 18 in, centre ≈ **(36, 36)** | §9.3, Figure 9-5 |
| Audience-side LAUNCH ZONE | triangle, base x = 48…96 on the bottom wall, apex **(72, 24)** | §9.3 ("2 TILES wide and 1 TILE deep") |
| GOAL-side LAUNCH ZONE | triangle, base = the whole top wall, apex (72, 72) | §9.3 ("6 TILES wide by 3 TILES deep") |
| GATE ZONE | right wall, ≈ **(140, 70)** | `[DERIVED]`: 27 in GOAL + ~47 in RAMP + 46.5 in SECRET TUNNEL + 23 in LOADING ZONE = 143.5 ≈ 144 in of wall, so the GATE sits ~74 in down from the F6 corner |

**Drive speed `[JUDGMENT]`:** assumed free speed 52 in/s × **0.7** (acceleration, turns, traffic — the
protocol's mandated realism factor) = **36 in/s**, i.e. 1.5 tiles/s. Every travel term below is
`distance ÷ 36`.

### 3.2 The two candidate TELEOP cycles

Supply is at A1, the GOAL is at F6. There are only two shapes of cycle.

**Cycle L — reload at A1, shoot long from the audience-side LAUNCH ZONE apex (72, 24)**

| Term | Distance / basis | Seconds |
|---|---|---:|
| `t_acq` | HUMAN PLAYER hands over 3 ARTIFACTS (G408 cap), robot stationary | 2.5 |
| `t_out` | (11.5,11.5)→(72,24): √(60.5² + 12.5²) = 61.8 in ÷ 36 | 1.7 |
| `t_align` | heading lock on AprilTag **ID 24** (§9.10) at 10 ft | 1.5 |
| `t_deliver` | 3 shots × 0.8 s flywheel recovery | 2.4 |
| `t_back` | 61.8 in ÷ 36 | 1.7 |
| **`t_cycle`** | 2.5 + 1.7 + 1.5 + 2.4 + 1.7 | **9.8** |
| **×1.3 pessimism** | | **12.7** |

Shot distance: (72,24)→(130,130) = √(58² + 106²) = **121 in = 10.1 ft.** Make rate `[JUDGMENT]` **60 %**.

**Cycle N — reload at A1, drive up and shoot short from inside the GOAL-side LAUNCH ZONE (110, 110)**

| Term | Distance / basis | Seconds |
|---|---|---:|
| `t_acq` | as above | 2.5 |
| `t_out` | (11.5,11.5)→(110,110): √(98.5² + 98.5²) = 139 in ÷ 36 | 3.9 |
| `t_align` | 28 in shot, forgiving | 1.0 |
| `t_deliver` | 3 × 0.8 | 2.4 |
| `t_back` | 139 ÷ 36 | 3.9 |
| **`t_cycle`** | 2.5 + 3.9 + 1.0 + 2.4 + 3.9 | **13.7** |
| **×1.3 pessimism** | | **17.8** |

Shot distance: (110,110)→(130,130) = √(20² + 20²) = **28 in.** Make rate `[JUDGMENT]` **85 %**.

**`[DERIVED]` The two cycles are dead even at those assumptions:**
- Cycle L: 3 shots × 0.60 = 1.8 made × 3 pts = 5.4 pts ÷ 12.7 s = **0.43 pts/s**
- Cycle N: 3 shots × 0.85 = 2.55 made × 3 pts = 7.65 pts ÷ 17.8 s = **0.43 pts/s**

**Break-even make rate for the long shot** `[DERIVED]`: solve `x × 3 shots × 3 pts ÷ 12.7 s = 0.43 pts/s`
→ `x = 0.43 × 12.7 ÷ 9 = 0.607`. **Hit 61 % or better at 10 ft and the long shot wins. Below 61 %, drive
the ball to the goal.** This single number should be the first thing measured on a taped mock-up in week 1.

### 3.3 The full points-per-second table

`t_per_artifact` = `t_cycle ÷ 3` (G408 caps CONTROL at 3). Cycle L: 12.7 ÷ 3 = **4.2 s/ARTIFACT**.
AUTO preload shot (robot starts at F6 touching its own GOAL per **G304.B**, so range is short): the AUTO
opening sequence is 1.0 s off the line + 1.0 s align + 2.4 s for 3 shots = 4.4 s ×1.3 = 5.7 s ÷ 3 =
**1.9 s/ARTIFACT** at the 85 % near-range make rate.

| # | Action | Points | Seconds charged | Division | pts/s | Repeatable? |
|--:|---|---:|---:|---|---:|---|
| 1 | **AUTO CLASSIFIED onto a matching index** | 3 + 2 + 2 = **7** | 1.9 | 7 × 0.85 ÷ 1.9 | **3.13** | yes (×9 max) |
| 2 | **BASE — both ROBOTS fully returned** | 10 + 10 + 10 = **30** | 10 | 30 ÷ 10 | **3.00** | no, one-shot |
| 3 | **Open your own GATE** | 0 direct; converts the next 9 ARTIFACTS from OVERFLOW (1) to CLASSIFIED (3) = 9 × 2 = **+18 enabled** | 7.0 (see §3.4) | 18 ÷ 7 | **2.57** | yes |
| 4 | **LEAVE** (both ROBOTS) | 3 + 3 = **6** | 2.0 (1.0 s per robot, on the path anyway) | 6 ÷ 2.0 | **3.00** | no, one-shot |
| 5 | **BASE — one full + one partial** | 10 + 5 = **15** | 8 | 15 ÷ 8 | **1.88** | no, one-shot |
| 6 | **AUTO CLASSIFIED, non-matching** | **3** | 1.9 | 3 × 0.85 ÷ 1.9 | **1.34** | yes |
| 7 | **DEPOT dump** (already parked at your GOAL) | **1** each | 1.0 | 1 ÷ 1.0 | **1.00** | yes but see §6 |
| 8 | **TELEOP CLASSIFIED onto a matching index** | 3 + 2 = **5** | 4.2 | 5 × 0.60 ÷ 4.2 | **0.71** | yes (×9 max) |
| 9 | **TELEOP CLASSIFIED, non-matching (Cycle L)** | **3** | 4.2 | 3 × 0.60 ÷ 4.2 | **0.43** | yes |
| 10 | **TELEOP CLASSIFIED, non-matching (Cycle N)** | **3** | 5.9 | 3 × 0.85 ÷ 5.9 | **0.43** | yes |
| 11 | **TELEOP OVERFLOW** | **1** | 4.2 | 1 × 0.60 ÷ 4.2 | **0.14** | yes — *and it feeds the opponent* |

**Reading of the table `[DERIVED]`:** rows 1–4 all sit between 2.5 and 3.2 pts/s and rows 9–11 sit between
0.14 and 0.43. **There is a 6-to-20× gap between the cheap achievements and the cycling achievements.** A
programme that lands LEAVE, a clean AUTO, a disciplined GATE routine and a reliable double-BASE collects
more points per second than one that out-cycles it — right up until the cheap achievements run out of cap.
They do: LEAVE caps at 6, BASE caps at 30, PATTERN caps at 36. After ~72 points the only thing left is
cycling at 0.43 pts/s.

### 3.4 Where the GATE-open time comes from

`[DERIVED]` From the Cycle-L shooting spot (72,24) to the GATE ZONE (140,70): √(68² + 46²) = 82 in ÷ 36 =
2.3 s out, 2.3 s back, plus ~2.4 s to push and **hold**. §9.8.3 orange box `[MANUAL, non-binding]`: "The
GATE will take variable amounts of time to close… teams should be prepared to **hold the GATE open** to
fully clear the RAMP." Total ≈ **7.0 s**. §9.8.3 also gives the mechanism spec for free: the contact area is
3.75–5.5 in above the TILE, the throw is ~2 in horizontal, and the orange box tells you to build a flat
vertical plate up to 5.5 in. **This is the cheapest mechanism in the game and it is worth 2.57 pts/s.**

---

## 4. THE POINT BUDGET

### 4.1 Structural ceilings (per ALLIANCE, per MATCH)

| Bucket | Ceiling | Operands `[DERIVED]` |
|---|---:|---|
| LEAVE | **6** | 3 pts × 2 ROBOTS |
| AUTO PATTERN | **18** | 9 indices × 2 pts |
| TELEOP PATTERN | **18** | 9 indices × 2 pts |
| **PATTERN total** | **36** | 18 + 18 (contingent on §2.3 — halves to 18 if the Q&A says otherwise) |
| BASE | **30** | 10 + 10 + 10 bonus |
| AUTO ARTIFACT | **27 + overflow** | 9 CLASSIFIED × 3 (RAMP capacity), everything beyond at 1 |
| **AUTO period ceiling** | **51 + overflow** | 6 LEAVE + 27 CLASSIFIED + 18 AUTO PATTERN |
| TELEOP ARTIFACT / DEPOT | **uncapped** | bounded by shot rate and the recirculation loop, not by the rules |

### 4.2 A realistic MATCH for *this* programme — bottom-up

**AUTO (30 s).** `[JUDGMENT]` Both ROBOTS start at F6 touching the red GOAL (G304.B), fire 3 preloads each
at short range, one ROBOT then collects one SPIKE MARK set on its own side (G402 confines AUTO to columns
D, E, F for red) and fires again.

```
LEAVE                    2 ROBOTS × 3 pts                       =  6
CLASSIFIED               6 made × 3 pts                         = 18
AUTO PATTERN             4 matching indices × 2 pts             =  8
                                                          AUTO  = 32
```

**TELEOP (120 s).** `usable = 120 − 5 (startup) − 10 (BASE parking) = 105 s`. One ROBOT also does GATE
duty twice: `105 − 14 = 91 s`.

```
ROBOT A   N_cycles = floor(105 ÷ 12.7) = 8    8 × 1.8 made = 14.4 ARTIFACTS
ROBOT B   N_cycles = floor( 91 ÷ 12.7) = 7    7 × 1.8 made = 12.6 ARTIFACTS
alliance  (14.4 + 12.6) × 0.85 LOADING-ZONE congestion [JUDGMENT] = 23 ARTIFACTS
```

RAMP accounting `[DERIVED]` — AUTO left 6 on the RAMP, so TELEOP tops it to 9, opens the GATE, refills 9,
opens again, refills 9:

```
CLASSIFIED     3 (top-up) + 9 + 9 = 21    × 3 pts  = 63
OVERFLOW       23 − 21 = 2               × 1 pt   =  2
TELEOP PATTERN 6 of the final 9 indices match × 2  = 12
BASE           1 fully (10) + 1 partially (5)      = 15
                                            TELEOP = 92
```

```
MATCH TOTAL = AUTO 32 + TELEOP 92 = 124
```

### 4.3 The same number, top-down from the manual's own thresholds — a cross-check

`[DERIVED]` Table 10-3 tells you what FIRST thinks "good" looks like at a Qualifier: 36 ARTIFACTS through
the SQUARE, 18 PATTERN points, 16 combined LEAVE + BASE. Price that alliance:

```
36 ARTIFACTS = 27 CLASSIFIED (three RAMP fills) × 3 = 81
             +  9 OVERFLOW                     × 1 =  9
PATTERN RP threshold                                = 18
MOVEMENT RP threshold (LEAVE 6 + one full BASE 10)  = 16
                                              TOTAL = 124
```

**Both routes land on 124.** `[JUDGMENT]` Treat that as *reassuring, not confirming* — the two paths share
the same 3-pt CLASSIFIED assumption and differ in their CLASSIFIED fraction (93 % bottom-up vs 75 %
top-down), so the agreement is partly coincidence. But it clears the protocol's §3.4 guard: the model does
not say a rookie-legal robot wins by a factor of three. **Plan for a realistic winning score at a Qualifier
of 100–140.** `[JUDGMENT]`

### 4.4 Fractions of a realistic 124-point MATCH

| Period | Points | Share | Seconds | pts/s of period |
|---|---:|---:|---:|---:|
| **AUTO** | 32 | **26 %** | 30 (20 % of play) | 32 ÷ 30 = **1.07** |
| **TELEOP cycling + PATTERN** (0:00–1:50) | 77 | **62 %** | 110 | 77 ÷ 110 = **0.70** |
| **"Endgame" — BASE, last ~10 s** | 15 | **12 %** | 10 | 15 ÷ 10 = **1.50** |

**`[DERIVED]` AUTO is 26 % of the score in 20 % of the clock, and its ceiling is 51 points — 41 % of a
realistic winning score.** No other 30 seconds of this game is worth that much. The reason is §2.3: an AUTO
PATTERN placement is the only action in the game that gets paid twice.

If the Q&A kills the double count, recompute: AUTO drops to 32 − 8 = 24 of 116 = **21 %**, AUTO ceiling
drops to 51 − 18 = 33 of ~116 = **28 %**, and AUTO stops being special.

---

## 5. RANKING POINTS AND THE FULL TIEBREAKER LADDER

### 5.1 How RP become rank

`[MANUAL]` §13.6.3: "RANKING POINTS (RP) are units credited to a team based on their ALLIANCE'S performance
in Qualification MATCHES… A team's **RANKING SCORE (RS) is the average number of RANKING POINTS earned by a
team** throughout their Qualification MATCHES (excluding any SURROGATE MATCH)… A MATCH in which a team is
DISQUALIFIED contributes 0 to all sort criteria."

`[MANUAL]` §13.7: "Teams do not earn RANKING POINTS" in the Playoffs.

**The 60-second test (`ANALYSIS-PROTOCOL.md` §3.3 Q5) — *is there any way to earn RP other than winning?*
YES: three of them, worth 1 each, against 3 for a WIN.** `[DERIVED]` Winning is worth as much as all three
achievement RPs put together; a 6-RP match requires the win *and* a clean sweep.

### 5.2 RP conditions, priced

| RP | Condition (Table 10-2) | Threshold, All Other Events (Table 10-3) | What it actually costs `[DERIVED]` |
|---|---|---:|---|
| **MOVEMENT** | Combined LEAVE + BASE points ≥ threshold | **16** | LEAVE 3 + 3 = 6, then **either** one ROBOT fully returned (10) → 16 **or** both partially returned (5 + 5) → 16. **A drivetrain and nothing else.** |
| **PATTERN** | PATTERN points ≥ threshold | **18** | 9 matching indices across the two assessments — e.g. 4 in AUTO (8) + 5 in TELEOP (10) = 18. Half the 36 ceiling. |
| **GOAL** | ARTIFACTS through the SQUARE ≥ threshold | **36** | **36 ARTIFACTS — the entire field's supply.** 36 ÷ 150 s = one every **4.2 s** sustained by two ROBOTS, i.e. one every 8.3 s each. Our modelled alliance manages 6 + 23 = **29**. |
| **WIN / TIE** | more / equal MATCH points | — | 3 RP / 1 RP |

**`[DERIVED]` The headline mispricing: MOVEMENT RP and GOAL RP are worth exactly the same 1 RP.** MOVEMENT
needs 16 points of the two cheapest achievements in the game. GOAL needs 36 ARTIFACTS through the SQUARE —
by §3.3 row 9 that is 36 × 4.2 s = 151 seconds of *pure* cycling, which is the entire match with zero time
for AUTO setup, GATE opens or BASE parking, at a 100 % make rate. **GOAL RP is not reachable by this
programme and should be treated as an opponent's problem, not a target.**

**`[DERIVED]` GOAL RP and PATTERN RP are *not* in conflict, contrary to first impression.** GOAL RP counts
ARTIFACTS cumulatively as they pass the SQUARE; opening the GATE never un-counts them. PATTERN is only
assessed at two instants. So the correct play is: **open the GATE freely for the first ~100 seconds to keep
every ARTIFACT at 3 points instead of 1, then stop opening it and spend the last ~9 shots building the MOTIF.**
The only real constraint is discipline about the final fill and about AUTO (never open the GATE in AUTO —
it forfeits the end-of-AUTO PATTERN assessment).

### 5.3 The tiebreaker ladders, in full

**Qualification ranking — Table 13-1 (`TABLES.md` p.162):**

| Sort | Criterion |
|---:|---|
| 1st | RANKING SCORE (RS) |
| 2nd | Average ALLIANCE MATCH points, **not including MINOR FOULS and MAJOR FOULS** |
| 3rd | **Average BASE points** |
| 4th | **Average AUTO points** |
| 5th | Random sort by the FIRST event management software |

**`[DERIVED]` BASE is the 3rd sort — ahead of AUTO.** Its 30-point face value understates it: a consistent
double-BASE is simultaneously (a) 30 match points at 3.0 pts/s, (b) most of the MOVEMENT RP, and (c) the
first tiebreaker anyone actually reaches. For a two-robot programme where both robots must do the same
thing, that is an unusually high return on one mechanism.

**`[DERIVED]` Sort 2 excludes FOULS.** You are not rewarded in the tiebreaker for points the opponent handed
you, but MAJOR FOULS you *commit* still cost your opponent nothing in sort 2 — they only move the win/loss.
FOUL avoidance protects the RS (sort 1) via wins, not sort 2.

**Playoffs — §13.7:** double elimination, upper/lower bracket, "once they lose 2 total MATCHES, they are out."
`[MANUAL]` "**Ties play another MATCH until the MATCH results in 1 winner.**" No RP. **T705** `[MANUAL]`:
"if an ALLIANCE is DISQUALIFIED, the DISQUALIFIED ALLIANCE loses; if both are DISQUALIFIED, the one that is
DISQUALIFIED first chronologically loses; if… simultaneously DISQUALIFIED, the MATCH results in a tie."

**FIRST Championship da Vinci round robin — Table 15-3 (`TABLES.md` p.181):** Championship Score (CS) →
average ALLIANCE MATCH points excluding FOULS → **average BASE points** → **average AUTO points** → random.
Identical shape to Table 13-1. **C501** `[MANUAL]` governs DQ there.

**Advancement — Table 4-2 (`TABLES.md` p.26), the 10-deep ladder that decides who moves on:**

| Sort | Criterion |
|---:|---|
| 1st | Total Advancement Points (Table 4-1) |
| 2nd | Judged Team Award Points |
| 3rd | Playoff Advancement Points |
| 4th | ALLIANCE Selection Results Points |
| 5th | Qualification Phase Performance Points |
| 6th | Average Qualification MATCH Points (excluding FOULS) |
| 7th | **Average Qualification AUTO Points** |
| 8th | Highest individual Qualification MATCH Points (excluding FOULS) |
| 9th | Second Highest individual Qualification MATCH Points (excluding FOULS) |
| 10th | Random Selection by Event Management System |

`[MANUAL]` Table 4-1 weights: Inspire 1st = **60** advancement points; Playoff Winners = **40**; ALLIANCE
lead = 21 − lead number; qualification rank = 16 down to 2. `[DERIVED]` **The judged-award leg outweighs the
playoff leg 60 to 40 and is the 2nd sort.** The scoring model is not the whole advancement model — but AUTO
points appear as a sort in *both* ladders (Table 13-1 sort 4, Table 4-2 sort 7), which is a second, independent
reason to over-invest in the 30-second routine.

---

## 6. BEST POINTS-PER-SECOND, AND WHAT IS UNDERPRICED

### 6.1 Best points-per-second

**Repeatable:** **an AUTO CLASSIFIED shot that lands on a MOTIF-matching index — 3.13 pts/s** (§3.3 row 1),
because it is the only action paid three times from one trigger pull: 3 CLASSIFIED + 2 AUTO PATTERN + 2
TELEOP PATTERN = 7 points for 1.9 seconds of AUTO. Its ceiling is 9 shots.

**One-shot:** **both ROBOTS fully returned to BASE — 3.00 pts/s** (30 points for the last 10 seconds), tied
with **LEAVE** at 3.00 pts/s (6 points for 2 robot-seconds that were on the path anyway).

**Best non-scoring action:** **opening your own GATE — 2.57 pts/s of enabled value** (§3.3 row 3). It scores
nothing itself and is worth more per second than any TELEOP cycle.

**Worst:** **OVERFLOW at 0.14 pts/s**, and it is worse than the number says — see §6.3.

### 6.2 The most underpriced objective: **PATTERN**

`[DERIVED]` Ranked by (points available) ÷ (engineering effort for a 15-student, no-CNC, two-robot programme):

| Rank | Objective | Points available | Marginal build cost over a plain shooter |
|---:|---|---:|---|
| **1** | **PATTERN** | **36** (29 % of a realistic 124-pt win) + 1 RP | **A colour sensor and shot-order logic.** No new mechanism. |
| 2 | LEAVE | 6, and 6 of the 16 needed for MOVEMENT RP | One line of AUTO code. |
| 3 | GATE operation | +18 enabled per open, ~2 opens/match = +36 | A flat plate 5.5 in tall (§9.8.3 gives the spec). |
| 4 | BASE, partial | 5 per ROBOT | Overlap a tape line and stop. |
| 5 | BASE, full ×2 + bonus | 30, and the 3rd ranking sort | Positioning accuracy — see §6.4. |

**Why PATTERN is underpriced.** Table 10-2 prices a matching ARTIFACT at 2 points against a CLASSIFIED
ARTIFACT's 3, which *reads* as a minor bonus. It is not:

1. It is paid **twice** (§2.3), so the real rate is 4 points per ARTIFACT held for the whole match, not 2.
2. Its ceiling is **36 points** — larger than the BASE ceiling (30) and larger than the entire AUTO ARTIFACT
   ceiling (27).
3. The marginal cost is **zero travel**. Every PATTERN point rides on a shot you were taking anyway. Compare
   §3.3 rows 8 and 9: colour discipline lifts a TELEOP cycle from 0.43 to **0.71 pts/s — a 65 % improvement
   with no change to the drivetrain, the intake or the launcher.**
4. The supply ratio cooperates: 24 P : 12 G on the field, 2 P : 1 G in every MOTIF (§1.5). You never run out
   of the colour you need.
5. It carries an RP whose threshold (18 of a 36 ceiling) is 50 %, versus GOAL RP's 36-of-36.

**The cost is a sequencing problem, not a mechanism problem** — read AprilTag 21/22/23 off the OBELISK
(§9.10; the manual warns the OBELISK "is not recommended for ROBOT navigational use," so read it for the
MOTIF only), then fire a fixed colour sequence starting at index 1. That is exactly the kind of work a
software-heavy, hardware-light, two-robot programme can duplicate for free on the second robot.

**Risk to the claim:** the whole case rests on the double-count in §2.3. **Q&A question #1 is the highest
priority item on the entire kickoff list.**

### 6.3 The most overpriced objectives — the traps

**OVERFLOW.** 1 point at 0.14 pts/s, *and* §9.8.3 says OVERFLOW ARTIFACTS "pass over the top of the GATE to
exit the RAMP into the opposing ALLIANCE'S SECRET TUNNEL ZONE," which Figure 9-3 shows terminating at the
opponent's LOADING ZONE. `[DERIVED]` **An OVERFLOW ARTIFACT scores you 1 point and hand-delivers a
3-point opportunity to your opponent's human player.** Its true value is closer to 1 − (0.6 × 3) = **−0.8
points**. Never shoot into a full RAMP. Open the GATE, or hold the ball.

**DEPOT.** Also 1 point — but §10.5.1 `[MANUAL]`: "To qualify for DEPOT points, ARTIFACTS must be over the
DEPOT… DEPOT points are assessed after the MATCH without regard to which ALLIANCE placed the ARTIFACTS in
the DEPOT. DEPOTS are not protected zones, and either ALLIANCE can remove ARTIFACTS from either DEPOT
during the MATCH." `[DERIVED]` DEPOT is worth the same 1 point as OVERFLOW **and does not resupply the
opponent** — so with a full RAMP and no time to open the GATE, dumping in your DEPOT strictly dominates
shooting. But it is unprotected and un-owned: an opponent can clear your DEPOT, and can *feed* your DEPOT
by accident. Treat it as a last-30-seconds dump, never as a strategy. Its physical capacity (30 in of tape,
5 in ARTIFACTS) is **UNVERIFIED** — the manual sets no numeric cap.

**GOAL RP.** See §5.2. 36 ARTIFACTS for the same 1 RP that 16 points of LEAVE + BASE buys.

### 6.4 One geometry finding that changes the BASE mechanism

`[MANUAL]` §9.3: the BASE ZONE is **18 in × 18 in**, and there is **one per ALLIANCE**. **R105.A**: a ROBOT
"must remain within a fixed 18 in. (45.70 cm) by 18 in." So two full-size ROBOTS cannot both stand in the
box.

But `[MANUAL]` §10.5.3: "A ROBOT fully returned to BASE must **only be supported, either directly or
transitively**, by the TILE in the BASE ZONE," and the accompanying orange box (`[MANUAL, non-binding]`,
illustrating binding §10.5.3 prose) reads: "Support comes, either directly or **transitively through other
items on the FIELD (e.g., SCORING ELEMENTS, another ROBOT)**, through the TILE in the BASE ZONE."

`[DERIVED]` **The 10-point "2 ROBOTS fully returned" bonus is a robot-on-robot support problem.** ROBOT A
parks inside the 18-in box; ROBOT B's entire support path runs through ROBOT A. **G415** independently
permits expansion to 38 in "during the final 20 seconds of the MATCH" and "when not in any LAUNCH ZONES" —
and the BASE ZONE at B2 is not in a LAUNCH ZONE. The rules are pointing at a lift or a ramp, deployed in
the last 20 seconds, in the BASE ZONE.

`[DERIVED]` The alternative for a two-robot programme with modest tooling: build both ROBOTS **≤ 9 in wide**
so both fit side by side in the 18-in box. Note that only the *support* must be inside — wheel contact
patches, not the frame — so an 18-in ROBOT with inboard wheels may already have ~16 in of contact span and
need only ~2 in of parking accuracy. **Measure this on a taped 18-in square in week 1.**
**[prior-knowledge agreement — not used as evidence]**

---

## 7. WHAT THIS GAME REWARDS — in plain language

This is a **shooting game with a memory**. You cannot lift a ball into the goal — the lip is 38.75 inches and
the rules keep you at 18 inches for all but the last twenty seconds — so every point starts as a shot fired
from a taped zone. But the goal is not just a bucket. Underneath it is a nine-slot ramp, and the game keeps
looking at what is sitting in that ramp: once at the end of autonomous, and once again at the end of the
match. Balls that happen to land in the right colour order, in the order the obelisk randomly picked before
the match, get paid both times. So the game does not reward volume so much as **volume plus order**. The
team that fires forty balls at random beats nobody; the team that fires twenty-five in a known colour
sequence and leaves nine of them sitting correctly at 0:00 wins comfortably.

The second thing the game rewards is **cheapness**. Rolling off a tape line is three points a robot. Parking
in an eighteen-inch square at the buzzer is ten, and thirty if both robots manage it, and it is the third
ranking tiebreaker on top. Pushing a small green lever to dump your ramp costs seven seconds and turns your
next nine balls from one point each into three. All three of those are worth more per second than actually
driving balls up the field, and none of them needs a machine shop. A fifteen-student team with a printer and
hand tools should build a very reliable shooter, a colour sorter that lives mostly in software, a flat plate
that opens a gate, and a way to get both robots into one small square — and should stop there. That list is
duplicable twice, which is the whole point.

The third thing to understand is that **the field is a loop, and it runs through your opponent.** Your goal
is diagonally opposite your own loading zone, and everything you score rolls out of your ramp and down the
wall into the *other* alliance's loading zone, where their human player picks it up and hands it back to
their robots. The more you score, the better you supply them. That is why the one-point actions matter more
than one point suggests: an overflow ball scores you one and gifts them three, while a ball dropped in your
own depot scores the same one and gifts them nothing.

Finally, the game punishes **touching things that are not yours** far harder than it rewards defence. Fifteen
points per ball for reaching into a ramp — including your own. Fifteen points plus a handed-over ranking
point for touching the wrong gate. Fifteen points plus up to twenty points of free base scoring for bumping
somebody in their base zone in the last twenty seconds. The whole penalty structure says: play your own
field, shoot your own colours, park cleanly, and let the other alliance make the mistakes.

---

## 8. OPEN QUESTIONS — for `D0-open-questions.md` and the Game Q&A

| # | Question | Why it matters | Status |
|--:|---|---|---|
| **1** | **Are AUTO PATTERN and TELEOP PATTERN points additive for the same ARTIFACT?** (§2.3) | Doubles or halves the PATTERN ceiling; changes AUTO from 41 % of the score to 28 % | `[DERIVED]` yes, from 22 > 18 — **not stated in words** |
| 2 | Is there a cap on the number of ARTIFACTS that can score DEPOT points? "over the DEPOT" is not given a volume | Prices the endgame dump | **UNVERIFIED** |
| 3 | Does an ARTIFACT that leaves the RAMP through the GATE and is re-scored through the SQUARE count a second time toward GOAL RP? | Decides whether GOAL RP = 36 is reachable at all | **UNVERIFIED** — Table 10-2 says only "the number of ARTIFACTS scored through the SQUARE" |
| 4 | Does a ROBOT sitting on the DEPOT tape at the end of AUTO forfeit LEAVE? §9.3 says "The DEPOT tape **is a LAUNCH LINE**"; §10.5.3 requires being "no longer over **any** LAUNCH LINE" | Costs 3 points per ROBOT for a robot that parks at its own goal | `[DERIVED]` yes, it forfeits — worth confirming |
| 5 | For "fully returned to BASE," is the test the ROBOT's support (contact patches) or its projected footprint? | Decides whether an 18-in ROBOT can ever be "fully" returned | `[DERIVED]` support, per §10.5.3 wording — worth confirming |
| 6 | If the GATE is open at 0:00 but ARTIFACTS are still on the RAMP at rest, are they "retained by the GATE" per §10.5.2? | The G203/G204 examples imply no; the wording is not explicit | **UNVERIFIED** |
| 7 | Do the "All Other Events" RP thresholds apply to League Meets and League Tournaments? | Section 14 (League Play, V1) not reviewed in R3 | **UNVERIFIED** — R3b/R5 scope |

---

## Beta feedback

**What the harness got right.** `TABLES.md` fully earned its keep: Table 10-2 came out of the geometry
extractor with every value on its correct row, and the `figures/p088` render confirmed it cell-for-cell.
The `full_layout.txt` rendering of the same table is genuinely unusable — it prints the row labels
`LEAVE / ARTIFACT / PATTERN / BASE` in a block and then floats `3 3 3 1 1 2 2 5 10 10` underneath in a
separate column, exactly as `ANALYSIS-PROTOCOL.md` §3.1 warns. Rule 6 of the house rules is load-bearing and
was validated. `rules_full.tsv` with the `violation` column split out is the single most useful file in the
bundle; §1.4 of this document would have taken an hour without it.

**Things that were wrong, missing, or made the work harder:**

1. **`bundle/TABLES.md` has no Section 8/9/10 *prose*, so the critical-path question could only be answered
   from the "last resort" file.** The §10.5 A–F assessment list — the single most important passage in the
   manual for R3, and the thing question 2 of my task asks about — is body prose, not a table and not a
   numbered rule, so it appears in **neither** `TABLES.md` **nor** `rules_full.tsv`. I had to read it out of
   `full_layout.txt`, which the STATUS.md feed order labels "last resort." The house rule "never take point
   values from full_layout" is right, but the bundle currently gives no *sanctioned* home for scoring
   **criteria**. **Fix: emit `bundle/SCORING_PROSE.md` — Sections 8, 10.1, 10.4, 10.5.x and 9.6–9.9 verbatim,
   extracted by geometry like the tables are.** Without it, R3's most important answer is sourced from the
   file the protocol tells you not to trust.

2. **`rules_full.tsv` truncates rule bodies into the following section's text.** Several bodies run past the
   rule and swallow the next heading: G402's body ends `"G402.B. 11.4.2TELEOP"`, G404's begins with a stray
   `"."` and ends `"11.4.3SCORING ELEMENT"`, and **G434's body contains the entire opening of Section 12 plus
   the complete 16-page Glossary** — several thousand words. The violation strings are similarly clipped
   mid-sentence (G402: `"MAJOR FOUL per ARTIFACT in"` — the object of the sentence is gone; G419: `"...if"`
   with nothing after it). It was recoverable here, but on a real kickoff a truncated violation clause is
   exactly the kind of thing that gets mis-cited. **Fix: bound each rule body at the next rule id or the next
   `\d+\.\d+` section heading.**

3. **No `bundle/GLOSSARY.md`.** The Section 16 glossary is where CLASSIFIED, OVERFLOW, MOTIF, PATTERN, LEAVE,
   BASE, CONTROL and LAUNCH are actually defined, and it is the fastest way into a brand-new game. I found it
   only by accident, buried inside the over-long G434 body in `rules_full.tsv`. It should be a first-class
   bundle file listed in the feed order.

4. **`caps_NOVEL_ranked.txt` is polluted with parser noise and the stoplist is leaking.** The list mixes real
   game vocabulary (ARTIFACTS 87, GATE 65, GOAL 58) with OCR fragments and part numbers — `NADO`, `NZS`,
   `NMH`, `HLS`, `DFR`, `SKU`, `BNO`, `JST`, `IEC`, `VDC`, `CDT`, `OAK`, `GPT`, `DECODETM`, and the manual's
   own typo `ARTFACTS`. It also lists `WIN`, `TIE`, `RESULTS`, `LIMITS`, `AIM`, `AGE` as "novel game
   vocabulary." Everything below about frequency 4 was noise. **Fix: drop tokens with count < 5 by default,
   and extend the stoplist with the electronics-vendor acronyms.**

5. **No field-geometry summary; I had to measure the field off PNGs by eye.** §3.1 of this document — the
   coordinates that every points-per-second number divides by — was reconstructed by reading tile columns off
   `figures/p063` and estimating landmark centres from pixel positions in `figures/p061`. That is the least
   reliable step in the whole analysis and it feeds *everything*. **Fix: `bundle/GEOMETRY.md` listing every
   named zone with its dimensions and its TILE coordinate, harvested from the §9.3 bullet list (which already
   gives exact dimensions in text) plus the Figure 9-5 grid.** Alternatively, ingest the field CAD.

6. **The label vocabulary conflicts between the task and the protocol.** My task mandates
   `[MANUAL] / [DERIVED] / [JUDGMENT] / UNVERIFIED`; `ANALYSIS-PROTOCOL.md` §0.1 and
   `STRATEGY-RANKING-PROTOCOL.md` §0.2 mandate `[C] / [H] / [J] / [M] / [E] / [U]`. These are not
   interchangeable — the protocol's set distinguishes MEASURED from ESTIMATED, which is a real distinction
   my label set collapses (every cycle time in §3 is `[JUDGMENT]` here but would be `[E]` there, and the
   protocol's ×1.3 pessimism rule keys off that label). I used the task's set and applied the ×1.3 rule
   anyway. **Fix: pick one vocabulary, or publish the mapping.**

7. **`ANALYSIS-PROTOCOL.md` §3 is not runnable under the beta rules.** Its R3 step routes through
   `SCORING-PATTERNS.md` five times — §B.1 clock precedents, §B.5, §B.8 historical pts/s bands, §B.10
   pre-load, §B.11 the score-inflation curve, and most importantly **"Then answer the pre-written 18
   questions in `SCORING-PATTERNS.md` §C.2"**, which is a mandatory done-criterion. That file is on the
   forbidden list. The §3.4 guard ("a realistic winning score… §B.11 has the historical inflation curve") is
   likewise unusable. I substituted the manual's own RP thresholds as the calibration source (§4.3), which
   worked well and is arguably *better* because it is game-internal rather than historical — but that was an
   improvisation, not the protocol. **Fix: either move the game-agnostic §C.2 question list into a separate
   method file, or write the 18 questions into `ANALYSIS-PROTOCOL.md` directly.**

8. **The protocol's output path and my task's output path disagree.** §0 says "R3's artifact is exactly D0's
   `analysis/kickoff/D0-scoring-table.md`"; my task specified `R3-scoring-model.md`. I wrote the task's path.
   Downstream steps that glob for `D0-scoring-table.md` will not find this file.

9. **`STATUS.md` and `figures/MANIFEST.txt` disagree about what was ingested.** STATUS.md names
   `DECODE_Competition_Manual_TU32.pdf`; MANIFEST.txt says "rendered from
   `BIOBUZZ_Competition_Manual_KICKOFF.pdf` (188 pages)"; `TABLES.md`'s header says
   `BIOBUZZ_Competition_Manual_KICKOFF`. For a harness whose central discipline is "never confuse this
   season's manual with last season's," having three filenames for one artefact inside one bundle is the
   exact failure mode the discipline exists to prevent. **Fix: stamp one provenance line, from one source,
   into every generated file.**

10. **Minor: `TABLES.md` repeats a caption across unrelated tables.** Three consecutive blocks on p.91 are all
    labelled "Table 10-6: Violation examples" when p.90–91 actually hold Table 10-5 plus continuation rows,
    and Table 10-1 appears three times for p.80. Caption inheritance is running past the table it belongs to.
    Cite-by-page rather than cite-by-caption is the safe workaround, which is what §1.3 of this file does.

11. **Nothing in the bundle flags rules that pay in RP rather than points.** §1.4 here is the most
    strategically important table in this document and I built it by grepping `VIOLATIONS.tsv` for the string
    "RP". Six rules can hand your opponent a ranking point or strip yours, and no points-based model can
    price them. **Fix: `VIOLATIONS.tsv` should carry a boolean `affects_rp` column.**
