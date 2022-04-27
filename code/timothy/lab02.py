# # ....Lab 02 Version 1.0 (INCOMPLETE, NEED TO USE FOR LOOP)
# nums = [5, 0, 8, 3, 4, 1, 6]
# print(f"My numbers are {nums}")
# total = sum(nums)
# print(f"The sum of my numbers is {total}.")
# elements = len(nums)
# print(f"I have {elements} numbers in my list.")
# average = total / elements
# print(f"The average of my numbers is {average}")

# ....Lab 02 Version 1.2 (COMPLETE)
# nums = [5, 0, 8, 3, 4, 1, 6]
# print(f"My numbers are {nums}")
# total = 0
# for num in nums:
#     total += num
# print(f"The sum of my numbers is {total}.")
# elements = len(nums)
# print(f"I have {elements} numbers in my list.")
# average = total / elements
# print(f"The average of my numbers is {average}")




# ....Lab 02 Version 2 (COMPLETE)
nums = []
while True:
    num = input("Enter a number, or done: ")
    if num == "done":
        break
    nums.append(int(num))
print(f"Your numbers are {nums}")
total = 0
for num in nums:
    total += num
print(f"The sum of your numbers is {total}.")
elements = len(nums)
print(f"You have {elements} numbers in your list.")
average = total / elements
print(f"The average of your numbers is {average}")