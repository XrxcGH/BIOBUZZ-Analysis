<!--
  ============================================================================
  STANDING MEETING AGENDA + NOTES — ONE FILE PER MEETING
  ============================================================================
  WHERE IT LIVES:  meetings/YYYY-MM-DD.md

  TIME BUDGET:  5 minutes at the end of the meeting. Not more.
  SCRIBE:       rotates every meeting. Everyone writes; nobody becomes the
                bottleneck; everybody learns what the record needs to contain.

  THIS FILE HAS TWO JOBS:
    1. Run the meeting (the agenda half, sections A-E). Follow it; it ends on time.
    2. Be portfolio input (the log half, sections 1-7). At the end of the month
       you point Claude at meetings/ and decisions/ and it drafts the page:
       tools/ai/PROMPTS-portfolio.md PF1.

  THE AGENDA IS ADAPTED FROM  research/SEASON-CADENCE.md section 8.2, which has
  the reasoning, the Saturday variant, and the phase-by-phase content table.
  Two rules from there that make it work:
      - the robot touches the FIELD every meeting, even if it is broken
      - the meeting ENDS ON TIME  (small teams burn out in October and have
        nothing left in January)

  A201 PII RULE: first names and last initials only, everywhere, including
  photo captions and file names. "Maya R.", never "Maya Rodriguez".
  ============================================================================
-->

# Meeting — <YYYY-MM-DD> (<Weekday> / <Saturday>)

| | |
|---|---|
| **Start / End** | <18:30> – <21:30> (planned) · <actual> |
| **Scribe** | <First L.> |
| **Present** | <First L., First L., First L.> (<n> students, <n> mentors) |
| **Absent** | <First L. — reason, and what they own that is now blocked> |
| **Season phase** | P0 pre-season / P1 kickoff / P2 strategy / P3 prototyping / P4 CAD-freeze / P5 build / P6 tuning / P7 readiness / P8 event-to-event |
| **Days to next gate** | <n> days to <gate: first event / freeze date / portfolio deadline> |
| **Today's ONE objective** | <a single sentence. If you cannot name one, the meeting has no plan.> |

---

## THE AGENDA

### A. Standup — 10 min, standing, at the gate board
*45 seconds each. Did / doing / blocked. **No problem-solving in standup** — a
blocker gets a name and a time, not a discussion.*

| Who | Did since last time | Doing today | Blocked by |
|---|---|---|---|
| <First L.> | | | |
| <First L.> | | | |
| <First L.> | | | |

Coach reads the next gate date aloud: **<gate> is in <n> days.**

### B. Rules delta — 10 min, **Thursdays only** (skip other days)
*Team Updates post every Thursday from Kickoff (12 Sep 2026) until two weeks
before Championship (BIOBUZZ §1.7.3). Game Q&A answers post from each Monday
and close Thursday 5:00 p.m. ET (§1.7.4).*

- Team Update **#<n>** reviewed by <First L.> — changes: <none / list rule ids>
- Q&A answers reviewed — relevant to us: <none / list>
- **Does anything here change our robot, our auto, or our scoring math?** <yes/no + what>
- New rule ambiguity for our Q&A candidates list: <none / the question>
- Files that need updating as a result: <reference/CONSTRUCTION-RULES-R.md, tools/ai/inspection-checklist.template.md, none>

*(Prompt: `tools/ai/PROMPTS-strategy.md` S7 does the diff for you.)*

### C. Focus block — 2 hours, at most TWO parallel workstreams
*Phones in a box. Named owner on each stream. The coach floats and unblocks; the
coach does not do the work.*

| Stream | Owner | Goal for today | Result at the end |
|---|---|---|---|
| 1 | <First L.> | <...> | <...> |
| 2 | <First L.> | <...> | <...> |

### D. Field block — 20 min, **mandatory once a robot exists**
*The robot touches the tiles every meeting. Even broken. Drive practice, a
measured test, or an auto run — something on the field.*

- What we ran: <...>
- What we measured: <the number>
- Battery voltage at start / end: <n> V / <n> V
- Anything that broke: <...>

### E. Log and close — 20 min
*Photos taken → notes written → next task named → clean up → end on time.*

- Photos taken this meeting: <n> (filenames: `media/<YYYY-MM-DD>-<subject>.jpg`)
- Each stream names its ONE top task for next meeting → section 6 below.
- Room cleaned, tools accounted for, batteries on charge: ☐

---

## THE LOG *(this half becomes the portfolio)*

### 1. What we did today

*One short paragraph per workstream. Plain language, students' voice, numbers
where there are numbers. This is the raw material for PF1.*

**<Workstream / mechanism>** — <what we did, what we measured, what we learned>

**<Workstream / mechanism>** — <...>

### 2. Numbers measured today

*Every number gets a unit and a method. A number with no method is not evidence.*

| What | Value | Unit | How measured | Where it is logged |
|---|---|---|---|---|
| <e.g. intake cycle time> | <5.4> | s | mean of 10 stopwatch trials | `mechanisms/intake/log.md` |
| <e.g. lift hold current> | <1.8> | A | Driver Station telemetry, 30 s hold | `docs/TUNING-LOG.md` |

### 3. Decisions made today

*Anything that changes what we build, buy, or run. Every one gets a decision-log
file: `decisions/YYYY-MM-DD-<slug>.md` from `tools/ai/decision-log.template.md`.*

| Decision | Owner | Decision-log file created? |
|---|---|---|
| <...> | <First L.> | ☐ `decisions/<...>.md` |

*If a decision was made and no file exists by the end of the week, it did not
happen as far as the portfolio is concerned.*

### 4. Problems found

| Problem | Severity (blocks-us / slows-us / annoying) | Owner | Next step |
|---|---|---|---|
| <...> | | <First L.> | <...> |

### 5. Judge-question drill — 2 min
*Two random questions from the judging question bank; two students answer. This
is 2 minutes a meeting and it is the entire preparation for the Initial
Interview. `tools/ai/PROMPTS-portfolio.md` PF7 runs the drill.*

| Question asked | Who answered | How it went (1 line) |
|---|---|---|
| <...> | <First L.> | <...> |
| <...> | <First L.> | <...> |

**Thing to say differently next time:** <...>

### 6. Next meeting

| Stream | Top task | Owner | Needs first |
|---|---|---|---|
| 1 | <...> | <First L.> | <part arriving / a decision / nothing> |
| 2 | <...> | <First L.> | <...> |

**Anything we must ORDER before next meeting:** <part, vendor, SKU, price — then
add the row to `tools/bom/BOM.template.csv`. Lead times are the silent killer.>

### 7. Attendance and hours *(Sustain Award input)*

| | |
|---|---|
| Student-hours this meeting | <n students × n hours = n> |
| Cumulative student-hours this season | <n> |
| Outreach or fundraising activity today | <none / what, and it gets its own `outreach/` entry> |

---

<!-- ==========================================================================
     SATURDAY VARIANT — replace sections A-E with this on long days.
     Full reasoning in research/SEASON-CADENCE.md section 8.3.

       0:00 – 0:15   Standup + gate board + set the day's ONE objective
       0:15 – 2:15   Focus block A — the hardest thing, while everyone is fresh
       2:15 – 2:30   Break
       2:30 – 4:00   Focus block B
       4:00 – 4:45   LUNCH — eat together, no work. This is the team building.
       4:45 – 6:15   Focus block C  (from week 6 on, this is DRIVER PRACTICE,
                     non-negotiable)
       6:15 – 6:45   FULL-TEAM DEMO — every workstream shows the whole team what
                     it built. This is the only reliable defence against two
                     students building incompatible things for three weeks.
       6:45 – 7:15   Log, photos, portfolio paragraphs
       7:15 – 7:30   Clean up + plan next week's meetings
     ========================================================================== -->

<!-- ==========================================================================
     EVENT-DAY VARIANT — use tools/ai/match-day-runbook.template.md instead.
     After the event, come back and file a debrief as a normal meeting note
     with these extra sections:
       - What broke, and the fix
       - What the judges asked (verbatim, as best we remember)
       - The A212 judging feedback form -> tools/ai/PROMPTS-portfolio.md PF8
       - Results pulled:  fetch_events.py matches --source scout --season 2026 \
                            -e <CODE> -t <our number>
     ========================================================================== -->

<!-- ==========================================================================
     MONTHLY, ~30 MINUTES: the portfolio pass.
       Point Claude at meetings/ and decisions/ for the month and run
       tools/ai/PROMPTS-portfolio.md PF1. It drafts; a student edits and
       fact-checks every claim against the logs. That is the whole system:
       the portfolio is an EXPORT of this file, not a writing project in February.
     ========================================================================== -->
