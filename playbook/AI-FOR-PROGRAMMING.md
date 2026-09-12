# AI FOR PROGRAMMING — Claude Code across the FTC software workstream

**Season:** 2026-27 BIOBUZZ, presented by RTX. Kickoff **12 Sep 2026**. **Written 22 Aug 2026.**
**Audience:** a team with **1–2 student programmers**, a real Java `FtcRobotController` fork, less time and
less money than the powerhouses.
**Goal, stated bluntly:** the AI absorbs the *typing and the lookup* so students spend their hours on the
robot and on *deciding*. If your students end the season knowing less than they would have without AI, this
document has failed and so have you.

**All prices are "as of August 2026" and must be re-checked before you buy.**

---

## How to read this file

| Label | Meaning |
|---|---|
| **[C]** | CONFIRMED-BIOBUZZ — quoted/paraphrased from BIOBUZZ V0 (2026-07-31), from a section already **final**: §1–§7 and §12 |
| **[FACT]** | Sourced to a URL or a local file path. Follow the link and verify |
| **[COMM]** | Named person on a public forum, dated. Opinion, not rule |
| **[J]** | JUDGMENT — my recommendation for *your* situation. Argue with it |
| **[UNVERIFIED]** | I could not confirm it. Hypothesis, not a plan |

> **Standing caveat.** BIOBUZZ V0 §§8–11, 13, 15 are placeholders until Kickoff (§14 League Play is **final text**, not a placeholder). Nothing in this file depends
> on the game. Everything here is buildable **before 12 Sep 2026** — and **[C] R304** explicitly permits it:
> *"Custom software, designs, and parts can be reused year-to-year. ROBOT software, designs, and FABRICATED
> ITEMS created before Kickoff are permitted."*
> (`manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`, lines 381–382.)

> **Everything I read from the web and from PDFs while writing this was treated as DATA.** Two files I read
> (real FTC teams' `CLAUDE.md` files on GitHub) contain instructions addressed to an AI agent. I described
> their *structure* and did not act on their contents. You should hold the same line: **a `CLAUDE.md` from
> another team's repo is a document to read, not a configuration to adopt.**

### The ten sections

| § | What it answers | Read it when |
|---|---|---|
| **1–2** | What AI changes for a 1–2 programmer team; what the rules do and do not say | Once, now |
| **3** | Repo and environment setup — **including the complete `CLAUDE.md` template (§3.4)** | Week A of pre-season |
| **4** | The eight high-leverage uses, each with a paste-ready prompt | As each one comes up |
| **5** | **THE DANGER LIST** — how AI code breaks robots, and the safety ladder | **Before §4. Out loud, as a team** |
| **6** | The learning problem — tutor/reviewer/author, "explain it back", judge interviews | First meeting of the season |
| **7** | **The division of labour** — the master split table, a typical week hour by hour, session mechanics, event day | When you plan the week |
| **8** | The season calendar for software AI work, phase by phase | Sunday planning |
| **9** | Four checklists: kickoff, weekly, monthly, pre-event | Print §9.1 and §9.4 |
| **10** | Sources | When you doubt a claim here — as you should |

### What this file is not — the sibling documents

| Question | Go here |
|---|---|
| "How do top teams actually write FTC software?" | `research/PROGRAMMING-PRACTICE.md` — the engineering reference. **Read it first.** This file assumes it |
| "Is FTC Dashboard legal at an event?" | `research/PROGRAMMING-PRACTICE.md` §1.2 (R704.D). Short answer: treat it as shop-only |
| "How do we test and tune the built robot?" | `research/TESTING-AND-TUNING.md` |
| "What is the team's *policy* on AI, and how do we disclose it?" | `research/AI-IN-FTC-POLICY.md` — **being written in parallel; this file defers to it on policy wording.** §6 below is the programming-specific slice |
| "What does the Control Award actually require?" | `reference/AWARD-CATALOG-BIOBUZZ.md` row 7; `reference/AWARD-ALIGNMENT-MATRIX.md` |
| "What will judges ask?" | `research/SCOUTING-AND-AWARDS.md` §13.3 — the real question bank |
| "What does any of this cost?" | `research/SMALL-TEAM-ECONOMICS.md` |
| "What week is it?" | `research/SEASON-CADENCE.md`, `research/SEASON-CALENDAR.md` |

---

## 0. Executive summary — the fifteen things that matter

| # | Claim | Consequence |
|---|---|---|
| 1 | **AI-written robot code that has never been run WILL eventually break the robot or the field.** This is not a hedge; it is the base case. A `setPosition()` past a hard stop strips a servo; an unclamped PID output slams a slide at full power into its end stop | §5 is the longest section in this file for a reason. Read it before §4 |
| 2 | The single highest-value artifact you will produce is a **150-line `CLAUDE.md`** at your repo root. It is worth more than any plugin, MCP server or marketplace skill | §3.4 is a complete, ready-to-paste template |
| 3 | **Real FTC teams already do this.** GitHub code search on 22 Aug 2026 returns FTC robot repos with a root `CLAUDE.md`, including **6165 MSET Cuttlefish** and **Mona Shores Robotics (19429/20245)** | §3.3. You are not pioneering; you are catching up |
| 4 | Mona Shores ships a **`.githooks/` pre-commit hook that blocks changes to Gradle/SDK versions** — a *physical* guard, not a polite request | §3.6. Copy the idea. Instructions are advisory; hooks are enforcement |
| 5 | **`permissions.deny` on `Edit(/FtcRobotController/**)`** costs you 30 seconds and removes the single most common way an agent bricks an FTC project | §3.5 |
| 6 | **Iteration speed is the whole game.** Sloth (`deploySloth`) hot-reloads TeamCode to the robot in **under a second** vs 40+ s for a normal install | §3.9. This is the difference between "AI suggests, we test" and "AI suggests, we guess" |
| 7 | **AI cannot tune your PID from a chat window.** It has never felt your slide's friction, your battery's sag, or your belt's stretch. Every gain it produces is a *starting guess to be measured* | §5.4. Non-negotiable |
| 8 | The correct role split is **AI as tutor and reviewer, student as author** for anything that will run on the robot; **AI as author** only for scaffolding, tests, tuning harnesses and documentation | §6.2 |
| 9 | The **"explain it back" rule**: no diff merges until a student can explain every line without the AI in the room. This is simultaneously your safety gate, your learning mechanism, and your judge-interview rehearsal | §6.3 |
| 10 | **[C]** The manual explicitly permits AI for portfolios and **requires a credit**: *"Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a footnote or endnote credit."* (§6, A201 discussion) | §6.5. There is no equivalent rule for *code*. **[C] R101** governs the robot; §6.5 explains what that means |
| 11 | The Control Award question bank already contains the question that exposes you: **"What pre-programmed libraries or outside resources did your team use?"** | `research/SCOUTING-AND-AWARDS.md` §13.3. Prepare an honest 20-second answer |
| 12 | **Community sentiment is a live risk.** A Chief Delphi thread on 13 May 2026 ("Student written code") ran 66 posts, opened by a poster observing that many teams brag their code is AI-written and asking which teams still used human programmers | §6.1. Being *seen* as an AI-code team is a reputational cost you can avoid by being straightforward first |
| 13 | The **highest-leverage AI use for a small team is not writing code — it is writing the *tuning harness*, the *tests*, and the *documentation***, because those are what small teams skip and what awards reward | §4.6, §4.7 |
| 14 | Keep a **`known-good` tag on `main` before every event.** `git tag qual-1-2026-11-14`. Your rollback must be one command, executable by a panicking 15-year-old | §5.6 |
| 15 | Two FTC-specific AI toolkits exist as of Aug 2026: **`ncssm-robotics/ftc-claude`** (MIT, plugin marketplace, ~4 stars) and **`Sanjit-K/ftc-toolchain`** (MIT, MCP server, ~0 stars). **[J] Evaluate; do not adopt blind.** Neither is load-bearing | §3.10 |

---

## 1. What AI actually changes for a 1–2 programmer team

### 1.1 The labor arithmetic

**[J]** A world-championship program has 4–8 programmers, a software mentor who is a professional engineer,
and 15 hours a week of shop access. You have 1–2 students and maybe 6 hours. The gap is not talent; it is
**throughput on non-creative work**. Here is where a small team's software hours actually go, and what AI can
and cannot take back:

| Task | Typical share of a small team's software hours **[J]** | Can AI absorb it? | What is left for the student |
|---|---|---|---|
| Boilerplate: `hardwareMap` wiring, OpMode skeletons, telemetry plumbing, enum scaffolds | 20–25% | **Yes, almost entirely** | Reading the diff; naming things |
| Looking things up: SDK method signatures, Road Runner/Pedro API shapes, Gradle syntax | 15–20% | **Yes** — and faster than a web search | Asking the right question |
| Debugging build failures and stack traces | 10–15% | **Mostly** | Reproducing the failure on the robot |
| Writing tests and tuning OpModes | 5% (usually 0% — small teams skip it) | **Yes** — this is the biggest *net gain* | Deciding what "correct" means |
| Writing documentation / portfolio content | 5–10% | **Yes, from the code and git log** | The engineering decisions being described |
| **Designing the mechanism's control strategy** | 10% | **No** | All of it |
| **Turning knobs and watching the robot** | 20–25% | **No — see §5.4** | All of it |
| **Driver-interface design and driver practice** | 5–10% | **No** | All of it |

**[J] The honest headline:** AI can plausibly return **40–55% of your software hours**. It returns *zero* of
the hours that decide whether you win, and it returns *negative* hours if you skip the review step and spend
the evening un-breaking a mechanism.

### 1.2 The three ways this goes wrong

**[J]** Every failure of AI-assisted FTC programming is one of three:

| Failure | What it looks like | Where it is addressed |
|---|---|---|
| **Broken hardware / broken field** | Slide drives itself into its end stop at full power. Servo strips because `0.0` was outside the mechanical range. Robot lurches off the tile during an auto test and takes out a field element | §5 (DANGER LIST) |
| **Hollow students** | The code works, nobody can explain it, and the Control Award interview turns into 12 minutes of "um." Next season the codebase is unmaintainable because nobody understands it | §6 (LEARNING) |
| **Silent quality rot** | It compiles, it runs, and it is 30% slower or 5% less reliable than it should be, because nobody read the loop-time telemetry. Small teams never find this because they never measure | §4.5 (footgun review), §4.6 (tuning) |

---

## 2. What the rules actually say (and don't say) about AI in code

**[C] There is no BIOBUZZ rule about AI-written software.** I read every AI reference in the V0 manual. There
are exactly two:

| Where | Verbatim | Reading |
|---|---|---|
| **§6 Awards, in the A201 PORTFOLIO discussion** (`06_Awards_A_p43-58.txt`, line 238) | *"Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a footnote or endnote credit. Example Credit: 'Portfolio created by Team XXXXX and ChatGPT'"* | **AI use in the portfolio is explicitly permitted and explicitly must be credited.** This is the only AI *requirement* in the manual |
| **§1.7.2 Translations & Other Versions** (`02_SeasonOverview_p5-21.txt`, line 598) | *"Additional resources such as a FIRST Tech Challenge AI Chatbot (coming soon) are provided as a helpful tool, but the Competition Manual is the final authority."* | FIRST is shipping its own AI. **Never quote a chatbot as a rule source** — the PDF is authoritative |

**[C] The rule that actually governs the robot is R101** (`12_RobotConstruction_R_p64-88.txt`, lines 142–166):

> *"It is your team's ROBOT. The ROBOT and its MAJOR MECHANISMS must be built by the FIRST Tech Challenge
> team that has registered for the event…"*

and its stated intent:

> *"The intent of this rule is that a team's ROBOT is a product that's representative of the current team
> members' experience and is intended to discourage complete solutions which are provided wholly by outside
> organizations or companies."*

R101's own blue box lists *"writing software"* among the forms of **assistance from other teams that the rule
is explicitly not intended to prohibit**.

**[J] What this means, stated plainly.**
1. Nothing in the rules prohibits AI-assisted code. Do not let anyone tell you otherwise, and do not tell
   anyone else otherwise.
2. **R101's *intent* clause is the standard you should hold yourself to.** If your software is not
   *"representative of the current team members' experience"* — if no student can explain it — you have
   satisfied the letter and failed the point, and the judges will find out in the interview (§6.4).
3. The portfolio rule tells you the disclosure norm FIRST is comfortable with: **use it, credit it.** **[J]**
   Extend the same norm to code voluntarily. It costs one sentence and buys you the entire "did AI write
   this?" conversation on your own terms.
4. **[UNVERIFIED]** No Team Update or Q&A entry on AI-written code exists for BIOBUZZ as of 22 Aug 2026 — the
   The Game Q&A opens **Mon 28 Sep 2026, 12:00 p.m. ET** — 16 days after Kickoff, not at Kickoff (`research/SEASON-CALENDAR.md`). Put "check Q&A for AI/code-authorship guidance" on your kickoff checklist (§9).

---

## 3. Repo and environment setup for AI-assisted work

### 3.1 Why a stock `FtcRobotController` fork is hostile to an AI agent

**[FACT]** The upstream repo ([FIRST-Tech-Challenge/FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController))
has this top level: `TeamCode/`, `FtcRobotController/`, `libs/`, `doc/`, `gradle/wrapper/`, `build.gradle`,
`build.common.gradle`, `build.dependencies.gradle`, `settings.gradle`, `gradle.properties`, `gradlew`,
`gradlew.bat`, `.github/`, `LICENSE`, `.gitignore`. The README directs teams to modify **`TeamCode/`** and
points at the samples in `FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples`
as material to copy. Requirements: **Android Studio Ladybug (2024.2) or later**, **minSdkVersion 24**.
**[FACT]** The current SDK release as of 21 Aug 2026 is **v11.2.1 (2026-07-31)**; **v12.0 for BIOBUZZ has not
shipped** (verified in `research/PROGRAMMING-PRACTICE.md` §2.3 — expect it ~5–8 Sep 2026).

**[J] Five properties of that layout actively hurt an agent:**

| Problem | Why it hurts | Fix |
|---|---|---|
| **~200 sample OpModes** live in `FtcRobotController/.../samples/`, all annotated `@Disabled` | Grep for `DcMotorEx` returns dozens of sample files. The agent reads samples and copies sample idioms (blocking `sleep()` chains, magic numbers) into your code | Tell it in `CLAUDE.md`: samples are *reference only*, never edit, never imitate their structure |
| **The `FtcRobotController/` module looks editable** | An agent "fixing" a compile error edits the SDK module. Your build then differs from every other team's and no online answer applies | `permissions.deny` on `Edit(/FtcRobotController/**)` (§3.5) **and** a pre-commit hook (§3.6) |
| **Hardware names are strings** typed into the Robot Controller config app, invisible to the repo | The agent invents `"frontLeft"` when your config says `"lf"`. Compiles fine; `NullPointerException` on init | A **hardware map table in `CLAUDE.md`** (§3.4) plus a `HardwareNames.java` constants file |
| **No test source set by default** | The agent has no way to verify anything without a robot | Add `TeamCode/src/test/java/` + JUnit 5 (see `research/PROGRAMMING-PRACTICE.md` §7.8) |
| **Gradle version pinning is fragile** | An agent "helpfully" bumps AGP or the Gradle wrapper and the SDK stops building | Deny-list those files; hook-block the commit |

### 3.2 The target layout

**[J]** Start from the structure in `research/PROGRAMMING-PRACTICE.md` §7.1 (modelled on **FTC #23511 Seattle
Solvers**, [FTC-23511/Decode-2026](https://github.com/FTC-23511/Decode-2026)) and add the agent-facing files:

```
<repo root>/
├── CLAUDE.md                     # <- §3.4. The single most valuable file here
├── .claude/
│   ├── settings.json             # <- §3.5, committed
│   ├── settings.local.json       # personal, gitignored
│   ├── hooks/
│   │   └── protect-sdk.sh        # <- §3.6
│   ├── skills/
│   │   ├── new-subsystem/SKILL.md    # <- §3.7
│   │   ├── footgun-review/SKILL.md
│   │   ├── explain/SKILL.md
│   │   └── control-award/SKILL.md
│   └── agents/
│       └── log-triage.md         # <- §3.8
├── .githooks/pre-commit          # <- §3.6, belt and braces
├── docs/
│   ├── HARDWARE.md               # wiring + config names, the human copy
│   ├── TUNING-LOG.md             # every tuning session, dated
│   └── CONTROL-AWARD.md          # generated from code, §4.7
├── logs/                         # pulled robotControllerLog.txt + datalogs, gitignored
├── TeamCode/src/main/java/org/firstinspires/ftc/teamcode/
│   ├── config/Constants.java     # EVERY tunable number, one file
│   ├── config/HardwareNames.java # EVERY hardwareMap string, one file
│   ├── subsystems/               # Drive, Intake, Lift, ...
│   ├── opmodes/auto/  opmodes/teleop/
│   ├── tuning/                   # one OpMode per mechanism, kept all season
│   └── util/MathFunctions.java   # pure math, no SDK imports -> unit-testable
├── TeamCode/src/test/java/       # JUnit 5
└── FtcRobotController/  libs/  gradle/  gradlew  ...   # DO NOT TOUCH
```

**[J] The three files that do most of the work** are `CLAUDE.md`, `config/Constants.java` and
`config/HardwareNames.java`. Together they mean the agent never has to *guess* a number or a string — the two
things it guesses worst and that cost you the most.

### 3.3 What belongs in a `CLAUDE.md` — and the evidence

**[FACT] How `CLAUDE.md` works.** Claude Code loads `./CLAUDE.md` (or `./.claude/CLAUDE.md`) at the start of
every session, concatenated with any `CLAUDE.md` in parent directories and a gitignored `CLAUDE.local.md`.
The docs give three hard pieces of guidance: **target under 200 lines**, be **specific enough to verify**
("Use 2-space indentation", not "format code properly"), and avoid **contradictions** — if two rules conflict
Claude may pick either. It is *context, not enforcement*: to block an action regardless of what the model
decides, the docs direct you to a PreToolUse hook instead.
([code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory))

**[FACT] Real FTC teams' `CLAUDE.md` files, read 22 Aug 2026.** A GitHub code search for `CLAUDE.md` in
repos containing `FtcRobotController` returns 11 hits, including these robot repos:
`6165-MSET-Cuttlefish/summer-2026`, `Mona-Shores-FTC-Robotics/DECODE`, `Limelight-Robotics/ftc-2026`,
`FTC-24180/BB-Lib`, `STMARobotics/ftc-fusion-decode`, `Cyber-Salam-FTC/TeleOp-Auto`, `dr-hextanium/jimmy`.
**[UNVERIFIED]** the competitive results or code quality of most of these. Two are worth studying:

| Repo | What its `CLAUDE.md` records | The transferable idea |
|---|---|---|
| **[6165-MSET-Cuttlefish/summer-2026](https://github.com/6165-MSET-Cuttlefish/summer-2026/blob/main/CLAUDE.md)** | Sections: *Project context · Keep this file fresh · Build & deploy · Module/Gradle structure · Framework layout · OpMode lifecycle · Module pattern · Action system · Path-action scheduler · Tuning · Testing · Conventions · Repo conventions discovered from prior conversations*. Records SDK **11.1.0**, **Java 17**, `./gradlew :TeamCode:assembleDebug`, `deploySloth` hot-reload, Control Hub `arm64-v8a` only. Conventions include: comments explain *why* not *what*; no commented-out code or section banners; fail fast rather than swallowing exceptions; tunables live in `@Config` nested classes, never ad-hoc statics | **"Keep this file fresh"** and **"Repo conventions discovered from prior conversations"** — the file is treated as a *living record of corrections*, which is exactly what the Claude Code docs recommend: add to it when Claude makes the same mistake twice |
| **[Mona-Shores-FTC-Robotics/DECODE](https://github.com/Mona-Shores-FTC-Robotics/DECODE/blob/master/CLAUDE.md)** | Two robots (19429, 20245) off one codebase via `RobotProfile.java`; gradle + `deploySloth` commands with the caveat that hot-reload only covers `org.firstinspires.ftc.teamcode`; subsystem list (Drive, Vision, Launcher, Intake, Lighting); pinned library versions (Pedro Pathing 2.0.4, Pedro Ivy 1.0.0, FTC Dashboard 0.5.1, AdvantageScope Lite 26.0.0, goBILDA Pinpoint); three telemetry verbosity levels (MATCH / PRACTICE / VERBOSE); **pre-commit hooks that block SDK changes**; troubleshooting playbooks for vision, odometry and performance | **Pin every library version in the file**, and back the "don't touch the SDK" rule with a **hook**, not a sentence. The repo also carries a `codex/` directory of task-runner scripts and prompt templates — the same idea as `.claude/skills/` |

**[J] The eight things a good FTC `CLAUDE.md` must contain**, in order of how much pain each one saves:

1. **Hardware map table** — every config string, device type, hub, port, direction. Stops invented names.
2. **"Never modify these files"** — with the reason. Stops SDK edits and Gradle bumps.
3. **Pinned versions** — SDK, Java, path library, dashboard, vendor drivers. Stops API hallucination against
   the wrong version.
4. **Units, stated once, everywhere** — inches vs mm, degrees vs radians, ticks vs inches. Stops the single
   most expensive class of bug (§4.5).
5. **Build/deploy commands, verbatim** — so the agent runs the right Gradle task instead of inventing one.
6. **Subsystem contract** — `periodic()` once per loop, `atTarget()`, no `sleep()`, no gamepad reads.
7. **Safety rules addressed to the agent** — soft limits, clamped outputs, never widen a servo range.
8. **"When you are unsure, ask"** — an explicit instruction to stop and ask rather than guess a number.

---

### 3.4 THE TEMPLATE — a complete, ready-to-use `CLAUDE.md` for an FTC robot repo

**[J]** Copy the block below to `<repo root>/CLAUDE.md`. Replace every `<…>` placeholder. Delete sections you
genuinely do not have — an inaccurate `CLAUDE.md` is worse than a short one. Keep it under ~200 lines as you
fill it in. Re-read it at every event and after every mechanism rebuild.

~~~markdown
# FTC Team <NNNNN> — BIOBUZZ 2026-27 Robot Code

## What this project is
Android Studio / Gradle fork of FIRST-Tech-Challenge/FtcRobotController.
Runs on a REV Control Hub (REV-31-1595). All team code lives in `TeamCode/`.
Competition code must work with **no laptop connected** — see "Competition mode" below.

## Pinned versions — never change these unless a human asks you to
- FTC SDK: <11.2.1>            (declared in `build.dependencies.gradle`)
- Java 17 (Temurin) · Android Studio Ladybug 2024.2+ · minSdk 24 · ABI arm64-v8a
- Path library: <Pedro Pathing vX.Y.Z | Road Runner 1.0.x>
- Dashboard: <FTC Dashboard 0.4.x | FTControl Panels vX.Y.Z>   (SHOP ONLY — see Competition mode)
- Odometry: <goBILDA Pinpoint V2 (3110-0002-0002) driver vX | SparkFun OTOS | drive encoders>
- Vision: <Limelight 3A firmware vX | SDK VisionPortal AprilTagProcessor | none>
If you need an API that does not exist in these versions, STOP and say so. Do not upgrade anything.

## Build, deploy, logs — use exactly these commands
- Compile only (fast, no robot):  `./gradlew :TeamCode:compileDebugJavaWithJavac`
- Unit tests (no robot):          `./gradlew :TeamCode:test`
- Full build:                     `./gradlew :TeamCode:assembleDebug`
- Install to robot:               `./gradlew installDebug`      <- ASK A HUMAN FIRST
- Hot reload TeamCode only:       `./gradlew deploySloth`        <- ASK A HUMAN FIRST
- Connect over robot Wi-Fi:       `adb connect 192.168.43.1:5555`
- Pull the RC log:                `adb pull /sdcard/robotControllerLog.txt logs/`
You may run compile and test freely. You may NOT install, deploy or restart the robot unless asked.

## NEVER modify these files or directories
- `FtcRobotController/**` — the SDK module. Read the samples for reference; never edit them and never
  imitate their blocking `sleep()` style. If a compile error looks like it is "in the SDK", the bug is in
  TeamCode.
- `libs/**`, `gradle/**`, `gradlew`, `gradlew.bat`, `settings.gradle`, `build.gradle`,
  `build.common.gradle`, `build.dependencies.gradle`, `gradle.properties`
- `.githooks/**`, `.claude/settings.json`
A pre-commit hook and a permissions deny-rule both enforce this. If you hit either, that is the system
working — report it, do not work around it.

## Hardware map — the ONLY source of truth for device names
Names must match the Robot Controller configuration file exactly (case-sensitive). Constants live in
`TeamCode/.../config/HardwareNames.java`. Never type a device-name string anywhere else.

| Constant | Config name | Type | Hub | Port | Direction | Notes |
|---|---|---|---|---|---|---|
| `LF` | `<lf>` | DcMotorEx | Control | 0 | REVERSE | goBILDA 5203-2402-0019, 537.7 ticks/rev |
| `LB` | `<lb>` | DcMotorEx | Control | 1 | REVERSE | same |
| `RF` | `<rf>` | DcMotorEx | Control | 2 | FORWARD | same |
| `RB` | `<rb>` | DcMotorEx | Control | 3 | FORWARD | same |
| `LIFT` | `<lift>` | DcMotorEx | Expansion | 0 | FORWARD | encoder zero = fully retracted |
| `CLAW` | `<claw>` | Servo | Control | 0 | — | SAFE RANGE 0.30–0.65 |
| `IMU` | `<imu>` | IMU (BHI260AP) | Control | I2C 0 | — | logo <UP>, USB <FORWARD> |
| `PINPOINT` | `<pinpoint>` | I2C | Control | I2C 1 | — | pods: X <+dir>, Y <+dir> |
<add every device you have; delete rows you do not>

## Units — one convention, no exceptions
- Distance: **inches**. Angles: **degrees** at every API boundary; radians only inside a single math method.
- Motor position: **encoder ticks**; convert at the subsystem edge with a named constant, never inline.
- Time: **seconds** (`ElapsedTime.seconds()`), never milliseconds.
- Field frame: <describe your origin and +X / +Y / heading convention, or write "TBD until kickoff">
Any variable holding a converted value carries its unit in its name: `liftHeightIn`, `armAngleDeg`,
`targetTicks`. Reject any change where a bare number crosses a unit boundary.

## Where things go
- `config/Constants.java`     — EVERY tunable number. No numeric literal outside this file except 0 and 1.
- `config/HardwareNames.java` — EVERY hardwareMap string.
- `subsystems/`               — one class per mechanism. Owns its hardware. Exposes intent, not implementation.
- `opmodes/auto/`, `opmodes/teleop/` — name autos after what they score, not after a code word.
- `tuning/`                   — one OpMode per mechanism, kept all season. Instrumentation, not throwaway code.
- `util/MathFunctions.java`   — pure static math, NO SDK imports, so it is unit-testable.
- `TeamCode/src/test/java/`   — JUnit 5. Any pure function you write should get a test.

## Subsystem contract — every subsystem obeys all six
1. Constructor takes `HardwareMap`; it does all `hardwareMap.get()` calls and nothing else expensive.
2. Exactly one `periodic()`, called once per loop from the OpMode.
3. Public methods express **intent** (`setState(State.SCORE)`), never raw power.
4. Exposes `atTarget()` so state machines and autos can sequence on it.
5. Never reads the gamepad. Never calls `telemetry.update()`. Never calls `sleep()` or `Thread.sleep()`.
6. Never blocks. If a behaviour takes time it is a state machine, not a wait.

## Safety rules you must follow when writing robot code
- Every closed-loop output is clamped: `Range.clip(out, -MAX, MAX)` with MAX from `Constants`.
- Every position setpoint is clamped to a soft limit from `Constants` before it reaches hardware.
- Servos: `setPosition()` arguments must lie inside the SAFE RANGE in the hardware table above. Never widen a
  servo range and never call `scaleRange()` to make a target "fit". If a target is outside the range, STOP.
- Every `while` loop in a `LinearOpMode` has `opModeIsActive()` or `!isStopRequested()` in its condition.
- New mechanism motors get `motor.setCurrentAlert(<A>, CurrentUnit.AMPS)`, and the subsystem checks
  `isMotorOverCurrent()` and cuts power. Control Hub motor ports are 10 A continuous / 20 A peak.
- Voltage-compensate anything tuned: scale output by `12.0 / batteryVoltage`.
- Bulk reads on for both hubs: `setBulkCachingMode(BulkCachingMode.AUTO)`.
- Loop time is always on driver-station telemetry. If a change could slow the loop, say so.

## Numbers you may NOT invent
PID/PIDF gains, feedforward constants, servo positions, encoder-to-inch ratios, arm angles, timing
constants, camera offsets, field coordinates. If a number is needed and is not in `Constants.java`, write a
clearly-marked placeholder (`= 0.0; // TODO MEASURE`) and tell the human what to measure and how. Never copy
a gain from another team's repo, from a tutorial, or from your own estimate.

## Competition mode
`Constants.COMPETITION_MODE` gates every dashboard/telemetry-streaming code path. Rule R704.D names FTC
Dashboard and FTControl Panels as prohibited on the Robot Controller Wi-Fi network, and no laptop may be on
that network during a match. Debugging at events is by on-robot file logging, pulled over USB afterwards.
Never add a code path that requires a laptop connection in order to work.

## Git
- `main` is always what is on the robot right now.
- One short-lived branch per feature: `feat/lift-pid`, `fix/claw-range`.
- Commit message: `<subsystem>: what changed` — e.g. `lift: raise kG to 0.0009 after new spool`.
- Tuning-value changes get their own commits, separate from logic changes.
- You may `git add` and `git commit`. You may NOT `git push`, `git reset --hard`, `git clean`, or rebase.

## How to work with us
- We are students learning to program. **Explain what you did and why, in plain language, every time.**
- Prefer the smallest change that works. Do not refactor code you were not asked to touch.
- If a request is ambiguous — especially about hardware, geometry, or a number — ASK. Do not guess.
- When you finish a change, say in one sentence what could physically go wrong on the robot if it is wrong.
- Never call a change "tested" unless a test actually ran. Compiling is not testing.

## Keep this file fresh
If you are corrected twice on the same thing, propose an edit to this file. If a mechanism is rebuilt, the
hardware table and safe ranges above are stale until a human updates them — say so rather than trusting them.
~~~

**[J] Two things to notice about that template.** First, roughly half of it is *prohibitions*. That is correct
for robotics: the cost of an agent doing something clever is far higher than the cost of it doing nothing.
Second, the "Numbers you may NOT invent" section is the single highest-value paragraph in the file — see §5.4
and §5.5.

---

### 3.5 `.claude/settings.json` — permissions that make it safe *and* fast

**[FACT] How permissions work.** Settings files live at `.claude/settings.json` (shared, commit it),
`.claude/settings.local.json` (personal, gitignore it) and `~/.claude/settings.json` (user). Rules are
`Tool` or `Tool(specifier)`. Bash rules glob: `Bash(git commit *)` matches any command starting
`git commit `, and `Bash(ls *)` enforces a word boundary so it matches `ls -la` but not `lsof`. Claude Code
is shell-aware, so `Bash(safe-cmd *)` does **not** authorise `safe-cmd && rm -rf .` — each subcommand must
match a rule independently. `Read`/`Edit` rules use gitignore-style paths: a leading `/` anchors at the
settings source (so `Edit(/FtcRobotController/**)` in project settings means `<project root>/FtcRobotController/**`),
`//` means filesystem root, and a bare filename matches at any depth. `Edit` rules cover all built-in
file-editing tools; a path rule written for `Write` is accepted but never consulted, so always write
`Edit(...)`. `permissions.defaultMode` sets the starting mode: `default` (prompt on first use — labelled
Manual), `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`.
([permissions](https://code.claude.com/docs/en/permissions), [settings](https://code.claude.com/docs/en/settings))

⚠️ **[FACT]** Deny and ask rules apply immediately; **`allow` rules and `additionalDirectories` only take
effect after each person trusts the folder.** So the safety rules bite from the first second — good.

**[J] Commit this as `.claude/settings.json`:**

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "defaultMode": "default",
    "allow": [
      "Bash(./gradlew :TeamCode:compileDebugJavaWithJavac)",
      "Bash(./gradlew :TeamCode:test)",
      "Bash(./gradlew :TeamCode:assembleDebug)",
      "Bash(git status *)",
      "Bash(git diff *)",
      "Bash(git log *)",
      "Bash(git show *)",
      "Bash(git add *)",
      "Bash(git commit *)",
      "Bash(git branch *)",
      "Bash(git checkout -b *)",
      "Bash(adb devices)",
      "Bash(adb logcat -d *)",
      "Bash(adb pull *)",
      "WebFetch(domain:gm0.org)",
      "WebFetch(domain:ftc-docs.firstinspires.org)",
      "WebFetch(domain:pedropathing.com)",
      "WebFetch(domain:rr.brott.dev)",
      "WebFetch(domain:javadoc.io)"
    ],
    "ask": [
      "Bash(./gradlew installDebug)",
      "Bash(./gradlew deploySloth)",
      "Bash(adb install *)",
      "Bash(adb shell *)",
      "Bash(adb connect *)",
      "Bash(git push *)",
      "Bash(git merge *)"
    ],
    "deny": [
      "Edit(/FtcRobotController/**)",
      "Edit(/libs/**)",
      "Edit(/gradle/**)",
      "Edit(/gradlew)",
      "Edit(/gradlew.bat)",
      "Edit(/settings.gradle)",
      "Edit(/build.gradle)",
      "Edit(/build.common.gradle)",
      "Edit(/build.dependencies.gradle)",
      "Edit(/gradle.properties)",
      "Edit(/.githooks/**)",
      "Edit(/.claude/settings.json)",
      "Bash(git push --force *)",
      "Bash(git push -f *)",
      "Bash(git reset --hard *)",
      "Bash(git clean *)",
      "Bash(git rebase *)",
      "Bash(rm -rf *)"
    ]
  }
}
```

**[J] Why each block is shaped this way:**

| Block | Rationale |
|---|---|
| `allow` compile + test | These are the *feedback loop*. If the agent needs permission to compile, it stops compiling, and un-compiled code is the thing you are trying to avoid |
| `allow` read-only git + `add`/`commit` | Commits are cheap and reversible; they give you the bisectable tuning journal `research/PROGRAMMING-PRACTICE.md` §7.2 asks for |
| `ask` on anything that touches the robot | `installDebug`, `deploySloth`, `adb install/shell` all change what the physical machine does. A human must be looking at the robot when this happens (§5.3) |
| `ask` on `push`/`merge` | Publishing and integrating are human decisions |
| `deny` on SDK/Gradle paths | The single highest-value line in the file. `Edit(/FtcRobotController/**)` alone eliminates the most common way an agent bricks an FTC project |
| `deny` on history-destroying git | `reset --hard`, `clean`, `rebase`, force-push. On a robotics team the working tree *is* the backup |
| `WebFetch` allow-list | Lets the agent read GM0 and the official docs without prompting, and keeps it from wandering |

**[J] Do not set `defaultMode` to `bypassPermissions` or `auto` on a robot repo.** The whole point of the
ask-list is that a human is looking at the robot at the moment code reaches it.

**Also add to `.gitignore`:** `.claude/settings.local.json`, `CLAUDE.local.md`, `logs/`.

### 3.6 The hook that physically blocks SDK edits

**[FACT]** Claude Code hooks are configured in settings JSON under `hooks.<EventName>`, each entry with a
`matcher` and a list of hook commands. A `PreToolUse` hook blocks the tool call either by exiting with code
**2**, or by printing JSON with `hookSpecificOutput.permissionDecision: "deny"`. Hooks can carry an `if`
condition using permission-rule syntax, and `${CLAUDE_PROJECT_DIR}` resolves to the repo root.
([hooks](https://code.claude.com/docs/en/hooks))

**[J]** The deny rules in §3.5 already stop the agent's file tools. The hook exists to stop everything else —
a shell one-liner, a `sed`, a script. Belt and braces, because the cost of a broken build the night before a
qualifier is a whole event.

`.claude/settings.json` (merge into the file above):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/protect-sdk.sh" }
        ]
      }
    ]
  }
}
```

`.claude/hooks/protect-sdk.sh` (`chmod +x` it):

```bash
#!/bin/bash
# Block any Bash command that writes to the SDK module or the Gradle build files.
CMD=$(jq -r '.tool_input.command // empty')
if printf '%s' "$CMD" | grep -Eq '(FtcRobotController/|build\.dependencies\.gradle|build\.common\.gradle|settings\.gradle|gradle-wrapper|gradlew)'; then
  if printf '%s' "$CMD" | grep -Eq '(^|[|;&[:space:]])(rm|mv|cp|sed -i|tee|truncate|chmod)([[:space:]]|$)|>'; then
    jq -n '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",
      permissionDecisionReason:"Protected SDK/Gradle path. Team policy: only humans change the SDK module or build files."}}'
    exit 0
  fi
fi
exit 0
```

**[FACT] The idea is proven in the wild:** `Mona-Shores-FTC-Robotics/DECODE` ships a `.githooks/` directory
whose pre-commit hook blocks accidental Gradle/SDK version modifications. **[J]** Add the git-side guard too,
because it catches humans as well as agents:

`.githooks/pre-commit` (then `git config core.hooksPath .githooks`):

```bash
#!/bin/bash
BLOCKED=$(git diff --cached --name-only | grep -E '^(FtcRobotController/|libs/|gradle/|gradlew|settings\.gradle|build.*\.gradle|gradle\.properties)')
if [ -n "$BLOCKED" ]; then
  echo "BLOCKED: this commit touches SDK/build files:"; echo "$BLOCKED"
  echo "If this is deliberate, re-run with: git commit --no-verify"
  exit 1
fi
```

### 3.7 Skills — the four worth writing, complete

**[FACT]** A skill is a `SKILL.md` in `.claude/skills/<name>/`. Frontmatter is all optional but
`description` is what tells Claude when to load it; `disable-model-invocation: true` makes it manual-only
(`/name`); `allowed-tools` pre-approves tools for the turn that invokes it; `` !`cmd` `` runs a shell command
and inlines the output *before* Claude sees the content; `$ARGUMENTS`, `$0`, `$1` are argument placeholders;
`${CLAUDE_PROJECT_DIR}` resolves to the repo root. Files in `.claude/commands/*.md` behave the same way.
Skills load **on demand**, so long reference material in one costs no context until used.
([skills](https://code.claude.com/docs/en/skills))

**[J] Write these four. They are the ones you will run 50+ times a season.**

**(a) `.claude/skills/footgun-review/SKILL.md`** — the highest-value skill in the repo (see §4.5):

~~~markdown
---
description: Review the current diff for FTC-specific bugs that break robots. Use before any code is deployed to the robot, and whenever the user asks for a code review, a pre-deploy check, or "is this safe to run".
allowed-tools: Bash(git diff *) Bash(git status *) Read Grep Glob
---

## The diff under review
!`git diff HEAD`

## Your job
Review ONLY the diff above against the checklist below. For each finding give: file:line, the rule broken,
what physically happens on the robot if it ships, and the minimal fix. Rank by physical risk, worst first.
If the diff is clean, say so in one line — do not invent findings.

### Checklist — FTC footguns
1. Blocking: `sleep()`, `Thread.sleep()`, or a `while` that waits on a condition, anywhere outside an
   explicitly-approved init sequence.
2. Any `while` in a `LinearOpMode` whose condition lacks `opModeIsActive()` or `!isStopRequested()`.
3. Any `hardwareMap.get()` outside a constructor/init, or any device-name string literal not read from
   `HardwareNames`.
4. PID / feedforward output that is not `Range.clip`ed before reaching a motor.
5. Position setpoint that is not clamped to a soft limit from `Constants` before reaching hardware.
6. `Servo.setPosition()` with an argument outside the SAFE RANGE in CLAUDE.md, or any `scaleRange()` /
   `setPwmRange()` call. Flag `setPosition(0)` and `setPosition(1)` as suspicious by default.
7. Units: any arithmetic mixing ticks with inches, degrees with radians, or ms with s. Any bare numeric
   literal outside `Constants.java`.
8. Any new `hardwareMap` device, camera open, or I2C read inside the loop rather than init (loop-time risk).
9. `RUN_TO_POSITION` set before `setTargetPosition` (throws `TargetPositionNotSetException`).
10. Angle arithmetic without wrapping to a stated range.
11. Missing `atTarget()` / state-machine exit condition, so a state can never advance.
12. Division that can divide by zero (loop dt, battery voltage, tick ratios).
13. Motor direction or encoder sign assumed rather than read from CLAUDE.md's hardware table.
14. Anything that only works with a laptop connected (dashboard-only code paths) not gated behind
    `Constants.COMPETITION_MODE`.
15. Exception swallowed with an empty catch.
~~~

**(b) `.claude/skills/new-subsystem/SKILL.md`** — see the worked example in §4.1:

~~~markdown
---
description: Scaffold a new FTC subsystem class plus its tuning OpMode and constants block from a plain-English hardware description. Use when the user says they have built a new mechanism and need code for it.
argument-hint: [subsystem name] [one-line hardware description]
disable-model-invocation: true
---

## Repo conventions
@CLAUDE.md

## Existing subsystems (match this style exactly)
!`ls TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/`

## Task
Create a subsystem named $0 for this mechanism: $ARGUMENTS

Produce, and nothing else:
1. `subsystems/$0.java` following the six-point subsystem contract in CLAUDE.md.
2. A `Constants` block with every number the subsystem needs, each one `= 0.0; // TODO MEASURE: <how>`.
   Do not invent a single value.
3. `tuning/$0Tuner.java`: a `@TeleOp` OpMode in the `tuning` group that moves the mechanism under direct
   operator control in the smallest safe increments, prints the live encoder/position and current draw, and
   has a hard stop on a face button. This is what the students will use to fill in the constants.
4. A short list, in plain English, of what the student must measure and in what order.

Before writing anything, restate the mechanism back to me in three sentences and list the hardware names you
intend to use from CLAUDE.md's table. If a name is missing from that table, STOP and ask.
~~~

**(c) `.claude/skills/explain/SKILL.md`** — the tutor mode (see §4.3 and §6.3):

~~~markdown
---
description: Explain an FTC/SDK/Road Runner/Pedro API or a piece of our code to a student, without writing code. Use whenever the user asks what something does, how an API works, or why code behaves a certain way.
argument-hint: [class, method, or file:line]
disable-model-invocation: true
---

Explain $ARGUMENTS to a high-school student who knows basic Java but is new to FTC.

Rules for this answer:
- **Do not write or modify any code.** If the student needs code, tell them what to write, not the text.
- Start with one sentence on what problem this thing exists to solve.
- Then the mechanism: what it actually does, in order.
- Then the FTC-specific gotcha: what goes wrong when people use it naively on a robot.
- Then the units and the valid range of every argument and return value.
- Cite the version-appropriate source (the SDK javadoc, GM0, the library's own docs) and say which version
  you are describing. If our pinned version in CLAUDE.md might behave differently, say so.
- End with exactly two questions the student should be able to answer before using it. Do not answer them.
~~~

**(d) `.claude/skills/control-award/SKILL.md`** — see §4.7:

~~~markdown
---
description: Draft or refresh the Control Award portfolio material from the actual code, git log and tuning notes. Use when preparing portfolio or judging material about the control system.
allowed-tools: Bash(git log *) Read Grep Glob
---

## Recent history
!`git log --oneline -n 60`
## Tuning journal
!`git log -p --follow -n 30 -- TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/Constants.java`

## Task
Read the subsystems, the tuning OpModes, `docs/TUNING-LOG.md` and the history above, then draft
`docs/CONTROL-AWARD.md` with these sections, and ONLY from evidence in the repo:

1. **Sensor and control component inventory** — a table: component, what it senses/controls, which game
   challenge it solves, which file implements it.
2. **External-feedback loops** — for each closed loop: the sensor, the controller type, the actuator, and
   the measured before/after behaviour. Cite the commit or log file that shows the measurement.
3. **Autonomous** — how the robot knows where it is; how it decides what to do; what it does when a sensor
   disagrees.
4. **Driver assistance in TeleOp** — each macro or aid, and what it saves the driver.
5. **Reliability** — how we measured it, over how many attempts, with the numbers.
6. **What we learned / what we would improve** — from the actual history of failed approaches.

Rules: every claim must trace to a file, a commit or a log. Where evidence is missing, write
`EVIDENCE NEEDED: <what to measure>` instead of prose. Do not include code listings — the portfolio does not
need the code itself. Write at a level a non-programmer judge can follow.
~~~

**[J] Do not write more than four or five skills.** A skill you invoke twice a season is a maintenance
liability. The four above map to the four things you do constantly: review, scaffold, learn, document.

### 3.8 One subagent worth having

**[FACT]** Subagents are markdown files in `.claude/agents/` with `name` and `description` required, plus
optional `tools`, `model`, `memory`, `permissionMode`. They run in an **isolated context window** and return
a summary, which is exactly what you want for work that produces a wall of output.
([sub-agents](https://code.claude.com/docs/en/sub-agents))

**[J]** A `robotControllerLog.txt` from one practice session is tens of thousands of lines. Reading it into
your main conversation destroys the context you were using to think. Put it in a subagent.

`.claude/agents/log-triage.md`:

~~~markdown
---
name: log-triage
description: Triage a pulled Control Hub log or datalog CSV and report only what matters. Use when the user has a robotControllerLog.txt, a logcat dump, or a datalog from a practice session.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You triage FTC Robot Controller logs. Read the file(s) named by the caller. Return ONLY:

1. Every exception, with its first stack frame inside `org.firstinspires.ftc.teamcode` and the timestamp.
2. Every "stuck in start/loop/stop" event, with the OpMode name and how long it ran first.
3. Every Lynx/hub communication error, I2C failure, or device-not-found, with the device name.
4. Battery voltage: starting, minimum, and the timestamp of the minimum.
5. Loop-time statistics if present: median, 95th percentile, worst, and when the worst occurred.
6. A timeline of at most 10 lines: what happened, in order.
7. One ranked list of hypotheses, each with the specific evidence line number that supports it.

Do not paste raw log lines except single lines cited as evidence. Do not propose code changes.
~~~

### 3.9 The deploy loop — this is the whole game

**[J]** AI-assisted programming multiplies the number of candidate changes you produce. If each candidate
costs 60 seconds to test, you have made things *worse*: you now have a queue of untested guesses. Every
minute you cut from the edit→robot loop is a minute of real feedback.

| Method | Speed | Notes |
|---|---|---|
| `./gradlew :TeamCode:compileDebugJavaWithJavac` | ~5–15 s | **[J]** The agent should run this after every edit. It catches ~40% of AI mistakes for free |
| `./gradlew :TeamCode:test` (JUnit 5) | ~5–20 s | **[FACT]** FTC #23511 does exactly this in GitHub Actions CI (`research/PROGRAMMING-PRACTICE.md` §7.8). Catches the math errors compilation cannot |
| USB-C install | ~40–60 s | Default. Keep a 10 ft USB-C cable in the pit |
| ADB over Wi-Fi (`adb connect 192.168.43.1:5555`) | ~40–60 s, no cable | **[FACT]** Control Hub RC address is `192.168.43.1` ([ftc-docs, Managing a Control Hub](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.html)). ⚠️ R704.C: laptop off the RC network during match play |
| **Sloth hot reload (`./gradlew deploySloth`)** | **< 1 s** | **[FACT]** [Dairy-Foundation/Sloth](https://github.com/Dairy-Foundation/Sloth) v0.2.4, BSD-3-Clause-Clear, ~46 stars as of Aug 2026. Gradle plugin `dev.frozenmilk.sinister.sloth.load` + `dev.frozenmilk.sinister:Sloth`, from `https://repo.dairy.foundation/releases`. Adds `deploySloth` and `removeSlothRemote`. **Only reloads classes in `org.firstinspires.ftc.teamcode`**; library changes, non-teamcode edits and `@Pinned` changes need a full install |

**[J] Recommendation:** install Sloth in pre-season week 1 and verify it before you rely on it. Real FTC teams
are already depending on it — both `6165-MSET-Cuttlefish/summer-2026` and `Mona-Shores-FTC-Robotics/DECODE`
document `deploySloth` as their normal deploy command. **[UNVERIFIED]** Sloth's compatibility with SDK v12.0,
which has not shipped. Put "re-verify Sloth against v12.0" on the kickoff checklist (§9). Have the plain
`installDebug` path working as a fallback, always.

⚠️ **[J] Sloth's failure mode is nasty and you must teach it:** code that compiles and hot-loads can behave
differently from the same code fully installed, because hot reload does not re-initialise everything.
**Before every event, do one full `installDebug` and re-run your checklist.** Never let an event build be a
hot-reload build.

### 3.10 FTC-specific AI tooling: what exists, what to actually install

| Thing | What it is | Status as of 22 Aug 2026 | **[J] Verdict** |
|---|---|---|---|
| **[ncssm-robotics/ftc-claude](https://github.com/ncssm-robotics/ftc-claude)** | Claude Code plugin marketplace of FTC skills: `pedro-pathing`, `roadrunner`, `ftclib`, `nextftc`, `pinpoint`, `limelight`, `panels`, `ftc-dashboard`, `robot-dev`, `decode`. Install: `/plugin marketplace add ncssm-robotics/ftc-claude` then `/plugin install <name>@ncssm-robotics/ftc-claude`. MIT, ~4 stars, active | Skills for the library you actually use. Follows the open Agent Skills standard | **Try the one plugin matching your path library, and `robot-dev`. Nothing else.** A skill for a library you do not use is context you pay for and never spend. No BIOBUZZ game plugin exists yet ([UNVERIFIED] whether one will appear) |
| **[Sanjit-K/ftc-toolchain](https://github.com/Sanjit-K/ftc-toolchain)** | MCP server exposing FTC operations as tools: `list_samples`, `search_docs`, `create_opmode`, `create_subsystem`, `hardware_manifest`, `validate_hardware`, `build`, `deploy`, `build_and_deploy`, `wifi_deploy_start`, `adb_connect`, `robot_logs`, `restart_robot_controller`, and more. MIT, needs Node 18+, adb, JDK 17 | **~0 stars, ~22 commits.** Effectively unproven | **[J] Skip for now.** It duplicates what `Bash` + your own skills already do, and it can *deploy to the robot* — that is exactly the capability you least want behind an unfamiliar abstraction. Revisit if it gains traction |
| **The `/init` command** | Generates a starting `CLAUDE.md` by analysing the codebase | Built in | **[J] Run it once, then throw away 60% of its output** and replace it with §3.4. `/init` describes the code; the value is in the things the code cannot tell it — hardware names, units, safe ranges, prohibitions |
| **Auto memory** | Claude Code writes its own notes per repository into `~/.claude/projects/<project>/memory/`, on by default | Built in | **[J] Leave it on, and read `/memory` once a month.** It captures the corrections you gave and did not write down. Do **not** let it become the only place a safety rule lives — those belong in `CLAUDE.md`, which is committed and reviewable |
| **FIRST Tech Challenge AI Chatbot** | **[C]** Announced in the V0 manual, §1.7.2: *"coming soon"* | Not available as of 22 Aug 2026 | **[J]** When it ships, use it for *"where is this in the manual"* only. The manual says explicitly that the PDF is the final authority. Never quote a chatbot to a referee |

---

## 4. The eight high-leverage uses

Each subsection gives a **worked prompt you can paste**, the **expected workflow**, and the **split** between
agent and student. The prompts assume the `CLAUDE.md` from §3.4 is in place — that is what makes them short.

> **[J] A note on prompt style that matters more than any individual prompt.** The three moves that
> consistently improve output on an FTC codebase are: (1) **give it the physical facts** (motor, gear ratio,
> travel, hard stops) rather than asking it to infer them; (2) **make it restate the problem before it writes
> code**; (3) **ask for placeholders, not values**, for anything measurable. Every prompt below does all three.

---

### 4.1 Scaffolding subsystems and OpModes from a hardware description

**When:** a mechanism just got built and there is no code for it. This is the highest-frequency AI task of the
season and the safest, because the output is structure, not behaviour.

**The prompt** (or `/new-subsystem Lift "..."`):

```
We just built a vertical lift. Physical facts:
- One goBILDA 5203-2402-0019 (19.2:1, 312 RPM, 537.7 ticks/rev at the output shaft), config name "lift",
  Expansion Hub port 0.
- Spool diameter is 1.5 in nominal, but I have NOT measured the actual inches-per-tick yet.
- Travel is about 26 in from hard-stopped bottom to hard-stopped top. Encoder zero = fully retracted.
- Gravity pulls it down; it will not hold position at zero power.
- There is a magnetic limit switch at the bottom, config name "liftBottom", digital port 0.
- Three useful heights: stowed, low, high. I have not measured any of them.

Write:
1. subsystems/Lift.java following the subsystem contract in CLAUDE.md.
2. The Constants block, every number as a TODO MEASURE placeholder with a comment saying how to measure it.
3. tuning/LiftTuner.java so I can find those numbers on the robot.

Before you write anything: restate the mechanism in three sentences, list the hardware names you will use,
and tell me the three most likely ways this code damages the lift.
```

**Expected workflow:**

| # | Who | Step |
|---|---|---|
| 1 | Agent | Restates the mechanism; lists `HardwareNames.LIFT`, `HardwareNames.LIFT_BOTTOM`; names the damage modes (driving into the top hard stop under P-control, no soft limit; holding full power at a stall; zeroing the encoder at the wrong end) |
| 2 | **Student** | **Confirms or corrects the restatement.** If the agent got the mechanism wrong, stop here — everything downstream is wrong |
| 3 | Agent | Writes the three files. Every gain and height is `0.0; // TODO MEASURE` |
| 4 | Agent | Runs `./gradlew :TeamCode:compileDebugJavaWithJavac` |
| 5 | **Student** | Reads the whole diff aloud. Runs `/footgun-review` (§3.7a) |
| 6 | **Student** | Robot on blocks, mechanism free to move. Runs `LiftTuner`, fills in constants by measuring (§4.6) |
| 7 | **Student** | Commits constants in their own commit: `lift: measured inPerTick=0.0187, heights` |

**[J] What the agent must NOT produce here:** a PID gain, a height in ticks, an inches-per-tick ratio, or a
`sleep()`-based "raise then open" sequence. If it does, that is a `CLAUDE.md` bug — add the correction.

**[J] The bonus you get for free:** a `tuning/` OpMode per mechanism is exactly what
`research/PROGRAMMING-PRACTICE.md` §7.1 identifies as one of the five things to steal from a Worlds-level
repo, and it is the thing small teams never build because it feels like a detour. The AI makes it a
30-second detour.

---

### 4.2 Translating a mechanism spec into a state machine

**When:** a sequence takes time and currently exists as `sleep()` calls, or in a student's head.

**[J] The rule: the student draws the state machine on a whiteboard first.** The AI translates a design; it
does not do the design. This is the difference between a student who can answer "walk us through your
scoring sequence" and one who cannot.

**The prompt:**

```
Here is the scoring sequence I designed on the whiteboard. Translate it to a state machine in
subsystems/ScoringSequence.java, non-blocking, one step per periodic() call.

States and transitions:
  IDLE      -> RAISING   when the driver presses the trigger AND lift.isHomed()
  RAISING   -> RELEASING when lift.atTarget()
  RELEASING -> LOWERING  when 300 ms have elapsed since the claw opened
  LOWERING  -> IDLE      when lift.atTarget()
  ANY       -> ABORTING  when the driver presses B
  ABORTING  -> IDLE      when lift.atTarget() at stowed

Constraints:
- The drivetrain must keep responding to the driver in every state.
- The driver can cancel at any point (that is what ABORTING is for).
- No sleep(), no Thread.sleep(), no busy-wait.
- 300 ms is a placeholder; mark it TODO MEASURE.
- Every state must have a way out. Tell me if any state in my design can deadlock.
- Do not touch Lift.java or Claw.java.

Before writing: draw my state machine back to me as a table of (state, exit condition, next state) and tell
me which transitions I have not specified.
```

**Expected workflow:** agent tabulates → **student confirms the table matches the whiteboard** → agent writes
the class → compile → `/footgun-review` → bench test with the mechanism unloaded → field test.

**[FACT]** This is the pattern GM0 documents under *Finite State Machines*
([gm0.org](https://gm0.org/en/latest/docs/software/concepts/finite-state-machines.html)), and GM0's
*Common Issues* page names the underlying failure directly: in a `LinearOpMode`, loops must include
`opModeIsActive()` or `!isStopRequested()` or the OpMode gets stuck in start/loop/stop
([gm0.org](https://gm0.org/en/latest/docs/software/getting-started/common-issues.html)).

**[J] The judge-interview payoff.** "Walk us through the process your team used" (Innovate) and "What
enhancements did your team program to assist the drivers?" (Control) are both in the real question bank
(linked from `research/SCOUTING-AND-AWARDS.md` §13.3). A student who designed the state table can answer both from
memory. A student who prompted for a scoring sequence cannot.

---

### 4.3 Explaining unfamiliar SDK / Road Runner / Pedro / FTCLib APIs

**When:** constantly. **[J] This is the single best use of AI for a small team**, because the alternative is
20 minutes of searching forum posts written against a three-year-old SDK version.

**The prompt** (or `/explain DcMotorEx.setVelocity`):

```
Explain DcMotorEx.setVelocity() to me. I know Java but I am new to FTC.
Do not write code. Tell me:
- what problem it exists to solve, and what it does differently from setPower()
- what units the argument is in, and how that relates to my motor's 537.7 ticks/rev
- which PIDF coefficients it actually uses, and whether they survive a power cycle
- the FTC-specific gotcha that bites people
- which SDK version you are describing, and whether our pinned 11.2.1 differs
Then give me two questions I should be able to answer before I use it. Do not answer them.
```

**Expected workflow:** agent explains → **student writes the answer to the two questions in their own words in
`docs/` or the notebook** → student writes the code themselves.

⚠️ **[J] The version trap.** FTC's API surface has changed materially across SDK versions, and the model's
training data is full of code from every one of them. Three defences:
1. **Pin the version in `CLAUDE.md`** (§3.4) so the model is told which one you are on.
2. **Ask it to cite the doc**, and allow-list the doc domains in `settings.json` (§3.5) so fetching is free.
3. **Compile before you believe it.** A hallucinated method fails in 10 seconds.

⚠️ **[FACT] A specific, expensive trap the model will get wrong unless told.** "PIDF" means two different
things in FTC — the SDK's `F` is a *velocity feedforward*, while the `F` in most community `PIDFController`
code is a *gravity constant* — and **PIDF coefficients do not persist across a power cycle**. This is
documented in `research/PROGRAMMING-PRACTICE.md` §6.1b and on
[ftc-docs, Changing PIDF Coefficients](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/pidf_coefficients/pidf-coefficients.html).
**[J] Put a one-line note about it in your `CLAUDE.md` if you use `DcMotorEx` velocity control.**

---

### 4.4 Debugging from logs, telemetry dumps and stack traces

**When:** the robot did something wrong and you have a log, not a theory.

**[FACT] Where the evidence lives.** The Robot Controller log is `robotControllerLog.txt`, downloadable from
the Control Hub's Manage page or over adb; `adb connect 192.168.43.1:5555` gets you on wirelessly
([ftc-docs](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.html)).
The SDK also ships a four-part **Datalogging** tutorial that writes CSV to the RC
([FtcRobotController wiki](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Datalogging)).
**[J]** Under R704.D, **file logging is the debugging strategy that is unambiguously safe at events** — see
`research/PROGRAMMING-PRACTICE.md` §7.7.

**The prompt** (after `adb pull /sdcard/robotControllerLog.txt logs/`):

```
Use the log-triage agent on logs/robotControllerLog.txt.

Context: during our third practice auto, the robot drove the first leg correctly, then stopped moving but the
OpMode kept running for another 8 seconds before I hit stop. Battery was around 12.4 V at start. This is the
first run after we merged feat/lift-pid.

After triage, give me a ranked list of hypotheses. For each: the evidence line, and the ONE cheapest
experiment that would confirm or kill it. Do not change any code yet.
```

**Expected workflow:**

| # | Who | Step |
|---|---|---|
| 1 | Agent | Subagent triages the log in an isolated context; returns exceptions, stuck-in-loop events, hub errors, voltage minimum, loop-time stats, a 10-line timeline |
| 2 | Agent | Ranks hypotheses with evidence and proposes one cheap experiment each |
| 3 | **Student** | **Runs the experiment on the robot.** This is the step that cannot be delegated |
| 4 | Agent | Given the experiment result, proposes the minimal fix |
| 5 | **Student** | Reads it, understands it, applies the safety ladder in §5.3 |

**[FACT] The four exceptions GM0's *Common Issues* page says you will actually see**, and what each means:

| Exception | Cause per GM0 | **[J] What the agent should look for in your code** |
|---|---|---|
| `NullPointerException` | Using a variable that is null; `hardwareMap` is null before `init()` runs | A `hardwareMap.get()` at field-declaration time instead of in init; or a config-name typo |
| `TargetPositionNotSetException` | `RunMode` changed to `RUN_TO_POSITION` before a target was set | Order of `setTargetPosition` / `setMode` |
| `ArithmeticException` | Illegal arithmetic such as divide-by-zero | Loop dt, battery voltage, tick ratios |
| `InterruptedException` | Normal when the SDK asks the OpMode to stop | A `Thread.sleep()` that should not be there at all |
| "Stuck in start/loop/stop" | An OpMode method exceeded its time limit; loops need `opModeIsActive()` / `!isStopRequested()` | Blocking loops — the #1 FTC footgun |

⚠️ **[J] The debugging anti-pattern to ban outright:** pasting a stack trace and saying "fix it." The model
will produce *a* change that makes *that* symptom go away, often by widening a range, catching and swallowing
an exception, or removing a check. **Always ask for a diagnosis before a patch**, and always ask "what would
prove this?" A fix you cannot explain is a fix you cannot defend at 8 am at a qualifier.

---

### 4.5 Reviewing student code for the FTC-specific footguns

**When:** before *every* deploy. `/footgun-review` (§3.7a). **[J] This is the use with the best
risk-adjusted return in this whole document** — it costs 20 seconds and it is the only review a
one-programmer team will ever get.

**The full footgun catalogue** — this is the checklist the skill encodes, with the physical consequence
stated, because that is what makes students take it seriously:

| # | Footgun | How it looks | What physically happens | Source |
|---|---|---|---|---|
| 1 | **Blocking loop / busy-wait** | `while (Math.abs(err) > 5) { ... }`, `sleep(1200)` | Drivetrain stops responding mid-sequence; driver cannot cancel; OpMode can hang past the buzzer | **[FACT]** GM0 *Common Issues*, *LinearOpMode vs OpMode* |
| 2 | **Missing `opModeIsActive()` / `!isStopRequested()`** | Any `while` in a `LinearOpMode` | "Stuck in start/loop/stop"; the app must be restarted; you lose a match | **[FACT]** GM0 *Common Issues* |
| 3 | **Unclamped controller output** | `motor.setPower(kP * error)` | With a big error, full power instantly. Slide slams its end stop; arm whips; belt skips; 9.2 A stall current on a 5203 against a 10 A continuous port | **[FACT]** goBILDA 5203-2402-0019 stall current 9.2 A @12 V; **[FACT]** REV Control Hub motor port 10 A continuous / 20 A peak ([REV docs](https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics)) |
| 4 | **No soft limits** | Setpoint straight from a button press to the motor | Mechanism drives into a hard stop and holds there at full power until something breaks or the port thermally protects | **[FACT]** REV: "outputs will self protect once they approach their thermal limit" — i.e. your robot stops mid-match |
| 5 | **Servo range error** | `setPosition(0.0)` / `setPosition(1.0)`; a `scaleRange()` added to make a value "fit" | Servo drives past the mechanism's hard stop, strips its gears or bends linkage. Silent, permanent, and it happens in one second | **[FACT]** `Servo.setPosition` takes 0–1; `scaleRange(min,max)` remaps that range ([SDK javadoc](https://javadoc.io/static/org.firstinspires.ftc/RobotCore/7.1.0/com/qualcomm/robotcore/hardware/ServoImplEx.html)) |
| 6 | **Hardware-map typo** | `hardwareMap.get(DcMotor.class, "frontleft")` vs config `"frontLeft"` | Compiles, deploys, then `NullPointerException` on init. At an event this is a red card for your nerves | **[FACT]** GM0 *Common Issues* |
| 7 | **Units confusion** | Ticks added to inches; degrees passed to a radian API; ms compared to s | Robot travels 25× too far, or a turn overshoots by 57×. This is the most expensive single bug class in FTC | **[J]** — hence the units section in `CLAUDE.md` |
| 8 | **Magic numbers in subsystems** | `if (pos > 1400)` inside `Lift.java` | The mechanism gets rebuilt Thursday night and there are now seven places to change. One gets missed | **[FACT]** #23511's layout puts every number in `globals/Constants.java` |
| 9 | **`RUN_TO_POSITION` before `setTargetPosition`** | Mode set first | `TargetPositionNotSetException` | **[FACT]** GM0 *Common Issues* |
| 10 | **Hardware calls in the hot loop** | `hardwareMap.get(...)`, camera open, or an un-cached I2C read inside `loop()` | Loop time jumps from 8 ms to 60 ms; every control loop degrades at once, and it looks like a tuning problem | **[FACT]** GM0 *Bulk Reads*; SDK `ConceptMotorBulkRead` |
| 11 | **Unwrapped angle arithmetic** | `error = target - heading` across ±180° | Robot spins the long way round, or oscillates at the wrap point | **[J]** |
| 12 | **State with no exit** | A state whose transition condition can never become true | Robot freezes mid-sequence with the OpMode still running | **[J]** |
| 13 | **Swallowed exception** | `catch (Exception e) {}` | The robot silently does nothing and the log is empty. You lose an entire debugging session | **[FACT]** 6165's own `CLAUDE.md` conventions call for fail-fast, not swallowing |
| 14 | **Dashboard-only code path** | Behaviour that only works with FTC Dashboard connected | Works in the shop, dead at the event; and R704.D names Dashboard/Panels as prohibited on the RC network | **[C]** R704.D; `research/PROGRAMMING-PRACTICE.md` §1.2 |
| 15 | **No voltage compensation** | Gains tuned on a fresh battery | Auto works in practice at 13.2 V and fails in match 4 at 11.8 V | **[J]** |

**[J] Run the review on the *diff*, not the *file*.** A whole-file review returns generic advice; a diff
review returns things that are actually about to ship. That is why the skill in §3.7a injects `git diff HEAD`.

---

### 4.6 Generating tuning scaffolding and interpreting tuning data

**[J] This is where AI helps most and is trusted least, and both are correct.** Split it in two:

| Half | Who | Why |
|---|---|---|
| **Building the harness** — a tuning OpMode, a CSV logger, a plotting script, a JUnit test of the math | **Agent, freely** | It is code with no gains in it. Nothing it produces can be wrong about your robot because it asserts nothing about your robot |
| **Producing the gains** | **Student, on the robot, always** | See §5.4 |
| **Interpreting the data the student collected** | **Agent, as an analyst** | The model is genuinely good at "here are 300 rows of setpoint vs measured, what is wrong with this response" — because now it has evidence |

**Prompt A — build the harness:**

```
Write tuning/LiftPidTuner.java. Requirements:
- @TeleOp, group "tuning". Not @Disabled.
- @Config so the gains are live-editable from the dashboard (shop only, gate on Constants.COMPETITION_MODE).
- Left stick Y jogs the lift manually at a power capped by Constants.LIFT_JOG_MAX.
- A button commands a step from the current position to current + Constants.LIFT_STEP_TICKS.
- Every loop, write one CSV row to the RC: timestamp_s, setpoint_ticks, measured_ticks, error_ticks,
  output, current_amps, battery_v, loop_ms. Use the SDK Datalogger pattern.
- Telemetry shows: measured, setpoint, error, output, current, loop time — in that order, big enough to read
  from 6 feet away.
- A face button is a hard stop: zero power, clear the setpoint.
- Soft limits from Constants enforced even in jog mode.
- Every gain starts at 0.0 with a TODO MEASURE comment. Do not put a number in.
```

**Prompt B — interpret the data (the student has now run it):**

```
Attached is logs/lift-step-2026-10-14.csv from a step response on the lift: setpoint jumped 900 ticks at
t=2.15 s. Gains at the time: kP=0.004, kI=0, kD=0, kG=0.06. Battery 12.6 V falling to 12.1 V.

Tell me, from the data only:
- rise time, overshoot %, settling time to +/-15 ticks, steady-state error
- whether this response is dominated by too little P, too much P, missing D, or missing gravity feedforward
- which ONE gain to change next, in which direction, and roughly how much
- what to look for in the next run to confirm the change worked
Do not tell me the final gains. Do not change any code.
```

**[FACT] For drivetrain tuning, do not invent a procedure — Road Runner 1.0 ships one** with named OpModes in
a fixed order: direction debugger → `ForwardPushTest` (`inPerTick`) → `LateralPushTest` (`lateralInPerTick`)
→ `ForwardRampLogger` / `LateralRampLogger` / `AngularRampLogger` (`kS`, `kV`, `trackWidthTicks`) →
`ManualFeedforwardTuner` (add `kA`) → `ManualFeedbackTuner` → `SplineTest`
([rr.brott.dev tuning](https://rr.brott.dev/docs/v1-0/tuning/)). Pedro Pathing has its own equivalent.
**[J] Use the AI to explain what each step is measuring and to sanity-check your numbers — never to replace
a step.** See `research/PROGRAMMING-PRACTICE.md` §5.2 and §6.2–6.5 for the per-mechanism procedures, and
`research/TESTING-AND-TUNING.md` §4 for how to know what you are actually bad at.

**[J] The meta-rule, restated because it is the one that makes tuning survive the season:** every tuning
session ends with a git commit whose diff is the changed constants, plus two lines in `docs/TUNING-LOG.md`
saying what you changed and what you observed. The AI can write those two lines from the diff. That log is
Control Award evidence, for free (§4.7).

---

### 4.7 Writing code documentation and Control Award material *from the actual code*

**[C] What the Control Award actually requires** (`reference/AWARD-CATALOG-BIOBUZZ.md` row 7):
**R1** a PORTFOLIO containing **all of** (A) the hardware or software control COMPONENTS on the robot, (B) the
challenges each solves, (C) the function of each; **R2** one or more solutions that use **external feedback**
to control the robot and improve performance; **E3** works consistently during most matches; **E4** the team
can explain reliability; **E5** describe what they learned using the engineering process. Notably: *"The
PORTFOLIO does not need to include the full code itself."*

**[J] This is the perfect AI task and small teams systematically underuse it**, because writing documentation
feels like the thing you do if you have spare time, and you never have spare time. You now do.

**The prompt** (or `/control-award`):

```
/control-award

Additional context for this pass: our two closed loops are the lift position loop (motor encoder feedback)
and the heading hold on the drivetrain (Pinpoint IMU feedback). Our reliability numbers are in
docs/TUNING-LOG.md under "2026-11-02 reliability run". Draft docs/CONTROL-AWARD.md.

Then give me a separate list: every claim in the draft that is NOT supported by something in this repo, so I
know exactly what we still have to measure before the qualifier.
```

**Expected workflow:**

| # | Who | Step |
|---|---|---|
| 1 | Agent | Reads subsystems, tuning OpModes, `TUNING-LOG.md`, and `git log -p` on `Constants.java`; drafts `docs/CONTROL-AWARD.md`; marks every unsupported claim `EVIDENCE NEEDED` |
| 2 | **Student** | Goes and gets the missing evidence. **This is the real output of the exercise** — the draft's gaps are your test plan |
| 3 | **Student** | Rewrites the draft in their own voice. A portfolio in model-English reads like a portfolio in model-English |
| 4 | **Student** | Adds the AI credit required by the manual for portfolio content (§6.5) |

**[J] Three things this earns you beyond the award:**
1. **The `EVIDENCE NEEDED` list is a reliability test plan** you would not otherwise have written.
2. **It forces the tuning log to exist**, which makes next season's team functional.
3. **It is interview rehearsal.** "How did your team measure reliability?" appears in *both* the Innovate and
   Control question banks (`research/SCOUTING-AND-AWARDS.md` §13.3). If you wrote §5 of that document, you
   have already answered it.

⚠️ **[J] Do not let the AI write the *engineering decisions*.** It can describe what the code does; it cannot
know why you chose a PID over bang-bang, or why you abandoned the first intake. Those sentences are the ones
judges probe, and they must come from the students.

---

### 4.8 Converting a scoring analysis into an autonomous route plan

**When:** kickoff week, then after every strategy change. **[J] The AI is a *constraint checker and options
generator* here, not a strategist.** It has never watched your robot cycle.

**The prompt** (post-kickoff; the numbers below are placeholders because BIOBUZZ §§8–11 are not public):

```
Here is our scoring analysis for the auto period (from reference/SCORING-PATTERNS.md and our own measurements):
- Auto is <N> seconds.
- Scoring option A: <points> points, our measured cycle time <t> s, our measured success rate <p>%.
- Scoring option B: <points> points, cycle <t> s, success <p>%.
- Parking in <zone> is worth <points> and takes <t> s from <where>.
- Our robot's measured top translation speed is <v> in/s and it needs <t> s to settle before scoring.
- Preload capacity: <n>. Field pickup: <possible/not>.

Produce three candidate auto routes: a conservative one, an expected-value-maximising one, and an aggressive
one. For each: the sequence of actions, the expected points, the expected points multiplied by our measured
success rates, and the single failure that costs the most.

Then tell me which assumptions in my input the answer is most sensitive to — i.e. which number I should go
measure again before we commit a week of build time to one of these.

Do NOT write any path code. Do NOT invent any timing, distance or success-rate number I did not give you.
```

**Expected workflow:** agent produces the three routes and the sensitivity list → **student picks one and can
say why** → student sketches the path in MeepMeep / the Pedro visualiser → student writes the trajectory →
`/footgun-review` → simulator (virtual_robot) → robot on blocks → half-speed on the field → full speed.

**[J] The sensitivity question is the whole value of this prompt.** A small team's fatal error is committing
three weeks to an auto whose value rests on a success rate nobody measured. Making the model name the
load-bearing assumption converts an opinion into a measurement task.

⚠️ **[UNVERIFIED]** Everything about BIOBUZZ scoring until 12 Sep 2026. Build the *structure* now — the
randomisation vote-and-latch pattern, a `FieldTags` abstraction, an auto that is a state machine over
objectives — and fill in the game later. See `research/PROGRAMMING-PRACTICE.md` §5.4.

---

## 5. THE DANGER LIST

### 5.0 Read this paragraph out loud at your first meeting

**AI-written robot code that has never been run WILL break the robot or the field.** Not "might." The model
has never seen your robot. It does not know that your lift's third stage binds at 22 inches, that your claw
servo stalls at 0.28, that your battery sags to 11.6 V on the fourth match, or that the field tile in front
of your goal is warped. It writes code that is *plausible*. Plausible code driven into an aluminium hard stop
at 9.2 amps strips a gearbox in under a second, and it costs $54.99 and an evening you did not have.

**The rule that follows from that:** *code is not real until it has run, and it does not get to run until a
human who understands it is standing next to the robot with a finger on stop.*

Nothing in this section is optional, and none of it is about trusting the AI more or less. It is about the
fact that **software failures in robotics are physical failures**, and physical failures cost money, field
time, and matches.

### 5.1 The ten ways AI-generated code actually breaks things

| # | Failure | The mechanism | Realistic cost | The guard |
|---|---|---|---|---|
| 1 | **Unclamped output into a hard stop** | Proportional control with a large initial error commands full power. The mechanism arrives at its end stop at speed and keeps pushing | Stripped gearbox ($55 motor / $30 gearbox), bent slide, broken belt, lost evening | `Range.clip` on every output + soft limits + current alert (§5.3) |
| 2 | **Servo commanded past its mechanical range** | `setPosition(0.0)` when the mechanism's safe minimum is 0.30 | Stripped servo gears in ~1 second. Silent. Often not discovered until the mechanism misbehaves at an event | SAFE RANGE table in `CLAUDE.md`; `/footgun-review` item 6; **always jog a new servo by hand first** |
| 3 | **Runaway auto on a real field** | Wrong sign on a heading, wrong `inPerTick`, or an unwrapped angle. Robot accelerates toward a wall or a field element | Broken robot, broken field element, and you are the team that broke the field | Simulator → blocks → half speed → full speed (§5.2). **Never run a new auto at full speed on a real field first** |
| 4 | **Blocking loop hangs the OpMode** | A `while` without `opModeIsActive()`. The app must be restarted | One match, and a very public 30 seconds | `/footgun-review` items 1–2; GM0 *Common Issues* |
| 5 | **Encoder zeroed at the wrong end** | Init routine assumes a home position the robot is not in | Mechanism immediately drives toward a "target" that is on the far side of a hard stop | Limit-switch homing, and a check that the encoder moved in the expected direction before enabling closed loop |
| 6 | **Motor direction flipped** | The agent guessed `REVERSE`. Positive feedback instead of negative | Mechanism accelerates away from its target at full power until something stops it | Direction is in the `CLAUDE.md` hardware table, measured once; a jog test before any closed loop is enabled |
| 7 | **Units error scaled by 25.4 or 57.3** | mm treated as inches, radians as degrees | Robot travels 25× too far. Same physical outcome as #3 | Units section in `CLAUDE.md`; unit in every variable name; a JUnit test on the conversion |
| 8 | **Silent thermal shutdown mid-match** | Sustained stall above 10 A continuous. The Control Hub port self-protects | Robot goes dead in a match, and the log looks like nothing happened | Current alerts + a subsystem that cuts power and tells you (§5.3) |
| 9 | **"Works on my bench" hot-reload artifact** | Sloth reloaded a class but not the state around it. Behaviour differs from a clean install | An event build that behaves differently from everything you tested | One full `installDebug` + re-run the checklist before every event (§3.9) |
| 10 | **A "fix" that removes a check** | Asked to make an exception go away, the model widens a range, catches-and-ignores, or deletes a guard | You have converted a loud failure into a silent one. This is the worst outcome in the table | Always ask for a **diagnosis before a patch** (§4.4); `/footgun-review` items 5 and 13 |

### 5.2 The safety ladder — seven rungs, no skipping

**[J]** Every change that will run on the robot climbs this ladder. A change may skip *upward* only when the
rung below has passed. Print this and tape it to the laptop.

| Rung | Gate | Who | Typical time | What it catches |
|---|---|---|---|---|
| **0** | **A student read every line and can explain it** — §6.3 | Student | 2–10 min | Everything the model misunderstood about your robot. **The single most effective rung** |
| **1** | **Compiles** — `./gradlew :TeamCode:compileDebugJavaWithJavac` | Agent | 5–15 s | Hallucinated APIs, wrong SDK version, typos |
| **2** | **Unit tests pass** — `./gradlew :TeamCode:test` | Agent | 5–20 s | Math, conversions, decision logic, angle wrapping |
| **3** | **`/footgun-review` on the diff is clean** — §4.5 | Agent + student | 30 s | The 15 FTC footguns |
| **4** | **Simulator, for anything that moves the robot in space** — [virtual_robot](https://github.com/Beta8397/virtual_robot) for autos/paths, [EOCV-Sim](https://github.com/deltacv/EOCV-Sim) for vision, MeepMeep / Pedro visualiser for path geometry | Student | 2–10 min | Paths into walls, wrong signs, impossible geometry — **before** the robot moves |
| **5** | **Bench test: robot on blocks, wheels off the ground, mechanism free to travel, hand on stop** | Student | 2–5 min | Direction errors, range errors, runaway loops — at zero risk to the field |
| **6** | **Field test at reduced authority** — first run with power/velocity caps at ~40–50%, then full | Student | 5 min | Everything that only shows up under real friction, real load and real battery sag |

**[J] Rung 4 is the one small teams skip and should not.** `research/PROGRAMMING-PRACTICE.md` §7.8 lays out
the simulation tiers and their setup cost — all $0. A path that ends inside a wall in `virtual_robot` costs
you nothing; the same path on a real field costs you a field element and the goodwill of whoever owns it.

**[J] The bench-test rig is a $0 purchase you must make in week 1.** Two blocks of 2×4 under the frame so the
wheels spin free. Every "the robot took off across the shop" story starts with someone skipping this.

### 5.3 Current limits, soft limits, and the three guards every mechanism needs

**[FACT] The hardware numbers that set the budget:**

| Item | Number | Source |
|---|---|---|
| Control Hub motor ports | **4**, **10 A continuous**, **20 A absolute peak** per port; outputs *"self protect once they approach their thermal limit"* | [REV Control Hub specs](https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics) |
| Control Hub servo ports | **6**, sharing power in pairs (0-1, 2-3, 4-5), **2 A max per pair**, **5 A total** | same |
| goBILDA 5203-2402-0019 | 19.2:1, 312 RPM, **537.7 PPR at the output shaft**, stall torque 24.3 kg·cm, **stall current 9.2 A @ 12 V**, **$54.99** (Aug 2026) | [goBILDA product page](https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-19-2-1-ratio-24mm-length-8mm-rex-shaft-312-rpm-3-3-5v-encoder/) |
| **[C]** Servo class limit | 8 W mechanical output @ 6 V; linear servos 1 A @ 6 V (Table 12-2, R502/R503) | `12_RobotConstruction_R_p64-88.txt` |

**[J] Read line 3 against line 1.** One stalled 5203 draws 9.2 A into a port rated 10 A continuous. **A single
stalled motor is already at the port's continuous limit.** Two mechanisms stalling together, or one stalling
while the drivetrain works, is how a robot dies mid-match with a clean-looking log.

**[FACT]** `DcMotorEx` exposes `setCurrentAlert()`, `getCurrentAlert()`, `isMotorOverCurrent()` and a current
read. GM0's *SDK Motors* page notes an important performance detail: **the raw current read is not bulk-read,
but `isMotorOverCurrent()` is** — so checking the alert in your loop is cheap and reading the amperage is not
([gm0.org SDK Motors](https://gm0.org/en/latest/docs/software/adv-control-system/sdk-motors.html)).

**[J] The three guards, in the order you add them:**

```java
// GUARD 1 — soft limits on the setpoint, before it ever reaches the controller.
targetTicks = Range.clip(targetTicks, Constants.LIFT_MIN_TICKS, Constants.LIFT_MAX_TICKS);

// GUARD 2 — clamp on the controller output, before it ever reaches the motor.
double out = pid.calculate(motor.getCurrentPosition(), targetTicks) + Constants.LIFT_KG;
out = Range.clip(out, -Constants.LIFT_MAX_OUT, Constants.LIFT_MAX_OUT);
motor.setPower(out * 12.0 / batteryVoltage);          // voltage compensation

// GUARD 3 — current alert, set once in init; checked every loop.
//   in init:
motor.setCurrentAlert(Constants.LIFT_CURRENT_ALERT_A, CurrentUnit.AMPS);   // e.g. 6.0 A, well under 9.2
//   in periodic():
if (motor.isMotorOverCurrent()) {          // bulk-read, cheap
    motor.setPower(0);
    stalled = true;                        // surface it on telemetry; do not hide it
}
```

**[J] `LIFT_MAX_OUT` is the parameter that turns "AI wrote it" from dangerous into merely wrong.** Set it to
**0.35 for the first run of any new mechanism.** A wrong sign at 0.35 power is a mechanism that drifts the
wrong way and gets stopped; a wrong sign at 1.0 is a repair.

**[J] Servo guard.** There is no current alert for servos. The only guard is the number:

```java
// in Constants.java — measured by hand-jogging with the mechanism visible
public static double CLAW_MIN = 0.30, CLAW_MAX = 0.65;
public static double CLAW_OPEN = 0.61, CLAW_CLOSED = 0.32;
// in the subsystem — the clamp exists so a bad caller cannot strip the servo
servo.setPosition(Range.clip(pos, Constants.CLAW_MIN, Constants.CLAW_MAX));
```

Never let an agent "fix" a servo problem by widening `CLAW_MIN`/`CLAW_MAX` or by adding `scaleRange()`. Those
two numbers are physical facts about your mechanism, measured with your eyes.

### 5.4 AI cannot tune your PID from a chat window

**This is the one people argue with, so here it is without hedging.**

A PID gain is not a property of the code. It is a property of **this motor, on this gearbox, with this
spool, carrying this mass, on this battery, with this much friction, at this loop rate, today.** The model
has access to exactly none of that. When it produces `kP = 0.005`, it has produced a number with the
statistical flavour of numbers that appear near the token `kP` in Java files. That is not an estimate. It is
a **prior**, and a weak one.

**[J] What actually happens when you accept a chat-window gain:**

| Symptom | What students conclude | What is actually true |
|---|---|---|
| Mechanism oscillates | "The AI's gain is wrong, ask for another" | You now have a random-search process with a 3-minute cycle time and no record |
| Mechanism is sluggish | "Add I" | You have added an integrator to a system you have not characterised, and it will wind up into the hard stop |
| It works on the bench, fails on the field | "Weird" | You tuned at 12.8 V with no load |
| It worked last week | "Something broke" | It did: the spool wore, the belt stretched, or the battery is older. **You cannot tell, because there is no tuning log** |

**[J] The correct workflow, which takes 20 minutes and produces a number you own:**

1. The **student** runs the tuning OpMode the AI built (§4.6, Prompt A) with **all gains at zero**.
2. Student raises **kP** alone until the mechanism reaches the setpoint and *just* begins to overshoot.
   Halve it. **This number is measured, and the student watched it happen.**
3. Add **kG** (gravity feedforward) for anything that falls, found by asking: what constant power holds it
   still? That is kG. Measured, not guessed.
4. Add **kD** only if there is overshoot left. Add **kI** essentially never — see
   `research/PROGRAMMING-PRACTICE.md` §6.2–6.4 for the per-mechanism procedures.
5. **Commit the constants.** Write two lines in `docs/TUNING-LOG.md`: what changed, what you observed.
6. Re-check on a **half-charged battery** and on the **actual field**, under load.

**Where the AI legitimately helps, and it is a lot:**

| Yes | No |
|---|---|
| Build the tuning OpMode and the CSV logger | Produce a gain |
| Explain what kP/kI/kD/kG/kV/kA each physically do | Tell you which one is wrong without data |
| Read a 300-row step-response CSV and compute rise time, overshoot %, settling time | Predict any of those from the code |
| Tell you *which gain to change next, in which direction*, **given the data** | Tell you the value |
| Write the JUnit test that your conversion math is right | Verify anything about physical behaviour |
| Draft the tuning-log entry from the diff | Decide the tuning is finished |

⚠️ **[FACT] One more reason the number cannot come from a chat window:** if you use `DcMotorEx`'s built-in
PIDF, **the coefficients do not persist across a power cycle**, and the SDK's `F` means something different
from the community `PIDFController`'s `F` (`research/PROGRAMMING-PRACTICE.md` §6.1b;
[ftc-docs PIDF coefficients](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/pidf_coefficients/pidf-coefficients.html)).
A number you did not measure, applied to the wrong `F`, and wiped at the next power cycle, is three failures
stacked. **[J]** This one trap has eaten more FTC weekends than any other single thing in this document.

### 5.5 Numbers you must measure, never accept

**[J]** Print this list. If any of these arrives from a chat window without a measurement behind it, it is a
bug regardless of whether the robot appears to work.

| Category | Examples |
|---|---|
| **Control gains** | kP, kI, kD, kF, kG, kS, kV, kA — every one, every mechanism |
| **Geometry** | `inPerTick`, `lateralInPerTick`, `trackWidth`, wheel diameter as built, odometry pod offsets, camera position and angle |
| **Mechanism positions** | Every servo position; every arm angle; every lift height in ticks; every soft limit |
| **Timing** | How long the claw takes to close; how long the flywheel takes to spin up; every timeout |
| **Field coordinates** | Every pose; every AprilTag position **[UNVERIFIED until Kickoff — BIOBUZZ §§9–10 are placeholders]** |
| **Performance claims** | Cycle time, success rate, auto reliability. **Especially these** — they go in the portfolio, and a judge may ask how you measured them |

**[J] The convention that makes this enforceable:** any unmeasured number in the repo is written
`= 0.0; // TODO MEASURE: <exactly how>`. A `grep -rn "TODO MEASURE" TeamCode/` at the end of every week is
your build-quality dashboard, and it costs nothing.

### 5.6 Branch discipline and the known-good rollback

**[J]** With one programmer and a robot that has to work Saturday morning, git is not version control; it is
**your undo button under stress**. Three rules:

| Rule | Command | Why |
|---|---|---|
| **`main` is what is on the robot right now** | — | So "put it back how it was" is unambiguous |
| **Tag before every event** | `git tag qual-1-2026-11-14 && git push --tags` | Rollback is `git checkout qual-1-2026-11-14`, executable by a panicking 15-year-old with no debugging required |
| **Event work happens on an event branch** | `git checkout -b event/qual-1` | Event hacks are event hacks. Merge on Sunday, deliberately, or throw them away |

Plus, specific to AI work:

- **One session, one branch, one mechanism.** `feat/lift-pid`. If the session goes sideways,
  `git checkout main` is a complete recovery.
- **Never let an agent run `git reset --hard`, `git clean`, `git rebase`, or a force-push.** These are in the
  `deny` list in §3.5 for exactly this reason. On a robotics team the uncommitted working tree is frequently
  the only copy of the thing that worked at 11 pm last night.
- **Commit before every deploy, even a bad commit.** `wip: about to try the new lift loop` is a perfectly
  good message. What you want is a point to return to.
- **[FACT]** Fork the SDK once per season into a fresh repo rather than merging upstream releases into last
  season's — the SDK's own contributor guidance warns that upstream pulls are not how team repos work
  (`research/PROGRAMMING-PRACTICE.md` §7.2).

### 5.7 The pre-deploy checklist — print it, tape it to the laptop

**[J]** Ten items. Under 90 seconds once it is habit. Nothing goes to the robot without it.

```
BEFORE CODE TOUCHES THE ROBOT
[ ]  1. A student read every changed line and can explain it without the AI open.
[ ]  2. ./gradlew :TeamCode:compileDebugJavaWithJavac  -> BUILD SUCCESSFUL
[ ]  3. ./gradlew :TeamCode:test                       -> all pass
[ ]  4. /footgun-review on the diff                    -> clean, or every finding answered
[ ]  5. Every new number is measured, or marked TODO MEASURE and set to a safe value.
[ ]  6. Output clamp present and set to <= 0.35 for anything new.
[ ]  7. Soft limits present on every setpoint that reaches hardware.
[ ]  8. Servo targets are inside the SAFE RANGE in CLAUDE.md. Nobody widened a range.
[ ]  9. Committed. If this is an event, we are on the event branch and main is tagged.
[ ] 10. Robot is on blocks, mechanism is free to travel, a human has a finger on STOP.

AFTER THE FIRST RUN
[ ] 11. It did what we predicted. If not, STOP and diagnose before changing anything.
[ ] 12. Loop time on the driver station is still what it was.
[ ] 13. Anything we measured went into Constants.java and docs/TUNING-LOG.md, in its own commit.
```

### 5.8 "A student reads and understands every line" is a safety control, not a nicety

**[J]** People treat rung 0 as the educational rung. It is also, empirically, the **most effective safety
rung**, because it is the only one that checks the code against facts that exist nowhere in the repo:
that the lift binds at 22 inches, that the claw servo was replaced last week and its range moved, that the
odometry pod on the left is 3 mm lower than the right one.

The agent cannot know those things. The student can. That is not a limitation of the tool; it is the actual
division of labour, and §7 makes it concrete.

---

## 6. The LEARNING problem — using AI so students learn MORE, not less

> **Cross-reference.** `research/AI-IN-FTC-POLICY.md` is the team-level policy document (what the rules
> permit, how to disclose, how to talk about it with judges and parents). This section is the
> **programming-specific slice**: how to run a software workstream so the AI raises the ceiling on what
> students understand instead of lowering the floor on what they have to.

### 6.1 The problem is real, and the community is already watching

**[COMM]** On **13 May 2026**, a thread titled *"Student written code"* opened on Chief Delphi's Programming
forum and ran to **66 posts**. Its premise, from the opening post: many teams were publicly celebrating that
most or all of their code — or their scouting app — was AI-written, most often with Claude, and the poster
asked which teams still used human programmers, arguing that hand-written code deserves recognition too.
([chiefdelphi.com/t/student-written-code/520752](https://www.chiefdelphi.com/t/student-written-code/520752))

**[COMM]** A mentor in that thread described the policy this document recommends, almost word for word:
students may use AI to ask questions, find references, or get line-by-line syntax suggestions, but they write
every line themselves with their own comments and must be able to say exactly what it does. *(seg9585,
13 May 2026, same thread.)*

**[COMM]** On **2 Feb 2026**, a separate thread, *"AI Use in FIRST?"*, ran 52 posts on the same question.
The most-supported framing was not prohibition but conditionality: opposition specifically *"if it hinders
students' learning"*, because the point is not to program a robot but to learn by programming it — with the
acknowledgement that AI legitimately explains concepts and gives starting points, and the caution that it
often gives false information. Another poster's version: use it responsibly and nobody minds; treat it as
having absolute authority and they do.
([chiefdelphi.com/t/ai-use-in-first/513475](https://www.chiefdelphi.com/t/ai-use-in-first/513475))

**[J] Three conclusions for your team:**
1. **The norm is "disclosed and understood," not "prohibited."** Nobody credible is arguing you cannot use it.
2. **The reputational risk is real and asymmetric.** Being known as the team whose code nobody can explain
   costs you goodwill with the exact people — mentors, alliance partners, judges — whose regard is worth the
   most to a small team. Getting ahead of it costs one sentence (§6.5).
3. **Note that these threads are FRC-leaning** (roboRIO, CAN IDs, swerve templates). The FTC-specific
   norms are less settled. **[UNVERIFIED]** whether an FTC-specific consensus exists as of Aug 2026.

### 6.2 Three modes, and which is allowed for which task

**[J]** Every AI interaction is one of three modes. Name them out loud, because "I used AI" hides the
distinction that actually matters:

| Mode | What happens | Learning effect | Where it is allowed |
|---|---|---|---|
| **TUTOR** — AI explains, student writes | Student asks "how does X work"; AI explains; **student writes the code** | **Strongly positive.** This is a private tutor with infinite patience and no schedule | **Everywhere. Encourage it. This should be 60%+ of your usage** |
| **REVIEWER** — student writes, AI critiques | Student writes; AI reviews against the footgun checklist and explains each finding | **Positive.** It is the code review a one-programmer team can never otherwise have | **Everywhere. Mandatory before every deploy** (§4.5) |
| **AUTHOR** — AI writes, student reviews | AI produces the code; student reads, understands, edits, owns it | **Negative *if unchecked*; neutral-to-positive if rung 0 is enforced** | **Only on the allow-list below** |

**[J] The AUTHOR allow-list — where letting the AI write is a good trade:**

| Task | Why authoring is fine here |
|---|---|
| Subsystem/OpMode **scaffolding** from a hardware description (§4.1) | It is structure, not behaviour. The student still supplies every number |
| **Tuning OpModes, dataloggers, CSV/plot scripts** (§4.6) | Instrumentation. Contains no claim about your robot |
| **JUnit tests** for a function the student specified | The student defined "correct"; the AI typed the assertions |
| **Documentation, portfolio drafts, tuning-log entries** from repo evidence (§4.7) | Derived from things the students did |
| **Build/tooling glue**: gradle test config, CI workflow, adb scripts, git hooks | Not robot behaviour. Failure is loud and cheap |
| **Boilerplate refactors** the student designed on a whiteboard (e.g. `sleep()` chain → state machine, §4.2) | The design is the student's; the transcription is typing |

**[J] The AUTHOR deny-list — never, regardless of deadline pressure:**

| Never AI-authored | Why |
|---|---|
| Any **control gain or physical constant** | §5.4, §5.5 |
| The **control strategy** for a mechanism (which controller, which sensor, what the states are) | This is the engineering. It is also literally what the Control and Design awards judge |
| The **auto route decision** (§4.8 gives you options; the choice is yours) | Judges ask *why*, and strategy is the team's identity |
| The **driver interface** — button mapping, macros, what the driver sees | Only your drivers know what they need. See `research/PROGRAMMING-PRACTICE.md` §8 |
| **Portfolio sentences about engineering decisions** | §4.7. Judges probe exactly these |
| **Anything you will be asked about in an interview and cannot currently explain** | The clean general rule |

### 6.3 The "explain it back" rule, operationalised

**The rule, in one sentence:** *no code merges until a student has explained every changed line out loud, to
another human, with the AI conversation closed.*

**[J] How to actually run it, in 5 minutes:**

| Step | What happens |
|---|---|
| 1 | Student closes the AI session. Opens `git diff`. |
| 2 | Reads the diff aloud to a teammate or the coach — **line by line, saying what it does and why it is there.** |
| 3 | For any line where the answer is "I think it..." or "the AI said..." — **that line does not merge.** Go back to TUTOR mode on that line specifically. |
| 4 | Teammate asks the three standing questions: **(a) What number in here did you measure?** **(b) What happens on the robot if this line is wrong?** **(c) What would you change to make it faster/simpler?** |
| 5 | Only then: rungs 1–6 of the safety ladder (§5.2). |

**[J] Why this specific ritual and not "be careful":**
- It has a **binary output** (merged / not merged), so it cannot degrade into a vibe.
- It is **fast enough to survive a build season.** 5 minutes. If it were 20, you would stop doing it.
- **It is simultaneously the safety gate and the interview rehearsal.** You are running your judge prep 40
  times a season without allocating any time to judge prep.
- **The teammate does not need to be a programmer.** The build lead is a perfectly good audience — arguably
  better, because they will ask what happens physically.

**[J] The variant for a one-programmer team.** With exactly one programmer there is no teammate to explain
to. Do it anyway, to the coach, or to a phone recording. A 90-second voice memo per merge, in a folder, is
(a) the same forcing function, (b) portfolio raw material, and (c) the single best onboarding asset for next
season's programmer.

**[J] The counter-test that catches self-deception.** Once a week, pick one file the AI wrote and have the
student **change it in a way that should break it in a specific, predicted way**, run it on blocks, and see
whether the prediction was right. If you can predict how it breaks, you understand it. If you cannot, you
have been reading, not understanding.

### 6.4 How this maps to surviving a judge interview

**[FACT]** The real FIRST Judging Question Bank (rev 25-26.1; the BIOBUZZ revision is "coming soon" per the
V0 manual) contains these **Control Award** questions verbatim
(`research/SCOUTING-AND-AWARDS.md` §13.3):

| The question | What it is really testing | What "explain it back" gave you |
|---|---|---|
| *"What pre-programmed libraries or outside resources did your team use?"* | Whether you know what is yours and what is not | **This is where AI belongs in your answer.** §6.5 gives the sentence |
| *"What sensors and hardware did your team use on your robot? — What worked, what did not, and why?"* | Whether you made choices or inherited them | You reviewed every sensor's code line by line and know why each one is there |
| *"How does your robot: know where it is on the field? control acquisition of scoring elements? measure and control the speed of the motors?"* | Whether a *student* understands the control loops | Rung 0, forty times over |
| *"What enhancements did your team program to assist the drivers during Teleop?"* | Whether software serves the drive team | You designed the state machines (§4.2); the AI transcribed them |
| *"How did your team measure reliability?"* | Whether you measure anything at all | `docs/TUNING-LOG.md` and the `EVIDENCE NEEDED` list from §4.7 |

**[FACT] The format makes it harder, not easier.** BIOBUZZ §6.1.2 allows an **unscheduled pit interview**:
judges arrive at your pit unannounced, in a noisy environment; the Judge Advisor picks two mandatory
questions from the bank (one MCI, one TA) that every team is asked. **[FACT]** Follow-up pit interviews are
run by **award-specific panels** — if the questions cluster on control, you have been nominated for Control.
**[FACT]** Judges are trained that *"a Judge's role is to recognize teams doing something right, not to
penalize teams from doing something wrong"* (FIRST *Judge Manual* rev 25-26.1).

**[J] What that adds up to.** Nobody is going to accuse you of using AI. What will happen is far simpler and
far more decisive: **a judge will ask a student how something works, and either the student can answer or
they cannot.** Everything in §6.3 exists to make sure the answer is yes.

**[J] The 20-second answer, drilled.** When asked about libraries and outside resources, the strong version is
concrete and finishes on your own engineering:

> "We use *(your path library)* for path following and the SDK's VisionPortal for AprilTags. We use Claude
> Code as a programming assistant — mostly to explain APIs and to review our code for the mistakes that break
> robots. Every line that runs on our robot was read and understood by one of us before it shipped, and every
> number in it — our PID gains, our servo positions, our inches-per-tick — we measured ourselves on the robot.
> Here's our tuning log."

Then hand them the tuning log. **[J]** That is a *stronger* answer than "we wrote everything ourselves,"
because it is verifiable, it is specific, and it demonstrates a process. Practise it until it is boring.

### 6.5 Disclosure — what the manual requires, and what to write

**[C] For the portfolio, credit is required.** §6/A201: *"Teams may use AI and research aids to compose their
portfolios, provided they respect intellectual property rights and include a footnote or endnote credit.
Example Credit: 'Portfolio created by Team XXXXX and ChatGPT'"*

**[C] For code, there is no rule** — R101 governs the robot and its major mechanisms, and its blue box
explicitly does not prohibit outside help with *"writing software."* Its intent clause is the standard:
the robot should be *"representative of the current team members' experience."*

**[J] What to actually write**, in three places:

| Where | What |
|---|---|
| **Portfolio endnote** (required) | `Portfolio prepared by FIRST Tech Challenge Team <NNNNN>. Drafting assistance from Claude (Anthropic). All engineering content, data and decisions are the team's own.` |
| **Portfolio, control-system section** (optional, **[J] recommended**) | One sentence: `Our software is written with AI assistance (Claude Code) used as a tutor and code reviewer. Every line was reviewed and understood by a student before deployment; every control constant was measured on the robot.` |
| **Repo `README.md`** (**[J]** recommended) | The same sentence, plus a link to your team AI policy. Costs nothing; ends the conversation before it starts |

**[J] Also log it in the engineering notebook the way you would log a mentor's suggestion** — "asked Claude
to explain `setVelocity` vs `setPower`; chose `setPower` with our own PID because…". That is exactly the kind
of decision-with-reasoning trail the Think Award rewards, and it doubles as your AI disclosure.

### 6.6 A one-page team AI policy for the software workstream

**[J]** Adopt this, or something you argue your way to. Have every programmer and the coach sign it in
September. It takes ten minutes and it settles every argument you would otherwise have in February at 10 pm.
*(The team-wide version — covering portfolio, outreach and business — belongs in
`research/AI-IN-FTC-POLICY.md`; this is the code-specific extract.)*

```
TEAM <NNNNN> SOFTWARE AI POLICY — 2026-27 BIOBUZZ

1. We use AI. We say so. We are not embarrassed about it and we are not casual about it.
2. Default mode is TUTOR (it explains, we write) and REVIEWER (we write, it critiques).
   AI may AUTHOR only: scaffolding, tuning harnesses, tests, tooling, and documentation drafts.
3. No line of code reaches the robot until a student has read it aloud and explained it,
   with the AI closed. If you cannot explain a line, it does not merge.
4. No control gain, servo position, distance, angle or timing constant ever comes from a chat window.
   Every one is measured on the robot and committed with a note in docs/TUNING-LOG.md.
5. Every deploy passes the pre-deploy checklist. No exceptions on event days -- especially on event days.
6. We never ask AI for a rule interpretation. The Competition Manual PDF is the only authority.
7. We disclose AI assistance in the portfolio (required by A201) and in our repo README (our choice).
8. If a judge asks who wrote our code, we answer honestly and specifically, and we show the tuning log.
9. If AI use is making someone learn less, we change how we are using it. That is the whole point.

Signed: ______________________  ______________________  ______________________   Date: __________
```

---

## 7. THE DIVISION OF LABOUR — who does what, task by task, week by week

**[J]** §6 said *why* the split matters. This section is the split itself: concrete enough to print, argue
about, and tape to the wall next to the pre-deploy checklist (§5.7).

### 7.1 The rule in one line, and the four-question test

> **The AI may do the typing. It may never do the deciding, the verifying, or the explaining.**

**[J]** Before you hand any task to Claude Code, ask four questions in this order. The answer to the first,
third and fourth is **always "a student."** Only the second is negotiable.

| # | Question | Who must answer it | If you get this wrong |
|---|---|---|---|
| 1 | **Who DECIDES?** — what the mechanism should do, which controller, what "correct" means | **Student, always** | You have outsourced the engineering. This is exactly what Design, Think and Control judge |
| 2 | **Who TYPES?** — who produces the characters in the file | Negotiable — see the AUTHOR allow-list (§6.2) | Nothing, if rungs 0–6 hold |
| 3 | **Who VERIFIES?** — who puts the robot on blocks and watches it move | **Student, always** | §5. The robot or the field pays |
| 4 | **Who EXPLAINS IT TO A JUDGE?** — in 90 seconds, laptop closed | **Student, always** | §6.4. You lose the interview, and you deserve to |

**[J] The corollary that saves the most time:** if a task fails question 1, 3 or 4, **do not start the
prompt.** Most wasted AI time on a robotics team is a student prompting their way around a decision they had
not made yet. Ten minutes at a whiteboard first is not overhead; it is the input.

### 7.2 The master split table — every software task of a season

**[J]** Columns: what the agent does, what the student does, what is **never** delegated, the gate that signs
it off (rung numbers are the safety ladder, §5.2), and my estimate of hours returned. The estimates are
judgment, not measurement — **measure your own and correct this table in December.**

| # | Task | Agent does | Student does | NEVER the agent | Gate | Hours saved **[J]** |
|---|---|---|---|---|---|---|
| 1 | **Repo + toolchain setup** (fork, test source set, `.gitignore`, CI, hooks) | Writes the Gradle test config, CI workflow, `.claude/` files, `protect-sdk.sh` | Runs a clean-clone build; confirms deploy to the Control Hub | Bumping SDK/AGP/Gradle versions on its own initiative | Clean clone builds and deploys | 3–5 h, once |
| 2 | **`CLAUDE.md` authoring** (§3.4) | Drafts from `/init` + the template; keeps it under 200 lines | Fills the hardware map, units and safe ranges **from the physical robot** | Inventing a config name, a safe range, or a version number | `/context` shows it loaded; every string matched to the RC config screen | 1 h once, +10 min/week |
| 3 | **Hardware map change** (motor added/moved) | Updates `HardwareNames.java`, `docs/HARDWARE.md`, `CLAUDE.md` from dictation | Reads the names off the Driver Station config screen out loud | Guessing the string | `init()` runs on the robot with no `NullPointerException` | 15 min each |
| 4 | **Subsystem + OpMode scaffolding** (§4.1) | Writes the class, the constants block with `TODO MEASURE`, and the tuner OpMode | Confirms the restatement; reads the diff aloud; measures every constant | Producing any number that could be measured | Rungs 0→3, then 5 | 1–2 h per mechanism |
| 5 | **State machine from a spec** (§4.2) | Transcribes the whiteboard into an enum + `periodic()`; adds timeouts | **Draws the state machine first**; names the states; sets the timeouts | Inventing states or transitions the student did not draw | Rung 0 + a dry run on blocks | 1–2 h per sequence |
| 6 | **Path library setup** (Pedro / Road Runner) | Gradle coordinates, quickstart wiring, explains each tuner OpMode | Runs every tuner; records every number in `docs/TUNING-LOG.md` | Producing localization constants, track width, or ticks-per-inch | Repeatable point-to-point, ±1 in (`research/SEASON-CADENCE.md` §3.4 Week C) | 3–4 h, once |
| 7 | **PID / feedforward tuning** (§4.6, §5.4) | Builds the harness; plots and interprets logged data; proposes the *next experiment* | Turns the knobs, on the robot, and writes down what happened | **Any gain. Ever. From a chat window** | Rung 6 + tuning-log entry | 2–3 h per mechanism (harness only) |
| 8 | **Autonomous route** (§4.8) | Converts the agreed plan into path stubs and a timing budget; flags overruns | Decides *what to score and in what order*; runs it ×10; records the success rate | Choosing the scoring priority — that is the strategy judges probe | Rung 4 (sim) → 5 → 6, then 10 consecutive runs | 2 h per route revision |
| 9 | **Vision (AprilTag / colour)** | `VisionPortal` boilerplate; explains exposure/gain/threshold parameters; EOCV harness | Lighting tests **on the actual field**; thresholds measured under venue light | Threshold values; camera pose numbers | Detection rate measured at ≥2 distances | 2–3 h |
| 10 | **Teleop bindings and driver macros** | Types exactly what the driver dictated; nothing more | **Designs the control scheme.** Drives. Changes it. Drives again | Designing or "improving" a control scheme | The driver says it is right, after driving it | ~0 — and that is correct |
| 11 | **Telemetry + datalogging** | Authors the whole thing (verbosity levels, CSV datalogger, field overlays) | Says which signals matter | — | Loop time unchanged (§4.5) | 2–4 h |
| 12 | **Unit tests** | Authors the assertions | Defines what "correct" means, in numbers | Deciding the expected values | `./gradlew :TeamCode:test` green in CI | 3–6 h across the season |
| 13 | **Log triage** (§3.8) | Subagent reads `robotControllerLog.txt`; returns a ranked hypothesis list with evidence lines | Reproduces the top hypothesis on the robot | Declaring a root cause without a reproduction | Failure reproduced on demand | 30–60 min per incident |
| 14 | **Build-failure debugging** | First pass on the stack trace; names the file and the likely cause | Confirms on the machine; keeps the fix minimal | Editing the SDK module to make an error go away (denied, §3.5) | Build green, no SDK diff | 20–40 min each |
| 15 | **Pre-deploy code review** (§4.5) | `/footgun-review` on the diff | **Answers every finding out loud** — accept or reject, with a reason | Being the last reviewer before the robot moves | Rung 3, then the §5.7 checklist | The whole point |
| 16 | **Git hygiene, branches, event tags** (§5.6) | Proposes exact commands; writes commit messages from the diff | **Runs anything irreversible personally** | `reset --hard`, `clean`, force-push, rebase (denied, §3.5) | `main` tagged before every event | 20 min/week |
| 17 | **Code documentation** (§4.7) | Drafts from the code and the git log | Corrects every claim about *why* | Inventing a rationale the team never had | A student can defend each sentence | 3–5 h per event cycle |
| 18 | **Control Award submission** (§4.7) | Assembles the draft from the repo, tuning log and match data | **Rewrites it in their own voice**; cuts anything they cannot demo | Any claim the robot cannot perform on request | Read aloud, timed, judged internally | 4–6 h |
| 19 | **Notebook / tuning-log entries** | Formats the student's numbers into the template | Supplies the numbers and the decision | Fabricating a session that did not happen | Dated entry, same day | 15 min/session |
| 20 | **Rule interpretation** | **Nothing** | Reads the manual PDF; posts to the official Q&A | **All of it.** The PDF is the only authority (§6.6 rule 6) | Rule number cited from the PDF | 0 — deliberately |
| 21 | **Scouting → software decisions** | Pulls and summarises match data, computes rates (see `playbook/AI-FOR-DESIGN-AND-ANALYSIS.md`) | Decides which auto to run against which alliance | Deciding the strategy | Decision written on the strategy board | 1–2 h per event |
| 22 | **Event-day fix** (§7.7) | Explains and reviews only, read-only | **Types every character** | Writing code between matches | Two students agree; bench test if any mechanism moves | Negative — see §7.7 |

**[J] Read the last column downward.** The hours come back from **rows 1, 4, 11, 12, 17, 18** — setup,
scaffolding, instrumentation, tests and writing. They do **not** come back from rows 7, 8, 10, 20, 22 —
tuning, strategy, driver interface, rules, event day. That is exactly the shape §1.1 predicted, and it is
the argument for doing the boring infrastructure work *with* AI in September so the students have February
free for the things AI cannot touch.

### 7.3 A typical build-season week — the 12 h/week shape, hour by hour

**[J]** This overlays the software workstream onto the standing agendas in `research/SEASON-CADENCE.md` §8.2
(3-hour weekday) and §8.3 (Saturday). **The AI column is the point:** notice how much of the week is
deliberately **AI-OFF**.

**Assumptions:** 2 × 3 h weekday meetings + 1 × 6 h Saturday = 12 h in the room, plus ~2.5 h async per
programmer (`research/SEASON-CADENCE.md` §8.7, quoting GM0: *"software can be written outside of practice
hours"*). One or two programmers; weeks 3–9 of build.

| When | Block | AI | Who does what |
|---|---|---|---|
| **Mon · async · 45 min** | **Spec + plan, no code** | **ON — plan mode only** | Student writes the week's software task as a spec. Runs Claude Code in **plan mode** (`Shift+Tab` until the status bar shows `⏸ plan mode on`, or `claude --permission-mode plan`) so it reads the repo and answers questions **without editing** ([best practices](https://code.claude.com/docs/en/best-practices)). Output is a plan file, not a diff. **Nothing merges on a Monday** |
| **Tue 0:00–0:10** | Standup | OFF | 45 seconds each: did / doing / blocked |
| **Tue 0:10–0:20** | Hardware sync | OFF | Build lead states what physically changed since Thursday. Student edits the `CLAUDE.md` hardware map **in the room** |
| **Tue 0:20–2:20** | **Focus block — implement** | **ON — author mode, scaffolding only** | Agent scaffolds what Monday's plan specified (§4.1/§4.2); compiles after every edit; student reads every diff aloud (rung 0) and runs `/footgun-review` (rung 3). Target state: **compiled and tested, not yet deployed** |
| **Tue 2:20–2:40** | **FIELD BLOCK** | **OFF — laptop closed except the Driver Station** | Robot on blocks first (rung 5), then tiles at ≤50 % authority (rung 6). Somebody has a finger on stop |
| **Tue 2:40–3:00** | Log + close | ON — dictation only | Student dictates what happened; agent formats it into `docs/TUNING-LOG.md`. Commit. Name tomorrow's single task |
| **Wed · async · 45 min** | **Instrumentation + tests** | **ON — full author** | The highest-value async hour of the week: tuning OpModes, dataloggers, JUnit tests, plot scripts (§4.6). None of it changes robot behaviour, so it is safe to write with no robot present |
| **Thu 0:10–0:20** | **Rules delta** | **OFF** | Rules Night owner presents the Team Update diff. **The agent is not consulted on rules** (§6.6 rule 6) |
| **Thu 0:20–2:20** | **Focus block — measure** | ON — interpreter mode | Run Wednesday's tuning OpModes on the robot. Student turns the knobs; agent reads the logged CSV and proposes the **next experiment**, never the gain (§5.4) |
| **Thu 2:20–2:40** | FIELD BLOCK | **OFF** | As Tuesday. Every measured number lands in `Constants.java` in its own commit |
| **Fri · async · 30 min** | **Log triage + writing** | ON — subagent | Pull `robotControllerLog.txt`; run the log-triage subagent (§3.8); draft the week's documentation paragraph from the git log (§4.7) |
| **Sat 0:00–0:15** | Standup, one objective | OFF | The day gets **one** software objective. Not three |
| **Sat 0:15–2:15** | **Focus A — the hard thing** | Mixed | Auto route iteration (§4.8): sim first (rung 4), then blocks, then field. Agent writes path stubs; student decides the route and counts successes out of ten |
| **Sat 2:30–4:00** | Focus B — integration | Mixed | Everything the week produced runs together, once, end to end. This is where loop-time regressions surface |
| **Sat 4:45–6:15** | **DRIVER PRACTICE (W6+)** | **OFF — non-negotiable** | The AI has no role here and never will. This block decides your season |
| **Sat 6:15–6:45** | Full-team demo | OFF | Software shows the whole team what changed, in plain language. **This is judge-interview rehearsal disguised as a demo** (§6.4) |
| **Sun · 20 min** | **Weekly checklist** | ON — assistant | Run §9.2: tag, prune `CLAUDE.md`, update the tuning log, write next week's one-line goal |

**[J] Three rules that make the week work:**

1. **Nothing written on Monday or Wednesday deploys until Tuesday or Thursday, with a human watching.**
   Async AI work accumulates *candidates*; the meeting is where candidates become code. This single
   discipline is what keeps AI throughput from becoming a queue of untested guesses (§3.9).
2. **The field block is AI-off, every meeting, no exceptions.** If the answer to "what do we do now" comes
   out of a chat window while the robot is on the tiles, the students have stopped observing their own robot.
3. **One software objective per session.** An agent will happily open four workstreams at once. A
   one-programmer team cannot verify four workstreams at once, and unverified is worse than undone.

### 7.4 The same week at 4.5 hours — the compressed shape

**[FACT]** `research/SEASON-CADENCE.md` §8.2 records a real counter-example: **FTC 17012 runs 2:45–5:00 pm
twice a week — 4.5 h/week** — and still reached an archetype decision in Week 2. **[J]** If that is your
reality, do not run the §7.3 week badly. Run this instead.

| Keep at full size | Cut, or move async | Why |
|---|---|---|
| The **field block, both meetings** (20 min each) | — | The robot touches the field every meeting. Cut anything else first |
| **Rung 0 read-aloud** and `/footgun-review` | — | These are the safety gates — and the fastest items on the list |
| **Driver practice from W6** | — | Cutting driver practice to write more code is the most common losing trade in FTC |
| Tuning **measurement** on the robot | Tuning **harness** authoring → async Wednesday | Only the measuring needs the room |
| One weekly integration run | Scaffolding, tests, docs, log triage → **all async** | None of it needs the robot |
| — | **Cut: the second auto route.** Ship one and make it 90 % reliable | Reliability beats variety at every level below Worlds |
| — | **Cut: vision beyond what your auto actually requires** | The most seductive time sink in FTC software |

**[J] The compressed week in one line:** *everything that does not need the robot happens between meetings
with the agent; the meeting is robot time, and the agent is closed for most of it.* At 4.5 h/week the AI's
contribution is not speed — it is that your two async hours are worth four.

### 7.5 Two programmers, or one — how to divide the humans

**[J]** With **two** programmers, split by *subsystem ownership*, not by "one writes, one reviews" — then
swap the review role weekly so both can answer any judge question.

| | Programmer 1 | Programmer 2 |
|---|---|---|
| Owns | Autonomous, path following, tuning | Teleop, driver interface, vision, telemetry |
| Reviews | P2's diffs (rung 0 + `/footgun-review`) | P1's diffs |
| Must still be able to | Explain P2's vision pipeline to a judge | Explain P1's PID loop to a judge |
| Weekly swap | Alternate ownership of the auto route on odd/even weeks | Prevents the single-deep failure (`research/SEASON-CADENCE.md` §8.1) |

**[FACT] The reviewer should not be the author's session.** The Claude Code docs recommend a **Writer /
Reviewer** pattern across two sessions precisely because *"a fresh context improves code review since Claude
won't be biased toward code it just wrote"* ([best practices](https://code.claude.com/docs/en/best-practices)).
**[J]** Do the human version of the same thing: the student who ran the session is not the student who signs
the diff.

**[J] With one programmer** you cannot do that, so buy the substitute twice over: run the review as a
**fresh subagent** on the diff — the bundled `/code-review` skill reviews the current diff in a separate
context and returns findings ([best practices](https://code.claude.com/docs/en/best-practices)) — **and** have
a non-programmer teammate sit through the read-aloud. They will not catch a sign error, but they will catch
"wait, why does that happen twice?" more often than you expect, and the explaining itself is the learning
(§6.3).

### 7.6 Session mechanics — the ten moves that decide whether any of this works

**[FACT]** All from the official Claude Code documentation, read 22 Aug 2026. The **[J]** verdicts are mine.

| Move | What it is | Why it matters on an FTC repo |
|---|---|---|
| **Plan mode** | `Shift+Tab` until the status bar shows `⏸ plan mode on`, or start with `claude --permission-mode plan`. Claude reads and answers without making changes; `Ctrl+G` opens the plan in your editor ([best practices](https://code.claude.com/docs/en/best-practices)) | **[J] The default mode on a robot repo.** Use it for anything bigger than a one-line fix. The docs' own exception is the right one: skip planning when *"you could describe the diff in one sentence"* |
| **Give it a check it can run** | The docs' first principle: *"Give Claude a check it can run: tests, a build, a screenshot to compare."* | **[J]** On an FTC repo that check is `:TeamCode:compileDebugJavaWithJavac` plus `:TeamCode:test` — both pre-approved in §3.5. Without a check, **you** are the verification loop, and you are also the person who has to be standing at the robot |
| **`/clear` between tasks** | Resets the context window entirely | **[J]** Clear between *mechanisms*. A session that debugged the lift, then wrote a vision pipeline, then returned to the lift is a session that will hallucinate lift constants |
| **The two-correction rule** | Docs: after two failed corrections, `/clear` and write a better prompt incorporating what you learned | **[J]** On FTC code a third correction almost always means the agent is missing a *physical fact*. Add the fact to `CLAUDE.md`, then start over |
| **`/compact <instructions>`** | Compaction with steering, e.g. `/compact Focus on the lift tuning numbers` | **[J]** Use it before a long tuning session so the measured numbers survive summarisation |
| **`/rewind` (Esc Esc)** | Restores conversation and/or code to an earlier checkpoint | ⚠️ **[FACT] Checkpoints only track changes made through Claude's file-editing tools — changes made through Bash are not captured, and checkpointing is "not a replacement for git."** **[J]** Commit before anything risky. Your rollback is a git tag (§5.6), never a checkpoint |
| **Subagents for investigation** | *"use subagents to investigate X"* — they run in a separate context and report back a summary ([sub-agents](https://code.claude.com/docs/en/sub-agents)) | **[J]** Exactly right for log triage (§3.8) and for "where is this hardware name used across the whole repo" |
| **Adversarial review** | The bundled `/code-review` skill reviews the current diff in a fresh subagent and returns findings | **[J]** Run it *after* `/footgun-review` and *before* the read-aloud. Two different lenses, both cheap |
| **`claude -p` non-interactive** | `git diff main \| claude -p "..."` as a project linter; `--allowedTools` to scope permissions; `--output-format json` for scripts; `--bare` for CI ([headless](https://code.claude.com/docs/en/headless)) | **[J] The one to actually build:** a pre-commit footgun linter that pipes the staged diff into `claude -p`. Piping the diff means it needs no Bash permission at all — the safest possible shape for automation on a robot repo |
| **`/context` and `/doctor`** | `/context` confirms `CLAUDE.md` was loaded; `/doctor` proposes cuts to a checked-in `CLAUDE.md` | **[J]** Run `/context` the first time each student opens the repo. Half of "the AI ignored our rules" turns out to be "the AI never loaded the file" |

⚠️ **[J] One warning about auto mode.** On Pro/Max/Team plans, interactive sessions start in **auto mode**,
where a classifier model reviews most actions instead of you ([best practices](https://code.claude.com/docs/en/best-practices)).
That is fine for a web app. On a robot repo, **verify by hand, once, that your `ask` rule on `installDebug`
and `deploySloth` still prompts you** before you rely on it. A classifier that has never met your robot
cannot know that deploying *is* the dangerous step. If it does not prompt, move those commands to `deny` and
run them yourself in a second terminal.

### 7.7 Event week and event day — the division of labour changes

**[J]** This is the part teams get wrong most often, and it is the cheapest thing on this page to get right.

| Phase | The AI's role | Hard rules |
|---|---|---|
| **Event − 7 days** | Normal, but this is the last window for **new** AI-authored behaviour | Feature freeze Sunday night. After that: bug fixes and tuning only |
| **Event − 2 days** | Documentation and checklists only | One **full `installDebug`** — never take a hot-reload build to an event (§3.9). Tag `main`. Charge everything |
| **Event day, in the pit** | **Read-only: explain, review, diff. Nothing else** | **No AI-authored code goes on the robot at an event.** If a change is genuinely needed between matches, a student types it, a second student reads it, and it gets a bench test if any mechanism moves |
| **Event day, on the field** | None | R704.C — the laptop is off the robot's network during match play (`research/PROGRAMMING-PRACTICE.md` §1.2) |
| **Event night** | Log triage, match-data summary, tomorrow's list | Fix nothing at 11 pm that you cannot bench test at 11:15 pm |

**[J] Why "read-only at events" is not paranoia.** At an event you have no bench, no blocks, five minutes,
and an audience. Every safety rung that makes AI-authored code acceptable (§5.2) is unavailable. The correct
mental model: **at an event the AI is a very fast reference manual and a very good rubber duck, and nothing
else.**

### 7.8 Five ways the division of labour breaks, and the fix for each

| Anti-pattern | What it looks like | Fix |
|---|---|---|
| **Prompt-instead-of-decide** | A student prompts three times to avoid choosing between two control approaches | Whiteboard first. §7.1, question 1 |
| **The unverified queue** | Six AI-written changes, none deployed, all "probably fine" | One objective per session (§7.3, rule 3). Deploy it or delete it |
| **The silent co-owner** | One student runs every session; the other has not written code since October | Weekly ownership swap (§7.5), enforced at the Saturday demo |
| **The number that came from a chat** | A servo position in `Constants.java` that nobody can trace to a measurement | Every constant commits with a tuning-log line (§5.5). No line, no merge |
| **Event-day heroics** | New feature written in the pit at 9:40, deployed 9:44, robot dead at 9:52 | §7.7. The feature freeze is a rule, not a preference |

---

## 8. Where this lands on the calendar — the software AI plan, phase by phase

**[J]** §7 is a week. This is the season. It is the software-specific expansion of the phase table in
`research/SEASON-CADENCE.md` §9, and it assumes the dates in §1.1 of that file.

### 8.1 The 21 days before kickoff — 22 Aug to 11 Sep 2026

**[FACT]** `research/SEASON-CADENCE.md` §3.4 already gives the team-wide three-week plan. **[C] R304** permits
software written before Kickoff to be reused, so **every hour spent here is banked, not wasted**. Below is the
software column, expanded with the AI work — this is the single highest-return AI window of your entire season,
because none of it is game-dependent and all of it is infrastructure.

| Week | Ship this | AI does | Student does | Done when |
|---|---|---|---|---|
| **A · Aug 22–28**<br>*infrastructure* | Fork on **v11.2.1**; the §3.2 layout; `CLAUDE.md`; `.claude/settings.json`; `protect-sdk.sh`; test source set + CI | Scaffolds every file above; writes the CI workflow and the pre-commit hook; drafts `CLAUDE.md` from `/init` + §3.4 | Installs Android Studio; deploys one OpMode; **fills the hardware map by reading the RC config screen**; runs `/context` to confirm the file loads | Every student has pushed one commit and deployed one OpMode; a clean clone builds |
| **A · Aug 22–28** | The four skills (§3.7) + the log-triage subagent (§3.8) | Writes them from the templates in this file | Tests `/footgun-review` against a deliberately broken OpMode | `/footgun-review` finds a planted `sleep()` and an unclamped output |
| **B · Aug 29–Sep 4**<br>*drivetrain* | Teleop drive, telemetry, Driver Station practice timer; Sloth verified | Scaffolds the drive subsystem and telemetry levels; explains `setPower` vs `setVelocity` (§4.3) | **Drives a figure-8.** Measures ticks-per-inch. Writes both into `Constants.java` with a tuning-log entry | Chassis drives a figure-8; `deploySloth` demonstrated **and** plain `installDebug` demonstrated |
| **B · Aug 29–Sep 4** | Unit tests for `util/MathFunctions.java` | Authors the assertions | Defines the expected values (angle wrap, clamps, unit conversions) | `./gradlew :TeamCode:test` green in CI |
| **C · Sep 5–11**<br>*measure & rehearse* | Path library chosen and **tuned**; point-to-point ±1 in | Explains each tuner OpMode; interprets the logged data; builds the plotting script | **Runs every tuner. Records every number.** Repeats the localization test ten times | Repeatable point-to-point moves; a tuning log with dated entries |
| **C · Sep 5–11** | The **pre-kickoff dress rehearsal for the merge** | Writes the "copy `TeamCode` into a fresh v12.0 clone" runbook | Practises it once, against a fresh v11.2.1 clone, and times it | The runbook exists and someone has executed it once |

**[J] The pre-kickoff item nobody does and everybody should:** rehearse the SDK migration *before* the SDK
exists. **[FACT]** `research/PROGRAMMING-PRACTICE.md` §2.3: FTC upstream releases are *not* merge-friendly, and
the recommended path is a fresh clone of the new quickstart with your `TeamCode` copied in. **[J]** Doing that
once, in early September against a v11.2.1 clone, converts kickoff week's scariest task into a 30-minute
checklist item. Have the agent write the runbook; have a student execute it.

### 8.2 Kickoff weekend and kickoff week — 12–18 Sep 2026

**[FACT]** Kickoff broadcast is **12:00 p.m. ET, Saturday 12 Sep 2026**
(`research/SEASON-CADENCE.md` §4; [FIRST game & season page](https://www.firstinspires.org/programs/ftc/game-and-season)).
**[FACT]** The scoring element is **Pollen** — plastic balls of roughly 3 in. diameter, described as similar in
character to DECODE's Artifacts
([FIRST community: BIOBUZZ season dates](https://community.firstinspires.org/key-upcoming-biobuzz-season-dates)).
**[UNVERIFIED]** everything else about the game until 12 Sep.

| When | Software task | AI role |
|---|---|---|
| **Sat 12 Sep, +2 h** | Manual ingest (`tools/ingest-manual.sh`); build the searchable rule index | **High** — this is a pure reading-and-indexing task, the thing AI is unambiguously best at |
| **Sat 12 Sep, evening** | **Nothing in code.** Strategy is a whiteboard activity | **None.** The archetype decision is the students', and judges will ask them to defend it (`research/SEASON-CADENCE.md` §9) |
| **Sun 13 Sep** | Auto *time budget* arithmetic for the two candidate strategies | Medium — arithmetic and sensitivity, from the students' own numbers |
| **Mon–Wed 14–16 Sep** | **SDK v12.0 migration** using the rehearsed runbook (§8.1) | Medium — it executes the runbook; a student verifies the deploy and re-runs the drive test |
| **Wed 16 Sep** | Update `CLAUDE.md`: pinned versions, new game vocabulary, new field coordinates | High — but a student checks every version string against the actual `build.dependencies.gradle` |
| **Thu 17 Sep** | Re-verify **Sloth against v12.0**; re-verify the CI build | Medium — see §9.1, item 6 |
| **Fri 18 Sep** | First game-specific subsystem scaffold (§4.1) | High — structure only, no numbers |

⚠️ **[J] The kickoff-week trap.** The agent's training data will contain a great deal about INTO THE DEEP and
DECODE and **nothing** about BIOBUZZ. Expect confident, wrong statements about scoring, field geometry and
element names for the first several weeks. **Treat every game-specific claim from the AI as [UNVERIFIED] and
check it against the manual PDF.** This is not a temporary bug — it is the permanent condition for any brand-new
game, and it is exactly why §6.6 rule 6 exists.

### 8.3 Build to your first event — W1 to W9

| Weeks | Software focus | Where AI earns its keep | Where it must stay out |
|---|---|---|---|
| **W1–W2** | Subsystem scaffolds as mechanisms appear; hardware map churn | Scaffolding (§4.1); keeping `HardwareNames.java` and `CLAUDE.md` in sync with a robot that changes daily | Mechanism control strategy |
| **W3–W4** | State machines; first auto path; tuning harnesses | §4.2, §4.6 — the harness work small teams always skip | Every gain and setpoint |
| **W5–W6** | Auto reliability; teleop macro design; **driver practice starts** | Log triage, loop-time analysis, unit tests | The driver interface (§7.2 row 10) |
| **W7–W8** | Integration, failure hunting, second driver's controls | `/footgun-review` on everything; datalog analysis across many runs | Deciding which failures matter |
| **W9** | **Freeze, document, rehearse** | Control Award draft from the repo (§4.7); documentation; the pre-event checklist | New features |

### 8.4 Between events — November to February

**[J]** The between-events loop is where a small team can out-improve a bigger one, because improvement here
is *analysis-limited*, not labour-limited — and analysis is the AI's strongest suit.

| Cadence | Task | AI role |
|---|---|---|
| **Event night** | Pull all logs and match data; produce a ranked failure list with evidence | High — subagent triage (§3.8) |
| **Event + 2 days** | Turn the failure list into a prioritised software backlog | Medium — students rank; agent estimates |
| **Weekly** | Team Update diff → does anything change our software? | Medium — **[J]** the agent summarises; the student owns the answer (§6.6 rule 6) |
| **Monthly** | `CLAUDE.md` prune and refresh (§9.3); re-run `/doctor` | High |
| **Before each event** | §9.4 | Medium |

### 8.5 Off-season — May to September 2027

**[J]** Two things only, and they compound: (1) **write down every correction you gave the agent this
season** and fold it into next year's `CLAUDE.md`; (2) **teach the next programmer** using the TUTOR mode of
§6.2, with the outgoing programmer sitting in. `research/SEASON-CADENCE.md` §7.2 argues that the off-season is
where the next season is actually won; the software version of that claim is that a `CLAUDE.md` refined over
two seasons is worth more than any library you could adopt.

---

## 9. Checklists

**[J]** Four checklists. Print §9.1 and §9.4; put §9.2 in your Sunday calendar; put §9.3 in the first
meeting of each month. The pre-deploy checklist (§5.7) is separate and lives on the laptop.

### 9.1 Kickoff-day and kickoff-week software checklist — 12–18 Sep 2026

```
KICKOFF SOFTWARE CHECKLIST                                 Team <NNNNN> · Sep 2026

MANUAL AND RULES
[ ]  1. Run tools/ingest-manual.sh on the kickoff manual; confirm sections 8-11, 13, 14 now have content.
[ ]  2. Diff the final Section 12 (R-rules) against the V0 version. Anything that changes wiring,
        current limits or software behaviour goes on the software backlog the same day.
[ ]  3. CHECK THE OFFICIAL Q&A for any guidance on AI use and code authorship (the Q&A opens **28 Sep 2026, 12:00 p.m. ET**, not at Kickoff;
        no such entry existed as of 22 Aug 2026 -- section 2, item 4). Record the answer in the team
        AI policy (section 6.6). Do NOT ask the AI what the rules say.

SDK AND TOOLCHAIN
[ ]  4. SDK v12.0 released? Version number recorded: ______________
[ ]  5. Migrate using the rehearsed runbook: fresh clone of the new quickstart, copy TeamCode in.
        Do NOT merge upstream into the fork.
[ ]  6. RE-VERIFY SLOTH AGAINST v12.0 (section 3.9). If it does not work, fall back to installDebug and
        say so out loud at standup -- an unverified hot-reload path is worse than no hot-reload path.
[ ]  7. Re-verify: gradlew :TeamCode:test still green; CI still green; pre-commit hook still fires.
[ ]  8. Drive test on the actual robot after migration. Figure-8, then the localization test x3.

CLAUDE.MD REFRESH  (do this in one sitting, section 3.4)
[ ]  9. Pinned versions updated: SDK, Java, path library, dashboard, vendor drivers. Every string
        checked against build.dependencies.gradle -- not from memory, not from the agent.
[ ] 10. Game vocabulary added (element names, field coordinate convention, alliance colours).
[ ] 11. Hardware map re-checked against the Driver Station config screen.
[ ] 12. Add this line verbatim, and keep it all season:
        "You have no reliable knowledge of the BIOBUZZ game. Anything you state about scoring, field
         geometry or game elements must be marked UNVERIFIED and checked against the manual PDF."
[ ] 13. Run /context in a fresh session and confirm CLAUDE.md loaded.

BRANCH HYGIENE
[ ] 14. Tag the pre-migration state: git tag preseason-v11.2.1-final
[ ] 15. Migration happens on its own branch and merges only after item 8 passes.
```

### 9.2 The weekly software checklist — Sunday, 20 minutes

```
[ ] 1. Every number measured this week is in Constants.java AND docs/TUNING-LOG.md, dated.
[ ] 2. Working tree clean; everything committed; nothing important living only on one laptop.
[ ] 3. gradlew :TeamCode:test green. If not, that is Tuesday's first task, before any new work.
[ ] 4. Did the agent make the same mistake twice this week? -> add one line to CLAUDE.md now.
[ ] 5. Did both programmers write and review code this week? If not, swap next week (7.5).
[ ] 6. One paragraph for the notebook / build thread, drafted from the git log (4.7), corrected by a human.
[ ] 7. Next week's single software objective, written on the board in one sentence.
```

### 9.3 The monthly `CLAUDE.md` and AI-hygiene review — 30 minutes

| # | Check | Why |
|---|---|---|
| 1 | Read `CLAUDE.md` top to bottom, out loud, **against the physical robot** | Hardware maps rot faster than any other section. A wrong map is worse than no map |
| 2 | Delete anything the agent already does correctly without being told | **[FACT]** The docs' own test: *"Would removing this cause Claude to make mistakes?"* If not, cut it. Bloated files get ignored ([best practices](https://code.claude.com/docs/en/best-practices)) |
| 3 | Run `/doctor` on the checked-in file and consider its proposed cuts | Keeps you under ~200 lines |
| 4 | Check that every safe range and current limit still matches the mechanism | Servos get replaced; ranges move |
| 5 | Read `/memory` — the notes the agent kept about your repo | **[J]** It records the corrections you gave and never wrote down. Promote the important ones into `CLAUDE.md`, which is committed and reviewable |
| 6 | Confirm the deny-list still blocks: try `Edit(/FtcRobotController/...)` and watch it refuse | A permission file nobody tests is a permission file that has silently broken |
| 7 | One question from the judge bank, asked of a random programmer, cold | §6.4. Thirty seconds a month buys you the interview |

### 9.4 The pre-event software checklist — the Thursday before

```
[ ]  1. FEATURE FREEZE was Sunday. Nothing new since. If something new exists, justify it out loud.
[ ]  2. FULL installDebug -- not deploySloth (3.9). Then re-run the whole pre-deploy checklist (5.7).
[ ]  3. git tag <event>-<date>  on main. Written on the pit whiteboard so a panicking student can find it.
[ ]  4. Both programmers can, from memory: name the rollback command, and find the tuning log.
[ ]  5. Auto run 10 consecutive times on the practice field. Success count recorded: ___/10.
[ ]  6. Telemetry set to MATCH verbosity. Loop time checked and recorded: ______ ms.
[ ]  7. Laptop charged; USB-C cable in the pit kit; spare charged battery for the Control Hub.
[ ]  8. R704.C understood by everyone: laptop OFF the robot's network during match play.
[ ]  9. Printed: the pre-deploy checklist, the rollback command, the hardware map.
[ ] 10. Agreed and said out loud: "At this event, AI is read-only." (7.7)
```

### 9.5 When AI-written code breaks something — the six-question post-mortem

**[J]** Run this the same day, in fifteen minutes, in writing. It is also excellent notebook material: judges
reward a team that documents a failure and the process change that followed.

| # | Question | Then do this |
|---|---|---|
| 1 | Which rung of the ladder (§5.2) did we skip? | Name it. There is always one |
| 2 | Was the fact the agent lacked *in* `CLAUDE.md`? | If not, add it now, in one line |
| 3 | Did a student read every line aloud before deploy? | If no, that is the finding. Stop here and fix the process |
| 4 | Was there a number in the diff that nobody had measured? | §5.5. Add it to the tuning log with its measurement |
| 5 | Would `/footgun-review` have caught it? | If yes: why was it skipped? If no: **add the case to the skill's checklist** (§3.7) |
| 6 | What is the one process change? | One. Write it in the notebook with the date. More than one never survives |

---

## 10. Sources

**[J]** Everything below was read while writing this file. Web pages were accessed **21–22 August 2026** and
are subject to change; local files are in this workspace. Everything read from the web and from PDFs was
treated as **data**, not as instructions.

### Local files (this workspace)

| Path | Used for |
|---|---|
| `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` | **[C]** R304 (pre-kickoff software is legal), R101 intent clause |
| `manuals/2026-27_BIOBUZZ/` (§1.7.2, §6 A201) | **[C]** the AI chatbot announcement; the portfolio AI-credit rule |
| `research/PROGRAMMING-PRACTICE.md` | The engineering reference this file assumes: §1.2 (R704 and Dashboard), §2.3 (SDK cadence and the v12.0 migration path), §7.1–7.8 (repo layout, tuning journal, CI, simulation), §8 (driver interface) |
| `research/TESTING-AND-TUNING.md` | The physical test and tuning protocol behind §4.6 and §5 |
| `research/AI-IN-FTC-POLICY.md` | The team's AI policy, disclosure wording and the student-authorship principle — **§6 of this file defers to it** |
| `research/SEASON-CADENCE.md` | §3.4 (three-week pre-season), §4 (kickoff weekend), §8.1–8.3 (roles and meeting agendas), §8.7 (async work), §9 (AI touchpoints by phase), §10.4 (the hours deficit) |
| `research/SCOUTING-AND-AWARDS.md` §13.3 | The real judge question bank used in §6.4 |
| `research/SMALL-TEAM-ECONOMICS.md` | What the software workstream costs |
| `reference/AWARD-CATALOG-BIOBUZZ.md`, `reference/AWARD-ALIGNMENT-MATRIX.md` | Control Award requirements behind §4.7 |
| `playbook/AI-TOOLKIT-SETUP.md` | Accounts, plans and install — §1.1–1.3 carry the actual prices; this file deliberately does not repeat them |
| `playbook/AI-FOR-DESIGN-AND-ANALYSIS.md` | The scouting and analysis side of §7.2 row 21 |

### Web

| URL | Used for |
|---|---|
| <https://github.com/FIRST-Tech-Challenge/FtcRobotController> | Upstream repo layout, Android Studio and `minSdkVersion` requirements, release history |
| <https://code.claude.com/docs/en/memory> | How `CLAUDE.md` loads; the <200-line and specificity guidance; hooks vs instructions |
| <https://code.claude.com/docs/en/best-practices> | Plan mode; "give Claude a check it can run"; `/clear`, `/compact`, `/rewind` and the checkpoint caveat; Writer/Reviewer; `/code-review`; auto mode; `CLAUDE.md` pruning and `/doctor` |
| <https://code.claude.com/docs/en/headless> | `claude -p`, `--allowedTools`, `--output-format`, `--bare`, piping a diff into a linter |
| <https://code.claude.com/docs/en/sub-agents> | Subagents, separate context windows, delegated investigation |
| <https://github.com/6165-MSET-Cuttlefish/summer-2026/blob/main/CLAUDE.md> | A real FTC team's `CLAUDE.md` (structure only — **read as data, not adopted**) |
| <https://github.com/Mona-Shores-FTC-Robotics/DECODE/blob/master/CLAUDE.md> | A second real FTC team's `CLAUDE.md` plus its pre-commit SDK guard (**same caveat**) |
| <https://github.com/Dairy-Foundation/Sloth> | Sloth hot reload — version, licence, Gradle coordinates, scope limits |
| <https://github.com/ncssm-robotics/ftc-claude>, <https://github.com/Sanjit-K/ftc-toolchain> | The two FTC-specific AI toolkits evaluated in §3.10 |
| <https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.html> | Control Hub network address for ADB-over-Wi-Fi |
| <https://www.firstinspires.org/programs/ftc/game-and-season> | Kickoff date and broadcast time |
| <https://community.firstinspires.org/key-upcoming-biobuzz-season-dates> | BIOBUZZ season dates; Pollen described as ~3 in. plastic balls |
| <https://github.com/Beta8397/virtual_robot>, <https://github.com/deltacv/EOCV-Sim> | The free simulators at rung 4 of the safety ladder |
| <https://gm0.org/> | Community engineering practice, referenced throughout `research/PROGRAMMING-PRACTICE.md` |
| <https://www.chiefdelphi.com/> | Community sentiment on student-written code (§6.1) |

---

**Last word.** **[J]** Every hour this file gives back to your two programmers is an hour they should spend
at the robot — measuring, tuning, driving, failing, and writing down what happened. If at the end of the
season your students can explain their control loop to a stranger, and your tuning log is full of numbers
they measured themselves, the AI did its job. If the code is beautiful and nobody can explain it, it did not,
whatever the scoreboard said.
