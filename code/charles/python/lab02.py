# nums = [5, 0, 8, 3, 4, 1, 6]

# sums = 0

# for i in range(len(nums)):
#     sums += nums[i]
#     print(sums)
    
# print(f'Your average is: {round(sums / len(nums), 4)}')

nums = []

sums = 0

enter = True

while enter:
    add = input('Please enter a number or type done for you average: ')
    if add == 'done':
        enter == False
        break
    else:
        nums.append(int(add))

for i in range(len(nums)):
    sums += nums[i]

print(f'Your average is: {round(sums / len(nums), 3)}')