number=[2,4,7,4,2,9,6]
print("The given list is :",number)

largest_num=number[0]
second_largest=number[0]

for num in number:
    if num > largest_num:
        second_largest=largest_num
        largest_num=num
    elif num > second_largest and num !=largest_num:
        second_largest=num

print("The seccond largest element is :",second_largest)