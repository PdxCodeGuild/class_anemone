"""lab 2 v1 & v2"""

nums = [] # setting this for this variable to work in my loop

user = ''
counter = 0
input("press any key to find the average of a set of numbers...")
while True:
    user = 0.0
    if user == 'done':
        nums.pop()
        break
    user = (input("add a number, or type 'done' to get the average: "))
    if user != 'done':
        user = float(user)
        nums.append(user)
        counter += 1
        # print(nums)
        if user == 'done':
            nums.pop()
            break
    # print(nums)
    if user == 'done':
        break
print(nums)
def avg(total, n):
    return total / n
sum = 0
for num in nums:
    sum += num
n = counter
print(f"sum: {sum}; avg: {(avg(sum,n))}")    
# print(avg(sum, n))






    
