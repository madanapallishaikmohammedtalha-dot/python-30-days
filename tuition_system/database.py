#database.py
from models import Student

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


# database.py
from models import Student

def add_student(name, age, course):
    # 1. Connect
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()

    # 2. Insert (using arguments passed into the function)
    local_cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (name, age, course))

    local_conn.commit()
    local_conn.close()

def list_students():
    # 1. Open the connection locally
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()

    # 2. Retrieve the data
    local_cursor.execute("SELECT name, age, course FROM students")
    rows = local_cursor.fetchall()

    # 3. Close the connection right after fetching (before printing!)
    local_conn.close()
    students=[]
    for row in rows:
        students.append(Student(row[0], row[1], row[2]))
    return students


def search_student(name):
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()

    local_cursor.execute("SELECT name, age, course FROM students WHERE name = ?", (name,))
    row = local_cursor.fetchone() # row is either ("talha", 19, "python") OR None

    local_conn.close() # Close connection right after fetching
    return row != None


def update_course(name,new_course):

    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()
    local_cursor.execute("UPDATE students SET course = ? WHERE name = ?", (new_course, name))
    local_conn.commit()
    count=local_cursor.rowcount 
    local_conn.close()
    return count > 0

def delete_student(name):
    local_conn = sqlite3.connect("students.db")
    local_cursor = local_conn.cursor()
    local_cursor.execute("DELETE FROM students WHERE name=?", (name,))
    local_conn.commit()
    count = local_cursor.rowcount # Save this BEFORE closing
    local_conn.close()
    return count > 0 # Return True if deleted, False if not