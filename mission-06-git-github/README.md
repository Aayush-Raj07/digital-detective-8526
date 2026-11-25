# Mission 6 — Git and GitHub

## 1. Task / objective

Understand how Git tracks changes, practise core Git commands, create a feature branch, push it to GitHub, and open a Pull Request.

## 2. Work completed

- Practised `git status`, `git add`, `git commit`, and `git log`.
- Created the `update-about` branch and added the "My Learning" section to the root README.
- Pushed the branch to GitHub and opened Pull Request #1.
- Documented the full Git command glossary.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `git status` | Show which files are modified, staged, or untracked |
| `git add <file>` | Stage a file for the next commit |
| `git commit -m "..."` | Save staged changes to the repository history |
| `git log --oneline` | Show compact one-line commit history |
| `git branch` | List local branches |
| `git switch -c <branch>` | Create and switch to a new branch |
| `git push -u origin <branch>` | Push a branch to GitHub and set the upstream |
| `gh pr create` | Create a Pull Request on GitHub via CLI |

## 4. My understanding

### Task 6.1 — Basic Git workflow

Before staging `mission-06-git-github/README.md`:

```
git status
```
Output:
```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
        mission-06-git-github/
```

After `git add mission-06-git-github/README.md`:
```
Changes to be committed:
        new file: mission-06-git-github/README.md
```

**Difference between staging and committing:**
- **Staging (`git add`)** selects which changes to include in the next commit — like packing a box. I can review exactly what will be saved.
- **Committing (`git commit`)** seals that selection permanently into the repository with a message, author, and timestamp — like labelling and storing the box.

`git log --oneline` after the Mission 6 commit:
```
fd5c326 Complete Git and GitHub collaboration mission
cae40dc Build number converter and practise data representation
84bfce1 Compare compilers and interpreters
f3586cc Document operating system and file management
c1e729c Complete Terminal and file management mission
90fca1b Complete computer basics and IPOS mission
71b908e Set up Digital Detective mission structure
```

---

### Task 6.2 — The `update-about` branch

Starting from `main`, I created the branch and added a learning section to the root README:

```bash
git switch -c update-about
# (edit README.md — add "My Learning" section)
git add README.md
git commit -m "Add My Learning section to root README"
git push -u origin update-about
```

A branch is a lightweight pointer to a commit. It lets me work on a change in isolation without affecting `main`. If the change is approved, it can be merged back.

---

### Task 6.3 — Pull Request

I created PR #1 from `update-about` into `main`:

```bash
gh pr create \
  --title "Add My Learning section to root README" \
  --body "Adds a short reflection on what was learned from Missions 0–5." \
  --base main \
  --head update-about
```

**PR details:**
| Field | Value |
|-------|-------|
| PR number | #1 |
| Title | Add My Learning section to root README |
| Source branch | `update-about` |
| Target branch | `main` |
| Status | **Open — not merged** |
| URL | https://github.com/Aayush-Raj07/digital-detective-8526/pull/1 |

The PR is left open and unmerged as instructed. After creating it, I switched back to `main`:

```bash
git switch main
```

---

### Task 6.4 — Git command glossary

| Command | What it does |
|---------|-------------|
| `git init` | Initialises a new Git repository in the current folder |
| `git status` | Shows which files are modified, staged, or untracked |
| `git add` | Moves changes from the working directory into the staging area |
| `git commit` | Saves staged changes permanently to the repository with a message |
| `git log` | Lists the commit history with hashes, authors, and messages |
| `git branch` | Lists existing branches or creates a new one |
| `git switch` | Switches to a different branch |
| `git push` | Uploads local commits to a remote repository (such as GitHub) |
| `git fetch` | Downloads updates from the remote without changing local files |
| `git pull` | Downloads and merges remote updates into the current branch |

**Retrieving remote changes:** `git fetch` downloads new commits from GitHub so I can see what teammates have pushed. `git pull` does the same and also merges those changes into my current branch automatically.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-06-git-github/README.md` — this file
- Branch `update-about` published to GitHub
- PR #1: https://github.com/Aayush-Raj07/digital-detective-8526/pull/1 (open, not merged)

## 8. Commit details

Mission 6 commit message: `Complete Git and GitHub collaboration mission` (`fd5c326`)
Branch commit message: `Add My Learning section to root README` (`79572f3` on `update-about`)
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`
