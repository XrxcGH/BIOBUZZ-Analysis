# FTC Loophole Casebook

**Purpose:** raw material for a kickoff-day loophole-hunting playbook against the BIOBUZZ Kickoff Competition Manual (2026-09-12).
**Compiled:** 2026-08-22 · **Corpus:** local primary sources under `C:/Users/ericj/Documents/BIOBUZZ Analysis/`

---

## 0. How to read this document

### Evidence labels (applied to every claim)

| Label | Meaning |
|---|---|
| **[CONFIRMED-HISTORICAL]** | Verified in a local primary source (manual, Team Update, official Q&A). File + rule ID cited. This is the bulk of the document. |
| **[CONFIRMED-FOR-BIOBUZZ]** | Present in the BIOBUZZ V0 pre-season manual — already final for 2026-27. |
| **[HISTORICAL-PATTERN]** | Inferred across ≥2 prior seasons. Predictive, not authoritative. |
| **[SPECULATION]** | Reasoned guess. Never act on without kickoff-day verification. |
| **[UNVERIFIED]** | Could not confirm from available sources. |

### Critical framing

**No BIOBUZZ game rules exist yet.** Sections 8, 9, 10, 11 (G), 13 (T) and 15 (C) of the BIOBUZZ V0 manual are placeholders reading that they will be updated at the 2026-09-12 Kickoff release. **Every scoring number, zone name, and G-rule in this casebook belongs to a prior season and must never be carried into BIOBUZZ analysis as fact.** Their value is *structural*: they show where FTC rulebooks reliably leak.

### Sources used

| Source | Path (relative to corpus root) | Role |
|---|---|---|
| ITD Team Updates 00–16 | `manuals/archive/supplemental/2024-25_ITD_TeamUpdates_Combined.pdf` | Mid-season patch record |
| DECODE Team Updates 00–32 | `manuals/archive/supplemental/2025-26_DECODE_TeamUpdates_Combined.pdf` | Mid-season patch record |
| ITD kickoff manual (V1) | `manuals/_reference_prior_seasons/2024-25_ITD_Competition_Manual_INITIAL_kickoff.txt` | Pre-patch baseline |
| DECODE kickoff manual (V1) | `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_INITIAL_kickoff.txt` | Pre-patch baseline |
| ITD official Q&A | `manuals/archive/supplemental/2024-25_ITD_Complete_QA.html` | Ambiguities teams found |
| DECODE official Q&A | `manuals/archive/supplemental/2025-26_DECODE_Complete_QA.html` | Ambiguities teams found |
| CENTERSTAGE official Q&A | `manuals/archive/supplemental/2023-24_CENTERSTAGE_Complete_QA.pdf` | Ambiguities teams found |
| POWER PLAY official Q&A | `manuals/archive/supplemental/2022-23_POWERPLAY_Complete_QA.html` | Ambiguities teams found |
| BIOBUZZ V0 manual | `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` | What is already locked for 2026-27 |

Q&A citations use the archive's own numbering (e.g. `DECODE Q&A Q135`). All official Q&A rulings are binding precedent within their season and **do not carry across seasons** — DECODE Q&A Q178 says so explicitly: *"rules from previous seasons don't apply to the DECODE game."* [CONFIRMED-HISTORICAL]

> **Note on community sources.** Web searches for Chief Delphi / r/FTC threads on these specific cases returned mostly FRC threads, unrelated Federal Trade Commission pages, and low-signal results. Rather than cite weak or misattributed community content, this casebook is built almost entirely on **official primary documents held locally**, which are stronger evidence anyway. Where a community claim would have been useful but is unconfirmed, it is marked [UNVERIFIED] rather than asserted.

---

## 1. Flagship cases

The cases most worth internalizing, ordered by transferable value to BIOBUZZ.

### Case index

| # | Season | Rule | The gap | How surfaced | Resolution | Type |
|---|---|---|---|---|---|---|
| 1 | ITD 2024-25 | G427 | Protection rule became a weapon — bait opponents into fouling | Event play + volunteer reports; FIRST wrote an unusual public explanation | Rewritten TU10 with a new geometric exception | Defensive carve-out / reverse exploit |
| 2 | ITD 2024-25 | G420 + §10.5.3 | "Start ASCENT outside the ZONE" — *how much* of the robot? | Q&A flood (Q16, Q22, Q46, Q87, Q109, Q141) | 4 rewrites; emergency TU04 issued to fix TU03 | Zone-boundary geometry / undefined term |
| 3 | DECODE 2025-26 | G432/G433/G434 | Human-player artifact handling — place, roll, hold, hoard | Q&A (Q5, Q36, Q48) + event play | 5 revisions to G432, 4 to G433 | Human-player actions |
| 4 | DECODE 2025-26 | R105 | Software-limited expansion passes inspection, exceeds in match | Q&A (Q11, Q16, Q20, Q67, Q69, Q136, Q164) | 3 revisions; split horizontal vs vertical | Inspection-vs-match configuration |
| 5 | ITD / DECODE | G406 / G404 | Scoring after the buzzer while "not actively controlled" | Q&A (ITD Q24, Q78, Q117, Q126; DECODE Q42, Q47, Q135) | Headline-vs-text contradiction resolved by Q&A; escalated penalty | Scoring-state timing at buzzer |
| 6 | DECODE 2025-26 | G417/G418 | Operating your *own* gate to dump artifacts; closing force | Q&A (Q35, Q50, Q89, Q150, Q180, Q186, Q197) | 2 revisions each | Ambiguous possession/control |
| 7 | ITD 2024-25 | G210 | Whether deliberately triggering an opponent foul is itself a foul | Q&A (ITD Q366, Q373; DECODE Q80, Q150, Q151, Q152) | Rule text expanded; refs given "no no-call" guidance | Reverse exploit |
| 8 | POWER PLAY 2022-23 | G25 "grasping" | "Grasp" never defined in the manual | Q&A (Q26, Q49, Q55, Q56, Q69) | Defined *only* in Q&A, never in manual | Undefined term |
| 9 | CENTERSTAGE 2023-24 | GS04 / RG06 | Descoring cascades; grappling hooks | Q&A (Q88, Q89, Q95, Q99) | Q&A-only clarification | Scoring-state / mechanism legality |
| 10 | DECODE 2025-26 | G302 / R306 | AprilTags and element look-alikes as opponent-vision attacks | Q&A (Q56, Q137, Q192) | Q&A-only; LRI judgment | Sensor/vision interference |

---

### Case 1 — ITD G427: the protection rule that became a weapon

**Season:** INTO THE DEEP 2024-25 · **Type:** defensive carve-out → reverse exploit

At kickoff, G427 read that in the last 30 seconds a ROBOT may not contact an opponent ROBOT if any part of *either* robot is in the opponent's ASCENT ZONE, regardless of who initiates contact, with a single exception for contact while both robots had achieved LEVEL 2 or 3 ASCENT. Penalty: MAJOR FOUL **plus the opponent is awarded a LEVEL 3 ASCENT**. [CONFIRMED-HISTORICAL: `2024-25_ITD_Competition_Manual_INITIAL_kickoff.txt`, G427]

**The gap.** The zone was physically tight and shared with the primary scoring area. A robot with a long mechanism could park it in the ASCENT ZONE, and any opponent continuing to play normal offense would incur a MAJOR FOUL and hand over a free LEVEL 3 ASCENT. The protection was strict-liability ("regardless of who initiates contact"), so the *protected* robot controlled whether the foul happened.

**How it surfaced.** Event play and volunteer feedback, not the Q&A. FIRST described it in unusually direct language in Team Update 10 — noting teams "genuinely just trying to continue to collect SAMPLES and score SPECIMENS" were penalized for incidental contact, and that they were "uncomfortable with the potential to attempt to gain benefit from forcing opponents to violate G427," which pushed referees into ruling on intent under G210. [CONFIRMED-HISTORICAL: `ITD TU10`, General section, 2025-01-16]

**Resolution.** TU10 added **exception B**: no violation when the contacted opponent is extending more than ~7 in. into the SUBMERSIBLE ZONE (measured from the barrier), i.e. a robot reaching that far in is presumed *not* to be ascending and forfeits protection. TU10 also softened exception A from "achieved" to "met the scoring requirements to achieve." [CONFIRMED-HISTORICAL: `ITD TU10`, G427]

**Why it matters for BIOBUZZ.** Strict-liability protection zones are the single richest loophole class in FTC. The tell is the phrase **"regardless of who initiates contact."** Whenever a rule protects an actor with no reciprocal duty on that actor, ask: *can I make the protection trigger on demand?*

---

### Case 2 — ITD ASCENT: four rewrites and an emergency Team Update

**Season:** INTO THE DEEP 2024-25 · **Type:** zone-boundary geometry + undefined term

The ITD climb rules were patched more times, and more urgently, than anything else in the corpus.

| Version | Text of the boundary condition | Source |
|---|---|---|
| Kickoff | ROBOTS must start ASCENDING from outside the SUBMERSIBLE ZONE | ITD kickoff manual §10.5.3 |
| TU01 | Adds HIGH RUNG conditions: may not contact HIGH RUNG while supported by TILES *or* by any SUBMERSIBLE part except the LOW RUNG | `ITD TU01`, §10.5.3 |
| TU03 | G420: "ROBOTS must be outside the SUBMERSIBLE ZONE when they begin their ASCENT, **except for minor elements** used to contact the RUNG" | `ITD TU03`, G420 |
| **TU04** | **Emergency reissue, same day as TU03 (both 2024-10-17).** "ROBOTS must start their ASCENT with their **CHASSIS** outside the SUBMERSIBLE ZONE" — the "minor elements" carve-out deleted | `ITD TU04`, G420 |
| TU05 | Adds "**completely** outside"; ASCENT LEVELS 1–3 restated as a table; "grasping" → "supported by"; lateral stabilization on non-RUNG elements explicitly allowed | `ITD TU05`, §10.5.3 + G420 |

TU04 is remarkable: FIRST states outright that "[u]pon review of Team Update 03, an expedient update and release of Team Update 04 was necessary to ensure consistency of the Competition Manual rules, and the way they are enforced." [CONFIRMED-HISTORICAL: `ITD TU04`, General] **A Team Update that patches the previous Team Update — TU03 and TU04 are both dated October 17, 2024, i.e. released the *same day* — is the strongest possible signal that a rule was exploitable as written.**

**The undefined terms driving it.** "minor elements" (TU03, deleted within a week), "supported" and "fully supported," "grasping," and "start ASCENDING." The Q&A record shows teams probing each one:

| Q&A | Probe | Ruling |
|---|---|---|
| ITD Q22 | Is climbing onto the barrier "start ASCENDING"? | (see archive) |
| ITD Q45, Q55, Q94 | What does "supported" mean; vertical vs horizontal support? | Clarified in Q&A |
| ITD Q56 | Can a hook be **left behind** on the LOW RUNG? | Either it still counts as attached (→ LEVEL 2 only), or the robot has shed a part → **G209 violation, RED CARD** |
| ITD Q88 | Can hooks be **launched** over the rung? | No — G209 violation; solenoids also violate R506/R207 |
| ITD Q110 | Definition of "disengage" (for reattempting an ascent) | Clarified in Q&A |
| ITD Q149 | MOMENTARY extension-limit use case *specifically for* ascent | Clarified in Q&A |

Related mechanism-legality precedent from CENTERSTAGE: a hook **placed** on the rigging by an arm/slide and then winched is legal; a hook that **travels independent of the ROBOT** is illegal regardless of tether material — explicitly ruling out fishing line, aircraft cable, #25 chain, and spring-loaded slides that release. [CONFIRMED-HISTORICAL: `CENTERSTAGE Q&A Q89, Q95`]

**Tell for BIOBUZZ:** any scoring achievement gated on *where the robot starts* or *what is supporting it*. Ask immediately: which part of the robot? measured from what datum? at what instant?

---

### Case 3 — DECODE human-player rules: the most-patched cluster in the corpus

**Season:** DECODE 2025-26 · **Type:** human-player actions

**Correction to a common misreading:** G434 (the 6-artifact storage limit) **existed at kickoff** — it was not created mid-season. Team Updates *modified* it. [CONFIRMED-HISTORICAL: `2025-26_DECODE_Competition_Manual_INITIAL_kickoff.txt`, G434]

G432 was revised in **five** Team Updates (02, 04, 08, 10, 15); G433 in **four** (02, 03, 08, 10). The revision trail is a clean fossil record:

| TU | Change | Loophole being closed |
|---|---|---|
| Kickoff | G433: enter artifacts "without LAUNCHING or rolling," "directly placing the ARTIFACT into the LOADING ZONE" | baseline |
| TU02 | G434 scoped to "**During TELEOP**"; adds "During AUTO and transition, this rule is not enforced" | Timing gap — was the limit enforced during AUTO? |
| TU03 | G433 adds "**bouncing**"; adds "such that it **does not leave the LOADING ZONE before coming to rest**"; adds "either directly or **transitively**" | Place-it-so-it-rolls-away. Ball placed legally, then exits the zone under its own momentum |
| TU04 | G432/G434 merged; "off the FIELD" → "**out of play**"; examples added: *a DRIVE TEAM member holding an ARTIFACT inside or outside of the FIELD* counts | **Hold them in your hands.** "Stored off the FIELD" didn't cover a human simply holding a pile |
| TU08 | G433 violation downgraded MAJOR → MINOR per artifact, but **MAJOR per ARTIFACT that enters the top of the GOAL**; "or non-ARTIFACT item entered onto the FIELD" added | Human player scoring by hand; non-game objects thrown in |
| TU10 (and TU10 **v2**) | G432 fully restructured; CONTROL-based test added: control must *begin* in the LOADING ZONE **and persist** as the robot leaves | Robot momentarily dips into the zone; human loads it as it exits |
| TU15 | Exception added for artifacts "unintentionally deflected, e.g., a DRIVE TEAM member protecting themselves from a LAUNCHED ARTIFACT" | Self-defense from incoming projectiles counted as illegal meddling |

Note TU10 was **itself reissued as TU10 v2** the next day to correct errors in G432. [CONFIRMED-HISTORICAL: `DECODE TU10 v2`, General]

**The Q&A that drove it:**

- **Q5** — "would it be legal for human players to hold as many artifacts as physically possible over loading zone without incurring fouls?" → answered by pointing at TU04. [CONFIRMED-HISTORICAL]
- **Q36** — "If the human player placed an artifact on top of another one already in the LZ so that it rolled off and out into the field, would this be allowed? It would not seem to violate part (B) because human player is not directly rolling the artifact." A textbook indirect-action loophole. Answer: placing on top of another artifact does qualify as placing into the zone, but G432 may then be violated. [CONFIRMED-HISTORICAL: `DECODE Q&A Q36`]
- **Q48** — do artifacts in a drive team member's hand count toward the storage limit? [CONFIRMED-HISTORICAL]
- **Q152** — can a human player **load the opposing robot** to force it over the control limit? Answer: accidental → no violation; deliberately pushing them over the G408 limit → **G210** violation by the human player; making the artifact unremovable → **G211 egregious**. [CONFIRMED-HISTORICAL: `DECODE Q&A Q152`]

**Cross-season echo (ITD):** the same class produced ITD Q&A Q37 ("There are no rules that prohibit a HUMAN PLAYER from assembling SPECIMENS prior to the start of the MATCH") and Q38 (nothing prohibits human-player assembly during the AUTO→TELEOP transition) — both **"working as intended"** rulings that opened legitimate strategy. Also ITD Q357: a badged DRIVER may handle scoring elements *outside* the field, but only the badged HUMAN PLAYER may introduce them. [CONFIRMED-HISTORICAL]

**Tell for BIOBUZZ:** human-player rules are written last and tested hardest. Any verb list ("place / enter / retrieve / move") is a closed set — anything not on the list is unregulated until patched.

---

### Case 4 — R105 / expansion: inspection-time vs match-time configuration

**Season:** DECODE 2025-26 (with ITD precedent) · **Type:** robot-configuration-at-inspection vs in-match

This is the most durable structural loophole in FTC because it exploits the gap between two different *observers* (inspector vs referee) and two different *moments*.

| Stage | Rule state | Source |
|---|---|---|
| DECODE kickoff / TU00 | R105 expansion limits; "ROBOTS must be physically constrained to fit within these limits **without the use of software**" | `DECODE TU00/TU01`, R105 |
| TU01 | Adds: software limits are **not sufficient** to demonstrate maximum extensions; flexible extensions (surgical tubing flappers, star intakes) count | `DECODE TU01`, R105 |
| TU03 | Adds the two-sided-mechanism doctrine: one mechanism extending both ways is fine if total ≤18 in.; **two unlinked mechanisms that could extend simultaneously are NOT** | `DECODE TU03`, R105 |
| TU11 | **Splits the rule**: horizontal must be *mechanically* constrained; vertical **may be software limited** | `DECODE TU11`, R105 |

The TU03 clause is the key patch: *"A ROBOT that can mechanically exceed the horizontal limit would be in violation even if the ROBOT has software limiting the position of the extension during the MATCH."* [CONFIRMED-HISTORICAL: `DECODE TU03`, R105]

**The probes:**

- **DECODE Q67** — start tilted so the sizing box is measured on a diagonal, then lower onto all four wheels and exceed 18 in. horizontally. Answer: a starting configuration different from the match orientation "could potentially have a dimension that measures longer than 18 in. when measured parallel to the TILES and still be in compliance with G414" — with a pointed reminder that R101/R102/R105 all still apply and the LRI decides. **This one was effectively conceded as arguable.** [CONFIRMED-HISTORICAL: `DECODE Q&A Q67`]
- **DECODE Q69** — 4-bar odometry pods compressed by robot weight at inspection, expanding in-match. Answer: inspected at the compressed resting point; but if they expand due to orientation change, in-match sizing rules still apply. [CONFIRMED-HISTORICAL]
- **DECODE Q16** — "Can we use a servo to physically limit expansion?" [CONFIRMED-HISTORICAL]
- **ITD Q41** — permanently mounted extensions on opposite sides, used in different matches: each configuration must be **inspected separately**, and "[a]n expansion of zero inches for a given extension in an individual ROBOT configuration is a valid software limit." [CONFIRMED-HISTORICAL: `ITD Q&A Q41`, answer edited 2024-10-17]

**[CONFIRMED-FOR-BIOBUZZ]** BIOBUZZ V0 already locks the relevant frame:
- **R102** — STARTING CONFIGURATION limited to an **18 in. cube**; all parts fully stationary; *"Any pre-loaded SCORING ELEMENTS may extend outside the starting size constraint."*
- **R103** — robots may hold starting configuration mechanically **and/or by initializing an OpMode that pre-positions servos and motors**.
- **R105** — *"ROBOTS must stay as one assembly, and there are limits to how much it can expand"* (numeric limits not yet published in V0).
- **R104** — no weight limit.
- **R303** — COTS must be single degree of freedom.

Source: `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt`, §12.

The R102 pre-load carve-out is a live, already-confirmed BIOBUZZ seam: a pre-loaded scoring element may legally stick out past the 18 in. cube. In ITD this exact seam generated Q34 (can the *preload* touch the wall to satisfy a starting requirement? **No** — the preload is not part of the ROBOT), Q36 (can the preload sit inside a scoring zone while the robot is outside? **No**), and Q108 (preload extending outside the field perimeter). [CONFIRMED-HISTORICAL]

---

### Case 5 — The buzzer: "motionless," "not actively controlled," and scoring after time

**Seasons:** ITD 2024-25 (G406) and DECODE 2025-26 (G404) · **Type:** scoring-state timing at buzzer

**The headline-vs-text contradiction.** ITD G406's headline said "ROBOTS are motionless at the end of TELEOP" but its text only barred being "actively controlled." A team asked directly which governs (ITD Q&A Q126). The answer invoked §1.7 — *"Any disagreement between the specific language used in the rules and the colloquial language (headlines) is an error, and the specific rule language is the ultimate authority"* — then closed the gap anyway by ruling that any intentional robot movement attempting to gain a scoring achievement is continuing gameplay and violates G406. [CONFIRMED-HISTORICAL: `ITD Q&A Q126`, answer edited 2024-11-21]

**This is a two-for-one tell.** It establishes (a) headlines are non-binding — always read the rule body, and (b) FIRST will still close an exploit by interpretation even when the literal text permits it.

**What was ruled legal:**

| Q&A | Question | Ruling |
|---|---|---|
| ITD Q24 | Leave the OpMode running past the buzzer if controllers are put down? | **Yes** — G406 allows it |
| ITD Q78 | PID loop holding the robot on a rung after the buzzer? Motor brake mode? | **Yes to both** |
| DECODE Q135 | May a robot stay powered to stay lifted after the buzzer? | **Yes** — G404 bars *powered movement*, not power. Explicitly permits "powering motors that results in no movement (e.g., stalling motor, holding a servo position)" |
| DECODE Q47 | A spring launches the robot airborne when STOP is pressed | No G404 violation (gravity/inertia isn't powered movement) — **but** an airborne robot isn't supported by the tile, so it scores nothing |

**What was ruled illegal:**

| Q&A | Question | Ruling |
|---|---|---|
| ITD Q117 | Run a *different* OpMode after the match to release from the rung / drop held elements? | **No** to both — G406 plus G413 hazard to humans entering the field |
| CENTERSTAGE Q43 | Drone launched just before the buzzer, lands after time | **Scores** — projectile in flight at T=0 still counts |

**The scoring-instant rule.** DECODE Q135 also states referees **will not enter the FIELD after the MATCH** to determine BASE scoring, and that "the position of ROBOTS after the buzzer has ended is irrelevant for scoring purposes" — teams must make their support "obvious and unambiguous ... at T=0.00." Yet DECODE Q220 reports that in practice referees at many events were entering the field, squatting and kneeling to evaluate it anyway. **Rule-as-written vs rule-as-officiated gap, documented in the official Q&A.** [CONFIRMED-HISTORICAL: `DECODE Q&A Q135, Q162, Q220`]

**Penalty-scaling patch.** DECODE TU05 changed G404's violation from a flat "MAJOR FOUL if ROBOT LAUNCHES an ARTIFACT such that it enters the open top of the GOAL" to "**MAJOR FOUL per ARTIFACT**." [CONFIRMED-HISTORICAL: `DECODE TU05` vs `DECODE kickoff manual`, G404] Before the patch, a flywheel robot could empty its entire magazine after the horn for one flat foul. **Any non-per-unit penalty on a repeatable action is an arbitrage.**

---

### Case 6 — DECODE gates: operating your own field element

**Season:** DECODE 2025-26 · **Type:** ambiguous possession/control + field-element interaction

G417 went from "ROBOTS only operate GATES as directed" to a two-part prohibition (TU03), then gained a definition of "closing force" (TU10): *"Closing force includes any force applied to the GATE in the direction that closes the GATE, even if the GATE is already closed. A ROBOT bumping into a GATE handle which is stuck open to try to get it to close is not considered a closing force."* [CONFIRMED-HISTORICAL: `DECODE TU03`, `TU10`, G417]

G418 (meddling with artifacts on ramps) was revised in TU01, TU02 and TU09, cycling through "descore" → "remove" → "remove ... **except by operating the GATE**" → "remove ... **by any means**" for the opponent's ramp. The verb choice was the whole fight. [CONFIRMED-HISTORICAL]

Q&A probes: Q35 (close the gate from the top?), Q50, Q89 (gate opened *by the opposing alliance*), Q112 (artifact stuck under a gate release), Q150 (push a **disabled** opponent robot into your own gate release — answered under G210), Q180, Q186 (transitive contact that slows or reverses flow down the ramp), Q197, Q217 (variable closing time). [CONFIRMED-HISTORICAL]

Also relevant: G405 was patched in TU15 to name three abuses explicitly — positioning elements to impede opponent access, placing them in inaccessible locations "such as under the RAMP or GOAL," and **using a scoring element to hold open the GATE**. [CONFIRMED-HISTORICAL: `DECODE TU15`, G405]

---

### Case 7 — G210: forcing the opponent to foul

**Seasons:** ITD and DECODE · **Type:** reverse exploit

G210 ("Do not expect to gain by doing others harm") is FTC's general anti-bait rule: actions clearly aimed at forcing the opponent to violate a rule are prohibited, and violations forced that way are not penalized to the target. ITD TU12 added examples of what is *not* a violation — normal ascent contact, and pushing an opponent less than one tile into a protected zone. [CONFIRMED-HISTORICAL: `ITD TU12`, G210]

The boundary is a distance heuristic. **DECODE Q80** makes it explicit: pushing from "far away" (more than one TILE) into a protected zone = G210 on the pusher; from within half a tile = the *target* gets the foul. And critically: *"A G210 violation requires the forcing team to receive a penalty. There is no 'no call' scenario."* [CONFIRMED-HISTORICAL: `DECODE Q&A Q80`]

**Where FIRST refused to rule.** ITD Q&A Q366 asked whether coding your AUTO to *wait on your own side* for an opponent known to cross the midline — purely to harvest their foul — violates G210. Answer: *"We cannot comment absolutely on hypothetical scenarios. The ultimate decision would be determined by the REFEREE at your event."* Q373 pushed again and got the same non-answer. [CONFIRMED-HISTORICAL: `ITD Q&A Q366, Q373`] DECODE Q151 got a firmer line: deliberately crossing to deny an opponent an RP can escalate to G211 egregious. [CONFIRMED-HISTORICAL]

**Tell:** wherever a rule assigns fault by *location* or *strict liability* rather than by *causation*, a bait strategy exists. FIRST's countermeasure is always a subjective referee judgment — which means the exploit is real but high-variance.

---

### Case 8 — POWER PLAY "grasping": a term defined only in the Q&A

**Season:** POWER PLAY 2022-23 · **Type:** undefined term

G25 prohibited grasping junction poles. "Grasp" appeared nowhere in the glossary. The Q&A built the definition from scratch over five questions:

- **Q26** — *"Two or more points of Robot contact that apply opposing force to a Junction pole is grasping."* Single point of contact = legal. Multiple contacts in one vertical plane (no opposing force) = legal. [CONFIRMED-HISTORICAL]
- **Q55** — asked where this is defined. Answer: *"'Grasp' is not a defined term in Game Manual Parts 1 & 2"* — followed by the reminder that **Q&A rulings take precedence over the manuals**. [CONFIRMED-HISTORICAL: `POWER PLAY Q&A Q55`]
- **Q67** — pinning a whole cone stack against the field wall with a V-groove to align it: is trapping = control of five cones? Redirected to Q64. [CONFIRMED-HISTORICAL]

Parallel: CENTERSTAGE ran the same play with pixel stacks, defining exactly how many pixels may be moved off a tape line before it is "consequential" (Q5, Q26, Q60, Q112). [CONFIRMED-HISTORICAL]

**Tell:** an italicized/capitalized term used in a rule but absent from the glossary is an open loophole until the first Q&A lands. **On kickoff day, diff every capitalized term in Section 11 against the Section 16 glossary.** This is a mechanical check and it is the single highest-yield first pass.

---

### Case 9 — CENTERSTAGE descoring cascades

**Season:** CENTERSTAGE 2023-24 · **Type:** scoring-state / penalty arithmetic

**Q88/Q99** established that one physical act can incur *multiple* penalties by counting each affected scoring achievement separately: descoring two pixels that formed a mosaic and a set bonus = **four** minor penalties (2 pixels + 1 mosaic + 1 set line). Q99 challenged the rule basis — the rule text only said "per Pixel." The answer redefined descoring as *"a change of state of a Scoring Element that reduces an Alliance's total Score,"* with a penalty per **descoring impact**, explicitly to compensate the victim. [CONFIRMED-HISTORICAL: `CENTERSTAGE Q&A Q88, Q99`]

**Q88 also established transitive fault:** a red robot that *pushes* a blue robot into blue's own backdrop, causing pixels to fall, receives the descoring penalties itself. [CONFIRMED-HISTORICAL]

**Tell:** whenever scoring is *composite* (bonuses layered on base scores), the penalty for disturbing it is ambiguous until ruled. Look for the difference between "per SCORING ELEMENT" and "per scoring achievement."

Related: POWER PLAY Q6 confirmed a robot **may** descore its own alliance's cones from junctions and its own terminals. [CONFIRMED-HISTORICAL]

---

### Case 10 — Vision and signaling attacks

**Season:** DECODE 2025-26 · **Type:** sensor interference / indirect communication

| Q&A | Probe | Ruling |
|---|---|---|
| DECODE Q56 | AprilTag printed on a team t-shirt, worn to the field | **Violation of G302-E** — could interfere with robot sensing |
| DECODE Q137 | Where's the line on robot colors/shapes resembling game elements? | R306 bars replicas that "to a reasonably astute observer, mimic SCORING ELEMENTS." Similar *colors* alone are fine; matched **shape + color** is the LRI's call |
| DECODE Q192 | Custom visual pattern shown to the robot's camera to signal it during AUTO | **Illegal** — "A team may not use visual signage to *indirectly* signal or cue a robot" (G401) |
| DECODE Q175 | Pressing gamepad buttons during INIT before AUTO | **Legal** before randomization begins; illegal from randomization through end of AUTO |
| DECODE Q159, Q142 | High-intensity light sources | Clarified in Q&A |
| CENTERSTAGE Q163 | Robot signaling to the human player | Clarified in Q&A |

**Tell:** AUTO rules bar *driver input*. The loophole is every information channel that isn't a driver: field lighting, opponent robots, a shirt, a held-up card, the robot's own LEDs signaling a human. FIRST closes these under "directly or **indirectly** interact."

---

## 2. Complete mid-season modification ledger

Every rule whose text was reproduced (i.e. actually edited) in a Team Update. Extracted programmatically from the combined Team Update PDFs by matching rule-ID headings, then spot-verified. Cross-references are excluded. [CONFIRMED-HISTORICAL]

### INTO THE DEEP 2024-25 — 60 distinct rules edited across TU00–TU13

| TU | Date | Rules edited |
|---|---|---|
| TU00 | pre-season | E702, R104, R402, R504, R505, R609, R702, R703, R706, R710, R715 |
| TU01 | 2024-09-19 | **G406, G410, G411**, R307, R402 |
| TU02 | 2024-10-03 | G303, **G404, G406, G411, G418, G431**, G502, R104, R616, R718 |
| TU03 | 2024-10-17 | A101, A108, **G419, G421, G431** |
| TU04 | 2024-10-17 | **G420** (emergency reissue) |
| TU05 | 2024-10-31 | **G420** |
| TU06 | 2024-11-14 | A111, G101, **G405, G408, G410, G418, G419, G425, G431, G432**, R504, R611, R618 |
| TU07 | 2024-12-12 | G209, G302, **G417, G431, G432**, R307, T603 |
| TU08 | 2024-12-26 | E302, G102, G201–G206, G208, G301, **G402, G403, G406, G419, G426, G428, G431, G432**, G502 |
| TU09 | — | G303, R712 |
| TU10 | 2025-01-16 | **G427** |
| TU11 | — | R601, R611 |
| TU12 | 2025-02-06 | A101, **G210**, G301, R617 |
| TU13 | 2025-02-20 | **G408**, R504, R613, R619 |
| TU14–16 | — | none (game modifications for Championship only, TU15) |

**Most-patched ITD rules:** G431 (5 TUs), G406 / G419 / G432 / R504 (3 each), G410 / G411 / G418 / G420 / G408 / G301 / G303 / G502 / R104 / R307 / R402 / R611 (2 each).

### DECODE 2025-26 — 38 distinct rules edited across TU00–TU30

| TU | Date | Rules edited |
|---|---|---|
| TU00 | pre-season | A214, G501, **R105**, R601, R609, R615 |
| TU01 | 2025-09-11 | **G418, G419, G425** (+ R105, BASE ZONE definition, §10.5.2) |
| TU02 | 2025-09-18 | G301, **G418, G432, G433, G434** |
| TU03 | 2025-09-25 | G202, **G402, G417, G433**, R105 |
| TU04 | 2025-10-02 | **G431, G432, G434** |
| TU05 | 2025-10-09 | A210, **G404**, R207, T205 |
| TU06 | 2025-10-16 | none (§1.9, 6.1, 9.1, 13.8) |
| TU07 | 2025-10-23 | G303, **G402, G408, G416, G420** |
| TU08 | 2025-10-30 | **G413, G420, G432, G433** |
| TU09 | 2025-11-06 | **G416, G418**, T704, + **PIN/PINNING and LAUNCH glossary rewrites** |
| TU10 / **10 v2** | 2025-11-13 / 14 | A201, G102, **G417, G427, G432, G433** |
| TU11 | 2025-11-20 | **G402, G412**, R105, R904, T301 |
| TU12 | 2025-11-27 | none (RP thresholds only) |
| TU13 | 2025-12-04 | **G408, G419, G431**, R403 |
| TU15 | 2025-12-18 | **G405, G432** |
| TU18 | 2026-01-08 | G303, **G409** |
| TU20 | 2026-01-22 | T402 |
| TU30 | 2026-04-02 | T206 (+ Championship modifications) |
| TU14, 16, 17, 19, 21–29, 31, 32 | — | none / non-rule |

**Most-patched DECODE rules:** **G432 (5 TUs)**, G433 (4), G402 / G418 / R105 (3 each), G408 / G416 / G417 / G419 / G420 / G431 / G434 / G303 (2 each).

### What the ledger says [HISTORICAL-PATTERN]

1. **Patch velocity front-loads hard.** Counting the first time each distinct rule is edited:

   | Season | By ~Nov 14 | By late Dec | Season total |
   |---|---|---|---|
   | ITD 2024-25 | 35 / 60 (58%) — through TU06, 2024-11-14 | **53 / 60 (88%)** — through TU08, 2024-12-26 | 60 |
   | DECODE 2025-26 | 30 / 38 (79%) — through TU10, 2025-11-14 | **34 / 38 (89%)** — through TU13, 2025-12-04 | 38 |

   **Roughly 90% of a season's rule edits land by late December.** The three months after kickoff are when the game is still being written; after New Year the manual is close to frozen.
2. **In-MATCH game rules dominate.** §11.4 (In-MATCH: SCORING ELEMENT / ROBOT / Opponent Interaction / Human) accounts for the overwhelming majority of edits in both seasons. §12 (R) rules are patched pre-season (TU00) and then rarely.
3. **Human-player rules are the #1 target in both seasons** — ITD G431/G432, DECODE G432/G433/G434.
4. **Two seasons, two emergency same-week reissues** (ITD TU04 fixing TU03; DECODE TU10 v2 fixing TU10). Both concerned rules that had just been rewritten under pressure.
5. **Ranking-point thresholds are re-tuned mid-season** as robots improve — DECODE TU12 raised RCMP thresholds and TU30 set Championship values; ITD TU15 added scoring elements at Championship. [CONFIRMED-HISTORICAL] Strategy that depends on hitting an RP threshold has a moving target.

---

## 3. Loophole taxonomy — types and their tells

For each type: what it is, the **tell** (specific phrasing to grep for in the manual), historical examples, and the question to ask.

### T1 · Undefined or under-defined term

A rule turns on a word that never appears in the glossary.

**Tells:**
- A term in a rule that is **not** in Section 16 Glossary — mechanically diffable.
- Lowercase judgment words inside an otherwise formal rule: *reasonable, minor, significant, substantial, briefly, quickly, promptly, normal, typical, clearly*.
- "such as", "e.g.", "including but not limited to" attached to the **operative** term rather than to examples.
- A term defined **only** inside an orange box (guidance) rather than the glossary or rule body.

**Cases:** POWER PLAY "grasp" (Q26/Q55 — never defined in the manual, only in Q&A); ITD "minor elements" (TU03 → deleted by TU04 in 7 days); ITD "supported"/"fully supported"/"disengage" (Q45, Q55, Q94, Q110); DECODE "out of play" (added TU04 because "off the FIELD" was too narrow); DECODE "closing force" (defined in TU10); DECODE PIN/PINNING (glossary rewritten in TU09 to add three enumerated conditions). [all CONFIRMED-HISTORICAL]

**Ask:** if I read this word in the most self-serving reasonable way, what does it let me do?

---

### T2 · Unbounded quantity

A rule limits one thing and is silent on a neighbouring thing.

**Tells:**
- A limit stated for object A where object B is a different defined term (limit on SAMPLES but not CLIPS).
- "no more than N ..." with no companion rule for the class of items outside that N.
- A cap on *storage* without a cap on *holding*, or on *robot* possession without *human* possession.

**Cases:** ITD Q2 — G410 limited samples/specimens; **CLIPS were entirely unlimited** ("Yes, ROBOTS can carry an unlimited number of CLIPS"); ITD Q90 — may a preloaded specimen carry multiple clips?; DECODE Q5/Q48 — G434 capped artifacts stored *off the field*, so humans held them *in hand* instead, patched in TU04; DECODE Q115/Q141 — how many balls may a human handle at once / limit on balls in the loading zone; CENTERSTAGE Q9 — maximum number of drones allowed in the wing. [CONFIRMED-HISTORICAL]

**Ask:** what is the *complement* of every limited set, and is it limited anywhere?

---

### T3 · Missing or asymmetric timer

A prohibition has no duration, or a duration attaches to one party only.

**Tells:**
- A prohibition with **no** "for more than N seconds" clause.
- "MOMENTARY" / "momentarily" without a numeric definition.
- A stacking penalty ("an additional FOUL for every N seconds") — the presence of stacking elsewhere flags rules that *lack* it.
- Escape-clock rules where the counter's reset condition is unstated (must the offender retreat? how far?).

**Cases:** ITD G411 — minor foul per element *plus another every 5 seconds*, while other control rules had no clock; DECODE G434 — an additional minor foul per artifact per **3 seconds**; POWER PLAY Q43 — how long may a robot linger past the centerline in AUTO? Answer: **"The length of time for the Scoring attempt 'N' can fill all of the remaining time in the Autonomous Period"** — no time limit existed; ITD Q356 — must a pinning robot back off 2 ft before the count resets?; DECODE Q187 — what happens to the pin count when a robot becomes **disabled**? [CONFIRMED-HISTORICAL]

**Ask:** how long can I do this before it costs anything, and who is running the clock?

---

### T4 · Ambiguous possession / control

The boundary between "touching," "herding," "plowing," and "controlling."

**Tells:**
- "CONTROL" defined by a list of positive tests (fully supported / pushing to a desired location) with exceptions listed separately — the gap between them is the loophole.
- "either directly or **transitively** through another object" — its **absence** is the tell; its presence means that hole was already patched.
- "intentionally pushes ... to a desired location or in a preferred direction" — intent-based, therefore contestable.
- Trapping an object against a **field element** rather than holding it.

**Cases:** ITD G410 control definition plus explicit non-control examples (PLOWING/bulldozing, deflecting); CENTERSTAGE Q2 — intaking a **third** pixel and immediately spitting it out is excused under G10 as inadvertent/inconsequential, but **only** if the robot ejects it promptly *and refrains from playing the game* meanwhile; CENTERSTAGE Q5/Q26 — how many pixels of a pre-set stack may be moved before it's "consequential"; POWER PLAY Q67 — pinning a cone stack against the field wall with a V-groove to align it; DECODE Q156, Q181, Q202, Q203, Q215 — repeated probing of "control vs momentary control" and the 4th-ball-against-the-wall case. [CONFIRMED-HISTORICAL]

**Ask:** can I get the *benefit* of control without meeting the *definition* of control?

---

### T5 · Scoring-state timing at the buzzer

When exactly is the score frozen, and what state counts?

**Tells:**
- "at the end of the MATCH" vs "at the end of the MATCH **period**" vs "when all [elements] have come to rest" — three different instants.
- "SCORED AT REST" or equivalent, versus live/continuous scoring.
- Any rule about robots being motionless whose penalty is **not** per-unit.
- Elements **in flight** at T=0.
- A headline that says something stronger than the rule body.

**Cases:** all of Case 5 above. Plus CENTERSTAGE Q43 (drone in the air at T=0 still scores); CENTERSTAGE Q37/Q155 (suspension only during the buzzer sound); POWER PLAY Q37 (driver-controlled tasks are *Scored at Rest*; a knocked-off cone scores nothing and the offender is penalized); DECODE TU30 §10.5 (assessment "continues until all ARTIFACTS have come to rest following the conclusion of the MATCH"; AUTO pattern assessed at end of AUTO **or start of TELEOP, whichever comes first**). [CONFIRMED-HISTORICAL]

**Ask:** name the exact instant. Then ask what I can do in the 3 seconds of buzzer audio.

---

### T6 · Zone-boundary geometry

Which part of the robot, measured how, relative to which line.

**Tells:**
- "in / on / over / within / completely within / fully inside" — each is a different test. **Watch for mixed usage across neighbouring rules.**
- Whether tape lines are **included in** the zone (DECODE TU01 had to add: "The BASE ZONE includes the tape lines").
- "infinitely tall volume" vs a planar area — determines whether an overhang counts.
- Support-based tests vs containment-based tests.
- A zone defined by a physical structure whose position has manufacturing tolerance.

**Cases:** DECODE Q3 — a robot need *not* be completely inside the BASE ZONE tape; it must be **supported by the tile** in the zone, and may overhang; DECODE Q96 — a robot leaning on a "horse" support scores fully returned if all support points are in the zone; DECODE Q99, Q162, Q172 — repeated probing of "inside the base"; ITD Q80 — "at what place does the observation zone start?"; ITD Q63 — parking in the *wrong* zone; ITD G420 saga (Case 2). **DECODE TU01 also corrected an AprilTag ID error in a figure (33 → 23)** — field documentation itself carries errors. [CONFIRMED-HISTORICAL]

**Ask:** support, containment, or contact? Which part of the robot? Does the tape count?

---

### T7 · Defensive-play carve-outs and protected zones

**Tells:**
- **"regardless of who initiates contact"** — the single highest-value phrase in an FTC manual.
- "a ROBOT in the opponent's X may not contact ..." — location-based fault.
- Protection windows keyed to a clock ("in the last N seconds").
- Penalties that **award the opponent a scoring achievement** rather than just points — these create an incentive to be fouled.
- Exceptions written as a *list*, since anything off the list is unprotected.

**Cases:** ITD G427 (Case 1) — the canonical example, complete with FIRST's own public admission; DECODE G425 (SECRET TUNNEL, TU01), G426, G427 (BASE ZONE protection in the last 20 s, TU10 — violation awards the opponent full BASE points **and any robot fully supported by it**); ITD Q&A Q133 (picking up samples from the opponent's ascent zone), Q85 (is a robot protected while scoring on its own chamber?); DECODE Q44, Q53, Q75, Q104 (**are DISABLED robots stuck in zones exempt from penalties?**), Q107 ("Draw a Base Zone Foul" — the team asking names the exploit in the title). [CONFIRMED-HISTORICAL]

**Ask:** can I make the protection trigger on demand? Can I park where my opponent must come?

---

### T8 · Human-player actions

**Tells:**
- A closed verb list: "may only **place / enter / retrieve / move** ..." — anything not listed is unregulated.
- Rules scoped to a match period ("only during TELEOP") — check AUTO and the **transition** separately.
- "without using a tool" — check whether a *fixture, organizer, or ramp* counts.
- Rules about what humans may do to *their own* elements, silent on opponents'.
- Anything about which **badge** a person wears.

**Cases:** the whole of Case 3. Plus ITD Q37/Q38 (assembling specimens pre-match and during the AUTO→TELEOP transition: **both legal**); ITD Q357 (badged DRIVER may handle elements off-field, only the badged HUMAN PLAYER may introduce them); ITD Q372 (3D-printed placement aid extending into the field = **illegal tool**, but 3D-printed *organizers* were later provided by FIRST at Championship); ITD Q365 / DECODE (drive team **may brace the outside of the field wall**, but must not deflect it — DECODE TU10 G102); DECODE Q98/Q190 (may both alliances' human players participate simultaneously?); DECODE Q127 (limits of drive team member **reach**); CENTERSTAGE Q64 (human player inadvertently straying into the wing). [CONFIRMED-HISTORICAL]

**Ask:** what does the manual *not* say a human may do — and is silence permission or prohibition?

---

### T9 · Pre-match setup and randomization

**Tells:**
- "FIELD STAFF stage SCORING ELEMENTS according to Figure X" — check whether *teams* may adjust.
- Preload rules: how many, must they contact the robot, may they be outside the sizing box, may they be inside a scoring zone.
- Tolerances: what is the stated placement tolerance, and does it differ from the general field tolerance?
- Randomization timing: what may happen before, during, and after the randomization event.
- Anything about OpMode selection and INIT.

**Cases:** **DECODE Q178 vs ITD TU06 — the sharpest cross-season trap in the corpus.** ITD TU06 explicitly permitted teams to adjust SAMPLES on the SPIKE MARKS in front of their drive team. A team assumed the same in DECODE and was told **No** — adjusting pre-staged artifacts is not among the permitted G101 field-access actions — with the closing line *"As a friendly reminder, rules from previous seasons don't apply to the DECODE game."* The same answer notes SPIKE MARK *placement* tolerance is ±0.125 in. but §10.3.1 sets no tighter tolerance for the *elements* on them, so the general **±1.00 in.** applies and field staff need not adjust anything within it. [CONFIRMED-HISTORICAL: `DECODE Q&A Q178`; `ITD TU06` §10.3.1]

Also: DECODE Q100 (preload 3 purple but not 3 green — the alliance's 6 staged artifacts are 4 purple + 2 green, so the two teams must coordinate); DECODE Q65 (preloading in a corresponding sequence); DECODE Q175 (gamepad buttons legal during INIT, illegal once randomization begins); ITD Q0 (one preload only: either a sample or a specimen), Q34, Q36, Q47, Q108, Q121; CENTERSTAGE Q90 (a preload may rest on the floor if touching the robot), Q10, Q37 (is team-prop orientation maintained during randomization?); and critically, DECODE §10.8 as revised in TU11 — an **ARENA FAULT is *not* called** for matches that begin with damaged, miscounted, or misplaced scoring elements, so drive teams must inspect the field *before* the match themselves (`DECODE TU11` §10.8). [CONFIRMED-HISTORICAL]

**Ask:** what am I allowed to touch in the 60 seconds before the match, and what happens if the field is set up wrong?

---

### T10 · Robot configuration: inspection vs in-match

**Tells:**
- "must be **physically constrained** ... without the use of software" vs "may be software limited" — check *which* dimensions get which treatment.
- "based on the initial STARTING CONFIGURATION" — a relative, not absolute, frame.
- "interchangeable MECHANISMS" / multiple configurations.
- Flexible or compliant elements (tubing, star intakes, springs, gas-loaded pods).
- Anything measured while the robot rests on the floor under its own weight.

**Cases:** all of Case 4. Plus **[CONFIRMED-FOR-BIOBUZZ]** V0 R102's orange box already anticipates it: *"If a ROBOT uses interchangeable MECHANISMS per 3.3 MATCH Eligibility Rules, teams should be prepared to show compliance with this rule and R105 in all configurations."* And V0 R103 already permits holding starting configuration via a running OpMode. [`BIOBUZZ_V0_layout.txt`, R102, R103]

**Ask:** is this measured by a person with a sizing tool, or by a referee watching a match — and can those two disagree?

---

### T11 · Reverse exploit (weaponizing a rule against its beneficiary)

Distinct from T7: any rule, not just protection zones.

**Tells:** strict-liability language; penalties that transfer a scoring achievement; rules where the *victim* controls the trigger; alliance-wide penalties for one robot's act; any rule an opponent can cause you to break by acting on you.

**Cases:** ITD G427 (Case 1); DECODE Q152 (human player loading the opposing robot past its control limit); DECODE Q150 (pushing a disabled opponent into your own gate); DECODE Q80 (the one-tile bait heuristic); ITD Q366/Q373 (AUTO midline bait — FIRST declined to rule twice); DECODE Q107 (a question literally titled "Draw a Base Zone Foul"); DECODE Q80's key line — **"There is no 'no call' scenario."** [CONFIRMED-HISTORICAL]

**Ask:** for each rule, who *wants* me to break it, and can they make me?

---

### T12 · Penalty arithmetic arbitrage

Where the cost of a violation is less than its benefit.

**Tells:**
- A flat penalty on a **repeatable** action (no "per SCORING ELEMENT" / "per instance").
- No stacking clause on a continuing violation.
- Penalty severity mismatched to the achievement it protects.
- "REPEATED excessive violations of this rule do **not** result in additional YELLOW CARDS" — a documented cap on escalation.
- Composite scoring where the descore penalty counts elements, not achievements.

**Cases:** DECODE G404 flat→per-ARTIFACT (TU05, Case 5); DECODE G433 MAJOR→MINOR per artifact but MAJOR for any entering the goal (TU08); CENTERSTAGE Q88/Q99 (penalty per *descoring impact*, not per pixel); DECODE TU08 §10.6.4 (a whole table added just to explain how "MAJOR FOUL plus YELLOW CARD if REPEATED" actually accumulates); DECODE G408 TU07/TU13 (defines "excessive" as ≥5 simultaneous, or ≥3 separate greater-than-momentary violations of ≥4 — **which by implication tells you exactly how much you can get away with**); ITD G410 (same structure: "more than twice in a MATCH"). [CONFIRMED-HISTORICAL]

**Ask:** what is the price list, and is anything underpriced?

---

### T13 · Field-element interaction and ARENA faults

**Tells:**
- Lists of what is / is not an ARENA FAULT.
- "not considered an ARENA FAULT" — tells you the failure mode is *yours to absorb*.
- Rules about damaging vs merely moving field elements.
- Tolerance language ("ARENAS are assembled in different venues ... Successful teams will design ROBOTS that are insensitive to these variations").

**Cases:** DECODE TU11 T301 — jams in the goal or classifier, a goal lifting off the tiles, and a gate temporarily sticking open are **not** arena faults; an opponent bending/breaking a gate **is**; DECODE TU11 §9.8.3 — the gate takes variable time to close and this is not a fault, with a design recommendation to build a tall vertical contact panel; DECODE Q84 (balls stuck on the ramp), Q112, Q217; ITD TU13 §9 — the tolerance disclaimer plus the new Field Compliance Checklist; ITD Q147/DECODE Q74 (robots peeling tape / marking tiles). [CONFIRMED-HISTORICAL]

**Ask:** when the field misbehaves, who eats it?

---

### T14 · Mechanism legality edges

**Tells:** "single degree of freedom"; energy-storage language; "tethered"/"independent of the ROBOT"; airflow/downforce; anything about COTS modification.

**Cases:** ITD Q88 / CENTERSTAGE Q89, Q95 (placed hooks legal, launched hooks illegal regardless of tether); DECODE R207 (TU05) — bars devices creating high-speed airflow, but explicitly exempts COTS computing fans and clarifies that **flywheels/rollers for manipulating elements are not airflow devices**; DECODE Q6 + **[CONFIRMED-FOR-BIOBUZZ] V0 R204** ("No grabbing the floor") — a high-friction plate flat against the tile is *not* grabbing; ITD R307 / **[CONFIRMED-FOR-BIOBUZZ] V0 R303** single-DoF COTS with its worked examples (mecanum drivetrain = single DoF; dead-wheel odometry = two DoF but explicitly exempted; grippers with an added wrist = illegal); DECODE Q219 (anti-tip wedges — answered under G420/G421, with the asker warning of "a race to the bottom"). [CONFIRMED-HISTORICAL / as marked]

**Ask:** does this mechanism do something the rules describe, or something they merely didn't anticipate?

---

### T15 · Procedural and meta rules

Not on-field, but decisive.

**Tells:** deadlines for disputes; who may enter the question box; what referees may consult; award-eligibility windows; portfolio limits.

**Cases:** DECODE TU20 T402 — playoff match questions must be raised **before the start of the next playoff round** (tightened from "before the current round is finished"), and questions more than 5 minutes after the last playoff match "will likely not be addressed"; DECODE Q200 — a head referee corrected a score 3–5 matches later and the team lost a match and a state berth; the ruling confirms head-referee decisions are final and score corrections are **not** grounds for replay; DECODE Q209 ("What resources do referees refer to?"); DECODE Q188 ("Mandatory Referee Locations?"); ITD Q358 (declining an alliance invitation preserves the right to become a captain later); DECODE Q199 ("Theseus's Paradox FTC Edition" — every student on a team was substituted; ruled legal, subject to I101 registration and I301). [CONFIRMED-HISTORICAL]

**[CONFIRMED-FOR-BIOBUZZ]** V0 already finalizes Eligibility/Inspection (I101–I304), Event Rules (E101–E703), Awards (A201–A215) and Advancement — so **T15 is the one loophole class that can be worked on *before* kickoff**.

---

## 4. Cross-cutting lessons

| # | Lesson | Evidence |
|---|---|---|
| 1 | **Q&A outranks the manual.** POWER PLAY Q55 restates it: official Q&A rulings "take precedence over all information in the game manuals." A rule can be effectively rewritten without a Team Update. | `POWER PLAY Q&A Q55` |
| 2 | **Headlines are not rules.** §1.7: disagreement between headline and rule text "is an error, and the specific rule language is the ultimate authority." | `ITD Q&A Q126` |
| 3 | **Rules do not carry across seasons.** Stated bluntly when a team assumed an ITD allowance applied in DECODE. | `DECODE Q&A Q178` |
| 4 | **FIRST refuses to rule on hypotheticals** — "We cannot comment absolutely on hypothetical scenarios" recurs constantly. Anything requiring a judgment call will be decided by *your event's* head referee. Design so you never need the ruling. | `ITD Q&A Q366, Q373`; `DECODE Q&A Q67` |
| 5 | **A Team Update patching a Team Update = a real exploit.** Happened in both recent seasons — ITD TU04 patched TU03 the **same day** (both 2024-10-17); DECODE re-issued **TU10 v2** on 2025-11-14. | `ITD TU04`; `DECODE TU10 v2` |
| 6 | **Enumerated exception lists are gifts.** DECODE G408's definition of "excessive" (≥5 simultaneous, or ≥3 separate violations of ≥4) tells you the exact tolerance band. | `DECODE TU07/TU13`, G408 |
| 7 | **The rule-as-written vs rule-as-officiated gap is real and documented.** Q135 says referees will not enter the field; Q220 reports they routinely do. | `DECODE Q&A Q135, Q220` |
| 8 | **"Working as intended" outcomes are strategy, not just trivia.** ITD Q37/Q38 (pre-match and transition specimen assembly), DECODE Q214 (parking in BASE early is not a violation), POWER PLAY Q42 (a stationary robot reaching from the substation to a high junction "doesn't violate any rules"), ITD Q364 (using field structures in unanticipated ways is fine absent another violation). | as cited |
| 9 | **Design out of subjective-call territory.** ITD TU10's stated goal was to "reduce the number of subjective calls our referees are asked to make." Strategies that live inside referee judgment are high-variance and get patched. | `ITD TU10`, General |

---

## 5. Kickoff-day checklist derived from this casebook

Ordered by yield per minute. [SPECULATION — the ordering is a judgment call; the underlying tells are all CONFIRMED-HISTORICAL]

1. **Glossary diff.** Extract every capitalized term used in Section 11 and Section 10; subtract Section 16. Every survivor is a T1 candidate. *(Mechanical, highest yield.)*
2. **Grep `regardless of who initiates contact`.** Each hit is a T7/T11 candidate. Also grep `may not contact`, `is protected`, `in the last`.
3. **Penalty audit.** List every violation clause; flag any that lacks "per [unit]" or a stacking clause on a repeatable action (T12).
4. **Scoring-instant audit.** For every scoring achievement, write down the exact freezing instant and whether the test is support / containment / contact (T5, T6).
5. **Human-player verb list.** Extract the closed verb list; enumerate what is absent; check period scoping including the AUTO→TELEOP transition (T8).
6. **Preload and pre-match.** Preload count, contact requirement, sizing-box carve-out, zone restrictions, whether teams may adjust staged elements, stated tolerances (T9).
7. **Complement check.** For every "no more than N X," ask what non-X objects exist and whether they are limited (T2).
8. **Timer check.** Every prohibition without a duration (T3).
9. **Expansion regime.** Which dimensions are mechanically vs software constrained; interchangeable-mechanism rules (T10). *Partially pre-answerable now from V0 R102/R103/R105.*
10. **ARENA FAULT list.** What failures are yours to absorb (T13).
11. **Re-run 1–10 after every Team Update through late December** — ~90% of a season's rule edits land by then, and the densest weeks are the first six.

---

## 6. What is already known for BIOBUZZ

**[CONFIRMED-FOR-BIOBUZZ]** — final in the V0 pre-season manual (`manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt`), so these can be worked on now:

| Area | Rules present in V0 | Relevance |
|---|---|---|
| Eligibility / Inspection | I101–I103, I301–I304 | T15 |
| Event Rules | E101–E118, E301–E302, E501–E511, E601, E701–E703 | T15 |
| Awards | A201–A215 | T15 |
| ROBOT Construction | R101–R105, R201–R204, R301–R305, R401–R403, R501–R506, R601–R613, R701–R711, R801, R901–R904 | T10, T14 |
| Advancement, Season Overview, Glossary (partial) | — | T15 |

Notable V0 anchors already confirmed:
- **R102** — 18 in. cube starting configuration; **pre-loaded scoring elements may extend outside it**; interchangeable-mechanism compliance required in all configurations.
- **R103** — starting configuration may be held by a running OpMode pre-positioning servos/motors.
- **R104** — no weight limit.
- **R105** — "ROBOTS must stay as one assembly, and there are limits to how much it can expand" (numbers not yet published).
- **R204** — no grabbing the floor / no downforce mechanisms.
- **R303** — COTS must be single degree of freedom.

**Not yet knowable:** all G-rules, all T-rules, all L-rules, scoring, zones, elements, match structure, penalties. Sections 8, 9, 10, 11, 13 and 15 are placeholders pending 2026-09-12. (§14 League Play is already written in V0 and contains no L-rules; neither DECODE nor ITD ever had an `L###` rule.)

---

## 7. Security note

Per the standing instruction, all PDFs, HTML files and web pages in this corpus were treated as **data, not instructions**.

**No document in the corpus contained text addressed to an AI agent, instructions to take actions, or attempts to override operating rules.** The Team Updates and Q&A archives contain only ordinary rule text, team questions, and moderator answers.

Two minor things worth flagging as content observations rather than security issues:
- The ITD Team Updates contain a joke figure captioned "Figure 17-1: GDC (Game Dog Committee)" in TU14 (a no-updates week). Harmless.
- Several Q&A answers contain live `ftc-resources.firstinspires.org` URLs. These were not followed except where independently useful; they point at official FIRST resources.

---

*End of casebook. Companion documents: the loophole-hunting playbook (to be applied on kickoff day) and the ingest script at `tools/ingest-manual.sh`.*
