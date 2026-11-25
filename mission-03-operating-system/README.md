# Mission 3 — Understand the Operating System

## 1. Task / objective

Explore the macOS operating system by running Terminal commands, observe running processes, understand file paths and permissions, and explain the six core responsibilities of an OS.

## 2. Work completed

- Inspected OS version and build using `sw_vers`.
- Checked current account identity using `whoami` (redacted in public docs).
- Examined root disk storage using `df -h /`.
- Captured a system activity snapshot using `top -l 1`.
- Listed running processes and their PIDs using `ps -A -o pid,comm | head -n 15`.
- Explained absolute and relative paths with examples from the repository.
- Inspected file permissions on `notes.txt` using `ls -l`.
- Documented all six OS responsibilities with explanations and examples.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `sw_vers` | Display macOS product name, version, and build |
| `whoami` | Display the current logged-in account name |
| `df -h /` | Show disk capacity and usage in human-readable units |
| `top -l 1 -n 3` | Take a one-shot system activity snapshot |
| `ps -A -o pid,comm` | List every running process with its PID and command path |
| `ls -l <file>` | Show detailed file attributes including permission string |

## 4. My understanding

### Task 3.1 — Explore the operating system

**OS version (`sw_vers`):**
```
ProductName:    macOS
ProductVersion: 27.2.1
BuildVersion:   26B131
```
This tells us the exact OS distribution and version. The kernel and system libraries in macOS manage all hardware and provide services to every running app.

**Account identity (`whoami`):**
```
[redacted]
```
This prints the active user's login name. The OS uses this identity to enforce file ownership and access controls. The actual username is redacted here for privacy.

**Storage (`df -h /):**
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   926Gi    13Gi   769Gi     2%    487k  4.3G    0%   /
```
The root volume has 926 GiB total; only 13 GiB (2%) is used, leaving 769 GiB free. The OS manages this APFS partition, tracking which blocks are allocated and which are free.

**System activity snapshot (`top -l 1 -n 3`):**
```
Processes: 846 total, 3 running, 843 sleeping, 4140 threads
Load Avg: 1.71, 2.00, 2.07
CPU usage: 6.53% user, 12.53% sys, 80.92% idle
PhysMem: 15G used (2473M wired, 4339M compressor), 211M unused.
```
846 processes are on the system; the snapshot showed 3 processes in the running state and 843 sleeping (waiting for input or a timer). Physical memory shows 15 GB used and 211 MB unused.

---

### Task 3.2 — Understand processes

A **process** is an instance of a program that is currently running. When I launch Terminal, the OS creates a process for it, allocates memory, and schedules it on the CPU.

The **PID (Process ID)** is a unique number the OS assigns to each active process. It is used to track, communicate with, and terminate processes.

**Actual output of `ps -A -o pid,comm | head -n 15`:**
```
  PID COMM
    1 /sbin/launchd
  332 /usr/libexec/logd
  334 /usr/libexec/smd
  335 /usr/libexec/UserEventAgent
  337 ...fseventsd
  338 ...mediaremoted
  340 /usr/libexec/uarpd
  342 /usr/sbin/systemstats
  344 ...accessoryupdaterd
  345 /usr/libexec/uarpassetmanagerd
  346 /usr/libexec/configd
  347 endpointsecurityd
  348 ...powerd
  349 /usr/libexec/IOMFB_bics_daemon
```

Two examples:
1. **`launchd` (PID 1):** The init process started directly by the kernel. It manages all background daemons and services on macOS.
2. **`logd` (PID 332):** The unified logging daemon. It collects and stores diagnostic log events from apps and system components.

---

### Task 3.3 — Paths and permissions

**Absolute path:** Starts from the root directory `/` and gives the complete location regardless of where you currently are.
> Example: `/Users/[redacted]/Desktop/digital-detective-8526/mission-02-terminal/README.md`

**Relative path:** Gives the location relative to the current working directory.
> Example (from inside `digital-detective-8526`): `mission-02-terminal/README.md`

**File permissions from `ls -l mission-02-terminal/terminal-practice/notes.txt`:**
```
-rw-r--r--@ 1 [redacted]  staff  40 Nov 25 18:48 notes.txt
```

Breaking down `-rw-r--r--`:
| Characters | Who | Permissions |
|-----------|-----|-------------|
| `rw-` | Owner | Can **read** and **write**; cannot execute |
| `r--` | Group (staff) | Can **read** only |
| `r--` | Others | Can **read** only |

- **r (read):** Can view the file's contents.
- **w (write):** Can modify or save the file.
- **x (execute):** Can run the file as a program (not set here — `.txt` is not an executable).

The owner can read and edit `notes.txt`. No one can execute it, which is correct for a plain text file.

---

### Task 3.4 — OS responsibilities

| Responsibility | What it does | Practical example |
|---------------|-------------|-------------------|
| Process management | Creates, schedules, and terminates processes; gives each a share of CPU time | Switching between Terminal and a web browser while both stay responsive |
| Memory management | Allocates RAM to processes; isolates each process's memory; swaps to disk when RAM is full | Ensuring Terminal cannot read memory used by another app |
| Device management | Uses device drivers to communicate with hardware peripherals | Translating a key press on the keyboard into a character in Terminal |
| File management | Organises files in directories; tracks disk blocks; enforces access rules | Creating and saving `notes.txt` to the APFS filesystem |
| User interface / shell | Provides graphical GUI and text-based CLI for user interaction | The macOS Aqua desktop and the Zsh shell in Terminal |
| Security and permissions | Enforces file permissions, user authentication, and process isolation | Preventing one user from reading another user's files |

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-03-operating-system/README.md` — all command outputs and explanations (this file)

## 8. Commit details

Commit message: `Document operating system and file management`
Correction commit: `Clarify process states in Mission 3 OS snapshot`
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`
