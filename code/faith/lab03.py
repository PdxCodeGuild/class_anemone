numbersunder10 = {
    0:'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    7: 'six',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
numbersover20 = {
    2: 'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety'
}

def num_to_phrase(number):
    if number < 20:
     result = numbersunder10[number]
     return result
    elif number <100:
        ones = number % 10
        tens = number // 10
        if ones == 0:
            result = numbersover20[tens]
        else:
            result = numbersover20[tens]+ '-' + numbersunder10[ones]
        return result

