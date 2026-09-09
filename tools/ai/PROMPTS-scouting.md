# PROMPTS — Scouting, Data and Alliance Selection

Copy-paste prompt library for the data workstream.

---

## The split that makes this work

**[FACT]** Public reports from FRC/FTC mentors (Chief Delphi thread 519529,
April 2026) say an LLM picklist built from real scouting data was *"worse than
sorting by averages"*, while the same thread reports LLM-written **analysis
scripts** working well (Team 254 used them for match energy analysis).
See `research/AI-IN-FTC-POLICY.md` §9.

**[JUDGMENT] Therefore:**

| Give the AI | Keep for humans |
|---|---|
| Writing and debugging the fetch/OPR/merge scripts | Ordering the pick list |
| Pulling and reshaping data into CSV | Judging driver quality |
| Arithmetic: OPR, trends, percentiles, correlations | Judging whether a robot is *reliable* |
| Generating printable dossiers and blank scout forms | Negotiating with a candidate partner in the pits |
| Finding contradictions between data and our notes | Deciding what we need from a partner |

The machine proposes **tiers**. Humans **order within tiers**. That is the whole
protocol.

**Companion files**
- The working script: `tools/ai/scouting/fetch_events.py` (`--help` for usage)
- Setup, API keys, tiers: `tools/ai/scouting/README.md`
- The strategy behind it, OPR's real limits, alliance-selection negotiation:
  `research/SCOUTING-AND-AWARDS.md` §1–§6
- A ready-to-run OPR/picklist script: `research/SCOUTING-AND-AWARDS.md` §5.3a

---

## Contents

| # | Prompt | When |
|---|---|---|
| SC1 | Set up API credentials and verify | once |
| SC2 | Pre-event dossier (T-3 days) | before every event |
| SC3 | Design the scout form for THIS game | after kickoff |
| SC4 | Compute OPR and trends from a match CSV | at lunch, every event |
| SC5 | Build a TIERED pick list (not an ordered one) | before alliance selection |
| SC6 | Reconcile data with human observation | mid-event |
| SC7 | Our own performance post-mortem | after every event |
| SC8 | Regional advancement reality check | pre-season and December |
| SC9 | Write or fix a scouting script | as needed |
| SC10 | Partner-negotiation brief | 30 min before selection |
| SC11 | Opponent brief for a specific match | between matches |
| SC12 | Season-long trend report | monthly |

---

## SC1 — Set up API credentials and verify

```
Help me get FTC data access working on this machine.

1. Read tools/ai/scouting/README.md
   and tell me, in numbered steps, exactly what I have to do.
2. Run:
     python "tools/ai/scouting/fetch_events.py" check
   and interpret the output for me line by line.
3. If credentials are missing, tell me exactly where to register and what to do
   with the username and key I receive. Do NOT ask me to paste my token into
   the chat — tell me to set the environment variable or write the credentials
   file myself.
4. Confirm the season number to use. FTC seasons are named by their starting
   year: BIOBUZZ 2026-27 = 2026, DECODE 2025-26 = 2025.
5. Run one no-credentials command against last season to prove the pipe works:
     python fetch_events.py events --source scout --season 2025 --limit 5

Tell me plainly if something does not work, and what the next diagnostic step is.
Do not tell me it works if you have not seen it work.
```

---

## SC2 — Pre-event dossier *(T-minus 3 days)*

```
Build our pre-event dossier for <event code>, season <2026>.

1. Run:
     python "C:/.../tools/ai/scouting/fetch_events.py" dossier \
        --season 2026 -e <CODE> -o scouting/<CODE>-dossier.csv
   Show me any warnings it printed.
2. Read the CSV and produce a printable Markdown briefing with:
   a. A ranked table of every registered team by season total OPR, with their
      auto / driver-controlled / endgame component OPR and the rank of each.
   b. A WATCH LIST: teams in the top 20% by season OPR, plus any team that has
      won Inspire or Control this season (pull awards for their prior events).
   c. Our own row highlighted, with our percentile.
   d. Any team with a large gap between total OPR and its rank — those are the
      teams whose record understates them, and they go undrafted.
   e. Any rookie team (rookieYear = 2026) — unknown quantity, needs pit scouting.
3. A one-page blank pit-scout form sized for this event's team count, with the
   fields from SC3.

Rules:
- Every number comes from the CSV. Do not fill a gap with an estimate; write
  "no data" and say why (team is a rookie, has not competed this season, etc.).
- State the sample size behind every OPR: an OPR from 5 matches at one event is
  not comparable to one from 40 matches across four events.
- Format it to PRINT on paper. Venue Wi-Fi will fail. Assume no screen.
```

---

## SC3 — Design the scout form for THIS game

**Run after Kickoff, once the scoring table exists.**

```
Design our pit-scout form and our match-scout form for BIOBUZZ 2026-27.

Read the scoring table we extracted at <path> (from PROMPTS-strategy.md S1).

Constraints:
- We have ONE scout, part time. The match form must be fillable in under 15
  seconds per match while watching. The pit form must take under 90 seconds
  per team.
- Only include fields that are NOT already available from the API. We already
  get: rank, RP, W-L-T, matches played, total and component OPR, awards.
  Adding a field that duplicates the API is a net loss.
- Prioritise, in this order, the things research/SCOUTING-AND-AWARDS.md section
  5.2 says only a human can capture: auto start position (the highest-ROI single
  field, because it determines auto conflicts), auto reliability rate, downtime
  and its cause, driver quality, defence given and received.

Produce:
1. The pit form: field | type (number / 1-5 / checkbox / free text) | the exact
   question to ASK the team, in words a student can say out loud.
2. The match form: same, but every field must be markable with one pen stroke.
3. The CSV header row for each, so they merge with the dossier CSV on teamNumber.
4. A one-paragraph explanation of what decision each field is FOR. If a field
   does not change a decision, cut it and say so.

Then tell me which two fields to drop if we only have time for the short version.
```

---

## SC4 — Compute OPR and trends *(at lunch, every event)*

```
We are at <event code>, and qualification round <n> just finished.

1. Pull the current matches:
     python fetch_events.py matches --source scout --season 2026 -e <CODE> \
        -o scouting/<CODE>-matches.csv
   (--source scout works without credentials and is faster to get running at a
   venue; use --source ftc if scout has not synced.)
2. Compute from the raw scores in that CSV:
   - total OPR for every team, solved by least squares
   - component OPR for each scoring category present in the score-breakdown
     columns. READ the actual column names in the CSV — BIOBUZZ score fields
     are new this season, do not assume DECODE's names.
   - "last 3 matches" OPR for each team, and the delta vs their overall OPR
   - each team's score standard deviation (consistency)
3. Merge with our human observations at <path to our scout CSV> on teamNumber.
4. Output a single sorted CSV plus a printable table.

Rules:
- State the number of matches the OPR is solved from. Below round 3 the numbers
  are not stable — say so explicitly at the top of the output.
- Flag any team whose last-3 OPR differs from their overall OPR by more than
  25%: those are the teams that fixed something or broke something.
- Show me the code you ran. If you wrote a new script, save it under
  tools/ai/scouting/ so we have it next event.
- Do not rank teams for picking. That is SC5.
```

---

## SC5 — Build a TIERED pick list *(the machine proposes tiers; we order)*

```
Build a TIERED pick list from our merged data at <path>.

What we need from a partner, in priority order: <e.g. "1. reliable auto that
does not conflict with ours (we start left), 2. consistent cycler, 3. anything
in endgame">
Our own capabilities: <...>
Our likely seed: <n>

Produce THREE tiers, not an ordered list:
  TIER A — teams that would materially raise our expected score
  TIER B — solid, would not hurt us
  TIER C — would not help / would conflict with us

For every team, give: teamNumber | tier | the 2-3 data points that put them in
that tier | the ONE unknown that could move them a tier | who has to check it
and how (pit visit? watch match N?)

Hard rules:
- Do NOT order teams within a tier. We do that, out loud, as a team.
- State the evidence for every placement. "Tier A" with no cited number is not
  an answer.
- Explicitly flag every team where the DATA and our HUMAN NOTES disagree — those
  are the most valuable rows on the sheet, and they always get resolved in
  favour of the human note.
- Flag auto conflicts explicitly: any team whose auto start position matches
  ours goes in a separate CONFLICT column regardless of tier.
- Remind me at the top: OPR is a season/event-level average and says nothing
  about whether a robot was on the field for the whole match.
```

---

## SC6 — Reconcile data with human observation

```
Our scouting notes and the API data disagree. Reconcile them.

Numbers: <paste rows from the merged CSV>
Our notes: <paste what the scout wrote>

For each disagreement:
1. State it precisely: what the number says, what the human says.
2. List the reasons a number could be misleading here — a strong partner
   inflating OPR, a broken match dragging it down, a small sample, a surrogate
   match, a no-show opponent, a defence-heavy match.
3. List the reasons the human note could be wrong — one match watched, confusing
   two teams, watching the wrong field.
4. Say which you would trust for THIS specific decision, and why.
5. Name the single observation that would settle it, and when we can make it
   (which upcoming match, or a pit visit).

Default rule you must follow: for anything about RELIABILITY, DOWNTIME, DRIVER
SKILL or DEFENCE, the human note wins — none of those are in the data at all.
For anything about SCORING RATE, the data wins over a single-match impression.
```

---

## SC7 — Our own performance post-mortem

```
Post-mortem our performance at <event code>.

1. Pull our own matches:
     python fetch_events.py matches --source scout --season 2026 -e <CODE> \
        -t <our team number> -o scouting/<CODE>-us.csv
   and our rankings row.
2. Compute: our alliance's average score with us on it, our total and component
   OPR, our score variance, our record, and how our component OPR compares to
   the event median in each category.
3. Answer, with numbers:
   - In which scoring category are we furthest from the event's top quartile?
   - How many points per match would we gain by closing that gap halfway?
   - Did our performance trend up, down, or flat across the day? Show the
     per-match series.
   - In matches we lost, what was the margin, and would closing the gap above
     have changed the result? Count them.
4. Cross-reference our own match notes at <path>: which losses were mechanism
   failures vs. capability gaps? Those need completely different responses.

Then: the three changes with the best expected-points-per-hour before our next
event, and one thing we should stop doing.

Show the arithmetic. Flag small samples — an event is 5-8 qualification matches
and that is not many.
```

---

## SC8 — Regional advancement reality check

**[JUDGMENT]** The best pre-season use of the official API. Answers "what does it
actually take to advance out of our region?" with data instead of folklore.

```
Work out what it took to advance from our region last season.

Our region: <name>. Season to analyse: 2025 (DECODE).

Using the official API (needs credentials):
1. python fetch_events.py events --season 2025 -o events25.csv
   and find every event in our region, including the regional championship.
2. For our regional championship, pull:
   - rankings           (what rank did advancing teams finish?)
   - alliances --selection   (the ACTUAL draft order and declines)
   - awards             (who won what)
   - advancement and advancement points, if available for that event
3. Answer, with numbers:
   - What rank did the last-advancing team finish?
   - What OPR (from ftcscout) did the last-advancing team have?
   - How many advancement slots did our region get, and how many teams competed?
   - What fraction of advancing teams advanced on an AWARD vs. on ALLIANCE
     PLACEMENT? This is the number that should drive our award strategy.
   - Which awards actually carried advancement weight in practice?
4. Do the same for one comparable region so we know whether ours is unusual.

State the sample size for everything. Note explicitly that 2026-27 slot
allocations are published on the FTC-Events page "starting in early December"
after the 17 November 2026 registration cutoff, so last year's numbers are a
guide, not a guarantee.
```

---

## SC9 — Write or fix a scouting script

```
Write a Python script for: <what it should do>.

Non-negotiable constraints:
- PYTHON STANDARD LIBRARY ONLY. No pip install. The laptop that runs this at a
  venue cannot install anything and often has no working network.
- Must run offline against a CSV we already downloaded, as well as online.
- Every API endpoint URL is a named module-level constant with a comment saying
  when it was last verified. Do not bury a URL in the middle of a function.
- Graceful failure with an actionable message, never a bare traceback. If
  credentials are missing, say where to get them.
- --help that a student can read and act on.
- Writes CSV with utf-8-sig so Excel on Windows opens it correctly.
- Column names are stable and documented. Season-specific score fields must be
  discovered from the data at runtime, NOT hardcoded — BIOBUZZ adds new score
  columns that do not exist in any prior season.

Reference implementation to match in style and rigour:
  tools/ai/scouting/fetch_events.py

Before you finish: run `python -m py_compile <file>` and show me the result, and
run the script against real data (or a saved fixture) and show me the first
5 rows of output. Do not tell me it works without running it.
```

---

## SC10 — Partner-negotiation brief

```
We are seeded <n> and alliance selection is in 30 minutes. Prepare our brief.

Our tiers from SC5: <paste>
Teams already likely to be taken by higher seeds: <your estimate, and say it is
an estimate>
Our capabilities and what we need: <...>

Produce a single printable page:
1. Our call order: first choice, and the next three fallbacks in order, with the
   one-line reason for each. (I will confirm or change this — you are proposing.)
2. For each of our top 4: the exact question to ask them in the pit right now,
   whose answer would confirm or kill them. One question each. Make it specific
   and answerable in 20 seconds.
3. The auto-conflict matrix: for each candidate, does their auto start position
   conflict with ours? What is the workaround and who has to change?
4. If we are PICKED rather than picking: the 30-second pitch for why they should
   want us, in our own plain words, with two real numbers in it.
5. The one thing we must NOT say (over-promising a capability we have not
   demonstrated today).

Keep it to one page. We will be reading it while standing up.
```

---

## SC11 — Opponent brief for a specific match

```
We play <team>, <team> in match <n> in about 20 minutes.

Data: <paste their rows from our merged CSV>
Our notes on them: <paste>
Our partner: <team>, and what we know: <paste>

Give me, in under 150 words total:
1. Their biggest threat, with the number that proves it.
2. Where they are weakest, with the number.
3. One thing our drivers should do differently in this match.
4. One thing our drivers should NOT do (the penalty risk in this specific
   matchup, with the rule id).
5. What to tell our partner, in one sentence, before the match.

If the data is too thin to say something useful, say "not enough data" for that
line rather than filling it. A confident wrong brief is worse than a short one.
```

---

## SC12 — Season-long trend report

```
Produce our season trend report as of <date>.

Pull our results from every event we have attended this season:
  python fetch_events.py events --source scout --season 2026 -t <our number>
then matches and rankings for each event code returned.

Report:
1. Our total and component OPR at each event, as a series. Plot it as an ASCII
   chart or a Markdown table — I need to see the shape.
2. Our percentile within each event's field, so we can separate "we got better"
   from "the field was weaker."
3. Our reliability trend from our own match notes: matches with a mechanism
   failure as a fraction of matches played, by event.
4. The single scoring category where we have improved most, and the one where we
   have not moved.
5. What this predicts for our next event, stated as a range, with the reasoning
   and the caveat that the sample is small.

Then write the 100-word paragraph version for the portfolio, in the students'
voice, with the numbers in it (see tools/ai/PROMPTS-portfolio.md PF1 for the
style rules).
```

---

## Anti-prompts

| Don't ask | Why | Ask instead |
|---|---|---|
| "Build our pick list" | Publicly reported as worse than sorting by average score | SC5 — tiers, not an order |
| "Which team is better, X or Y?" | Encourages a confident answer from thin data | SC6 — reconcile data with observation, name the deciding observation |
| "Predict who will win this event" | Not decision-useful, and the sample is 5–8 matches | SC11 — one actionable line per opponent |
| "What's a good OPR?" | Meaningless without the field and the sample | SC2 — percentile within *this* event's field |
| "Scrape ftc-events.firstinspires.org for me" | The site's own HTML source says "PLEASE DO NOT SCRAPE WEBPAGES FOR EVENT DATA! We have an API" | Use the API via `fetch_events.py` |
