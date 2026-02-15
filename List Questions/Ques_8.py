numbers=[2,3,1,4,2,5,1,6,6]
print("Given list is :",numbers)

unique_list=[]

for i in numbers:
    if i not in unique_list:    
        unique_list.append(i)

print("Removed dublicate values :",unique_list)
