#function basics
def square(n):
    return(n*n)
print(square(5))

#function with condition
def is_even(n):
    return n%2==0
print(is_even(5))

#if/elif/else
num=int(input("Enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#for loop with range
for i in range(10,51,10):
    print(i,end=" ")

#list operation
colours=["red","green","blue"]
colours.append("yellow")
print(colours[1])
print(len(colours))

#Dictionary lookup
marks={"Talha":85, "Ayaan":92, "Zoya":78}
print(marks["Ayaan"])
marks["Riya"]=88
for name in marks:
    print(name)