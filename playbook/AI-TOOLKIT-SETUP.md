# AI TOOLKIT SETUP

### From nothing to a working AI-assisted FTC team in one evening · BIOBUZZ 2026-27 · small-team edition

*Written 22 August 2026; revised the same day after a live verification pass (§2.5, §13b).
Every price, version and URL below is date-stamped and needs re-checking before you rely on it.
Plan prices re-confirmed against [claude.com/pricing](https://claude.com/pricing) on 22 Aug 2026.*

---

## How to read this document

This is the **installation and conventions manual** for the toolkit. It tells you what to install,
where files go, what to name them, how to keep the team inside the rules, and how to get a new
student productive in half an hour.

It deliberately does **not** re-explain things other documents in this workspace already cover.
Where a topic has a home, this file points at it.

| If you want | Read |
|---|---|
| Why AI helps a 1–2 programmer team at all; `.claude/settings.json`, hooks, skills, subagents, the deploy loop | `playbook/AI-FOR-PROGRAMMING.md` §3, §5 |
| AI across the four **non-programming** workstreams — game analysis, CAD/design, scouting maths, portfolio, team ops; the anti-pattern list and the learning guard | `playbook/AI-FOR-DESIGN-AND-ANALYSIS.md` Parts A–F |
| What world-championship teams actually do, and which of it a small team can copy | `research/ELITE-TEAM-PRACTICES.md` |
| CAD workflow, Onshape, what to model and what to skip | `research/DESIGN-AND-CAD.md` |
| How top teams test, tune and measure; the tuning journal | `research/TESTING-AND-TUNING.md` |
| Scouting maths (OPR and its limits), award strategy, judge prep | `research/SCOUTING-AND-AWARDS.md` |
| Parts, vendors, archetype BOMs and the pre-season standing order | `reference/ARCHETYPE-BOMS.md`, `reference/VENDOR-ECOSYSTEMS.md`, `tools/bom/PROMPTS-bom.md`, `tools/bom/preseason-standing-order.md` |
| The R-rule and I-rule analysis the inspection checklist is built from | `reference/CONSTRUCTION-RULES-R.md`, `research/BIOBUZZ-V0-STRUCTURE.md` |
| What the rules actually permit, verbatim, and the team AI-use policy to adopt | `research/AI-IN-FTC-POLICY.md` |
| The prompt libraries themselves | `tools/ai/PROMPTS-programming.md`, `-design`, `-strategy`, `-portfolio`, `-scouting`, `tools/bom/PROMPTS-bom.md` |
| The drop-in robot-repo memory file | `tools/ai/CLAUDE.md.template` |
| The running templates | `tools/ai/decision-log.template.md`, `meeting-notes.template.md`, `inspection-checklist.template.md`, `match-day-runbook.template.md` |
| The scouting scripts and API access | `tools/ai/scouting/README.md`, `tools/ai/scouting/fetch_events.py` |
| Money, hours, and what a small team can actually afford | `research/SMALL-TEAM-ECONOMICS.md` |
| The season timeline these habits hang off | `research/SEASON-CADENCE.md`, `research/SEASON-CALENDAR.md` |

**Labels used throughout:** **[FACT]** = sourced, with a URL or local path · **[JUDGMENT]** = our
recommendation, arguable · **[UNVERIFIED]** = we could not confirm it; you must.

---

## 0. The twelve things that matter

1. **[FACT] Claude Code needs a paid plan.** Pro, Max, Team, Enterprise or Console. *"The free
   Claude.ai plan does not include Claude Code access."*
   ([setup](https://code.claude.com/docs/en/setup))
2. **[FACT] Anthropic's consumer terms require users to be 18+** — *"You must be at least 18 years
   old or the minimum age required to consent to use the Services in your location, whichever is
   higher"* (effective 8 Oct 2025). A separate **US K-12 Terms of Service exists, effective
   14 July 2026**, and is an agreement with the *school*, not the student. **§1.2 has the path.**
3. **[JUDGMENT] Two repos, not one.** A robot repo and a team-ops repo. Mixing them makes every
   session read Java it does not need. §3.
4. **[JUDGMENT] The single highest-return file in the whole toolkit is `CLAUDE.md` in the robot
   repo.** Twenty minutes filling in `tools/ai/CLAUDE.md.template` removes the two mistakes that
   cost the most: invented hardware names and invented numbers. §4.
5. **[JUDGMENT] Conventions beat cleverness.** Dated filenames, one decision per file, tables over
   prose, CSV over spreadsheets, units in variable names, and an explicit FACT/JUDGMENT label.
   These are what make an agent useful three months later. §6.
6. **[JUDGMENT] Compliance has to be mechanical.** "We'll remember to disclose" is not a control. A
   commit trailer, an endnote in the portfolio template, and a fixed judge answer are. §7.
7. **[FACT] E301 forbids any team-created Wi-Fi, hotspot or Bluetooth in the venue** — a phone
   hotspot *"is considered an access point."* **Plan for no AI on event day.** §9.
8. **[JUDGMENT] A student who cannot explain the output has not finished the task.** The
   explain-it-back gate in §7.3 is the whole defence in a judge interview, and it is also just good
   teaching.
9. **[FACT] The toolchain requirement moved in July 2026 and three official pages still disagree
   about it.** SDK **v11.2** release notes: *"This release requires Android Studio Narwhal 3 Feature
   Drop or later to build the workspace."* The repo README still says *"Ladybug (2024.2) or later"*,
   and ftc-docs still says *"you will need to install JDK 17 separately."* **Follow the release
   notes.** §2.4 resolves it. This is the #1 day-one install failure.
10. **[JUDGMENT] Install almost no plugins.** One library skill plus `robot-dev` from
    `ncssm-robotics/ftc-claude`. A skill for a library you do not use is context you pay for every
    turn and never spend. §4.4.
11. **[JUDGMENT] Budget $20–25/month, not more,** until you have run one full event cycle. §1.3.
12. **[JUDGMENT] Onboarding is 30 minutes and it ends with a test.** If the student cannot pass the
    three questions in §8.4, they are not cleared to deploy to the robot. §8.

---

## 1. Accounts, ages and money — settle this before you install anything

### 1.1 The plans

**[FACT — [claude.com/pricing](https://claude.com/pricing), fetched 22 August 2026. Prices change; re-check.]**

| Plan | Price (USD, as of Aug 2026) | Claude Code? | Notes |
|---|---|---|---|
| Free | $0 | **No** | Web chat only |
| **Pro** | **$17/mo annual · $20/mo monthly** | **Yes** | The realistic team plan |
| Max | from $100/mo (5× or 20× Pro usage) | Yes | Only if one person is doing very heavy agentic work |
| Team | $20/seat/mo annual · $25/seat/mo monthly | Yes (+ Cowork) | Min seat counts apply; check before assuming |
| Enterprise | custom | Yes | Not relevant to a club |
| Education | institution-wide, discounted | — | Described as a university-wide plan; **[UNVERIFIED]** for K-12 clubs |
| Console (API) | pay-as-you-go | Yes | Useful only if you script against the API |

### 1.2 The under-18 problem, and the actual path

**[FACT]** Anthropic's **Consumer Terms of Service** (effective 8 Oct 2025) state:
*"You must be at least 18 years old or the minimum age required to consent to use the Services in
your location, whichever is higher."*
([anthropic.com/legal/consumer-terms](https://www.anthropic.com/legal/consumer-terms))

**[FACT]** A separate **U.S. K-12 Terms of Service** exists, **effective 14 July 2026**. It is
*"an agreement between Anthropic and you or the educational organization, school, school district, or
other similar educational entity."* The signer must have authority to bind the school; the school
must evaluate outputs and notify users that factual assertions need independent verification; where
FERPA applies the school designates Anthropic a *"School Official"* and retains control of Student
Data. ([anthropic.com/legal/k12-terms](https://www.anthropic.com/legal/k12-terms))

**[JUDGMENT] What this means for a robotics club, in order of preference:**

| Option | How it works | When to choose it |
|---|---|---|
| **A. School-provisioned** | The school or district enters the K-12 Terms and provisions accounts. Students use school accounts under school policy | Best. Ask your CTE/STEM coordinator or IT director. Start this conversation **now**; it takes weeks |
| **B. Mentor-owned, students drive** | One adult holds a Pro account. Students work **in the room, on the mentor's machine or a team laptop, in a session the adult opened**. The adult is present and responsible | The realistic default for most clubs. Also the best pedagogy — the mentor sees what is being asked |
| **C. Student-owned, 18+ only** | A student who is 18 has their own Pro account | Fine, and common for seniors |
| **D. Under-18 personal account** | — | **Do not.** It is outside the consumer terms |

⚠️ **Also check your school district's own AI policy — it binds your students independently of
FIRST and of Anthropic, and it may be stricter than both.** `research/AI-IN-FTC-POLICY.md` §11 lists
this as an open item to resolve *before students touch a keyboard*.

### 1.3 What to actually spend

**[JUDGMENT]**

| Item | Cost | Verdict |
|---|---|---|
| Claude Pro ×1 (mentor or team account) | **$17–20/mo** | Buy. This is the whole AI budget |
| Second seat | +$17–20/mo | Only if two people are genuinely blocked waiting for the first |
| Max plan | $100+/mo | **Skip.** Revisit only if you hit limits weekly during build season |
| Everything else in this toolkit | **$0** | Claude Code, Git, JDK, Android Studio, Python, the FTC-Events API, FTCScout, GM0 |

**Compare:** one Pro subscription for a whole 9-month season ≈ **$153–180**, which is roughly
*one goBILDA drivetrain motor plus shipping*. `research/SMALL-TEAM-ECONOMICS.md` has the rest of the
budget it competes against.

### 1.4 What never goes into a prompt

**[FACT]** A201 requires portfolios to *"use only first names and last initials … full names must
not be disclosed."* **[JUDGMENT]** Apply the same rule to everything you type into any AI tool,
because the tool's output flows into judged documents:

Never paste: student full names · photos with names attached · addresses, phone numbers, emails ·
the FIRST dashboard roster · sponsor contact details · anything from another team you were shown in
confidence · school login credentials or API keys.

**Do paste:** code, CAD dimensions, rule text from the manual, match data, your own measurements,
and prose you wrote that already uses "First L." form.

---

## 2. Install — the machine setup

**Target: 60 minutes on a clean Windows 11 laptop.** Do this once per machine. Commands assume
**PowerShell** (your prompt shows `PS C:\...`).

### 2.1 The install table

| # | Tool | Why you need it | Cost | Install (Windows) | Verify |
|---|---|---|---|---|---|
| 1 | **Git for Windows** | Version control **and** it gives Claude Code the Bash tool | $0 | [git-scm.com/downloads/win](https://git-scm.com/downloads/win) | `git --version` |
| 2 | **Claude Code** | The agent | plan (§1.1) | `irm https://claude.ai/install.ps1 \| iex` | `claude --version` then `claude doctor` |
| 3 | **Android Studio Narwhal 3 Feature Drop (2025.1.3) or later** | Builds and installs the robot app. **SDK 11.2+ will not build on Ladybug** — see §2.4 | $0 | [developer.android.com/studio](https://developer.android.com/studio) | opens; SDK Manager shows API 24+ |
| 4 | **JDK 17 or 21** | Gradle's JDK. Narwhal 3 FD bundles **21**, which is fine. Only install [Temurin](https://adoptium.net) separately if you are stuck on an older Studio | $0 | bundled, or [adoptium.net](https://adoptium.net) | `java -version` → `17.x` or `21.x` |
| 5 | **Android platform-tools (adb)** | Deploy and pull logs from the Control Hub | $0 | bundled with Android Studio; add to `PATH` | `adb devices` |
| 6 | **Python 3.11+** | The scouting scripts (standard library only) | $0 | [python.org](https://www.python.org/downloads/) — tick *Add to PATH* | `python --version` |
| 7 | *(optional)* VS Code + Claude Code extension, or the Claude desktop app | GUI instead of terminal | $0 | [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) | — |

**[FACT] Alternative Claude Code installers:** `winget install Anthropic.ClaudeCode` (does **not**
auto-update; run `winget upgrade Anthropic.ClaudeCode`), or `npm install -g @anthropic-ai/claude-code`
(needs **Node.js 22+** as of v2.1.198). The native PowerShell installer **auto-updates in the
background** and is the recommended path.
([setup](https://code.claude.com/docs/en/setup))

**[FACT] System requirements:** Windows 10 1809+ / macOS 13+ / Ubuntu 20.04+, 4 GB+ RAM, x64 or
ARM64, internet connection. Shell: Bash, Zsh, PowerShell or CMD.

**[FACT] Git for Windows is what enables the Bash tool.** Without it, Claude Code uses the PowerShell
tool instead. If it cannot find Git Bash, set it explicitly in `settings.json`:

```json
{ "env": { "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe" } }
```

⚠️ **[FACT] Sandboxing is not supported on native Windows** — only under WSL 2. **[JUDGMENT]** For a
robot repo this is acceptable *because* you are relying on deny-rules and hooks (see
`playbook/AI-FOR-PROGRAMMING.md` §3.5–3.6) rather than on process isolation. Do not compensate by
turning on a permissive default mode.

### 2.2 Verify the whole toolchain in one go

A ready-to-run checker ships with this toolkit: **`tools/ai/verify-setup.ps1`**. It is read-only —
it installs nothing and changes nothing.

```powershell
# tools only
powershell -ExecutionPolicy Bypass -File "tools\ai\verify-setup.ps1"

# tools + robot-repo wiring
powershell -ExecutionPolicy Bypass -File "tools\ai\verify-setup.ps1" -RepoPath C:\dev\robot-repo

# ...and actually build it (the only real proof)
powershell -ExecutionPolicy Bypass -File "tools\ai\verify-setup.ps1" -RepoPath C:\dev\robot-repo -Compile
```

It checks: `git`, `claude`, `java` (**and specifically that the major version is 17**), `python`,
`adb`; runs `claude doctor`; then confirms the repo has `gradlew.bat`, `TeamCode/`, `CLAUDE.md`,
`.claude/settings.json`, the hooks, the skills and the subagent — and warns if `CLAUDE.md` is over
220 lines or still contains unfilled `<placeholder>` tokens. Exit code `0` = ready, `1` = something
required is missing. `-Help` prints usage.

A green compile at the end means the machine is ready. **[JUDGMENT] Do not let a student's first
Claude Code session be on a machine that has never compiled the robot code** — you will spend the
session debugging Gradle and conclude that AI is useless.

### 2.3 First login

```powershell
cd "C:\path\to\robot-repo"
claude
```

Follow the browser prompt. Then, inside the session, type `/context` — it lists what is loaded,
including **Memory files**. If your `CLAUDE.md` is not listed there, it is not being read, and
nothing in §4 is working.

### 2.4 The toolchain conflict — read this before you install Android Studio

**This is the single most likely thing to cost you an evening**, because three official sources
say three different things and the newest one is the least prominent.

| Source | What it says | Fetched |
|---|---|---|
| **FtcRobotController v11.2 release notes** | *"This release requires **Android Studio Narwhal 3 Feature Drop or later** to build the workspace."* | 22 Aug 2026 |
| FtcRobotController **v11.2.1 README** | *"Android Studio **Ladybug (2024.2) or later**"*; Gradle **9.1**; AGP **8.13.2**; minSdk **24** | 22 Aug 2026 |
| **ftc-docs** install page | *"With the introduction of Android Studio Ladybug, the JDK that is packaged with Android Studio is incompatible with the FtcRobotController workspace"* → *"you will need to install **JDK 17** separately"* | 22 Aug 2026 |
| **Android developer docs** | AGP 8.13.0 shipped alongside Android Studio **Narwhal 3 Feature Drop (2025.1.3)**; the AGP 8.13/9.x line has a **minimum JDK of 17** | 22 Aug 2026 |

**[JUDGMENT] The resolution, and what to actually do:**

1. **Install Android Studio Narwhal 3 Feature Drop (2025.1.3) or later.** The README's "Ladybug or
   later" line is a stale boilerplate header; the release notes are the change record for the
   version you are actually cloning. When two official pages disagree, believe the more specific
   and more recent one.
2. **Do not install JDK 17 separately unless you have a reason to.** Narwhal 3 FD bundles JDK 21,
   AGP 8.13.2 accepts 17 *or* 21, and the ftc-docs warning is a Ladybug-specific artefact. If you
   already have JDK 17 installed and it builds, leave it alone — both work.
3. **Anything below JDK 17 is a hard failure**, not a warning. AGP 8.13.2 will not run on it.
4. **Never "fix" a Gradle error by editing `gradle/**`, `build.gradle` or `build.dependencies.gradle`.**
   Those paths are deny-listed in `tools/ai/CLAUDE.md.template` precisely because an agent asked to
   fix a version error will otherwise happily downgrade your SDK. Upgrade Studio instead.
5. **Pin what you actually run** in `CLAUDE.md`. The template's *Pinned versions* block now carries
   Narwhal 3 FD / Gradle 9.1 / AGP 8.13.2 / JDK 17-or-21 / minSdk 24 with this conflict noted inline,
   so the agent does not "helpfully" cite the ftc-docs page at you.

**[FACT] SDK release history, as of 22 Aug 2026** (`api.github.com/repos/FIRST-Tech-Challenge/FtcRobotController/releases`):
`v11.2.1` 2026-07-31 · `v11.2` 2026-07-15 · `v11.1` 2026-01-20 · `v11.0` 2025-09-06 · `v10.3` 2025-06-25.
**[JUDGMENT]** The v11.0 date — 6 Sep 2025, six days before that season's kickoff — is the pattern to
expect: a BIOBUZZ-season SDK will very likely land in the **first week of September 2026**, before
kickoff on the 12th. Do not start the season on 11.2.1 without checking. §13 item 3.

### 2.5 What was actually run and verified on a real machine, 22 August 2026

**[FACT]** Everything in this table was executed on the author's Windows 11 machine on 22 Aug 2026,
not merely read about. If your results differ, your setup differs.

| Command | Result |
|---|---|
| `verify-setup.ps1` (no args) | `PASS -- 1 warning(s). Machine is ready.` git 2.55.0, claude 2.1.228, **java 21.0.11**, python 3.14.6, gh 2.97.0; `adb` not on PATH (the warning) |
| `claude doctor` (via the script) | `No installation issues found.` |
| `fetch_events.py check` | FTCScout OK (`team 16321 = 'X Drive'`); FTC-Events index OK, `apiVersion=2.0 status=normal currentSeason=2026 maxSeason=2026`; **no credentials on this machine** → prints the full registration walkthrough, exit 2 |
| `fetch_events.py events --source scout --season 2025 --region USTXHO --limit 8` | 8 rows × 24 cols. Real data, e.g. `USTXHOCMP · Texas - Houston Championship · 2026-02-21 · San Jacinto College, Pasadena TX` |
| `fetch_events.py events --source scout --season 2025 --region USNYLI --limit 4` | 4 rows. Second region confirmed: `USNYLIBAQ`, `USNYLIBAS`, `USNYLICMP`, `USNYLIFPQ1` |
| `fetch_events.py events --source scout --season 2025 --team 16321` | 3 rows — every event that team attended, with per-event stats |
| `fetch_events.py matches --source scout --season 2025 -e USTXHOCMP` | **56 rows × 88 cols**, full DECODE score breakdown |
| `fetch_events.py teams` / `rankings`, same event | 36 rows × 183 cols each |
| `fetch_events.py awards --source scout --season 2024 -e FTCCMP1` | 18 rows × 9 cols, incl. Dean's List winners |
| `fetch_events.py dossier --season 2025 -e USTXHOCMP` | **36 rows × 31 cols** — OPR bands + ranks + event W-L-T + blank human-observation columns. ~3 minutes |
| `python -m py_compile fetch_events.py` | clean |
| R/I-rule coverage audit of the inspection checklist | All **52** R-rules and all **7** I-rules in the V0 PDF are covered (audit script and the ID list are in the checklist's header comment) |

⚠️ **[FACT] A real bug was found and fixed during that pass.** `events --source scout` had been
returning a bare **HTTP 400**: the GraphQL query asked FTCScout for `venue city state country` as
top-level `Event` fields, but they live under `location { … }`. Fixed, plus a `--region` flag added.
**[JUDGMENT] The lesson generalises:** a script that has only ever been syntax-checked is not a
working script. Run every path of every tool in this toolkit against live data once, before you
depend on it in a pit.

---

## 3. How the workspaces are organised

### 3.1 Two repos, one shared shape

**[JUDGMENT]** A small team should run **two** git repositories plus this analysis workspace:

```
robot-repo/            ← Java. The robot. Fast, tight context. Students live here.
team-ops/              ← Markdown + CSV. Decisions, meetings, events, portfolio, scouting output.
BIOBUZZ Analysis/      ← This workspace. Rules analysis, research, reference, templates, tools.
```

| Repo | Contains | Who edits | Session length | Why separate |
|---|---|---|---|---|
| **robot-repo** | `TeamCode/`, `CLAUDE.md`, `.claude/`, `docs/`, `logs/` | Programmers | Short, many | An agent here should read Java and nothing else. Every markdown file you add here is context tax on every code session |
| **team-ops** | `decisions/`, `meetings/`, `events/`, `portfolio/`, `scouting/`, `outreach/` | Everyone | Long, few | Portfolio work wants long context and no code. Also: the whole team can commit here without touching robot code |
| **BIOBUZZ Analysis** | `manuals/`, `reference/`, `research/`, `playbook/`, `tools/` | Mentor + analysts | Occasional | Read-mostly. The manual and the rule analysis are *reference data*, not team output |

**[JUDGMENT] Why not one repo?** Because context is the scarce resource in an agent session, and
because the portfolio and the robot code have different review standards. A single repo means every
"fix the lift PID" session also loads your outreach essays. If you insist on one repo — some teams
genuinely prefer it — put team-ops content under `docs/` and add a line to `CLAUDE.md` telling the
agent not to read it unless asked.

### 3.2 Where each template in this toolkit lands

| Template (`tools/ai/`) | Copy to | Renamed |
|---|---|---|
| `CLAUDE.md.template` | robot-repo root | `CLAUDE.md` |
| `decision-log.template.md` | `team-ops/decisions/` | `YYYY-MM-DD-<slug>.md` per decision |
| `meeting-notes.template.md` | `team-ops/meetings/` | `YYYY-MM-DD.md` per meeting |
| `inspection-checklist.template.md` | `team-ops/events/` | `inspection-<event>.md` per event |
| `match-day-runbook.template.md` | `team-ops/events/<date>-<code>/` | `runbook.md` per event |
| `PROMPTS-*.md` | stay here; **read, don't copy** | — |
| `scouting/fetch_events.py` | stays here; write output into `team-ops/scouting/` | — |

---

## 4. Wire up the robot repo — 30 minutes

Everything in this section is a *checklist*; the **reasoning and full file contents** are in
`playbook/AI-FOR-PROGRAMMING.md` §3.2–§3.10. Do not skip reading it — it explains why each deny-rule
exists.

### 4.1 The order

| # | Step | Time | Detail lives in |
|---|---|---|---|
| 1 | Fork/clone `FIRST-Tech-Challenge/FtcRobotController`; confirm it compiles | 15 min | FIRST's README |
| 2 | Create the target directory layout (`config/`, `subsystems/`, `opmodes/`, `tuning/`, `util/`, `src/test/java/`) | 10 min | `AI-FOR-PROGRAMMING.md` §3.2 |
| 3 | Copy `tools/ai/CLAUDE.md.template` → `CLAUDE.md`, **fill every `<…>`** | **20 min** | `tools/ai/CLAUDE.md.template` |
| 4 | Create `.claude/settings.json` (deny SDK edits, allow compile/test, ask before deploy) | 10 min | `AI-FOR-PROGRAMMING.md` §3.5 |
| 5 | Add `.claude/hooks/protect-sdk.sh` and `.githooks/pre-commit` | 10 min | `AI-FOR-PROGRAMMING.md` §3.6 |
| 6 | Add the four skills (`footgun-review`, `new-subsystem`, `explain`, `control-award`) | 15 min | `AI-FOR-PROGRAMMING.md` §3.7 |
| 7 | Add `.claude/agents/log-triage.md` | 5 min | `AI-FOR-PROGRAMMING.md` §3.8 |
| 8 | Install **one** library plugin (§4.4) | 5 min | below |
| 9 | Update `.gitignore` (§4.5) | 2 min | below |
| 10 | Verify (§4.6) | 5 min | below |

### 4.2 Filling in `CLAUDE.md` — the part people get wrong

The template's hardware table is the highest-value block in it. **[JUDGMENT] Fill it in with the
Robot Controller configuration file open in front of you and read the strings character by
character.** Case matters. `"Lift"` and `"lift"` are different devices, and the failure is a
`NullPointerException` at init during your first match, not a compile error.

Three rules while filling it in:

1. **Delete every row you do not have.** An inaccurate `CLAUDE.md` is worse than a short one.
2. **Keep the finished file under ~200 lines.** **[FACT]** The Claude Code docs warn that memory
   files over 200 lines *"consume more context and reduce adherence."*
   ([memory](https://code.claude.com/docs/en/memory))
3. **Fill in pinned versions honestly.** **[FACT]** The current SDK as of 21 Aug 2026 is **v11.2.1
   (released 2026-07-31)**; a v12.0 for BIOBUZZ has **not** shipped (expected ~5–8 Sep 2026 per
   `research/PROGRAMMING-PRACTICE.md` §2.3). Writing a version you do not run is how you get API
   hallucination.

### 4.3 Marking the file stale

Add this to your build-season habits: **after any mechanism rebuild, rewiring, or port change, the
hardware table in `CLAUDE.md` is stale until a human updates it.** The template already instructs
the agent to say so rather than trust it — but the human still has to do the edit. Put it on the
meeting agenda (`tools/ai/meeting-notes.template.md`, section C).

### 4.4 Plugins — install almost none

**[FACT]** `ncssm-robotics/ftc-claude` is a Claude Code plugin marketplace of FTC skills:
`pedro-pathing`, `roadrunner`, `ftclib`, `nextftc`, `pinpoint`, `limelight`, `panels`,
`ftc-dashboard`, `robot-dev`, and `decode` (the 2025-26 game). MIT licensed, ~4 stars, 84 commits
(GitHub, fetched 22 Aug 2026).

```
/plugin marketplace add ncssm-robotics/ftc-claude
/plugin install pedro-pathing@ncssm-robotics/ftc-claude    ← or roadrunner / ftclib, whichever you use
/plugin install robot-dev@ncssm-robotics/ftc-claude
/reload-plugins
```

**[JUDGMENT] Install the one that matches your path library, plus `robot-dev`. Nothing else.** Skip
`decode` — it is last season's game. There is no BIOBUZZ plugin as of 22 Aug 2026
(**[UNVERIFIED]** whether one will appear).

⚠️ **[FACT]** *"Plugins and marketplaces are highly trusted components that can execute arbitrary
code on your machine with your user privileges."* Read what you install.
([discover-plugins](https://code.claude.com/docs/en/discover-plugins))

**To make it a team decision instead of a per-laptop chore**, commit the marketplace into the repo's
`.claude/settings.json` — once a teammate trusts the folder, Claude Code registers it without another
prompt (**[FACT]**, same page):

```json
{
  "extraKnownMarketplaces": {
    "ftc-claude": { "source": { "source": "github", "repo": "ncssm-robotics/ftc-claude" } }
  }
}
```

Each teammate still runs `/plugin install <name>@ftc-claude` once — an external-source plugin enabled
only by project settings does not auto-install.

### 4.5 `.gitignore` additions

```gitignore
# Claude Code
.claude/settings.local.json
# Robot logs pulled off the hub -- large, and full of session noise
logs/
# Local build junk
.gradle/
build/
*.apk
```

**[JUDGMENT] Commit `.claude/settings.json`, `.claude/skills/`, `.claude/agents/` and `CLAUDE.md`.**
They are team infrastructure and they belong in review. Only `settings.local.json` is personal.

### 4.6 Verify

| Check | How | Expected |
|---|---|---|
| Memory loaded | `/context` in a session | `CLAUDE.md` appears under **Memory files** |
| Deny rules bite | ask it to "add a print statement to a sample OpMode" | it refuses / is blocked, and says so |
| Hook works | `bash .claude/hooks/protect-sdk.sh` with a fake SDK path | non-zero exit |
| Skill loads | `/footgun-review` | runs and shows the current diff |
| Subagent visible | `/context` → Custom Agents | `log-triage` listed |
| Compile loop | ask it to run the compile task | it runs `:TeamCode:compileDebugJavaWithJavac` and reports |

---

## 5. Wire up the team-ops workspace — 20 minutes

### 5.1 The layout

```
team-ops/
├── CLAUDE.md                      # §5.2 -- paste the file below
├── decisions/                     # one file per decision, from decision-log.template.md
│   └── 2026-09-14-drivetrain-choice.md
├── meetings/                      # one file per meeting, from meeting-notes.template.md
│   └── 2026-09-16.md
├── events/
│   └── 2026-11-14-USTXHOQ1/
│       ├── runbook.md             # from match-day-runbook.template.md
│       ├── inspection.md          # from inspection-checklist.template.md
│       ├── dossier.csv            # from fetch_events.py
│       ├── matches.csv
│       └── debrief.md
├── scouting/
│   ├── forms/                     # blank printable scout forms
│   └── data/                      # raw CSV pulls, never edited by hand
├── portfolio/
│   ├── 2026-27/                   # page drafts, one file per page
│   ├── photos/                    # captions use First L. only
│   └── ENDNOTE.md                 # the A201 AI credit line -- §7.2
├── outreach/
│   └── 2026-10-03-library-demo.md # date-slug per event, with the verified attendance number
└── admin/
    ├── budget.csv
    └── AI-USE-POLICY.md           # adopted from research/AI-IN-FTC-POLICY.md §10
```

### 5.2 `team-ops/CLAUDE.md` — paste this, then edit the bracketed parts

```markdown
# Team <NNNNN> — season operations workspace

## What this is
Markdown and CSV only. No robot code lives here (that is in <robot-repo-url>).
This workspace holds our engineering decisions, meeting notes, event records,
scouting data, outreach records and the engineering portfolio.

## Ground truth, in order
1. `../BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/` — the Competition Manual PDF. It wins over
   everything, including you and including anything you remember about FTC.
2. `../BIOBUZZ Analysis/reference/` and `research/` — our rule analysis. Cite the file.
3. This repo's `decisions/` and `meetings/` — what we actually did.
Anything not in those three is a guess and must be labelled one.

## Sections 8-11, 13 and 15 of the manual are PLACEHOLDERS until Kickoff, 12 September 2026
Game, ARENA, scoring and game rules are NOT public yet. If a task needs them, say so and stop.
Never answer a scoring question from prior-season memory — DECODE and INTO THE DEEP rule numbers
are wrong for BIOBUZZ.

## Labels — use them in every document you write here
- **[FACT]** followed by a citation: a local file path or a URL. No citation, no FACT label.
- **[JUDGMENT]** for a recommendation or an inference.
- **[UNVERIFIED]** for anything you could not confirm. Prefer this over guessing.
Never present a number, date, attendance figure, price or award result without one of these.

## Rules you must not break
- **No full names.** First name and last initial only, everywhere, including photo captions and
  file names (Competition Manual A201). If a source document has a full name, abbreviate it.
- **Do not invent** outreach attendance numbers, sponsor names, dates, test results, part prices,
  or award results. If a number is needed and we have not measured it, write
  `<TODO: measure/ask>` and tell us who should get it.
- **Do not overwrite a file you did not create in this session** without saying so first.
- **Do not delete a decision entry.** Supersede it with a new dated entry and link back.

## Conventions
- File names: `YYYY-MM-DD-short-slug.md`. Dates are ISO, always.
- Tables beat paragraphs. Numbers beat adjectives.
- Data lives in CSV under `scouting/data/`, never in a spreadsheet binary.
- Every claim that will appear in the portfolio must be traceable to a file in `decisions/`,
  `meetings/`, `events/` or `outreach/`.

## How to help us
Draft, restructure, check arithmetic, find contradictions, and ask what evidence backs a claim.
We do the judging, the deciding and the interviews. If we cannot explain it to a judge without
you, we will not use it — so explain your reasoning, briefly, every time.
```

**[JUDGMENT]** Keep this file under 60 lines forever. It is read at the start of every session in
this repo; every line you add is paid for on every turn.

---

## 6. File conventions that make agents effective

These are the conventions that separate a workspace an agent can work in from one it flails in.
**[JUDGMENT] throughout, but each one is here because its absence has a specific, predictable cost.**

| # | Convention | Do this | Not this | What it costs you if you skip it |
|---|---|---|---|---|
| 1 | **ISO dates in filenames** | `2026-11-14-qualifier-debrief.md` | `Nov qualifier notes (2).md` | The agent cannot order your season, so "what changed since the last event" fails |
| 2 | **One decision per file** | `decisions/2026-10-14-intake-roller-vs-claw.md` | one long `decisions.md` | Diffs become unreadable; the agent rewrites unrelated decisions |
| 3 | **Label every claim** | `[FACT] R503 caps motors at 8 (manual p.79)` | "we can only use 8 motors" | Unlabelled guesses get promoted into the portfolio and then into a judge interview |
| 4 | **Cite a path or a URL** | ``see `reference/CONSTRUCTION-RULES-R.md` §12.7`` | "per the rules" | You cannot re-check it in February, so you re-derive it |
| 5 | **Tables over prose** | a 6-column comparison table | three paragraphs of comparison | Agents parse tables reliably and summarise prose lossily |
| 6 | **Numbers, with units, in the name** | `liftHeightIn`, `armAngleDeg`, `cyclesPer90s` | `height`, `angle`, `rate` | Unit-boundary bugs — the most expensive class of AI code error |
| 7 | **CSV, not spreadsheets** | `scouting/data/2026-11-14-matches.csv` | `scouting.xlsx` | An agent cannot diff, grep or safely edit a binary; merge conflicts become unresolvable |
| 8 | **Never delete — supersede** | new dated entry, "supersedes DEC-007" | edit DEC-007 in place | The Think Award criterion is *"comparing choices"*; deleted options are deleted evidence |
| 9 | **Small files, stable names** | 200–400 line documents, renamed never | one 4,000-line master doc | Every session re-reads the whole thing; links rot |
| 10 | **ASCII, mostly** | `->`, `<=`, plain quotes | smart quotes, em-dashes copied from Word, emoji in filenames | Windows/PowerShell encoding breakage in scripts and grep misses |
| 11 | **Raw data is append-only** | scripts write `data/`, humans write `analysis/` | hand-editing a pulled CSV | You lose the ability to re-run and reproduce; a judge asks "how do you know" and you cannot answer |
| 12 | **First L. everywhere** | `Maya R.` | `Maya Rodriguez` | A201 PII violation propagates into the portfolio |
| 13 | **`TODO:` with an owner and a verb** | `<TODO Devon L.: measure spool dia. with calipers>` | `TODO: fix` | Unowned TODOs survive to February |
| 14 | **Placeholders are loud** | `= 0.0; // TODO MEASURE: kG, hang test` | `= 0.0012; // approx` | A plausible fabricated number is more dangerous than an obvious zero |

### 6.1 The one convention worth arguing about

**[JUDGMENT] Write the decision *before* you build, not after.** A decision log written afterwards
is a justification, and judges can tell. `tools/ai/decision-log.template.md` is structured to make
this cheap: problem, options, evidence, decision, owner — five minutes, at the moment of the
decision, before anyone picks up a drill. The "what actually happened" field gets filled in later,
honestly, including when you were wrong. An entry that says *"we were wrong, here is what we
learned"* is worth more to a judge than three that say "we chose correctly."

---

## 7. Staying inside the policy — controls, not intentions

`research/AI-IN-FTC-POLICY.md` establishes what the rules permit. This section is the
**operational** half: for each rule, the mechanism in this toolkit that enforces it.

### 7.1 Rule → mechanism

| Policy line (from `AI-IN-FTC-POLICY.md` §8) | The mechanism that makes it true |
|---|---|
| ❌ No off-board/cloud inference to or from the robot during a match (E301, R704.A) | `CLAUDE.md` §"Competition mode" forbids any code path needing a laptop; `.claude/settings.json` has no network-to-robot allowance; §9 below plans event day as offline |
| ❌ Never present work no student can explain | The explain-it-back gate, §7.3. Enforced at the point of deploy and at the point of committing a portfolio page |
| ❌ Never recite AI-drafted answers in a judge interview | `PROMPTS-portfolio.md` PF7 generates **questions to drill against**, never answers to recite. Cue card in the match-day runbook §10 is 5 bullets the student wrote |
| ❌ Never let AI invent an outreach number, sponsor, date or test result | Convention #14 + the team-ops `CLAUDE.md` "do not invent" block + `[UNVERIFIED]` label |
| ❌ Never paste student PII | Convention #12 + §1.4 + `CLAUDE.md` PII rule in both repos |
| ❌ Never tell a judge we didn't use AI | §7.2 disclosure artifacts — the answer already exists, in writing, before the question |
| ❌ Never accuse another team of AI-generating their work | Written into the adopted team policy (`admin/AI-USE-POLICY.md`), read aloud at the first meeting |
| ✅ Disclose in the portfolio | `portfolio/ENDNOTE.md` is a required file; the portfolio checklist fails without it |
| ✅ Disclose in the repo | The README line + the commit trailer, §7.4 |

### 7.2 The three disclosure artifacts — create them on day one, not in February

**[FACT — A201, verbatim]** *"Teams may use AI and research aids to compose their portfolios,
provided they respect intellectual property rights and include a footnote or endnote credit."*

**1. `portfolio/ENDNOTE.md`** — one line, pasted onto the last content page of the portfolio:

> *Portfolio composed by Team #### with drafting and editing assistance from Anthropic Claude. All
> engineering content, data, testing results and conclusions are the team's own work.*

**2. `robot-repo/README.md`** — a paragraph near the top:

> *Portions of this code were developed with assistance from Anthropic Claude and were reviewed,
> tested and tuned by Team ####. Every file in `TeamCode/` has been read and is understood by a
> student on this team.*

**3. The spoken answer** — memorised by every student, because the FIRST Control question bank
literally asks what outside resources you used:

> *"We use Claude Code the same way we use GM0, Pedro Pathing and goBILDA's CAD — as a tool. It
> drafts and checks; we decide, test and tune. Ask me about any line in our codebase."*

**[JUDGMENT]** Deliver it confidently and matter-of-factly, never apologetically. Then immediately
demonstrate understanding of whatever it was used for. `AI-IN-FTC-POLICY.md` §9 documents that the
community objection is *always* about comprehension and *never* about permission — so the defence is
a student who answers the follow-up, not a policy argument.

### 7.3 The explain-it-back gate — how to actually run it

**[JUDGMENT]** One rule, applied identically to AI assistance and mentor assistance (which is what
Competition Manual §1.4.3 already asks of mentors):

> **No AI-assisted output ships until one student can explain it, out loud, with the tool closed.**

| Where | Who asks | What they ask | Consequence of failing |
|---|---|---|---|
| **Before a deploy** | The other programmer, or a mentor | "What does this change make the robot do, and what breaks if it's wrong?" | The change waits. It does not go on the robot |
| **Before a portfolio page is committed** | The portfolio owner | "Which file in `decisions/` is this sentence sourced from?" | The sentence is cut or sourced |
| **Weekly, 10 minutes** | Rotating | One student explains one recent AI-assisted change to the group | Nothing punitive — this is the teaching mechanism |
| **Dress rehearsal (G7)** | Mentor plays judge | "Walk me through your autonomous." | You find out in November, not at the event |

**[JUDGMENT] The gate is also the pedagogy.** `playbook/AI-FOR-PROGRAMMING.md` §6.2 defines three
modes — *explain* mode, *pair* mode and *generate* mode — and which is allowed for which task. The
gate is what stops a team from silently sliding into generate mode for everything.

### 7.4 A provenance convention that costs nothing

**[JUDGMENT]** Add a trailer to commits with substantial AI assistance:

```
lift: add soft limit + current guard

Assisted-by: Claude Code
Reviewed-by: Devon L.
Tested-on-robot: 2026-10-21, bench then field, 12 cycles
```

Now `git log --grep="Assisted-by"` answers "how much of this did AI write?" with a number instead of
a shrug — which is a better answer than most teams can give, and it is Control Award evidence about
your process. **[JUDGMENT]** `Reviewed-by` is the load-bearing line, not `Assisted-by`.

### 7.5 The two things that would actually get you in trouble

**[FACT]** Nothing in FIRST's published policy makes AI use a disqualifying offence, and the Judging
Guide says failure to credit *"should never"* cause disqualification. The real exposure is narrower:

1. **Telling a judge you did not use AI when you did.** That is the Competition Integrity Contract
   §1.5.1 — *We Always Behave with Integrity* — and it is the only genuine DQ path here.
2. **Presenting work no student can defend.** Not a rules violation; simply losing. Control
   criteria 4/5, Design 4 and Think 1 all test defensibility directly.

---

## 8. The 30-minute student onboarding

Run this **once per student**, at a laptop that has already passed §2.2, with the robot repo cloned
and compiling. One mentor, one student, 30 minutes, phone away.

### 8.1 Minute by minute

| Time | Mentor does | Student does | Point being made |
|---|---|---|---|
| **0–3** | Open `admin/AI-USE-POLICY.md`. Read the "explain it without the tool" sentence out loud | Listens, asks one question | The rule comes first, before the tool |
| **3–5** | — | Runs `claude` in the robot repo, then `/context` | Sees `CLAUDE.md` under **Memory files**. "That file is why it knows our motor names" |
| **5–10** | — | Asks: *"Read `subsystems/Lift.java` and explain what it does, line by line, to someone who has never seen FTC code"* | **Explain mode first.** The first thing they ever do with it is *learn*, not generate |
| **10–13** | Asks them to summarise it back | Explains the lift, without reading the answer aloud | The gate, demonstrated on minute 13 |
| **13–18** | — | Runs the footgun review: `/footgun-review` on a deliberately broken branch you prepared | Sees it catch a real bug. Trust is built on a catch, not a claim |
| **18–23** | — | Asks: *"Add a soft limit to the lift so it cannot drive past `<N>` ticks. Do not change any tuned number. Show me the diff and tell me what breaks if you're wrong"* | **Pair mode.** Note the three constraints in the prompt — that is the house style |
| **23–26** | Points at the refusal, or at the placeholder | Reads the diff, runs the compile, does **not** deploy | Compile is not test. Deploy needs a human at the STOP button |
| **26–30** | Runs the graduation test, §8.4 | Answers | Cleared, or not |

### 8.2 Prepare these before the session (mentor, 10 minutes, once)

- A branch with a deliberate FTC footgun in it: a `while` loop without `opModeIsActive()`, or a
  servo `setPosition(0.95)` outside the safe range in `CLAUDE.md`.
- The lift soft-limit task actually being undone in the code.
- `tools/ai/PROMPTS-programming.md` open in a second window.

### 8.3 The four sentences to say out loud

1. *"It will be confidently wrong about numbers. Every gain, servo position, ratio and field
   coordinate it produces is a guess until you measure it."*
2. *"Compiling is not testing. Testing is the robot on blocks with your hand on stop."*
3. *"If you can't explain it to me with the screen closed, it doesn't go on the robot — and it
   doesn't go in the portfolio."*
4. *"Ask it to explain things to you at least as often as you ask it to write things for you."*

### 8.4 The graduation test — three questions, all must pass

| # | Question | A passing answer |
|---|---|---|
| 1 | "Where does it get our motor names from, and what happens if that file is wrong?" | `CLAUDE.md`'s hardware table; wrong names compile fine and NullPointerException at init |
| 2 | "It just gave you a PID gain of 0.0035. What do you do?" | Do not use it. It is a guess. Measure it with the tuning OpMode and log the result in `docs/TUNING-LOG.md` |
| 3 | "A judge asks whether you used AI. What do you say?" | The §7.2 answer, then offer to explain any line of the code |

**Fail any one → not cleared to deploy.** They can still use explain mode all they like; that is the
point. Re-test next meeting. **[JUDGMENT]** This takes 90 seconds and prevents the single failure
mode the whole community worries about.

### 8.5 What *not* to teach in the first 30 minutes

Skills authoring · subagents · MCP servers · hooks · settings.json · plugin marketplaces · anything
about the portfolio. **[JUDGMENT]** They are all in this toolkit and they all matter, but a first
session that covers configuration instead of use produces a student who can configure and cannot
work. Teach the second half in week three, to the one or two students who ask for it.

---

## 9. The event-day blackout — design for no network

**[FACT — E301, verbatim]** *"Teams may not set up their own Wi-Fi (802.11a/b/g/n/ac/ax/be) wireless
communication (e.g., access points or ad-hoc networks), Bluetooth, or any other communications
systems using 2.4GHz or 5GHz wireless in the venue,"* and the manual's note: *"A wireless hot spot
created by a cellular device, camera, smart TV, etc. is considered an access point."*

**[FACT — E109]** *"Do not arrange for power, internet access, or phone lines from venue service
providers or attempt to use venue internet connections reserved for event purposes."*

**[JUDGMENT] Consequence: assume you have no AI, and probably no internet, from load-in to teardown.**
This is the constraint that shapes the whole toolkit. Everything an agent was going to do for you
must be done and **printed** before you leave.

**[UNVERIFIED]** Whether **USB tethering** to a phone is permitted. It does not create a wireless
access point in the venue, so a plain-language reading of E301 does not reach it — but the phone's
own Wi-Fi radio may still be active, and we have not found a Q&A ruling. **Ask the FTA at your first
event, before you do it.** Do not reason your way into it from this document.

### 9.1 The pre-event export list

Run these the night before, at home, on a real network:

| ✔ | Artefact | Command / prompt | Goes where |
|---|---|---|---|
| ☐ | Pre-event dossier for every registered team | `python tools/ai/scouting/fetch_events.py dossier --season 2026 -e <CODE> -o dossier.csv` | printed + `events/<date>-<code>/` |
| ☐ | Watch list (top ~20% by season OPR, plus Inspire/Control winners) | `PROMPTS-scouting.md` SC2 | printed |
| ☐ | Blank pit-scout cards | `PROMPTS-scouting.md` SC3 | printed, one per team at the event |
| ☐ | Filled self-inspection checklist | `tools/ai/inspection-checklist.template.md` | printed |
| ☐ | Match-day runbook, crew table filled | `tools/ai/match-day-runbook.template.md` | printed, one per crew member |
| ☐ | Portfolio ×2 | — | printed |
| ☐ | Judge drill done, cue card written | `PROMPTS-portfolio.md` PF7 | pocket |
| ☐ | **Known-good build installed on the robot over USB** | `./gradlew installDebug` | the robot |
| ☐ | Repo cloned and **compiling offline** on the event laptop | `:TeamCode:compileDebugJavaWithJavac` | laptop |

**[JUDGMENT] Test the laptop with Wi-Fi switched off before you leave.** Gradle will happily reach
for the network on a cold cache and fail in the pit. Run one full offline compile at home.

### 9.2 What still works offline

Local `git`, Gradle with a warm cache, `adb`, every Python script in `tools/ai/scouting/` **against
CSVs you already pulled**, and your printed paper. That is the complete list. Claude Code is a
network client; it does not work offline.

---

## 10. Keeping it alive — the maintenance cadence

| Cadence | Task | Owner | Time |
|---|---|---|---|
| **Every meeting** | Anything corrected twice → propose a `CLAUDE.md` edit | Programmer | 2 min |
| **Every meeting** | Meeting notes filed from the template | Rotating scribe | 5 min |
| **Every decision** | Decision entry written **before** the build starts | Whoever owns it | 5 min |
| **Weekly (Thursday)** | Grep the new Team Update for `AI\|artificial\|ChatGPT` and for changed R/I/E rule numbers | Mentor | 10 min |
| **Weekly** | 10-minute explain-it-back round | Rotating | 10 min |
| **After a rebuild** | Update the `CLAUDE.md` hardware table and safe ranges | Programmer | 5 min |
| **Monthly** | Portfolio pass: point Claude at `meetings/` + `decisions/`, run `PROMPTS-portfolio.md` PF1, a student fact-checks every claim | Portfolio owner | 30 min |
| **Monthly** | Read `/memory`; promote any safety-relevant note into the committed `CLAUDE.md` | Programmer | 10 min |
| **Monthly** | `claude doctor`; confirm auto-update is working | Mentor | 2 min |
| **Per event** | Copy runbook + inspection templates; run the §9.1 export list; file the debrief within 48 h | Log keeper | 60 min |
| **At kickoff** | §13 | All | see §13 |

---

## 11. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `claude: command not found` | PATH not refreshed | New terminal; then `claude doctor` |
| `/plugin` not recognised | Old version | `claude update`, restart the terminal |
| It invents hardware names | `CLAUDE.md` not loaded, or its table is stale | `/context` → check **Memory files**; then re-read the table against the RC config |
| It edits the SDK module | Deny rule missing or folder not trusted | **[FACT]** deny/ask rules apply immediately, but `allow` rules and `additionalDirectories` only apply after each person trusts the folder. Re-check `.claude/settings.json`; add the hook (`AI-FOR-PROGRAMMING.md` §3.6) |
| Bash tool unavailable on Windows | Git for Windows missing | Install it, or set `CLAUDE_CODE_GIT_BASH_PATH` |
| Gradle "works for me, not for them" | Two machines on different Studio/JDK majors | Compare `java -version` **and** Studio version on both. Fix by moving both to Narwhal 3 FD or later; set the Gradle JDK explicitly at *Settings > Build Tools > Gradle > Gradle JDK* (§2.4) |
| `Minimum supported Gradle version is 9.1` / `AGP requires Android Studio…` | Studio older than Narwhal 3 Feature Drop, against SDK 11.2+ | Upgrade Studio. Do **not** downgrade the SDK's Gradle wrapper — `gradle/**` is a deny-listed path for a reason (§4.5, `CLAUDE.md.template`) |
| Skills don't appear | Plugin cache | `rm -rf ~/.claude/plugins/cache`, restart, reinstall (**[FACT]**, discover-plugins) |
| Sessions feel slow / it forgets things | Too much loaded | Trim `CLAUDE.md` toward 200 lines; uninstall unused plugins; move long reference into a skill (loads on demand) |
| `fetch_events.py` returns nothing | Season number or event code wrong, or no credentials | `python tools/ai/scouting/fetch_events.py check`, then `endpoints`; see `scouting/README.md` §3–§4 |
| It cites a DECODE rule number | Prior-season training data | Point it at `manuals/2026-27_BIOBUZZ/` explicitly; use `PROMPTS-strategy.md` S5, which forces a verbatim quote from the local file |

---

## 12. What the whole toolkit costs

**[FACT] for prices, as of August 2026. [JUDGMENT] for the verdicts.**

| Item | Cost | Notes |
|---|---|---|
| Claude Pro ×1 | **$17–20/mo** | The only recurring cost |
| Git, JDK 17/21, Android Studio, Python, adb | $0 | |
| `ncssm-robotics/ftc-claude` plugins | $0 | MIT |
| FTC-Events API | $0 | Free registration; non-commercial use, link back requested |
| FTCScout | $0 | No auth |
| GM0, ftc-docs, FIRST Q&A archives | $0 | |
| Printing (per event: portfolio ×2, dossier, forms, runbook) | ~$5–15 | |
| **Season total (9 months)** | **≈ $155–200** | Roughly one drivetrain motor set |

---

## 13. Kickoff day — 12 September 2026

The toolkit has a kickoff-day job list of its own. Everything below is blocked until the manual
drops, and all of it is stale-by-design right now.

| # | Action | File to update |
|---|---|---|
| 1 | Run `tools/ingest-manual.sh` on the Kickoff manual; re-extract sections | `manuals/2026-27_BIOBUZZ/` |
| 2 | Download the **2026-27 Inspection Checklist and Inspection Quick Reference** the moment they post; reconcile | `tools/ai/inspection-checklist.template.md` |
| 3 | Check whether a new **SDK** shipped (v11.0 landed **6 days before** the 2025-26 kickoff — expect the same). If so, read its release notes for a **toolchain bump** (§2.4), update pinned versions **as a deliberate human decision**, then re-verify Sloth and your path library against it | robot `CLAUDE.md`, `verify-setup.ps1` |
| 4 | Re-fetch the **FTC Judging Process Guide** and the **Judging Question Bank** (both listed as coming soon in V0); re-check the AI section against `research/AI-IN-FTC-POLICY.md` §2.2 | `research/AI-IN-FTC-POLICY.md` |
| 5 | Add the real **G-rules** and scoring categories to the runbook's match log and the strategy prompts | `tools/ai/match-day-runbook.template.md`, `PROMPTS-strategy.md` |
| 6 | Confirm **Section 10 DRIVE TEAM** composition; update the crew table | `tools/ai/match-day-runbook.template.md` §1 |
| 7 | Fill in **R105** sizing numbers (deferred in V0) | inspection checklist |
| 7b | **Re-run the R/I-rule ID audit** on the Kickoff manual: `grep -oE "R[0-9]{3}" manuals/2026-27_BIOBUZZ/v0_pymupdf.txt \| sort -u -V`. Any ID not in the 52 listed in the checklist header is a NEW rule with no checklist row | `tools/ai/inspection-checklist.template.md` |
| 8 | Design the season's scout form around the real scoring categories | `PROMPTS-scouting.md` SC3 |
| 9 | Re-run `fetch_events.py check` and confirm `currentSeason = 2026`; expect new score-breakdown columns | `tools/ai/scouting/` |
| 10 | Adopt the team AI policy at the first post-kickoff meeting and file it | `team-ops/admin/AI-USE-POLICY.md` |

**[JUDGMENT] Do items 1, 2 and 3 on kickoff morning, before anyone starts sketching a robot.** They
are the ones that invalidate other work if they land late.

---

## 13a. The shop-wall card — print this, tape it up

**[JUDGMENT]** One page. It is the whole toolkit compressed to what someone needs at 7pm on a
Tuesday when the mentor is across the room.

---

> ### TEAM #### · AI RULES OF THE ROOM
>
> **1. The gate.** Nothing ships until a student can explain it **with the screen closed**.
> Applies to code, portfolio pages, CAD and analysis. No exceptions, no "it's just a small change".
>
> **2. It lies about numbers.** Every PID gain, servo position, gear ratio, field coordinate, part
> price, attendance figure and award result it gives you is a **guess until you measure it or find
> the source**. Placeholders are `0.0 // TODO MEASURE`, never a plausible-looking decimal.
>
> **3. Compile ≠ test.** Test is: robot on blocks, hand on STOP, then the field. Deploy needs a
> second human present.
>
> **4. Names.** First name + last initial. Everywhere. Photos, captions, filenames, prompts.
>
> **5. Label everything you write.** `[FACT]` + a path or URL · `[JUDGMENT]` · `[UNVERIFIED]`.
> No citation → not a FACT.
>
> **6. Sections 8-11 of the manual are blank until 12 Sep 2026.** If it answers a scoring question
> before then, it is reciting DECODE. Stop and check the PDF.
>
> **7. Event day = no AI, no internet.** E301. Everything printed the night before.
>
> **8. If a judge asks:** *"We use Claude Code the way we use GM0 and goBILDA CAD — a tool. It
> drafts and checks; we decide, test and tune. Ask me about any line in our codebase."* Then answer
> the follow-up.
>
> **Never:** paste PII · invent a number · recite an AI answer in an interview · say we didn't use
> it · accuse another team of using it.
>
> **Files:** `CLAUDE.md` (robot repo) · `tools/ai/PROMPTS-*.md` (prompts) ·
> `team-ops/decisions/` (write it **before** you build) · `admin/AI-USE-POLICY.md`

---

## 13b. What changed in this revision — 22 August 2026, verification pass

**[FACT]** A second pass ran every tool in `tools/ai/` against live data and re-audited the
rule-derived templates against the manual text. Changes:

| File | Change | Why |
|---|---|---|
| `tools/ai/scouting/fetch_events.py` | **Bug fix.** FTCScout `events` GraphQL query asked for `venue/city/state/country` at the top level of `Event`; they are under `location {}`. Returned HTTP 400 for every user | Found by running it, not reading it |
| `tools/ai/scouting/fetch_events.py` | Added `--region` (FTCScout `RegionOption` enum, 97 values); replaced unverified example event codes with three that were run live | You cannot list a season's events usefully without a region filter |
| `tools/ai/scouting/fetch_events.py` | **Gap closed.** The `/teams/{n}/events/{season}` endpoint was declared in the constants but no subcommand reached it — so `PROMPTS-scouting.md` SC12 (season trend report) named a command that silently ignored `--team`. Now wired to `events --source scout --team <n>` | A prompt library that names a command the script does not implement is worse than no prompt |
| `tools/ai/scouting/README.md` | Documented both GraphQL gotchas with re-introspection commands; verification log extended with 10 live results | So the next person does not lose the same hour |
| `tools/ai/verify-setup.ps1` | JDK check now accepts **17 or 21**, hard-fails below 17, warns above 21. Previously warned on 21 — i.e. it warned on a *correct* modern setup | §2.4 |
| `tools/ai/CLAUDE.md.template` | Pinned-versions block now carries Narwhal 3 FD / Gradle 9.1 / AGP 8.13.2 / JDK 17-or-21, with the three-way source conflict noted inline | Stops the agent citing the stale ftc-docs page |
| `tools/ai/inspection-checklist.template.md` | Added the missing **R703** row (smartphone-RC USB connection); added a coverage-audit header proving all **52** R-rules and **7** I-rules in the V0 PDF are covered; flagged the extra rule IDs in `reference/CONSTRUCTION-RULES-R.md` that do not appear in the PDF | A checklist with a silent gap is worse than no checklist |
| This file | §2.4 (toolchain conflict), §2.5 (live verification log), §13a (shop-wall card), expanded routing table, new sources | — |

---

## 14. Sources

### Local files (this workspace)

`research/AI-IN-FTC-POLICY.md` §2, §8, §9, §10, §11 · `research/PROGRAMMING-PRACTICE.md` §2.3, §7.1,
§7.8 · `research/SCOUTING-AND-AWARDS.md` §5.3, §13.1, §16 · `research/SEASON-CADENCE.md` §8.2, §8.5,
§8.6 · `research/SMALL-TEAM-ECONOMICS.md` · `research/TESTING-AND-TUNING.md` §3.3 ·
`reference/CONSTRUCTION-RULES-R.md` · `playbook/AI-FOR-PROGRAMMING.md` §3.1–§3.10, §5, §6 ·
`tools/ai/*` (all templates and prompt libraries) ·
`manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` (Sections 3, 5, 6, 12 final;
8–11, 13 and 15 placeholders; §14 League Play is final text).

### Web (all fetched 22 August 2026)

| Claim | URL |
|---|---|
| Install methods, system requirements, Windows/WSL, sandboxing, `claude doctor`, plan requirement | <https://code.claude.com/docs/en/setup> |
| `CLAUDE.md` loading, 200-line guidance | <https://code.claude.com/docs/en/memory> |
| Permissions, deny/allow timing, path rules | <https://code.claude.com/docs/en/permissions> |
| Plugin install commands, `extraKnownMarketplaces`, scopes, trust warning, cache fix | <https://code.claude.com/docs/en/discover-plugins> |
| Plugin structure, skills, `/reload-plugins` | <https://code.claude.com/docs/en/plugins> |
| Plan prices | <https://claude.com/pricing> |
| 18+ requirement (effective 8 Oct 2025) | <https://www.anthropic.com/legal/consumer-terms> |
| US K-12 Terms of Service (effective 14 Jul 2026) | <https://www.anthropic.com/legal/k12-terms> |
| Ladybug bundled JDK incompatible; install JDK 17 separately | <https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/android_studio/installing_android_studio/Installing-Android-Studio.html> |
| FTC Claude skills marketplace (10 skills, MIT, ~4 stars) | <https://github.com/ncssm-robotics/ftc-claude> |
| FtcRobotController upstream | <https://github.com/FIRST-Tech-Challenge/FtcRobotController> |
| SDK release history and dates (v11.2.1 2026-07-31 … v10.3 2025-06-25) | <https://api.github.com/repos/FIRST-Tech-Challenge/FtcRobotController/releases> |
| **v11.2 release notes** — *"requires Android Studio Narwhal 3 Feature Drop or later"* | <https://api.github.com/repos/FIRST-Tech-Challenge/FtcRobotController/releases/tags/v11.2> |
| v11.2.1 README — Gradle 9.1, AGP 8.13.2, minSdk 24, "Ladybug (2024.2) or later" | <https://raw.githubusercontent.com/FIRST-Tech-Challenge/FtcRobotController/master/README.md> |
| AGP release/compatibility (AGP 8.13 ships with Narwhal 3 FD; min JDK 17) | <https://developer.android.com/build/releases/gradle-plugin> · <https://developer.android.com/build/releases/agp-8-13-0-release-notes> |
| FTC-Events OpenAPI spec (every path in `fetch_events.py`) | <https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json> |
| FTC-Events API registration | <https://ftc-events.firstinspires.org/services/API/register> |
| FTCScout REST + GraphQL (no auth); `Event.location`, `RegionOption` enum | <https://api.ftcscout.org/graphql> · <https://ftcscout.org/api> |

### Known gaps

| # | Gap | How to close it |
|---|---|---|
| 1 | Whether USB tethering is acceptable under E301 | Ask the FTA at your first event; consider a Q&A submission after 28 Sep 2026 |
| 2 | Whether an Anthropic Education/K-12 plan is available to a **club** rather than a district | Ask the school's IT or CTE lead; **[UNVERIFIED]** |
| 3 | Your district's own AI policy | Ask administration in writing, before students start |
| 4 | Whether the 2026-27 Judging Process Guide changes the AI language | Re-fetch at kickoff (§13 item 4) |
| 5 | Prices and plan structure | Re-check `claude.com/pricing` before budgeting |
| 6 | Whether a BIOBUZZ plugin appears in `ftc-claude` | Re-check after kickoff |
| 7 | Whether the FtcRobotController README's "Ladybug (2024.2) or later" line gets corrected to match the v11.2 release notes | Re-read the README at kickoff; until then follow the release notes (§2.4) |
| 8 | `reference/CONSTRUCTION-RULES-R.md` enumerates R-rule IDs (R205-R208, R306-R307, R614-R619, R712-R718, R905-R906) that do **not** appear in the V0 PDF text | Treat the PDF as ground truth. Re-audit both against the Kickoff manual (§13 item 7b) |

---

*Companion files: `playbook/AI-FOR-PROGRAMMING.md` (the software workstream in depth) ·
`research/AI-IN-FTC-POLICY.md` (what the rules permit) · `tools/ai/` (everything you actually run).*
