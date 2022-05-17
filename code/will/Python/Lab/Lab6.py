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

    



final = sum(nums)
comparison = final %10
print (comparison)

if comparison == check_number:
    print("You have a valid card!")
elif comparison != check_number:
    print("You have entered a bad card number")