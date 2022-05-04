# define the list nums with the numbers
nums = [5, 0, 8, 3, 4, 1, 6]
# define running sum variable and start it at 0
running_sum = 0

# create for loop to add all of the number to running sum
for num in nums:
    running_sum = running_sum + num
    #determine the average of all the numbers
    average = running_sum/len(nums)
# print the average outside the for loop to get just the average of all of the numbers together
print(average)