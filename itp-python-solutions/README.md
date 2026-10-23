# ITP Python Practical Solutions

Solutions for all 10 uploaded Introduction to Programming worksheets (VBCS1101): **219 question-specific Python programs**. Both implementation questions and practice exercises are included, along with Practical 7's separate indexing and slicing section.

## Setup and run

Use Python 3.10 or newer. NumPy is the only external dependency, required for array questions.

```bash
python -m pip install -r requirements.txt
python practical_01/main_01.py
python practical_06/practice_01.py --demo
python run_all.py
python -m unittest discover -s tests -v
```

On Windows, use `py` in place of `python` if needed. Run these commands from the extracted project folder.

For questions requiring input, enter your own values or press Enter to accept the sample value shown in brackets. `--demo` uses the sample values without waiting for keyboard input. Fixed-data and output-prediction questions run directly using the worksheet values. Intentional errors are caught and explained, or corrected with comments. Input validation is educational and may raise a clear `ValueError` rather than repeatedly prompting.

## Find a question

| Practical | Topic | Main | Additional slicing | Practice | Total |
|---|---|---:|---:|---:|---:|
| 1 | Variables, constants, types | 11 | 0 | 10 | 21 |
| 2 | Input/output and expressions | 10 | 0 | 10 | 20 |
| 3 | Decision making | 10 | 0 | 10 | 20 |
| 4 | Loops and patterns | 10 | 0 | 10 | 20 |
| 5 | break, continue, pass | 10 | 0 | 10 | 20 |
| 6 | Lists as matrices and NumPy arrays | 12 | 0 | 10 | 22 |
| 7 | Lists, tuples, indexing and slicing | 12 | 8 | 10 | 30 |
| 8 | Dictionaries | 12 | 0 | 10 | 22 |
| 9 | Functions and recursion | 12 | 0 | 10 | 22 |
| 10 | Strings | 12 | 0 | 10 | 22 |
| **Total** | | **111** | **8** | **100** | **219** |

`practical_XX/main_YY.py` matches implementation Question YY. `practice_YY.py` matches the practice exercise with that number. Practical 7's repeated Question 1–8 numbering is kept separately as `slicing_01.py` through `slicing_08.py`.

Each practical folder includes `ANSWERS.md`, with links to its programs and their actual sample outputs. `manifest.json` lists every question. Memory identity values in Practical 1 vary between runs, as do platform-specific integer dtype labels.

## Assumptions and worksheet inconsistencies

- Examples without supplied values use clearly visible sample data; these are not claimed to be worksheet datasets. Personal details in examples are illustrative.
- Indices are zero-based unless labelled as one-based positions, days, patients, rooms, shelves or slots. Practical 6 main Q1's `(2,3)` is interpreted as the second row, third column; Practical 7 NumPy `(1,2)` is interpreted as zero-based indexing.
- Practical 2 main Q5 has no deductions: its requested net salary is basic + HRA + DA. Main Q7 uses an illustrative fixed INR 83/USD rate, not a current exchange rate.
- Where grades are unspecified, use Practical 3's thresholds: A >=90, B >=75, C >=50, else Fail. Marks are assumed out of 100 per subject.
- Practical 2 practice Q1: Rs 150 covers up to 100 units; only excess units attract Rs 6 each. Q7 explicitly uses simple interest over 24 months, not a reducing-balance EMI formula.
- Practical 3 main Q8 omits comparison symbols: use >=2000 and >=1000. Practice Q3 explicitly says "above", so use strict >5000 and >2000.
- Practical 3 practice Q5 assumes any started parking hour is chargeable, zero hours is free, and the input covers one day (0–24 hours). Q6 assumes child 0–12, teen 13–19, adult 20–59, senior 60+.
- BMI exercises use assumed adult classroom bands: <18.5, <25, <30, otherwise obese. Practical 3 practice Q9 uses assumed systolic-only bands: <120 normal, <130 elevated, <140 stage 1, otherwise stage 2. These are programming classifications, not individual medical assessments.
- Practical 5 main Q6 prints strictly positive numbers, excluding zero. Practice Q5's "unlimited retries" conflicts with its five-failure limit; the five-failure cap is implemented. Practice Q9 assumes day 1 is Monday. Sensor negatives are skipped because the worksheet explicitly defines them as faulty.
- Practical 6 practice Q1 defines highest/lowest day by cross-zone daily average and also gives each zone's high/low days. Q2 labels temperatures Celsius, but values resemble Fahrenheit: original values are retained without silently relabelling or converting them. "Critical" has no supplied threshold, so the highest-temperature patient is identified.
- Practical 6 practice Q3 reports both busiest rooms in a tie. Q5 interprets busiest shelf as largest total stock. Q6 supplies 24 values and explicitly requests 3 x 8, despite mentioning 3 junctions over 24 hours; all 24 values are reshaped to 3 x 8. Q9 and Q10 use random data with seed 42 for reproducibility and inclusive specified bounds.
- Practical 7 practice Q1 assumes newest-first book history, with the oldest item at the end. Q5 replaces a tuple in the outer mutable list after demonstrating failed tuple-element assignment. Q8 says 20 route points but supplies only 10: those 10 are used. Q10 reports repeated room IDs and floor-category counts to address both interpretations of "categories".
- Practical 9 practice Q1 uses five elapsed intervals for six hourly battery readings: average drop is 4.8 percentage points per hour. Recursive examples are intended for small classroom inputs; large recursion depths can hit Python's recursion limit.
- Practical 10 main Q2 uses the conventional exclusive slice endpoint `[2:7]` and explains `[2:8]` for inclusive index 7. Main Q11 ignores case, spaces and punctuation when checking palindromes. Main Q12 counts case-insensitive word tokens, includes spaces in character count, and reports all most-frequent ties. Practice Q4 assumes a minimum password length of eight because the worksheet omits it.
- Passwords and PINs in these examples are demonstration values, not a production authentication design.

## Validation

The included tests execute all 219 scripts in demo mode, check independently specified outputs for 54 questions, and exercise 31 input/boundary cases. All tests passed in the preparation environment. See `VALIDATION.md` for the exact run result.

## Repository

Published in [void111x/depos](https://github.com/void111x/depos), in the `itp-python-solutions` folder. Original worksheet PDFs are not included.
