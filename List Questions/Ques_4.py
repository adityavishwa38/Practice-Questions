nums=int(input("Kitna number chahiye :"))
number=[]

for i in range(nums):
    value=int(input("List me element dale :"))
    number.append(value)

print("List ke sabhi element :",number)

# print("List ka sabse bada element :",max(number))
# print("List ka sabse chota element :",min(number))


# second method for doing this

largest=number[0]
smallest=number[0]
for i in number:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i    

print("List ka sabse bada element :",largest)
print("List ka sabse chota element :",smallest)
