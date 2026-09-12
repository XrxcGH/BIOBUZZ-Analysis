# AI in FTC: Rules of the Road (2026-27 BIOBUZZ)

**Purpose:** establish what is actually permitted, forbidden and undecided regarding AI/LLM use by an FTC team, so every downstream workstream (code, CAD, strategy, scouting, portfolio, outreach) can proceed without guessing.

**Status:** research + recommendation. Revised **2026-08-22**, pre-kickoff. Every manual quote below was verified by full-text grep against the local PDF extract; every web quote was fetched and diffed against the source document. Sections 8-11, 13 and 15 of the BIOBUZZ manual are placeholders, and the 2026-27 Judging Process Guide and Question Bank are not yet published. **Re-verify everything marked (SEASON-DEPENDENT) after kickoff on 2026-09-12.**

---

## 0. Bottom line up front

| Question | Answer | Confidence |
|---|---|---|
| Can we use AI on the engineering portfolio? | **Yes, explicitly, with a footnote/endnote credit.** Written into BIOBUZZ rule A201. | **FACT — verified verbatim** |
| Can we use AI to write robot code? | **Yes, and FIRST says "permitted and encouraged."** Stated in the FTC Judging Process Guide and the FIRST program-wide policy blog. **Not** restated in the BIOBUZZ manual. | **FACT — verified verbatim** |
| Will judges penalize us for using AI? | **They are instructed not to.** FTC: AI use "should not [be] the single determining factor." FRC: "should not discredit a team who uses AI or rank them lower simply for using the tool." | **FACT — verified verbatim** |
| Will judges penalize us for *not being able to explain* AI output? | **Yes, effectively.** "students are ultimately responsible for the answers they give to the Judges." This is the real gate. | **FACT — verified verbatim** |
| Does the new Competition Integrity Contract (§1.5) mention AI? | **No. Not once.** Verified by reading §1.5 in full. The CIC covers cheating, loopholes, rule-enforcement behavior, sportsmanship, safety and health. Zero AI language. | **FACT — full-text verified** |
| Is there a manual rule requiring work to be "student-created"? | **No such rule exists.** Grep for `student-created / own work / plagiar / citation` across all 93 pages returns nothing relevant. The authorship principle lives *only* in judge-facing guidance and award criteria. | **FACT — full-text verified** |
| Can AI run off-robot during a match? | **No** — but for control-system reasons (E301, R704.A/D), not AI policy. | **FACT — verified verbatim** |
| Can our under-18 students use Claude directly? | **No.** Anthropic requires all users to be 18+, with **no exception for education or supervised school use**. This is the sharpest real constraint we face. | **FACT — verified, newly resolved** |
| Is anything genuinely grey? | **Yes: CAD geometry, outreach materials, interview answers, and the scope of the code credit.** See §7. | JUDGMENT |

**The one-sentence version:** FIRST has taken an unusually permissive, explicitly pro-AI position — AI is framed as a tool like CAD or a 3D printer — and has moved the burden entirely onto *student comprehension and attribution*, not tool restriction. **Our FIRST-policy risk is near zero. Our two real risks are (1) the judge interview and (2) the vendor age terms.**

> **The two findings that should change what we actually do:**
>
> 1. **Under-18 students cannot hold Claude accounts** (§6.1). Our AI workflow must be mentor-operated by construction. Conveniently, this is the *same* workflow FIRST's mentor model already blesses — see §4.2.
> 2. **~37% of the FIRST community self-identifies as against generative AI** (Chief Delphi poll, n=384, Feb 2026 — §9). Policy protects us; the human in the room may not share it. **Disclose confidently, lead with student understanding, never lead with the tool.**

---

## 1. Source hierarchy — what actually binds us

FTC has four distinct layers of AI guidance and they do **not** all say the same thing. Ranked by authority:

| # | Source | Binding on | AI scope | Force of credit requirement | Where |
|---|---|---|---|---|---|
| 1 | **BIOBUZZ V0 Competition Manual, rule A201** (§6.2, p.48) | Teams. Enforceable. | **Portfolio only** | "include a footnote or endnote credit" (mandatory) | `ROOT/manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` line 1789 (a local text extract of the manual, not published with the repository; p.48 locates the text in the manual itself) |
| 2 | **FTC Judging Process Guide**, "Artificial Intelligence in FIRST Tech Challenge" (**Rev 25-26.3**, p.20 of 60) | Judges + Judge Advisors. Shapes our score. | **Portfolio *and* robot code** | "are expected to provide proper credit" — **and never a DQ if you don't** | https://ftc-resources.firstinspires.org/ftc/archive/2026/event/judging-guide |
| 3 | **FIRST program-wide policy blog**, Chris Rake (EVP & COO), 2023-11-01 | All FIRST programs. Policy, not rule. | Award submissions, handouts, robot code, "etc." | "must provide proper credit and attribution" | https://community.firstinspires.org/expanding-the-first-toolbox-with-artificial-intelligence |
| 4 | **FRC 2026 Judge Manual**, "Use of Artificial Intelligence (AI)" (p.14, **Rev 2 – 2/18/2026**) | FRC judges. **Not binding on FTC.** Evidence of intent. | Award submissions, handouts, robot code | "**must** provide proper credit" + bans AI detectors | https://info.firstinspires.org/hubfs/web/program/frc/awards/judge-manual.pdf |

> **Two gaps worth naming.**
>
> **Gap 1 — scope.** Layer 1, the only layer teams are *bound* by, covers **only the portfolio**. Layers 2-4 cover **code as well**. There is no *rule* granting or restricting AI in robot code; there is the absence of a prohibition plus affirmative policy encouragement. Strong, but a policy position rather than a rule.
>
> **Gap 2 — force.** FRC says teams **must** credit. FTC's judge guide says teams are **expected to** credit and then explicitly removes the teeth: "A team should never be disqualified for failing to properly credit AI-generated content." FTC is the softer sibling on enforcement, and the *only* mandatory credit obligation on an FTC team is A201's, which is portfolio-scoped.

### 1a. How the language evolved (useful for reading intent)

| Season | Where the AI language lived | Scope | Key clause |
|---|---|---|---|
| 2022-23 POWERPLAY | *(none)* | — | grep returns zero hits |
| 2023-24 CENTERSTAGE | **Manual §9.2.5.1**, its own numbered section: *"Artificial Intelligence in the Engineering Portfolio"* | Portfolio **and Robot Code** | "Teams are permitted to use Artificial Intelligence (AI) to assist in the creation of their Engineering Portfolio and in their Robot Code." |
| 2024-25 INTO THE DEEP | Demoted to guidance text under A101 | Portfolio only | "...must be credited via footnote or endnote." |
| 2025-26 DECODE | Guidance text under A201 | Portfolio only | "...credited via footnote or endnote, and respect intellectual property rights and licenses." |
| 2026-27 BIOBUZZ | Guidance text under A201, shortest wording yet | Portfolio only | "Teams may use AI and research aids to compose their portfolios..." |

**JUDGMENT:** this is **normalization, not tightening**. AI moved from a special-cased section with its own heading to an ordinary line of portfolio guidance sitting next to "avoid fonts under 10 pt." That is what policy looks like when an organization stops treating something as exceptional. Meanwhile the *robot code* permission migrated out of the manual into the judge-facing guide, where it got **stronger** ("permitted and encouraged"). FIRST is not retreating — it is shipping its own **"FIRST Tech Challenge AI Chatbot (coming soon)"** (BIOBUZZ V0 §1.7.2, p.18, line 663).

---

## 2. The operative texts, verbatim

### 2.1 BIOBUZZ V0 — rule A201, §6.2 Team Judged Award Rules (p.48, line 1789)

Appears in the **guidance text** beneath `A201 *Team PORTFOLIOS have limits.`, alongside the other portfolio guidance paragraphs:

> "Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a footnote or endnote credit.
> Example Credit: `Portfolio created by Team XXXXX and ChatGPT`"

Three obligations are embedded: **(a)** respect intellectual property rights, **(b)** include a footnote **or** endnote credit, **(c)** it is scoped to *composing the portfolio*.

Neighbouring guidance in the same rule that constrains how AI output can be delivered:

- 1 cover page + **no more than 15 pages of content**; US Letter or A4; **<15MB** if digital; content only from **since January 1, 2026**.
- "JUDGES will not click on links, websites, or videos in a PORTFOLIO."
- "Teams must strictly minimize Personally Identifying Information (PII)... use only first names and last initials. While student photographs are permitted, full names must not be disclosed."

### 2.2 FTC Judging Process Guide — "Artificial Intelligence in FIRST Tech Challenge" (Rev 25-26.3, p.20) (SEASON-DEPENDENT)

The most important paragraph we have, because it is what the *judges* are trained on. Its operative phrases are quoted; the rest is paraphrased:

- Teams are "permitted and encouraged to use Artificial Intelligence (AI) to assist in the creation of their Portfolio and robot code," and FIRST says that using every tool available supports discovery, innovation and learning.
- FIRST puts AI resources in the same category as CAD programs, programming languages and 3D printers: tools that students may use.
- Teams that use AI for code or content are "expected to provide proper credit and attribution," and to "respect intellectual property rights and licenses." The guide's sample credit line names a team and ChatGPT.
- "A team should never be disqualified for failing to properly credit AI-generated content," although "teams are ultimately responsible for the content they provide to the Judges."
- A Judge may ask clarifying questions about interview and Portfolio content but "should not consider the use (or lack) if AI as the single determining factor" when nominating or deliberating.

*("the use (or lack) if AI" is a typo for "of AI" in the source document — reproduced as printed.)*

**Four consequences:**

1. Failing to credit AI is **not disqualifying**. (Credit anyway — §8.)
2. "Teams are ultimately responsible for the content" — **we own every claim the model made, including hallucinated ones.**
3. Judges **may probe** portfolio content with clarifying questions. Expect it and prepare for it.
4. AI use — *or non-use* — cannot be the deciding factor. A team that loudly refuses AI earns no credit for that either.

Note also: the same guide encourages **judges themselves** to use AI to help draft award scripts. FIRST is not squeamish about this.

### 2.3 FIRST program-wide policy — Chris Rake, EVP & COO, 2023-11-01

> "*FIRST* teams can use AI to assist in the creation of award submissions, handouts, writing robot code, etc."

> "Judges have been instructed to evaluate teams based on what they have accomplished in relation to the judging criteria, and not discredit a team or rank them differently based on the tools they used."

> "*FIRST* may revisit this subject in future seasons as the world evolves and new standards for the use of AI are introduced."

That last sentence is the standing caveat: **this policy is explicitly revisable.** As of August 2026 it has stood ~3 seasons and has been reinforced, not weakened.

### 2.4 FRC 2026 Judge Manual, p.14 — sibling program, two useful additions

> "Judges should not discredit a team who uses AI or rank them lower simply for using the tool. Teams should be compared based on what they have accomplished in relation to the award judging guidelines. Additionally, while there are some sites that check if a submission used AI, they are not accurate and should not be used to verify."

**FIRST has explicitly told FRC judges not to use AI detectors.** **FACT: the FTC Judging Process Guide contains no equivalent sentence** — Rev 25-26.3 was grepped for `detect / verify / plagiar / authentic` and the only hits are unrelated (judging-packet verification). **JUDGMENT:** the FRC statement is strong evidence of organizational intent and we should not fear a detector false positive — but it is *not* currently binding on an FTC judge. Either way: never accuse another team based on one.

### 2.5 The third sibling — FIRST LEGO League

**FACT:** FLL has no comparable published team-AI-use policy. FLL's 2026 "Future Edition" announcements concern **AI content in the game and curriculum** (LEGO Education Computer Science & AI sets), not rules about teams using AI tools, and FIRST states students "will not be expected to use the AI features" in the initial season. **Do not cite FLL as precedent in either direction.**

---

## 3. The Competition Integrity Contract (§1.5) — what it actually says about AI

**FACT: nothing.** A full-text grep of `BIOBUZZ_V0_layout.txt` for `artificial intelligence | generative | LLM | ChatGPT | large language | AI` returns exactly **two** substantive hits in the entire 93-page manual — the A201 portfolio credit line (p.48, line 1789) and the "FIRST Tech Challenge AI Chatbot (coming soon)" note (p.18, line 663). **Neither is in Section 1.5.** I read §1.5 in full (lines 436-557) to confirm.

The CIC is new this season and is "an actionable part of the Framework of Behaviors described in Section 1.4.2" (§1.5, p.14). It has two halves.

**§1.5.1 Sporting Ethics Code** — **four** certifications, all mandatory ("which all teams must follow to protect the integrity of the competition"):

| Certification | Operative language | Does it reach AI? |
|---|---|---|
| **We Don't Cheat.** | "Our team will never intentionally violate the spirit of a rule. We won't circumvent the systems *FIRST* uses to keep the competitions running." | Only if you break an actual rule. Using AI breaks no rule. **Misrepresenting who did the work** would engage this. |
| **We Always Behave with Integrity.** | "We take pride in behaving with honor, even when 'no one is watching.'... Our actions are based on what is right, not what we think we can get away with." | **This is the clause that matters.** It is the honest-attribution clause by implication. |
| **We Play the Game as Intended.** | "Our team will not try to gain an advantage using any 'loopholes' in the rules. If there is ever ambiguity in the specific wording of a rule, we will look to the intent of the rule and spirit of the competition to guide our behavior." | Directly governs the grey areas (§7): **resolve ambiguity toward disclosure**, not away from it. |
| **We Know Our Team Doesn't Enforce the Rules.** | "it is not appropriate for us to accuse, investigate, publicly call-out, or persecute anyone for a perceived infraction, especially in a disrespectful or confrontational manner." | **Do not accuse another team of AI-generating their portfolio.** Ever. Not in the pits, not online. Explicit CIC violation. |

**§1.5.2 Behavior Guidelines** — **eight** aspirational certifications: Journey Before Destination; Respect and Good Sportsmanship; We Help Each Other; Take the High Road; Respect Property and Facilities; Positive Culture of Safety; **We Make Healthy Choices**; We're All on the Same Team. One is quietly relevant to a small team:

> "We also understand that in any creative process a measured (and sometimes relaxed) schedule which leaves time for recuperation will often result in a better outcome than 'grinding' for long hours."

**JUDGMENT:** For a small, under-resourced team this is the *strongest available framing* for AI use in a portfolio or judge interview. FIRST wrote into the manual that grinding is not the goal. Using AI to eliminate 15 hours of boilerplate so six students can spend that time on the robot is not a workaround of the CIC — it is a direct expression of the "We Make Healthy Choices" guideline. That is a genuinely good and honest thing to say to a judge.

**§1.5.3 Infractions, Mitigations & Escalation:** violations "may occur at an event and/or outside of events"; serious Sporting Ethics Code violations escalate to the Event Director and/or FIRST Headquarters, and "following an investigation, at the discretion of FIRST Headquarters, serious violations could result in a team or individuals being suspended or permanently removed from the FIRST Tech Challenge program."

**Honest reading:** there is **no AI-specific tripwire in the CIC.** The only realistic path from "we used AI" to a CIC infraction is **affirmatively lying to a judge about authorship**. Not "we used AI and didn't mention it" — that is explicitly non-disqualifying per §2.2 — but "a judge asked and we said no," or "we presented mentor/AI work as our own design reasoning." That is a *We Always Behave with Integrity* violation and it is our **only real exposure**.

---

## 4. The student-authorship principle — the actual gate

### 4.1 There is no student-authorship *rule*

**FACT, and it surprises people:** the BIOBUZZ manual contains **no rule** requiring that portfolio content, code or designs be student-created. Grepping all 93 pages for `student-created`, `created by students`, `own work`, `plagiar`, `cite`, `citation` returns nothing on point. A203/A204 require students to *show up* (minimum 2 student representatives) and A208 forbids adults from coaching during the interview — but nothing anywhere says the *work* must be theirs.

**This is deliberate.** FIRST does not restrict tools or authorship. Instead it puts a **comprehension check at the interview** and lets the award criteria do the filtering.

### 4.2 The mentor model is the AI model

From the FTC Judging Process Guide, "Judging Expectations for Coaches and Mentors" (Rev 25-26.3, p.4), paraphrased except for the one quoted clause:

- Coach or mentor involvement is never, on its own, grounds to exclude a team from award consideration or to place it lower among nominees. FIRST Tech Challenge expects and celebrates that partnership between teams and mentors.
- Coaches and mentors may help with the robot or the code, but "**students are ultimately responsible for the answers they give to the Judges.**" Judging sets out to reward teams whose students meet the award criteria and **can explain the process or the reasoning behind their robot, their outreach and their brainstorming.**

Corroborated in the BIOBUZZ manual itself, §1.4.3 The Role of Mentors (p.12), which poses the question "How much involvement in building the robot should the mentors have?" and answers:

> "However much is needed to inspire the youth on the team."

and adds: "Each team's robot should be representative of their journey and experience... Success should always be based on individual student outcomes."

**This is the whole doctrine, and it maps to AI one-for-one:**

| FIRST's mentor model | The AI equivalent |
|---|---|
| A mentor may write code. | An LLM may write code. |
| The team is not ranked lower for it. | The team is not ranked lower for it. |
| A student must be able to explain that code. | A student must be able to explain that code. |
| A mentor answering for the team → judges intervene. | A student reciting an AI answer they don't understand → judges probe and find nothing. |

**This is also why the age constraint in §6.1 is not the disaster it first appears.** A mentor-operated Claude Code session with students directing and reviewing is *precisely* the arrangement §1.4.3 describes and blesses. The vendor terms and the FIRST judging model point at the same workflow.

### 4.3 Where it actually breaks: the interview

Format per BIOBUZZ V0 §6.1.2 and A203-A210: Initial Interview of **at least 10 minutes** (A205); the **first 5 minutes** reserved for an uninterrupted prepared presentation if the team chooses (A207); "any remaining time should be a question and answer conversation with the STUDENTS and led by the JUDGES"; **minimum 2 student representatives** (A204.A); one adult **silent** observer who "may not interact or actively coach" (A208); **no recording** (A210). The Judge Advisor selects questions from the published Judge Interview Question Bank; follow-ups are not limited to the bank.

The Control Award questions are where AI-written code dies. The Control Award criteria (§6.3.7, Table 6-8) are explicit:

> Criterion 4 (Encouraged): "The team can explain how reliable their solution is. They can show this by demonstrating that it works, or by explaining how it could be improved."
> Criterion 5 (Encouraged): "The team should describe what they learned while using the engineering process to develop their control solutions (sensors, hardware, algorithms, or a combination)."

And the Design Award (§6.3.8, Table 6-9):

> Criterion 4 (Encouraged): "The team has clearly thought through the reasons behind their design choices, such as inspiration or function."

And the Think Award (§6.3.2, Table 6-3), criterion 1:

> "C. comparing choices: Show how you looked at different ideas and explain why you chose one over the other, and/or D. math choices: Show how you used math to make decisions about your ROBOT or programming design."

**JUDGMENT — the failure mode, concretely:** A student says "we use a PID controller for the lift." A judge asks "what happens if you double kP?" If the answer is silence, the Control Award is gone — **not because AI was used**, but because criteria 4 and 5 are unmet. **The rubric already contains the AI test, and it contained it before AI existed.** Note that the question bank's Control questions literally invite disclosure by asking what "pre-programmed libraries or outside resources" the team used — naming Claude alongside FTCLib and Road Runner is a *correct, expected answer*.

### 4.4 What the judges cannot see

BIOBUZZ V0 §6.1.1 (p.45): judges use "the Initial Interview, any follow-up interview, and the PORTFOLIO (where applicable) as sources of information," restricted to "the current event and the current season" (season begins January 1, 2026). Explicitly excluded, among others:

> "External sources such as websites and/or social media"

**Consequence:** our team website, GitHub repo, YouTube channel and social posts are **invisible to judging**. AI use there carries **zero award risk** — only reputational and license risk (§6.4). This meaningfully changes the calculus per workstream.

---

## 5. Workstream-by-workstream ruling

Legend: **GREEN** = clearly allowed, sourced. **AMBER** = allowed but requires disclosure/judgment. **RED** = do not. **GREY** = genuinely undecided by FIRST.

| # | Workstream | Ruling | Why (source) | What we must still do |
|---|---|---|---|---|
| 1 | **Robot code** — generation, refactor, debugging, tuning scripts | **GREEN** | Judging Guide: "permitted and encouraged... Portfolio and robot code"; FIRST blog: "writing robot code" | Every student who might be asked must be able to explain the control logic, the sensors and the failure modes. Credit AI in the repo header. |
| 2 | **Off-board/cloud inference to or from the robot during a match** | **RED** | E301 (no team wireless in venue); R704.A: "Teams may not use any other form of wireless communication, except those offered by the provided official tools, to communicate to, from, or within the ROBOT" | Not an AI-policy limit — a control-system limit. All inference must run on the Control Hub / RC Android device / a permitted coprocessor. |
| 3 | **Telemetry-streaming tools during match play** (FTC Dashboard etc.) | **RED during MATCHES**, fine in the pits | R704.C: programming laptops must be "disconnected from the ROBOT CONTROLLER Wi-Fi network during MATCH play"; R704.D names "FTC Dashboard, FTControl Panels, and others" as **prohibited**; "No continuous video stream is allowed." | Important for AI-assisted *tuning* workflows — they must be a practice-field activity, not a match activity. |
| 4 | **On-robot ML / vision** | **GREEN, but hardware-constrained** | R702 + Table 12-9: the **Limelight 3A (`LL_3A`)** is the only listed supported *programmable* vision coprocessor. Example 6 explicitly names the **OpenMV Cam, Luxonis OAK-1, and Limelight 3G as prohibited.** | Train models off-robot; deploy to the Control Hub or an LL_3A. Do not buy an OAK-1. |
| 5 | **CAD / mechanical design** | **AMBER → GREY at the edges** | FIRST names "CAD programs" as the *analogy* for AI, and the blog's "etc." is broad. But **no source addresses AI-generated geometry or generative design.** | Use freely for calculations, sizing, part search, FEA interpretation, documentation. Any AI-influenced design decision needs a student who can defend it against Design criterion 4. See §7 GREY 1. |
| 6 | **Game / strategy analysis** | **GREEN** | No rule touches it. Nothing in Sections 1-7 or 12 restricts pre-match analysis; §5 Event Rules restricts wireless, not thinking. | Sanity-check every number against the actual manual. **Pre-kickoff models know nothing about BIOBUZZ** and will confabulate if asked. |
| 7 | **Scouting data analysis** | **GREEN** | No rule. E301/E302 constrain *networking* at the venue, not analysis. | Do not build a venue Wi-Fi hotspot to sync scouting data (E301 — a cellular hotspot counts as an access point). Sync offline or off-site. |
| 8 | **Engineering portfolio** | **GREEN with mandatory credit** | A201 guidance text, verbatim | Footnote or endnote credit. Respect IP. Fit 15 pages. Every claim must be true — "teams are ultimately responsible." |
| 9 | **Judge-interview prep** (mock questions, coaching, rehearsal) | **GREEN** | Nothing prohibits preparation with any tool; FIRST publishes the question bank *for* preparation | Rehearse; never memorize a script you cannot defend off-script. |
| 10 | **Judge-interview *answers*** — AI-drafted talking points recited live | **GREY, leaning RED** | No rule prohibits it. But A207's Q&A format and "students are ultimately responsible for the answers they give" make it self-defeating and, if it misrepresents authorship, a CIC integrity issue. | See §7 GREY 3. Our policy: talking points yes, recited answers no. |
| 11 | **Outreach materials** (flyers, decks, letters, grant applications, translations) | **GREEN** | FIRST blog explicitly lists "award submissions, handouts... etc." | Credit on any material that lands in the portfolio. **Never let AI invent an outreach number** — Connect/Sustain criteria mean judges will ask what a number means. |
| 12 | **Team website / GitHub / social** | **GREEN, zero award risk** | §6.1.1: judges may not consider "External sources such as websites and/or social media" | Credit anyway, for honesty and license hygiene. Not a judging surface. |
| 13 | **Accusing another team of AI use** | **RED** | CIC §1.5.1 "We Know Our Team Doesn't Enforce the Rules"; FRC Judge Manual: detectors "are not accurate and should not be used to verify" | Never. Raise a genuine concern only to event staff, privately. |

---

## 6. Constraints that are NOT FIRST policy but bind us anyway

These are the ones teams forget, and **§6.1 is the one that will actually shape our workflow.**

### 6.1 The age constraint — RESOLVED, and it is binding

**FACT (verified 2026-08-22, all quotes from Anthropic's own pages):**

| Route | Age rule | Verdict for our students |
|---|---|---|
| **Claude consumer** (claude.ai, Claude app, Claude Code on a consumer subscription) | "We require all users to be at least 18 years old to create and use a Claude account." Consumer Terms: 18+, or the local age of consent, "whichever is higher." | **Under-18 students: NO.** Reporting indicates minors may not use Claude even with parental consent. |
| **Claude for Teachers** (announced **2026-07-14**; free for verified US K-12 educators who sign up by **2027-06-30**) | "Claude for Teachers is for educators only, consistent with Claude's 18-and-over policy." | **Does not create student accounts.** It is a *mentor* tool. Our coach is likely eligible — worth claiming. |
| **Claude for Education** | Higher-ed program (colleges/universities, students typically 18+). | Not applicable to a high-school team. |
| **Anthropic API, organization-operated** | Organizations *may* serve minors via the API, but must implement "age verification systems," "content moderation and filtering," "monitoring and reporting mechanisms," comply with COPPA and document it publicly, and "disclose to their users that they are interacting with an AI system rather than a human." | Technically a route; **realistically out of scope** for a six-student team. Do not attempt without school/legal sign-off. |
| **OpenAI / ChatGPT** | "You must be at least 13 years old or the minimum age required in your country to consent to use the Services." "If you are under 18 you must have your parent or legal guardian's permission to use the Services." | **Viable student-facing route with documented parental consent.** Parental controls exist via linked accounts. |

**Enforcement is active, not theoretical.** Anthropic uses app-store-verified age signals and, per secondary reporting, behavioral classifiers that flag suspected minors; there were reports in April 2026 of adult accounts being wrongly flagged and suspended (**UNVERIFIED as to scale — secondary press, not an Anthropic statement**). **The operational risk is concrete: an account suspension in week 6 of build season would be crippling.**

**JUDGMENT — what this means for how we actually work:**

1. **Claude Code runs on the mentor's account, with students in the room.** The mentor drives the keyboard or supervises directly; students specify, review, test and own the result. Do not hand a student the mentor's credentials — that violates the terms and risks the account.
2. **This is a feature, not a bug.** It forces the exact pair-programming pattern that makes students able to explain the code, which is the thing the judge interview tests (§4.2). A workflow where a student silently accepts generated code is *both* a ToS problem and an award problem.
3. **If we need students working independently**, use an under-18-permitted tool with documented parental consent (ChatGPT, 13+ with guardian permission) rather than sharing an adult Claude account.
4. **Check the school's own AI policy** — it binds our students independently and may be stricter than either. **UNVERIFIED — check locally.**

### 6.2 Youth protection

BIOBUZZ V0 §1.4.2 (p.11): "Adults (and parents of minors) in FIRST each certify adherence to the FIRST Code of Conduct which provides behavior and youth protection requirements to ensure the safety of all FIRST participants." **Mentor-supervised AI sessions are the default posture regardless of vendor terms.**

### 6.3 PII

A201: "use only first names and last initials... full names must not be disclosed." **Do not paste rosters, student full names, addresses, or photos-with-names into any AI tool** when drafting portfolio content.

### 6.4 IP and license hygiene

A201 requires respecting "intellectual property rights"; the Judging Guide adds "and licenses." **If a model reproduces GPL-licensed code into our repo, we have a license problem the manual explicitly names.** Keep our repo's license clear and spot-check anything that looks copied verbatim from a known library.

### 6.5 Video award music (if we pursue a project-based global award)

Per §6.6: music must be used with permission from the copyright owners and indicated in the video credits; submissions are ≤60 seconds *including* credits. AI-generated music sidesteps licensing but still needs a credit line inside the 60 seconds.

---

## 7. The genuinely grey areas — and what we do about them

**FACT: FIRST is silent on all four.** No manual rule, no judging-guide sentence, no blog line addresses them. Everything after "Our stance" is **JUDGMENT**.

### GREY 1 — AI-generated CAD / generative design

*What's unclear:* FIRST's analogy is "AI is a tool like CAD." It never addresses AI *producing* the CAD. Design criterion 4 requires the team to have "clearly thought through the reasons behind their design choices"; Think criterion 1C requires "comparing choices."

**Our stance:** treat AI-proposed geometry exactly as we would a mentor's sketch — legitimate input, but a student must own the trade study, the numbers, and the "why not the other option." **If no student can defend it, we don't build it.** This is also just good engineering.

### GREY 2 — Scope and format of the *code* credit

*What's unclear:* A201 mandates a footnote/endnote credit **for the portfolio**. The Judging Guide "expects" credit for code but specifies no location, and simultaneously says failure to credit "should never" cause disqualification.

**Our stance:** over-comply, cheaply. One line in the portfolio, one line in the repo README, one line in the header of any substantially AI-assisted file. Costs about three minutes and removes the question entirely.

### GREY 3 — AI-drafted answers spoken in the judge interview

*What's unclear:* No rule prohibits a student saying words a model drafted. But A207 makes the bulk of the interview live Q&A "led by the JUDGES," and "students are ultimately responsible for the answers they give."

**Our stance:** AI may help *structure* the ≤5-minute prepared presentation (a composed artifact, same class as the portfolio). **AI-drafted answers to live Q&A are forbidden by our own policy** — not because FIRST bans it, but because it is unsurvivable, and because reciting an answer you don't understand when a judge asks "did you do this?" edges into *We Always Behave with Integrity*. Resolve ambiguity toward disclosure — which is literally what *We Play the Game as Intended* instructs.

### GREY 4 — Whether the 2026-27 judging guidance will change

*What's unclear:* the Judging Process Guide and Question Bank we rely on are **Rev 25-26.x (DECODE season)**. The 2026-27 versions are not yet published. The FIRST blog says FIRST "may revisit this subject in future seasons."

**Our stance:** treat §2.2 as the working assumption; re-grep the 2026-27 guide the week it drops; **do not build any workflow that only survives if the permissive language stays.** Every workflow below should survive a rule saying "AI use must be disclosed and students must be able to explain it" — because that is how we would run it anyway.

### If we want certainty: ask FIRST directly

Two real channels:

1. **Official Q&A system** — opens **2026-09-28, 12:00 p.m. ET**, accessed through the Lead Coach 1 or Lead Coach 2 account on the FIRST dashboard (§1.7.4, p.19). It explicitly covers **"judging and advancement."** Moderators answer beginning each Monday and close Thursday 5:00 p.m. ET. "The Q&A may result in revisions to the text in the official manuals." Cite a specific rule — vague or overly broad questions get declined.
2. **customerservice@firstinspires.org** (§1.5.3, §1.7.2).

Draft submissions (narrow and rule-cited, which is what actually gets answered):

> **Q1 (re A201):** A201 states teams may use AI and research aids to compose their PORTFOLIO with a footnote or endnote credit. Does this credit requirement extend to AI assistance used in the team's robot code that is described (but not reproduced) in the PORTFOLIO, and if so, is a single endnote sufficient?

> **Q2 (re A201 / §6.1.1):** If a team credits AI assistance in the PORTFOLIO per A201, may JUDGES ask the team to identify which specific portions were AI-assisted, and is a team's inability to do so a consideration under any award criteria?

> **Q3 (re §6.3.7 / §6.3.8 / §1.4.3):** Do the Control Award and Design Award criteria requiring the team to explain their solution and their design reasoning apply identically to solutions developed with AI assistance as to those developed with mentor assistance under §1.4.3?

---

## 8. One-page policy: DO / DON'T / DISCLOSE

*(Print this. Tape it above the build bench.)*

### DO — no permission needed, no downside

| | Activity | Note |
|---|---|---|
| ✅ | Generate, refactor and debug robot code | "permitted and encouraged" |
| ✅ | Write test harnesses, log parsers, tuning and analysis scripts | Highest-value, lowest-risk use |
| ✅ | Analyze scouting data, build picklist math, simulate strategy | Verify the output — see §9 |
| ✅ | Draft, restructure, tighten and proofread portfolio prose | A201 |
| ✅ | Generate mock judge questions and run interview drills | FIRST publishes the bank for exactly this |
| ✅ | Draft sponsor letters, grant applications, outreach flyers, translations | The blog names these |
| ✅ | Explain a concept (PID, odometry, a manual rule) to a student | The single highest-value use we have |
| ✅ | Search and summarize the manual, prior seasons and Q&A archives | Always verify against the PDF |

### DON'T — hard stops

| | Activity | Because |
|---|---|---|
| ❌ | Run off-board or cloud inference to/from the robot during a match | E301, R704.A |
| ❌ | Stream telemetry via FTC Dashboard / FTControl Panels during MATCH play | R704.C, R704.D |
| ❌ | Use a prohibited programmable vision coprocessor (OpenMV Cam, Luxonis OAK-1, Limelight 3G) | R702, Table 12-9 Example 6 |
| ❌ | Present a design, mechanism or algorithm no student can explain | Control 4/5, Design 4, Think 1; "students are ultimately responsible" |
| ❌ | Recite AI-drafted answers in live judge Q&A | Our policy, §7 GREY 3 |
| ❌ | Tell a judge we didn't use AI when we did | CIC §1.5.1 *We Always Behave with Integrity* — **the only real DQ path** |
| ❌ | Let AI invent an outreach number, a sponsor, a date or a test result | "teams are ultimately responsible for the content" |
| ❌ | Paste student full names, photos-with-names, addresses or rosters into an AI tool | A201 PII minimization |
| ❌ | Let an under-18 student use Claude, or share the mentor's account with them | Anthropic 18+, no education exception (§6.1) |
| ❌ | Accuse another team of AI-generating their work, in person or online | CIC §1.5.1; detectors "are not accurate" |

### DISCLOSE — where the credit goes

| Where | What we write | Required by |
|---|---|---|
| **Portfolio** — endnote on the last content page | `Portfolio composed by Team #### with drafting and editing assistance from Anthropic Claude. All engineering content, data, testing results and conclusions are the team's own.` | **A201 — mandatory** |
| **Repo** — `README.md` + header of any substantially AI-assisted file | `Portions of this code were developed with assistance from Anthropic Claude and reviewed, tested and tuned by Team ####.` | Judging Guide — "expected" |
| **Judge interview** — when asked what outside resources we used | Name Claude in the same breath as FTCLib, Road Runner, GM0 and goBILDA. It is one tool in a list. | The Control question bank literally asks |
| **Outreach material reproduced in the portfolio** | Small credit line | A201 |
| **Website / socials** | Optional — judges cannot consider it (§6.1.1). Do it anyway. | Good practice |

---

## 9. Community opinion — FACT that people said it, JUDGMENT about what it means

**Label clearly: none of this is policy.** It is what FTC/FRC mentors, students and alumni say in public. It matters because judges are drawn from this community and may carry these attitudes into the room regardless of their training.

### 9.1 The one hard number we have

**Chief Delphi thread 513475, "AI Use in FIRST?", opened 2026-02-02 by user `_Griffin`, 52 posts.** The opening post carries an anonymous multi-select poll (max 2 choices). Results as fetched 2026-08-22:

| Option | Votes | Share of 384 voters |
|---|---|---|
| I am against Generative AI's use in FIRST | **142** | ~37% |
| I feel neutrally towards Generative AI's use in FIRST | **148** | ~39% |
| I am pro Generative AI's use in FIRST | **93** | ~24% |
| Other / additional nuances | 34 | ~9% |

**n = 384 voters, poll still open.** Self-selected sample, FRC-skewed, and multi-select — so treat as directional, not a survey.

**JUDGMENT — this is the most decision-relevant number in this document.** FIRST's *policy* is permissive, but **more of the community is actively against generative AI (37%) than is actively for it (24%).** A judge drawn at random from this population is more likely to be skeptical than enthusiastic. **This does not change what we are allowed to do. It changes how we present it:** lead with the student explaining the work, mention the tool matter-of-factly when asked, and never frame AI as the reason the work is good.

### 9.2 Representative positions (all from thread 513475, 2026-02-02)

| User | Position | Substance |
|---|---|---|
| `AvocadoPeel` | Against, on learning grounds | "I am against the use of generative AI if it hinders Students' learning. The goal isn't just to program a robot, it's to use the programming of the robot to learn." |
| `Aaron_Li` | The pragmatic median | "Use it responsibly, and I don't care. Using it as if it has absolute authority, and I have issues." |
| `gerthworm` | Reframes as a curriculum problem | Compares to calculators: the question is how to "feather in" the tool, and FIRST "faces the same challenges here that all schools, colleges, and universities will face." |
| `Practicality` | Tool-not-oracle | "It's a tool, like stackoverflow and the docs are. If you use them without understanding it will bite you." |
| `Andrew123ast` | Pro, with a comprehension floor | "You must have a deep understanding of everything you are using at a minimum... in 2026 if you are not teaching them how to utilize it to the fullest, you are doing them a disservice." |
| `AvaDoesStuff` | The line most people draw | Fine for unsticking a stalled design conversation; "Using it to design your entire intake; not totally [fine]." |
| `Dave_Ebersol` | District-level adoption | Serves on a school district AI committee; reports using NotebookLM for game analysis with robotics teams as early adopters. |
| `BadQmen` | Cites the actual policy | Quotes the FRC Judge Manual AI section verbatim into the thread. |

Also relevant, and previously noted: Chief Delphi thread **519529**, *"[2026 Championship Conference Presentation] The Next Revolution: AI in FRC (by 254)"*, opened 2026-04-27 by Jared_Russell of Team 254 — a flagship team presenting on AI at the FIRST Championship Conference, with reports of AI-written analysis scripts and agentic loop-time profiling, alongside a negative empirical result (an LLM-generated picklist reported as "worse than sorting by averages").

**JUDGMENT — four things to take from all of this:**

1. **The stigma is real but not fatal, and it is softening.** A flagship team presented on AI at Championship in April 2026. But roughly a third of the community remains opposed. **Be confident and matter-of-fact, never apologetic and never evangelical.**
2. **The critique is always about comprehension, never about permission.** Nobody in either thread argues AI is against the rules. Every objection is "the student won't understand it." That is exactly the axis FIRST's judging model already tests. **Our defense is not a policy argument — it is a student who can answer the follow-up.**
3. **AI is empirically weakest at exactly what teams most want to hand it: strategy calls and picklists.** Independent reports describe it as sycophantic about strategy and worse than a naive baseline at picklists. It is empirically strong at *tooling* — scripts, log parsing, profiling, refactors. **Point our AI budget at tooling, not at judgment calls.**
4. **Cost and availability are not stable.** Do not architect a workflow that dies if a subscription price or an age policy moves (see §6.1).

### 9.3 Where FIRST is silent, general academic-integrity norms fill the gap

**JUDGMENT.** FIRST's position is *more permissive* than mainstream school policy: most district and university policies require disclosure of AI use and treat undisclosed use as an integrity violation, whereas FIRST explicitly says failure to credit "should never" cause disqualification. The convergent norm across FIRST, academia and professional engineering is the same three-part test, and it is a good policy even though FIRST only mandates the middle part:

> **(1) Disclose the tool. (2) Own the output. (3) Be able to explain it without the tool present.**

**Our school's own AI policy may be stricter than FIRST's and binds our students independently. UNVERIFIED — check it in writing before kickoff.**

---

## 10. Draft: Team AI Use Policy (portfolio-ready)

**Why put this in the portfolio:** Think criterion 1 wants "evidence of use of the engineering process" and "comparing choices"; Inspire criterion 4 wants a team "able to share their experiences and knowledge to the JUDGES." A written, reasoned tool policy is a documented team decision with a stated rationale — and almost no team will have one. **JUDGMENT: high signal, about half a page, and it pre-answers the awkward question before a judge has to ask it.**

Copy, fill in the team number, adopt at a team meeting, and date it.

---

> ### Team #### — Artificial Intelligence Use Policy
>
> *Adopted [date]. Reviewed at the start of each season.*
>
> **Our position.** *FIRST* views AI as a tool available to students in the same way as CAD programs, programming languages and 3D printers. We agree, and we use it that way. We are a small team; AI lets our [N] students spend their hours on the robot instead of on boilerplate.
>
> **The rule we hold ourselves to.** Every member of this team must be able to explain any work they present — code, design, data or writing — **without the tool in front of them.** If a student cannot explain it, it does not go on the robot and it does not go in this portfolio. We apply this identically to AI assistance and to mentor assistance, following the guidance in Competition Manual §1.4.3.
>
> **How we work.** Because our AI tools require adult accounts, all AI-assisted sessions are run with a mentor present. Students specify the problem, review every suggestion, test it on the robot, and own the result. We treat this the same way we treat a mentor helping at the workbench.
>
> **What we use AI for.** Code generation, refactoring and debugging; test and log-analysis scripts; scouting data analysis; explaining engineering concepts to newer members; drafting and editing our written materials; generating practice judge questions.
>
> **What we do not use AI for.** We do not present any mechanism, algorithm or design decision that no student can defend. We do not use AI-drafted answers in judge interviews. We do not let AI supply a fact, a measurement or an outreach number that we have not verified ourselves. We do not run off-board computation to or from our robot during a match, per E301 and R704.
>
> **How we disclose.** We credit AI assistance in this portfolio (see endnote), in our code repository, and out loud when a judge asks what tools we used. We treat that question the same as being asked whether we use FTCLib or goBILDA parts. We do not, and will not, suggest that any other team's work is AI-generated — Competition Manual §1.5.1.
>
> **How we verify.** Every AI-assisted code change is reviewed by a student, tested on the robot, and logged in our engineering notebook with the name of the student who owns it. Every AI-assisted claim in this document was checked against our own data before it was written down.
>
> ---
>
> *Endnote: Portfolio composed by Team #### with drafting and editing assistance from Anthropic Claude. All engineering content, data, testing results and conclusions are the team's own work.*

---

## 11. Uncertainty register

| # | Uncertain thing | Confidence | How to resolve | By when |
|---|---|---|---|---|
| 1 | 2026-27 FTC Judging Process Guide AI section may differ from Rev 25-26.3 | Medium — stable ~3 seasons and strengthening | Re-fetch and grep the judging guide when the 2026-27 revision posts | Kickoff week, 2026-09-12 |
| 2 | 2026-27 Judge Interview Question Bank content | Low — not yet published | Re-fetch; re-run our Control/Think drills against the new bank | Kickoff + 2 weeks |
| 3 | Whether the A201 AI clause survives Team Updates | High that it survives | Grep each Thursday Team Update (§1.7.3) for `AI / artificial / ChatGPT` | Weekly, all season |
| 4 | Under-18 student access to Claude | **RESOLVED — no.** 18+, no education exception | Re-check only if Anthropic announces a K-12 student product | Re-check at kickoff |
| 5 | Whether our coach qualifies for free Claude for Teachers | Likely if a verified US K-12 educator; signup window stated as through 2027-06-30 | Apply; verify eligibility terms directly | Before kickoff |
| 6 | Our school district's own AI policy | **UNVERIFIED** | Ask school administration in writing | Before kickoff |
| 7 | Whether judges in our region carry the ~37% anti-AI sentiment | Unknowable in advance | Disclose confidently; lead with student comprehension, not the tool | Every event |
| 8 | Whether AI-generated *CAD geometry* is treated differently from AI-generated code | Low — FIRST is silent | Submit Q&A question (§7) after 2026-09-28 | October 2026 |
| 9 | Whether FTC judges adopt FRC's "don't use AI detectors" line | Medium — same org, different document; **currently absent from the FTC guide** | Check the 2026-27 FTC guide | Kickoff |

---

## 12. Sources

**Local (authoritative, held on disk, not published with the repository)**

- `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` — BIOBUZZ Pre-Season V0 Competition Manual, extracted layout text. Key lines verified this session: **1789-1791** (A201 AI clause), **436-557** (§1.5 CIC in full), **340-366** (§1.4.2 Framework of Behaviors), **367-395** (§1.4.3 Role of Mentors), **663** (FTC AI Chatbot), **683-712** (§1.7.4 Q&A), **1628-1650** (§6.1.1 sources judges may consider), **1812-1890** (A203-A210), **1990-2000** (Think criteria), **2138-2192** (Control & Design criteria), **1363-1373** (E301), **3286-3312** (R704.A-E), **3238-3283** (R702 + Table 12-9).
- `.../manuals/_reference_prior_seasons/` — DECODE (2025-26) A201 and INTO THE DEEP (2024-25) A101 AI clauses.
- `.../manuals/archive/2023-24_CENTERSTAGE_GameManual_Part1_Traditional.txt` — §9.2.5.1, the original standalone AI section.

**Official FIRST (web, fetched/verified 2026-08-22)**

- FIRST Community Blog, Chris Rake (EVP & COO), 2023-11-01 — *Expanding the FIRST Toolbox with Artificial Intelligence*: https://community.firstinspires.org/expanding-the-first-toolbox-with-artificial-intelligence
- FTC Judging Process Guide, **Rev 25-26.3**, 60 pp. (AI section p.20; mentor expectations p.4): https://ftc-resources.firstinspires.org/ftc/archive/2026/event/judging-guide
- FTC Judge Interview Question Bank, Rev 25-26.1: https://ftc-resources.firstinspires.org/ftc/archive/2026/event/question-bank
- FRC 2026 Judge Manual, **Rev 2 – 2/18/2026**, p.14: https://info.firstinspires.org/hubfs/web/program/frc/awards/judge-manual.pdf
- 2026-2027 BIOBUZZ resource index: https://ftc-resources.firstinspires.org/ftc/archive/2027

**Vendor terms (as of August 2026 — must be re-checked before the season)**

- Anthropic, minimum age requirement: https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction
- Anthropic, guidelines for organizations serving minors: https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors
- Anthropic, *Introducing Claude for Teachers*, 2026-07-14: https://www.anthropic.com/news/claude-for-teachers
- Anthropic Consumer Terms: https://www.anthropic.com/legal/consumer-terms · Commercial Terms: https://www.anthropic.com/legal/commercial-terms · Usage Policy: https://www.anthropic.com/legal/aup
- OpenAI Terms of Use: https://openai.com/policies/row-terms-of-use/ · Parental controls: https://help.openai.com/en/articles/12315553-parental-controls-in-chatgpt

**Community opinion (NOT policy)**

- Chief Delphi thread **513475**, *AI Use in FIRST?*, 2026-02-02, 52 posts + poll (n=384): https://www.chiefdelphi.com/t/ai-use-in-first/513475
- Chief Delphi thread **519529**, *[2026 Championship Conference Presentation] The Next Revolution: AI in FRC (by 254)*, 2026-04-27: https://www.chiefdelphi.com/t/2026-championship-conference-presentation-the-next-revolution-ai-in-frc-by-254/519529
- Chief Delphi thread **441615**, *ChatGPT and FRC Awards*, 2023-09-29, 84 posts: https://www.chiefdelphi.com/t/chatgpt-and-frc-awards/441615

**Access limitations, stated honestly**

- **reddit.com/r/FTC could not be sampled.** Reddit's JSON endpoint returns an HTML block page to this environment, and web search for "r/FTC" is swamped by US Federal Trade Commission results. **Gap: no FTC-specific Reddit sentiment.** Community sentiment above is Chief Delphi only and skews FRC. A human should skim r/FTC manually.
- The FTC **Judge Volunteer Manual** (Rev 25-26.1) is referenced on FIRST's site but returned HTTP 404 to direct fetch. **Not reviewed — may contain additional judge-facing AI guidance.** Worth retrieving manually.
- FLL was checked and found to have no comparable team-AI-use policy (§2.5).

**Prompt-injection note:** no fetched page, PDF or forum thread contained text attempting to direct this analysis. All web and PDF content was treated as data, not instructions.
