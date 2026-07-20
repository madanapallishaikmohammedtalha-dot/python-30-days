#database.py
from models import Student
import sqlite3
def setup_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade TEXT NOT NULL,
            joining_date TEXT NOT NULL,
            fees_allotted REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, grade, joining_date, fees_allotted):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    # Note: 4 placeholders for 4 columns (excluding id because it's autoincrement)
    cursor.execute("INSERT INTO students (name, grade, joining_date, fees_allotted) VALUES (?, ?, ?, ?)",
                   (name, grade, joining_date, fees_allotted))
    conn.commit()
    conn.close()

def list_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade, joining_date, fees_allotted FROM students")
    rows = cursor.fetchall()
    conn.close()

    # Map raw rows to your updated Student object
    return [Student(row[0], row[1], row[2], row[3]) for row in rows]

def search_student(name):
    conn=sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade, joining_date,fees_allotted FROM students WHERE name=?",(name,))
    rows =cursor.fetchone()
    conn.close()
    return rows!= None

def update_details(name,new_grade,new_joining_date,new_fees):
    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE students SET grade = ?,joining_date =?,fees_allotted = ? WHERE name =?",(new_grade,new_joining_date,new_fees,name))
    conn.commit()
    count=cursor.rowcount
    conn.close()
    return count > 0

def delete_student(name):
    conn=sqlite3.connect("students.db")
    cursor =conn.cursor()
    cursor.execute("DELETE FROM students WHERE name = ?",(name,))
    conn.commit()
    count=cursor.rowcount
    conn.close()
    return count > 0
