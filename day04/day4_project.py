# This is my experimental branch - testing Git features!
import sqlite3
conn=sqlite3.connect("students.db")
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               name TEXT,
               age INTEGER,
               course TEXT
               )
               """)

conn.commit()
conn.close()
class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def __str__(self):
        return f"name:{self.name} |age:{self.age} |course:{self.course}"

def add_student():

    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()

    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    local_cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (name, age, course))
    local_conn.commit()
    local_conn.close()
    print(f"\n added {name} successfully ✔️")

def list_students():
    # 1. Open the connection locally
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()

    # 2. Retrieve the data
    local_cursor.execute("SELECT name, age, course FROM students")
    rows = local_cursor.fetchall()

    # 3. Close the connection right after fetching (before printing!)
    local_conn.close()

    # 4. Print the results using our Student class
    print("\n----- Retrieved Students -----")
    for row in rows:
        student_obj = Student(row[0], row[1], row[2])
        print(student_obj)

def search_student():
    name = input("Enter student name to search: ")
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()

    local_cursor.execute("SELECT name, age, course FROM students WHERE name = ?", (name,))
    row = local_cursor.fetchone() # row is either ("talha", 19, "python") OR None

    local_conn.close() # Close connection right after fetching

    if row is not None:
        # No loop! Just make the student object directly from the row
        student_obj = Student(row[0], row[1], row[2])
        print(student_obj)
    else:
        print("\n❌ Student not found.")

def update_course():
    name= input("Enter student name to update: ")
    new_course = input("Enter new course: ")
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()
    local_cursor.execute("UPDATE students SET course = ? WHERE name = ?", (new_course, name))
    if local_cursor.rowcount > 0:
        print(f"\n✅ Successfully updated {name}'s course to {new_course}!")
    else:
        print("\n❌ Student not found.")
    local_conn.commit()
    local_conn.close()

def delete_student():
    name = input("Enter student name to delete: ")
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()
    local_cursor.execute("DELETE FROM students WHERE name=?",(name,))
    if local_cursor.rowcount >0:
        print(f"\nsucessfully deleted {name}")
    else:
        print("student not found")
    local_conn.commit()
    local_conn.close()

while True:
    print("\n======== STUDENT MANAGEMENT========")
    print("1.Add Student")
    print("2.List of students")
    print("3.Search Student ")
    print("4.Update Course")
    print("5.Delete Student")
    print("6.quit ")

    choice=input("Enter your choice(1-5):")
    if choice == "1":
        add_student()
    elif choice == "2":
        list_students()
    elif choice == "3":
        search_student()
    elif choice =="4":
        update_course()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("quit")
        break
    else:
        print("invalid input")