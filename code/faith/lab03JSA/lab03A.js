number = input('Please enter credit card number: ')

nums = []



while True:
    r_input = (input("Please enter a number -done when completed-  "))
    if r_input == 'done':
        break
    nums.append(int(r_input))
 
for num in nums:
    print(num)
length = len(nums)
total = sum(nums)
answer = total / length
print(answer)


