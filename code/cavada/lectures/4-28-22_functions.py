"""functions"""
# def say_hello(first_name, last_name):
#     print('Hello ' + first_name + ' ' + last_name)

# fn = input('what is your first name? ')
# ln = input('what is your last name? ')
# say_hello(fn, ln)

# def useless_function():
#     pass

# rule of thumb for breaking off things into function
    # dont repeat yourself, instead build function
def p(x):
    print(x)


# a = "what is up"
# b = input("type your name")

# p(f"{a} {b}")    
# print(a, b)

# def input(x):
#     x = input("what is up!")
#     return x

# input(x = input("what is up"))   

"""optional arguments"""
def subtracts(a, b=1):
    return a - b


subtracts(5,8)
subtracts(4)

username = input("type username: ")
def movie_ratings(username, *args, **kwargs):
    """Update the user’s ratings for movies.
    Update movies from *args that are keys in **kwargs.
    """
    print(username)
    for arg in args:  # Loop through the tuple `args`
        if arg in kwargs:  # Loop through keys of the `kwargs` dictionary
            print(arg, kwargs[arg])

"""args and kwargs"""

movies = ['Sharknado', 'Frozen', 'Transformers']
ratings = {
    'Sharknado': 3,
    'Frozen': 2,
    'Transformers': 5
}

movies_args = "', '".join(movies)
mv_args = (f"'{movies_args}'")
# movies_args = 'Sharknado', 'Frozen', 'Transformers'
# p(mv_args)
print(ratings.keys())
print(ratings.values())
ratings = f"{ratings.keys[0]}:{ratings.values[0]}"
movie_ratings(username, *movies_args, Sharknado=3, Frozen=2, Fargo=5)

""" Output is:
Sharknado 3
Frozen 2
"""
"""functions again"""

# def more_nums():
#     x = 30
#     y = 40
#     print(x, y)

# more_nums()    

# return 

"""decorators"""

# @something (functions that 'wrap around' functions)
# import math
"""recursion"""
# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)

# factorial(456)

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# factorial(2)

# a = lambda x,y: x + y
# print(a,(5,4)) # 9

# s = lambda x,y: x-y
# print(s,(5,4)) # 1
    


