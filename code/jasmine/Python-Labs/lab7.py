

#ROT 13 Cipher



user_input = input("Enter a message that you would like to encrypt: ")

def encrpyt_message(user_input):
    # dict index of alphabets already translated

    dict_1 = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', }
    #empty string to store characters
    cipher = ''
    for letter in user_input:
        # if upper case letters entered
        letter = letter.lower()
        #avalable keys in dict
        if letter in dict_1.keys():
            cipher += dict_1[letter]
        else: 
            cipher += letter 
    return cipher

#encyrpted message saved to message and printed
message = encrpyt_message(user_input)
print(message) 

print(f'{user_input} is equivalent to {message}')