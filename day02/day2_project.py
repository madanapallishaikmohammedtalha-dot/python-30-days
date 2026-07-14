# Student Management System

students = []


# Function 1: Add Student
def add_student(students):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print(f"\n✅ Added {name} successfully.\n")


# Function 2: List Students
def list_students(students):
    if not students:
        print("\nNo students yet.\n")
        return

    print("\n----- Student List -----")

    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")

    print()


# Function 3: Search Student
def search_student(students, name):
    found = False

    for student in students:
        if name.lower() in student["name"].lower():
            print("\nStudent Found")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}\n")
            found = True

    if not found:
        print("\nNo match found.\n")


# Function 4: Update Course
def update_course(students, name, new_course):
    for student in students:
        if student["name"].lower() == name.lower():
            student["course"] = new_course
            print(f"\nUpdated {student['name']}'s course to {new_course}.\n")
            return

    print("\nStudent not found.\n")


# ---------------- Main Program ----------------

while True:

    print("========== Student Management ==========")
    print("1. Add Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Update Course")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        list_students(students)

    elif choice == "3":
        name = input("Enter student name to search: ")
        search_student(students, name)

    elif choice == "4":
        name = input("Enter student name: ")
        new_course = input("Enter new course: ")
        update_course(students, name, new_course)

    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.\n")