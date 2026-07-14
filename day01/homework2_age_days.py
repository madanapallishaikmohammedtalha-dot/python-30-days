
# Homework 2 — Age in Days

name=input("name:")
age=int(input("age:"))
days=age*365
hours=days*24
minutes=hours*60

print(f"Name:              {name}")
print(f"Age:               {age}")
print(f"{name} has lived:  {days:,} days")
print(f"{name} has lived:  {hours:,} hours")
print(f"{name} has lived:  {minutes:,} minutes")