nums = [5, 0, 8, 3, 4, 1, 6]

sums = 0

for i in range(len(nums)):
    sums += nums[i]
    print(sums)
    
print(f'Your average is: {round(sums / len(nums), 4)}')