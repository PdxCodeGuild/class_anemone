nums = []
maxlengthlist = 16
while len(nums) < maxlengthlist:
    num = input('Enter each digit of your credit card, pressing enter after each number: ')
    nums.append(int(num))

    
nums.pop(15)

nums.reverse()


print(nums)

double = (nums[::2]) * 2 

for x in nums:
    if x > 9:
        x -= 9


print(nums)
final = sum(nums)

print(final)