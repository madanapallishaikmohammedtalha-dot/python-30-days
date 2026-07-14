#Day 1 Challenge — interactive student profile
name=input("name:")
age=int(input(" age:"))
city=input("City:")
college_name=input("college name:")
goal=input("What do you want to become? :")
daily_study=float(input("Hours per day you'll study python:"))
total_hours=daily_study*30

print("\n=============== STUDENT PROFILE =======")
print(f"Name:              {name}")
print(f"Age:               {age}")
print(f"City:              {city}")
print(f"College name:      {college_name}")
print(f"Goal:              {goal}")
print(f"Daily study:       {daily_study} hours")
print(f"30-day total:      {total_hours} hours")
print("=======================================")