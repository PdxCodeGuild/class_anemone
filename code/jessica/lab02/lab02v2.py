
nums = []

while True: #infinite loop (requiring break to end the loop)
    numbers = int(input("Enter a number or 0 to quit: "))
    nums.append(numbers)
    print(nums) 
    print(len(nums))
    

    if numbers == 0:
        for num in nums:
            avg = sum(nums) / len(nums)
        break # end the loop
    
    

print(f'\nYou entered {nums}')
print(f'\nThe average of the numbers is {avg}')


