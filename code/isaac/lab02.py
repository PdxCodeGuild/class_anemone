'''Average Numbers'''

nums = [5, 0, 8, 3, 4, 1, 6]

# elements
for num in nums:
    sum_nums = sum(nums)
    print(sum_nums, end=' ')

# indicies
for i in range(len(nums)):
    sum_nums = sum(nums) / len(nums)
    print(round(sum_nums), end=' ')

# ------------------------------------------------- #

# VERSION 2

nums = []

user_input = input("Enter a number or type 'done' to quit: ")
user_input = int(user_input)

while len(nums) < 10:
    if user_input == 'done':
        len(nums) / sum(nums)
        break
    else:
        print(user_input)
        nums.append(user_input)
        print(nums)