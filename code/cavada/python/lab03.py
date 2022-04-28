print("\n")
dig_1st_plus = {    #potentially not the best way
    0: "zero",      #to have created my dictionaries       
    1: "one",       #and didn't actually use the 
    2: "two",       #dictionary list I ended up 
    3: "three",     #compiling, but I imagine I might
    4: "four",      #benefited from it
    5: "five", 
    6: "six",
    7: "seven",
    8: "eight", 
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen", 
    18: "eighteen",
    19: "nineteen"
}
dig_2nd_minus = {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy", 
    8: "eighty",
    9: "ninety"
}
x = "hundred"
dig_3rd = {
    1: "one hundred",
    2: "two hundred",
    3: "three hundred",
    4: "four hundred",
    5: "five hundred", 
    6: "six hundred",
    7: "seven hundred", 
    8: "eight hundred", 
    9: "nine hundred"
}

# dig = [] # created dict list in the event I might use it
# dig.append(dig_1st_plus) 
# dig.append(dig_2nd_minus)
# dig.append(dig_3rd)
# # print(dig)

# print('\n')
# print(dig[1].values())
import random # imported random to make testing easier
orig = random.randint(0,999) # use this to text all the numbers I need to be able to convert from digits to phrase
# orig = 70 # would use this line occasionally to target 'difficult' numbers like 204, 70, and 400
print(orig)
orig_a = list(str(orig))
print(orig_a) # used this to split up number to return phrase part based on digit and placement of digit
orig_b = list(str(orig)) # used this later when I had a problem, worked!

number = str(orig) # not entirely sure if I actually needed this
number = list(number)

if 0 < len(orig_a) < 3 and 0 < orig < 20: # used this to capture anything 0-9
        value = dig_1st_plus[orig]
        print(value)
# used next conditional to catch any numbers from 20 - 99
elif 1 < len(number) < 3 and not 10 < orig < 20 and len(number) != 0:
    digit = int(number[0])
    index = number.pop()
    value = dig_1st_plus[digit]
    if int(orig_a[1]) == 0:
        value = int(orig_a[0])
        first = dig_2nd_minus[value]
        print(first)
    elif len(orig_a) == 2 and orig != 0:
        # print("yes")
        first = dig_2nd_minus[digit]
        # print(first)
        orig_a.pop(0)
        if len(orig_a) == 1:
            digit = int(orig_a[0])
            index = number.pop()
            second = dig_1st_plus[digit]
            print(first, second)
        else:
            print("what")
while orig > 99: # used this while loop to get all the 3 digit numbers
    num_c = []
    num_c.extend(orig_b)
    check = num_c.pop(1)
    check += num_c.pop(1)
    if len(number) == 3 and int(number[1]) == 0 and int(number[2]) == 0:
        value = int(number[0])
        first = dig_3rd[value]
        print(first)

    elif len(number) == 3 and int(number[2]) == 0:
        value = int(number[0])
        first = dig_3rd[value]
        value = int(number[1])
        second = dig_2nd_minus[value]
        print(first, second)

    elif len(number) == 3 and int(number[1]) == 0:
        value = int(number[0])
        first = dig_3rd[value]
        value = int(number[2])
        second = dig_1st_plus[value]
        print(first, second)

    elif len(number) == 3 and not 10 < int(check) < 20 and int(number[1]) != 0 and int(number[2]) != 0:
        value = int(number[2])
        third = dig_1st_plus[value]
        # print(third)
        value = int(number[1])
        second = dig_2nd_minus[value]
        value = int(number[0])
        first = dig_3rd[value]
        print(first, second, third)
    elif len(number) == 3 and 10 < int(check) < 20:
        value = int(number[0])
        first = dig_3rd[value]
        second = dig_1st_plus[int(check)]
        print(first, second)
    break


    


