#Average Numbers Lab

nums = []

while True:
    num = input('enter number: ')
    if num == 'done':
        break
    nums.append(int(num))


print(nums)

sum = sum(nums)

final = sum / len(nums)

print(final)
