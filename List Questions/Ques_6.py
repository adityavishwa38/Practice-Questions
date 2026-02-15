Numbers=[2,3,4,5,6,7,7,8,89,9,12,32,32,12,11]
print("Given list is :",Numbers)

num=len(Numbers)
#another method 
#range(start , end , increaemnt/decreament)
# reversed_list=[]
# for i in range(num-1,-1,-1):
#     reversed_list.append(Numbers[i])
# print("Reversed number is ",reversed_list)


for i in range(num // 2):
    temp=Numbers[i]
    Numbers[i]=Numbers[num-i-1]
    Numbers[num-i-1]=temp

print("Reversed list is :",Numbers)