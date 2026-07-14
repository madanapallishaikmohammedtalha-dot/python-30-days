#filter 
numbers=[12 ,7 ,18 ,3 ,25 ,19 ,14]
filtered_even=[]
for number in numbers:
    if number%2==0:
        filtered_even.append(number)
print("original list:",numbers)
print("filtered even list:",filtered_even)