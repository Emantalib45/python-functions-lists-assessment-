# Student Marks and Result Programs

This repository contains two Python programs for recording student marks and displaying academic performance reports.

## Files Included

| File | Description |
|---|---|
| `class_marks_analyzer.py` | Collects marks for an entire class and generates a class performance report. |
| `student_result_card_generator.py` | Collects one student's details and subject marks, then generates an individual result card. |

## Requirements

- Python 3
- A terminal or command prompt, or a Python IDE such as IDLE or VS Code

No external Python libraries are required.

## 1. Class Marks Analyzer

### Purpose
Analyzes the marks of all students in a class and displays overall class performance.

### How it works
1. Asks how many students are in the class.
2. Collects each student's name and marks.
3. Stores names in `student_names` and marks in `student_marks`.
4. Checks that each mark is between 0 and 100. Invalid marks are requested again.
5. Calculates the class average.
6. Finds the highest and lowest marks and displays every student who achieved each.
7. Counts passing students (50 or above) and failing students (below 50).
8. Displays students whose marks are above the class average.
9. Displays marks sorted from highest to lowest.

### Python concepts used
- Lists and `.append()`
- `for` and `while` loops
- `len()`, `sum()`, `max()`, `min()`, and `sorted()`
- Conditional statements and input validation

### Run the program
```bash
python class_marks_analyzer.py
```

Enter a positive whole number of students when prompted. Then enter each student's name and a numeric mark from 0 to 100.

## 2. Student Result Card Generator

### Purpose
Creates a formatted result card for one student, including subject marks, total, percentage, letter grade, and final pass/fail status.

### How it works
1. Asks for the student's name and formats it by removing extra spaces and capitalizing each word.
2. Requests a roll number and accepts digits only.
3. Collects marks for five subjects:
   - English
   - Mathematics
   - Computer
   - Science
   - Statistics
4. Validates each mark so it is numeric and between 0 and 100.
5. Calculates the total out of 500 and the percentage.
6. Assigns a letter grade based on the percentage.
7. Sets the final status to **Fail** if any subject mark is below 40; otherwise, the status is **Pass**.
8. Prints a formatted result card.

### Grade scale

| Percentage | Grade |
|---:|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | Fail |

**Important:** The final status uses a separate subject-level rule: a student fails if any one subject mark is below 40. If the final status is Fail, the displayed letter grade is also set to Fail.

### Python concepts used
- Functions and return values
- Lists and `.append()`
- `while` loops and `for` loops
- `try` / `except` for invalid numeric input
- `sum()`, `all()`, and `zip()`
- Conditional statements and formatted strings

### Run the program
```bash
python student_result_card_generator.py
```

Enter the student's name, a digits-only roll number, and marks for each of the five subjects.

## Running the Programs

Save both `.py` files in the same folder. Open a terminal in that folder and run either command:

```bash
python class_marks_analyzer.py
```

or

```bash
python student_result_card_generator.py
```

Each program runs independently.

## Notes

- Marks must be numeric values from 0 to 100.
- The Class Marks Analyzer expects a positive number of students.
- The Student Result Card Generator uses five fixed subjects and a maximum total of 500 marks.
- All information is entered during program execution; these programs do not save results to a file or database.
