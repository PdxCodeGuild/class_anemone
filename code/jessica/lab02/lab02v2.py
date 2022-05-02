
nums = []

while True: #infinite loop (requiring break to end the loop)
    numbers = input("Enter a number or done to quit: ")
    
    print(nums) 
    if numbers == 'done':
        for num in nums:
            avg = sum(nums) / len(nums)
        break # end the loop
    nums.append(int(numbers)) ##put at the end of the if statement because if kept throwing a str not a base ten error
    
    

print(f'\nYou entered {nums}')
print(f'\nThe average of the numbers is {avg}')


