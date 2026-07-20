# main.py
import database
database.setup_database()
while True:
    print("\n======== STUDENT MANAGEMENT ========")
    print("1. Add Student\n2. List Students\n3. Search\n4. Update\n5. Delete\n6. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        # UI layer asks for data
        name = input("Name: ")
        grade = int(input("Grade: "))
        joining_date = input("Joining Date: ")
        fees_allotted=input("Fees allotted: ")
        # Controller layer calls the database function
        database.add_student(name, grade, joining_date,fees_allotted)
        print("✅ Added successfully!")

    elif choice == "2":
        # List returns the list of students, UI prints them
        students = database.list_students()
        for s in students:
            print(s)

    elif choice == "3":
        name=input("Name:")
        if database.search_student(name):
            print("student found")
        else:
            print("student not found")

    elif choice == "4":
        name=input("Name:")
        new_grade=input("New grade:")
        new_joining_date=input("New Joining Date:")
        new_fees=input("New Fees:")
        if database.update_details(name,new_grade,new_joining_date,new_fees):
            print("successfully updated course")
        else:
            print("student not found")

    elif choice == "5":
        name=input("Name:")
        if database.delete_student(name):
            print(f"successfully deleted {name}")
        else:
            print("Student not found")

    # ... handle other choices similarly ...
    elif choice == "6":
        break

    else:
        print("invalid input.")