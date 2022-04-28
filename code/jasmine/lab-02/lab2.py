import random


# ##Version 1
# new_num = 0
# nums = [5,0,8,3,4,1,6]
# for i in range(len(nums)):
#     print(nums[i])

#     new_num += random.choice(nums)
# #print(new_num)
   
# print(new_num/len(nums))


##Version 2 

#empty list to collect input
nums = []
user_num = ''

#While loop to create numbers list
while user_num != 'done':

    user_num = input('Enter a number or done : ')
    
    if user_num != 'done':
        nums.append(user_num)
    
#print(nums)

for x in range(len(nums)):
    nums[x] = int(nums[x])

#Show the sum of nums in list

#print(sum(nums))

#print average
print(f'Average: {sum(nums) / len(nums)}')



