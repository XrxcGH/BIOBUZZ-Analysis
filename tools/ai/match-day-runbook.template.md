<!--
  ============================================================================
  MATCH-DAY RUNBOOK — BIOBUZZ 2026-27  ·  small-team edition
  ============================================================================
  WHERE IT LIVES:  events/YYYY-MM-DD-<event-code>/runbook.md
      e.g.         events/2026-11-14-USTXHOQ1/runbook.md

  HOW TO USE IT
    1. Copy this file per event. Fill the header and the CREW table at your last
       meeting before the event -- NOT in the car.
    2. PRINT IT. Two-sided, one copy per crew member, plus one taped to the pit
       table. Sections are sized to break on page boundaries.
    3. It is a WORKING document: the match log, failure log and debrief are
       filled in with a pen, on the day.
    4. On the drive home, one student types the filled pages back into the repo.
       That typed copy is portfolio evidence (Think/Control/Design criteria) and
       feeds tools/ai/PROMPTS-portfolio.md PF1 at the end of the month.

  WHY A PAPER RUNBOOK IN AN AI PLAYBOOK
    Rule E301 forbids teams from setting up ANY Wi-Fi access point, hotspot or
    Bluetooth link in the venue -- "A wireless hot spot created by a cellular
    device, camera, smart TV, etc. is considered an access point." E109 forbids
    arranging venue internet. So on event day you should plan for NO NETWORK and
    therefore NO AI. Everything an agent was going to do for you has to have
    been done, and printed, before you leave the house. That constraint is the
    reason this file exists.
    (See playbook/AI-TOOLKIT-SETUP.md section 9 "The event-day blackout".)

  SOURCES FOR EVERY RULE CITED BELOW
    manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf
    Sections 3 (I-rules), 5 (E-rules), 6 (A-rules), 12 (R-rules) are FINAL in V0.
    Sections 8-11 (game, ARENA, game details, game rules) and 13-14 are
    PLACEHOLDERS until Kickoff, 12 September 2026 -- see the KICKOFF TODO at the
    end of this file.

  A201 PII RULE: first names and last initials only, everywhere.
  ============================================================================
-->

# Match-Day Runbook — Team `<NNNNN>`

| | |
|---|---|
| **Event** | `<name>` · code `<USTXHOQ1>` · `<Qualifier / League Meet / League Tournament / Championship>` |
| **Date** | `<2026-11-14>` |
| **Venue** | `<name, address>` |
| **Doors open / load-in** | `<07:00>` |
| **Quals start (scheduled)** | `<09:30>` → **check-in deadline is 45 min earlier: `<08:45>`** (I102) |
| **Judging format** | `<scheduled in-person / unscheduled in-person / remote>` (§6.1.2 — confirm at check-in) |
| **Departure from home base** | `<05:30>` · **drive time** `<1:45>` · **buffer** `<0:45>` |
| **Responsible adults on site** | `<First L.>`, `<First L.>` — at least 1, preferably 2, **for the whole event** (I103) |
| **Robot inspection status** | self-inspected `<date>` using `tools/ai/inspection-checklist.template.md` |
| **This copy belongs to** | `<First L.>` |

> **Print check:** did you also print — portfolio ×2, pre-event dossier, blank pit-scout cards, blank match log, inspection checklist, this runbook? See §2.

---

## 1. Crew — every seat has a name and a backup

Fill this in **before** the event. A seat with no name is a seat that gets
improvised at 09:20 by whoever is standing closest.

| Seat | Primary | Backup | Owns |
|---|---|---|---|
| **Drive coach** | `<First L.>` | `<First L.>` | Alliance strategy, the clock, the one instruction at a time |
| **Driver 1** | `<First L.>` | `<First L.>` | Controls. Never leaves the queue line to fetch anything |
| **Driver 2 / human player** | `<First L.>` | `<First L.>` | Controls / scoring-element handling |
| **Robot technician** | `<First L.>` | `<First L.>` | The only person who touches the robot at the field. Battery, cables, mechanism reset |
| **Checklist runner** | `<First L.>` | `<First L.>` | Runs §4 out loud, every match, no exceptions |
| **Pit boss / logistics** | `<First L.>` | `<First L.>` | Pit kit, batteries on the charger, queue timing, food |
| **Scout** | `<First L.>` | `<First L.>` | Pit-scout cards, match observations, the tier sheet |
| **Judge crew** (2 students min, A204) | `<First L.>`, `<First L.>` | `<First L.>` | Portfolio copy in hand, ready for an unscheduled visit |
| **Log keeper** | `<First L.>` | `<First L.>` | §7 failure log, within 5 minutes of every failure |

**[FACT]** DRIVE TEAM composition is defined in **Section 10, which is a placeholder in the V0 manual**
(*"will be updated with the Kickoff Competition Manual release on September 12, 2026"*). Plan on the
DECODE-season structure — up to 4 people, at most 1 non-student, badges required — and **re-verify on
kickoff morning**. (`research/TESTING-AND-TUNING.md` §3.2.)

**Minimum-crew rule:** if fewer than 5 students travel, collapse in this order —
scout folds into pit boss, log keeper folds into checklist runner. **Never**
collapse the checklist runner into the technician: one person cannot both
verify and perform.

---

## 2. The night before — load list

Sign each line. An unsigned line is an unpacked line.

### 2.1 Robot and electronics

| ✔ | Item | Qty | Notes / rule |
|---|---|---|---|
| ☐ | Robot, fully assembled, in the configuration you will inspect | 1 | I301: bring **every** component you may use, including decorative parts |
| ☐ | OPERATOR CONSOLE (Driver Station device + gamepads) | 1 | I301 requires it at inspection |
| ☐ | Batteries, **charged**, tested under load | ≥3 | See §5 |
| ☐ | Battery charger(s) + power strip | 1 | Confirm the venue allows your strip; E109 — do not arrange extra power |
| ☐ | ROBOT SIGNS, ≥2, ≥90° apart, ≥6.5 in × 2.5 in, robust material | 2+ | **R401.A–D** |
| ☐ | Spare gamepad | 1 | The most common event-day electronics failure |
| ☐ | Spare motor / servo of each type on the robot | 1 ea | I302: spares count toward the electronics budget only if *used* |
| ☐ | Spare wheels, belts, chain, surgical tubing | — | |
| ☐ | Spare hub / spare wiring harness (if you have one) | — | |
| ☐ | USB-C cable ≥10 ft, plus a spare | 2 | Deploy path when Wi-Fi is unusable |
| ☐ | Laptop + charger, **repo cloned, last known-good build already installed on the robot** | 1 | See §8 |

### 2.2 Paper — because there is no network (E301)

| ✔ | Item | Qty | Produced by |
|---|---|---|---|
| ☐ | Printed PORTFOLIO | 2 | A204 wants a copy on hand for reference; I102.D lists it as a check-in item |
| ☐ | This runbook | 1/crew + 1 pit | — |
| ☐ | Pre-event dossier (every team at this event, OPR percentile, awards, blanks) | 1 | `python tools/ai/scouting/fetch_events.py dossier --season 2026 -e <CODE> -o dossier.csv` |
| ☐ | Blank pit-scout cards | 1/team at event | `tools/ai/PROMPTS-scouting.md` SC3 |
| ☐ | Blank match log (§6) | 1 | This file |
| ☐ | Self-inspection checklist, already filled | 1 | `tools/ai/inspection-checklist.template.md` |
| ☐ | Judge cue card (§10) | 1/judge-crew student | This file |
| ☐ | Team roster from the FIRST dashboard | 1 | **I102.A** — check-in may require it |
| ☐ | Consent / registration forms if your region requires them | — | **I102.B** — varies by region, ask your Program Delivery Partner |

### 2.3 Tools and consumables (fits in one toolbox)

☐ Hex drivers (metric + imperial) ☐ nut drivers ☐ pliers ☐ side cutters ☐ small file
☐ Zip ties ☐ electrical tape ☐ gaffer tape ☐ threadlocker ☐ spare screws/nuts/spacers, sorted
☐ Multimeter ☐ battery load tester ☐ soldering iron *(only if your pit has power and you have practised with it)*
☐ **Safety glasses for every person, plus 2 spares** — **E101.A**, ANSI/UL/CE EN166/AS-NZS/CSA rated
☐ Closed-toe shoes on every foot (E101.B) ☐ hair ties (E101.C)

### 2.4 Do **not** bring (E108)

Skateboards · hoverboards · **drones** · bottled gas (helium) · noisemakers, air horns, whistles,
floor stompers · scooters (except accommodations) · **anything with lights flashing faster than
~5 Hz** · firearms, weapons or realistic prop weapons (E114).
**And per E301: no personal Wi-Fi access point, no phone hotspot, no Bluetooth speaker, no smart TV
with its factory access point still enabled.**

---

<!-- ============================ PAGE BREAK ============================ -->

## 3. The day, in order

Times are relative to **quals start = T0**. Fill the absolute times in the right column at check-in.

| Clock | What happens | Owner | Actual |
|---|---|---|---|
| T−3:00 | Depart. Robot strapped down, batteries **not** in the robot | Pit boss | `<>` |
| T−2:00 | Load in. Find the pit, find Pit Admin, find the practice field, find the restrooms | All | `<>` |
| T−1:45 | **Batteries on the charger the minute you have power** | Pit boss | `<>` |
| **T−0:45** | **CHECK-IN DEADLINE — I102.** An **adult** checks in at Pit Administration; at least one **student** must be at the venue | Adult + 1 student | `<>` |
| T−1:30 | Pit setup: table, signs, portfolio out and visible, tools laid out the same way every event | Pit boss | `<>` |
| T−1:30 | **Inspection.** Present robot + OPERATOR CONSOLE + all components. Demonstrate every configuration (I301) | Technician + 1 | `<>` |
| T−1:00 | Practice field **only after passing full inspection** (E115) | Drivers | `<>` |
| T−1:00 | Pit scouting begins — 90 s per team, dossier in hand | Scout | `<>` |
| T−0:30 | Driver warm-up in the pit *(pit or designated practice area only — E106)* | Drivers | `<>` |
| T−0:15 | **Whole-crew huddle.** Read §4 out loud once. Confirm who does what | Coach | `<>` |
| **T0** | Quals begin | — | `<>` |
| ~T+2:00 | **Lunch = the data window.** Pull matches, recompute, re-tier the pick list (§9) | Scout | `<>` |
| after quals | **Alliance selection** — §9 | Coach + scout | `<>` |
| after playoffs | Awards. **Sit together. Stand up when called.** | All | `<>` |
| end | Teardown. Nothing leaves the venue un-inventoried. §11 debrief in the vehicle | All | `<>` |

**Judging can happen at any point.** If the format is *unscheduled in-person*, judges walk up to your
pit without warning. From the moment doors open, the judge crew is **on call**: phones down, someone
standing, portfolio within reach. (§6.1.2; `research/SCOUTING-AND-AWARDS.md` §13.1.)

---

## 4. The match cycle — read this out loud, every match

The checklist runner reads. The technician performs. **They are never the same person.**

### T−20 min · Queue

| ✔ | Step | Owner |
|---|---|---|
| ☐ | Robot on the cart, **fresh battery installed and strapped** | Technician |
| ☐ | Both gamepads present, cables checked, correct ports | Driver 1 |
| ☐ | Driver Station charged >50 %, correct OpMode list loaded | Driver 1 |
| ☐ | **Alliance strategy agreed in ONE sentence** with both partners; written on the wrist card | Coach |
| ☐ | Auto route chosen and named out loud; both partners know your starting tile | Coach |
| ☐ | Nothing is being fabricated except in a legal place (**E107**: your pit, another team's pit with permission, in the queue with extra safety scrutiny, an event-designated area, or an open machine shop) | Pit boss |

### T−5 min · Field setup

| ✔ | Step | Owner |
|---|---|---|
| ☐ | Robot placed, starting position matches the auto you selected | Technician |
| ☐ | Mechanisms in their start configuration; nothing pre-loaded that shouldn't be | Technician |
| ☐ | **Robot signs visible from ≥2 sides** (R401) | Runner |
| ☐ | Programming laptop **disconnected** from the Robot Controller Wi-Fi (**R704.C**) | Pit boss |
| ☐ | Dashboard / Panels streaming **off** (**R704.D** names FTC Dashboard and FTControl Panels as prohibited) | Driver 1 |
| ☐ | Init run, telemetry sane, no error toast on the DS | Driver 1 |
| ☐ | Coach confirms the one-sentence plan with the drivers, then **stops talking** | Coach |

### During the match

| Phase | Coach says | Coach must NOT |
|---|---|---|
| AUTO | *(nothing)* — watch the **opponents** | Narrate your own auto |
| TELEOP 0–30 s | Field state only: what's where, what they're doing | Call button presses |
| TELEOP middle | **One** instruction at a time. Countdown at 40 s, 30 s, 20 s | Stack three instructions in one breath |
| Endgame | Owns the clock: *"Twelve seconds — go now."* | Panic-narrate |

### T+2 min · Post-match, at the cart

| ✔ | Step | Owner |
|---|---|---|
| ☐ | Battery **out**, straight onto the charger, labelled with cycle count | Technician |
| ☐ | Walk the robot: fasteners, belts, wires, wheels. Hands on every mechanism | Technician |
| ☐ | Match log row filled in (§6) — score, what worked, what didn't | Log keeper |
| ☐ | Any failure → §7 failure log **within 5 minutes**, while the memory is accurate | Log keeper |
| ☐ | One specific positive thing said out loud, then one specific fix named | Coach |
| ☐ | **Debrief in the pit, never on the field** | All |

---

<!-- ============================ PAGE BREAK ============================ -->

## 5. Battery discipline — the cheapest points at any event

Log every pack. A pack you cannot account for is a pack you should not trust in match 9.

| Pack ID | Resting V at load-in | Match # used | V after match | On charger at | Notes |
|---|---|---|---|---|---|
| `A` | `<>` | `<>` | `<>` | `<>` | |
| `B` | `<>` | `<>` | `<>` | `<>` | |
| `C` | `<>` | `<>` | `<>` | `<>` | |
| `D` | `<>` | `<>` | `<>` | `<>` | |

**Rules of thumb (JUDGMENT):** one pack per match, never reused in the same round · a pack that
rests below `<12.0>` V is a practice pack, not a match pack · packs charge in rotation with the
oldest-rested pack going in next · label packs with a paint pen, not tape.

**[FACT]** Your code should already voltage-compensate (`12.0 / batteryVoltage`) — that is in the
`CLAUDE.md` safety list (`tools/ai/CLAUDE.md.template`). Compensation hides a weak pack right up
until it doesn't.

---

## 6. Match log — fill a row per match, in pen

| # | Time | Alliance partner(s) | Opponents | Auto result | Teleop cycles | Endgame | Final score | One thing to fix |
|---|---|---|---|---|---|---|---|---|
| Q`<>` | | | | | | | | |
| Q`<>` | | | | | | | | |
| Q`<>` | | | | | | | | |
| Q`<>` | | | | | | | | |
| Q`<>` | | | | | | | | |
| Q`<>` | | | | | | | | |
| Q`<>` | | | | | | | | |

> **KICKOFF TODO:** replace the middle columns with the actual BIOBUZZ scoring categories once
> Sections 8–11 publish on **12 Sep 2026**. Use `tools/ai/PROMPTS-strategy.md` S1 to derive the
> column set from the real manual, then re-print.

---

## 7. Failure log — within 5 minutes, every time

The single highest-value page in this file. It is also direct Think/Design award evidence, and it
is the input to the next decision-log entry (`tools/ai/decision-log.template.md`).

| # | Match | Time | What failed | What we saw | What we did | Did it work? | Root cause (fill in later) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |

**Write the symptom, not the diagnosis.** "Lift stopped 4 in low, motor was hot" is useful.
"Lift PID broken" is a guess that will send you down the wrong path in the pit and again at home.

---

## 8. Changing the robot at an event — what needs re-inspection

**[FACT — I303, verbatim list.]** Re-inspection is **generally not necessary** for:

| | Change |
|---|---|
| A | addition, relocation, or removal of fasteners (cable ties, tape, rivets) |
| B | addition, relocation, or removal of labeling or marking |
| C | addition, relocation, or replacement of the team SIGN |
| **D** | **revision of ROBOT code** |
| E | replacement of a COMPONENT with an **identical** COMPONENT |
| F | replacement of a MECHANISM with an **identical** MECHANISM (size, weight, material) |
| G | additions, removals, or reconfiguration of the ROBOT with a **subset of MECHANISMS already inspected** |

— *"unless they result in a significant change to the ROBOT'S size, legality, or safety."*
Anything else: **request re-inspection (I303)**. If unsure, ask the LRI or FIELD STAFF — the manual
says so explicitly. **I304: never use re-inspection to get around another rule.**

### Software changes at an event — the discipline

1. **The build on the robot at load-in is the last known-good build, installed over USB, at home.**
   Never let an event build be a hot-reload build (`playbook/AI-FOR-PROGRAMMING.md` §3.9).
2. Code changes at an event are allowed (I303.D) but every change is a risk taken between matches.
   Rank each candidate by **matches lost per occurrence**; fix only the top one.
3. Change **one number or one line**, note it in §7, and say out loud what you expect to see.
4. Full `installDebug` over USB. Verify the version/build string on the DS before you queue.
5. **R704.C: the laptop comes off the Robot Controller Wi-Fi before the robot goes to the field.**
6. If you cannot state the physical failure mode of the change in one sentence, do not deploy it.

---

<!-- ============================ PAGE BREAK ============================ -->

## 9. Scouting and alliance selection

### The lunch window (~10 minutes, offline)

Everything below runs on the laptop with **no network** if you pre-cached the event, and on the
printed dossier if you did not. See `tools/ai/scouting/README.md` §6 (the 45-minute pipeline) and §7
(what the script does and does not do).

| ✔ | Step |
|---|---|
| ☐ | Merge the morning's pit cards + your match observations into the dossier printout |
| ☐ | Recompute OPR / component OPR / last-3 trend **if** you have match data cached |
| ☐ | Re-tier the list — **tiers, not a strict order** |
| ☐ | Cross out anyone you would not accept; circle anyone you must not lose |

### Tier sheet

| Tier | Teams | Why they are in this tier | What we need from them |
|---|---|---|---|
| **A — take immediately** | `<>` | | |
| **B — good, ordered by fit** | `<>` | | |
| **C — acceptable** | `<>` | | |
| **Do not pick** | `<>` | | |

**The rule:** the machine proposes tiers; **humans order within a tier**. Published reports from FRC
mentors say LLM-built pick lists came out *worse than sorting by averages*
(`research/AI-IN-FTC-POLICY.md` §9). Do not outsource this decision.

### At the selection

☐ Two people at the table: one talks, one holds the sheet and crosses off names as they go
☐ Know your fallback three deep before your turn — teams disappear fast
☐ If you are picked: say yes or no in one word, then thank them
☐ Write down **who picked whom** — it is scouting data for the next event

---

## 10. Judge cue card — cut this out and keep it in a pocket

**[FACT]** Judges select **two questions from the FIRST Judging Question Bank** that every team at
the event is asked: one from the MCI award category, one from the TA category
(`research/SCOUTING-AND-AWARDS.md` §13.3). Up to ~5 minutes of uninterrupted presentation is allowed
(A205), then open-ended Q&A. **E116 / §6: no recording during the Initial Interview.**

**Our 5 sentences — say these no matter what is asked**

1. `<Who we are: N students, first year doing X, our constraint is Y.>`
2. `<The one design decision we are proudest of, and the number that justifies it.>`
3. `<The failure we had, what we measured, and what we changed.>`
4. `<What our outreach actually accomplished, with a number we can source.>`
5. `<What we would do differently next season.>`

**When asked "what outside resources did you use?"** — name Claude in the same breath as GM0,
FTCLib/Road Runner/Pedro, goBILDA and your mentors. It is a tool in a list of tools. Then
immediately demonstrate that you understand the thing you used it for. Confident and matter-of-fact;
never apologetic, never concealed (`research/AI-IN-FTC-POLICY.md` §8 DISCLOSE).

**If you do not know an answer:** *"I don't know — `<teammate>` owns that, and here's what I do
know about it."* Judges reward the honest handoff and punish the confident bluff.

**Never:** recite a memorised AI-drafted answer · claim a number you have not verified · say another
team's work looks AI-generated (§1.5.1).

**Pit visit = you were nominated for something.** Notice which award the questions cluster around
and answer *that* award's criteria. Stand up. Phones down.

---

## 11. Drive-home debrief — 10 minutes, before anyone sleeps

| Question | Answer |
|---|---|
| Matches played / won | `<>` |
| Rank at end of quals | `<>` |
| Alliance outcome | `<>` |
| Awards | `<>` |
| **Top 3 fixes, ranked by matches lost per occurrence** | 1. `<>` 2. `<>` 3. `<>` |
| What went right that we should keep doing | `<>` |
| What we did not have that we needed | `<>` |
| One thing to add to the pit kit | `<>` |
| One thing to add to `CLAUDE.md` or the inspection checklist | `<>` |
| Who types this file back into the repo, by when | `<First L.>`, `<date>` |

**Then, within 48 hours:** the log keeper commits the filled runbook to
`events/<date>-<code>/runbook.md`, and any failure with a real root cause becomes a
`decisions/` entry. That is how event day becomes portfolio content without anyone writing a
portfolio (`research/SCOUTING-AND-AWARDS.md` §16).

---

## 12. Rules that bite at events — one-line reference

| Rule | The short version |
|---|---|
| **I102** | Adult checks in at Pit Admin **≤45 min before quals**; a student must be at the venue. Bring the dashboard roster; region may want consent forms |
| **I103** | ≥1 (preferably 2) responsible adult present **the whole event** |
| **I301** | Bring the complete robot **and** OPERATOR CONSOLE and every component, including decorative, to inspection; demonstrate every configuration |
| **I302** | Electronics limits apply across **all** configurations combined, not per configuration |
| **I303 / I304** | Most changes need re-inspection; the A–G list above does not. Never exploit re-inspection |
| **E101** | Safety glasses in specified areas (10-min grace at doors), closed-toe shoes, hair tied back, walk |
| **E105** | Only teams registered for the event may use its fields and inspection |
| **E106** | Practise only in your pit, a designated practice area, or a Practice MATCH. No practice rigs outside your pit. Demonstrating to judges/guests is not "practice" |
| **E107** | Fabricate only: your pit · another team's pit *with permission* · in the queue *(extra safety scrutiny)* · an event-designated area · an open-to-all machine shop |
| **E108** | No skateboards, hoverboards, drones, gas tanks, noisemakers, scooters, >5 Hz flashing lights |
| **E109** | Do not arrange venue power/internet/phone or use event-reserved internet |
| **E115** | Practice field requires a **complete passed inspection** first |
| **E116** | No recording anyone without consent; **no recording during the Initial Interview** |
| **E301** | **No team Wi-Fi, hotspot, Bluetooth or 2.4/5 GHz gear in the venue.** A phone hotspot counts as an access point |
| **E302** | Do not interfere with or connect to other networks |
| **R401** | ≥2 robot signs, ≥90° apart, ≥6.5 in × 2.5 in, robust, frame-supported |
| **R704.C** | Programming laptops **off the RC Wi-Fi during match play** |
| **R704.D** | FTC Dashboard, FTControl Panels and similar streaming tools are **prohibited** on the RC network; no continuous video stream |
| **R705** | Devices named `<team>-RC` and `<team>-DS` |

Full rule text and analysis: `reference/CONSTRUCTION-RULES-R.md`,
`reference/PENALTY-AND-ENFORCEMENT.md`, and the V0 PDF itself.

---

## 13. KICKOFF TODO — 12 September 2026

Sections 8–11 of the manual (Game Overview, ARENA, Game Details, Game Rules) and Sections 13–14 are
**placeholders in V0**. The moment the Kickoff manual posts:

1. Add the **G-rules** that produce penalties on your team (pre-match setup, human player, endgame).
2. Rewrite §6 match-log columns around the real scoring categories.
3. Add a **pre-match setup checklist** for whatever the game requires you to stage or pre-load.
4. Confirm **Section 10 DRIVE TEAM** composition and badge rules; update §1.
5. Add game-specific items to §2 (scoring-element handling gear, alignment tools, endgame props).
6. Re-run `tools/ai/inspection-checklist.template.md` against the Kickoff manual and R105's
   now-published sizing numbers.
7. Re-print everything and re-date this file.

`tools/ai/PROMPTS-strategy.md` S1/S7 and `tools/ai/PROMPTS-scouting.md` SC3 are the prompts for
steps 1–5. **Every output still needs a human who has read the actual rule.**

---

*Runbook version `<v1>` · filled by `<First L.>` · `<date>`. Sourced from the BIOBUZZ V0
Competition Manual (Sections 3, 5, 6, 12 — final), `research/TESTING-AND-TUNING.md` §3.3,
`research/SEASON-CADENCE.md` §8.5, and `research/SCOUTING-AND-AWARDS.md` §5.3/§13.*
