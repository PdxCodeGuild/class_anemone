"""lab 2 v1 & v2"""

nums = [] # setting this list to gather user input numbers

user = '' # setting this up to serve as an interm
counter = 0
input("press any key to find the average of a set of numbers...") # gathering user input for summing and eventually finding avg of numbers
while True: # setting up while loop to continuously collect user input until they prompt termination of collection
    user = 0.0 # might be overkill, did this to make sure user was a float
    if user == 'done': # honestly not sure if this is neceessary, but intended to prevent counting str 'done' later 
        nums.pop() 
        break
    user = (input("add a number, or type 'done' to get the average: ")) # this is actual prompt to collect data
    if user != 'done': 
        user = float(user)
        nums.append(user)
        counter += 1 # not sure if this is efficient but using this to get count of numbers input by user
        # print(nums) 
        if user == 'done':
            nums.pop()
            break
    # print(nums)
    if user == 'done':
        break
print(nums)
def avg(total, n): # made this function just to get into the habit of using functions
    return total / n
sum = 0 # used this variable and subsequent 'for loop' to sum the values in list num
for num in nums:
    sum += num
n = counter
print(f"sum: {sum}; avg: {(avg(sum,n))}")    







    
