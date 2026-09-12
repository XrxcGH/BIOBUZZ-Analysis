# R5 — G-rules and penalty exposure

**Phase:** R5 (ANALYSIS-PROTOCOL.md §6) · **Run:** 2026-08-23 · **Manual:** ingested bundle, 188 pp, 214 rules, 53 G-rules, 17 orange (STATUS.md)
**Sources used:** `bundle/rules_full.tsv`, `bundle/VIOLATIONS.tsv`, `bundle/rules_GAMESPECIFIC.txt`, `bundle/TABLES.md` (all point values), `bundle/ORANGE_BOXES.md` (non-binding, flagged as such), `bundle/full_layout.txt` (glossary + two truncated Violation strings only — **no point values**).
**Bundle availability:** `tools/RUN-KICKOFF.sh` generated the bundle locally from `DECODE_Competition_Manual_TU32.pdf`; it is not published with this repository, because it is FIRST's manual text. Page and table numbers refer to the manual; `L` numbers are lines of the generated `full_layout.txt`.
**Method files consulted:** `reference/ANALYSIS-PROTOCOL.md` §6 only.
**Deliberately NOT opened:** `reference/PENALTY-AND-ENFORCEMENT.md`, `reference/SCORING-PATTERNS.md`, `research/LOOPHOLE-CASEBOOK.md`, `reference/ROBOT-ARCHETYPE-LIBRARY.md`, `manuals/_reference_prior_seasons/`. See Beta feedback #1 — one allowed method file leaked answers anyway.

**Label key:** `[MANUAL]` = read directly from the bundle with a citation · `[DERIVED]` = arithmetic on manual numbers, operands shown · `[JUDGMENT]` = my inference, arguable · `[UNVERIFIED]` = I could not find it and did not invent it.

---

## 0. The two numbers everything else hangs on

| Tier | Value | Source |
|---|---|---|
| MINOR FOUL | **a credit of 5 points toward the opponent's MATCH point total** | [MANUAL] TABLES.md p.89 Table 10-4 |
| MAJOR FOUL | **a credit of 15 points toward the opponent's MATCH point total** | [MANUAL] TABLES.md p.89 Table 10-4 |
| YELLOW CARD | warning; **a subsequent YELLOW CARD within the same tournament phase results in a RED CARD** | [MANUAL] TABLES.md p.89 Table 10-4 |
| RED CARD | team is **DISQUALIFIED for the MATCH** | [MANUAL] TABLES.md p.89 Table 10-4 |
| DISQUALIFIED | **0 MATCH points and 0 RANKING POINTS** in a Qualification MATCH; causes the ALLIANCE to receive 0 MATCH points in a Playoff MATCH | [MANUAL] TABLES.md p.89 Table 10-4 |
| DISABLED | REFEREE instructs the team to stop the ROBOT — inoperable for the remainder of the MATCH | [MANUAL] TABLES.md p.89 Table 10-4 |
| ALLIANCE ineligible for RP | overrides any RP awarded through normal MATCH play | [MANUAL] TABLES.md p.89 Table 10-4 |

**Duration vocabulary** [MANUAL] glossary, recovered via `full_layout.txt` L2865–2867 and confirmed in the C501 body dump of `rules_full.tsv`:

- **MOMENTARY** — fewer than approximately **3 seconds**
- **CONTINUOUS** — more than approximately **10 seconds**
- **REPEATED** — actions that happen **more than once within a MATCH**

**Scoring baseline for pricing** [MANUAL] TABLES.md p.88 Table 10-2:
LEAVE 3 (AUTO) · ARTIFACT CLASSIFIED 3 (AUTO) / 3 (TELEOP) · OVERFLOW 1 / 1 · DEPOT 1 (TELEOP) · PATTERN (matches MOTIF) 2 / 2 · BASE partial 5 · BASE full 10 · both-ROBOTS-fully-returned bonus +10 · WIN 3 RP · TIE 1 RP · MOVEMENT/GOAL/PATTERN RP 1 each.

**MATCH structure** [MANUAL] glossary: 30 s AUTO + 8 s transition + 2:00 TELEOP; "Final 20 seconds" audio cue at 0:20 (TABLES.md p.77 Table 9-1). ALLIANCE = 2 teams (glossary). 5 or 6 Qualification MATCHES per team (full_layout L5939).

---

## 1. Every G-rule (all 53)

Column *Scope* is the parser's own class tag from `rules_full.tsv` field 3. **15 of 53 G-rules are GAMESPEC (orange)**; the other 2 orange rules in `rules_GAMESPECIFIC.txt` are R105 and C501, outside the G series.

### 11.1 Personal Safety

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G101 | Humans, stay off the FIELD during the MATCH | DRIVE TEAM entering the FIELD except pre-MATCH setup (G301/G303/G304) and post-MATCH retrieval when instructed | VERBAL WARNING | EVERGREEN |
| G102 | Be careful when interacting with ARENA elements | climbing on / hanging from / deforming / damaging ARENA elements | VERBAL WARNING → YELLOW CARD on subsequent violations **during the event** | EVERGREEN |

### 11.2 Conduct

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G201 | Be a good person | incivility toward people or equipment | VERBAL → YELLOW (event) | EVERGREEN |
| G202 | DRIVE TEAM Interactions | distracting/interfering with the opposing ALLIANCE; taunting | VERBAL → YELLOW (event) | EVERGREEN |
| G203 | Asking other teams to throw a MATCH | encouraging a non-ALLIANCE-mate to play beneath ability | VERBAL → **RED** (event) | EVERGREEN |
| G204 | Letting someone coerce you | playing beneath ability as a result of such encouragement | VERBAL → **RED** (event) | EVERGREEN |
| G205 | Throwing your own MATCH | intentionally losing / sacrificing RP to manipulate rankings | VERBAL → **RED** (event) | EVERGREEN |
| G206 | Don't violate rules for RPs | colluding to purposefully violate a rule to influence RP | **YELLOW CARD + ALLIANCE ineligible for PATTERN and GOAL RPs** | EVERGREEN |
| G207 | Do not abuse ARENA access | badged non-DRIVE-TEAM members assisting/coaching/signalling | VERBAL → YELLOW (event) | EVERGREEN |
| G208 | Show up to your MATCHES | not sending ≥1 DRIVE TEAM member to an assigned Qual MATCH | **DISQUALIFIED** from the current MATCH | EVERGREEN |
| G209 | Keep your ROBOT together | intentionally detaching or leaving a part on the FIELD | **RED CARD** | EVERGREEN |
| G210 | Do not expect to gain by doing others harm | actions clearly aimed at forcing the opponent to violate a rule | MINOR → **MAJOR if REPEATED**; targeted ALLIANCE is not penalised | EVERGREEN |
| G211 | Egregious or exceptional violations | catch-all: egregious behaviour or subsequent violations of *any* rule | YELLOW **or** RED CARD, Head REFEREE discretion | EVERGREEN |
| G212 | All teams can play | encouraging another team to sit out or be DQ'd from a Qual MATCH | YELLOW; **RED if the ROBOT does not participate** | EVERGREEN |

### 11.3 Pre-MATCH

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G301 | Be prompt | causing significant delay to MATCH start (both: start time passed **and** not MATCH-ready / no good-faith effort) | Qual: VERBAL → **MAJOR FOUL for the upcoming MATCH** on a subsequent violation within the tournament phase; **DISABLED** if not ready within **2 minutes**. Playoff: same ladder applied to the ALLIANCE | EVERGREEN |
| G302 | Limit what you bring to the FIELD | extra equipment that is a hazard, **> 6 ft 6 in (~198 cm)** above the TILES, communicates outside the ARENA, blocks visibility, or jams the ARENA | MATCH won't start until remedied; **YELLOW CARD** if discovered/used inappropriately during a MATCH | EVERGREEN |
| G303 | ROBOTS on the FIELD must come ready | hazardous ROBOT; uninspected; non-I305-compliant after modification; extra team items on FIELD; wrong ROBOT SIGN colour; not motionless after init | MATCH won't start (quick remedy) / **DISABLED**; **RED CARD** if a ROBOT non-compliant with B or C participates | EVERGREEN |
| G304 | ROBOTS must be set up correctly | not over a LAUNCH LINE; not touching own GOAL or perimeter; not fully on own side (cols A–C blue / D–F red); attached to a FIELD element; outside STARTING CONFIGURATION; over the pre-load limit | MATCH won't start / **DISABLED** | EVERGREEN |
| G305 | Teams must select an OpMode | failing to select + INIT an OpMode (AUTO OpMode must have the 30 s AUTO timer enabled) | MATCH won't start / **DISABLED** | EVERGREEN |

Pre-load limit referenced by G304.F: **up to 3 ARTIFACTS per ROBOT**, pre-staged from the ALLIANCE AREA [MANUAL] full_layout L2578 §10.3.1.

### 11.4.1 AUTO

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G401 | Let the ROBOT do its thing | DRIVE TEAM interacting with ROBOT/OPERATOR CONSOLE from randomisation until end of AUTO (exceptions: MOMENTARY ▶ press, ■ stop, safety) | **MAJOR FOUL** + ALLIANCE **not eligible for PATTERN points in AUTO** if an ARTIFACT enters the open top of the GOAL after the interaction and before end of AUTO | EVERGREEN |
| **G402** | **No AUTO opponent interference** | during AUTO: (A) contacting an opponent ROBOT completely within the opponent's side (directly or transitively through an ARTIFACT); (B) disrupting a pre-staged ARTIFACT on the opponent's side, incl. by LAUNCHING into it | **MAJOR FOUL per instance of ROBOT contact (G402.A)** and **MAJOR FOUL per ARTIFACT (G402.B)** | **GAMESPEC** |

### 11.4.2 TELEOP

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G403 | ROBOTS are motionless between AUTO and TELEOP | any powered movement during the 8 s transition | **MAJOR FOUL** | EVERGREEN |
| G404 | ROBOTS are motionless at end of TELEOP | powered movement after TELEOP ends until the signal to retrieve | MINOR FOUL; **MAJOR per ARTIFACT** that enters the open top of a GOAL after TELEOP; **MAJOR** if the ROBOT contacts a GATE after TELEOP | EVERGREEN |

### 11.4.3 SCORING ELEMENT

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G405 | ROBOTS use SCORING ELEMENTS as directed | using a SCORING ELEMENT to ease/amplify a FIELD-element challenge other than as intended | **MAJOR FOUL per SCORING ELEMENT** | EVERGREEN |
| G406 | Keep SCORING ELEMENTS in bounds | intentionally ejecting a SCORING ELEMENT from the FIELD, incl. by bouncing off a FIELD element or ROBOT | **MAJOR FOUL per SCORING ELEMENT** | EVERGREEN |
| G407 | Do not damage SCORING ELEMENTS | ROBOT or human damaging an ARTIFACT | VERBAL → **MAJOR if REPEATED**; **DISABLED** if ROBOT-caused and further damage likely; corrective action / re-inspection | EVERGREEN |
| **G408** | **No more than 3 at a time** | simultaneously CONTROLling **more than 3 ARTIFACTS** | **MINOR FOUL per SCORING ELEMENT over the limit**; **YELLOW CARD if excessive** | **GAMESPEC** |

### 11.4.4 ROBOT

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G409 | ROBOTS must be under control | disrupting anything outside the FIELD / contacting a human outside the FIELD; dangerous operation | **DISABLED** + VERBAL; YELLOW if REPEATED or subsequent (event) | EVERGREEN |
| G410 | ROBOTS must stop when instructed | not pressing ■ when a REFEREE orders DISABLE per T202 | **MAJOR FOUL** if greater-than-MOMENTARY (>~3 s) delay; **RED CARD if CONTINUOUS** (>~10 s) | EVERGREEN |
| G411 | ROBOTS must be identifiable | team number / ALLIANCE colour becoming indeterminate | VERBAL → MINOR on subsequent (event) | EVERGREEN |
| G412 | Don't damage the FIELD | damaging FIELD elements | VERBAL; **DISABLED** if further damage likely; YELLOW for any subsequent damage in the event | EVERGREEN |
| G413 | Watch your ARENA interaction | grabbing / grasping / attaching to / entangling with / suspending from an ARENA element (SCORING ELEMENTS excepted, see G407) | **MAJOR FOUL** + YELLOW if REPEATED or greater-than-MOMENTARY; DISABLED if damage likely | EVERGREEN |
| **G414** | **ROBOTS have horizontal expansion limits** | exceeding R105.A horizontal limits during the MATCH (exception: damage not used for strategic benefit) | **MINOR FOUL**; **MAJOR FOUL if the over-expansion is used for strategic benefit, including if it impedes or enables a scoring action** | **GAMESPEC** |
| **G415** | **ROBOTS have vertical expansion limits, with exceptions** | exceeding R105 vertical limits; may only exceed 18 in up to 38 in when **both** (A) during the final 20 s **and** (B) not in any LAUNCH ZONE | **MINOR FOUL**; **MAJOR FOUL if used for strategic benefit / impedes or enables a scoring action** | **GAMESPEC** |
| **G416** | **LAUNCHING in the LAUNCH ZONE only** | LAUNCHING a SCORING ELEMENT while not inside a LAUNCH ZONE or overlapping a LAUNCH LINE | **MINOR FOUL per LAUNCHED SCORING ELEMENT**; **MAJOR FOUL per LAUNCHED SCORING ELEMENT that enters the open top of the GOAL** | **GAMESPEC** |
| **G417** | **ROBOTS only operate GATES as directed** | (A) contacting the opponent's GATE, directly or through a SCORING ELEMENT; (B) applying any closing force to either GATE | **MAJOR FOUL** + **opposing ALLIANCE awarded the PATTERN RP if G417.A** | **GAMESPEC** |
| **G418** | **ROBOTS may not meddle with ARTIFACTS on RAMPS** | contacting ARTIFACTS on any RAMP incl. your own; (A) removing an ARTIFACT from your own RAMP other than by operating the GATE; (B) removing one from the opponent's RAMP by any means | **MAJOR FOUL per ARTIFACT**; ALLIANCE **ineligible for PATTERN RP** if G418.A; **opposing ALLIANCE awarded PATTERN RP** if G418.B | **GAMESPEC** |
| **G419** | **ROBOTS LAUNCH into their own GOAL** | (A) intentionally placing/LAUNCHING ARTIFACTS directly onto your own RAMP; (B) placing/LAUNCHING into the opponent's GOAL or onto the opponent's RAMP | **MAJOR FOUL per ARTIFACT** + **opposing ALLIANCE awarded the PATTERN RP if G419.B** | **GAMESPEC** |

### 11.4.5 Opponent Interaction

> Manual note inside G419's body: *"G420 and G421 are mutually exclusive. A single ROBOT to ROBOT interaction which violates more than 1 of these rules results in the most punitive penalty, and only the most punitive penalty, being assessed."* [MANUAL] rules_full.tsv G419 body.

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G420 | This is not combat robotics | deliberately functionally impairing an opponent ROBOT | **MAJOR FOUL + YELLOW CARD**; **MAJOR FOUL + RED CARD if the opponent ROBOT is unable to drive**. Only 1 MAJOR FOUL per single violation (TABLES.md p.93) | EVERGREEN |
| G421 | Do not tip or entangle | deliberately attaching to, tipping, or entangling an opponent ROBOT | **MAJOR FOUL + YELLOW**; **MAJOR + RED if CONTINUOUS or opponent unable to drive** | EVERGREEN |
| G422 | There is a 3-count on PINS | PINNING an opponent ROBOT for **more than 3 seconds** | **MINOR FOUL + an additional MINOR FOUL every 3 seconds** until corrected | EVERGREEN |
| G423 | Do not shut down major parts of gameplay | isolating or closing off any major element of MATCH play for **greater-than-MOMENTARY** duration | **MINOR FOUL + an additional MINOR FOUL every 3 seconds** until corrected | EVERGREEN |
| **G424** | **GATE ZONE is OFF LIMITS** | contacting an opponent ROBOT, directly or through a SCORING ELEMENT, **if either ROBOT is in the opponent's GATE ZONE — regardless of who initiates**. Exception A: a ROBOT in its own GATE ZONE *and* in the opponent's SECRET TUNNEL ZONE is not protected | **MINOR FOUL** | **GAMESPEC** |
| **G425** | **Keep out of opponent's SECRET TUNNEL** | a ROBOT **in the opponent's SECRET TUNNEL ZONE** contacting an opponent ROBOT, directly or transitively, regardless of who initiates | **MINOR FOUL** | **GAMESPEC** |
| **G426** | **LOADING ZONE protection** | contacting an opponent ROBOT while **either ROBOT is in the opponent's LOADING ZONE**, regardless of who initiates | **MINOR FOUL** | **GAMESPEC** |
| **G427** | **BASE ZONE protection** | **during the last 20 seconds**, contacting an opponent ROBOT while either is in the **opponent's BASE ZONE**, regardless of who initiates | **MAJOR FOUL** + **the opponent ROBOT and any ROBOT fully supported by it are awarded fully returned to BASE points** | **GAMESPEC** |

### 11.4.6 Human

| ID | Headline | What it forbids | Violation tier | Scope |
|---|---|---|---|---|
| G428 | No wandering | DRIVE TEAM members leaving their designated ALLIANCE AREA; not staged inside it before MATCH start | VERBAL → MINOR on subsequent (event) | EVERGREEN |
| G429 | DRIVE COACHES: hands off the controls | anyone but that team's DRIVERS operating the ROBOT; DRIVE COACH handling gamepads (may still hold/troubleshoot the DS device and press INIT/▶/■ and select OpModes) | **MAJOR FOUL**; **YELLOW CARD if greater-than-MOMENTARY** | EVERGREEN |
| G430 | DRIVE COACHES, SCORING ELEMENTS are off limits | DRIVE COACH contacting SCORING ELEMENTS (safety excepted) | **MINOR FOUL** | EVERGREEN |
| G431 | DRIVE TEAMS, watch your reach | once a MATCH starts, a DRIVE TEAM member inside the FIELD: (A) contacting a ROBOT, (B) contacting a SCORING ELEMENT in contact with a ROBOT, (C) disrupting SCORING ELEMENT scoring, (D) contacting a FIELD element | **MAJOR FOUL + YELLOW if G431.A**; **RED CARD + opposing ALLIANCE awarded the PATTERN RP if G431.C** | EVERGREEN |
| **G432** | **Humans, only meddle with ARTIFACTS in the LOADING ZONE** | introducing/removing/moving ARTIFACTS anywhere but the LOADING ZONE; must be TELEOP-only, tool-free, may not bring an ARTIFACT *into* the LOADING ZONE from elsewhere on the FIELD, and may not let one *leave* the LOADING ZONE unless a ROBOT took CONTROL of it while in the LOADING ZONE and still CONTROLS it on exit | **MINOR FOUL per ARTIFACT**; **MAJOR FOUL per ARTIFACT that enters the open top of the GOAL** | **GAMESPEC** |
| **G433** | **Humans may only enter SCORING ELEMENTS** | DRIVE TEAM entering anything but ARTIFACTS onto the FIELD | **MINOR FOUL per non-ARTIFACT item entered onto the FIELD** | **GAMESPEC** |
| **G434** | **The ALLIANCE AREA has a storage limit** | during TELEOP, an ALLIANCE storing **more than 6 ARTIFACTS out of play** (good-faith immediate re-entry is the exception) | **MINOR FOUL per ARTIFACT over the limit** *and an additional MINOR FOUL per ARTIFACT over the limit **every 3 seconds*** until corrected | **GAMESPEC** |

---

## 2. Recurring archetypes and their numeric thresholds this season

Archetype set from `ANALYSIS-PROTOCOL.md` §6 pass 2 plus the seven the task named. **Every number in this table is [MANUAL] with the cited rule.**

| Archetype | Rule(s) | The number | Notes / gotchas |
|---|---|---|---|
| **Control limit (elements at once)** | **G408** | **3 ARTIFACTS** simultaneously CONTROLled | CONTROL = fully supported by / stuck in-on-under the ROBOT, **or intentionally pushing an ARTIFACT in a preferred direction (herding)**, incl. transitively through other elements (glossary). Pre-load limit is separately **3 per ROBOT** (§10.3.1). |
| **Pinning limit** | **G422** | **3 seconds**; escalates **every 3 s**. PIN count ends at **2 ft (~61 cm)** separation for **>3 s**, or either ROBOT moving **2 ft** from the pin origin for **>3 s**, or the pinner being pinned | Count **pauses** (does not reset) on the 2 ft break and resumes if you close back inside 2 ft. A single PIN **>15 s** is named as YELLOW/RED CARD territory under G211 (TABLES.md p.99). |
| **Trapping / blocking** | **G423** | greater-than-MOMENTARY = **>~3 s**; escalates **every 3 s** | Distinct from G422 — it covers isolating a *FIELD region*, not a robot. The manual points G424 and G426 defence toward G423 escalation (ORANGE_BOXES after G424 and G426 — non-binding). |
| **Horizontal expansion** | **G414 → R105.A** | **18 in × 18 in (45.70 cm)** fixed footprint when fully expanded, **must be physically constrained — software limiting is not sufficient** | STARTING CONFIGURATION is an 18 in cube (R101). So there is **no horizontal growth at all**: the expanded footprint equals the starting footprint. |
| **Vertical expansion** | **G415 → R105.B/C** | **18 in (45.70 cm)** normally; **38 in (96.50 cm)** only when **(A) during the final 20 seconds AND (B) not in any LAUNCH ZONE** | Vertical may be software-limited (R105.B/C) unlike horizontal. Both conditions must hold — this is an AND, not an OR. |
| **Launching restriction** | **G416** | LAUNCH only **inside a LAUNCH ZONE or overlapping a LAUNCH LINE** | LAUNCH ZONES: audience side **2 TILES × 1 TILE**, GOAL side **6 TILES × 3 TILES**, both infinitely-tall triangles bounded by LAUNCH LINES + perimeter (§9, full_layout L2230–2234). TILE ≈ **24 in** (L2170), FIELD ≈ **144 in × 144 in** (glossary). |
| **Opponent interference — AUTO** | **G402** | Whole-side exclusion for 30 s: cols **A/B/C = blue**, **D/E/F = red** | Both a *contact* ban and an *ARTIFACT-disruption* ban. Deflections that reach the far side accidentally are excused (TABLES.md p.104 Example 2); a direct LAUNCH that disrupts is not (Example 1). |
| **Opponent interference — TELEOP** | G420, G421 | No numeric threshold — "deliberate" as perceived by a REFEREE | G420/G421 mutually exclusive; most punitive penalty only. |
| **Protected zone — GATE** | **G424** | **GATE ZONE = 2.75 in (7.00 cm) wide × 10 in (25.40 cm) long**, infinitely tall, bounded by two parallel 10 in ALLIANCE-coloured tape segments adjacent to each GATE | Protection is **bidirectional and initiator-blind** ("regardless of who initiates"). Exception G424.A defers to G425. |
| **Protected zone — SECRET TUNNEL** | **G425** | **~46.5 in (118.10 cm) long × ~6.125 in (15.55 cm) wide**, infinitely tall | Asymmetric: this one penalises **the ROBOT that is in the opponent's tunnel**, not "either ROBOT". |
| **Protected zone — LOADING** | **G426** | **~23 in (58.40 cm) wide × ~23 in (58.40 cm) deep**, infinitely tall | Initiator-blind, either-ROBOT. |
| **Protected zone — BASE** | **G427** | **18 in ± 0.125 in × 18 in ± 0.125 in**, infinitely tall, **active only in the last 20 seconds** | The only protected zone whose penalty **awards real scoring points**, not just foul credit. |
| **Human-player limits** | G428, G429, G430, G431, **G432**, **G433**, **G434** | DRIVE TEAM = **up to 4 people** (glossary); DRIVE COACH max **1**; DRIVER max **3**, must be STUDENTs; **HUMAN PLAYER max [UNVERIFIED]** — the Max column for that row did not survive extraction. ALLIANCE AREA = **96 in × 54 in** (glossary). Storage cap **6 ARTIFACTS out of play per ALLIANCE**; human handling confined to the LOADING ZONE, **TELEOP only**, **no tools** | The HUMAN PLAYER row of Table 10-1 is mangled in both `TABLES.md` and `full_layout.txt`. See Beta feedback #5. |
| **Equipment height at the FIELD** | G302.B | **6 ft 6 in (~198 cm)** above the TILES | Applies to DRIVE TEAM equipment, not the ROBOT. |
| **Promptness** | G301 | **2 minutes** from the VERBAL WARNING / MAJOR FOUL; minimum break 5 min (Qual) / 8 min (Playoff) per T206 | |

### Archetype with **no** rule this season — the permissions

- **No ROBOT weight limit at all** (R103, explicit) — [MANUAL].
- **No rule prohibiting descoring in the G series.** Descoring is only reachable through G431.C (a *human* disrupting scoring) and as a named G211 escalation trigger ("descoring SCORING ELEMENTS strategically or REPEATEDLY", TABLES.md p.99). [JUDGMENT] There is no G-rule that makes robot-on-robot descoring a foul in itself — but the CLASSIFIER architecture makes it nearly unreachable, because G418 forbids touching ARTIFACTS on **any** RAMP including your own, at MAJOR FOUL per ARTIFACT.
- **No "one robot per zone" or possession-time rule** beyond G408 and G422/G423.
- **No restriction on being in the opponent's LOADING or GATE ZONE per se** — G424/G425/G426 penalise *contact*, not *presence*. [JUDGMENT] Parking a robot in an opponent protected zone without touching anyone is not itself a G-rule violation, though it is exactly the fact pattern G423 exists to catch.

---

## 3. Which fouls scale, and which escalate automatically

### 3a. Per-occurrence scaling (multiply by count)

| Rule | Scaling unit | Per unit |
|---|---|---|
| **G402** | per instance of ROBOT contact (A) / **per ARTIFACT** (B) | 15 |
| G404 | **per ARTIFACT** entering the GOAL after TELEOP | 15 |
| G405 | **per SCORING ELEMENT** | 15 |
| G406 | **per SCORING ELEMENT** | 15 |
| **G408** | **per SCORING ELEMENT over the limit** | 5 |
| **G416** | **per LAUNCHED SCORING ELEMENT** (5) / **per LAUNCHED ELEMENT that enters the GOAL** (15) | 5 or 15 |
| **G418** | **per ARTIFACT** | 15 |
| **G419** | **per ARTIFACT** | 15 |
| **G432** | **per ARTIFACT** (5) / **per ARTIFACT entering the GOAL** (15) | 5 or 15 |
| **G433** | **per non-ARTIFACT item** entered onto the FIELD | 5 |
| **G434** | **per ARTIFACT over the limit** — *and simultaneously per 3 s* | 5 |

Manual's own worked examples confirming multiplication: **G402** — one LAUNCH disrupting 2 pre-staged ARTIFACTS = **2 MAJOR FOULS** (TABLES.md p.104 Ex.1). **G417+G418** — opening the blue GATE and dumping 5 ARTIFACTS off the blue RAMP = **6 MAJOR FOULS**, 1 under G417.A and 5 under G418.B, plus blue gets the PATTERN RP (TABLES.md p.110 Ex.3). [DERIVED] that is **6 × 15 = 90 points** from one contact.

### 3b. Time scaling (multiply by duration)

| Rule | Clock | Manual's own worked number |
|---|---|---|
| **G422** (PIN) | MINOR at t=0, **+1 MINOR every 3 s** | **15 seconds = 6 MINOR FOULS** [MANUAL] TABLES.md p.92 |
| **G423** (blocking) | identical clock | same |
| **G434** (storage) | **per ARTIFACT over the limit, every 3 s** — a *product* of count and time, the only compound scaler in the manual | — |

[DERIVED] G422 at 15 s: 6 × 5 = **30 points**. Operands: 6 MINOR FOULS (manual's own count) × 5 pts/MINOR (Table 10-4).

[DERIVED] G434, 2 over the limit for 9 s: initial 2 MINOR + 3 additional 3-second intervals × 2 = 8 MINOR = 8 × 5 = **40 points**. Operands: (1 + 3) intervals × 2 ARTIFACTS × 5 pts. [JUDGMENT] the interval count on the initial assessment is my reading of "and an additional MINOR FOUL … for every 3 seconds"; worth a Q&A submission.

### 3c. Once per occurrence, flat

G401, G403, G413, G414, G415, G417, G420, G421, G424, G425, G426, G427, G429, G430, G431. TABLES.md p.93 is explicit for G420: *"Only 1 MAJOR FOUL is earned for a single violation."*

### 3d. Automatic escalation on repetition

Two distinct clocks, and they are not the same clock:

**Within a MATCH** (REPEATED = more than once in a MATCH):

- G210 MINOR → **MAJOR**
- G407 VERBAL → **MAJOR**
- G413 MAJOR → MAJOR + **YELLOW CARD**
- G409 DISABLED+VERBAL → **YELLOW CARD**

**Within the EVENT** ("if subsequent violations occur during the event", which TABLES.md p.92 defines as including *the same MATCH, a later MATCH in the same phase, or a later phase*):

- → YELLOW: G102, G201, G202, G207, G409, G412
- → RED: G203, G204, G205
- → MINOR FOUL: G411, G428

**Within the TOURNAMENT PHASE:**

- G301: VERBAL → **MAJOR FOUL charged to the *upcoming* MATCH**. The only forward-carrying foul in the manual.
- The card ladder itself: **YELLOW + a second YELLOW in the same tournament phase = RED = DQ** (Table 10-4).

**Discretionary but automatic-in-practice:** G211 sweeps up "subsequent violations of any rule or procedure during the event", so *every* rule in the manual has a YELLOW/RED tail.

---

## 4. The strategic asymmetry: a foul is a credit to the opponent, not a debit to you

This is the single most important structural fact in Section 11, and it cuts in three directions.

**(a) Your own score is untouched.** MINOR/MAJOR FOUL are defined as *"a credit of N points towards the opponent's MATCH point total"* (Table 10-4). Nothing is subtracted from you. [DERIVED] Therefore **your fouls cannot cost you the MOVEMENT, GOAL or PATTERN RP**, because those three RP are gated on *your own* LEAVE+BASE points, ARTIFACT-through-SQUARE count, and PATTERN points respectively (Table 10-2/10-3) — categories foul credit never enters. The exceptions are explicit and enumerated in the rule text, not implied: G206, G401, G417.A, G418.A/B, G419.B, G427, G431.C.

**(b) But foul points do decide the WIN.** WIN = 3 RP, the largest single RP source in the game (Table 10-2). Foul credit lands in the opponent's MATCH point total, which is exactly what WIN is computed on.

**(c) And foul points are invisible to the ranking tiebreaker.** Sort 2 in Table 13-1 is *"Average ALLIANCE MATCH points, **not including** MINOR FOULS and MAJOR FOULS"*. [DERIVED] So drawing fouls out of an opponent helps you win matches but does **not** improve your own 2nd-order sort. Conversely, committing fouls does not damage your 2nd-order sort either — it only costs you the 3 RP for the WIN. The whole penalty economy is a **win/loss instrument, not a ranking instrument**, except through RP.

### The price list

| Tier | Cost to you, in the currency that matters | [DERIVED] operands |
|---|---|---|
| MINOR FOUL | **5 opponent points** = 1.67 CLASSIFIED ARTIFACTS | 5 ÷ 3 pts per CLASSIFIED |
| | = 2.5 PATTERN points | 5 ÷ 2 |
| | = 5 DEPOT or OVERFLOW ARTIFACTS | 5 ÷ 1 |
| | = 0.5 of a full BASE return | 5 ÷ 10 |
| MAJOR FOUL | **15 opponent points** = **5 CLASSIFIED ARTIFACTS** | 15 ÷ 3 |
| | = 7.5 PATTERN points | 15 ÷ 2 |
| | = 15 DEPOT/OVERFLOW ARTIFACTS | 15 ÷ 1 |
| | = 1.5 full BASE returns | 15 ÷ 10 |
| YELLOW CARD | 0 points, but **half a DQ** — the next YELLOW in the phase is a RED | Table 10-4 |
| RED CARD / DISQUALIFIED | **0 MATCH points and 0 RP for that MATCH**, and the match "contributes 0 to all sort criteria" (full_layout L5991) | |
| RED CARD, in ranking terms | over 5 quals, losing one match's worth of RP costs **20% of your RANKING SCORE**; over 6 quals, **16.7%** | 1 ÷ 5 = 0.20; 1 ÷ 6 = 0.167 |
| RED CARD, worked | a team averaging 4.0 RP over 5 quals drops to **3.2 RS** if one match is zeroed | (4.0 × 5 − 4.0) ÷ 5 = 16 ÷ 5 = 3.2 |
| RP-forfeit clauses (G206, G417.A, G418, G419.B, G431.C) | **1–2 RP**, worth up to **2/3 of a WIN** | 2 RP ÷ 3 RP per WIN |

### The four most expensive single rules in the manual

[DERIVED] worst-case single-incident cost, ranked:

1. **G427 (BASE ZONE protection) — up to 45 points from one touch.** MAJOR FOUL 15 + contacted ROBOT awarded fully-returned-to-BASE 10 + a ROBOT it fully supports awarded 10 + the both-ROBOTS-fully-returned bonus 10 = **15 + 10 + 10 + 10 = 45**. And unlike every other foul, **those 30 BASE points are real scoring points that count toward the opponent's MOVEMENT RP threshold** (Table 10-3: 16 at non-Championship events). [DERIVED] two LEAVEs (3 + 3 = 6) plus one awarded full BASE (10) = **16 = exactly the MOVEMENT RP threshold** — so a single G427 can hand an otherwise-parked opponent their MOVEMENT RP. *[JUDGMENT/UNVERIFIED: whether the +10 two-ROBOT bonus triggers off rule-awarded BASE credit is not stated. Submit to Q&A.]*
2. **G418 + G417 combined (GATE/RAMP meddling) — 90 points, demonstrated by the manual itself.** 6 MAJOR FOULS × 15 = 90, plus the opponent gets the PATTERN RP (TABLES.md p.110 Ex.3).
3. **G416 (launching outside the LAUNCH ZONE) — unbounded, 15/ball.** A 6-ball burst from the wrong place that all score = 6 × 15 = **90**.
4. **G419.B (launching into the opponent's GOAL) — 15/ball plus a free PATTERN RP to them.**

### The cheapest rules — and therefore the ones that are *strategically priceable*

G424, G425, G426, G430 are all a flat **MINOR FOUL (5 points)** with no per-element and no per-second multiplier and no card attached. [JUDGMENT] **This is the deliberate-risk window.** 5 points is 1.67 CLASSIFIED ARTIFACTS. A defender who denies an opponent one full cycle by taking a G424 or G426 has broken even at roughly two denied ARTIFACTS. That is a real, defensible trade — with one caveat: the manual's own commentary explicitly warns that repeated protected-zone contact escalates into **G423** (MINOR + MINOR/3 s) and thence **G211** (cards). The trade only stays cheap while it stays *occasional*.

---

## 5. The two strategy profiles

### 5a. High-cycle-rate scorer — the three rules it will break

Cycle economics first, so the fouls have something to be priced against. [DERIVED] TELEOP is **120 s** (glossary). A CLASSIFIED ARTIFACT is **3 points** (Table 10-2). If the robot cycles 3 ARTIFACTS per trip (the G408 cap) at, say, 12 s per trip, that is 120 ÷ 12 = 10 trips × 3 = 30 ARTIFACTS × 3 = 90 TELEOP points. *[The 12 s figure is [UNVERIFIED] — R3/R4 own the cycle model; I use it only as a denominator.]* At that rate **one MAJOR FOUL (15) erases 1.7 trips; five MAJOR FOULS erase the whole TELEOP.**

| # | Rule | Why this architecture trips it | Cost per match [DERIVED] |
|---|---|---|---|
| **1** | **G416** — LAUNCH only in a LAUNCH ZONE or overlapping a LAUNCH LINE | A shooter's whole value proposition is *shoot without stopping*. Firing while still rolling out of, or short of, the LAUNCH ZONE is the single easiest mistake to make at speed — and the penalty is worse when you *succeed*: **MAJOR per ball that goes in.** | One bad 3-ball burst that scores: 3 × 15 = **45**. A robot that mis-locates its LAUNCH ZONE boundary twice in a match: 6 × 15 = **90**, i.e. the entire TELEOP output above. |
| **2** | **G408** — CONTROL ≤ 3 ARTIFACTS | A high-throughput intake wants a magazine, and **CONTROL includes herding** — an intake bar sweeping a fourth and fifth ball ahead of the robot counts even if only three are indexed. | 5 held = (5 − 3) × 5 = **10**. Three such events: **30**, plus the "excessive" YELLOW CARD trigger (ORANGE_BOXES gloss, non-binding: 5+ simultaneous, or 3+ separate greater-than-MOMENTARY events at 4). |
| **3** | **G418** — no contact with ARTIFACTS on **any** RAMP, including your own | The RAMP holds up to 9 CLASSIFIED ARTIFACTS (glossary) and sits on the CLASSIFIER attached to the GOAL — exactly where a fast scorer parks. Any bumper brush, any ball CONTROLLED by the robot grazing the RAMP. **MAJOR per ARTIFACT**, and touching your *own* RAMP costs you the PATTERN RP. | 2 ARTIFACTS disturbed: 2 × 15 = **30** + PATTERN RP forfeited. The manual's own example reaches 6 × 15 = **90**. |

**The architectural finding, and it is the biggest one in R5.** [DERIVED from G415 + G416 + R105.B] G416 says you may only LAUNCH inside a LAUNCH ZONE. G415 says you may only exceed 18 in of height when **(A) in the final 20 s AND (B) not in any LAUNCH ZONE**. The two conditions are mutually exclusive by construction: **anywhere you are legally allowed to shoot, you are capped at 18 in tall.** A launcher that must raise a hood, turret or elevator above 18 in to fire is illegal in every position from which firing is legal. And G415's violation is *MINOR, escalating to MAJOR "if the over-expansion … enables a scoring action"* — raising to shoot **is** enabling a scoring action, so the real price is **15 per shot cycle, not 5**.

→ **Design consequence for BIOBUZZ-style planning: the entire launcher, at full firing extension, must live inside the 18 in cube. The 38 in allowance is an endgame-only, non-shooting allowance** — for a lift, a hook, or a BASE-return mechanism, not a shooter.

Second architectural finding: **R105.A permits no horizontal growth whatsoever** (18 in expanded = 18 in starting, per R101), and it must be **mechanically** constrained — ORANGE_BOXES after R105 notes software limits are not accepted at inspection for horizontal, and flexible extensions like surgical-tubing flappers and star intakes count. *[Non-binding commentary; the binding text is R105.A "physically constrained … without the use of software".]* For a two-robot program with hand tools and 3D printing, that rules out compliant-flap intakes that flex past the frame — a duplicability-relevant constraint, since a hard mechanical stop must be built and verified twice.

### 5b. Defensive / denial robot — the three rules it will break

| # | Rule | Why this architecture trips it | Cost per match [DERIVED] |
|---|---|---|---|
| **1** | **G422** — 3-count on PINS | Defence *is* pinning. The count only pauses at **2 ft** separation held for **>3 s**, so a defender who backs off 18 in and re-engages never clears the count. | 15 s pin = **6 MINOR = 30** (manual's own count × 5). Two such pins = **60**. A single pin past 15 s is a named G211 card trigger. |
| **2** | **G424 / G425 / G426 / G427** — the four protected zones | The GATE ZONE is **2.75 in wide**, the SECRET TUNNEL **6.125 in wide**. These are narrow enough that a defender pressuring the opponent's scoring corridor is *inside one of them most of the time*, and G424/G426 are **initiator-blind** — the opponent can back into you and you still get the foul. | Four incidental contacts: 4 × 5 = **20**. Add one G427 in the last 20 s: 15 + 10 = **25**, up to **45** if it completes the pair. Realistic defender total: **45–65**. |
| **3** | **G420 / G421** — impairment and tipping | A defender that plays hard enough to matter eventually catches a wheel or a frame rail. First offence is **MAJOR + YELLOW immediately** — no warning step — and RED if the opponent cannot drive. | **15** plus a YELLOW that is half a DQ. Two YELLOWs in a phase = RED = **0 MATCH points and 0 RP**, worth ~20% of RANKING SCORE over a 5-match schedule. |

Runner-up for the defender: **G423** — the manual's commentary after both G424 and G426 explicitly says protected-zone actions "may also fall under other penalties including G423", which carries the same 3-second escalating clock as pinning.

### 5c. The comparison, and the recommendation for a 15-student two-robot program

[DERIVED] Expected per-match foul exposure, using the mid-range figures above:

| | Realistic bad match | Worst realistic match | Points as a share of a 90-point TELEOP |
|---|---|---|---|
| High-cycle scorer | 30–45 | 90–135 | 33%–150% |
| Defender | 45–65 | 90–120 | 50%–133% |

**[JUDGMENT]** The two profiles carry similar *magnitude*, but not similar *shape*, and the shape is what should decide it for this team:

- The scorer's exposure is **eliminable by design and practice**. G416 is a localisation problem (know where the LAUNCH LINE is), G408 is a mechanical problem (build a magazine that physically cannot hold four), G418 is a geometry problem (a bumper standoff that cannot reach the RAMP). All three are fixed once, in CAD, and then **duplicate identically across both robots** — which is exactly the property a two-robot program needs. None of them carry a card on first offence.
- The defender's exposure is **irreducible**, because G424/G426 are initiator-blind: the opponent controls whether you foul. And G420/G421 issue a **YELLOW on the first offence**, which is the only mechanism in the manual that compounds *across matches*. A driver who is 90% clean over 5 quals still has a meaningful chance of collecting the second YELLOW that becomes a RED.
- Defence is also the **least duplicable** skill on offer. Mechanisms duplicate; driver judgment does not. With two teams and ~15 students, you will field two drive crews of uneven experience, and the penalty ladder punishes the weaker crew far harder in a defensive role than in a scoring role.

**Recommendation:** build both robots as scorers with the three design constraints above baked in as hard mechanical limits (18 in cube at full firing extension; magazine capacity 3; bumper standoff clear of the RAMP). Treat defence as a **priced, occasional tool** — G424/G425/G426 at a flat 5 points with no card is a legitimate trade for denying more than ~2 ARTIFACTS — and set a standing drive-team rule of **no pin past a 2-count** and **no contact anywhere near a BASE ZONE in the last 20 seconds**, since G427 is the single most expensive touch in the game.

---

## 6. Open questions for the Q&A queue (feeds R6)

1. **G427 + the BASE bonus.** Does rule-awarded "fully returned to BASE" credit for two opponent ROBOTS also trigger the +10 two-ROBOTS bonus in Table 10-2? Difference between a 35-point and a 45-point penalty.
2. **G434 interval counting.** Is the initial MINOR-per-ARTIFACT assessed at t=0 *in addition to* the first 3-second interval, or does the first interval subsume it?
3. **LAUNCH vs CONTROL overlap.** LAUNCH is defined as including *"propelled across the floor to a desired location or in a preferred direction"*; CONTROL is defined as including *"intentionally pushes a SCORING ELEMENT to a desired location or in a preferred direction (i.e., herding)"*. These are near-identical wordings. Does herding an ARTIFACT across the floor outside a LAUNCH ZONE constitute LAUNCHING under G416, at 5 points per element? This is a significant and possibly unintended exposure for any robot that pushes balls.
4. **G415 + G416 mutual exclusion.** Confirm that a launcher may never legally exceed 18 in while firing. If confirmed, this is a headline design constraint; if there is an intended reading that permits it, the whole shooter archetype changes.
5. **G424.A geometry.** The exception requires being simultaneously in your own GATE ZONE **and** the opponent's SECRET TUNNEL ZONE. Is that overlap physically possible on the field? If it is not, the exception is dead text and G425 governs alone. Needs the R4 geometry pass to answer.
6. **HUMAN PLAYER count.** Table 10-1's Max/DRIVE TEAM value for HUMAN PLAYER did not extract. Read it off the rendered page.

---

## Beta feedback

**1. An "allowed" method file contains answer-key material.** `reference/ANALYSIS-PROTOCOL.md` is on the allowed list, but §5 (R4) item 5 hands over DECODE's AprilTag family, size and IDs verbatim, and §6 (R5) pass 6 hands over the MOMENTARY/CONTINUOUS/REPEATED thresholds as "about 3 s / about 10 s / more than once per MATCH" *before I derived them from the manual*. I derived them independently at `full_layout.txt` L2865–2867 and the numbers match, so nothing here is contaminated — but the protocol should carry its DECODE calibration in a separate file, or the test is not clean. **This is the most important fix before 2026-09-12.**

**2. Two Violation strings in `VIOLATIONS.tsv` and `rules_full.tsv` are truncated mid-sentence.** G402 ends at *"…and MAJOR FOUL per ARTIFACT in"* and G419 at *"…awarded the PATTERN RP if"*. The missing tokens are the clause references (`G402.B.` and `G419.B.`), which the parser threw into the *body* field of the same row instead. Both are among the 15 game-specific rules — the highest-value rows in the file. I recovered them from `full_layout.txt` L3524 and L3836. Fix: keep scanning the Violation block until a blank line or the next rule id.

**3. `rules_full.tsv` for C501 swallowed the entire 6-page glossary** (740 words in G434's body, ~9,000 characters in C501's). The bug: the last rule of a section absorbs everything up to the next rule id, so terminal rules eat the following section wholesale. G434's body ends with the whole preamble to Section 12. It was accidentally useful — that dump is the only clean, correctly-paired copy of the glossary in the bundle — but it is not the intended behaviour, and it means **the last rule in every section has an untrustworthy body**.

**4. The glossary is not in the bundle as a first-class file, and it should be.** MINOR FOUL, MAJOR FOUL, CONTROL, LAUNCH, PIN, MOMENTARY, CONTINUOUS, REPEATED and every zone dimension are glossary entries. R5 cannot be done without them, and the only route to them was `full_layout.txt` — the file I was told to treat as a last resort. In `full_layout.txt` the glossary is **column-mispaired**: at L6857 the term "LAUNCH/LAUNCHING" sits beside the GATE ZONE definition, and "MAJOR FOUL" beside "a SCORING ELEMENT manager". I only trusted definitions I could confirm twice. Ask for `bundle/GLOSSARY.tsv` with `term<TAB>definition`.

**5. Table 10-1 (DRIVE TEAM roles) is unrecoverable in both `TABLES.md` and `full_layout.txt`.** The Role, Description and Max columns are interleaved three ways: DRIVE COACH's description lands on DRIVER's row, and the HUMAN PLAYER maximum is simply absent. It is a 3-row table. `TABLES.md` also emits it three separate times under the same caption with different fragments each time. Human-player limits are one of the seven archetypes R5 is asked to quantify, so this is a real gap — I had to return `[UNVERIFIED]`.

**6. `TABLES.md` repeats captions and drops others.** "Table 10-6: Violation examples" appears four times over pages 91–93 with different content; 30-odd sections are captioned "(no caption on page)" and several of those are actually blue/orange sidebars, not tables. Distinguishing a *binding* worked example (the G402 and G417/G418 examples, which I priced against) from *non-binding* orange-box commentary required cross-checking every one against `ORANGE_BOXES.md`. That cross-check should be done by the ingest, and each `TABLES.md` block tagged `BINDING` / `NON-BINDING`.

**7. No penalty-tier rollup was provided, and it is mechanical.** Every one of the 53 Violation strings parses cleanly into (tier, scaling unit, escalation trigger, RP effect). I built that by hand — it is §1 and §3 above and it took most of the phase. A `bundle/PENALTY_LADDER.tsv` with columns `id | base_tier | per_unit | time_scaled | card | rp_effect` would collapse R5 from ~45 minutes to ~15 and remove the transcription risk from the highest-consequence numbers in the analysis.

**8. What worked well and should not change.** `rules_GAMESPECIFIC.txt` is the single best file in the bundle — 17 lines that correctly isolate what is new, and the `GAMESPEC`/`EVERGREEN` class tag in `rules_full.tsv` field 3 reproduces it exactly (15 G-rules + R105 + C501), so the two cross-validate. `caps_NOVEL_ranked.txt` was a fast orientation to the vocabulary. `TABLES.md` was reliable for the numbers that matter most — Table 10-2 and Table 10-4 both extracted cleanly, and Table 10-4 appears twice (p.89 and again near L1110) with identical values, which is a free consistency check.

**9. Leakage self-report, as instructed.** I recognised the game as DECODE from `STATUS.md` (the manual filename is in the header) and from the vocabulary list. I did not open any forbidden file and I did not use recalled DECODE knowledge anywhere in this document — every number above traces to a bundle citation. Two moments where I noticed prior knowledge surfacing, both of which I resolved from the manual instead: the FTC TILE dimension (confirmed at `full_layout.txt` L2170, ~24 in) and the fact that an FTC ALLIANCE is two teams (confirmed at L2496 and in the glossary). Flagging them so the harness can see where the boundary got tested.
