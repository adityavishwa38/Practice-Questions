nums=int(input("How many numbers :"))
print("\n")
numbers=[]
sum=0

for i in range(nums):
    value=int(input("Write here input :"))
    numbers.append(value)

print("Total element in list :",numbers)

for i in range(nums):
    sum=sum+numbers[i]

print("Sum of numbers in given list :",sum)  

