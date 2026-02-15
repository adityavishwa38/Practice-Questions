Tuples=(1,2,3,4,5,6,7,8)
print("Display element of tuple:",Tuples)
value=int(input("Write element to search :"))
count=0

for num in Tuples:
    if num==value:
        count+=1

if count==1:
    print("Element found")
else:
    print("Element not found")