# ....Lab 03 Version 1 (COMPLETE)
# num = int(input("Give me a number: "))
# tens_digit = num//10
# ones_digit = num%10

# num_pairs1 = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
# 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
# 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

# if num >= 0 and num <= 19:
#     print(num_pairs1[num])
# elif num > 19 and num < 100:
#     print(num_pairs1[tens_digit * 10] + ' ' + num_pairs1[ones_digit])

# ....Lab 03 Version 2 (Works for all numbers except for hundred-teens...)
# num = int(input("Give me a number: "))
# hundreds_digit = num//100
# tens_digit = num%100//10
# ones_digit = num%10

# num_pairs1 = {0:' ', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
# 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
# 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'one hundred',
# 200:'two hundred', 300:'three hundred', 400:'four hundred', 500:'five hundred', 600:'six hundred', 700:'seven hundred',
# 800:'eight hundred', 900:'nine hundred'}

# if num >= 0 and num <= 20:
#     print(num_pairs1[num])
# elif num > 20 and num < 100:
#     print(num_pairs1[tens_digit * 10] + ' ' + num_pairs1[ones_digit])
# elif num >= 100 and num <= 999:
#     print(num_pairs1[hundreds_digit * 100] + ' ' + num_pairs1[tens_digit * 10] + ' ' + num_pairs1[ones_digit])

# ....Lab 03 Version 2 (REVISING)

num = int(input("Give me a number: "))
hundreds_digit = num//100
tens_digit = num%100//10
huntens_digit = num%100
ones_digit = num%10
# print(huntens_digit)
# print(ones_digit)


ones = {0:' ', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
tens = {0:' ', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

# print(ones[ones_digit])

if num == 0:
    print('zero')
elif num in range(10):
    print(ones[num])
elif num in range(10, 20):
    print(teens[num])
elif num in range(20, 100):
    print(tens[tens_digit] + ' ' + ones[ones_digit])
elif num in range(100, 1000):
        if tens_digit == 1:
            print(ones[hundreds_digit] + ' hundred ' + teens[huntens_digit])
        else: print(ones[hundreds_digit] + ' ' + 'hundred' + ' ' + tens[tens_digit] + ' ' + ones[ones_digit])

