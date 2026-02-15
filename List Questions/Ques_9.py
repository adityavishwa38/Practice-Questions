Numbers=[2,3,4,5,6,7,7,8,89,9,12,32,32,12,11]
print("Given list is :",Numbers)
is_sorted=True

for i in range(len(Numbers)-1):
    if Numbers[i]>Numbers[i+1]:
        is_sorted=False
        break

if is_sorted:
    print("Given list is sorted")
else:
    print("Given list is not sorted")