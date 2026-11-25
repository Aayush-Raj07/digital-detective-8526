# Mission 4 — How Programs Run

## 1. Task / objective

Write and run a simple Python program, then explain the difference between compiled and interpreted languages.

## 2. Work completed

- Created `hello.py` with a single `print` statement.
- Ran it with `python3 hello.py` and verified the output.
- Built a compiler vs interpreter comparison table.
- Wrote a plain-language explanation of how Python executes code.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `python3 hello.py` | Run the Python script from Terminal |
| `python3 --version` | Verify the Python 3 version (`Python 3.15.2`) |

## 4. My understanding

### Task 4.1 — Writing and running hello.py

`mission-04-programs/hello.py` contains:

```python
print("Hello from Python")
```

Running it:
```bash
python3 mission-04-programs/hello.py
```

Actual output:
```
Hello from Python
```

The `print()` function sends the string to standard output (the Terminal window). One line of code, one line of output.

---

### Task 4.2 — Compiler vs interpreter

| Feature | Compiler | Interpreter |
|---------|----------|-------------|
| When translation happens | Once, before the program runs (compile time) | Each time the program runs (run time) |
| Typical output | A standalone binary/executable file | No separate file — the interpreter is the runtime |
| Example language | C, C++, Rust | Python, Ruby, Bash |
| Main advantage | Faster at runtime because translation is already done | Easier to develop and test — run code immediately without a separate build step |

**Explanation in simple terms:**

A compiler reads the entire source file and translates it into machine code before the program runs. The result is an executable file the CPU can run directly. An interpreter reads and executes the source code line by line at runtime, translating on the fly each time the program runs.

Python is usually described as interpreted. In practice, CPython (the standard Python runtime) first compiles source code to bytecode (`.pyc` files stored in `__pycache__/`), then the Python Virtual Machine interprets that bytecode at runtime. This means Python combines a compile step with an interpret step, but programmers do not need to manage this — just run `python3 script.py` and both happen automatically.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-04-programs/hello.py` — the Python program
- Actual output verified: `Hello from Python`

## 8. Commit details

Commit message: `Compare compilers and interpreters`
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`
