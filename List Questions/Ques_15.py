numbers=[1,2,3,4,5,7,8,9,10,11]
print("Given numbers are :",numbers)

even_list=[]
odd_list=[]

for num in numbers:
    if num % 2==0:
        even_list.append(num)
    else:
        odd_list.append(num)    

print("List of even number is :",even_list)
print("List of odd number is :",odd_list)