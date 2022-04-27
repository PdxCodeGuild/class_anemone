#Version 1
#Start with list, iterate through it, keep 'running sum', divide sum by number of elements in list

nums = [5, 0, 8, 3, 4, 1, 6]

total = 0

for num in nums:
    total = total + num

average = total / len(nums)

print (average)


#Version 2
#Let the user input the numbers one at a time

nums = []

while True:
    num = input('Enter a number. or "done": ')
    if num == 'done':
        break
    nums.append(int(num))

total = 0

for num in nums:
    total = total + num

average = total / len(nums)

print (average)
