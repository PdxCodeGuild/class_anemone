"""tuples: homogenous"""
list_of_tuples = [
    ('merritt', 'instructor', '503-123-4567'),
    ('liz', 'ta', '503-765-4321'),
    ('bruce', 'former student', '503-321-4567')
]
# print(list_of_tuples)
"""tuples: heterogenous"""

# fruits = {'apples', 'bananas', 'cherries', 'durian'}


# print
# for i in fruits:
#     print(i)

# for x in enumerate(fruits):f
#     print(x)

# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# for fruit in fruits:
#     fruit = fruit.upper
#     print(fruit)
fruits = {'apples', 'bananas', 'cherries', 'durian'}

# print(fruits)

"""list comprehensions (slick option)"""

# upper_fruits = [fruit.upper() for fruit in fruits]

# print(upper_fruits)

"""James Johnson is new TA"""

"""filter in list comprehensions"""

people = ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
# print(people)
bobs_only = [person for person in people if person.startswith('Bob')]
# print(bobs_only)
people = ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
bobs_only = [person*3 for person in people if person.startswith('Bob')]
# print(bobs_only)
people = ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
bobs_only = [person*2 if 'J' in person else person for person in people if person.startswith('Bob')]
# print(bobs_only)
"""error handling"""

"""indentation: number of spaces doesn't matter, but default is 4 spaces"""
# no indent where it should be in case of looping or otherwise
"""name error"""
# phantom variable, using variable that hasn't been declared yet
"""type error"""
# trying to use a type that doesnt work with a certain operation like doing math with strings, and concatonating ints

"""attribute error"""
# name error of misuing types

# x = 1
# y = 2
# z = str(x) + str(y)
# print(z, int(z)+y)

"""index error"""
# if you try to access index 
# that is not within the range
"""key error"""
# if you try to access a key that does not 
# exist within the dictionary you are referencing
"""value error"""
# if issue with concersion between 
# elements like string to base 10 integer


"""break1040-1050"""
"""raising exceptions"""
# def crash(i):
#     if i < 0:
#         raise ValueError('i cannot be less than 0')
#     print("continuing on...")
# print(crash(-1))

# try:
#     this_wont_work = 1 + 'hello'
#     this_wont_run()
# except TypeError:
#     print('That didn\'t work!')

"""easier to ask for forgiveness than permission"""

"""userproofing"""

# while True:
#     try:
#         num = int(input("enter a number: "))
#         break
#     except ValueError:
#         print("...that's not a valid number, plz enter a valid number...")
# print(num)


while True:
    try:
        num = int(input("enter a number: "))
        break
    except ValueError as e:
        print("...that's not a valid number, plz enter a valid number...",e)
# print(num)

"""best to use integers and not floats 
because of the rounding issues that arise"""

