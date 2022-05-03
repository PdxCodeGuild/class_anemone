# ....Lab 07 Version 1

# Version 1 using dictionary because dictionaries make sense to me..
def rot13_dictionary():
    alph_rot = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 
    'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', ' ': ' ' }
    user_input = input("Type your messsage to be encrypted: ")
    list(user_input)
    for letter in user_input:
        print(alph_rot[letter], end= '')

# Version 2 using two strings that made me experience imposter syndrome, but it works...
def rot13_strings():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    alphabet_rot = "nopqrstuvwxyzabcdefghijklm "
    user_input = input("Type message to encrypt: ")
    output = ''
    for letter in user_input:
        index = alphabet.find(letter)
        output += alphabet_rot[index]
    print(output)


def rot13():
    first_encrypt = input('Do you want to encrypt some text? y/n \n')
    if first_encrypt == "y":
        rot13_dictionary()
    elif first_encrypt == 'n':
        break
    second_encrypt = input('\nWant to encrypt some more text? y/n \n')
    if second_encrypt == "y":
        rot13_strings()
    else: print('That was fun, see ya later!')

rot13()