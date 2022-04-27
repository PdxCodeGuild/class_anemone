# Lab02.py - Averaging Numbers
# Fran Kappes

# Define variables
sum = 0
# Define and populate numbers list
nums = [5, 0, 8, 3, 4, 1, 6]

# Loop through numbers list and sum all the numbers
for num in nums:
	sum += num

 # Calculate the average
average = round((sum/(len(nums))),3)

# Print results
print(f"""
List: {nums}
Average: {average}""")
