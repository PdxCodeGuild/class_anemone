# Lab02.py - Averaging Numbers
# Fran Kappes

# Define variables
sum = 0

# Define list that will store numbers entered by user
nums = []

while True:
    num = input("enter a number or 'done': ")
    if num == 'done':
        break
    nums.append(int(num))

if len(nums) > 0:
    
    # Loop through numbers list and sum all the numbers
    for num in nums:
        sum += num

    # Calculate the average
    average = round((sum/(len(nums))),3)

    # Print results
    print(f"""
    List: {nums}
    Average: {average}
    """)
