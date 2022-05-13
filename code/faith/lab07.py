rot13={
'a':'n',
'b':'o',
'c':'p',
'd':'q',
'e':'r',
'f':'s',
'g':'t',
'h':'u',
'i':'v',
'j':'w',
'k':'x',
'l':'y',
'm':'z',
'n':'a',
'o':'b',
'p':'c',
'q':'d',
'r':'e',
's':'f',
't':'g',
'u':'h',
'v':'i',
'w':'j',
'x':'k',
'y':'l',
'z':'m'
}

userstring = input('Please enter a string:  ')
'''print(rot13[userstring])'''

new_word = []
newstring = list(userstring)
print(newstring)

for letter in newstring:
    new_word.append(rot13[letter])


print(''.join(new_word))




