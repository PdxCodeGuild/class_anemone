'''
class_anemone
Lab 2
Baiely Baker
'''



################## Version 1 ###########################
# # creating list of numbers

# nums = [5, 0, 8, 3, 4, 1, 6]
# avg = 0

# # using for loop to tally sum and then divide by length for average
# for num in nums:
#     avg += num

# avg = round(avg / len(nums), 4)

# print(avg)
#########################################################

############### Version 2 ##############################

nums = []
avg = 0

# While loop to get user input
while True:
    choice = input("enter a number, or 'done': ")

    if choice == 'done':
        break
    choice = int(choice)
    nums.append(choice)

# for loop to tally sum
for num in nums:
    avg += num

avg = round(avg / len(nums), 4)
# print the average 
print(f"average: {avg}")