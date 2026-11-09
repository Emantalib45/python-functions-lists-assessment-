# Task 2: Class Marks Analyzer

# Ask for the number of students
total_students = int(input("Enter the number of students: "))

# Create two empty lists
student_names = []
student_marks = []

# Input student names and marks
for i in range(total_students):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    student_names.append(name)

    # Validate marks
    while True:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            student_marks.append(marks)
            break
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")

# Calculate class average
class_average = sum(student_marks) / len(student_marks)

# Find highest and lowest marks
highest_marks = max(student_marks)
lowest_marks = min(student_marks)

# Count passing and failing students
passing_students = 0
failing_students = 0

for marks in student_marks:
    if marks >= 50:
        passing_students += 1
    else:
        failing_students += 1

# Display results
print("\n========== CLASS MARKS REPORT ==========")
print("Total Students:", len(student_names))
print("Class Average:", round(class_average, 2))

print("\nHighest Marks:", highest_marks)
print("Student(s) with Highest Marks:")

for i in range(len(student_marks)):
    if student_marks[i] == highest_marks:
        print(student_names[i])

print("\nLowest Marks:", lowest_marks)
print("Student(s) with Lowest Marks:")

for i in range(len(student_marks)):
    if student_marks[i] == lowest_marks:
        print(student_names[i])

print("\nPassing Students:", passing_students)
print("Failing Students:", failing_students)

# Display students scoring above class average
print("\nStudents Scoring Above Class Average:")

for i in range(len(student_marks)):
    if student_marks[i] > class_average:
        print(student_names[i], "-", student_marks[i])

# Sort marks from highest to lowest
sorted_marks = sorted(student_marks, reverse=True)

print("\nMarks Sorted (Highest to Lowest):")
print(sorted_marks)

print("\n========== END OF REPORT ==========")
