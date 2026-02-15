numbers=[2,3,-1,4,-2,5,6]
print("Given list is :",numbers)
positive_num=[]
nagative_num=[]

for i in numbers:
    if i<0:
        nagative_num.append(i)
    else:
        positive_num.append(i)

print("Positive number is :",positive_num)
print("Nagative number is :",nagative_num)
