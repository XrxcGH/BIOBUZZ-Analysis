<#
    verify-setup.ps1 -- one-shot toolchain check for an AI-assisted FTC team.

    WHAT IT DOES
        Checks that every tool in playbook/AI-TOOLKIT-SETUP.md section 2 is installed and
        on PATH, then (optionally) checks that a robot repo is wired for Claude Code and
        actually compiles.  Read-only: it installs nothing and changes nothing.

    USAGE
        powershell -ExecutionPolicy Bypass -File tools\ai\verify-setup.ps1
        powershell -ExecutionPolicy Bypass -File tools\ai\verify-setup.ps1 -RepoPath C:\dev\robot-repo
        powershell -ExecutionPolicy Bypass -File tools\ai\verify-setup.ps1 -RepoPath C:\dev\robot-repo -Compile
        powershell -ExecutionPolicy Bypass -File tools\ai\verify-setup.ps1 -Help

    EXIT CODES
        0  everything required passed
        1  at least one required check failed

    Companion: playbook/AI-TOOLKIT-SETUP.md sections 2.1 / 2.2 / 4.6
#>

[CmdletBinding()]
param(
    # Path to the FtcRobotController robot repo. Optional -- omit to check tools only.
    [string]$RepoPath = "",

    # Also run the Gradle compile task. Slow (~1-3 min cold) but it is the real test.
    [switch]$Compile,

    [switch]$Help
)

if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path -Detailed
    Get-Content $MyInvocation.MyCommand.Path -TotalCount 22 | Where-Object { $_ -notmatch '^<#|^#>' }
    exit 0
}

$script:Fail = 0
$script:Warn = 0

function Test-Tool {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Command,
        [Parameter(Mandatory)][string[]]$ToolArgs,
        [string]$Why = "",
        [switch]$Optional
    )
    $exe = Get-Command $Command -ErrorAction SilentlyContinue
    if (-not $exe) {
        if ($Optional) {
            Write-Host ("  WARN  {0,-18} not found  {1}" -f $Name, $Why) -ForegroundColor Yellow
            $script:Warn++
        } else {
            Write-Host ("  FAIL  {0,-18} not found  {1}" -f $Name, $Why) -ForegroundColor Red
            $script:Fail++
        }
        return
    }
    try {
        $out = & $Command @ToolArgs 2>&1 | Out-String
    } catch {
        $out = $_.Exception.Message
    }
    $line = ($out -split "`r?`n" | Where-Object { $_.Trim() -ne "" } | Select-Object -First 1)
    Write-Host ("  OK    {0,-18} {1}" -f $Name, $line.Trim()) -ForegroundColor Green
}

function Test-RepoFile {
    param(
        [Parameter(Mandatory)][string]$Relative,
        [string]$Why = "",
        [switch]$Optional
    )
    $full = Join-Path $RepoPath $Relative
    if (Test-Path $full) {
        Write-Host ("  OK    {0,-34} present" -f $Relative) -ForegroundColor Green
    } elseif ($Optional) {
        Write-Host ("  WARN  {0,-34} missing  {1}" -f $Relative, $Why) -ForegroundColor Yellow
        $script:Warn++
    } else {
        Write-Host ("  FAIL  {0,-34} missing  {1}" -f $Relative, $Why) -ForegroundColor Red
        $script:Fail++
    }
}

Write-Host ""
Write-Host "=== 1. Toolchain (playbook/AI-TOOLKIT-SETUP.md section 2.1) ===" -ForegroundColor Cyan

Test-Tool -Name "git"           -Command "git"    -ToolArgs @("--version")  -Why "https://git-scm.com/downloads/win -- also enables the Bash tool"
Test-Tool -Name "claude"        -Command "claude" -ToolArgs @("--version")  -Why "irm https://claude.ai/install.ps1 | iex"
Test-Tool -Name "java"          -Command "java"   -ToolArgs @("-version")   -Why "JDK 17 or 21. SDK 11.2+ builds on AGP 8.13.2 / Gradle 9.1 (min JDK 17); Narwhal 3 FD bundles 21"
Test-Tool -Name "python"        -Command "python" -ToolArgs @("--version")  -Why "3.11+, needed by tools/ai/scouting/fetch_events.py"
Test-Tool -Name "adb"           -Command "adb"    -ToolArgs @("version")    -Why "Android platform-tools; add to PATH" -Optional
Test-Tool -Name "gh (optional)" -Command "gh"     -ToolArgs @("--version")  -Why "GitHub CLI, only if you use PRs" -Optional

# Java major version -- the single most common day-one failure.
#
# VERIFIED 2026-08-22:
#   * FtcRobotController v11.2 release notes: "This release requires Android Studio
#     Narwhal 3 Feature Drop or later to build the workspace."
#   * v11.2.1 README: Gradle 9.1, AGP 8.13.2, minSdk 24.
#   * AGP 8.13+/9.x minimum JDK is 17; Android Studio Narwhal 3 FD bundles JDK 21.
#   * The ftc-docs "install JDK 17 separately" page is Ladybug-era advice and is
#     still correct-but-narrow: 17 works, 21 works, <17 does not.
# So: accept 17 or 21, warn on anything else, and hard-flag anything below 17.
$javaExe = Get-Command java -ErrorAction SilentlyContinue
if ($javaExe) {
    $vtext = (& java -version 2>&1 | Out-String)
    if ($vtext -match '"(\d+)') {
        $major = [int]$Matches[1]
        if ($major -eq 17 -or $major -eq 21) {
            Write-Host ("  OK    java major version   {0}" -f $major) -ForegroundColor Green
        } elseif ($major -lt 17) {
            Write-Host ("  FAIL  java major version   {0} -- too old. AGP 8.13.2 needs JDK 17 minimum." -f $major) -ForegroundColor Red
            $script:Fail++
        } else {
            Write-Host ("  WARN  java major version   {0} -- untested with SDK 11.2.x. Point Gradle at a 17 or 21 JDK (Android Studio > Settings > Build Tools > Gradle > Gradle JDK)." -f $major) -ForegroundColor Yellow
            $script:Warn++
        }
    }
}

Write-Host ""
Write-Host "=== 2. Claude Code health ===" -ForegroundColor Cyan
if (Get-Command claude -ErrorAction SilentlyContinue) {
    Write-Host "  running 'claude doctor' (read-only diagnostics)..."
    & claude doctor
} else {
    Write-Host "  SKIP  claude not installed" -ForegroundColor Yellow
}

if ($RepoPath -ne "") {
    Write-Host ""
    Write-Host "=== 3. Robot repo wiring (AI-TOOLKIT-SETUP.md section 4.6) ===" -ForegroundColor Cyan
    if (-not (Test-Path $RepoPath)) {
        Write-Host ("  FAIL  RepoPath does not exist: {0}" -f $RepoPath) -ForegroundColor Red
        $script:Fail++
    } else {
        Write-Host ("  repo: {0}" -f (Resolve-Path $RepoPath))
        Test-RepoFile "gradlew.bat"                    -Why "is this actually an FtcRobotController fork?"
        Test-RepoFile "TeamCode"                       -Why "TeamCode module missing"
        Test-RepoFile "CLAUDE.md"                      -Why "copy tools/ai/CLAUDE.md.template and fill it in"
        Test-RepoFile ".claude\settings.json"          -Why "see playbook/AI-FOR-PROGRAMMING.md 3.5"
        Test-RepoFile ".claude\hooks\protect-sdk.sh"   -Why "see playbook/AI-FOR-PROGRAMMING.md 3.6" -Optional
        Test-RepoFile ".githooks\pre-commit"           -Why "see playbook/AI-FOR-PROGRAMMING.md 3.6" -Optional
        Test-RepoFile ".claude\skills\footgun-review"  -Why "see playbook/AI-FOR-PROGRAMMING.md 3.7" -Optional
        Test-RepoFile ".claude\agents\log-triage.md"   -Why "see playbook/AI-FOR-PROGRAMMING.md 3.8" -Optional

        # CLAUDE.md length guidance: docs warn that files over ~200 lines reduce adherence.
        $claudeMd = Join-Path $RepoPath "CLAUDE.md"
        if (Test-Path $claudeMd) {
            $n = (Get-Content $claudeMd | Measure-Object -Line).Lines
            if ($n -gt 220) {
                Write-Host ("  WARN  CLAUDE.md is {0} lines -- trim toward 200 (code.claude.com/docs/en/memory)" -f $n) -ForegroundColor Yellow
                $script:Warn++
            } else {
                Write-Host ("  OK    CLAUDE.md length          {0} lines" -f $n) -ForegroundColor Green
            }
            # Unfilled placeholders are the most common cause of an agent inventing hardware names.
            $placeholders = (Select-String -Path $claudeMd -Pattern '<[A-Za-z0-9 .|/_-]+>' -AllMatches |
                             ForEach-Object { $_.Matches } | Measure-Object).Count
            if ($placeholders -gt 0) {
                Write-Host ("  WARN  CLAUDE.md still has {0} unfilled <placeholder> tokens" -f $placeholders) -ForegroundColor Yellow
                $script:Warn++
            }
        }

        if ($Compile) {
            Write-Host ""
            Write-Host "=== 4. Compile (the real test) ===" -ForegroundColor Cyan
            Push-Location $RepoPath
            try {
                & .\gradlew.bat :TeamCode:compileDebugJavaWithJavac
                if ($LASTEXITCODE -ne 0) {
                    Write-Host "  FAIL  compile failed" -ForegroundColor Red
                    $script:Fail++
                } else {
                    Write-Host "  OK    TeamCode compiles" -ForegroundColor Green
                }
            } finally {
                Pop-Location
            }
        } else {
            Write-Host ""
            Write-Host "  (re-run with -Compile to actually build -- a green compile is the only real proof)"
        }
    }
} else {
    Write-Host ""
    Write-Host "  (pass -RepoPath <path-to-robot-repo> to also check repo wiring)"
}

Write-Host ""
if ($script:Fail -eq 0) {
    Write-Host ("PASS -- {0} warning(s). Machine is ready." -f $script:Warn) -ForegroundColor Green
    exit 0
} else {
    Write-Host ("FAIL -- {0} required check(s) failed, {1} warning(s)." -f $script:Fail, $script:Warn) -ForegroundColor Red
    Write-Host "Fix list: playbook/AI-TOOLKIT-SETUP.md section 2.1 (install table) and section 11 (troubleshooting)."
    exit 1
}
