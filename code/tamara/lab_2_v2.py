# define empty list to store user number input 
nums = []
# define varible to store running sum of user number inputs
running_sum = 0 

# create while loop to get user number inputs and add them up in running_sum    
while True:
    user_number = input("Enter a number or type 'done' for all entered number total sum: ")
    # if user enters 'done' give them the average of all their entered numbers
    if user_number == 'done':
        print(f'The average of those numbers is {running_sum/len(nums)}')
        break
    # if user enters a number add it to the nums list and to the running sum
    else: nums.append(int(user_number))
    running_sum = running_sum + int(user_number)