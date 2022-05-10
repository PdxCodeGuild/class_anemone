rot13_dict = {
    'a':'n', 'b':'o', 'c':'p',
    'd':'q', 'e':'r', 'f':'s',
    'g':'t', 'h':'u', 'i':'v',
    'j':'w', 'k':'x', 'l':'y',
    'm':'z', 'n':'a', 'o':'b',
    'p':'c', 'q':'d', 'r':'e',
    's':'f', 't':'g', 'u':'h',
    'v':'i', 'w':'j', 'x':'k',
    'y':'l', 'z':'m', ' ':' '
}

data = input("Please enter a word or phrase you would like to be encoded: ")

for char in data:
    print(rot13_dict[char], end = '')

print('')