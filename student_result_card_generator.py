# Student Result Card Generator

def format_name(name):
    """Remove extra spaces and capitalize each word."""
    return name.strip().title()


def get_valid_marks(subject):
    """Ask for marks until a valid value between 0 and 100 is entered."""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks! Enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_percentage(total, max_total):
    """Calculate percentage."""
    return (total / max_total) * 100


def get_grade(percentage):
    """Return the letter grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "Fail"


def main():
    print("=" * 45)
    print("       STUDENT RESULT CARD GENERATOR")
    print("=" * 45)

    name = format_name(input("Enter student name: "))

    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            break
        print("Invalid roll number! Digits only.")

    subjects = ["English", "Mathematics", "Computer",
                "Science", "Statistics"]
    marks_list = []

    for subject in subjects:
        marks_list.append(get_valid_marks(subject))

    total_marks = sum(marks_list)
    max_total = 500
    percentage = calculate_percentage(total_marks, max_total)
    grade = get_grade(percentage)

    # A mark below 40 in any subject means the student fails.
    status = "Pass" if all(mark >= 40 for mark in marks_list) else "Fail"
    if status == "Fail":
        grade = "Fail"

    print("\n" + "=" * 45)
    print("             STUDENT RESULT CARD")
    print("=" * 45)
    print(f"Student Name    : {name}")
    print(f"Roll Number     : {roll_number}")
    print("-" * 45)
    print(f"{'Subject':<20}{'Obtained Marks':>20}")
    print("-" * 45)

    for subject, marks in zip(subjects, marks_list):
        print(f"{subject:<20}{marks:>20.2f}")

    print("-" * 45)
    print(f"Total Marks     : {total_marks:.2f} / {max_total}")
    print(f"Percentage      : {percentage:.2f}%")
    print(f"Letter Grade    : {grade}")
    print(f"Final Status    : {status}")
    print("=" * 45)
    print("          RESULT CARD GENERATED")
    print("=" * 45)


if __name__ == "__main__":
    main()
