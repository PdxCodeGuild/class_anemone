"""strings, integers, and floats"""
# ascii 
# my_string = str(chr(104) + chr(101) + chr(108) + chr(108) + chr (111))
# print(my_string)

# num1 = 5
# num2 = "5"

# print (f"{num1} {int(num2)}")

# print(num1, num2)

# status = input("how are you today? ")
# x = float(1000000)

# print(x)
# x = 30

# print(round(x, 4)) # print(".3333")
import math

"""arithmetic ops: floor division, modulus, exponentiation""" 

# x %= 25 # divides 30 by 5 and returns remainder (5)
# print(x) # print("5")
# x //= 2 # divides 5 by 2 and returns nearest integer (2)
# print(x)
# modulus can return a values divisibility by returning result of 0
# you can convert floats to ints and strings to ints, if possible
# x = -5
# print(abs(x)) # 

# print(x ** 2) # print(25)  -5^2
"""ascii (american standard code for information interchange)"""
# 127 characters, but includes extended 'codes'
# UTF-8 
# IANA internet assigned numbers authority code for encoding is UTF-8
"""escape characters"""
# tab /t
# enter /n
# backslash //
# ' within "" /'
# " within '' /"
# use 'r' string to turn off escape characters
# use 'f' string to input variables
# s = "hello"
# s += " space "
# print(f"{s}")
# s *= 4
# print(s)

# print(len(s))
# print(s[0:4])
# print(s[::2])
# print(s[::-1])
"""title case"""
# .lower 
# .upper
"""
.startswith() # returns bool for string
.endswith() # returns bool for string
.replace() # replace values in string
.strip() # strip string of undesirable characters
.split() # s.split(delimiter)
.join()
"""

"""lunch time ~1230-1330"""

"""booleans"""
import random
# true or false
# num = [0,1,2,3,4,5,6,7,9,10]
# x = random.choice(num)

# print(5 <= x >= 10)
# x *= 2
# print(x in num)
# my_list1 = [5, 4, 3, 2, 1]
# my_list2 = [5, 4, 3, 2, 1]

# print(my_list1 in my_list2)
"""conditionals"""
# temp = random.choice(range(50,100))
# print(f"the temperature is {temp} today:")
# if temp < 60:
#     print("whoa it's cold out!")
# elif temp < 70:
#     print("a little chilly today")
# elif temp < 80: 
#     print("t-shirt weather")
# elif temp < 90:
#     print("it's warm out today")
# else:
#     print("whoa, it's hot out!")
y = 2 

y = "positive" if y > 0 else "negatives"

print(y)

