# Mission 5 — Number Systems, Python and Text Encoding

## 1. Task / objective

Manually convert numbers between decimal, binary, and hexadecimal. Verify every conversion using Python. Build a working number converter program. Explain ASCII and UTF-8 text encoding.

## 2. Work completed

- Completed all seven manual conversions with working shown.
- Verified every result using Python built-in functions in the Terminal.
- Created `number_converter.py` and tested it with inputs 13, 25, 255, 0, -3, and invalid text.
- Documented ASCII codes for 'A' and 'a' and explained how UTF-8 extends ASCII.

## 3. Commands / tools used

| Command / function | Purpose |
|-------------------|---------|
| `python3 -c "..."` | Run short Python expressions from Terminal |
| `bin(n)` | Convert a decimal integer to its binary string (prefixed `0b`) |
| `hex(n)` | Convert a decimal integer to its hexadecimal string (prefixed `0x`) |
| `int(s, base)` | Parse a string in base 2 or 16 into a decimal integer |
| `python3 number_converter.py` | Run the interactive converter |

## 4. My understanding

### Task 5.1 — Manual conversions

| # | Question | Working | Answer |
|---|---------|---------|--------|
| 1 | Decimal 13 → binary | 13÷2=6 r**1**, 6÷2=3 r**0**, 3÷2=1 r**1**, 1÷2=0 r**1** → read remainders bottom-up | **1101** |
| 2 | Decimal 25 → binary | 25÷2=12 r**1**, 12÷2=6 r**0**, 6÷2=3 r**0**, 3÷2=1 r**1**, 1÷2=0 r**1** → read bottom-up | **11001** |
| 3 | Binary 1010 → decimal | (1×8)+(0×4)+(1×2)+(0×1) = 8+0+2+0 | **10** |
| 4 | Binary 1101 → decimal | (1×8)+(1×4)+(0×2)+(1×1) = 8+4+0+1 | **13** |
| 5 | Hex A → decimal | A means 10 in hex; 10×16⁰ = 10 | **10** |
| 6 | Hex 1F → decimal | (1×16)+(15×1) = 16+15 | **31** |
| 7 | Binary 1111 → hex | (1×8)+(1×4)+(1×2)+(1×1) = 15; 15 in hex is F | **F** |

---

### Task 5.2 — Python verification

```bash
python3 -c "print(bin(13)); print(bin(25)); print(int('1010',2)); print(int('1101',2)); print(hex(13)); print(hex(25)); print(int('A',16)); print(int('1F',16)); print(hex(0b1111))"
```

Actual output:
```
0b1101
0b11001
10
13
0xd
0x19
10
31
0xf
```

| Expression | Output | Matches manual? |
|-----------|--------|----------------|
| `bin(13)` | `'0b1101'` | ✓ Yes |
| `bin(25)` | `'0b11001'` | ✓ Yes |
| `int('1010', 2)` | `10` | ✓ Yes |
| `int('1101', 2)` | `13` | ✓ Yes |
| `hex(13)` | `'0xd'` | ✓ Yes |
| `hex(25)` | `'0x19'` | ✓ Yes |
| `int('A', 16)` | `10` | ✓ Yes |
| `int('1F', 16)` | `31` | ✓ Yes |
| `hex(0b1111)` | `'0xf'` | ✓ Yes |

All manual answers confirmed.

---

### Task 5.3 — Number converter program

`number_converter.py` asks for a positive integer and shows its binary and hexadecimal equivalents. It uses `bin()` and `hex()` from Python's standard library. Zero and negative numbers are rejected. Non-numeric input is caught with a `try/except ValueError` block.

**Actual test session:**
```
$ python3 mission-05-numbers-data/number_converter.py
Enter a positive integer (or 'q' to quit): 13
Decimal:     13
Binary:      0b1101
Hexadecimal: 0xd

Enter a positive integer (or 'q' to quit): 25
Decimal:     25
Binary:      0b11001
Hexadecimal: 0x19

Enter a positive integer (or 'q' to quit): 255
Decimal:     255
Binary:      0b11111111
Hexadecimal: 0xff

Enter a positive integer (or 'q' to quit): 0
Please enter a positive integer.

Enter a positive integer (or 'q' to quit): -3
Please enter a positive integer.

Enter a positive integer (or 'q' to quit): abc
That does not look like a whole number. Please try again.

Enter a positive integer (or 'q' to quit): q
Goodbye!
```

255 in binary is `11111111` — eight 1-bits, the maximum value of one byte (8 bits). Its hex equivalent is `ff`.

---

### Task 5.4 — Text encoding

Computers store text as numbers. An encoding standard defines which number maps to which character.

| Character | ASCII decimal | Binary | Hex |
|-----------|--------------|--------|-----|
| `A` | **65** | 01000001 | 0x41 |
| `a` | **97** | 01100001 | 0x61 |

**Why an encoding standard is needed:**  
Without an agreed mapping, the number 65 could mean different things on different systems. ASCII gave every computer the same table, so a file created on one machine displays correctly on another.

**Character outside basic ASCII:**  
The Euro symbol `€` is code point U+20AC. It does not exist in the 128-character ASCII table, so it needs an extended standard.

**How ASCII and UTF-8 relate:**  
ASCII covers 128 characters (0–127) using 7 bits. UTF-8 is a superset: for the first 128 code points it uses the exact same single byte as ASCII, so all ASCII files are automatically valid UTF-8. For characters beyond that — accented letters, Asian scripts, emoji — UTF-8 uses 2, 3, or 4 bytes per character. This design means old ASCII software still works unchanged, while UTF-8 can represent every language and symbol in the world.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-05-numbers-data/number_converter.py` — interactive number converter
- All seven manual conversions verified against Python output

## 8. Commit details

Commit message: `Build number converter and practise data representation`
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`
