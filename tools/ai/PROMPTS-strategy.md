# PROMPTS — Game Analysis and Strategy

Copy-paste prompt library for reading the game, choosing what to build, and
deciding what to do in a match.

---

## Read this before you use any prompt in this file

**[FACT]** Two independent public reports from FRC/FTC mentors say LLMs are
*empirically weak* at exactly this workstream. On Chief Delphi thread 519529
(April 2026), one participant reported an LLM picklist built from real scouting
data was **"worse than sorting by averages"**, and another observed that asked
for strategy advice it tells you "whatever strategy you come up with is
fantastic." The same thread reports LLMs being *strong* at tooling — scripts,
log parsing, profiling. (See `research/AI-IN-FTC-POLICY.md` §9.)

**[JUDGMENT] So every prompt in this file is built the same way:**

1. **Never ask "what should we do?"** Ask it to *enumerate*, to *compute*, to
   *argue the opposite*, or to *find what we missed*. Judgement stays with the
   students — which is also what Think criterion 1 and Design criterion 4 test.
2. **Force adversarial framing.** The default failure mode is agreeing with you.
   Several prompts below explicitly assign it the job of attacking your plan.
3. **Arithmetic, not opinion.** Where a question can be reduced to a scoring
   rate or an expected-value calculation, make it do the arithmetic and show it.
4. **Cite the manual.** Nothing about scoring is knowable from the model's
   training data — Sections 8–11 of the BIOBUZZ manual are placeholders until
   **Kickoff, 12 September 2026**. Point every prompt at the local files.

**Companion files**
- The full ranking protocol these prompts feed: `reference/STRATEGY-RANKING-PROTOCOL.md`
- Scoring-pattern taxonomy across seasons: `reference/SCORING-PATTERNS.md`
- Robot archetypes and their costs: `reference/ROBOT-ARCHETYPE-LIBRARY.md`
- Can we actually build it: `reference/ACHIEVABILITY-RUBRIC.md`, `reference/ACHIEVABILITY-FACTORS.md`
- Rule-edge precedent: `research/LOOPHOLE-CASEBOOK.md`
- Penalties: `reference/PENALTY-AND-ENFORCEMENT.md`
- Kickoff-day plan: `research/SEASON-CADENCE.md` §4

---

## Contents

| # | Prompt | When | AI is… |
|---|---|---|---|
| S1 | Kickoff manual ingest and scoring extraction | Kickoff day | strong (extraction) |
| S2 | Enumerate every scoring path (MECE) | Kickoff day | strong (enumeration) |
| S3 | Points-per-second arithmetic | Kickoff weekend | strong (arithmetic) |
| S4 | Red-team our strategy | before committing | strong (adversarial) |
| S5 | Rule-edge hunt (legal, not loophole abuse) | Kickoff week | medium |
| S6 | Achievability check against our real capacity | before committing | medium |
| S7 | Team Update diff watch | every Thursday | strong |
| S8 | Q&A answer digest | weekly | strong |
| S9 | Match strategy card generator | per event | medium |
| S10 | Penalty-risk audit of a plan | before each event | medium |
| S11 | "What does the winning robot look like?" from real data | Dec–Feb | medium |
| S12 | Devil's-advocate on a mid-season pivot | as needed | strong |

---

## S1 — Kickoff manual ingest and scoring extraction *(12 Sep 2026)*

```
The BIOBUZZ 2026-27 game manual has just been released. I have run
tools/ingest-manual.sh and the extracted text is at:
  <path to the new extracted .txt>

Read it. Then extract, with a page citation for EVERY line:

1. SCORING TABLE — every scoring action, its point value, when it can be scored
   (auto / teleop / endgame), and any cap or multiplier. One row per action.
2. RANKING POINTS — every RP, its exact threshold condition, and whether it is
   alliance-wide or per-robot.
3. MATCH STRUCTURE — period lengths, the exact transition rules, and what
   changes at each transition.
4. STARTING CONDITIONS — where robots start, what is preloaded, what is
   randomised, and when the randomisation is revealed.
5. PENALTIES — every MINOR and MAJOR foul, its point value, and its trigger.
6. THE R105 EXPANSION ENVELOPE — this was DEFERRED in V0 ("Sizing Constraints
   and more details will be released at Kickoff", V0 p. 68). Quote whatever it
   now says, exactly.
7. ANY OTHER PLACEHOLDER NOW FILLED — diff against
   research/BIOBUZZ-V0-STRUCTURE.md
   and list every section that changed from placeholder to real content.

Rules for you:
- Every single row cites a page number. No page number, no row.
- Quote the manual's exact wording for any threshold or number. Do not paraphrase
  a number.
- Where the text is ambiguous, say "ambiguous: <the two readings>" and add it to
  a list of candidate Q&A submissions. The Game Q&A opens 28 September 2026.
- Do not infer strategy yet. This prompt is extraction only.
```

---

## S2 — Enumerate every scoring path (MECE)

```
Using ONLY the scoring table you extracted in S1 (re-read it if needed), list
every distinct way an alliance can score points in a BIOBUZZ match.

Requirements:
- MECE: mutually exclusive, collectively exhaustive. If two paths overlap, split
  or merge them until they do not.
- Include the paths nobody will build: pure defence, pure support/feeding,
  endgame-only, auto-only, and any path that scores by DENYING the opponent.
  Contrarian options must appear.
- For each path give: the actions in sequence, the mechanisms required, the
  actuator count that implies (remember R503: 8 motors + 8 servos TOTAL), and
  the points per completed cycle.
- Mark each path's dependency on alliance partners: SOLO / NEEDS-COOPERATION /
  ONLY-WORKS-WITH-A-STRONG-PARTNER.

Then, separately, list every path you can find that is legal but that you expect
most teams to overlook, with the rule id that permits it.

Do NOT rank them. Do NOT recommend one. Ranking is the students' job and it uses
reference/STRATEGY-RANKING-PROTOCOL.md.
```

---

## S3 — Points-per-second arithmetic

**This is where AI is genuinely good: the arithmetic nobody wants to do.**

```
Compute the scoring rate for each of these strategies. Show every step.

Strategies: <paste the paths from S2 you want costed>
Match length and period split: <from S1>
Our measured or estimated cycle components — I will supply these, do not invent
any of them:
  travel time to <location>: <n> s
  acquire time: <n> s
  travel to score: <n> s
  score time: <n> s
  reliability (fraction of attempts that succeed): <0-1>

For each strategy produce:
1. Cycle time, and points per cycle.
2. Cycles available in the period, accounting for the first cycle starting from
   the starting position.
3. Expected points, including the reliability factor.
4. Sensitivity: how many points do we gain/lose per 1 second of cycle time
   improvement, and per 5 percentage points of reliability?
5. The BREAK-EVEN: what cycle time would this strategy need to beat <other
   strategy>?

Then a summary table sorted by expected points, and this sentence filled in:
"The cheapest single second to remove from our cycle is <where>, worth <n>
points per match."

Mark every input I flagged as an estimate. If the answer's ordering flips when
any single estimate moves 20%, say so in bold — that means we need to measure
that number before deciding anything.
```

---

## S4 — Red-team our strategy *(assign it the opposite job)*

```
You are the head strategist for the best team in our region, and you have just
been handed our plan. Your job is to beat us. Be specific and be harsh.

Our plan: <paste it>
Our robot's intended capabilities: <list>
The rules: read
  reference/CONSTRUCTION-RULES-R.md
  reference/PENALTY-AND-ENFORCEMENT.md
  and the current BIOBUZZ manual text.

Produce:
1. The three cheapest legal ways to reduce our scoring output, with the rule
   that makes each legal and the rule that would make it a foul if done wrong.
2. The single point in our cycle where a legal defensive robot costs us the most
   points, with the arithmetic.
3. What our plan assumes about our alliance partner. What happens to our
   expected score if we are paired with a robot that does nothing? Compute it.
4. The failure mode that would make our whole strategy worthless (a rule reading
   we got wrong, a mechanism that will not be reliable enough, a resource we do
   not have).
5. What we would have to see at our first event to know this plan was wrong —
   a specific, observable, falsifiable signal.

Do not soften anything. Do not end with encouragement. If the plan is good, say
which specific part is good and why; if it is not, say that first.
```

---

## S5 — Rule-edge hunt

**Boundary:** we are looking for *strategies the rules permit that teams
overlook*. We are **not** looking to "strategically circumvent" rules —
BIOBUZZ §3.3.1 says teams that do so "are not adhering to the Competition
Integrity Contract (CIC) and may be subject to mitigation."

```
Read the current BIOBUZZ manual text and
  research/LOOPHOLE-CASEBOOK.md
(which catalogues how prior-season rule edges were actually ruled on).

Find provisions in the CURRENT rules that permit something most teams will
assume is prohibited, or that leave a strategy open. For each, give:
  the rule id and exact quote | what it permits | why teams will miss it |
  the risk that a Q&A ruling or Team Update closes it | how we would find out

Then, separately and clearly labelled, list anything that looks like an edge but
that section 3.3.1 (spirit of the rules / CIC) would likely treat as
circumvention. We do not pursue those, and I want to know which is which.

For each real edge worth pursuing, draft the exact Game Q&A question we should
submit to get it confirmed in writing. Q&A opens 28 September 2026 at 12:00 ET;
questions are answered starting each Monday and close Thursday 5:00 p.m. ET.
Write questions that are answerable YES or NO and quote the rule id.
```

---

## S6 — Achievability check against our real capacity

```
Score this strategy for ACHIEVABILITY by OUR team, using the rubric in
  reference/ACHIEVABILITY-RUBRIC.md
Read that file and use its actual dimensions and scale — do not invent your own.

Our real capacity (be brutal with me if these are inconsistent):
- Students: <n>. Hours per week each, realistically: <n>
- Weeks until our first event: <n>
- Machine shop: <what we actually have>
- Programming experience: <describe>
- Budget remaining: $<n>
- Practice field: <full / partial / none — see research/TESTING-AND-TUNING.md §2>
- Things that will eat time and that we always forget: <exams, holidays, ...>

Produce the rubric score with the reasoning for each dimension, then:
1. Total build hours this strategy needs, itemised by mechanism.
2. Compare against hours actually available. State the ratio.
3. If it does not fit, the smallest scope cut that makes it fit, and what
   capability we lose.
4. The single resource that most limits us, and the cheapest way to relieve it.

If the honest answer is "this team cannot build this in this time," say exactly
that in your first sentence. Do not soften it. A plan that does not fit is the
most expensive mistake a small team can make.
```

---

## S7 — Team Update diff watch *(every Thursday)*

**[FACT]** BIOBUZZ §1.7.3: Team Updates post **every Thursday** beginning on
Kickoff day and ending two weeks before FIRST Championship.

```
A new BIOBUZZ Team Update has been posted at <path or URL>.

1. Produce a precise diff against our current understanding: which rule ids
   changed, what the old text said, what the new text says. Quote both.
2. For each change, tell me: does it affect (a) our robot design, (b) our code,
   (c) our strategy, (d) our inspection checklist, (e) nothing?
3. Grep the update for: AI, artificial, expansion, sizing, R105, servo, stall,
   and each rule id our robot depends on: <list yours>.
4. List the concrete actions this creates for us, with an owner-shaped
   description ("someone must re-measure X", "the inspection checklist line for
   R### must change to ...").
5. Update these files if anything changed, and show me the diff before writing:
     reference/CONSTRUCTION-RULES-R.md
     tools/ai/inspection-checklist.template.md

If the update changes nothing relevant to us, say so in one line. Do not
manufacture significance.
```

---

## S8 — Q&A answer digest

```
Read the latest official FTC Game Q&A answers at <URL or local archive path>.

Produce a table: Q&A number | rule id | the question in one line | the ruling |
does it AFFECT US? (yes/no/maybe) | what we do about it.

Then:
- List every ruling that CONTRADICTS an assumption in our current design or
  strategy documents. Search our reference/ and research/ files to find the
  assumption and cite the file and line.
- List every ruling that OPENS something we had assumed closed.
- Flag any ruling where the question asked was subtly different from the
  question we care about — those are the ones teams misapply.

Rules: quote the official answer verbatim for anything you say is binding. An
answer to a *similar* question is not a ruling on ours; label those "analogous,
not binding" and draft the question we should submit ourselves.
```

---

## S9 — Match strategy card

```
Generate a one-page match strategy card we can print and hand to our drive team.

Our robot's capabilities and measured cycle times: <list>
Alliance partner: team <n>. What we know about them: <paste their row from our
scouting CSV, or "unknown">
Opponents: <n>, <n>. What we know: <paste>
Match type and what we need from it: <qualification / playoff; do we need the
win, the RP, or both?>

The card must fit on one page and contain:
1. Our job in auto, in one sentence, and the fallback if the primary fails.
2. The division of labour with our partner in teleop — who does what, where,
   and the exact words to say to them in the pit beforehand.
3. Our endgame trigger: at what clock time do we stop scoring and start the
   endgame sequence? Give the number.
4. The two things that lose us this match, and the countermeasure to each.
5. The one behaviour that would draw a penalty against us in this specific
   matchup, with the rule id.
6. A blank three-line box for the drivers to write their own notes.

Plain language. Short sentences. No jargon our drivers do not already use.
Mark clearly anything you inferred rather than got from the data I gave you.
```

---

## S10 — Penalty-risk audit

```
Audit this plan for penalty risk. Read
  reference/PENALTY-AND-ENFORCEMENT.md
and the current BIOBUZZ game rules (Section 11) for the actual foul text.

Our plan: <paste>
Our robot's physical behaviours: <what it does that involves contact, extension,
possession, or the opponent's zone>

Produce: behaviour | rule that could be violated | MINOR or MAJOR | point cost |
how likely a referee calls it (H/M/L) and why | the design or driver change that
removes the risk.

Then compute: expected penalty points per match under this plan, versus the
expected points the risky behaviour earns us. State whether the trade is worth
it, with the arithmetic.

Finally: which of these risks are DRIVER-controllable (train it out) versus
DESIGN-controllable (must change the robot)? The second list is the urgent one.

Cite every rule id. If a rule is still a placeholder in our manual copy, say so —
Sections 8-11 were placeholders in V0 and are only final after Kickoff.
```

---

## S11 — What does the winning robot actually look like? *(uses real data)*

**Run this after real BIOBUZZ events exist — December onward.**

```
Use our scouting tooling to answer this with data, not opinion.

1. Run:
   python "tools/ai/scouting/fetch_events.py" \
       events --source scout --season 2026 -o events.csv
   then pull matches, rankings and awards for these events: <list of event codes
   in our region and 2-3 strong regions elsewhere>
2. From the match data, compute: the distribution of winning scores, the median
   and 90th-percentile alliance score, and how those changed month over month.
3. From the score BREAKDOWN columns (they are season-specific — read the actual
   column names in the CSV, do not assume), compute what fraction of a typical
   winning score comes from each scoring category.
4. Cross-reference the rankings and awards CSVs: what did the top 3 seeds at
   each event have in common in their score breakdown?
5. Answer: which single scoring category best predicts winning, and how strong
   is that relationship? Report the actual correlation and the sample size.

Rules:
- Show me the numbers and the sample size for every claim. n < 20 gets an
  explicit "small sample" warning.
- Do not tell me what to build. Tell me what the data says and what it does not
  say. Distinguish "correlated with winning" from "causes winning" explicitly.
- If the data does not support a conclusion, say "the data does not answer this."
```

---

## S12 — Devil's advocate on a mid-season pivot

```
We are considering a mid-season change: <describe it>
Current date: <date>. Our next event: <date>. Events after that: <dates>

Argue BOTH sides properly. Give me:

CASE FOR THE PIVOT
- the strongest three arguments, with the arithmetic where there is any

CASE AGAINST
- the strongest three arguments, with the arithmetic
- the hours this costs, itemised, including re-tuning, re-programming,
  re-inspection (I303 requires re-inspection for most robot changes) and driver
  re-practice — teams always forget the last two
- what capability we lose while it is torn apart, and how many practice hours
  and matches that costs

THE DECIDING QUESTION
- one question whose answer settles it, that we could actually answer this week

THE REVERSIBILITY TEST
- if we start this and it goes badly, at what point can we no longer go back?
  Give me the date.

Do not pick a side. Do not end with encouragement.
```

---

## Anti-prompts

| Don't ask | Why | Ask instead |
|---|---|---|
| "What's the best strategy for BIOBUZZ?" | The game is not in its training data, and it will agree with whatever you suggest | S1 → S2 → S3, then the students decide with `reference/STRATEGY-RANKING-PROTOCOL.md` |
| "Rank these strategies for us" | Sycophantic; documented to be worse than naive baselines | S3 (arithmetic) + S4 (red team), you rank |
| "Build our pick list" | Publicly reported as worse than sorting by average score | `tools/ai/PROMPTS-scouting.md` SC5 — machine tiers, humans order |
| "Is this rule interpretation right?" | It will confidently cite a renumbered prior-season rule | S5, which forces it to quote the local manual text, then submit the Q&A |
| "Will this strategy win?" | Unanswerable, and the answer will be encouraging | S4 — make it try to beat you instead |
