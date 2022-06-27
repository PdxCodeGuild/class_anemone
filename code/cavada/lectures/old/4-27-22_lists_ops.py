"""list ops"""
# access list elements using index number
# if you use index not in list, you get an error

# fruits = ['apples', 'bananas', 'pears', 'cherries']

# print(fruits[3])
# print(fruits[len(fruits)]) # error out of range of indicdes
# print(fruits[2:len(fruits)]) # list items from the '2' index (3rd item) until end

"""comparisons with lists"""
# use == and != with list to check equivelency, not 'sameness'
# fruits.append('pineapple')
# print(fruits)
# fruits.insert(1, 'grape')
# print(fruits)
# fruits.remove('pineapple')
# print(fruits)
# eaten = fruits.pop(1)
# print(fruits, eaten)

"""copy list to another list"""
# fruits1 = ['apples', 'bananas', 'pears']
# fruits2 = ['cherries', 'pineapples']

# fruits1.extend(fruits2) 
# print(fruits1)

"""copy method to copy list"""
# fruits1 = ['apples', 'bananas', 'pears']
# fruits2 = fruits1.copy()

# print(fruits1)
# # fruits2.append('pineapples')
# print(fruits2)
# print(fruits1 in fruits2)

"""lists slicing"""
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list)
# print(list[2::])
# print(list[:2:])
# print(list[::-1])
# print(list[2:4:])

"""list sorting"""

# name = ['j','o','n','a','t','h','o','n']
# print(name)
# # name.sort()
# # print(name)
# # list_r = reversed(list) # creates a 'lightweight' list
# # print(list_r)

# list_r = list(reversed(name))
# print(list_r)

# print(sorted.list_r) 

"""tuples: immutable lists"""
# not covered

"""loops"""
# i = 0
# while i <= 5:
#     print(i)
#     i += 1
# print('done') 

# name = ['j','o','n','a','t','h','o','n']

"""range """

# for i in range(10):
#     print(i, end= ' ')
# print("\n")

# for i in range(4, 10):
#     print(i, end= ' ')
# print("\n")
# for i in range(4, 10, 2): # third parameter tells it to do every other 2
#     print(i, end=' ')

fruits = ['apples', 'bananas', 'pears']

# for fruit in fruits:
#     fruit = 'grapes'

# for i, fruit in range(len(fruits)):
#     fruit[i] += "!!!"
#     print(fruit)

# print(fruits)

# for i, fruit in enumerate(fruits):
#     fruit += "!!!"
#     print(fruit)

"""while loops"""

# nums = []
# while True:
#     num = input('enter number: ')
#     if num == 'done':
#         break
#     nums.append(int(num))
# print(nums)


# selected_option = ''
# invalid_option = True
# while invalid_option: 
#     selected_option = input("a or b? ")
#     if selected_option == 'a' or selected_option == 'b':
#         invalid = False  
#     else:
#         print("please choose a or b")

# int - range
# char - string
# element - list
# element - tuple 
# key - dict

"""random module"""

# import random
# print(random.choice(['apples', 'bananas', 'pears']))
# print(random.choice('abc'))

