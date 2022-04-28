' Version 1 '

# nums = [5, 0, 8, 3, 4, 1, 6]
# sum = 0
# for num in nums:
#     sum = sum + num
# average = sum / len(nums)
# print(average)

' Version 2 '

nums = []
sum = 0
while True:
    num = input("Enter a number or 'done': ")
    if num == 'done':
        break
    nums.append(int(num))
for num in nums:
    sum = sum + num
average = sum/len(nums)
print(f"Your average is: {average}")