# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective

Practise navigating the filesystem, managing files, using command flags and pipes, and exploring the Homebrew package manager — all from the macOS Terminal.

## 2. Work completed

- Navigated directories using `pwd`, `ls`, and `cd`.
- Created, copied, moved, and read files using `touch`, `cp`, `mv`, and `cat`.
- Used `printf` with `>` and `>>` to write and append text to `notes.txt`.
- Demonstrated the `ls -lah` flag combination and a pipe to `head -n 5`.
- Checked Homebrew version and listed installed packages.
- Created `terminal-practice/notes.txt`, made a backup copy (`notes-backup.txt`), and renamed the backup to `terminal-practice/notes-backup-renamed.txt`.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `pwd` | Print the full path of the current directory |
| `ls` | List files and folders in the current directory |
| `ls -l` | Detailed listing with permissions, size, and date |
| `ls -lah` | Detailed listing including hidden files, human-readable sizes |
| `cd` | Change directory |
| `mkdir -p` | Create a directory (and parent directories if needed) |
| `touch` | Create an empty file |
| `cp` | Copy a file |
| `mv` | Move or rename a file |
| `cat` | Print a file's contents to the terminal |
| `printf` | Write formatted text; used with `>` (overwrite) and `>>` (append) |
| `head -n 5` | Show only the first 5 lines of input |
| `brew --version` | Show the installed Homebrew version |
| `brew list` | List all packages managed by Homebrew |

## 4. My understanding

### Task 2.1 — Basic Terminal operations

I ran these commands from inside `digital-detective-8526`:

| Command | Observation |
|---------|------------|
| `pwd` | Printed `/Users/[redacted]/Desktop/digital-detective-8526` — the absolute path of my location |
| `ls` | Listed all visible mission folders and README.md |
| `ls -l` | Same list with permissions, link count, owner, size in bytes, and date |
| `cd ..` | Moved up to Desktop; `pwd` confirmed `/Users/[redacted]/Desktop` |
| `cd digital-detective-8526` | Returned to the project folder |
| `mkdir -p terminal-practice` | Created the sub-folder (no error; `-p` prevents failure if it already exists) |
| `touch notes.txt` | Created an empty `notes.txt` |
| `cp notes.txt notes-backup.txt` | Made a copy |
| `mv notes-backup.txt notes-backup-moved.txt` | Renamed the copy |
| `cat notes.txt` | Displayed contents (empty at that point) |

---

### Task 2.2 — File operations in `terminal-practice/`

```bash
cd mission-02-terminal/terminal-practice
touch notes.txt
printf 'First line of text\n' > notes.txt
printf 'Second line appended\n' >> notes.txt
cat notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt notes-backup-renamed.txt
ls -lah
```

Output of `cat notes.txt`:
```
First line of text
Second line appended
```

Output of `ls -lah`:
```
total 16
drwxr-xr-x@ 4 [redacted]  staff   128B Nov 25 19:05 .
drwxr-xr-x@ 4 [redacted]  staff   128B Nov 25 18:49 ..
-rw-r--r--@ 1 [redacted]  staff    40B Nov 25 18:48 notes-backup-renamed.txt
-rw-r--r--@ 1 [redacted]  staff    40B Nov 25 18:48 notes.txt
```

**Q: What is the difference between replacing file contents and appending text?**
Using `>` replaces the file. Using `>>` adds to the end without touching existing content.

**Q: What is the difference between copying and moving?**
`cp` leaves the original file in place and creates a new copy. `mv` removes the file from its current location and places it in the new location (or renames it in place).

**Q: What does `pwd` tell us?**
It shows the full absolute path of the current directory, confirming exactly where you are.

**Q: Why is `ls` useful?**
It lets you quickly see what files and folders exist without opening a graphical file browser.

---

### Task 2.3 — Flags and pipes

A **flag** (or option) changes how a command behaves. For example:
- `-l` on `ls` enables the long format (permissions, owner, size, date).
- `-a` shows hidden files (names starting with `.`).
- `-h` makes file sizes human-readable (e.g., `128B` instead of `128`).

A **pipe** (`|`) sends the output of one command directly as input to the next.

```bash
ls -lah | head -n 5
```

Output:
```
total 16
drwxr-xr-x@ 13 [redacted]  staff   416B Nov 25 18:45 .
drwx------@ 12 [redacted]  staff   384B Nov 25 18:44 ..
-rw-r--r--@  1 [redacted]  staff   108B Nov 25 18:45 .gitignore
-rw-r--r--@  1 [redacted]  staff   2.2K Nov 25 18:45 README.md
```

`ls -lah` lists everything. `head -n 5` keeps only the first five lines. Without the pipe, the full listing would scroll off screen for large folders.

---

### Task 2.4 — Package manager (Homebrew)

Homebrew is the standard package manager for macOS. It lets you install command-line tools and libraries from the Terminal without manually downloading installers.

```bash
brew --version
```
Output: `Homebrew 7.0.13`

```bash
brew list | head -n 10
```
Output (first ten packages):
```
ada-url
brotli
c-ares
ca-certificates
cairo
certifi
cffi
dav1d
deno
ffmpeg
```

No packages were installed or removed during this mission.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-02-terminal/terminal-practice/notes.txt` — two-line text file created during the mission
- `mission-02-terminal/terminal-practice/notes-backup-renamed.txt` — renamed backup copy

## 8. Commit details

Commit message: `Complete Terminal and file management mission`
Correction commit: `Document backup rename in Mission 2 terminal practice`
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`
