students=[]
class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def __str__(self):
        return f"name:{self.name} |age:{self.age} |course:{self.course}"

def add_student():

    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")

    new_student = Student(name, age, course)

    students.append(new_student)

def list_students():
    for student in students:
        print(student)

while True:
    print("\n========== STUDENT MANAGENEMENT ==============")
    print("1. Add student")
    print("2. List of students")
    print("3. Quit")
    choice=input("enter the choice:")

    if choice == "1":
        add_student()
    elif choice =="2":
        list_students()
    elif choice=="3":
        print("quit")
        break
    else:
        print("invalid input")