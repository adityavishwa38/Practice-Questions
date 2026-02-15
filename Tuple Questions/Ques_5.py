nums=(1,3,4,5,6,7,8,9,11,22,33,34,21)
print("Given tuple element is :",nums)
count_even=0
count_odd=0

for num in nums:
    if(num%2==0):
        count_even+=1
    else:
        count_odd+=1


print("Numbers of even :",count_even)            
print("Numbers of odd :",count_odd)            