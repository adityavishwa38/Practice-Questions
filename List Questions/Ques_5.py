numbers=[3,4,5,6,4,6,5,3,9,5,8,3,2,9]
print("list element is ",numbers)

value=int(input("Jise khojna h use likhe :"))
count=0
for num in numbers:
    if num==value:
        count+=1

print("Number comes in :",count,"times")