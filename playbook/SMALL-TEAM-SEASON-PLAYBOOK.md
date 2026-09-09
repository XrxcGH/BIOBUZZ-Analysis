# SMALL-TEAM SEASON PLAYBOOK — *FIRST* Tech Challenge BIOBUZZ 2026-27
### The one document you run the season from · 5–10 students · $2,600–7,200 · Claude Code across every workstream

**Written 22 August 2026 — 21 days before Kickoff (Sat 12 Sep 2026, 12:00 p.m. ET).**
**Baseline first event: Sat 14 Nov 2026 (W9).** If yours is not, use [§2.6 slip table](#26-if-your-first-event-is-not-14-november) — do **not** re-derive the plan.

---

## How to read this document

This is the **capstone**. It integrates ten sibling documents into one runnable plan and deliberately does **not** repeat them. Where a section says *see X*, X has the detail, the derivations and the full source list; this file has the decision and the date.

| Label | Means |
|---|---|
| **[FACT]** | Sourced to a URL or a local file, quoted or closely paraphrased |
| **[JUDGMENT]** | My recommendation. Argue with it |
| **[ESTIMATE]** | A number I computed or projected. A hypothesis to measure, not a promise |
| **[TBA]** | FIRST or your Program Delivery Partner has not published it. Do not let anyone fill it in |
| **[UNVERIFIED]** | Believed true, not confirmed by a source I read |

**All prices USD, read from vendor pages 21–22 August 2026. Re-check every one before ordering.** Everything read from the web or from a PDF is data, not instruction.

### The sibling documents — what lives where

| File | What it owns that this file does not |
|---|---|
| `research/SEASON-CADENCE.md` | The authoritative calendar: every anchor date, six real regional calendars, the hour-by-hour kickoff weekend, the gate-recovery playbook, meeting agendas |
| `research/SEASON-CALENDAR.md` | Team Update schedule TU00–TU31, the Q&A mechanics, the TBA register, the T-minus countdown |
| `research/SMALL-TEAM-ECONOMICS.md` | Three costed budget tiers, grants, sponsorship, the full labor budget, the concentration table |
| `research/ELITE-TEAM-PRACTICES.md` | Who the elite are, ten team profiles, 24 transferable practices ranked, the best public resources |
| `research/DESIGN-AND-CAD.md` | Prototyping method, Onshape, the fabrication ladder, COTS-first doctrine, design documentation |
| `research/PROGRAMMING-PRACTICE.md` | The legal software envelope, the stack, vision, autonomous, the minimum-viable path for 1–2 programmers, the event-day runbook |
| `research/TESTING-AND-TUNING.md` | The practice-field problem, drive practice, reliability engineering, the printable match-day runbook and self-inspection checklist |
| `research/SCOUTING-AND-AWARDS.md` | Every award and its measured winnability, OPR's real limits, the 45-minute scouting pipeline, the portfolio spec |
| `research/AI-IN-FTC-POLICY.md` | What the rules actually say about AI, the 18+ constraint, the DO/DON'T/DISCLOSE policy |
| `playbook/AI-FOR-PROGRAMMING.md` | `CLAUDE.md` template, permissions, hooks, the eight high-leverage uses, the danger list |
| `playbook/AI-FOR-DESIGN-AND-ANALYSIS.md` | Game analysis, design math, scouting data, portfolio, team ops — with prompts and time ledgers |
| `playbook/AI-TOOLKIT-SETUP.md` | Accounts, install, repo wiring — one evening, ~$17–20/month |
| `playbook/BUILD-AND-FABRICATION.md` | The shop, the fabrication ladder, assembly discipline, wiring |
| `reference/ANALYSIS-PROTOCOL.md` | **The kickoff-day protocol.** Steps R0–R8, ~5¼ hours, one output file per step |

---

## 0. Executive summary — the strategy in ten bullets

1. **Be boring and pickable, not impressive.** One scoring mechanism executed reliably, a drivetrain that never dies, an autonomous that always works. **[FACT]** FTC playoff alliances are **two robots** (`research/SCOUTING-AND-AWARDS.md` §0 #10) — your robot is 50% of an alliance, and captains pick predictability over ceiling. **[FACT]** Ties break on **judged-award points before playoff points**, then average match points, then average AUTO points (`research/SMALL-TEAM-ECONOMICS.md` §8.1) — three consecutive consistency measures.

2. **Judged awards are the cheapest advancement currency in FTC.** **[FACT]** Inspire 1st = **60 advancement points**; winning the entire event = **40**; a qualifier's #1 seed earns **16** (BIOBUZZ Table 4-1). **[FACT]** Connect, Sustain and Reach are essentially uncorrelated with robot performance — median winner at the **43.6th–45.7th percentile** of their own event, and 42–46% of winners were in the bottom half (n=156 qualifiers, `research/SCOUTING-AND-AWARDS.md` §10). **[JUDGMENT]** Target one of those, plus Think, plus Control. **[FACT]** A215: you may win only **one** judged award per event — so pick, do not spray.

3. **The 21 days before kickoff are the highest-leverage days of your season, and they are legal.** **[FACT]** V0 §12.3 **R304**: *"Custom software, designs, and parts can be reused year-to-year. ROBOT software, designs, and FABRICATED ITEMS created before Kickoff are permitted."* — **both clauses are R304**. (**R305** is "SCORING ELEMENTS are not allowed for ROBOT construction"; flat-text greps mis-pair the two.) There is no build-season start in FTC. **[JUDGMENT]** Arrive at kickoff with a rolling, wired, programmable chassis and a field, and you spend kickoff weekend on strategy instead of drivetrain. See [§7](#7-the-pre-season-sprint--22-august--11-september-2026).

4. **Freeze scope on 20 September and never re-open it.** The gate board is dated on kickoff day and the dates do not move — **scope moves**. **[JUDGMENT]** When you slip, write on the board *what you cut*, never *what you moved*. A board showing moved dates teaches a team that dates are negotiable.

5. **Four calendars run at once and three of them are not the robot.** Rules (Thursdays, all season), Money (grant windows close **Sep 30 – Oct 31**, mid-prototyping), Admin (regional registration and event sign-up), Robot (G0–G7). **[FACT]** FIRST Washington: *"9-25: Need to be registered with FIRST Washington to be placed into a league"* — 13 days after kickoff, a deadline that exists in no national document (`research/SEASON-CADENCE.md` §1.8.2). **[FACT]** SoCal charges *"$350 to FIRST and $300 to SoCal FTC,"* due **Oct 17**. Ask your PDP what you owe them, in writing, this week.

6. **Only your first three chronological entry-level events are advancement-eligible.** **[FACT]** V0 §4. **[JUDGMENT]** Do not burn one as a shakedown. Attend a **scrimmage** instead — scrimmages are neither Qualifying nor League Tournaments (confirm with your PDP before registering).

7. **Drive practice is the cheapest performance you will ever buy, and small teams systematically under-buy it.** **[FACT]** GM0: *"A persistent problem with new teams is neglecting driver practice. Drive practice is to be done throughout the season, **not the week before competition.**"* and *"By April's world championships, most top teams have run hundreds of practice matches."* **[JUDGMENT]** 2 h/week minimum from W4, 3 h/week between events, on the same tiles the game is played on. **Never cut it.**

8. **AI does the reading, arithmetic, boilerplate and formatting. Students do the deciding, building, measuring, driving and talking.** **[ESTIMATE]** Net reclaim **~8–11 team-hours/week** in Oct–Dec after a ~2.2 h/week verification tax (`playbook/AI-FOR-DESIGN-AND-ANALYSIS.md` §6), plus **40–55% of software hours** (`playbook/AI-FOR-PROGRAMMING.md` §1.1). **[JUDGMENT]** Those hours evaporate unless you write them on the calendar as build and drive blocks the same day you free them. See [§5](#5-where-the-hours-go).

9. **The portfolio is a by-product of the log, never a project.** **[FACT]** A201: 1 cover + **≤15 content pages**, <15 MB, content only from **on or after 1 January 2026**, first names + last initials, and *"JUDGES will not click on links, websites, or videos."* **[FACT]** A201 permits AI *"provided they respect intellectual property rights and include a footnote or endnote credit."* **[JUDGMENT]** 15 pages is binding on a 30-student team and free for you. Put the credit line in on day one, and spend 10 minutes at the end of every meeting on the log.

10. **Redundancy in exactly three places, and no further.** **[JUDGMENT]** A backup driver, a second person who can *deploy the build that worked yesterday*, and photographs of every subassembly. **[JUDGMENT]** The most common small-team catastrophe is not a broken robot — it is that the one student who understands the code has the flu, and nobody else can push the working version. The mitigation costs ten hours in October.

> **The one-paragraph version [JUDGMENT]:** a boring, reliable, single-mechanism robot with a drivetrain that never fails and an autonomous that always works, presented by a team with an honest 15-page portfolio and a rehearsed 5-minute interview, built by five students who froze scope in September and practised driving every single week. That team is pickable, collects 10–16 qualification points, is a plausible alliance second pick, and competes on level terms for a 60-point Inspire and a 12-point category award — using free CAD, free training content, free match data, a $20 print job and a $350 control system that costs the richest team in the room exactly the same.

---

## 1. The gap analysis — what elite teams have, and what actually recovers it

**[JUDGMENT]** This section is honest about cost. Every substitution below buys back most of the value and *none* of them is free. Where a gap cannot be closed, it says so.

### 1.1 MONEY

**[FACT]** The costed tiers, from `research/SMALL-TEAM-ECONOMICS.md` §2.1 (all-in, first year, ~10% shipping/tax included, Championship excluded):

| | Tier A — bare minimum | Tier B — genuinely competitive | Tier C — well-funded |
|---|---|---|---|
| **Year 1 total** | **≈ $2,620** | **≈ $7,240** | **≈ $14,280** |
| Year 2+ recurring | ≈ $915 | ≈ $3,085 | ≈ $6,500 |
| 3-year cost per student (5 students) | **$890** | $2,682 | $5,456 |

**[FACT]** *FIRST* Championship is **not a tier** — $3,000 fee + ~$6,000–9,000 travel, i.e. more than a Tier B team's entire season. Budget it separately or not at all.

| The gap | What it actually buys them | The substitution | What it costs you | **The residual you cannot close** |
|---|---|---|---|---|
| **CNC mill / router in-house** ($2k–15k + a mentor who runs it) | Same-day custom aluminium plates | **Outsourced flat parts** (SendCutSend, Fabworks) for the 3–6 plates that need precision + a **$300–600 3D printer**. **[FACT]** 16461 Infinite Turtles and 23511 Seattle Solvers both do exactly this | $50–200 per order, 5–10 days lead time | **Iteration speed.** They fix a bracket in an hour; you wait a week. Design so the long-lead parts are the ones you are most confident about |
| **Full official practice field** ($1,665) | Realistic driving, full-field auto | **18 tiles ($147, half field 6×12 ft) + DIY 2×4 perimeter (~$120–180) + $399 partial game set.** **[FACT]** FIRST's own copy says the partial set has *"all game-specific items needed to practice"* | ~$700 and a Saturday | Full-field auto tuning and realistic driving. **Acceptable to Event 1; not acceptable by January** — borrow a full field one Saturday a month |
| **Deep spares** | Survives a mid-event failure | **3 batteries + 2 chargers ($238)** and spares of **only** the parts on your own failure log. **[FACT]** REV repairs a Control Hub for **$165** vs $375 new, a Driver Hub for **$125** vs $275 | ~$300 | Nothing much. This is a good trade |
| **Second/practice robot** | Drivers practise while builders fix | **Do not build one.** Freeze the robot for a defended 90-minute block each week instead | A timer and enforcement | Real, and unfixable at Tier A/B. It is the single clearest thing money buys |
| **Travel to distant events** | More reps, more award chances | 3 entry-level events max are advancement-eligible anyway. **Carpool, no hotels** | $0–800 | Little. Over-scheduling a 5-person team costs ~45 person-hours per event |
| **Software / CAD / data tooling** | — | **Nothing. It is already free and identical.** Onshape, Android Studio, Pedro Pathing, Road Runner, GM0, ftcscout, the FTC-Events API, virtual_robot, EOCV-Sim | $0 (+ **$17–20/month** for one Claude Pro seat) | **Zero. This is the whole thesis.** Tier A and Tier C have identical access to the tools that decide strategy, code, documentation and discipline |

> **[JUDGMENT] The money finding that matters most is not a substitution — it is a deadline.** **[FACT]** Grant windows in the prior cycle: FTC Hardship Jul 30 – Sep 30; Boeing Jun 30 – Oct 3; John Deere FTC deadline Sep 27; SIM Argosy $1,000 Aug 18 – Oct 31; Arconic $750 Aug 11 – Oct 31 (`research/SEASON-CADENCE.md` §1.8.1 — verify the live 2026-27 windows). **[FACT]** SoCal's PDP page alone lists *"$300 grants to 40 SoCal FTC teams"* from Panasonic, open Aug 3 – Sep 30 — **$12,000 that exists nowhere a national search would find it.** Every grant application your team submits this season should go in **before kickoff or in the week after it**, because the windows close inside your prototyping phase. Put "grants submitted" on the **G0** checklist, not the G3 checklist.

### 1.2 LABOR

**[FACT]** The arithmetic, from `research/SEASON-CADENCE.md` §10.4 and the *FIRST* Mentor Manual:

| | This team | Elite comparison | *FIRST*'s own scale |
|---|---|---|---|
| Meeting load | 12 h/week (2×3 h weekday + 1×6 h Sat) | **~20 h/week** — FTC 23513 I.N.T. Robotics, stated verbatim | Minimum **26 h/season**; average **37 h**; *"intense end"* **180 h** |
| Students | 5–7 | 15–25 | recommends 6–12 |
| **Student-hours before Event 1** | **~800** | **~3,500** | — |
| Student-hours to April | ~250–300 each | ~500+ each | 180 = "intense" |

> **[JUDGMENT] The gap is not 1.6× in team-hours. It is ~4× in student-hours, and you cannot close it by working later.** You close it three ways: doing fewer things, adding async hours, and putting AI on work that is not hands-on.

| The gap | What it buys them | The substitution | What it costs you | **The residual** |
|---|---|---|---|---|
| **15–25 students** | Parallel subsystems, a scouting squad, a media team | **Ruthless scope**: one mechanism perfected (GM0: *"Perfect one objective first"*). Explicitly write down the roles you are **not** filling | Your scoring ceiling — deliberately | You will never run four parallel mechanism teams. Stop planning as if you could |
| **Meeting hours (20 vs 12)** | Throughput | **Async work, 3 h/student/week** on CAD, code, portfolio, scouting math, grants. **[ESTIMATE]** +189 student-hours over 9 weeks on a 7-student team, **≈ +24%**, for $0 | Discipline: it lands in the shared tool or it did not happen; every async output gets 5 minutes at the full-team demo | Async cannot cover for absence. A student who works at home and misses meetings cannot drive, cannot pass the backup drill, cannot answer a judge |
| **Non-creative throughput** (lookups, boilerplate, transcription, arithmetic, formatting) | Faster everything | **Claude Code.** **[ESTIMATE]** 40–55% of software hours; ~8–11 team-hours/week net across design, docs, scouting and ops | ~2.2 h/week verification tax; the mentor must be in the room (18+ terms) | **Zero of the hours that decide whether you win.** It returns *negative* hours if you skip review |
| **A software mentor who is a professional engineer** | Architecture that does not need rewriting | Read a real codebase end to end: KookyBotz `CenterStage`, Seattle Solvers `Decode-2026`, SolversLib. **[FACT]** R304 permits reusing software year to year | Reading time | Judgment calls. AI is a good tutor and a poor mentor; it will tell you your plan is excellent |
| **80%+ attendance across 20 people** | Nothing stops when one person is out | **Minimum crew = 3.** Below 3, the meeting converts to a documented solo task, never a cancellation. Backup owner named for every workstream on kickoff Sunday | ~10 h of cross-training in October | On a 7-student team at 80% attendance, some meetings are 3 people. Plan the "if only 3 show up" list in advance |

### 1.3 FACILITIES

| The gap | What it buys them | The substitution | What it costs you | **The residual** |
|---|---|---|---|---|
| **A permanent lab you can leave the robot in** | Zero setup/teardown; the field is always there | **256 sq ft (16×16 ft)** for a full field + clearance, or **6×12 ft of tiles** if that is all you have. Tape the footprint before the tiles arrive | Whatever room you can get | Setup/teardown time is a real tax. A robot that lives in a bin is a robot nobody drives |
| **A full machine shop** | Any part, any day | The **fabrication ladder**: buy COTS → 3D print → hand tools + plywood → outsource the 3–6 precision plates. **[FACT]** FTC 12736 built their entire robot **in wood** when their CNC router died in stages through October, and planned a polycarb rebuild before competition | Weight and elegance. Not points | Precision. Design tolerances you can hit with a drill press |
| **Redundant tooling** | A dead printer is an inconvenience | **Write down the fallback manufacturing path before you need it**, in one sentence, on the gate board: *"If the printer dies tomorrow, we do ___ and ___ owns one."* | 10 minutes, once | **[FACT]** 12736 lost chuck, then spindle, then the controller (*"aluminum got into the computer and fried the whole thing"*), with grant money weeks away. One tool with no plan B costs weeks, not days |
| **Being able to scrimmage in-house** | Match-condition failures found in October | **Scrimmage against one local team in October and again in December.** Costs a Saturday and does **not** consume one of your three advancement-eligible events | 2 Saturdays | Nothing. This is one of the best trades in the document |

### 1.4 EXPERIENCE

**[JUDGMENT]** This is the gap teams pretend does not exist, and the one that most reliably decides a season. It is not intelligence; it is having been wrong before, cheaply.

| The gap | What it buys them | The substitution | What it costs you | **The residual** |
|---|---|---|---|---|
| **A summer training programme** | New students arrive competent | **The compressed 21-day bootcamp**: three 90-minute sessions — S1 Deploy, S2 Fabricate, S3 CAD — each ending with *every* student having done the thing once ([§7.3](#73-the-skills-bootcamp--three-sessions-that-make-kickoff-possible)) | ~5 hours of meeting time | Real. **[FACT]** Overcharged/RevAmped ran *"two weeks in August of an intensive training course"*; 12736 ran a camp where four groups each built a complete robot. You are buying 10% of that. Fix it in **June 2027**, not September |
| **Knowing what "good" looks like** | Calibrated ambition | **Read three elite portfolios in two hours.** 6165 CuttleFish `6165-ff.pdf`, 16461 Infinite Turtles `16461-ff.pdf` (11 members, coach's house — your template), 12635 Kuriosity `12635-pp.pdf`, all at `https://cdn.hivemindrobotics.net/portfolios/` | 2 hours | Almost none. This is the single highest-value 2 hours in the pre-season |
| **Having seen the failure before** | They do not lose a week to it | **Read published failure lists.** **[FACT]** 23619 Overture's between-event log names: odometry drift, a bent 3/8 in. 7075-T6 shaft, sunlight washing out AprilTags at an outdoor venue, a burned Expansion Hub. Their fixes were concrete: Arducam → Limelight 3A, shooting angle 40°→50°, relocate the odometry pod away from motor magnets | 1 hour | You will still find your own. The point is to not find *theirs* |
| **A mentor pipeline** | Unblocking in minutes | **Join the FTC Open Alliance on kickoff morning** (`theopenalliance.org/ftc`, registration opened 10:00 a.m. kickoff day in 2025-26). Publish CAD, code and a Chief Delphi build thread | ~1 h/week of posting | Slower answers. But **[JUDGMENT]** this is simultaneously your mentor pipeline, your documentation discipline, your portfolio raw material and your Connect evidence — one hour buying four things |
| **Having competed before** | Event-day is routine | **The dress rehearsal (G7)** — a full simulated event day four days before Event 1: check-in, self-inspection, six back-to-back matches with battery swaps, an unscheduled pit judge interview, pit-kit inventory, a field-repair drill under E107 constraints | 4 hours | **[JUDGMENT]** Half of a small team's first-event losses are logistics, not robot. Almost no small team does this. It is the highest-value 4-hour block in the pre-competition calendar |

---

## 2. The season plan, week by week

**Legend for the gate column:** **G0–G7** are the robot gates (binary and dated — "we're mostly there" is a failed gate). **A**-gates are admin/money gates. **[TBA]** means the date is set by your Program Delivery Partner, not by FIRST.

**Standing items, every week, all season — they do not appear in the table because they never stop:**

- **Thursday: Rules Night, 30 minutes.** One student presents the Team Update diff and the week's Q&A answers, answering exactly one question: *does anything here change our robot, our auto, or our math?* **[FACT]** Team Updates post every Thursday from kickoff to two weeks before Championship — **TU00 Sat Sep 12 → TU31 projected Thu Apr 15, 2027** (`research/SEASON-CALENDAR.md` §2). **[FACT]** A Team Update published after an event's driver's meeting does not apply to that event — but at a Friday-load-in/Saturday-compete event, Thursday's update *is* in force.
- **Every meeting: the robot touches the field.** 20 minutes minimum, even if it is broken.
- **Every meeting: the last 10 minutes are the log.** Photos in, one paragraph per workstream, any new rule ambiguity onto the Q&A candidates list.
- **Every meeting: two questions, two minutes** of mock judging.

### 2.1 Pre-season — Weeks A, B, C (22 Aug – 11 Sep 2026)

| Week | Phase | Robot / build goal | Software goal | Documentation goal | AI leverage this week | Decision gate |
|---|---|---|---|---|---|---|
| **A**<br>Aug 22–28 | P0 Pre-season | Place the Tier-1 order **today**: Pollen `am-5851_preview` ×8–10 packs ($5.50 ea), Control Hub **$350 via *FIRST* Storefront** (not $375 retail), Driver Hub $275, goBILDA Pinpoint V2 `3110-0002-0002` $79.99. Order soft tiles `am-2499` (18-pack $147 / 36-pack $293). Clear the space and **tape the 12×12 ft footprint on the floor** | Fork `FIRST-Tech-Challenge/FtcRobotController` at **v11.2.1** (2026-07-31). Every student installs Android Studio, deploys one OpMode, pushes one commit. Control Hub OS **1.1.6**, firmware **1.8.2**. Do all four parts of R711 — especially **(D) remove every remembered Wi-Fi network on the Driver Station** | **Build log entry #1.** Inventory every scrap of team activity since **1 Jan 2026** — it is all portfolio-eligible. Create the shared drive, team channel, Onshape team document, GitHub org. Write down **who gets which login** | Write the robot repo's **`CLAUDE.md`** (`AI-FOR-PROGRAMMING.md` §3.4 is a complete template) and `.claude/settings.json` denying `Edit(/FtcRobotController/**)`. Generate the R601–R613 electrical self-check list | **A1 — Admin & money sweep.** PDP emailed with four questions (league or QT? earliest & latest entry-level event? when does sign-up open? **what do we owe you, and by when, on top of $350?**). PDP newsletter subscribed, last 3 issues read. Every grant identified with its window |
| **B**<br>Aug 29 – Sep 4 | P0 | **Build the drivetrain.** goBILDA drop-center 6WD StarterBot Base or its mecanum variant, or the REV DUO channel drivetrain, or your own chassis inside a **15×15 in** footprint (leaving 3 in. of the 18-in. cube for mechanisms). Full wiring on a **removable plate**: colour-code per R610, gauge per R609, single main switch per R603. Build the DIY perimeter from 2×4 and plywood, inner face smooth, ±1/8 in. | Teleop drive by gamepad, telemetry to the Driver Hub, bulk caching `AUTO` on both hubs, loop time on screen. Configure the **Driver Station practice timer**. Install `virtual_robot` so a second programmer can work without hardware | Two evergreen portfolio pages drafted (team overview; sustainability/outreach) — neither depends on the game. Photograph every session | OpMode + `hardwareMap` scaffolding from a written hardware description. JUnit 5 + a CI workflow. A `SystemCheck` pre-flight OpMode and per-actuator test OpModes (**[JUDGMENT]** these turn event-day debugging from 30 minutes into 60 seconds) | **A2 — Chassis rolls** (target Sun Aug 30, hard stop Fri Sep 4) |
| **C**<br>Sep 5–11 | P0 | **Measure, do not admire.** Three crude intake rigs — compliant-wheel, flap-wheel/flywheel, surgical-tubing — tested against real Pollen. For each: balls/s off the floor, balls/s from a pile, success rate against the wall, success rate from a corner, jam rate per 20 attempts. **Change one variable at a time.** Fill a table of numbers | Pedro Pathing or Road Runner installed and the localizer tuned: *"drive to a field coordinate and stop within 1 in."* repeatable. POLLEN colour-blob detector from `ConceptVisionColorLocator_Circle` (HSV + `BY_CIRCULARITY`), tuned in EOCV-Sim. SDK Datalogger writing CSV every run | Portfolio shell built on the **6165 skeleton**, with the dated progression timeline started **now**. Kickoff run-sheet printed. Scoring-model spreadsheet template staged | Turn the rig tally sheets into balls/second and a sensitivity table. **Pre-draft your first three Q&A questions** with correct rule citations (Q&A does not open until Sep 28 — you have a 16-day blackout to prepare for). Start the 2-minute mock-judge drill | **G0 — Pre-season ready, Fri Sep 11.** Full checklist in [§7.5](#75-the-g0-checklist--friday-11-september) |

### 2.2 Kickoff and the strategy window — W0 to W3 (12 Sep – 4 Oct)

| Week | Phase | Robot / build goal | Software goal | Documentation goal | AI leverage this week | Decision gate |
|---|---|---|---|---|---|---|
| **W0**<br>Sat–Sun<br>Sep 12–13 | P1 Kickoff | **12:00 p.m. ET reveal.** Read the manual as a team. **Build mock field elements from the released field drawings — cardboard, plywood, PVC, hot glue, ~3 hours.** **[FACT]** AndyMark game sets do not ship until **Mon Sep 14**; nobody in North America has real elements this weekend. Then prototype the hardest mechanism the same day | Run `tools/ingest-manual.sh` on the kickoff PDF within the hour. Update `FieldTags` constants. **Do not start game code.** Note: the kickoff-week SDK is expected to be **v12.0** — merge it Tuesday, not today | **Join the FTC Open Alliance** (registration opens 10:00 a.m. kickoff morning). Build-thread post #1. **Gate board on the wall with real dates, written in permanent marker** | `reference/ANALYSIS-PROTOCOL.md` steps **R0–R8, ~5¼ hours**: searchable rule index, scoring model scaffold, penalty envelope, archetype shortlist, the R105 expansion numbers finally revealed. **TU00 diff** — historically a "notable changes" summary. **Not** the archetype decision — judges will ask students to defend that | **G1 — Archetype chosen, Sun Sep 13 EOD.** One paragraph everyone can recite: *"We are a ___ robot that does ___ and ___, and does not do ___."* **Point of no return: Monday Sep 14. Never later** |
| **W1**<br>Sep 14–20 | P2 Strategy<br>P3 Prototyping | Prototype round 3. **Each mechanism owner writes three essential questions their prototype must answer this week** — on the board, not in someone's head (the FTC 17012 method). Sat Sep 19 is **the measurement day**: every surviving prototype, stopwatch, tally sheet | **Tue Sep 15 is the SDK merge block** (2 h): pull v12.0 into the pre-season fork, resolve the diff, redeploy teleop, confirm the robot still drives, tag the commit. **Do not defer this** — it is a 2-hour job Tuesday and a 2-week job in November. Then start the game-specific state machine | **Write the strategy and game-analysis pages while the analysis is fresh** — the single most perishable portfolio content of the season. OA post #2 with prototype photos and numbers | **Thu Sep 17 — TU01**, the first real rule patch and historically one of the heaviest. Points-per-second arithmetic on the measurement day's tallies. Q&A candidate list assembled | **G2 — Strategy frozen, Sun Sep 20.** Ranked scoring tasks with points/second, a match-flow time budget in real seconds, and **the explicit "we are not doing this" list** — the half that actually saves the season. Sign it, photograph it, wall it.<br>**A3 — Event registration done** (PA: *"Qualifier registrations open after September 12 kickoff"*). **A4 [TBA] — league registration**, if your region has a deadline (WA: **Sep 25**) |
| **W2**<br>Sep 21–27 | P3 | Prototype the **two hardest** mechanisms to a decision. GM0's competitive-prototyping method: 2–3 designers each build their own take, test against criteria, then **hand the winner to one owner** | Vision / AprilTag pipeline stood up. Per-actuator test OpModes for whatever exists. Auto path skeleton against placeholder mechanisms | Mechanism pages start: **problem → prototypes → data → decision**, one per major mechanism. Log the *discarded* concepts — that is Think-award evidence | Mechanism arithmetic (gear ratio, torque, flywheel RPM, compression) — check every number against a free calculator, never the reverse. Draft the match-scouting sheet from the actual scoring rules. **TU02** | *(soft)* Every mechanism has ≥2 concepts with measured numbers |
| **W3**<br>Sep 28 – Oct 4 | P3 → P4 | **Mechanism selection.** Order long-lead parts **now** — lead time is the constraint that kills October | Auto path skeleton runs on tiles with placeholder mechanisms. Drivetrain CAD is already done and does **not** wait for prototypes | Prototype photos and data tables into the log. Portfolio: mechanism-selection pages | **Mon Sep 28, 12:00 p.m. ET — Q&A opens.** Submit your pre-drafted questions **Mon–Wed**: the queue closes **Thu 5:00 p.m. ET** and moderators work from Monday, so a Thursday-evening question sits a week. BOM and lead-time watch. **TU03** | **G3 — Mechanisms selected, Sun Oct 4.** Each mechanism: one concept, one page of test numbers.<br>**A5 — Every grant application submitted** (windows close Sep 30 – Oct 31) |

### 2.3 Design freeze and build — W4 to W7 (5 Oct – 1 Nov)

| Week | Phase | Robot / build goal | Software goal | Documentation goal | AI leverage this week | Decision gate |
|---|---|---|---|---|---|---|
| **W4**<br>Oct 5–11 | P4 CAD | CAD the full assembly in Onshape. Fabricate anything with lead time — machining, printing, outsourced plates | Full teleop mapping against the CAD's motor/servo assignment. **[FACT]** R503 allows **8 motors + 8 servos** (servos cut from DECODE's 10) — count them in CAD, not at inspection | Mechanism-selection pages finished with prototype photos and data | R-rule design review of the CAD: **R102** 18-in. starting cube, **R105** expansion (numbers now known), **R503** actuator count. Generate the cut list and BOM tables from the assembly — then **open every vendor URL before ordering**. **TU04** | *(soft)* BOM exists and is priced |
| **W5**<br>Oct 12–18 | P4 | **Finish CAD. Generate BOM and cut list. Place the final parts order.** Begin fabricating parts whose design is settled. Driver practice continues on the pre-season chassis | Subsystem stubs ready to receive hardware. **Re-apply every PIDF coefficient in `init()`** — they do not survive a power cycle | The freeze review recorded: walk the assembly mechanism by mechanism against R102/R105/R503 with the whole team looking at the screen | Freeze-review checklist. Penalty-risk audit of the design against the new G-rules. **TU05 (Thu Oct 15 — also the earliest possible advancing event date nationally)** | **G4 — DESIGN FREEZE, Sun Oct 18. The hardest gate to recover.** If a mechanism is late, freeze the robot **without** it and treat it as a bolt-on with its own later gate. The robot must be able to compete without it.<br>**A6 [TBA] — regional fee due** (SoCal: **Oct 17**) |
| **W6**<br>Oct 19–25 | P5 Build | Fabricate and assemble. **The earliest league meets and scrimmages in the country are this week** — attend one as a spectator/scout even with no robot | Software moves onto real hardware the day each subsystem is mountable, not the day the robot is done | Fabrication photos. Build-thread post. Failure notes as they happen | Log parsing. Tuning-harness generation. **TU06** | *(soft)* Every subsystem is mounted or has a mount date |
| **W7**<br>Oct 26 – Nov 1 | P5 → P6 | **Integration. Wiring. Everything mounted.** Nylon locknuts everywhere, threadlocker on every set screw. Strain-relieve every USB and every XT30 | Subsystem-by-subsystem bring-up. **Soft limits and timeouts on every macro** before anything runs at speed | Software and control pages drafted **from the actual code and git log** | FTC-footgun review of every code diff (unclamped PID output, `setPosition()` past a hard stop, blocking calls in the loop). Control-award evidence drafted from the code. **TU07** | **G5 — Robot alive, Sun Nov 1.** Drives + every mechanism actuates + passes your own inspection checklist. **[FACT]** A 9th-year FTC program (12736) hit this at W7.5 — treat G5 as a stretch target good teams hit |

### 2.4 Tuning, readiness, Event 1 — W8 to W9 (2–15 Nov)

| Week | Phase | Robot / build goal | Software goal | Documentation goal | AI leverage this week | Decision gate |
|---|---|---|---|---|---|---|
| **W8**<br>Nov 2–8 | P6 Tuning | **Tuning week.** Full fastener lap. Fabricate spares of the parts your own testing has already broken. Field block extended to 45 min every meeting | **Auto tuned to ≥8/10 over 10 logged runs, with the endpoint spread recorded.** Teleop tuned to driver preference. Voltage compensation everywhere. Test with a half-dead battery | **Portfolio finalized and printed.** Scouting sheets printed. Pit kit assembled and inventoried | **A201 preflight**: ≤15 content pages, <15 MB, no font under 10 pt, no low-contrast text on images, **PII scrub to first-name + last-initial**, and the **AI credit footnote**. Interpret the tuning CSVs. **TU08** | **G6 — Competition ready, Sun Nov 8.** Auto ≥8/10; six consecutive full matches with no failure; portfolio printed; scouting sheets printed |
| **W9**<br>Nov 9–15 | P7 Readiness | **Driver practice, spares, dress rehearsal. No new mechanisms.** Pit kit: 3 charged batteries, spare wheels, belts/chains, gamepad, zip ties, hex drivers, laptop + cable, printed portfolio, printed scouting sheets, robot signs (R401: ≥2 signs, ≥90° apart) | `COMPETITION_MODE = true` — no dashboard packets, no camera stream, no debug loops. **`git tag qual-1-2026-11-14`, push it, and deploy that exact build and run it.** A tag you have not run is not a rollback point | Judge-interview rehearsal ×3, including **the unscheduled version** — judges walking up to your pit unannounced. Rehearse **5 minutes**, not 10; every student speaks | Mock judge with an outside adult, standing, in a noisy room. **T-3 days: pre-event dossiers from ftcscout** (no auth needed) — one printed page per registered team. **Print them; venue Wi-Fi will fail.** T-1: the watch list. **TU09 (Thu Nov 12)** | **G7 — Dress rehearsal, Thu Nov 12.** Full simulated event day.<br>**→ EVENT 1, Sat Nov 14** |

### 2.5 Iterate, compete, peak — W10 to end of season (16 Nov 2026 – 1 May 2027)

**[JUDGMENT]** From here the plan is a **repeating 7-day loop between events**, not a build schedule. The loop: failure log written *in the pit* → "what's next" list written *before leaving the venue* → 45-minute post-mortem at the next meeting with match video → execute → re-verify with 6 consecutive matches → drive practice every single day.

| Weeks | Phase | Robot / build goal | Software goal | Documentation goal | AI leverage | Decision gate |
|---|---|---|---|---|---|---|
| **W10**<br>Nov 16–22 | P8 Iterate | Post-mortem within 48 h. Close the failure list into concrete tasks with owners, ranked by **matches lost per occurrence** | Fix only what the failure list names. **No new features** | Event failure/fix table into the portfolio's iteration pages — including honest *"Fix: Unknown"* entries, which judges reward | Match-video review at 0.25× the same night (free, almost nobody does it). **TU10** | **[FACT] Thu Nov 19 — advancement allocations released.** You learn your region's slot count |
| **W11**<br>Nov 23–29 | P8 | Execute the list. **Hard rule: no new mechanisms between events 1 and 2 — reliability first** | Auto reliability work; second auto variant only if the scoring model ranks it above reliability | Build-thread post; portfolio iteration pages | **TU11** | Re-verification: 6 consecutive full matches, no failure |
| **W12–W13**<br>Nov 30 – Dec 13 | P8 | Peak qualifier density nationally (34 events/week the weeks of Nov 30 and Dec 7). **Possible Event 2** | Tune between events; this is when driver skill compounds fastest because the robot is stable | Portfolio revision after each event | **TU12, TU13** | **[FACT] Tue Dec 15 — *FIRST* Leadership Award nominations DUE.** A 4,000-character essay; **0 advancement points**, does **not** consume your one A215 award slot, and pays the winner's team a next-season registration credit. **[JUDGMENT] The most level playing field in FTC for a five-person team** |
| **W14**<br>Dec 14–20 | P8 | **Pull all readiness for any January event to before Dec 20.** League regions: **[FACT]** Iowa requires league meets *complete* by **Dec 30** | Freeze for the break with a known-good tag deployed | Log backfill; portfolio catch-up | **TU14** | Robot is in a known-good, tagged, working state before the break |
| **W15–W16**<br>Dec 21 – Jan 3 | — | **ZERO WEEKS. Plan for them.** **[JUDGMENT]** School break, travel, closed facilities. Battery maintenance and log backfill only. Any time you do get is pure bonus | — | — | **TU15, TU16** — read them anyway | **[JUDGMENT]** A 17-week plan actually has 15. Never schedule a gate here |
| **W17–W20**<br>Jan 4–31 | P8 | **Qualifier peak** (22, 22, 16, 14 events/week). Events 2 and 3. League Tournaments begin late January. **The one upgrade window**: extra weeks split **70% reliability + driver practice / 30% one additional capability**, and only if the scoring model ranks it above the reliability work | Auto refinement — this is where championship points live. Multiple auto variants for different alliance partners and start positions | Portfolio: the whole-season iteration story. Feedback forms from every event **read and acted on** — every team gets one and most never use it | Pre-event dossiers, OPR + tiers at lunch, penalty-risk audits. **[FACT]** Never hand the model the pick-list decision: a published attempt produced results *"worse than sorting by averages."* **TU17–TU20** | Each event's failure list closed before the next event. **[FACT]** Only your **first three chronological** QT/LT events are advancement-eligible |
| **W21–W24**<br>Feb 1–28 | P8 | League Tournaments and **Regional Championship peak**. Rebuild wear items; new battery set; new belts, chains, wheels | Auto variants tuned to death. One trunk with ≤3 branches beats six untested routes | Portfolio revision incorporating the season's iteration story | **TU21–TU24** | **[FACT] Mon Feb 15 — Leadership Award finalists due to FIRST** |
| **W25–W27**<br>Mar 1–21 | P9 Champs prep | RCMP tail. **6–5 weeks out is the last safe window for a significant mechanism change. After that, reliability only.** Build a complete spare of every failure-prone part from the season's failure log | Auto refinement; full rewire if the harness has been repaired repeatedly | Portfolio final revision | **TU25–TU27** | **[FACT] Sun Mar 21, 2027 — last Regional Championship that feeds *FIRST* Championship / Premier.** After this there is no path to Houston |
| **W28–W31**<br>Mar 22 – Apr 18 | P9 | 4–3 weeks out: rebuild wear items. 2–1 weeks out: **driver practice at volume**, full-match simulations | Freeze. Tag. Deploy the tag and run it | Judge-interview rehearsal against unfamiliar adults | **TU28–TU31 (final projected Thu Apr 15 — rules can still change two weeks out)** | **[FACT] Fri Apr 9, 2027 — teams who have not paid and secured hotels are dropped from FCMP**, and slots reallocated regardless of region |
| **W32–W33**<br>Apr 19 – May 1 | P9 | **Nothing changes in the week before.** Pack | Nothing new. Rollback tag verified | Portfolio printed | Mock judge | **[FACT] *FIRST* Championship, Wed Apr 28 – Sat May 1, 2027** |
| **May – Sep 2027** | P10 Off-season | **[JUDGMENT] Where next season is actually won.** May: retrospective + inventory + register. June: recruit + fix the tooling that failed + grant windows open. July: one mechanism study + port the summer SDK release. **Aug: run the real two-week training course on BIOBUZZ Unlocked** (**[FACT]** released Jul 31, 2027) — a game you know cold, a field you own, rules you have read thirty times | Refactor now, never in season | The written season retrospective is portfolio content under the Jan-1 rule | Everything | **[FACT] Sep 11, 2027 — 2027-28 Kickoff.** Your next G0 should pass *before* kickoff week, comfortably |

### 2.6 If your first event is not 14 November

**[JUDGMENT]** Slide the four movable gates (G3–G6). **Hold G0, G1 and G2** — strategy and archetype are decided on kickoff weekend regardless of when you compete. A team that delays its archetype decision because "our event is in January" simply prototypes aimlessly for two extra months.

| Your first entry-level event | Weeks post-kickoff | G2 | G3 | **G4 freeze** | G5 alive | G6 ready | G7 rehearsal |
|---|---|---|---|---|---|---|---|
| **League Meet 1 — Oct 19** (earliest) | 5 | Sep 20 | **Sep 27** | **Oct 4** | **Oct 11** | **Oct 15** | Oct 17 |
| **Nov 14** — the baseline above | 9 | Sep 20 | Oct 4 | Oct 18 | Nov 1 | Nov 8 | Nov 12 |
| **Dec 5** | 12 | Sep 20 | Oct 11 | Nov 1 | Nov 15 | Nov 29 | Dec 3 |
| **Jan 9** | 17 | Sep 20 | Oct 18 | Nov 8 | Nov 29 | Dec 20 | Jan 7 |
| **Feb 6** (late region / LT) | 21 | Sep 20 | Oct 18 | Nov 15 | Dec 13 | Jan 24 | Feb 4 |

**[FACT] League teams: the meets are not warm-ups.** V0 §14 (final text): League Tournament rankings use **each team's top 10 League Meet matches plus the League Tournament matches**. Teams who played fewer than 10 League Meet matches get effectively-zero ranking points for the missing ones. **League Meet 1 carries permanent ranking weight — a league team must be reliable and scoring by W5, not W9.**

**[JUDGMENT] Two failures specific to a late first event.** *Scope inflation* — extra weeks get spent adding mechanisms instead of perfecting one, and the robot arrives in January less reliable than a November robot would have been. *Holiday collapse* — Dec 21 and Dec 28 are near-zero; a "17 continuous weeks" plan actually has 15. **And the compounding one [FACT]:** advancement allocations are released Nov 19 and the last RCMP is Mar 21 — a February first event means one, maybe two, of your three chronological shots before the window closes. Late-region teams do not get an easier season; they get **fewer attempts**.

### 2.7 The TBA register — do not let anyone fill these in

**[FACT]** From `research/SEASON-CALENDAR.md` §8. If someone hands you one of these numbers before FIRST publishes it, it is a prior-season figure or a guess.

1. **Your region's qualifier, league-meet and championship dates** — set by your PDP on `ftc-events.firstinspires.org`, not by FIRST HQ.
2. **Your region's advancement slot counts** — published Nov 19, 2026.
3. **All judged-award submission deadlines except the Leadership Award** — V0 §6 puts them on *"the deadline established by the Event Director or local Program Delivery Partner."* Nothing national can supply them. Set a recurring reminder to chase them.
4. **The Q&A close date** — never published, this season or prior ones.
5. **Last date to order BIOBUZZ field elements from AndyMark.**
6. **FCMP final payment deadline** (time known: 5:00 p.m. ET; date TBD) and the Registration/Storefront close date.

---

## 3. Roles for a small team

### 3.1 The minimum role chart — who must exist

**[FACT]** Hard constraints: **2–15 registered students**, grades 7–12; **2 screened adults** in Lead Coach 1/Lead Coach 2 with passed Youth Protection screening (screening is free, and I101 makes it a condition of earning an official season record); a DRIVE TEAM of **up to 4 people, at most 1 non-student** (the DRIVE COACH may be an adult). **[FACT]** BIOBUZZ §10 is a placeholder in V0 — re-verify DRIVE TEAM composition on kickoff morning.

**[JUDGMENT] The four roles that MUST exist. If one is missing you have a structural failure, not a staffing inconvenience:**

| # | Role | Owns | h/week, peak (Oct–Nov) | h/week, Dec–Mar | Backup required? |
|---|---|---|---|---|---|
| **1** | **Deployer** | Getting the build that worked yesterday onto the robot. **Not** writing features | 4–6 | 4 | **Yes — this is the most common single point of failure in small-team FTC** |
| **2** | **Driver 1** | Robot controls, the drive-practice log | 6 | 6–8 | **Yes, absolutely** |
| **3** | **Driver 2 / Human Player** | Second controller, human-player tasks | 5 | 5–6 | Yes |
| **4** | **Portfolio owner** | The 15 pages, the deadline, and the log at the end of every meeting | 5–6 | 4 | No — it is a shared cloud document |
| **5** | **Build lead / mechanism owner** | Fabrication, assembly, spares inventory | **10–12** | 8 | Yes |
| **6** | **CAD lead** | The Onshape master assembly, BOM, cut list | 8 (Sep–Oct), 2 after | 2 | **Yes — the most commonly single-deep role, and its absence stops fabrication, BOM and freeze at once** |
| **7** | **Drive coach / strategist** | Match strategy, alliance-selection input, scouting data → decisions. **May be the adult** | 3–4 | 5–6 | Yes |
| **8** | **Rules owner** | Thursday Rules Night, the Q&A candidates list | **0.5** | 0.5 | Yes (trivially) |
| **A1** | **Lead Coach 1 (adult)** | Legally mandatory. Registration, forms, event check-in, the money and admin calendars | 6–8 | 6–10 | The second adult *is* the backup |
| **A2** | **Lead Coach 2 (adult)** | Legally mandatory. **[JUDGMENT] Give them a defined job — logistics, ordering, transport — not engineering.** A parent who owns ordering and driving is worth more than a parent who "helps out" | 2–3 | 3–5 | — |

**[FACT]** The Mentor Manual's own role appendix lists **~27 student role-slots** and then recommends 6–12 students, resolving it with *"An individual can take on multiple roles; however, be sure that a single individual does not take on too many."* **[JUDGMENT] For a 5-student team that is 5.4 roles each. You cannot staff the official model, so decide in writing which roles you are *not* filling** — the alternative is filling all of them badly, which is what most small teams do by accident.

### 3.2 How the chart collapses onto real headcounts

| Students | Assignment | The honest verdict |
|---|---|---|
| **3** | ① Driver 1 + build lead ② Driver 2 + deployer ③ Portfolio + strategy + scouting + rules. Adult is DRIVE COACH | **[JUDGMENT] The true competitive floor.** Fails the moment one student is sick on event day. Nobody is redundant |
| **5** | ① Driver 1 + CAD ② Driver 2 + scouting ③ Deployer + vision ④ Build + spares ⑤ Portfolio + rules. Adult is DRIVE COACH + strategist | **[JUDGMENT] The small-team sweet spot.** The portfolio owner is not on the drive team, so they can be in the pit reading the judges' feedback form |
| **7** | Add a backup driver and a second builder. Rules owner becomes its own 30-min/week job | Two simultaneous absences become survivable |

**[JUDGMENT] The rule that keeps a small team from becoming brittle: every student attends every phase.** Do not let the programmers skip prototyping or the builders skip the portfolio. Specialization is what makes a small team fragile, and cross-training is what judges call "a team that understands its own robot."

### 3.3 Covering absences

**[JUDGMENT]** Assume **80% attendance** — normal for high-schoolers with jobs, sports, AP classes and college visits. On a 7-student team that is 5.6 at an average meeting, and the *distribution* matters more than the mean: some meetings are 3.

| Structural rule | Why |
|---|---|
| **Minimum crew = 3.** Below 3, the meeting converts to a documented solo task, never a cancellation | Cancelling is how a team loses 9 hours in a 9-week season without noticing |
| **Publish the "if only 3 show up, do this" list at the top of every meeting plan.** Good defaults: driver practice, spares fabrication, portfolio pages, log backfill, battery maintenance | Removes 20 minutes of milling around |
| **Never schedule G1, G4 or G7 on a low-attendance date.** Check the school calendar in Week A and mark conflicts on the gate board | These are whole-team decisions; re-running one costs a week |
| **Run the backup-owner drill once, in Week C.** Every role's backup does the role for two hours and the primary may not touch it | Surfaces which roles are single-deep *before* it costs you a week in November |
| **[FACT]** I102 requires an adult to check in **no later than 45 minutes before qualification matches**, with at least one student present | Adult coverage is a scheduling constraint, not a formality |
| **[FACT]** The manual explicitly permits loaning DRIVERS from a neighbouring team in a genuine emergency (*"a bus is delayed, a DRIVE COACH has no DRIVERS"*) — but **not** as a strategic upgrade | A real escape hatch. Know it exists; do not plan around it |

**The four artifacts that make absences survivable. Build them in October, not March:**

1. **A written pre-match checklist** — battery swapped and logged, fuse check, fasteners, wire strain relief, OpMode selected, starting configuration verified.
2. **A wiring/pinout map** — one page, laminated, in the pit box. Which motor in which port, which servo, which sensor.
3. **A deploy runbook** — numbered steps, **tested by someone who is not the programmer.**
4. **A shared drive, never a personal laptop.** Onshape is cloud-native; use that fact.

### 3.4 How AI absorbs the roles you cannot staff — and the ones it must never touch

**[JUDGMENT]** The design rule, stated once and enforced everywhere: **AI may compute, look up, draft, critique, format and record. Students generate the concepts, set the weights, take the measurements, observe the matches, make the calls, and say the words out loud to a judge.**

| Role you cannot staff | What AI actually absorbs | Time returned | What a student still must do |
|---|---|---|---|
| **Scouting analyst** | Writes the ftcscout pull + OPR script; generates pre-event dossiers and the watch list. **[FACT]** ftcscout's REST API needs **no authentication**; a **130-line pure-standard-library Python script** reproduces its published OPR to within 2.16 points and runs a 31-team event in 1.07 s | **[ESTIMATE]** ~0.5 h/week; **~5.5 h on an event week** | Walk the pits, watch robots, record downtime / auto-start conflict / driver quality — **none of which is in any dataset** — and order the pick list |
| **Technical writer** | Meeting notes → decision log → portfolio *draft* structure. Mechanical passes: page-count trim, contrast and font compliance, PII scrub, A201 preflight | **[ESTIMATE]** ~3–4 h/week Oct–Jan. **The portfolio lead is the single biggest beneficiary in the whole program** | Write the sentences that describe their own reasoning, and be able to expand on any page for two minutes in an interview |
| **Rules officer's reading load** | The Thursday Team Update diff, flagged against *your* subsystems, in ~8 minutes. The weekly Q&A answer digest | **[ESTIMATE]** ~1–2 h/week | Present the diff, decide whether it changes the robot, and own the Q&A candidates list |
| **Project manager** | Meeting agenda generated from the gate board; slip detection; the season plan kept current | **[ESTIMATE]** ~10 min/week | Run the standup and enforce the gate dates |
| **Grant writer / sponsorship coordinator** | Boilerplate from *your* narrative; budget tables; the cost-per-student figure that reads well in a letter | **[ESTIMATE]** ~1.5–2 h/week, front-loaded Aug–Oct | Sign it, send it, and maintain the relationship. Sponsors respond better to students |
| **Software mentor (partial)** | Boilerplate, `hardwareMap` wiring, OpMode skeletons, API lookups, stack-trace triage, **the tuning harness and the tests small teams always skip** | **[ESTIMATE]** 40–55% of software hours | Design the control strategy, turn the knobs, watch the robot, and explain every line without the AI in the room |
| **Judge-prep coach** | Mock judge, two questions in two minutes, every meeting; a full 45-minute mock two weeks before each event | **[ESTIMATE]** ~0 net — it *adds* value, not hours | Answer out loud, standing, in a noisy room |

**Roles AI cannot absorb at all — do not plan as if it can:** Driver · Drive Coach · Builder · **the person who deploys code at an event** · the student being interviewed · the person who decides which concept wins · anyone taking a measurement.

**[FACT] Two constraints that come before any of this** (`research/AI-IN-FTC-POLICY.md`): Anthropic's consumer terms require users to be **18+**, so **Claude Code runs on the mentor's account with students in the room** — never shared credentials; and **A201 requires an AI credit footnote** in the portfolio. **[JUDGMENT]** The 18+ constraint is a feature: it forces the pair-working pattern that makes a student able to answer the follow-up question, which is exactly what the judge interview tests. Also check your **school district's AI policy** — it binds your students independently of FIRST and of Anthropic, and may be stricter than both.

**[FACT] Community temperature, so you calibrate the interview:** a Chief Delphi poll (n=384) ran **37% against generative AI, 39% neutral, 24% for.** **[JUDGMENT]** A judge drawn at random is more likely skeptical than enthusiastic. Be matter-of-fact, never evangelical: name the tool in the same breath as FTCLib and goBILDA when asked, and **never frame AI as the reason the work is good**. And never tell a judge you did not use AI when you did — that is the only real disqualification path in this whole area (Competition Integrity Contract §1.5.1).

---

## 4. Deliverables parity — the elite version, the lean version, and what it costs

**[JUDGMENT]** "~80% of the value" is my estimate in each row, and the residual is named honestly. Costs are **as of August 2026** and need re-checking. Hours are **[ESTIMATE]** team-hours unless stated.

| Deliverable | Elite approach | The lean approach that gets ~80% | Cost | Hours | AI leverage | **The 20% you give up** |
|---|---|---|---|---|---|---|
| **Competitive robot** | Bespoke CAD-first robot, V1→V2→V3 across the season, in-house CNC, 15–25 students, 500+ h each. **[FACT]** 6165 CuttleFish CADed V1 **8 days** after kickoff | **StarterBot Base drivetrain** (goBILDA drop-center 6WD or its mecanum variant; REV DUO channel) as the *actual* competition chassis — legal under R304/R101 provided **your students assemble it** — plus **one** scoring mechanism perfected. COTS structure over custom plates. 3D print the brackets; outsource only the 3–6 plates that need precision | **$1,500–2,500** (Tier A–B robot lines) | **~260** to Event 1 | BOM and cut-list generation from the CAD; R102/R105/R503 design review; mechanism arithmetic (gear ratio, torque, flywheel RPM, compression); lead-time watch. **Never** the concept choice or any dimension | Scoring ceiling and a bespoke footprint. **[JUDGMENT] Rarely decisive.** A well-tuned mecanum or 6-wheel drivetrain won the 2026 championship |
| **Reliable autonomous** | Multi-branch autos, custom localizer, vision fusion, hundreds of logged runs, a dedicated software subteam | **Pedro Pathing or Road Runner** + a **goBILDA Pinpoint V2** ($79.99). **One trunk with ≤3 branches, tuned to death.** Success criterion: **8/10 over 10 logged runs with the endpoint spread recorded.** Log battery voltage on every run and never debug an auto without checking it first | **$80–280** (Pinpoint + 1–2 odometry pods at $99.99) | **~40** programmer-hours | Tuning harness, datalogger, CSV analysis, OpMode scaffolding, log-based debugging. **[FACT] AI cannot tune your PID from a chat window** — every gain it produces is a starting guess to be measured | Auto *ceiling*. **[JUDGMENT] Not auto reliability**, which is the part that is a tiebreaker. This row is close to full parity |
| **Driver skill** | Hundreds of practice matches by April; a second practice robot so drivers never wait on repairs | **18 tiles + DIY perimeter + the one scoring structure.** 2 h/week from W4, 3 h/week between events, 4 h+ for championship. Objective driver selection: a fixed 90-second drill, run twice, **scored again a week later — improvement matters more than the first number.** Pre-kickoff, use *FIRST*'s free **Skill Builders** mini-games as scored driver trials | **~$300** (tiles $147 + lumber $120–180) | **2–4 h/week, forever** | **None. Zero. This is the row the reclaimed hours are for** | The second robot. Real, and unfixable at Tier A/B — mitigate with a defended weekly freeze block instead |
| **Engineering portfolio** | 15 professionally designed pages, dated progression timeline, per-version strengths/weaknesses lists, a Problem → Solution → Key Feature template per mechanism | **The same 15-page limit** — binding on a 30-student team, free for you. Adopt the 6165 skeleton. Ten minutes at the end of **every** meeting: photos in, one paragraph per workstream. The portfolio is then an editing job, never a writing job | **~$20** print | **60–90** student-hours, front-loaded | Structure, page-budget trim, A201 preflight, contrast/font checks, PII scrub, the credit footnote. **Never prose the students did not write** — judges do not need a detector, they have a five-minute conversation with the author | Graphic design polish. **[JUDGMENT] A plain, honest 15 pages beats a beautiful 15 pages written in a panic** |
| **Control Award submission** | A dedicated software subteam, custom controllers, a published open-source library | Sensors + genuinely closed loop + **a written statement of how you measured reliability.** **[FACT]** Control is the most robot-correlated non-Inspire award (median winner at the **22nd percentile** of their event) but it rewards **feedback, not speed** — a slow robot with a real closed-loop auto is a genuine candidate | **~$130** (REV 9-Axis IMU $38 + Pinpoint $79.99 + a ~$10 break-beam) | Inside the software hours | Draft the Control content **from the actual code and git log**. Prepare an honest 20-second answer to the question already in the bank: *"What pre-programmed libraries or outside resources did your team use?"* | Nothing structural. This is the cheapest technical award for a small team |
| **Scouting data** | A custom two-part app (23619 Overture: React/Vite capture → QR → Streamlit processing) plus a dedicated scouting squad | **Tier 1 — one laptop, one notebook.** T-3 days: printed dossiers per registered team from ftcscout. Event morning: 90-second pit cards. Rounds 1–3: watch, record downtime / auto-start conflict / driver quality. Lunch: recompute OPR, emit tiers. Rounds 4–5: **negotiate in the pits** | **$0** + printing | 20 min prep + **~45 min** across an event day | AI writes the pipeline once (~12 h one-time). **[FACT]** Never the pick list: a published attempt was *"worse than sorting by averages."* **[FACT]** OPR's split-half reliability at a 5-match qualifier is **r = 0.53** — roughly a third of any statistical pick list is noise | Per-match cycle counts on tracked robots. **[JUDGMENT] Add them only if a student wants the project as their own portfolio artifact** |
| **Outreach (Connect / Sustain / Reach)** | **[FACT]** 8565 TechnicBots: ~2,000 outreach hours/year | **One recurring event + one sustained partnership, documented with counts.** **[FACT]** Judges weight *sustained* outreach above one-off outreach and will **audit** any defined term you use ("started a team", "reached N people"). One monthly partner beats six photo-ops. **[FACT]** Work since **1 Jan 2026** counts — inventory your spring and summer now | **$0–100** | **70–90** student-hours, front-loaded Aug–Oct | Sponsor and grant boilerplate from *your* narrative; outreach materials; the ask template. **Never a fabricated number** | Scale. **[JUDGMENT] Irrelevant** — Connect/Sustain/Reach winners sit at the 43rd–46th percentile of robot performance. These are your highest-probability awards |
| **Judge interview** *(bonus row — the uncapped resource)* | Rehearsed against unfamiliar adults, every student fluent | **Rehearse 5 minutes, not 10** — that is the only guaranteed uninterrupted judge contact all season (A205). Every student speaks. Rehearse the **unscheduled pit** version. **[FACT]** *"Teams may participate in judging regardless of the inspection status of their ROBOT and are eligible for awards even if they are attending the event without a ROBOT"* | **$0** | 2 min/meeting + 45 min before each event | Mock judge, every meeting. **[JUDGMENT] The cheapest award value AI produces in the whole program** | Nothing |
| **Reliability & spares** *(bonus row)* | A complete spare of every failure-prone part | **3 batteries + 2 chargers.** Nylon locknuts everywhere, threadlocker on every set screw, a full fastener lap before every event. Strain-relieve every USB and XT30. Spares of **only** what your own failure log names. **[FACT]** REV repairs a fried Control Hub for **$165** vs $375 new | **~$300–400** | ~4 h/week during build | Generate the pre-match checklist and the self-inspection checklist against V0 R-rules — **not last year's**, since R503 moved from 8 motors/10 servos to **8/8** | Depth. One catastrophic simultaneous failure still ends your day |

---

## 5. Where the hours go

### 5.1 The weekly budget, before and after AI

**[ESTIMATE]** A 6-student team, peak build season (Oct–Nov), at 12 in-room hours + 3 async hours per student = **~90 student-hours/week**. Figures are total person-hours across the team, not per person. **These are hypotheses to measure against — record your real hours for four weeks and correct this table.**

| Workstream | **Before AI** | **After AI** | Δ | Where the difference comes from |
|---|---|---|---|---|
| Build, fabricate, assemble | 26.0 | **30.0** | **+4.0** | Reclaimed hours land here first |
| **Drive practice** | 2.0 | **6.0** | **+4.0** | **The single most important reallocation in this document** |
| Prototype, test, measure | 8.0 | **11.0** | **+3.0** | One more prototype-and-test cycle per week |
| CAD + design arithmetic | 12.0 | 8.0 | −4.0 | BOM/cut-list generation, mechanism math, R-rule review |
| Software | 12.0 | 7.0 | −5.0 | Boilerplate, API lookup, stack traces, tuning harness (~42% — inside the 40–55% band) |
| Documentation + portfolio | 10.0 | 5.5 | −4.5 | Notes → decision log → draft structure; mechanical A201 passes |
| Rules reading + Team Update digest | 3.0 | 1.0 | −2.0 | The Thursday diff drops from ~an hour to ~8 minutes |
| Scouting prep + data | 3.0 | 1.5 | −1.5 | The pipeline was written once; it now runs |
| Team ops (grants, sponsors, ordering, scheduling) | 6.0 | 4.0 | −2.0 | Boilerplate and budget tables |
| Meetings, standups, cleanup, admin | 8.0 | 8.0 | 0 | Irreducible |
| **AI verification tax** | 0.0 | **2.2** | **+2.2** | **Real, and it grows if you cut it.** Every hour skipped is repaid at an event at a worse rate |
| **Total** | **90.0** | **90.0** | 0 | The week does not get longer |
| **Reclaimed and reallocated to hands-on work** | — | — | **+11.0 h/week** | Build +4, drive +4, prototype +3 |

**[JUDGMENT] Three honest caveats, or this table is a lie.**

1. **The hours are not evenly distributed.** Most land on the portfolio lead, the strategy lead and the mentor. A builder who does not write documents gains almost nothing from AI — which is fine, because a builder should be building.
2. **The verification tax is not optional.** It is the price of the other numbers being real.
3. **Reclaimed hours evaporate unless you schedule them.** This is the most common failure of the entire approach.

### 5.2 Claiming the hours — the rule that makes this real

**[JUDGMENT]** The day you free an hour, write the replacement block on the **same whiteboard as the gate board**, by name and time. If "Tuesday 7:00–8:00 p.m. — driver practice, Driver 1 and Driver 2" is not on the board, it will not happen, and you will have bought nothing.

| Reclaimed from | Converts into | Why this and not something else |
|---|---|---|
| Design arithmetic | **One more prototype-and-test cycle per week** | Iteration count is the design input that most reliably predicts a robot that works. **[FACT]** GM0's benchmark is *"10+ iterations of intake designs"* |
| Documentation | **Driver practice** and **judge-interview reps** | Driver practice is a discipline, not a warm-up; the interview is the only uncapped resource once the portfolio hits 15 pages |
| Scouting arithmetic | **Walking the pits, watching robots, negotiating** | The three things that decide alliance selection and that no dataset can do |
| Game analysis | **The Saturday prototype block** | Physical contact with a game element beats any additional analysis |
| Mentor operations time | **Standing at the bench during build sessions** | And the mentor must be present anyway for the AI sessions |

**[JUDGMENT] The AI-free block.** Make the Saturday prototype block AI-free by rule. A model generates infinite plans at near-zero cost; the gate dates and this rule exist to stop beautiful planning from replacing cardboard.

### 5.3 The async multiplier — the only lever that adds hours instead of cutting scope

**[FACT]** GM0: *"Team meetings should be used as time to catch up between squads, make decisions, and physically test parts of the robot. CAD design iterations can be created and reviewed at home, and software can be written outside of practice hours."*

| Must be in the room | Can be async |
|---|---|
| Driver practice · physical prototyping and testing · assembly, wiring, integration · **every gate decision G1–G7** · the design-freeze review · the full-team demo · judge-interview rehearsal | CAD iteration · code that does not need the robot (path planning, state machines, telemetry, unit-testable logic) · portfolio writing and layout · scouting spreadsheet and formula work · Team Update reading · grant applications and sponsor letters · BOM building and price checks |

**[ESTIMATE]** 3 async hours per student per week × 7 students × 9 weeks = **+189 student-hours ≈ +24%**, for zero dollars and zero extra facility time. That is larger than every hardware compression combined.

**Three rules that stop async work from becoming divergence [JUDGMENT]:** (1) **it lands in the shared tool or it did not happen** — a CAD file on someone's laptop is a liability, not work; (2) **every async output gets 5 minutes at the next full-team demo** — unreviewed async work is exactly how two students spend three weeks building incompatible things; (3) **async never covers for absence.**

---

## 6. The top ten mistakes that sink small teams

**[JUDGMENT]** Ranked by how often they end a small team's season, drawn from the failure modes in `research/SEASON-CADENCE.md` §10.2, `research/SMALL-TEAM-ECONOMICS.md` §5.2 and the anti-pattern list in `playbook/AI-FOR-DESIGN-AND-ANALYSIS.md` §7.

| # | Mistake | Why it feels right at the time | How you actually lose | **Countermeasure** | Early warning sign |
|---|---|---|---|---|---|
| **1** | **Cutting driver practice** | *"The robot isn't done, so we can't practise"* | **[FACT]** GM0 names this as the classic new-team failure. A robot that is 20% better, driven by someone with 3 hours of stick time, loses to a simpler robot with 30 hours. Cycle time is dominated by driver skill, not mechanism speed — and practice hours cannot be recovered, only spent in advance | **20-minute field block at every meeting, mandatory, from the day a chassis exists.** A defended weekly 90-minute robot freeze enforced with a timer, not a discussion. Put the practice surface in the *same room* as the workbench so practice and build run concurrently | It is W8 and no student has 10 logged hours of driving |
| **2** | **Serializing CAD behind prototyping** | *"We can't CAD until we know the mechanism"* | Design freeze slips 2 weeks → parts arrive late → integration compresses into event week → nothing is tuned, nothing is driven | **Drivetrain and electrical CAD start in W1 and never wait for prototypes.** Four things run in parallel by design; if the CAD workstream is idle in W1–W2 you have already lost two weeks | The CAD lead has nothing to do in kickoff week |
| **3** | **Writing the portfolio at the end** | *"We'll do it when we know what we built"* | The photos and the data **do not exist**. You cannot retroactively document a prototype you threw away in September, and A201 limits you to work you actually recorded since Jan 1 | **Ten minutes at the end of every meeting**, owned by one named person: photos in, one paragraph per workstream. Allocate the 15 pages on kickoff weekend and write each one in the week it happens | No dated build-log entries for W2–W5 |
| **4** | **Single-deep roles — especially the deployer** | *"There aren't enough of us"* | **[JUDGMENT] The most common small-team catastrophe is not a broken robot.** It is that the one student who understands the code has the flu on event day and nobody can push the working version. One absence stops a workstream for a week — 11% of a 9-week season | **Backup owner named for every workstream on kickoff Sunday.** The four artifacts in [§3.3](#33-covering-absences). Run the backup-owner drill in Week C. Redundancy in exactly three places: driver, deployer, assembly knowledge | The CAD lead is the only person with an Onshape login |
| **5** | **Attempting every scoring task** | *"More points is better"* | **[FACT]** R503 gives you 8 motors and 8 servos and R102 gives you an 18-inch cube — both hard. Four half-working mechanisms score less than two working ones and take three times as long to debug | **The "not doing" list at G2, signed and on the wall.** If the mechanism list grows after Sep 20, something else comes off. GM0: *"Perfect one objective first"* | Your mechanism list is longer in October than it was in September |
| **6** | **Burning an advancement-eligible event as a shakedown** | *"We need the experience"* | **[FACT]** V0 §4: you may attend more than three entry-level events but are eligible to advance **only from the first three chronological ones**. A shakedown qualifier with a robot you know is not ready spends one of three shots | **Go to a scrimmage instead** — neither a QT nor an LT, so it does not consume a slot (confirm with your PDP before registering). If your region runs only 2–3 qualifiers, pick the **latest** one and treat G6 as non-negotiable | You registered for the first event on the calendar without asking why |
| **7** | **Missing the money and admin calendars** | *"Grants are a fall problem"* | **[FACT]** Grant windows close **Sep 30 – Oct 31** — exactly W3 to W7, when the team is prototyping, freezing CAD and fabricating. A grant application written in October is written badly or not at all. **[FACT]** And regional deadlines exist that no national document contains: WA's *"9-25: Need to be registered… to be placed into a league"*; SoCal's **$300 due Oct 17** | **Every grant application goes in before kickoff or in the week after.** Put "grants submitted" and "PDP questions answered in writing" on the **G0** checklist. One adult owns the Tuesday admin sweep in kickoff week | A G4 parts order depends on money not yet in the account |
| **8** | **One tool, no fallback** | *"We have a printer, we're fine"* | **[FACT]** FTC 12736 lost their CNC router in stages through October — chuck, then spindle, then *"aluminum got into the computer and fried the whole thing"* — with replacement grant money weeks away. Their season survived only because they **rebuilt the entire robot in wood** | **Write the fallback manufacturing path on the gate board in one sentence** before you need it. **[JUDGMENT] And generalise their fix: build the geometry in the cheap material first.** Plywood and printed parts find the assembly-order problems while the real stock is still on order | You cannot name, in writing, what you would do tomorrow if the printer died |
| **9** | **Skipping the dress rehearsal** | *"It's just a qualifier"* | **[JUDGMENT] Half of a small team's first-event losses are logistics, not robot** — failing inspection on a robot-sign rule, a battery nobody charged, a portfolio nobody printed, an unscheduled pit interview nobody rehearsed | **G7 on the board from kickoff day**, four days before Event 1: check-in, self-inspection against the official checklist, six back-to-back matches with battery swaps, an unscheduled pit interview, pit-kit inventory, a field-repair drill under E107. If time collapses, run the **90-minute version** — never skip inspection and the pit kit | G7 is not on the board |
| **10** | **Letting AI hollow out the students — or letting the reclaimed hours evaporate** | *"We saved so much time this season"* | Two distinct losses, same root. **(a)** The code works and nobody can explain it; the Control interview becomes twelve minutes of "um", and a portfolio page the author cannot expand on loses Think, Control and Inspire at once. **(b)** You "saved" 11 hours a week and the drivers still have four hours of practice — which forfeits the entire premise | **(a)** The **"explain it back"** rule for code — no diff merges until a student can explain every line without the AI in the room; and the **whiteboard test** for design — draw it, name every dimension and where the number came from, name what will break it, name one concept you rejected. **If they cannot, the part is not designed — it is downloaded. Do not cut it.** **(b)** [§5.2](#52-claiming-the-hours--the-rule-that-makes-this-real): every freed hour gets a named calendar block the same day | A student says "the AI wrote that part" about anything on the robot or in the portfolio |

**Three runners-up that also end seasons [JUDGMENT]:** **no spares** (one bent 3/8 in. shaft ended a real team's event day); **budgeting on money you have been awarded** but not received; and the **January ground-up rebuild with no gate dates** — GM0 puts a rookie rebuild at *"50–100+ hours"*, which at 9 h/week is 6–11 weeks, i.e. past your regional championship.

---

## 7. The pre-season sprint — 22 August → 11 September 2026

### 7.1 Why this window is worth more than any three weeks in the season

**[FACT]** V0 §12.3 **R304**: *"Custom software, designs, and parts can be reused year-to-year. ROBOT software, designs, and FABRICATED ITEMS created before Kickoff are permitted."* — **both clauses are R304**. (**R305** is "SCORING ELEMENTS are not allowed for ROBOT construction"; flat-text greps mis-pair the two.) A FABRICATED ITEM is defined as anything *"altered, built, cast, constructed, concocted, created, cut, heat treated, machined, manufactured, modified, painted, produced, surface coated, or conjured partially or completely into the final form in which it will be used on the ROBOT."*

**[JUDGMENT]** There is **no build-season start in FTC**. This is the opposite of the FRC bag/withholding tradition and small teams routinely fail to exploit it. **[FACT]** Sections 1–7, 12, 14 and 16 of the V0 manual are **final now** — including every R-rule you will build to. Only the game itself (§§8–11, 13, 15) and R105's expansion numbers are hidden.

| You legitimately MAY, today | You still MAY NOT |
|---|---|
| Build a complete competition drivetrain and use it unchanged in November | Violate **R101** — MAJOR MECHANISMS must be built **by the team**. A mentor-built or vendor-built major mechanism is illegal no matter when it was made |
| Cut, drill, machine, 3D-print, weld, paint any structural part | Exceed **R102**'s 18-inch starting cube |
| Build and wire the entire electrical system on a plate | Exceed **R503**'s 8 motors + 8 servos |
| Write, test and reuse **all** software | Use a COTS MAJOR MECHANISM beyond R301's limits, or a COTS mechanism with >1 degree of freedom (R303) |
| Build spare parts, a spare drivetrain, a spare wiring harness | Use pneumatics (R801) |
| Build practice field elements and a practice field | Assume anything about the game — §§8–11 do not exist yet |
| Build sizing tools, pit carts, battery carts, cable management | Guess R105's expansion limits — **[TBA] at kickoff** |

**[FACT] And judging counts this work.** V0 §6.1.1 and A201.E: *"For the purposes of judging, the current season begins on January 1, 2026."* **Your August pre-season work is portfolio-eligible. Photograph and log it now.**

### 7.2 What FIRST has already told you about the game

**[FACT]** From `https://community.firstinspires.org/game-preview-field-elements`:

- **Scoring element: POLLEN** — *"plastic balls approximately 3 in. in diameter, that have similar characteristics to the Artifacts used in… DECODE."* Measured elsewhere in this workspace at **2.8 in ± 0.1 in, 0.055 lb (~25 g)**. Available for immediate shipment now.
- **Four named robot tasks teams are told to explore starting today, all acquisition-side:** intake Pollen off the foam field surface; intake **multiple** Pollen (in a line, and in piles); **intake off field walls and out of field corners** (*"Pollen will naturally roll against the field border, and into the field corners"*); **navigate and intake Pollen autonomously** between known locations with no human intervention.
- **StarterBot Bases** published by AndyMark, goBILDA, REV and Studica — each *"a drivetrain and intake."* Full StarterBot designs release at kickoff.
- ***FIRST* Tech Challenge Skill Builders** — seven free mini-games on the *FIRST* Training platform, with built-in lessons, build instructions from all four vendors, editable printable slides, **a scoring spreadsheet with built-in rankings and adjustable point values**, and a facilitator guide.

**[JUDGMENT] FIRST has shipped you a pre-season season.** Use Skill Builders two ways: run one per pre-season meeting as the field block, **scoring it properly, and pick your two drivers on the numbers rather than on seniority**; and hand the facilitator guide to a student and let *them* run it — that is Motivate/Reach evidence that costs an adult nothing.

### 7.3 The buy list, and the one supply warning

**[FACT] All prices read from vendor pages 21–22 August 2026. Verify before ordering.**

**Tier 1 — order this week, non-negotiable [JUDGMENT]**

| Item | SKU | Price | Note |
|---|---|---|---|
| BIOBUZZ POLLEN Preview Pack (3 balls) × 8–10 | `am-5851_preview` | **$5.50 ea → $44–55** | Ships immediately; **31,449 units in stock as of Aug 22**. Order once in volume — a customer review complains shipping was *"over $30 for $22 in pickleballs"* |
| REV Control Hub — via the storefront **Electronics/Control set** (Hub + servo + 2 sensors + cables), *not* a bare Hub | `REV-31-1595` | **set $350 via *FIRST* Storefront**; bare Hub $375 retail | Only officially supported robot controller (R701). **Buy it on your dashboard, not at retail — $25 saved for zero effort** |
| REV Driver Hub | `REV-31-1596` | **$275 retail**, or the storefront **Driver Kit $295** (Driver Hub + 2 gamepads + webcam) — buy the kit | Only officially supported driver station (R901) |
| goBILDA Pinpoint V2 Odometry Computer | `3110-0002-0002` | **$79.99** | Cheapest reliable path to good localization |
| *FIRST* Tech Challenge Field Soft Tiles | `am-2499` | **$147** (18, half field) / **$293** (36, full) | 24×24×5/8 in. EVA foam. **Lay them smooth side up.** All variants in stock |
| DIY perimeter — 2×4 and plywood | — | **~$120–180** [UNVERIFIED — get a local quote] | vs. **$740** for the official `am-0481b` kit. Measure to ±1/8 in.; make the inner face smooth, because Pollen rolls against the border by design |

**⚠️ [FACT] Supply warning, re-verified 2026-08-22: the REV Expansion Hub (`REV-31-1153`, $275) is OUT OF STOCK.** If your architecture needs a second hub, order it now or design without it. Discovering this in October is a season-shaping problem — and the **$125 Expansion Hub Repair Service** may be the only route to one.

**[JUDGMENT] Defer the game set.** The **$599 full set** is **1,568 units deep on backorder** against 291 for both $399 partial sets combined, it is **non-returnable** (cancellation is store credit less a 5% fee), and it starts shipping **Mon Sep 14 — two days after kickoff**. Buy Pollen now, buy tiles now, build the perimeter, and decide on a **partial set after you have seen the game.** FIRST's own copy says the partial set has *"all game-specific items needed to practice."* Supplement with 3D-printed Pollen for intake-geometry iteration — but keep at least a dozen real ones, because printed balls are useless for anything mass- or bounce-dependent.

**[ESTIMATE] Lean pre-season total:** Tier 1 + minimal Tier 2 + tiles + DIY perimeter ≈ **$1,100–1,400** assuming you already own structure and motors; ≈ **$2,000–2,300** green-field including the goBILDA FTC Starter Kit (`3200-4008-2627`, $899.99) — with the partial game set added in late September.

**Space requirement:** 12×12 ft of field plus ~2 ft of driver/working clearance on two sides ≈ **16×16 ft (256 sq ft)** minimum. If you cannot get that, get **half a field (6×12 ft)** — enough for intake work, cycle timing and one-side auto; not enough for full-field auto or realistic driving.

### 7.4 The skills bootcamp — three sessions that make kickoff possible

**[FACT]** Elite teams treat the summer as a training programme: Overcharged/RevAmped ran *"two weeks in August of an intensive training course"* in building, CAD, programming and electronics; 12736 ran a camp where *"four groups build FTC robots"* and played a tournament on the last day, explicitly *"to onboard new students."* GM0: *"Cross-train your members… Having all your members learn at least one skill outside of their expertise will go a long way."*

**[JUDGMENT]** You have 21 days, not a summer. Run the compressed version — **three 90-minute sessions, each taught by whoever on the team is strongest, each ending with every student having *done* the thing once.**

| Session | Week | Every student must personally complete | Why it pays off at kickoff |
|---|---|---|---|
| **S1 — Deploy** | A | Clone the repo, change one telemetry line, build, deploy to the Control Hub, drive the robot, commit and push | On kickoff Sunday, **any** student can test an idea in code without waiting for "the programmer" |
| **S2 — Fabricate** | B | Cut, drill and mount one bracket. Make one 3D print from an existing STL. Crimp and land one wire to R609/R610 spec | Kickoff-weekend prototyping is limited by how many people can safely make a part |
| **S3 — CAD** | C | Model one simple part in Onshape and place it in the shared team document | The design-freeze bottleneck is the single-deep CAD lead. Three people who can model a bracket removes it |

**Plus two drills that cost two hours and save weeks [JUDGMENT]:**

- **The backup-owner drill (Week C).** Every role's backup does the role for two hours; the primary may not touch it. It surfaces exactly which roles are single-deep.
- **The logins deliverable (Week A).** Answer GM0's question in writing: Onshape team document, GitHub org, shared drive, team channel, *FIRST* dashboard youth accounts, ftcscout. **A student who cannot open the CAD cannot help with the CAD.**

### 7.5 The G0 checklist — Friday 11 September

Print this. Tick it as a team. **[JUDGMENT] A failed G0 does not delay the season — it converts kickoff weekend into a build-the-drivetrain weekend and costs you the strategy window, which is the one thing you cannot buy back.**

- [ ] Chassis drives a **figure-8** under gamepad control
- [ ] Every student has deployed code to the robot at least once
- [ ] A taped or tiled field exists; **≥24 Pollen in hand**
- [ ] Three instrumented intake rigs **with a data table**, not opinions
- [ ] Path-following library installed; "drive to a coordinate and stop within 1 in." is repeatable
- [ ] **Two drivers selected on the numbers** from a scored drill, plus a named backup
- [ ] Team registration complete per **I101**: fee paid, **two adults in Lead Coach 1/2 with YPP screening passed**, all youth registered on the dashboard
- [ ] **S1/S2/S3 bootcamp done** — every student has deployed, fabricated and CADded once
- [ ] **Backup-owner drill run; single-deep roles identified in writing**
- [ ] **Every grant application submitted** (windows close Sep 30 – Oct 31, inside your prototyping phase)
- [ ] **PDP emailed and answered in writing**: league or QT? earliest and latest entry-level event? when does sign-up open? **what do we owe you and by when, on top of $350?**
- [ ] PDP newsletter subscribed; last three issues read; every regional deadline on the gate board
- [ ] **Fallback manufacturing path written down** — one sentence, on the board
- [ ] `CLAUDE.md` written; `permissions.deny` on the SDK directory; the deploy runbook tested **by someone who is not the programmer**
- [ ] Three elite portfolios read as a team; your portfolio shell exists with a **dated progression timeline already being dated**
- [ ] Kickoff run-sheet printed; mock-element materials, whiteboards, printed R-rule summary, scoring-model template and **food** all staged on Friday

### 7.6 Kickoff weekend, in one paragraph

**[FACT]** Broadcast **12:00 p.m. ET Saturday Sep 12**, in person or on the *FIRST* Tech Challenge YouTube channel. **[JUDGMENT]** Keep the three artifacts the elite pattern always produces, at whatever scale you can staff: **read the manual as a team, build a scoring model, and prototype the hard mechanism the same day** — that is FRC 254's canonical Day 1 log compressed to your size. Build **mock field elements from the released drawings** with cardboard and plywood in about three hours, because no team in North America has real elements this weekend. Run **divergent-then-convergent ideation with delayed judgment** (12736's method) rather than letting the first idea win. Join the **Open Alliance**. And end Sunday with **G1**: one paragraph everyone can recite. *Robot in 30 Hours* streams the same weekend from 1:30 p.m. ET — **[JUDGMENT] do not watch it live during your own strategy block**, because it will anchor you to other people's first guesses; watch the 8:00 p.m. Day 1 Recap *after* your decision, as a check on your reasoning. The hour-by-hour version is `research/SEASON-CADENCE.md` §4; the AI-side protocol is `reference/ANALYSIS-PROTOCOL.md`.

---

## 8. The wall version — print this page

```
AUG 22 ── PRE-SEASON (3 wks) ────────────────────────── SEP 11   G0  chassis drives, code deploys, field exists,
             W-A infrastructure + admin sweep + grants                 3 rigs measured, 2 drivers chosen, bootcamp done
             W-B drivetrain + wiring plate + perimeter          A1  PDP answered in writing, grants identified
             W-C measure the rigs + localization + drills       A2  chassis rolls (Aug 30 target / Sep 4 hard)

SEP 12 ── KICKOFF WEEKEND (48 h) ────────────────────── SEP 13   G1  archetype chosen — one paragraph, recitable
             12:00 ET reveal · manual read as a team                 POINT OF NO RETURN: MON SEP 14
             scoring model · mock elements from drawings
             prototype the hard mechanism · join Open Alliance
             GATE BOARD ON THE WALL, PERMANENT MARKER

SEP 14 ── STRATEGY (W1) ─────────────────────────────── SEP 20   G2  strategy frozen + THE "NOT DOING" LIST
             TUE = SDK MERGE BLOCK (2 h now, 2 wks in Nov)      A3  event registration done
             THU = TU01, the heaviest patch of the season       A4  [TBA] league registration (WA: SEP 25)
SEP 14 ── PROTOTYPING (W1–W3) ───────────────────────── OCT 04   G3  mechanisms selected, one page of numbers each
             SEP 28 Q&A OPENS 12:00 ET — submit MON–WED         A5  every grant application submitted
SEP 28 ── CAD (W3–W5) ───────────────────────────────── OCT 18   G4  DESIGN FREEZE — hardest gate to recover
                                                                A6  [TBA] regional fee due (SoCal: OCT 17)
OCT 05 ── BUILD + INTEGRATION (W4–W7) ───────────────── NOV 01   G5  robot alive        [earliest league meet OCT 19]
OCT 19 ── PROGRAMMING + TUNING (W6–W8) ──────────────── NOV 08   G6  competition ready — auto 8/10, portfolio printed
NOV 09 ── DRIVER PRACTICE + SPARES (W9) ─────────────── NOV 12   G7  dress rehearsal — full simulated event day

NOV 14 ── EVENT 1 ── iterate 7-day loop ── EVENT 2 ── iterate ── EVENT 3
             NOV 19 advancement allocations released           [QT peak NOV 30 – JAN 18]
             DEC 15 LEADERSHIP AWARD DUE (4,000 chars)         [LT late JAN – FEB]
             DEC 21 + DEC 28 = ZERO WEEKS. PLAN FOR THEM.      [RCMP DEC 5 – MAR 13]
MAR 21 ── LAST RCMP THAT FEEDS HOUSTON ───────────────────────  APR 09 unpaid/unhoteled teams dropped
MAR ─── CHAMPIONSHIP PREP (4–6 wks) ────────────────── APR 28   FIRST Championship APR 28 – MAY 1
MAY ─── OFF-SEASON LOOP ────────────────────────────── SEP 11 2027   next season's G0, passed early

EVERY THURSDAY:  Rules Night, 30 min. TU00 SEP 12 → TU31 APR 15. One question: does this change our robot, auto, or math?
EVERY MEETING:   The robot touches the field. The log gets an entry. Two mock-judge questions, two minutes.
EVERY WEEK:      Driver practice is on the calendar by name and time, or it does not happen.
ADVANCEMENT:     Only your FIRST THREE chronological QT/LT events are advancement-eligible. Pick them on purpose.
MONEY:           Every grant goes in BEFORE kickoff. Ask your PDP what you owe THEM on top of the $350.
AI:              It computes, looks up, drafts, critiques, formats and records. Students decide, build, measure,
                 drive, and say the words out loud to a judge. Explain-it-back for code. Whiteboard test for design.
WHEN YOU SLIP:   Cut scope, hold the date. Write on the board what you CUT — never what you MOVED.
```

---

## 9. Sources, and what to re-verify at kickoff

### 9.1 Local files this document integrates

All in ``:

`research/SEASON-CADENCE.md` · `research/SEASON-CALENDAR.md` · `research/SMALL-TEAM-ECONOMICS.md` · `research/ELITE-TEAM-PRACTICES.md` · `research/DESIGN-AND-CAD.md` · `research/PROGRAMMING-PRACTICE.md` · `research/TESTING-AND-TUNING.md` · `research/SCOUTING-AND-AWARDS.md` · `research/AI-IN-FTC-POLICY.md` · `research/BIOBUZZ-PRESEASON.md` · `research/BIOBUZZ-V0-STRUCTURE.md` · `playbook/AI-FOR-PROGRAMMING.md` · `playbook/AI-FOR-DESIGN-AND-ANALYSIS.md` · `playbook/AI-TOOLKIT-SETUP.md` · `playbook/BUILD-AND-FABRICATION.md` · `reference/ANALYSIS-PROTOCOL.md` · `reference/CONSTRUCTION-RULES-R.md` · `reference/AWARD-CATALOG-BIOBUZZ.md` · `reference/TOURNAMENT-AND-RANKING.md` · `reference/ROBOT-ARCHETYPE-LIBRARY.md` · `reference/ARCHETYPE-BOMS.md`

Primary manual sources: `manuals/2026-27_BIOBUZZ/` (V0 Competition Manual and section extracts) · `manuals/archive/supplemental/2026-27_BIOBUZZ_ImportantSeasonDates.pdf` · `manuals/archive/supplemental/2025-26_DECODE_InspectionChecklist.pdf` · `manuals/archive/supplemental/2026-27_BIOBUZZ_RobotSign_USLetter.pdf` · `manuals/_reference_prior_seasons/`

### 9.2 Primary web sources (verified by the Phase A/B passes, 21–22 August 2026; kickoff date re-verified 22 August 2026)

| Source | URL |
|---|---|
| BIOBUZZ Game & Season (kickoff **Sat Sep 12, 12:00 p.m. ET**) | https://www.firstinspires.org/programs/ftc/game-and-season |
| Game Preview — Pollen, StarterBots, field elements | https://community.firstinspires.org/game-preview-field-elements |
| Skill Builders | https://community.firstinspires.org/introducing-first-tech-challenge-skill-builders |
| Key upcoming BIOBUZZ season dates | https://community.firstinspires.org/key-upcoming-biobuzz-season-dates |
| Cost and registration ($350; Control Hub $350 / Driver Kit $295 / Build Kit $660) | https://www.firstinspires.org/programs/cost-and-registration |
| Team grant opportunities | https://www.firstinspires.org/programs/team-grant-opportunities |
| Find local support (your PDP) | https://www.firstinspires.org/find-local-support |
| Mentor Manual (26 / 37 / 180 hours) | https://info.firstinspires.org/hubfs/web/program/ftc/ftc-mentor-manual.pdf |
| FTC Events (live event calendar) | https://ftc-events.firstinspires.org/2026 |
| Official FTC-Events API (token required) | https://ftc-api.firstinspires.org/ |
| ftcscout (no auth required) | https://ftcscout.org/ · https://api.ftcscout.org/graphql |
| Game Manual 0 — design strategy, team organization, collaboration | https://gm0.org/en/latest/ |
| FTC Open Alliance | https://www.theopenalliance.org/ftc |
| Hivemind portfolio archive | https://portfolios.hivemindrobotics.net/ |
| goBILDA StarterBot resource guide | https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/ |
| REV FTC StarterBot / kickoff concepts | https://www.revrobotics.com/duo/ftc-starter-bot/ · https://docs.revrobotics.com/ftc-kickoff-concepts |
| Studica StarterBot build guide | https://www.studica.com/blog/ftc-starter-bot-build-guide-2026-2027/ |
| Pedro Pathing · Road Runner · SolversLib · KookyBotz | https://pedropathing.com/ · https://github.com/acmerobotics/road-runner · https://github.com/FTC-23511/SolversLib · https://github.com/KookyBotz/CenterStage |
| Build threads: 12736 · 17012 · 23513 · 23619 | https://www.chiefdelphi.com/ (topics 506022, 506118, 506299, 508083) |
| Regional PDPs cited: WA · PA · IA · OR · SoCal · Benelux | firstwa.org · ftcpenn.org · engineering.uiowa.edu · ortop.org · socalftc.org · ftcbenelux.eu |

### 9.3 Re-verify these on kickoff morning, 12 September 2026

1. **R105 expansion limits** — V0 says literally *"Sizing Constraints and more details will be released at Kickoff."* Commit to no extension geometry before you read them.
2. **DRIVE TEAM composition** — BIOBUZZ §10 is a placeholder; this plan assumes the DECODE structure (up to 4, at most 1 non-student).
3. **The award list** — does BIOBUZZ retain **Reach** and **Sustain** or revert to **Motivate**? Check `reference/AWARD-CATALOG-BIOBUZZ.md` against the kickoff manual. It changes your award targets in [§4](#4-deliverables-parity--the-elite-version-the-lean-version-and-what-it-costs).
4. **The kickoff-week SDK version** — projected **v12.0**; the Tuesday merge block assumes it.
5. **Whether the 2027 Championship keeps six divisions** — it changes the number of judged award slots and therefore your advancement odds.
6. **Every price in [§7.3](#73-the-buy-list-and-the-one-supply-warning)** and in `research/SMALL-TEAM-ECONOMICS.md` — as of August 2026, and volatile.
7. **Library maintenance status** — re-check push dates for Road Runner, Pedro Pathing, SolversLib and EasyOpenCV before committing. FTCLib has been stale since Aug 2024; that kind of fact changes.

---

*Written 22 August 2026 for a 5–10 student, Tier A/B FTC team preparing for BIOBUZZ presented by RTX. Every price, deadline and regional detail in this document needs checking against your own PDP and your own dashboard before you act on it. The gate dates do not.*
