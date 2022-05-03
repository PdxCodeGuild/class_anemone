nums = []
maxlengthlist = 16
while len(nums) < maxlengthlist:
    num = input('Enter each digit of your credit card, pressing enter after each number: ')
    nums.append(int(num))

check_number = nums.pop(15)  

   
nums.reverse()


print(nums)

for i in range(0,len(nums),2):
    nums[i] *= 2 

print(nums)

for i in range(len(nums)):
    if nums[i] > 9:
        nums[i] -= 9

    

print(nums)

final = sum(nums)




print(final)
print(check_number)