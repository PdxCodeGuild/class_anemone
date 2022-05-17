ones = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

teens = {
    0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen',
    5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'
}

tens = {
    2: 'twenty', 3: 'thirty', 4: 'fourty',
    5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
}

hundreds = {
    1: 'one hundred', 2: 'two hundred', 3: 'three hundred',
    4: 'four hundred', 5: 'five hundred', 6: 'six hundred',
    7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'
}

num = int(input("Enter a number 0-999: "))
hundreds_digit = num//100
tens_digit = (num//10)%10
ones_digit = num%10

if tens_digit == 0:
    phrase = ones[ones_digit]
elif tens_digit == 1:
    phrase = teens[ones_digit]
elif ones_digit == 0:
    phrase = tens[tens_digit]
elif tens_digit > 1:
    phrase = tens[tens_digit] + '-' + ones[ones_digit]

if hundreds_digit > 0:
    phrase = hundreds[hundreds_digit] + ' and ' + phrase

if ones_digit == 0 and tens_digit == 0:
        phrase = hundreds[hundreds_digit]

print(phrase)