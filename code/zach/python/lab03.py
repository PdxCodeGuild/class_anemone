def word_convert(numeric):
    digits = len(numeric)
    value = int(numeric)

    ones = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    teens = {
        '0': 'ten',
        '1': 'eleven',
        '2': 'twelve',
        '3': 'thirteen',
        '4': 'fourteen',
        '5': 'fifteen',
        '6': 'sixteen',
        '7': 'seventeen',
        '8': 'eightteen',
        '9': 'nineteen'
    }
    tens = {
        '0': '',
        '1': '',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }
    # using string manipulation to switch the numeric value with its coresponding word
    # 1-9: numeric[0] = ones, 10-99: numeric[0] = tens, 100-999: numeric[0] = hundreds
    if digits == 1:
        phrase = ones.get(numeric, 'Invalid Input')
    elif digits == 2 and value < 20:
        phrase = teens.get(numeric[1])
    elif digits == 2 and value < 100:
        phrase = tens.get(numeric[0]) + ' ' + ones.get(numeric[1])
    elif digits == 3 and numeric[1] == '1':
        phrase = ones.get(numeric[0]) + ' hundred ' + teens.get(numeric[2]) 
    else:
        phrase = ones.get(numeric[0]) + ' hundred ' + tens.get(numeric[1]) + ' ' + ones.get(numeric[2])

    return print(f'=> { phrase } ')

# ToDo: Add functionality to convert to roman numerals
def roman_convert(numeric):
    return print('roman_convert success')


def main():

    run = 'y'
    while run == 'y':
        user_number = input(str('Welcome, enter number to convert to phrase: '))
        word_convert(user_number)
        run = input('\nTo continue enter "y" =>')

    return 

main()



