# Student Report Card System

students = {}

# Function to add student details
def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!\n")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    student_class = input("Enter Class: ")

    students[roll_no] = {
        "Name": name,
        "Age": age,
        "Class": student_class,
        "Grades": {}
    }

    print("Student added successfully!\n")


# Function to add or update grades
def add_update_grades():
    roll_no = input("Enter Roll Number: ")

    if roll_no not in students:
        print("Student not found!\n")
        return

    while True:
        subject = input("Enter Subject Name: ")
        marks = float(input("Enter Marks (0-100): "))

        students[roll_no]["Grades"][subject] = marks

        choice = input("Add another subject? (yes/no): ").lower()
        if choice != "yes":
            break

    print("Grades updated successfully!\n")


# Function to display report card
def display_report_card():
    roll_no = input("Enter Roll Number: ")

    if roll_no not in students:
        print("Student not found!\n")
        return

    student = students[roll_no]

    print("\n========== STUDENT REPORT CARD ==========")
    print("Roll Number :", roll_no)
    print("Name        :", student["Name"])
    print("Age         :", student["Age"])
    print("Class       :", student["Class"])

    grades = student["Grades"]

    if not grades:
        print("\nNo grades available.")
        return

    print("\nSubject\t\tMarks")
    print("-" * 30)

    total = 0

    for subject, marks in grades.items():
        print(f"{subject}\t\t{marks}")
        total += marks

    average = total / len(grades)

    # Grade Calculation
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("-" * 30)
    print("Total Marks :", total)
    print("Average     :", round(average, 2))
    print("Grade       :", grade)
    print("=========================================\n")


# Main Menu
while True:
    print("===== Student Report Card System =====")
    print("1. Add Student")
    print("2. Add/Update Grades")
    print("3. Display Report Card")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_update_grades()
    elif choice == "3":
        display_report_card()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Please try again.\n")
