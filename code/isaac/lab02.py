'''Average Numbers'''

# VERSION 1

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

while True:
    num = input("Enter a number or type 'done' to quit: ")
    if num == 'done':
        break
    nums.append(int(num))
print("The average is: ", sum(nums) / len(nums))
