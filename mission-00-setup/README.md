# Mission 0 — Setup and GitHub Workspace

## 1. Task / objective

Create the assignment repository on GitHub, build the required folder structure locally, and push the first commit. Verify that Python and Git are available.

## 2. Work completed

- Verified Python 3 (`Python 3.15.2`) and Git (`git version 2.55.0`) are installed.
- Created the project folder `digital-detective-8526` on the Desktop.
- Created all nine mission folders plus the terminal-practice sub-folder.
- Created `.gitignore` to keep macOS metadata and Python cache out of the repository.
- Written the root `README.md` with the project title, mission index, and notes.
- Initialised a local Git repository and set the branch name to `main`.
- Created a public GitHub repository named `digital-detective-8526` under account `Aayush-Raj07`.
- Pushed the initial commit and verified the repository is visible on GitHub.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `python3 --version` | Verify Python 3 is available; actual output: `Python 3.15.2` |
| `git --version` | Verify Git is available; actual output: `git version 2.55.0` |
| `mkdir -p` | Create all required directories in one command |
| `git init` | Initialise an empty local Git repository |
| `git branch -M main` | Set the default branch name to `main` |
| `git add .` | Stage all new files for the first commit |
| `git commit -m` | Create a snapshot with a meaningful message |
| `git remote add origin` | Link the local repository to GitHub |
| `git push -u origin main` | Push `main` to GitHub and set the upstream |
| `gh repo create` | Create the public repository on GitHub via CLI |

## 4. My understanding

A **Git repository** is a folder that Git tracks. Every time I run `git commit`, Git saves an exact snapshot of the files I staged. This creates a history I can go back to at any point.

I organised the work into separate mission folders so each topic is self-contained and each commit maps to one piece of work. That makes the history easy to read and each folder easy to navigate.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `.gitignore` — excludes `.DS_Store` and `__pycache__/`
- `README.md` — project title, mission index, run instructions, learning summary
- All nine mission folders created on the Desktop

## 8. Commit details

Commit message: `Set up Digital Detective mission structure`
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`
