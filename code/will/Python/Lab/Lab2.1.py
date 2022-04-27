
nums = []

while True:
    num = input('enter number: ')
    nums.append(num)



    if num == 'done':
        break

sum = sum(nums)
final = sum/len(nums)
print(final)