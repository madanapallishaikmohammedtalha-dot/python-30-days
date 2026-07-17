import sqlite3

# 1. Connect
conn = sqlite3.connect("practice.db")
cursor = conn.cursor()

# 2. Select data (Read)
cursor.execute("SELECT name, age, course FROM students")
rows = cursor.fetchall()

# 3. Print the results
print("----- Retrieved Students -----")
for row in rows:
    # Each row is a tuple: (name, age, course)
    print(f"Name: {row[0]} |  Age: {row[1]} | Course: {row[2]}")

# 4. Close (No need to commit since we only read!)
conn.close()