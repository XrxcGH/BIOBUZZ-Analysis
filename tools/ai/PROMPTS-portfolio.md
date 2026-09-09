# PROMPTS — Engineering Portfolio, Judging and Outreach

Copy-paste prompt library for the written/judged workstream.

---

## The rule this whole file is built around

**[FACT — BIOBUZZ V0 rule A201, p. 47–48, quoted verbatim]**

> Teams may use AI and research aids to compose their portfolios, provided they
> respect intellectual property rights and include a footnote or endnote credit.
> Example Credit: "Portfolio created by Team XXXXX and ChatGPT"

So AI drafting is **explicitly permitted**, and the credit is **mandatory**. The
other A201 constraints, also verbatim:

| Constraint | Exact text |
|---|---|
| Cover page | "must consist of 1 cover page including the team number" (+ optional items). "None of the content of the cover page will be used by JUDGES to evaluate any awards criteria." **No cover page can mean disqualification from judging.** |
| Length | "no more than 15 pages of content". "Any content beyond the allowed 15 pages will not be reviewed" |
| Paper | "use only US Letter … or A[4] … size pages" |
| File size | "if submitted digitally, the complete submission must be less than 15MB" |
| Recency | "must only include progress, challenges, and accomplishments which have taken place since **January 1, 2026**" |
| PII | "use only first names and last initials … full names must not be disclosed" |
| Readability | "Avoid fonts under 10 pt and low-contrast text on images" |
| Links | "JUDGES will not click on links, websites, or videos in a PORTFOLIO" |

**[FACT]** A203: you must do the Initial Interview to be considered for any
judged award. A204: at least 2 student representatives, a copy of the portfolio
for reference. A212: every team receives judging feedback from the Initial
Interview. A213/A214: Inspire only in your HOME REGION, and not at multiple
Qualifying/League Tournaments.

**[JUDGMENT] The line we hold.** AI drafts and edits. Students supply every
fact, every number, every decision and every opinion — and can defend all of it
without the tool present. See `research/AI-IN-FTC-POLICY.md` §4 and §10.

**Companion files**
- Award criteria, evidence and interview tactics: `research/SCOUTING-AND-AWARDS.md` §7, §11–§15
- Which award to target with which robot: `reference/AWARD-ALIGNMENT-MATRIX.md`
- Full award catalogue: `reference/AWARD-CATALOG-BIOBUZZ.md`
- Documentation cadence that produces the portfolio as a by-product: `research/SCOUTING-AND-AWARDS.md` §16
- The decision log and meeting notes that feed it: `tools/ai/decision-log.template.md`, `tools/ai/meeting-notes.template.md`

---

## Contents

| # | Prompt | When |
|---|---|---|
| PF1 | Monthly logs → draft portfolio page | monthly |
| PF2 | Criterion-by-criterion coverage audit | 3 weeks before first judged event |
| PF3 | PII scrub | **before every submission** |
| PF4 | A201 mechanical preflight | before every submission |
| PF5 | Rewrite for judges, not for engineers | per page |
| PF6 | Evidence challenge — attack our own claims | before submission |
| PF7 | Mock judge interview | weekly, 2 minutes |
| PF8 | Turn the A212 feedback form into actions | after every event |
| PF9 | Sponsor / grant letter draft | as needed |
| PF10 | Outreach event log → portfolio paragraph | same day as the event |
| PF11 | Award-specific evidence pack | per targeted award |
| PF12 | Individual-award nomination draft | Nov–Dec |
| PF13 | Portfolio-to-pit-display condensation | before each event |

---

## PF1 — Monthly logs → draft portfolio page

**The highest-value use in this workstream.** It converts records you already
have into prose, which is transcription labour, not engineering judgement.

```
Read every file in these directories dated between <start> and <end>:
  decisions/    meetings/    mechanisms/    control/experiments/    outreach/

Draft ONE portfolio page (about 450-550 words plus 2 figure placeholders) that
covers this period, targeting the <Think / Design / Control / Innovate / Connect
/ Motivate / Sustain> Award criteria. Read the criteria in
  reference/AWARD-CATALOG-BIOBUZZ.md
first and tell me which specific criterion each paragraph is serving.

Hard rules:
- EVERY factual claim must trace to a specific file and date in the logs.
  Put the source in a bracket like [decisions/2026-10-14-drivetrain.md] after
  each claim while drafting; I will strip them before printing.
- If a claim I clearly want to make is NOT supported by the logs, do NOT write
  it. Instead list it at the end under "CLAIMS WITH NO EVIDENCE IN THE LOGS" so
  we can either find the evidence or drop the claim.
- Write in the students' voice: first person plural, plain language, short
  sentences. No marketing adjectives. No "leveraged", "utilized", "cutting-edge".
- Numbers beat adjectives. "Cycle time fell from 8.2 s to 5.4 s over three
  iterations" beats "we dramatically improved our cycle time."
- Only content from on or after 1 January 2026 (A201.E). Flag anything older.
- Mark each figure placeholder with exactly what photo or plot belongs there and
  which log entry it comes from.

At the end, list the three questions a judge would most likely ask about this
page, so we can prepare answers.
```

---

## PF2 — Criterion-by-criterion coverage audit

```
Audit our portfolio draft at <path> against the award criteria.

Read:
  reference/AWARD-CATALOG-BIOBUZZ.md
  reference/AWARD-ALIGNMENT-MATRIX.md
  research/SCOUTING-AND-AWARDS.md section 7

Produce ONE ROW PER CRITERION for these awards: <the 2-3 we are targeting, plus
Inspire>. Columns:
  award | criterion id and text | Required or Encouraged | is it addressed in our
  draft? | page and paragraph where | strength (STRONG / WEAK / ABSENT) | what
  specific evidence would move it up one level

Rules:
- Judge STRENGTH by whether a judge could point at a concrete artefact, number or
  dated event. Adjectives are WEAK by definition.
- Be harsh. A generous audit is worthless. If a criterion is ABSENT, say ABSENT.
- Do not suggest we write something we cannot evidence — suggest what we would
  have to DO to be able to evidence it, and how long it would take.

Finish with: the three highest-leverage changes to this draft, ranked by
criteria-strength gained per hour of work.
```

---

## PF3 — PII scrub *(run before every single submission)*

```
Scan <portfolio file, and every image caption and filename> for Personally
Identifying Information, per BIOBUZZ A201:

  "Teams must strictly minimize Personally Identifying Information (PII) in the
   PORTFOLIO. For student privacy, use only first names and last initials. While
   student photographs are permitted, full names must not be disclosed."

Find and list, with page and line:
1. Any full student name (first + last). Propose the replacement in
   "Firstname L." form.
2. Any student's full name in an image caption, an alt text, a filename, a chart
   label, a screenshot, an award certificate, a signature, or a t-shirt in a photo
   that you can read.
3. Home addresses, personal phone numbers, personal email addresses, personal
   social handles, school ID numbers, dates of birth.
4. Any team roster, sign-in sheet or contact list reproduced as an image.
5. Screenshots that show a logged-in account name, an email in a toolbar, or a
   file path containing a user name.

Output a table: page | what | exact text found | suggested replacement.
Then a single line: PASS or FAIL.

Do not modify the file. I will make the edits myself and re-run this.
Adult mentor and sponsor names are permitted — flag them separately as
"check with the person" rather than as violations.
```

---

## PF4 — A201 mechanical preflight

```
Preflight our portfolio against the mechanical requirements of BIOBUZZ A201.
File: <path to the PDF>

Check and report PASS/FAIL for each, with the measured value:
1. Exactly 1 cover page, and it contains the team number. (No cover page can
   mean disqualification from judging.)
2. Content pages <= 15, EXCLUDING the cover. Report the actual count.
3. Page size is US Letter (8.5 x 11 in) or A4 (210 x 297 mm), consistently.
   Report any page that differs.
4. File size < 15 MB for digital submission. Report the actual size in MB.
5. No body text below 10 pt. Report the smallest font size found and where.
6. Contrast: flag any text over an image, or any low-contrast pair. Give the
   contrast ratio if you can compute it and name the WebAIM threshold it fails.
7. The A201 AI credit footnote/endnote is present. Report its exact text.
8. Any hyperlink, QR code, embedded video or "see our website" pointer that
   assumes a judge will click it. A201: "JUDGES will not click on links,
   websites, or videos in a PORTFOLIO."
9. Any content dated before 1 January 2026 presented as current-season work
   (A201.E). Referencing a prior season to show growth is allowed; the emphasis
   must be on the current season.

For anything you cannot measure from the file, say NEEDS-HUMAN-CHECK and say
exactly what to check and how.
```

---

## PF5 — Rewrite for judges, not for engineers

```
Rewrite this portfolio section for a judge who is smart, is not an FTC expert,
and has about 90 seconds for this page.

<paste the section>

Rules:
- Keep every fact and every number exactly as written. If you think a fact is
  wrong, say so separately — do not silently change it.
- Lead with the outcome, then the method. Judges read the first sentence of each
  paragraph and skim the rest.
- Cut every adjective that is not doing work. Cut "very", "really",
  "successfully", "innovative", "state-of-the-art".
- Turn any list of three or more parallel items into a table or a bulleted list.
- Replace jargon with the plain term, or define it in-line in four words or fewer
  the first time.
- Target <n> words. Report the before and after word count.

Then show me a diff-style list of what you cut and why, so I can put anything
back that mattered.
```

---

## PF6 — Evidence challenge *(attack our own portfolio)*

```
You are a competition judge who has read 40 portfolios today and is sceptical.
Attack ours. Be specific and unkind.

<paste the portfolio text, or point me at the file>

For every claim, ask the follow-up question you would ask in the interview, and
say what answer would satisfy you.

Then produce three lists:
1. CLAIMS WE CANNOT DEFEND — where the follow-up question has no good answer
   from what is written. These are the dangerous ones. For each, say whether we
   should get the evidence or cut the claim.
2. NUMBERS THAT LOOK MADE UP — any figure with no stated method or source,
   especially outreach reach numbers, percentages and "improved by X%" claims.
3. THINGS EVERY TEAM SAYS — sentences that could appear in any team's portfolio
   unchanged. These waste page space.

Finish with: the single sentence in this portfolio that would most impress you,
and the single sentence that would most damage our credibility.
```

---

## PF7 — Mock judge interview *(2 minutes, every meeting)*

```
Run a mock FTC judge interview with me. You are the judge panel.

Our team context: <2 sentences>
Focus this round on: <Control / Think / Design / Connect / Motivate / Sustain /
Inspire>
Draw questions from the official FIRST judging question bank style; if you have
the 2026-27 bank, use it, and if you do not, say so and use the prior season's
style — the 2026-27 Judging Question Bank was listed as "coming soon" in the
BIOBUZZ V0 manual.

Rules of the drill:
- Ask ONE question. Wait for my answer. Do not answer for me.
- Then ask the follow-up a real judge would ask. Judges always follow up on a
  number or a claim.
- After three exchanges, score my answers on: was it specific? did it cite our
  own evidence? did it credit teammates? did I say "I don't know" honestly when
  I did not know?
- Tell me the one thing to say differently next time, in one sentence.
- If I gave a memorised-sounding answer, call it out. Judges notice.

Do NOT write an answer for me to memorise. If I ask you to, refuse and remind me
that our team policy is that no AI-drafted answer is spoken in a live judge
interview (research/AI-IN-FTC-POLICY.md section 8).
```

---

## PF8 — Turn the A212 feedback form into actions

**[FACT]** A212: "Judging feedback is provided to all teams" from the Initial
Interview. **[JUDGMENT]** It is free, unbiased, and almost nobody acts on it.

```
Here is the judging feedback form we received at <event, date>:
<paste it verbatim>

Produce:
1. A literal reading: what did they actually say, separated from what we wish
   they said. Quote them.
2. For each point of feedback, map it to the specific award criterion it relates
   to (read reference/AWARD-CATALOG-BIOBUZZ.md).
3. One concrete action per point: what we change in the portfolio, the pit, or
   the interview, and roughly how long it takes.
4. Rank the actions by impact per hour.
5. Compare against the feedback from our previous event at <path>: what did they
   say twice? Anything repeated is the thing to fix first.

Then draft the two-line entry for meetings/<date>.md recording what we decided
to do about it.
```

---

## PF9 — Sponsor / grant letter draft

```
Draft a <sponsorship request / thank-you / grant application / renewal> letter.

Recipient: <organisation, and what they actually do>
Our ask: $<n> or <in-kind item>, for <specific purpose>
What we can offer: <logo placement, shop visit, demo at their event, a report>
Prior relationship: <none / they gave $X in 2025 / we met at Y>
Our team, in numbers: <students, years running, events attended, outreach reach>
Deadline and format: <...>

Rules:
- One page maximum. Business tone, not student-newsletter tone.
- Lead with what they get, not with what we need.
- Every number about our team must come from the list I gave you. If you want to
  use a number I did not supply, ask me for it — do NOT estimate our outreach
  reach, our student count or our budget.
- Include a specific, dated, checkable commitment ("we will send a one-page
  season report by 1 May 2027"), because that is what gets renewals.
- Leave <BRACKETED> placeholders for anything only we can fill in.

After the letter, list the three things about this specific recipient we should
research before sending, and where to look.
```

---

## PF10 — Outreach event log → portfolio paragraph

```
Turn this outreach event into a dated log entry and a portfolio-ready paragraph.

What we did: <...>
Date, location, duration: <...>
Who we reached and HOW WE COUNTED THEM: <...>
Evidence we have: <photos, a sign-in count, an email from the host, a flyer>
What we learned / would do differently: <...>

Produce:
1. The dated entry for outreach/<YYYY-MM-DD>-<slug>.md with fields: objective,
   strategy, activity, reach with the counting basis, evidence, reflection.
2. A 90-word portfolio paragraph.

Hard rules on the reach number:
- Use ONLY the number I gave you and state the counting basis in the text
  ("42 students, counted from the sign-in sheet"). FIRST's outreach guidance is
  to estimate on the low end.
- If my basis is weak (e.g. "about a hundred people walked past"), say so and
  propose a defensible smaller number with a stated basis.
- Never aggregate across events into a season total unless I explicitly give you
  every component number.
- No full student names (A201 PII).

Then tell me the one piece of evidence we should have collected and did not, so
we get it next time.
```

---

## PF11 — Award-specific evidence pack

```
Build the evidence pack for the <award> Award.

Read the criteria in reference/AWARD-CATALOG-BIOBUZZ.md and the pairing guidance
in reference/AWARD-ALIGNMENT-MATRIX.md.

Search our repo (decisions/, mechanisms/, control/, outreach/, meetings/, the
robot code repo if I point you at it) and produce:

  criterion | our evidence | where it lives (file:line or photo filename) |
  is it IN the portfolio? (page) | is it in the PIT display? | can a student
  explain it? (I will fill this column)

Rules:
- Only real, findable evidence. Every row cites a real path. If nothing exists,
  the row says NO EVIDENCE.
- Separate "we have this evidence but it is not in the portfolio" from "we do
  not have this evidence" — these need completely different responses.
- End with the shortest path to making this award winnable: the specific
  artefacts to create, in priority order, with an hour estimate for each.
- Be honest about whether this award is realistic for us given what exists
  today. research/SCOUTING-AND-AWARDS.md section 10 has the measured base rates.
```

---

## PF12 — Individual-award nomination draft

**[JUDGMENT] The deadline nobody on a small team remembers.** Individual FIRST
awards (Dean's List, mentor awards) have their own submission windows, typically
well before your first event. Check `research/SCOUTING-AND-AWARDS.md` §15 and
**re-verify the 2026-27 dates on firstinspires.org — the exact deadline is
UNVERIFIED for this season.**

```
Help me draft the nomination for <award> for <first name + last initial>.

The official criteria: <paste them from the FIRST submission form — do not use
your memory of them>
Word/character limit: <n>
What this person actually did, with dates: <list — I supply all of it>
Specific moments that show it: <anecdotes>

Rules:
- Every sentence must be traceable to something I told you. Invent nothing.
- Lead each paragraph with a concrete action, then its effect, then the evidence.
- Show, do not assert: "she rebuilt the intake three times in two weeks and
  documented each version" beats "she is dedicated."
- Respect the word limit exactly. Report the count.
- Use first name + last initial only.
- Flag every place where a specific date, number or artefact would strengthen it
  and I have not given you one.

Then list what I should ask the nominee (or their mentor) to supply before we
submit.
```

---

## PF13 — Portfolio → pit display

```
Condense our portfolio into a pit display plan.

Portfolio: <path>. Pit space: <dimensions>. Budget: $<n>. Print options: <...>

Judges walk the pits and stop for 30-60 seconds. Produce:
1. The three things a judge must learn from our pit in 30 seconds, in priority
   order, with the exact words for each.
2. A layout: what goes at eye level, what goes low, what is on the table, what a
   student holds.
3. One "artefact of the season" to display physically — a failed part next to
   the part that replaced it is worth more than any poster. Pick ours from the
   mechanism logs and say why.
4. The one-page handout... and then remind me of A202: judges "cannot take extra
   printed papers from an interview back to their judging room," so the handout
   is for conversation in the pit, not for the judging room. Anything we need
   judged must be inside the 15 portfolio pages.
5. What NOT to put up: anything that duplicates the portfolio, anything with a
   full student name, anything a judge would have to read for more than 10 seconds.
```

---

## The credit line — copy this

**Required by A201.** Put it as a footnote or endnote on the last content page.

> Portfolio composed by Team **<NNNNN>** with drafting and editing assistance
> from Anthropic Claude. All engineering content, data, testing results and
> conclusions are the team's own work.

**Also disclose** (not required by A201, but recommended — see
`research/AI-IN-FTC-POLICY.md` §8 DISCLOSE):

- **Repo `README.md`:** "Portions of this code were developed with assistance
  from Anthropic Claude and reviewed, tested and tuned by Team ####."
- **In the interview**, when asked what outside resources you used: name Claude
  in the same breath as FTCLib, Road Runner, GM0 and goBILDA. It is a tool in
  the list. Say it matter-of-factly, then immediately demonstrate that a student
  understands the work.

---

## Anti-prompts

| Don't ask | Why | Ask instead |
|---|---|---|
| "Write our portfolio" | Judges follow up on every claim; you will be defending sentences no student wrote from evidence that does not exist | PF1 — logs in, one page out, sources attached |
| "How many people did our outreach reach?" | It will produce a plausible number. That number is a fabrication in a judged document | PF10 — you supply the count and the basis |
| "Write my answers for the judge interview" | Against our own policy, and judges can tell | PF7 — drill, don't script |
| "Make this sound more impressive" | Produces exactly the adjectives PF6 tells you to cut | PF5 — rewrite for a 90-second reader |
| "Is our portfolio good?" | Sycophantic | PF6 — make it attack the portfolio instead |
