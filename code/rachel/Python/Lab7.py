#Lab7
# Encode string with ROT13

import string


phrase = list(input("Enter a string: "))

abc = list(string.ascii_lowercase)
print (abc)

new_word = ''

for letter in phrase:
    letter_index = abc.index(letter)
    new_index = letter_index + 13
    #print (new_index)
    if new_index > 25:
        new_index -=  26
        print (new_index)
    cipher = abc[new_index]
    new_word += cipher

    
    print (cipher)
print(new_word)