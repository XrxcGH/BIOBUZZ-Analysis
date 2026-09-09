# PROMPTS — Programming

Copy-paste prompt library for the software workstream. Every prompt is
**self-contained**: it carries its own constraints, so it works even if
`CLAUDE.md` did not load or you are in a fresh session.

**How to use.** Fill the `<…>` placeholders. Paste the whole block, fences and
all. Read the answer before you run it. If a prompt asks for a citation and you
get none, the answer is not usable — say "you did not cite anything; try again
or tell me you don't know."

**Companion files**
- Why these work, and the eight highest-leverage uses: `playbook/AI-FOR-PROGRAMMING.md`
- Repo setup, `.claude/settings.json`, hooks, skills: `playbook/AI-TOOLKIT-SETUP.md` §3–§5
- What the rules allow: `research/AI-IN-FTC-POLICY.md` §8
- Legal software surface (R701–R711): `reference/CONSTRUCTION-RULES-R.md` §12.7
- Controls/tuning theory this assumes: `research/PROGRAMMING-PRACTICE.md` §6

**Standing rule for every prompt in this file:** if the answer contains a
PID gain, a servo position, an encoder ratio, a field coordinate, or a timing
constant that the model chose, it is wrong until a student measures it.

---

## Contents

| # | Prompt | Frequency | Risk if unverified |
|---|---|---|---|
| P1 | Bootstrap a subsystem | per mechanism | Medium |
| P2 | Pre-deploy footgun review | **every deploy** | **High** |
| P3 | Explain this code to me (learning) | weekly | None |
| P4 | Turn a symptom into a diagnosis plan | per bug | Medium |
| P5 | Write the tuning OpMode | per mechanism | Low |
| P6 | Log triage from `robotControllerLog.txt` | per event day | Low |
| P7 | Loop-time / performance audit | monthly | Medium |
| P8 | Unit tests for pure logic | per PR | None |
| P9 | Rule check: is this software legal? | before every event | **High** |
| P10 | Autonomous state-machine skeleton | 2–3× a season | Medium |
| P11 | Driver-experience review | before each event | Low |
| P12 | Control Award evidence extraction | 2× a season | Medium |
| P13 | Version/API check before writing code | per new API | **High** |
| P14 | Post-mortem a match failure | per failure | Medium |

---

## P1 — Bootstrap a subsystem

**When:** a new mechanism exists in metal and needs code.
**Do not** use this to design the mechanism. Use it after the geometry is fixed.

```
You are helping a small FTC team write robot code for the 2026-27 BIOBUZZ season.

Write a new subsystem class: <SubsystemName> in
TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/.

Hardware (this is the complete and only list — do not add devices):
<paste the rows from your CLAUDE.md hardware table for this mechanism>

What it must do, in plain language:
<e.g. "Hold one of four heights: STOWED, LOW, MID, HIGH. Driver presses a
button, it goes there and holds. It must not extend while the intake is down.">

Obey ALL of these, and tell me which ones constrained your design:
1. Constructor takes HardwareMap and does all hardwareMap.get() calls.
2. Exactly one periodic() method, called once per loop.
3. Public methods express intent, not raw power. Expose atTarget().
4. No gamepad reads, no telemetry.update(), no sleep(), no blocking of any kind.
   If it takes time, it is a state machine.
5. Every output clamped with Range.clip against a MAX from Constants.
6. Every setpoint clamped to a soft limit from Constants before it reaches hardware.
7. Units: inches for distance, degrees for angle, seconds for time, ticks only
   inside the subsystem. Every variable name carries its unit.
8. Any number you cannot derive from the hardware list above must be written as
   `= 0.0; // TODO MEASURE: <exactly what to measure and how>`.
   Do NOT invent PID gains, feedforward terms, servo positions or ratios.

Also produce:
- the new entries needed in config/Constants.java and config/HardwareNames.java
- a 5-line explanation, in language a first-year student understands, of how
  the control loop works
- one sentence naming the worst thing that happens physically if a constant is wrong.

Do not modify any existing file. Show me the diff you would apply.
```

---

## P2 — Pre-deploy footgun review *(run this every single time)*

**When:** before `installDebug` / `deploySloth`, always.
**This is the highest-value prompt in this file.** Make it a `.claude/skills/`
skill so it is one keystroke (see `playbook/AI-TOOLKIT-SETUP.md` §5).

```
Review the current uncommitted diff for FTC-specific bugs that break robots.
Run `git diff HEAD` yourself and review what it actually shows.

Check every one of these and report PASS / FAIL / N-A per line, with the file
and line number for every FAIL:

SAFETY
 1. Any motor or servo output that is not clamped before reaching hardware.
 2. Any servo setPosition() outside the SAFE RANGE recorded in CLAUDE.md.
 3. Any scaleRange() call, or any widening of a servo range.
 4. Any while/for loop in a LinearOpMode without opModeIsActive() or
    !isStopRequested() in its condition.
 5. Any new mechanism motor without a current limit / over-current check.
 6. Any code path that moves a mechanism during init (before START is pressed).

CORRECTNESS
 7. Unit mismatches: inches vs mm, degrees vs radians, ticks vs inches,
    seconds vs milliseconds. Check every arithmetic expression that mixes
    two variables whose names imply different units.
 8. Integer division where a fraction was intended.
 9. Sign/direction errors: a motor direction flipped without the paired
    encoder or feedforward sign being flipped.
10. Any hardwareMap.get() with a string literal instead of a HardwareNames constant.
11. Any numeric literal outside Constants.java other than 0 or 1.
12. State machines with a state that has no exit transition.

PERFORMANCE / RELIABILITY
13. sleep(), Thread.sleep(), or any blocking call inside a subsystem or a
    teleop loop.
14. Any per-loop allocation (new object, string concat, boxing) in a hot path.
15. Bulk caching not enabled, or a hub read that defeats it.
16. Anything that adds an I2C read to the main loop.

RULES (BIOBUZZ)
17. Any dashboard / FTControl Panels / third-party telemetry path not gated by
    COMPETITION_MODE  (R704.D prohibits these on the RC network).
18. Anything that requires a laptop connected to work (R704.C).

Then: name the SINGLE most likely way this diff breaks the robot on the field,
and the cheapest bench test that would catch it before we go to the field.
Do not fix anything yet. Report first.
```

---

## P3 — Explain this code to me *(the learning prompt)*

**When:** any time a student is about to own code they did not write. This is the
prompt that protects you in a judge interview — see `research/AI-IN-FTC-POLICY.md` §4.

```
I am a student on an FTC team. Explain <file / method / block> to me as if I
will be asked about it by a competition judge tomorrow.

Structure your answer:
1. What problem does this code solve, in one sentence, no jargon.
2. Walk through it line by line, in order, in plain language.
3. For every constant and every formula: where did that number come from, and
   what physically happens if it is 2x too big or 2x too small?
4. Name the two design alternatives we did NOT take, and one honest reason each
   was rejected.
5. Ask me three questions to check I actually understood it. Do not give me the
   answers. Wait for mine, then tell me what I got wrong.

If any part of this code is something I would not be able to defend, say so
plainly and tell me what I need to learn first.
```

---

## P4 — Symptom → diagnosis plan *(do not let it guess a fix)*

**When:** something is wrong on the robot and you do not know why.

```
Our robot has this symptom:
<exact symptom, e.g. "the lift drifts down ~2 inches over 10 seconds when
holding HIGH, but only when the battery is below about 12.0 V">

Context:
- Repo: <paste relevant subsystem file, or tell me to read it>
- What we changed most recently: <...>
- What we have already ruled out: <...>
- Hardware: <motor, gearbox, spool diameter, load>

Do NOT propose a code fix yet.

Instead:
1. List every hypothesis that could produce this exact symptom, mechanical and
   electrical as well as software. Rank them by prior probability for an FTC
   robot, and say why.
2. For each of the top 4, give me ONE experiment that DISTINGUISHES it from the
   others — what to do, what to measure, what number would confirm vs refute it.
   Each experiment must take under 10 minutes with a robot on blocks.
3. Tell me which single experiment to run first because it splits the hypothesis
   space most evenly.
4. Tell me what telemetry or logging I should add before running it.

I will run them and come back with numbers.
```

---

## P5 — Write the tuning OpMode

```
Write a tuning OpMode for <mechanism> at
TeamCode/src/main/java/org/firstinspires/ftc/teamcode/tuning/<Name>Tuner.java.

It is a measuring instrument, not a demo. It must:
- be a TeleOp OpMode in group "tuning", clearly named
- let the driver step the setpoint with the D-pad and hold with a bumper
- print to Driver Station telemetry ONLY (no dashboard, no third-party panel —
  R704.D prohibits FTC Dashboard and FTControl Panels on the RC network, so
  this must work with nothing but the Driver Station):
    setpoint, measured position, error, output command, motor current,
    battery voltage, and loop time in ms
- write a CSV line per loop to a timestamped file on the Control Hub under
  /sdcard/FIRST/tuning/ so we can pull it with adb and plot it later
- stop cleanly and close the file on OpMode stop
- never move the mechanism outside the soft limits in Constants
- refuse to start (telemetry error + no motion) if any required device is missing

Then write me a numbered PROCEDURE, on paper, that a student follows to tune
this mechanism with this OpMode: what to set, what to watch, what "good" looks
like numerically, and when to stop. Include the failure signature of each
common mistake (too much P, too much D, missing feedforward, backlash).
```

---

## P6 — Log triage

```
Read logs/robotControllerLog.txt (I have already pulled it with
`adb pull /sdcard/robotControllerLog.txt logs/`).

Produce:
1. A timeline table of every ERROR and WARN, with timestamp, the subsystem it
   came from, and a one-line plain-English meaning.
2. Any occurrence of: hub disconnection, I2C failure, USB reset, ESD/brownout
   indication, watchdog, "Problem with Expansion Hub", or an OpMode crash
   stack trace. Quote the exact log line for each.
3. Loop-time statistics if the log contains them: min, median, p95, max, and
   where the worst spikes are.
4. Your ranked list of the top 3 things this log says are wrong with our robot,
   with the evidence line number for each.
5. For anything you are NOT sure about, say "uncertain" and tell me what
   additional logging would settle it. Do not speculate as if it were fact.

Do not change any code.
```

---

## P7 — Loop-time / performance audit

```
Audit our TeleOp loop for anything that costs time. Read the main TeleOp OpMode
and every subsystem it calls.

Report a table: location | what it costs | estimated cost | how to fix.
Look specifically for:
- hardware reads not covered by bulk caching (setBulkCachingMode)
- I2C device reads in the main loop (IMU, distance sensors, colour sensors)
- object allocation, string concatenation, autoboxing, or format() per loop
- telemetry.addData with computed strings on every loop rather than every Nth
- vision processing on the main thread
- any sleep(), busy-wait, or blocking call
- repeated hardwareMap lookups outside the constructor

Then tell me, ranked, the three changes that would buy the most milliseconds
per loop, with the estimated saving and the risk of each. Cite the FTC SDK
behaviour you are relying on where relevant — if you are not sure the SDK
behaves that way in version <11.2.1>, say so.
```

---

## P8 — Unit tests for pure logic

```
Write JUnit 5 tests in TeamCode/src/test/java/ for <class or methods>.

Rules:
- Test only pure functions — anything with an SDK import cannot be unit-tested,
  and if the logic I asked about has SDK imports, your FIRST answer should be
  how to extract the pure part into util/MathFunctions.java.
- Cover: the normal case, both boundaries, one value outside each boundary,
  zero, negative, and the unit-conversion round trip (in -> ticks -> in).
- Every assertion gets a comment saying what physical situation it represents.
- Use exact expected values I can verify by hand, not values you computed by
  running the code in your head.

Then run `./gradlew :TeamCode:test` and show me the result. If a test fails,
tell me whether the TEST or the CODE is wrong, and why you believe that.
```

---

## P9 — Rule check: is our software legal? *(before every event)*

```
Check our robot software for compliance with the BIOBUZZ 2026-27 rules.
Read reference/CONSTRUCTION-RULES-R.md
section 12.7 for the rule text, and the V0 manual text at
manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt if you need the exact wording.
Do not rely on memory of prior seasons — the rules were renumbered for BIOBUZZ.

For each of R701 through R711, plus R202.C, tell me:
  rule id | what it requires | how our repo/robot complies | evidence (file:line
  or "requires physical check") | PASS / FAIL / NEEDS-HUMAN-CHECK

Pay particular attention to:
- R704.D: FTC Dashboard and FTControl Panels are named as PROHIBITED on the
  Robot Controller network. Find every code path that can start one and confirm
  it is gated off in competition mode.
- R704.C: nothing may require a laptop connected during a match.
- R702 / R708: which coprocessors and cameras we actually initialise in code,
  and whether each is on the legal list.
- R705: device naming convention in any code or config we control.

Quote the rule id in every finding. If a rule's text is a placeholder or
deferred in V0, say so rather than guessing — several sections are not final
until Kickoff on 12 September 2026.
```

---

## P10 — Autonomous state-machine skeleton

```
Design the state machine for this autonomous routine. Code second, design first.

Routine, in plain language: <...>
Time budget: <N> seconds. Starting position: <...>.
Mechanisms available and their timings (measured, from our tuning log):
<mechanism: time from X to Y = N seconds>

Step 1 — before any code, give me:
 (a) the state diagram as a table: state | entry action | exit condition |
     next state | timeout | what we do if the timeout fires
 (b) the total time budget summed across the happy path, compared to <N> seconds
 (c) every state where a failure would leave the robot in a position that costs
     us points or a penalty, and what the safe fallback is
 (d) the single riskiest state, and why

Step 2 — after I approve the table, write the code, using our existing
subsystems' atTarget() methods for transitions. No sleep(). No blocking.
Every state has a timeout. The routine must be safe to abort at any moment.

Do not invent any distance, angle or timing constant. Use TODO MEASURE markers
and tell me the procedure to measure each one.
```

---

## P11 — Driver-experience review

**Context:** driver-facing software is frequently worth more than mechanism speed
(`research/PROGRAMMING-PRACTICE.md` §8).

```
Review our TeleOp from the DRIVER's point of view, not the programmer's.

Read the TeleOp OpMode and answer:
1. Draw the full control map as a table: control | action | is it a toggle, a
   hold, or a momentary? | what happens if it is pressed at the wrong time?
2. Which actions require the driver to remember state that is not displayed to
   them? List each one — these are the ones that lose matches.
3. Which two controls are physically hardest to press simultaneously, and does
   any real sequence require that?
4. What happens on: a mid-match hub reset, a mechanism jam, a dropped game
   element, and pressing the scoring button while the mechanism is already moving?
5. Propose the smallest set of changes that would reduce driver cognitive load,
   ranked by benefit-per-line-of-code. For each, say what could go wrong.

Do not implement anything yet. Our drivers will pick.
```

---

## P12 — Control Award evidence extraction

```
Read our repo (TeamCode/, docs/TUNING-LOG.md, tuning/) and produce a factual
inventory of our control system for the Control Award, per the criteria in
reference/AWARD-ALIGNMENT-MATRIX.md
section M3 and research/SCOUTING-AND-AWARDS.md section 12.

Produce a table with one row per claim:
  claim | file:line or log entry that PROVES it | is this a sensor, an
  algorithm, or an autonomous behaviour? | one-sentence student explanation

Rules for you:
- Every row MUST cite a real file:line or a real dated entry in TUNING-LOG.md.
  If you cannot cite it, do not write the row — instead list it separately under
  "claims we cannot currently evidence".
- Do NOT write marketing language. Judges ask follow-ups; a claim we cannot
  defend is worse than no claim.
- Flag anything a student on our team probably cannot explain, so we can either
  learn it or drop it.

Output the table, then the gap list, then the three highest-value experiments we
could run in the next two weeks to close the biggest gaps.
```

---

## P13 — Version / API check *(run BEFORE writing code against an unfamiliar API)*

**Why:** hallucinated SDK methods are the single most common wasted hour.

```
I want to use <API / class / method, e.g. "the goBILDA Pinpoint driver's
setOffsets method"> with FTC SDK <11.2.1> and <library + version>.

Before writing any code:
1. Tell me whether that API exists in exactly those versions. If you are not
   certain, say "not certain" — do not guess a signature.
2. If you can verify it, cite where: the javadoc URL, the GitHub file path and
   line, or the vendor documentation URL. Fetch the page if you can.
3. Give me the exact signature, the units of every parameter, and the units of
   the return value.
4. Tell me the two most common mistakes people make with this API.
5. Only then, write the smallest possible example that compiles against our
   pinned versions.

If the API does not exist in our version, tell me what does exist instead. Do
not tell me to upgrade — upgrades are a human decision.
```

---

## P14 — Post-mortem a match failure

```
We had a failure in a real match. Help me write the post-mortem entry.

What happened: <...>
Match/time: <...>. What the drivers saw: <...>. What the robot did: <...>
Logs: logs/<file> (read it). Code state: commit <sha>.

Produce, in this order:
1. TIMELINE — what happened, second by second, using only evidence from the log
   and my description. Mark anything inferred as [inferred].
2. ROOT CAUSE — the mechanism of failure, not the trigger. Distinguish
   "the battery was low" (trigger) from "we have no voltage compensation" (cause).
3. WHY IT SURVIVED OUR TESTING — what test would have caught it, and why we
   didn't have it.
4. THE FIX — the smallest change that removes the root cause, and separately,
   the test that will keep it dead.
5. THE ENTRY — a dated Markdown block I can paste into docs/TUNING-LOG.md and
   later into our engineering portfolio, written in the students' voice.

Mark clearly anything you are not sure of. A post-mortem with a confident wrong
root cause is worse than none.
```

---

## Anti-prompts — things NOT to ask

| Don't ask | Why | Ask instead |
|---|---|---|
| "What PID gains should I use for a lift?" | It will give you plausible numbers that are wrong for your gearbox and load, and they will *almost* work, which is worse | P5 — the tuning OpMode and the procedure |
| "Write our whole autonomous" | You get code no student can defend; Control/Think/Design criteria all test defensibility | P10 — design table first, approve, then code |
| "Fix this bug" (with a symptom only) | It will change something plausible and you will not know if that was the cause | P4 — hypotheses and experiments first |
| "Is this legal?" (no manual) | Prior-season rule numbers are wrong for BIOBUZZ; it will confidently cite a DECODE rule id | P9 — points it at the actual local manual text |
| "Make the code better" | Unbounded refactors on a robot repo the week before an event | Name one specific property you want |
