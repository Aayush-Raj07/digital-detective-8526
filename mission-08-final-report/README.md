# Mission 8 — Final Report and Submission

## 1. Task / objective

Review the complete assignment repository, verify every required folder, file, program, and README, confirm Git commits and Pull Request status on GitHub, and prepare the repository URL for final submission.

## 2. Work completed

- Verified the full repository file structure against the assignment guide.
- Checked that all nine mission READMEs follow the required nine-section format and contain no private information.
- Executed `hello.py` and `number_converter.py` to confirm both Python programs run properly.
- Verified that `mission-02-terminal/terminal-practice/notes.txt` and `notes-backup-renamed.txt` exist.
- Audited the Git commit history across `main` and `update-about`.
- Confirmed that the repository is public and Pull Request #1 remains open and unmerged.
- Wrote the final review and checklist below.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `find . -not -path "./.git/*" -type f \| sort` | Verify all required folders and files exist |
| `python3 mission-04-programs/hello.py` | Test the Mission 4 Python script |
| `python3 mission-05-numbers-data/number_converter.py` | Test the Mission 5 number converter with positive inputs |
| `git status` | Check that the working tree is clean on `main` |
| `git log --oneline --all` | Review all commits across `main` and `update-about` |
| `gh repo view` | Verify repository visibility (`public`) and default branch (`main`) |
| `gh pr view 1` | Confirm Pull Request #1 is open and unmerged |

## 4. My understanding

### Final repository review

All required mission directories (`mission-00-setup` through `mission-08-final-report`), the root `README.md`, `.gitignore`, practice text files, and Python scripts (`hello.py` and `number_converter.py`) are present and verified. No empty placeholders or sensitive personal details (computer username, device name, private IP, or email) appear in any tracked file.

### Corrections made during audit

- Added the actual Mission 6 commit hash (`fd5c326`) and corrected the `git status` output snippet in `mission-06-git-github/README.md` in follow-up commit `7060d8d`.
- Renamed the Mission 2 backup file to `notes-backup-renamed.txt` and updated `mission-02-terminal/README.md` in follow-up commit `8e0432d` (`Document backup rename in Mission 2 terminal practice`).
- Clarified the running and sleeping process counts in `mission-03-operating-system/README.md` in follow-up commit `a29b332` (`Clarify process states in Mission 3 OS snapshot`).

### Mission status summary

| Mission | Topic | Status | Commit |
|---------|-------|--------|--------|
| Mission 0 | Setup and GitHub Workspace | Complete | `71b908e` (`Set up Digital Detective mission structure`) |
| Mission 1 | Computer Basics and IPOS | Complete | `90fca1b` (`Complete computer basics and IPOS mission`) |
| Mission 2 | Terminal and File Management | Complete | `c1e729c` (`Complete Terminal and file management mission`) & `8e0432d` (`Document backup rename in Mission 2 terminal practice`) |
| Mission 3 | Operating System | Complete | `f3586cc` (`Document operating system and file management`) & `a29b332` (`Clarify process states in Mission 3 OS snapshot`) |
| Mission 4 | How Programs Run | Complete | `84bfce1` (`Compare compilers and interpreters`) |
| Mission 5 | Numbers and Data | Complete | `cae40dc` (`Build number converter and practise data representation`) |
| Mission 6 | Git and GitHub | Complete | `fd5c326` (`Complete Git and GitHub collaboration mission`) & `7060d8d` (`Update Mission 6 README with commit hash`) |
| Mission 6 (branch) | `update-about` root README update | Complete | `79572f3` (`Add My Learning section to root README`) |
| Mission 7 | Computer Networks | Complete | `9393c78` (`Explain networking concepts and website communication`) |
| Mission 8 | Final Report and Submission | Complete | `01509b6` (`Complete final report and verify assignment submission`) & follow-up correction commit |

### Branch and Pull Request status

- **Repository URL:** https://github.com/Aayush-Raj07/digital-detective-8526 (Public, default branch `main`)
- **Branch `update-about`:** Published on GitHub
- **Pull Request #1:** https://github.com/Aayush-Raj07/digital-detective-8526/pull/1 (`update-about` → `main`) — **Open and unmerged** as instructed by the assignment rules.

### Final checklist

- [x] All mission folders exist (`mission-00-setup` through `mission-08-final-report`).
- [x] Every mission has its own `README.md`.
- [x] Every mission README contains all nine required sections.
- [x] Every mission has a dedicated meaningful commit pushed to GitHub.
- [x] IPOS, hardware, software, and everyday systems are covered.
- [x] Terminal operations and file management (`notes.txt`, `notes-backup-renamed.txt`) are covered.
- [x] Flags (`ls -lah`) and pipes (`ls -lah | head -n 5`) are explained.
- [x] Package manager (`brew`) observations are recorded.
- [x] OS details, processes (`ps`, `top`), paths, storage (`df -h /`), and permissions (`ls -l`) are covered.
- [x] All six OS responsibilities are explained.
- [x] `hello.py` runs and compiler vs interpreter are compared.
- [x] All seven number conversions include working and Python verification.
- [x] `number_converter.py` runs and was tested with 13, 25, and 255 (plus validation checks).
- [x] ASCII and UTF-8 text encoding are explained.
- [x] Git workflow, `update-about` branch, and open PR #1 are visible on GitHub.
- [x] LAN, MAN, WAN, DNS, router, protocol, packet switching, and client-server are explained.
- [x] Connectivity (`ping`) and DNS (`nslookup`) observations are safely recorded.
- [x] Website-opening sequence is explained in six steps.
- [x] Root `README.md` includes title, introduction, mission links, topics, converter instructions, and learning summary.
- [x] No personal or sensitive information is exposed.
- [x] Final changes are committed and pushed.

### Remaining manual submission step

Submitting the repository URL (`https://github.com/Aayush-Raj07/digital-detective-8526`) through the instructor's Google Form has **not** been done here and remains a manual step for the student.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-08-final-report/README.md` — this final report and checklist
- Complete repository published at `https://github.com/Aayush-Raj07/digital-detective-8526`

## 8. Commit details

Commit message: `Complete final report and verify assignment submission` (`01509b6`)
Correction commit: `Update Mission 8 final report with correction commits`
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`
