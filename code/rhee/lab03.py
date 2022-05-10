number = input("Type any number to convert: ")

singles = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
         'nineteen']
doubles = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']

hundreds = ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 'five hundred ', 'six hundred ',
            'seven hundred ', 'eight hundred ', 'nine hundred ']

word = ''
length = len(number)
change = length
increase = 0
while change > 0:
    if word == '0':
        print('zero')
        break
    if change > 1 and number[change - 2] == '1':
        for i in range(10):
            if number[change - 1] == str(i):
                word = teens[i] + word
    else:
        for i in range(10):
            if number[change - 1] == str(i):
                word = singles[i] + word
    if change > 1:
        for i in range(10):
            if number[change - 2] == str(i):
                word = doubles[i] + word
    if change > 1:
        for i in range(10):
            if number[change - 3] == str(i):
                word = hundreds[i] + word

    change = change - 3
    increase += 1
print(word)
