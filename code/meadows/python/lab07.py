import math

index = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 
'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'} 

roc_13 = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z',
'n': 'a', 'o': 'b','p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}

#made 2 index for the alphabet.. originally used 1:a so on the change roc_13 to the correct corrisponding spot for +13 
letter = input('\nInput a letter OR word below:\n \n').lower() 
for input in letter:    
    print(f'{roc_13[input]} is rock13 of {index[input]}')  # using the input from letter (input) to = the key of roc_13 and give its value while doing the same with
for input in letter:                                       # index but to show what the original input is ( couldn't get the key alone so I made a new dic )
    print(roc_13[input], end='')  # this is to make rock 13 not loop to go through each letter of what a rock is and make it joined to see what the word is and easier
                                    # decrypt what is if decrypting the word

# couldn't get list comp to work so i went with the other way which in turn worked