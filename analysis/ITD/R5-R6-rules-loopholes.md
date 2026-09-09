# R5 + R6 — Rules, Penalty Exposure and the Loophole Hunt

**Harness beta test #2 · manual treated as brand-new · run 2026-08-23**
**Source manual:** `Competition Manual – V14`, 146 pp, 209 rules, 53 G-rules, 16 orange (game-specific) — `analysis/ITD/STATUS.md`

---

## 0. Provenance, labels, and what I refused to use

**Read (bundle):** `STATUS.md` · `bundle/TABLES.md` · `bundle/rules_GAMESPECIFIC.txt` · `bundle/rules_full.tsv` · `bundle/VIOLATIONS.tsv` · `bundle/ORANGE_BOXES.md` · `bundle/caps_NOVEL_ranked.txt` · `bundle/TRIPWIRES.txt` · `bundle/rules_ADDED.txt` / `rules_REMOVED.txt` / `section_versions.txt` · `bundle/figures/` (MANIFEST, p046, p047, p059, p060, p062, p066) · `bundle/full_layout.txt` (prose only — §9.2, §10.3–10.8, §16 glossary; **no point value taken from it**).

**Method files read:** `reference/LOOPHOLE-PLAYBOOK.md` · `reference/ANALYSIS-PROTOCOL.md` §6 (R5) and §7 (R6).

**Refused (answer key):** `reference/SCORING-PATTERNS.md` · `research/LOOPHOLE-CASEBOOK.md` · `reference/ROBOT-ARCHETYPE-LIBRARY.md` · `reference/PENALTY-AND-ENFORCEMENT.md` · `research/SCOUTING-AND-AWARDS.md` · `manuals/_reference_prior_seasons/` · `manuals/archive/`. None opened. `ANALYSIS-PROTOCOL.md` R5 step 2 and R6 both dispatch to two of those files; I substituted a bundle-derived method (see §A2) and logged it in Beta feedback.

**Labels:** `[MANUAL]` = quoted or paraphrased binding rule text with an id · `[DERIVED]` = arithmetic or inference on `[MANUAL]` facts, operands shown · `[JUDGMENT]` = my call, not in the manual · `[ORANGE]` = non-binding commentary, **never load-bearing on its own** · `[UNVERIFIED]` = I could not find it in the bundle.

### 0.1 Leak flags — things I knew that I did not read in the bundle

Three came from an **allowed** method file, not from memory, and I have not used any of them as evidence:

| # | Leak | Where it leaked from | What I did |
|---|---|---|---|
| L1 | "ITD Q&A Q21 confirmed every AUTO element doubled (high chamber = 20)" | `LOOPHOLE-PLAYBOOK.md` §2 Pass 5 | Answer key for finding **F1**. I derived F1 independently from §10.5 + Table 10-3 and present only that derivation. F1 stays a Q&A question, not a settled fact. |
| L2 | "ITD priced HIGH CHAMBER at 10 above HIGH BASKET at 8, while the basket lip sat at 43.0 in — the harder mechanism paid *less*" | `LOOPHOLE-PLAYBOOK.md` §3 | Answer key for the underpriced-objective question. Both numbers are independently in `TABLES.md` Table 10-3 and `full_layout` §9.6, so I cite those; the *conclusion* I re-derived. |
| L3 | "ITD G423 5 s → DECODE G422 3 s (pin limits tightening)"; "ITD G427 is the canonical protected-zone case" | `LOOPHOLE-PLAYBOOK.md` §2 Pass 2 and §3 | Names the exact two rules this phase was supposed to find. I read G423 and G427 in `rules_full.tsv` regardless; the pin *trend* claim is unused. |

I did **not** consult personal recollection of this game. Where the bundle is silent I have written `[UNVERIFIED]` rather than filling the gap.

---

# PART A — Rules and penalty exposure

## A1. Every G-rule

53 G-rules. `Class` from the `class` column of `rules_full.tsv`; `GAMESPEC` = orange headline, cross-checked against `rules_GAMESPECIFIC.txt` (15 G-rules + R104 = the 16 orange rules). Tier key below the table.

### 11.1 Personal Safety

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G101 | Humans, stay off the FIELD during the MATCH | DRIVE TEAM on the FIELD except pre-MATCH placement / post-MATCH retrieval when signalled | verbal warning; YELLOW if subsequent | T0→T3 | evergreen |
| G102 | Be careful when interacting with ARENA elements | climbing on, hanging from, permanently deforming, or damaging ARENA elements | verbal warning; YELLOW if subsequent | T0→T3 | evergreen |

### 11.2 Conduct

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G201 | Be a good person | incivility, disrespect of equipment | verbal; YELLOW if subsequent; escalates via G211 | T0→T3 | evergreen |
| G202 | DRIVE TEAM Interactions | distracting/taunting the opposing DRIVE TEAM | verbal; YELLOW if subsequent | T0→T3 | evergreen |
| G203 | Asking other teams to throw a MATCH | encouraging a non-ALLIANCE team to play below ability | verbal; YELLOW if subsequent | T0→T3 | evergreen |
| G204 | Letting someone coerce you into throwing a MATCH | playing below ability because another team asked | verbal; YELLOW if subsequent | T0→T3 | evergreen |
| G205 | Throwing your own MATCH is bad | intentionally losing to manipulate rankings | verbal; YELLOW if subsequent | T0→T3 | evergreen |
| G206 | Do not abuse ARENA access | badge-holders assisting/coaching/signalling from restricted areas | verbal; YELLOW if subsequent | T0→T3 | evergreen |
| G207 | Show up to your MATCHES | no DRIVE TEAM member at the ARENA for an assigned qual | **DISQUALIFIED** from that MATCH | T4 | evergreen |
| G208 | Enter only 1 ROBOT | a second ROBOT / two concurrent events | verbal + **RED CARD** if not corrected | T3 | evergreen |
| G209 | Keep your ROBOT together | intentionally detaching or leaving a part on the FIELD | **RED CARD** | T3 | evergreen |
| G210 | Do not expect to gain by doing others harm | acts clearly aimed at forcing an opponent to violate a rule | MINOR; MAJOR if REPEATED. **Forced violation is not charged to the target** | T1→T2 | evergreen |
| G211 | Egregious or exceptional violations | egregious behaviour or repeat violations of anything | **YELLOW or RED CARD** at Head REFEREE discretion | T3 | evergreen |

### 11.3 Pre-MATCH

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G301 | Be prompt | significant delay to MATCH start (both: start time passed **and** not MATCH-ready / no good-faith effort) | verbal → MAJOR next MATCH → **DISABLED** after 2 min | T0→T2→T4 | evergreen |
| G302 | Only specific items to the MATCH | anything not on the A–I allowlist; wireless; anything affecting MATCH outcome | MATCH held; **YELLOW** if used in-MATCH | T3 | evergreen |
| G303 | ROBOTS must be set up to play | 11 start-state conditions A–K | quick remedy → hold; else **DISABLED**; **RED CARD** if a non-inspected ROBOT plays | T4/T3 | evergreen |
| G304 | Teams must select an OpMode | starting without an initialised OpMode | MATCH held; **DISABLED** if unresolvable | T4 | evergreen |

### 11.4.1 AUTO

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G401 | Let the ROBOT do its thing | DRIVE TEAM interaction in AUTO except ▶ / ■ / safety | **MAJOR** | T2 | evergreen |
| G402 | Start AUTO on time | ▶ pressed later than MOMENTARY after MATCH start | **MAJOR** + YELLOW if subsequent | T2→T3 | evergreen |
| G403 | OpModes are stopped by the end of AUTO | AUTO OpMode still running past 0:30 | MINOR, or **MAJOR if it produces a scoring achievement** | T1/T2 | evergreen |
| **G404** | **No AUTO opponent interference** | A: contacting an opponent ROBOT wholly in its own half · B: contacting a pre-set SAMPLE on the opponent half · C: moving elements onto the opponent half outside the SUBMERSIBLE ZONE | **MAJOR each occurrence** | T2 | **GAMESPEC** |

### 11.4.2 TELEOP

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G405 | Motionless between AUTO and TELEOP | any powered movement in the 8-second transition | **MAJOR** + YELLOW if subsequent | T2→T3 | evergreen |
| G406 | Motionless at the end of TELEOP | driver control after the buzzer | MINOR, or **MAJOR if it produces a scoring achievement** | T1/T2 | evergreen |

### 11.4.3 SCORING ELEMENT

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G407 | Use SCORING ELEMENTS as directed | using an element to ease/amplify a FIELD-element challenge (e.g. standing on samples to ASCEND) | **MAJOR per SCORING ELEMENT** | T2 | evergreen |
| G408 | Keep SCORING ELEMENTS in bounds | intentionally ejecting an element from the FIELD | **MAJOR per SCORING ELEMENT** | T2 | evergreen |
| G409 | Do not damage SCORING ELEMENTS | ROBOT or HUMAN PLAYER damaging an element | verbal + **MAJOR if REPEATED**; DISABLED + re-inspection if damage likely | T0→T2→T4 | evergreen |
| **G410** | **1 SAMPLE or SPECIMEN at a time** | CONTROL of >1 SAMPLE/SPECIMEN, directly or transitively. **No limit on CLIPS.** Exceptions: MOMENTARY excess while collecting inside the SUBMERSIBLE ZONE; own scored elements exempt | **MINOR per additional element** + YELLOW if excessive | T1→T3 | **GAMESPEC** |
| **G411** | **No CONTROL of opposing ALLIANCE SPECIFIC elements** | more than MOMENTARY control of an opponent's SPECIFIC SAMPLE/SPECIMEN | **MINOR per element, + MINOR per element per 5 s, + MAJOR per element scored while controlled** | T1→T2 | **GAMESPEC** |
| **G412** | **No de-scoring opponent elements** | removing opponent SAMPLES from the NET ZONE or BASKETS, or SPECIMENS **fully clipped** onto CHAMBERS | **MAJOR per element de-scored** | T2 | **GAMESPEC** |

### 11.4.4 ROBOT

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G413 | ROBOTS must be safe | contact outside the FIELD; dangerous operation/design | **YELLOW + DISABLED** if unsafe or CONTINUOUS | T3/T4 | evergreen |
| G414 | ROBOTS must stop when instructed | not pressing ■ after a REFEREE DISABLE | **MAJOR** if >MOMENTARY; **RED** if CONTINUOUS | T2→T3 | evergreen |
| G415 | ROBOTS must be identifiable | team number / ALLIANCE colour becoming indeterminate | verbal; YELLOW if subsequent | T0→T3 | evergreen |
| G416 | Watch your ARENA interaction | damaging ARENA elements; grabbing/grasping/attaching/entangling/suspending from any ARENA element **except SCORING ELEMENTS and your own RUNGS** | verbal → YELLOW if REPEATED or >MOMENTARY; DISABLED if damage likely | T0→T3→T4 | evergreen |
| **G417** | **Stay in CONTROL of your SCORING ELEMENTS** | LAUNCHING a SCORING ELEMENT | **MINOR per element LAUNCHED** | T1 | **GAMESPEC** |
| **G418** | **Horizontal expansion limit** | exceeding the R104 boundary after MATCH start | MINOR if >MOMENTARY; **MAJOR if the over-expansion gives strategic benefit, incl. impeding or enabling a scoring action** | T1/T2 | **GAMESPEC** |
| **G419** | **Watch out for Humans** | A: entering the OBSERVATION ZONE while a HUMAN PLAYER is in it · B: contacting an element the HUMAN PLAYER controls | **MINOR per occurrence** + YELLOW if the ROBOT contacts the HUMAN PLAYER | T1→T3 | **GAMESPEC** |
| **G420** | **No climbing on the inside** | starting an ASCENT with any part of the CHASSIS inside the SUBMERSIBLE ZONE | **MAJOR + all §10.5.3 ASCENT credit forfeited** | T2 | **GAMESPEC** |

### 11.4.5 Opponent Interaction — *G421 and G422 are mutually exclusive; a single interaction yields only the most punitive penalty* [MANUAL, G420 body]

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G421 | This is not combat robotics | deliberate damage or functional impairment of an opponent | **MAJOR + YELLOW**; **MAJOR + RED** if the opponent cannot drive | T2+T3 | evergreen |
| G422 | Do not tip or entangle | deliberately attaching to, tipping, or entangling an opponent | **MAJOR + YELLOW**; **MAJOR + RED** if CONTINUOUS or opponent cannot drive | T2+T3 | evergreen |
| G423 | There is a 5-count on PINS | PINNING an opponent >5 s | **MINOR + an additional MINOR every 5 s uncorrected** | T1 (stacking) | evergreen |
| G424 | No gameplay shutdown strategies | isolating/closing off any major element of MATCH play for >MOMENTARY | **MINOR + an additional MINOR every 5 s uncorrected** | T1 (stacking) | evergreen |
| **G425** | **NET ZONE Protection** | contacting an opponent ROBOT (directly **or through a controlled element**, **regardless of who initiates**) when any part of **either** ROBOT is in **the opponent's** NET ZONE | **MAJOR per occurrence** | T2 | **GAMESPEC** |
| **G426** | **OBSERVATION ZONE Protection** | being in the opposing ALLIANCE'S OBSERVATION ZONE. **Exempt if you are being PINNED** | **MINOR + MINOR every 5 s + MINOR per element contacted inside the zone** | T1 (stacking ×2) | **GAMESPEC** |
| **G427** | **Climbing ROBOTS are protected** | in the last 30 s, contacting an opponent (directly or through a controlled element, regardless of initiator) when any part of either ROBOT is in **the opponent's ASCENT ZONE**. Exceptions: (A) both robots already meet LEVEL 2/3 criteria; (B) the opponent extends >≈7 in into the SUBMERSIBLE ZONE from the barrier | **MAJOR + the affected opponent ROBOT is awarded a LEVEL 3 ASCENT** | T2 + score award | **GAMESPEC** |

### 11.4.6 Human / DRIVE TEAM

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G428 | No wandering | DRIVE TEAM members leaving their ALLIANCE AREA | verbal + **MINOR** if subsequent, any time in the event | T0→T1 | evergreen |
| G429 | Hands off the controls | DRIVE COACH handling gamepads (may hold/troubleshoot/select/INIT/▶/■ only) | **MAJOR** + YELLOW if >MOMENTARY | T2→T3 | evergreen |
| G430 | Watch your reach | any DRIVE TEAM member extending into the FIELD except per G431/G432 | **MAJOR per occurrence** + YELLOW if they contact the ROBOT | T2→T3 | evergreen |
| **G431** | **HUMAN PLAYERS manipulate elements within limits** | anyone but the HUMAN PLAYER introducing/retrieving elements in the OBSERVATION ZONE; contacting an element a ROBOT possesses; removing opponent elements from the zone. **A: any number of elements at a time. B: any orientation. C: AUTO and TELEOP only. E: may reintroduce elements a ROBOT knocked out** | **MINOR per occurrence** + YELLOW if they contact the ROBOT | T1→T3 | **GAMESPEC** |
| **G432** | **Watch out for ROBOTS** | HUMAN PLAYER breaking the vertical plane of the FIELD wall while a ROBOT is in the OBSERVATION ZONE (unless that ROBOT is DISABLED) | **MINOR per occurrence** + YELLOW if they contact the ROBOT | T1→T3 | **GAMESPEC** |
| **G433** | **HUMAN PLAYERS may not yeet SCORING ELEMENTS** | causing an element to exit the OBSERVATION ZONE into the rest of the FIELD | **MAJOR per SCORING ELEMENT** | T2 | **GAMESPEC** |
| **G434** | **No tools to introduce or retrieve elements** | the HUMAN PLAYER using any tool on a SCORING ELEMENT | **MINOR per occurrence** | T1 | **GAMESPEC** |

### 11.5 Post-MATCH

| id | headline | what it forbids | violation | tier | class |
|---|---|---|---|---|---|
| G501 | Leave promptly | significant or multiple post-MATCH delays | verbal; YELLOW if subsequent | T0→T3 | evergreen |
| G502 | Stop ROBOTS before entering the FIELD | entering before the Head REFEREE signals **and** ■ has been pressed | verbal; YELLOW if subsequent | T0→T3 | evergreen |

**Tier key** `[DERIVED]` from Table 10-4: **T0** verbal warning (no points) · **T1** MINOR FOUL (+5 to opponent) · **T2** MAJOR FOUL (+15 to opponent) · **T3** card (YELLOW = warning, second YELLOW → RED; RED = MATCH disqualification) · **T4** DISABLED / DISQUALIFIED (robot or match lost outright).

**The one construction rule in the orange set:** **R104 There is a horizontal expansion limit** — no violation line of its own; enforced in-match through **G418** [MANUAL, R104 body + ORANGE after R104].

---

## A2. Archetype coverage — built from the manual's own §11 headings

`ANALYSIS-PROTOCOL.md` R5 step 2 sends you to a forbidden file for the archetype list. **Substitute method, and it is season-agnostic:** the manual's own §11 subsection headings *are* the archetype list, in the manual's own words. Recovered from the section markers embedded in rule bodies in `rules_full.tsv`.

| Archetype (= §11 subsection) | G-rules | Game-specific rules here | Read-through |
|---|---|---|---|
| 11.1 Personal Safety | G101–G102 | 0 | Fully evergreen. No season-specific human-safety hazard was written. |
| 11.2 Conduct | G201–G211 | 0 | Fully evergreen. G210 does heavy work this season (§B, F5/F6). |
| 11.3 Pre-MATCH | G301–G304 | 0 | Evergreen — but G303.E/F/I are *loaded* with game-specific content by reference (§A3.7). |
| 11.4.1 AUTO | G401–G404 | **G404** | One rule, and it is a geometry rule. |
| 11.4.2 TELEOP | G405–G406 | **0** | **Permission.** No rule in the manual restricts TELEOP behaviour *as such*; everything is handled by the element/robot/opponent archetypes. |
| 11.4.3 SCORING ELEMENT | G407–G412 | **G410, G411, G412** | The densest game-specific block. Control limits and de-scoring. |
| 11.4.4 ROBOT | G413–G420 | **G417, G418, G419, G420** | LAUNCH ban, expansion, human proximity, ascent entry. |
| 11.4.5 Opponent Interaction | G421–G427 | **G425, G426, G427** | Three protected zones. This is where the money is. |
| 11.4.6 Human | G428–G434 | **G431, G432, G433, G434** | The HUMAN PLAYER is a first-class game actor this season. |
| 11.5 Post-MATCH | G501–G502 | 0 | Fully evergreen. |

`[DERIVED]` **The archetype with no game-specific rule and the most freedom is 11.4.2 TELEOP.** `[JUDGMENT]` That is a permission, not an oversight: it means the season's constraints are all about *what you touch* and *where you are*, never about *what you do with the drivetrain*.

---

## A3. The recurring archetypes, with this season's numbers

### A3.1 Duration vocabulary — the thresholds everything else is written in
[MANUAL, §10.6] **MOMENTARY** ≈ fewer than **3 seconds** · **CONTINUOUS** ≈ more than **10 seconds** · **REPEATED** = more than **once within a MATCH**. [MANUAL] "It is not the intent for REFEREES to provide a count during the time periods." `[JUDGMENT]` Design to half of every threshold: if the rule says MOMENTARY, build for 1.5 s.

### A3.2 Protected zones — the complete map

| Zone | Geometry [MANUAL, §9.2] | Protected by | Trigger window | Cost of violating |
|---|---|---|---|---|
| **NET ZONE** | infinitely tall triangle in the corner under the BASKETS; hypotenuse of ALLIANCE tape corner-to-corner across one TILE; outside edge **22.75 in** from the FIELD corner measured at the wall; **includes the tape** | **G425** | whole MATCH | **MAJOR (15) per occurrence** |
| **OBSERVATION ZONE** | infinitely tall 4-sided polygon, **36.6 in** at the widest × **13.1 in** deep, bounded by ALLIANCE tape and the adjoining FIELD wall; **includes the tape** | **G426** (robot) + **G419** (robot vs human) + **G432** (human vs robot) | whole MATCH | MINOR (5) **+ 5 per 5 s + 5 per element touched** |
| **ASCENT ZONE** | infinitely tall 5-sided polygon: two **9.25 in** sides on the SUBMERSIBLE outriggers, one **44.75 in** side on the SUBMERSIBLE barrier, two **26 in** white-tape sides running out to a point **20 in** from the barrier; **includes the tape**. **ALLIANCE SPECIFIC only during the last 30 seconds** | **G427** | **last 30 s only** | **MAJOR (15) + a LEVEL 3 ASCENT (30) awarded to the opponent = 45-point swing** |
| **SUBMERSIBLE ZONE** | **27.5 in** × **42.75 in**, infinitely tall, bounded by the innermost edge of the barriers | not a protected zone — but **G420** gates ascent entry and **G427(B)** revokes *your* protection if you reach >≈7 in into it | — | see G420 / G427 |
| **ALLIANCE AREA** | **120 in** × **42 in** × infinitely tall, outside the FIELD; includes the tape | **G428** (stay in it) | whole MATCH | verbal → MINOR |

`[DERIVED]` **"Includes the taped lines" appears on all four in-field zones.** So the boundary is the **outer edge of the 1-in gaffer tape**, and every zone rule that says "in" is satisfied by *any part* of the robot over that line — G425 and G427 both say "**any part of either ROBOT**". A 42-in-long extension puts you in a zone your chassis is nowhere near.

### A3.3 Pinning and trapping
[MANUAL, G423] **5 seconds.** PINNING = preventing an opponent's movement by contact, direct **or transitive** (e.g. against a FIELD element), **while the opponent is attempting to move**. The count **ends** if: (A) the robots separate by ≥ **2 ft (~61 cm)** for >5 s; (B) either robot moves 2 ft from where the pin initiated for >5 s; or (C) the pinning robot gets pinned. The count **pauses** (does not reset) at 2 ft separation and **resumes** on re-approach.
[MANUAL, VIOLATIONS G423] MINOR **plus an additional MINOR every 5 s uncorrected**.
[ORANGE, after G211, p.75 — non-binding] lists "PINNING in excess of 15 seconds" as an example that may draw a YELLOW or RED CARD.
[MANUAL, G424] Trapping-adjacent: isolating or closing off "any major element of MATCH play" for >MOMENTARY, same stacking MINOR structure.

### A3.4 Control limit
[MANUAL, G410] **1 SAMPLE or 1 SPECIMEN at a time**, directly or transitively. **CLIPS: no limit.**
CONTROL is (A) fully supported by the ROBOT, or (B) intentionally pushed to a desired location or preferred direction (herding).
Exceptions: (C) **MOMENTARY** excess while collecting inside the **SUBMERSIBLE ZONE**; (D) your own **already-scored** elements are exempt.
[MANUAL, G411] Opponent ALLIANCE SPECIFIC elements: **MOMENTARY only** (<≈3 s).
[MANUAL, VIOLATIONS] G410 → MINOR **per additional element**; G411 → MINOR per element **+ MINOR per element per 5-second interval + MAJOR per element scored while controlled**.

### A3.5 Expansion
[MANUAL, R101] STARTING CONFIGURATION: **18 × 18 × 18 in**, self-contained. Exceptions: preloaded SCORING ELEMENTS may protrude; flexible protrusions up to **0.25 in**.
[MANUAL, R102] May be held by mechanical means and/or by an initialised OpMode pre-positioning servos/motors — **must be self-supporting**, no force on the sizing tool.
[MANUAL, R103] **No weight limit.**
[MANUAL, R104] After the start: **no vertical height limit**; horizontal boundary is a **20 in × 42 in** rectangle coplanar with the TILE floor, which **translates and rotates with the CHASSIS**; the chassis' position and orientation **within** the box is chosen by the team and is then **fixed for all time**.
[MANUAL, G418] In-match enforcement: MINOR if >MOMENTARY, **MAJOR if the over-expansion is used for strategic benefit, including if it impedes or enables a scoring action**.

### A3.6 Opponent interference

| Situation | Rule | Limit |
|---|---|---|
| AUTO, opponent robot wholly in its own half | G404.A | **no contact at all** — MAJOR each occurrence |
| AUTO, pre-set SAMPLE on the opponent's half | G404.B | **no contact** — MAJOR each occurrence |
| AUTO, moving elements across the halfway line | G404.C | forbidden **except inside the SUBMERSIBLE ZONE** |
| Deliberate damage / functional impairment | G421 | MAJOR + YELLOW; RED if they cannot drive |
| Tipping / attaching / entangling | G422 | MAJOR + YELLOW; RED if CONTINUOUS or they cannot drive |
| Pinning | G423 | 5 s, then +5 pts per 5 s |
| Shutting down gameplay | G424 | >MOMENTARY, then +5 pts per 5 s |
| Contact near their NET ZONE | G425 | zero tolerance, **either** robot, **either** initiator — 15 pts |
| Being in their OBSERVATION ZONE | G426 | zero tolerance unless you are being pinned |
| Contact near their ASCENT ZONE, last 30 s | G427 | zero tolerance — 45-pt swing |
| Forcing an opponent into a violation | G210 | MINOR, MAJOR if REPEATED; **the target's foul is voided** |

[MANUAL] The half-field line for G404: "FIELD columns A, B, C constitute the blue side of the FIELD, and columns D, E, F (Figure 9-4) constitute the red side."

### A3.7 Human-player limits
[MANUAL, Table 10-1] **1 HUMAN PLAYER per ALLIANCE** (not per team) — a STUDENT with a badge. If the alliance cannot agree, the "Red 1"/"Blue 1" team's human player is used. DRIVE TEAM = up to 4, at most 1 non-STUDENT; 2 DRIVERS, 1 DRIVE COACH.
[MANUAL, G431] Only the HUMAN PLAYER may introduce or retrieve elements in the OBSERVATION ZONE. **A: any number at a time — there is no human control limit.** B: any orientation, may touch each other. C: AUTO and TELEOP only. D: may not touch an element a ROBOT possesses. E: may reintroduce elements knocked out of the FIELD during an OZ/wall collection attempt. F: may move, but not remove, opponent elements left in their own OZ.
[MANUAL, G432] May not break the FIELD-wall plane while a ROBOT is in the OZ (unless it is DISABLED).
[MANUAL, G433] May not cause an element to exit the OZ into the FIELD — **MAJOR per element**.
[MANUAL, G434] No tools — MINOR per occurrence.
[ORANGE, after G419/G431/G432] G419, G431 and G432 **do not stack**: one FOUL per occurrence per ALLIANCE.
[MANUAL, §10.3.1] Pre-load: **1 SAMPLE or 1 SPECIMEN per ROBOT**, in contact with the ROBOT, not in the OBSERVATION ZONE or NET ZONE.

---

## A4. Which fouls scale, and which escalate

### A4.1 Per-occurrence (charge once per event, can be charged many times a match)
G404 (*each occurrence*), G407 (*per SCORING ELEMENT*), G408 (*per element*), G410 (*per additional element*), G412 (*per element de-scored*), G417 (*per element LAUNCHED*), G419 (*per occurrence*), G425 (*per occurrence*), G430 (*per occurrence*), G431 (*per occurrence*), G432 (*per occurrence*), G433 (*per element*), G434 (*per occurrence*).

### A4.2 Time-stacking (a new foul every 5 seconds the state persists)
**G411**, **G423**, **G424**, **G426**.
[MANUAL, Table 10-6 worked example] the manual's own arithmetic for this pattern: *"A ROBOT in violation of this type of rule for 15 seconds receives a total of 4 [FOULS]"* — i.e. **1 on trigger + 1 per completed 5-second interval**.
`[DERIVED]` G426 stacks on **two axes at once** — time *and* elements touched. 10 s in an opponent's OBSERVATION ZONE while contacting 4 elements = 1 + 2 + 4 = **7 MINOR = 35 points**, from a zone that scores you nothing.

### A4.3 Once per match / state-based
G401, G402, G405, G413, G414, G420 (the ASCENT credit is forfeited for the match, not per attempt), G421, G422, G429.

### A4.4 Automatically escalating on repetition

| Escalator | Rules | Mechanism |
|---|---|---|
| verbal → YELLOW on any subsequent violation **in the event** | G101, G102, G201–G206, G415, G428, G501, G502 | the warning persists across tournament phases [MANUAL, §10.6.1] |
| verbal → MAJOR if **REPEATED** (>1 in a MATCH) | G209(damage path), G210, G409 | |
| MAJOR → +YELLOW on any subsequent violation in the event | G402, G405 | |
| MINOR/MAJOR → YELLOW if "excessive" / ">MOMENTARY" / "CONTINUOUS" | G410, G416, G429, G414(→RED), G422(→RED) | |
| YELLOW → RED automatically | **all of them** | [MANUAL, §10.6.1] "YELLOW CARDS are additive… a second YELLOW CARD is automatically converted to a RED CARD", **including two in a single MATCH** |
| Anything → YELLOW/RED at discretion | **G211** | the universal escalator; Head REFEREE may card any rule |

[MANUAL, §10.6.1] YELLOW cards clear at the end of qualification matches and at the end of division playoffs. **Verbal warnings do not clear** — they persist into later phases. `[JUDGMENT]` That asymmetry is the trap: three "harmless" verbal warnings on Saturday morning mean your first real mistake in playoffs is a card.
[MANUAL, §10.6.3] In playoffs, cards attach to the **whole ALLIANCE**; 2 YELLOWs → the alliance is RED-carded and disqualified.

---

## A5. What each tier costs the opponent's score

[MANUAL, Table 10-4]

| Tier | Effect on the opponent's score |
|---|---|
| **MINOR FOUL** | **a credit of 5 points towards the opponent's MATCH point total** |
| **MAJOR FOUL** | **a credit of 15 points towards the opponent's MATCH point total** |
| **YELLOW CARD** | 0 points. A warning; a second YELLOW in the same tournament phase becomes a RED |
| **RED CARD** | the carded team is **DISQUALIFIED** for that MATCH |
| **DISABLED** | 0 points directly; the robot is inoperable for the rest of the MATCH |
| **DISQUALIFIED** | **0 MATCH points and 0 RANKING POINTS** in a qual; the whole ALLIANCE gets 0 MATCH points in a playoff |

[MANUAL, Table 10-3 — the only source of point values]

| | AUTO | TELEOP |
|---|---|---|
| PARK, OBSERVATION ZONE | 3 | 3 |
| SAMPLE, NET ZONE | 2 | 2 |
| SAMPLE, LOW BASKET | 4 | 4 |
| SAMPLE, HIGH BASKET | 8 | 8 |
| SPECIMEN, LOW CHAMBER | 6 | 6 |
| SPECIMEN, HIGH CHAMBER | 10 | 10 |
| ASCENT LEVEL 1 | 3 | 3 |
| ASCENT LEVEL 2 | — | 15 |
| ASCENT LEVEL 3 | — | 30 |
| RANKING POINTS | Tie 1 · Win 2 | |

### A5.1 The exchange rate `[DERIVED]` — operands from Table 10-3 and Table 10-4

| Foul | = how much scoring | Arithmetic |
|---|---|---|
| 1 MINOR (5) | 2.5 NET ZONE samples | 5 ÷ 2 |
| 1 MINOR (5) | 1.25 LOW BASKET samples | 5 ÷ 4 |
| 1 MINOR (5) | 0.83 LOW CHAMBER specimens | 5 ÷ 6 |
| 1 MAJOR (15) | 1.9 HIGH BASKET samples | 15 ÷ 8 |
| 1 MAJOR (15) | **1.5 HIGH CHAMBER specimens** | 15 ÷ 10 |
| 1 MAJOR (15) | 1 LEVEL 2 ASCENT | 15 ÷ 15 |
| **G427 violation (45)** | **1.5 LEVEL 3 ASCENTS**, or 4.5 HIGH CHAMBER cycles | 15 + 30 = 45; 45 ÷ 10 |

**Headline `[DERIVED]`: one MAJOR FOUL costs more than the single most valuable repeatable scoring action in the game.** A HIGH CHAMBER specimen pays 10; a MAJOR pays the opponent 15. There is no defensive action in this manual whose penalty is cheaper than the scoring it denies, with one arguable exception (F11 below), and that one fails the ethics test.

### A5.2 Is defence rational this season? `[DERIVED]` — No.

Take the strongest case for defence: a 15-second pin on an opponent running HIGH CHAMBER cycles.
- Cost: G423 stacking, 15 s → **4 MINOR = 4 × 5 = 20 points** credited to them (Table 10-6 worked example + Table 10-4).
- Benefit: 15 s of denial. At an optimistic 12-second HIGH CHAMBER cycle that is **1.25 cycles × 10 = 12.5 points** denied.
- Net: **−7.5 points**, before any card risk, before G424 stacking on top, before the [ORANGE] 15-second card threshold.
Do the same sum at 5 s: cost 1 MINOR = 5; denial ≈ 0.42 cycles × 10 = 4.2. **Net −0.8.** Defence is negative at every duration on the curve. `[JUDGMENT]` For a two-robot program that also needs award evidence, dedicated defence is off the table; *positional* defence (occupying a cycle lane without contact) is the only version that survives the arithmetic.

### A5.3 The ranking multiplier `[MANUAL, Table 13-1]`
Qualification ranking sorts: **1st** RANKING SCORE · **2nd Average ALLIANCE AUTO Points** · **3rd Average TELEOP ALLIANCE ASCENT Points** · **4th Highest MATCH Score (including FOULS)** · 5th random.
`[DERIVED]` Fouls you *receive* raise your own 4th-order tiebreaker, which is nearly worthless. Fouls you *commit* lower the opponent's need to score, which is worth a lot. And **AUTO and ASCENT are the two tiebreakers the manual chose** — so AUTO points and ASCENT points are worth more than their face value in the standings. That is a season-shaping fact and it comes out of the ranking table, not the scoring table.

---

# PART B — The loophole hunt

Run per `LOOPHOLE-PLAYBOOK.md` §2, passes 1–7, with §4 (two-robot filter) and §5 (ethics test) applied to every candidate before it was allowed into the table.

**Taxonomy caveat.** The playbook's §7 table demands a taxonomy type, but the T1–T15 taxonomy itself lives in the forbidden casebook. The playbook names eight types in passing — **T1** undefined term, **T2** counting, **T3** timers, **T4** re-acquisition/reset, **T5** scored-live vs at-end, **T6** boundary geometry, **T7/T11** carve-outs and induced fouls, **T12** discretion/penalty arithmetic — and those are the only labels I can use honestly. Anything outside them is marked `T?`.

## B1. Pass log

- **Pass 1 (novel terms, T1).** `caps_NOVEL_ranked.txt` gave 63 tokens. Diffed against §16. The glossary *does* define the season's nouns (SUBMERSIBLE, SAMPLE, SPECIMEN, CLIP, CHAMBER, RUNG, BASKET, and all four zones). The gaps are **adjectives and thresholds, not nouns**: `EGREGIOUS`, `EXCESSIVE`, `de-score`, `herding`, `ALLIANCE SPECIFIC ZONE`, and `SCORING ELEMENT` (defined as "the SAMPLE and the CLIP" while SPECIMEN is separately called a SCORING ELEMENT). → **F7, F8**.
- **Pass 2 (orange rules).** All 15 game-specific G-rules + R104 read end to end; each written as "prevents X, therefore permits Y". → **F2, F3, F4, F5, F6, F9, F10, F12**.
- **Pass 3 (tripwire triage).** 312 lines, 5 categories. Counting words → F7/F8. Timers → F5/F6/F13. Carve-outs → F3, F9. Scored-live → **F1**.
- **Pass 4 (zone geometry, T6).** Figures p046 (Fig 9-2 zones), p047 (Fig 9-3/9-4 TILE grid) plus §9.2 measurements. → **F5, F6, F12**. **Blocked:** Figures 11-1/11-2/11-3 (the G427 protected/not-protected illustrations, pp. 86–87) and Figures 12-1/12-2 (R104 expansion examples, p. 94) were **not rendered** — the figure set stops at p. 70. See Beta feedback.
- **Pass 5 (the compounding question, T5).** → **F1**, the highest-value single finding in this manual.
- **Pass 6 (structural cross-check).** Glossary vs rule body (F7, F8), orange box vs rule (F13), scoring action with no governing rule (F4), R-rule vs G-rule (F10, F12), penalty with no detection (F14).
- **Pass 7 (penalty arithmetic, T12).** → §A5, **F11**, **F14**.

## B2. Findings — the §7 table

Ranked by (value × confidence × duplicability for two robots). 14 findings. Category per `ANALYSIS-PROTOCOL.md` R6: **(a)** legitimate reading · **(b)** ambiguity to ask about · **(c)** violates the spirit — never build.

| ID | rule id(s) | type | what the text permits | conf. | our exposure | our opportunity | Q&A? | fallback if patched |
|---|---|---|---|---|---|---|---|---|
| **F1** | §10.5 + Table 10-3 | T5 | Achievements are "officially scored **at the end of each MATCH period** based on the status of the FIELD". Nothing excludes AUTO-scored elements from the TELEOP evaluation → an element scored in AUTO and left alone is counted **twice** | med **(b)** | if wrong, we over-invest in AUTO | HIGH CHAMBER 10+10=**20**; HIGH BASKET 8+8=**16**; PARK 3+3=**6** — AUTO becomes the highest-density period in the match | **YES — #1** | AUTO still pays face value with the *same* hardware; only the priority order changes. Zero hardware cost either way |
| **F2** | 10.5.3 Table 10-2 + G427 | T? | **LEVEL 1 ASCENT = "ROBOT is in contact with the LOW RUNG at the end of a MATCH period"** — no support requirement, no height requirement beyond touching a bar whose top is 20 in up. Same 3 points as PARK | **high (a)** | none | 3 points (6 if F1 holds) from a **fixed passive hook**, no motors — and it happens in the ASCENT ZONE, which G427 protects in the last 30 s, whereas **PARK is protected by nothing** | no | PARK (identical 3 pts) |
| **F3** | G410 + §9.7.2/9.7.3 | T2 | "**There is no limit to the number of CLIPS a ROBOT may possess**", and a CLIP may be joined to a SAMPLE "by a HUMAN PLAYER **or ROBOT**". Attaching a CLIP converts a SAMPLE into a SPECIMEN — it does not add an element | **high (a)** | a clip magazine is dead weight if we never build the clipper | on-board clip magazine + clipper → make SPECIMENS without the OBSERVATION-ZONE round trip. HIGH CHAMBER is the top repeatable score at 10 | maybe | human-player clipping in the OZ — the baseline path, already required as a backup |
| **F4** | G412 (A/B/C only) | T? | G412 protects exactly three things: SAMPLES in the NET ZONE, SAMPLES in BASKETS, SPECIMENS **fully clipped** onto CHAMBERS. **PARK and ASCENT are protected by no de-scoring rule at all** | **high (a)** | an opponent can legally shove us out of our own OBSERVATION ZONE at 0:00 without entering it (G426 only bars *being in* the zone) — 3–6 points gone | choose **LEVEL 1 ASCENT over PARK** (F2): it is worth the same and G427 makes contact there a 45-point mistake for them | no | park early and deep, in the corner of the zone furthest from traffic |
| **F5** | G427 + G210 [ORANGE] | T7/T11 | G427 is "**regardless of who initiates contact**" and covers "**any part of either ROBOT**". [ORANGE after G210] blesses "a red ROBOT ASCENDING in their ASCENT ZONE in the final 30 seconds contacts a blue ROBOT" as *standard gameplay* — so the ascending robot is **not** a G210 violator | **high** — exposure **(a)**, weaponising it is **(c)** | **the single largest penalty in the manual, 45 points, and it can be drawn onto us by an opponent simply coming home to climb** | none we will take. Deliberately drawing this is category (c) | no | **driver rule: from the 30-second "Train Whistle" audio cue, both ASCENT ZONES that are not ours are no-go** |
| **F6** | G425 + G210 [ORANGE] | T7/T11 | Same shape, NET ZONE, **all match**. [ORANGE after G210] blesses "a red ROBOT attempts to enter their NET ZONE to place a SPECIMEN and pushes a blue ROBOT **that was less than 1 TILE away**" as standard gameplay | **high** — exposure **(a)** | 15 points, any time, for loitering. The NET ZONE tape is only 22.75 in from the corner; **one TILE = 24 in** | none we will take | no | **driver rule: never idle within one TILE (24 in) of either opponent NET ZONE corner** |
| **F7** | G410 body vs §16 CONTROL vs [ORANGE] | T1/T2 | Three different definitions of CONTROL. Rule body: herding "**often with a concave surface**". Glossary: "moving the SCORING ELEMENT in a preferred direction with a **flat or concave** face" = CONTROL, and adds "**stuck in, on, or under the ROBOT**". [ORANGE] PLOWING via "a flat or **convex** surface" = *not* CONTROL, but only when **inadvertent** | med **(b)** | a **flat** pusher plate is CONTROL under the glossary; a SAMPLE wedged **under** our chassis is CONTROL under the glossary but arguably not under G410.A. Either gives us MINOR fouls we never intended | build the front face **convex**, and floor the chassis so nothing can wedge underneath. Costs nothing, removes a whole foul class | **YES — #2** | a strictly single-element active intake; the convex face is free either way |
| **F8** | G410 violation ("if excessive") | T1/T12 | The binding text sets **no threshold** for "excessive". The only numbers — "3 or more simultaneous" and "more than twice in a MATCH" — live in a **non-binding orange box** | med **(b)** | our YELLOW-card exposure on the control limit is defined by commentary the manual says does not carry the weight of a rule (§1.7.1) | none — this is purely a risk to bound | **YES — #3** | design so we are never near the threshold: one element, one intake, always |
| **F9** | G410.C + SUBMERSIBLE ZONE | T3/T7 | "ROBOTS may **MOMENTARILY** exceed CONTROL limits while collecting SAMPLES that are in the SUBMERSIBLE ZONE" — MOMENTARY ≈ 3 s | **high (a)** | none if we respect ~1.5 s | a **forgiving wide intake** inside the submersible: scoop several, keep one, shed the rest within the window. This is the difference between a 90 %-reliable intake and a 60 % one, and it duplicates perfectly | no | narrow single-element intake — slower, still works |
| **F10** | G417 + §16 LAUNCH + [ORANGE] | T1 | LAUNCH = "shooting into the air, rolling/kicking across the floor with an active mechanism, or throwing in a forceful way". [ORANGE] exempts "running an intake in reverse causing a SCORING ELEMENT to travel a **short distance**" and herding "a short distance" | med **(b)** | "short distance" is undefined; a spitter that clears the 25.75-in LOW BASKET lip from below may read as a launch to one referee and an intake-reverse to another | a **short-throw ejector** into the LOW BASKET avoids building a 43.0-in lift for the HIGH BASKET. Compliant wheels + one motor duplicates trivially | **YES — #4** | a slow arm/lift to the LOW BASKET lip, or pivot the whole strategy to SPECIMEN + CHAMBER |
| **F11** | G417 vs Table 10-3 | T12 | **The uncomfortable question, asked and answered.** G417 costs **MINOR (5) per element LAUNCHED** — hit or miss. HIGH BASKET pays **8**. So a launcher nets +3 per successful shot in TELEOP | high — **category (c)** | **an opponent may do this to us.** Their 5-point gift does not offset an 8-point basket in a close match | **none. We will not build this.** At 70 % accuracy the real expectation is 0.7 × 8 − 5 = **+0.6 points per shot**, and G211 lets the Head REFEREE card it as egregious. It fails the arithmetic *and* the §5 test — you cannot explain a deliberate repeat foul to a referee | no | n/a — logged so we recognise it when it is used against us and can cite G417 + G211 in the Question Box |
| **F12** | R104 + G418 + [ORANGE after R104] | T6/C13 | Inspection verifies R104 with the **chassis stationary in a fixed 20 × 42 in taped box**, and explicitly states that "additional software within the OpMode designed for **emergency overrides, troubleshooting, or maintenance**… will not be evaluated as part of this compliance check" | **high (a)** | **legal at inspection, MAJOR FOUL in a match.** If an override is bound to a live gamepad input and a driver hits it, G418 charges 15 for an over-expansion that "enables a scoring action" | **there is no vertical height limit** (R104.A) — vertical is free, horizontal is the scarce resource. Place the chassis at one end of the 42-in box and spend the whole 24 in of surplus on one arm, in one direction, permanently | no | shrink the reach; the chassis-placement decision is a bolt pattern, not a rebuild |
| **F13** | G418 [ORANGE] vs R104 | T12 | The binding limit is **20 × 42 in**. The orange box tells referees to gauge expansion in the field against "TILES are approximately **24 in**" and "RUNGS… are **44.5 in** wide" | med — exposure **(a)** | **the measuring sticks do not match the rule.** A legal 42-in extension is 1.75 tiles and *looks* like two; a legal 20-in extension is 0.83 tiles and *looks* like one | build visibly inside the limit (target ≈38 in, ≈78 % of a rung), and keep the R104 inspection photo on the cart for the Question Box | no | reduce reach — a software limit change, not a hardware one |
| **F14** | T201 + T302 + G211 | T12 | [MANUAL, T201] "No event staff, including the Head REFEREE, will review video, photos… **under any circumstances**." [MANUAL, T302] "FIRST instructs REFEREES **not to self-track details** about MINOR FOULS and MAJOR FOULS; as a result, we do not expect REFEREES to recall details about what… fouls were made, when they occurred, and against whom" | **high (a)** | **fouls are unappealable and unauditable.** There is no mechanism to get a wrong call reversed, and none to find out what a call was for | **never let the match plan depend on a margin of one MINOR FOUL.** Send one student to the Question Box with the *rule id* written down — a specific citation is the only currency that works when nobody can recall the incident | no | n/a — this is a permanent operating condition |

## B3. The two-robot filter (§4) applied

| Finding | Build it twice? | Survives a Team Update? | Award evidence? | Verdict |
|---|---|---|---|---|
| F1 | n/a — a priority, not a part | yes; the fallback costs nothing | Think (trade-off analysis on AUTO value) | **adopt as a planning assumption, re-decide on the Q&A answer** |
| F2 | **yes** — a passive hook is the most duplicable part on the robot | a patch would have to redefine LEVEL 1 | Design (elegance, simplicity) | **adopt** |
| F3 | yes, if the clipper is a printed fixture and not a hand-tuned mechanism | a CLIP possession limit is a plausible TU | Innovate (creative, unique) + Control | **adopt with a named fallback** |
| F4 | n/a — a strategy choice | robust | Think | **adopt** |
| F5, F6 | n/a — driver discipline | robust (they are the rules, not gaps) | Control (a 30-second-cue behaviour is a documentable control decision) | **adopt as driver rules** |
| F7, F8, F10 | n/a — Q&A submissions | — | Think (documenting the questions we filed is engineering content) | **file 28 Sep 12:00 ET** |
| F9 | yes | the MOMENTARY carve-out is explicit text, unlikely to be removed | Innovate | **adopt** |
| F11 | **rejected on ethics before the filter** | — | **negative** — cannot appear in a portfolio | **do not build** |
| F12, F13 | n/a — inspection discipline | robust | Design + Control | **adopt as checklist items** |
| F14 | n/a | permanent | — | **adopt as an operating condition** |

## B4. Ethics test (§5) — "would you explain this to the referee at the driver's meeting?"

| Finding | Explain it out loud? | Verdict |
|---|---|---|
| F1, F2, F3, F4, F9, F12 | Yes, gladly — these are readings of the text, and every one of them is a sentence we would put in the portfolio | **(a) legitimate** |
| F5, F6, F13, F14 | Yes — they are self-imposed restrictions | **(a) legitimate** |
| F7, F8, F10 | Yes — we are *asking* the referee, in writing, before the season | **(b) ask** |
| **F11** | **No.** Its entire value depends on committing a foul repeatedly and hoping the arithmetic beats the referee's patience | **(c) EXPOSURE, not a plan** |
| Deliberately entering an opponent's NET/ASCENT zone to draw G425/G427 | **No** — and G210 forbids it explicitly ("actions clearly aimed at forcing the opponent ALLIANCE to violate a rule"), with the [ORANGE] examples naming trapping in your own ASCENT ZONE and pushing a robot into your own OZ | **(c) EXPOSURE, not a plan** |

**Our defence when it is done to us:** G210's binding sentence — "**Rule violations forced in this manner will not result in an assignment of a penalty to the targeted ALLIANCE.**" That sentence, quoted, is what goes to the Question Box.

## B5. The Q&A queue — file 28 September 2026, 12:00 p.m. ET (Lead Coach account)

1. **(F1)** §10.5 says accomplishments are scored at the end of *each* MATCH period. If a SAMPLE is in the HIGH BASKET at the end of AUTO and remains there at the end of TELEOP, is it counted in both the AUTO and the TELEOP totals?
2. **(F7)** G410 defines CONTROL by herding "often with a concave surface"; §16 defines it as a "flat or concave face" and adds "stuck in, on, or under the ROBOT"; the orange box after G410 says plowing "via a flat or convex surface" is not CONTROL. Which governs when a ROBOT deliberately moves a second SAMPLE with a **flat** face? And is a SAMPLE wedged under the chassis CONTROL?
3. **(F8)** G410's violation escalates to a YELLOW CARD "if excessive". The only thresholds appear in a non-binding orange box. What is the binding threshold?
4. **(F10)** Does an intake run in reverse that moves a SAMPLE ~10 in vertically into the LOW BASKET constitute LAUNCHING under G417, given the orange-box carve-out for elements travelling "a short distance"?
5. **(F4)** Is contacting an opponent ROBOT that is partially inside its own OBSERVATION ZONE, while the contacting ROBOT remains entirely outside that zone, a violation of any rule?
6. **(F5)** If our own ROBOT and our own HUMAN PLAYER are simultaneously in our OBSERVATION ZONE, which of G419/G432 is charged, and to whom? (The orange box says they do not stack, but does not say who yields.)

## B6. Rule-change exposure list — input to rubric factor F16

| If a Team Update patches… | …this dies | …this survives | Cost to us |
|---|---|---|---|
| AUTO elements no longer re-counted in TELEOP (**F1**) | the AUTO-first priority order | every piece of hardware; AUTO still pays face value | **zero hardware** — the reason F1 is safe to plan around |
| A CLIP possession limit added to G410 (**F3**) | the on-board clip magazine | the SPECIMEN scoring path via the HUMAN PLAYER | one printed magazine, ~1 build day |
| "Short distance" defined narrowly under G417 (**F10**) | the short-throw ejector | the drivetrain, the intake, the NET ZONE path | one mechanism; fall back to an arm or to SPECIMENS |
| The G410.C submersible MOMENTARY carve-out removed (**F9**) | the wide forgiving intake | a narrow intake, slower | intake rebuild, ~2 build days |
| LEVEL 1 redefined to require support (**F2**) | the passive hook | PARK, identical value | one bracket |
| G427 exception (B) 7-in threshold changed | our endgame approach geometry | everything else | driver retraining only |

`[JUDGMENT]` **No finding in this register is load-bearing.** Every one has a fallback that costs at most two build days, which is the whole point of §4.2 of the playbook. Nothing here becomes a design commitment on its own.

---

## Beta feedback

**What the harness got right.** The ingest is clean and the feed order works. `rules_full.tsv` separating `body` from `violation` is the single most useful artifact in the bundle — it made the A1 table and the whole of §A4 mechanical. `VIOLATIONS.tsv` as a standalone file is what makes §A4/§A5 possible in minutes. `ORANGE_BOXES.md` labelling non-binding text is exactly the guard rail the protocol says is the most common failure mode, and it worked. `TABLES.md` recovered Table 10-3 correctly — verified against figure p066 — while `full_layout.txt` mangled the same table into "`PARK OBSERVATION ZONE 3 3 2`" and "`SPECIMEN NET ZONE 2 2`". **The "never take point values from flat text" house rule is not paranoia; it is load-bearing, and this run proves it.**

**1. The allowed method file leaks the answers.** `LOOPHOLE-PLAYBOOK.md` is on the allowed list but its worked examples are this season's findings: it names G427 as "the canonical shape", tells me HIGH CHAMBER is 10 and HIGH BASKET is 8 with a 43.0-in lip, states G423's pin limit is 5 s, and gives away Pass 5's answer outright ("ITD Q&A Q21 confirmed every AUTO element doubled"). Three of my top four findings were pre-announced. Logged in §0.1 and independently derived, but **the beta result for those findings is unusable**. For BIOBUZZ the fix is either to strip season-specific examples from the method files or to accept that the method files are answer keys too.

**2. Two protocol steps dead-end in forbidden files.** `ANALYSIS-PROTOCOL.md` R5 step 2 requires the archetype list from `PENALTY-AND-ENFORCEMENT.md` §3, and R6 requires the T1–T15 taxonomy and Parts C/F of `LOOPHOLE-CASEBOOK.md`. Both are on the forbidden list, so R5 and R6 as written **cannot be run from the bundle alone**. Substitutes I used, both season-agnostic and both recommended for the harness: (a) **the manual's own §11 subsection headings are the archetype list** — Personal Safety / Conduct / Pre-MATCH / AUTO / TELEOP / SCORING ELEMENT / ROBOT / Opponent Interaction / Human / Post-MATCH — recoverable from the section markers embedded in the rule bodies; (b) for the taxonomy, use only the type labels the playbook itself names. Please emit the §11 heading map as a bundle file (`SECTION_MAP.txt`); it is trivially derivable at ingest and it removes the dependency.

**3. The figure set stops at page 70 and omits every figure a rules phase needs.** MANIFEST covers pp. 43–70 (Game Overview, ARENA, Game Details). The figures I actually needed were **Figure 11-1/11-2/11-3 (pp. 86–87), the protected-vs-not-protected illustrations for G427** — the highest-penalty rule in the manual, 45 points, with a "~7 inches" threshold whose meaning is *defined by those pictures* — and **Figures 12-1/12-2 (p. 94), the R104 expansion examples**. The ARENA figures answer field layout; the *rule* figures answer enforcement. **Recommendation: render figures for the G-rule and R-rule sections too, or at minimum any page whose rule body contains the string "Figure".** F5 and F12 are both lower-confidence than they should be because of this.

**4. `TRIPWIRES.txt` line numbers point at `full_layout.txt`, which we are told to avoid.** Every tripwire hit is `<line>:<text>`, and the only way to get context is to open the file the house rules call a last resort. It worked because the snippets are long enough, but the honest workflow is "read the tripwire, then open the forbidden-ish file". Emitting `rule_id` alongside the line number (you already have the mapping — it is in `rules_full.tsv`) would close this.

**5. The glossary is recoverable but only by counting.** §16 is a two-column table that `pdftotext -layout` collapses into a block of terms followed by an offset block of definitions, so `LAUNCH/LAUNCHING` sits on the same line as "generosity of spirit". I recovered CONTROL, PIN, LAUNCH and PLOWING by counting positions — and **F7 and F8, two of my six Q&A questions, depend entirely on that recovery**. This is fragile and it will break silently on a manual with a different column width. **Recommendation: a `GLOSSARY.tsv` (term, definition) in the bundle.** A `caps_NOVEL` frequency list is not a substitute — Pass 1 needs the *definitions*, not the counts, and the current `caps_NOVEL_ranked.txt` is padded with OCR noise (`NADO`, `HIPS`, `FOR`, `PER`, `DEEPSM`) that costs real triage time.

**6. `rules_ADDED.txt` / `rules_REMOVED.txt` / `section_versions.txt` are in the bundle but not in the feed order** and nothing in the task or protocol says what to do with them. They turned out to be useful — `section_versions.txt` shows Section 11 at V12 and Section 10 at V9 against Section 8 at V1, which is a direct signal about which sections have been churned by Team Updates and therefore which rules are already-patched ground. **Recommendation: promote `section_versions.txt` into the feed order as the "what has already been patched" input to R6 Pass 2.** On kickoff day for BIOBUZZ every section will read V0/V1 and the file will be uninformative, which is itself the correct signal.

**7. One protocol assumption did not fit this season's shape.** The playbook's Pass 6 example asks "R801 permits gas shocks; does any G-rule constrain stored-energy launching?" In this manual **R207 and R801 explicitly ban gas springs**, so the prompt sends you looking for a permission that does not exist. The generalised version — *"which stored-energy sources does the R-section permit, and what does the G-section say about propelling elements with them?"* — is the question that actually worked (mechanical springs are unrestricted; G417 is the only constraint, at 5 points per element). Worth rewording in the method file.

**8. Numbers I could not find.** None material. `[UNVERIFIED]`: the manual gives no explicit statement of whether AUTO-scored elements are re-counted in TELEOP (that is F1, and its absence *is* the finding); no definition of "egregious", "excessive", or "de-score"; no stated priority between G419 and G432 when the robot and human player belong to the same alliance; and the ~7 in threshold in G427(B) is anchored to "roughly the length of two SAMPLES" (2 × 3.5 in = 7.0 in, per §9.7.1) rather than to a measured datum — which is a genuine manual weakness, not an ingest one.

**Overall: the harness generalises.** Nothing in the bundle format was shaped around a particular game — the failures above are about *completeness* (figures, glossary) and about *contamination in the method files*, not about the harness assuming the wrong game shape. Fix items 1, 3 and 5 before 12 September and this runs clean on a manual nobody has read.
