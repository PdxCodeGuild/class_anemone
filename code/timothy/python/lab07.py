# ....Lab 07 Version 1

# def rot13(message):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     alphabet_rot = 'nopqrstuvwxyzabcdefghijklm'
#     for letter in range(alphabet[i]):
#         i = alphabet.find(letter)


def rot13():
    alph_rot = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 
    'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', ' ': ' ' }
    user_input = input("Type your messsage to be encrypted: ")
    list(user_input)
    for letter in user_input:
        print(alph_rot[letter], end= '')

rot13()