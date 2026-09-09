<!--
  ============================================================================
  ENGINEERING DECISION LOG — ONE FILE PER DECISION
  ============================================================================
  WHERE IT LIVES:  decisions/YYYY-MM-DD-<short-slug>.md
      e.g.         decisions/2026-09-20-drivetrain-choice.md
                   decisions/2026-10-14-intake-roller-vs-claw.md

  WHY IT EXISTS (the honest version):
    The February portfolio panic exists because teams treat the portfolio as a
    WRITING PROJECT rather than an EXPORT FORMAT. If every decision produces one
    artefact at the moment it is made, in a fixed place and a fixed shape, the
    portfolio becomes an editorial pass over things that already exist.
    (research/SCOUTING-AND-AWARDS.md section 16.1)

  WHAT IT FEEDS:
    - Think Award criterion 1 — "evidence of use of the engineering process"
      and "comparing choices". This file IS that evidence.
    - Design Award criterion 4 — students must defend the design rationale.
    - The judge interview: this is what you re-read the night before.
    (reference/AWARD-CATALOG-BIOBUZZ.md, reference/AWARD-ALIGNMENT-MATRIX.md)

  THE FIVE RULES:
    1. WRITE IT BEFORE THE BUILD STARTS, not after. A decision log written
       afterwards is a justification, and judges can tell.
    2. Every entry names an OWNER — a student, by first name and last initial
       only (A201 PII: "use only first names and last initials").
    3. Options you rejected are worth more page space than the one you chose.
       "We compared" is the criterion; "we chose" is not.
    4. Numbers, not adjectives. If there is arithmetic, show it.
    5. Come back and fill in "What actually happened". An entry with an honest
       "we were wrong, here is what we learned" is worth more to a judge than
       three entries that all worked.

  BUDGET: about 20 minutes per decision. If it is taking an hour, the decision
  is too big — split it.

  AI USE: you may paste your notes and ask Claude to structure them into this
  shape (tools/ai/PROMPTS-design.md D5). You may NOT ask it to score the options
  or pick for you. A judge will ask a student why you chose it, and the answer
  cannot be "the AI said so." (research/AI-IN-FTC-POLICY.md section 8)
  ============================================================================
-->

# DEC-<NNN> — <One-line decision title, phrased as the question you answered>

| | |
|---|---|
| **Date decided** | <YYYY-MM-DD> |
| **Owner** | <First L.> |
| **In the room** | <First L., First L., mentor First L.> |
| **Subsystem / area** | <drivetrain / intake / lift / autonomous / strategy / budget / process> |
| **Status** | PROPOSED / **DECIDED** / REVISITED / REVERSED |
| **Reversibility** | EASY (< 2 h to undo) / MODERATE (a build day) / HARD (a rebuild) |
| **Cost of this decision** | $<n> and <n> build hours |
| **Supersedes** | <DEC-### or "none"> |
| **Superseded by** | <DEC-### or "none"> |

---

## 1. The problem

*What forced this decision? Two or three sentences. State the trigger and the
constraint. If a rule constrains it, cite the rule id.*

<...>

**Constraints that were fixed before we started:**
- <e.g. R503 caps us at 8 motors + 8 servos across all configurations; we had 4 left>
- <e.g. no mill; drill press, hand tools and one FDM printer>
- <e.g. 5 weeks to our first event>
- <e.g. $<n> left in the parts budget>

**What "good" would look like:** <the measurable outcome that would tell us we
chose right — a cycle time, a success rate, a weight, a build-hour count>

---

## 2. Options considered

*At least three. If you only had two, say why the third was ruled out before it
was written down — an option list of two is usually an option list of one.*

| # | Option | How it works, in one sentence | Actuators | Est. cost | Est. build hours | Main risk |
|---|---|---|---|---|---|---|
| A | <name> | <...> | <n motors, n servos> | $<n> | <n> | <...> |
| B | <name> | <...> | <n, n> | $<n> | <n> | <...> |
| C | <name> | <...> | <n, n> | $<n> | <n> | <...> |
| — | <option we rejected before evaluating> | <...> | — | — | — | **Ruled out because:** <...> |

---

## 3. Criteria and weights

*Agree these BEFORE scoring. Changing weights after you see the scores is how a
decision matrix becomes theatre.*

| Criterion | Weight | Why it matters to us | How we measured it |
|---|---|---|---|
| <e.g. Cycle time> | <n> | <...> | <stopwatch on the prototype, 10 trials> |
| <e.g. Build hours> | <n> | <we are 4 students> | <estimate from the build plan> |
| <e.g. Reliability> | <n> | <...> | <n consecutive cycles without a jam> |
| <e.g. Actuator cost> | <n> | <R503 budget is our binding constraint> | <count> |
| | **<total>** | | |

---

## 4. Evidence

*This is the section judges actually read. Every claim gets a source.*

| Claim | Evidence | Source |
|---|---|---|
| <e.g. "Option A cycles in 5.4 s"> | 10 timed trials, mean 5.4 s, sd 0.6 s | `mechanisms/intake/log.md` 2026-10-11 |
| <e.g. "Option B needs a servo we do not have"> | R502 power calc = 9.1 W at 6 V, over the 8 W cap | `decisions/2026-10-14-servo-check.md` |
| <e.g. "Similar mechanisms fail at the roller mount"> | <team/season/source> | <URL or file> |
| <...> | <...> | <...> |

**Prototypes or tests we ran:** <what, when, for how long, what we measured>

**What we could NOT measure, and how that affects confidence:**
<be honest — this sentence is worth more than a page of confident prose>

---

## 5. Scores

*Students fill this in, out loud, together. Do not let one person score alone
and do not let AI score.*

| Criterion | Weight | A | B | C |
|---|---|---|---|---|
| <criterion> | <w> | <1-5> | <1-5> | <1-5> |
| <criterion> | <w> | | | |
| <criterion> | <w> | | | |
| **Weighted total** | | | | |

**Sensitivity:** *would the result flip if any single score moved by 1?*
<yes/no — and if yes, which cell. If yes, you do not really have a decision yet;
go get more evidence on that cell.>

---

## 6. Decision

> **We chose <Option X>.**

**The one-sentence reason a student says out loud in an interview:**
> <...>

**What we gave up by choosing it:** <the real trade-off, named plainly>

**Dissent:** *did anyone disagree? Record it. A recorded dissent that turns out
to be right is the best possible entry in this file.*
<name (first + last initial) and their argument, or "none">

**Decided by:** <First L.> · **Agreed by:** <First L., First L.>

---

## 7. What we do next

| # | Action | Owner | By when | Done? |
|---|---|---|---|---|
| 1 | <...> | <First L.> | <date> | ☐ |
| 2 | <...> | <First L.> | <date> | ☐ |
| 3 | <update BOM row / order part / update CLAUDE.md hardware table> | <First L.> | <date> | ☐ |

**Files this decision changes:** <BOM.csv row, CLAUDE.md hardware table,
Constants.java, the inspection checklist, the season plan>

---

## 8. What actually happened

*Come back and fill this in. Set a reminder. This section is the difference
between a decision log and a diary.*

| Filled in on | <YYYY-MM-DD> |
|---|---|

**Did it work?** <what we measured against the "good" definition in section 1>

**What surprised us:** <...>

**Would we choose the same again?** YES / NO / YES-BUT
<one honest paragraph>

**If we revisited this:** <DEC-### link, or "not revisited">

**The lesson, in one sentence, that transfers to the next decision:**
> <...>

---
---
---

<!-- ==========================================================================
     WORKED EXAMPLE — delete this whole block when you copy the template.
     Shown so a new student can see what "done" looks like. The numbers are
     ILLUSTRATIVE PLACEHOLDERS, not real data from any team.
     ========================================================================== -->

# DEC-007 — Roller intake or claw for ground pickup?

| | |
|---|---|
| **Date decided** | 2026-10-14 |
| **Owner** | Maya R. |
| **In the room** | Maya R., Devon T., Sam K., mentor Chris L. |
| **Subsystem / area** | intake |
| **Status** | **DECIDED** |
| **Reversibility** | MODERATE (one build day to swap the mount plate) |
| **Cost of this decision** | $34 and ~14 build hours |
| **Supersedes** | none |

## 1. The problem
Our drivetrain works and we can drive to a game element, but we cannot pick one
up. We have 5 weeks to our first event and 4 motors / 6 servos left under R503.
Whatever we build has to be tuned and driver-practised, not just built.

**Constraints fixed before we started:** 4 motors + 6 servos remaining (R503);
drill press + FDM printer only; 5 weeks; $80 left in the parts budget.

**What "good" would look like:** pick up a game element from the floor in under
2.0 s, succeeding on at least 9 of 10 attempts, with a driver who has practised
for 30 minutes.

## 2. Options considered
| # | Option | How it works | Actuators | Est. cost | Est. hours | Main risk |
|---|---|---|---|---|---|---|
| A | Compliant roller | Two counter-rotating compliant wheels sweep the element in | 1 motor | $28 | 10 | Only works at one approach angle |
| B | Servo claw | Two printed fingers close on the element | 2 servos | $34 | 14 | Requires precise driver alignment |
| C | Roller + passive ramp | Roller feeds a gravity ramp to a hold position | 1 motor | $41 | 18 | Most parts, most time |
| — | Pneumatic gripper | — | — | — | — | **Ruled out:** R801 permits only manufacturer-sealed closed-air systems and prohibits generating pressure. Not viable. |

## 3. Criteria and weights
| Criterion | Weight | Why | How measured |
|---|---|---|---|
| Pickup success rate | 5 | A missed pickup costs a whole cycle | 10 trials on the prototype |
| Driver difficulty | 4 | 1 driver, limited practice hours | Sam K. attempts after 10 min practice |
| Build hours | 4 | 4 students, 5 weeks | Estimate from build plan |
| Actuator cost | 3 | R503 budget is binding | Count |
| | **16** | | |

## 4. Evidence
| Claim | Evidence | Source |
|---|---|---|
| Roller prototype picked up 9/10 from a square approach, 4/10 at 30° | 20 timed trials 2026-10-11 | `mechanisms/intake/log.md` 2026-10-11 |
| Claw picked up 10/10 but needed ±0.5 in alignment | 10 trials, measured with a taped floor grid | `mechanisms/intake/log.md` 2026-10-12 |
| A claw wrist would exceed R303 if bought as a COTS 2-DoF unit | R303 caps COTS components at 1 degree of freedom | `reference/CONSTRUCTION-RULES-R.md` §12.3 |

**Prototypes:** cardboard-and-tape roller (2 h), printed claw fingers v1 and v2 (5 h).
**Could not measure:** durability over 40 matches. We have no way to test that in
5 weeks, so both options carry unquantified wear risk.

## 5. Scores
| Criterion | W | A roller | B claw | C roller+ramp |
|---|---|---|---|---|
| Pickup success | 5 | 3 | 5 | 4 |
| Driver difficulty | 4 | 5 | 2 | 5 |
| Build hours | 4 | 4 | 3 | 2 |
| Actuator cost | 3 | 5 | 3 | 5 |
| **Weighted total** | | **66** | **57** | **63** |

**Sensitivity:** yes — if "pickup success" for A moved from 3 to 2, C wins. That
cell is the one we are least sure about, so we agreed to re-test A's angled
approach before committing the mount plate.

## 6. Decision
> **We chose Option A, the compliant roller, with a re-test gate on angled pickup.**

**The one-sentence reason:** it is the option a single driver can use reliably
under pressure, and it costs us one motor instead of two servos we will want later.

**What we gave up:** raw pickup precision, and the ability to place an element
gently rather than eject it.

**Dissent:** Devon T. argued for C, on the grounds that the ramp removes the
"hold position" problem entirely and we will pay for it later. Recorded.

**Decided by:** Maya R. · **Agreed by:** Devon T. (with dissent noted), Sam K.

## 7. What we do next
| # | Action | Owner | By when | Done? |
|---|---|---|---|---|
| 1 | Re-test angled pickup, 20 trials at 0/15/30° | Devon T. | 2026-10-16 | ☑ |
| 2 | Build the mount plate | Maya R. | 2026-10-19 | ☑ |
| 3 | Add `INTAKE` row to CLAUDE.md hardware table + HardwareNames.java | Sam K. | 2026-10-19 | ☑ |

## 8. What actually happened
| Filled in on | 2026-11-08 |

**Did it work?** Partly. Success rate on the robot was 8/10 square, 6/10 angled —
better than the prototype at angle, worse square. Pickup time 1.6 s, inside target.

**What surprised us:** the failure mode was not the roller, it was the element
bouncing back out because we had no hold position. Devon's dissent was right about
the mechanism, wrong about the timing — the ramp was a 3-hour add-on later, not an
18-hour rebuild.

**Would we choose the same again?** YES-BUT — same roller, but we would have
built the passive hold on day one instead of arguing about it.

**If we revisited this:** DEC-013 (passive hold ramp, 2026-11-02).

**The lesson:** when a dissenting option is a superset of the chosen one, build
the chosen one and keep the dissent as the next iteration — do not treat it as a
competing branch.
