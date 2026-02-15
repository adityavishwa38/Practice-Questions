list_1=[1,2,3,4,5]
list_2=[2,3,7,8,9]
print("First list:",list_1)
print("Second list:",list_2)
common=[]

for num in list_1:
    if num in list_2:
        common.append(num)

print("Common element in this array :",common)