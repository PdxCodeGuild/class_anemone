

from string import ascii_lowercase


index1 = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
        'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26} 

index2 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m',
        14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'} 


phrase = list(input('Enter a phase to convert: ').lower())
def encrypt(oscar):
    cypher13 = ''
    for i in range(len(oscar)):
        if oscar[i] == ' ':
            cypher13 += ' '
        else:
            num = index1[oscar[i]] + 13
            let = index2[num % 26]
            cypher13 += let
    return cypher13

def decrypt(oscar):
    cypher13 = ''
    for i in range(len(oscar)):
        if oscar[i] == ' ':
            cypher13 += ' '
        
        else:
            num = index1[oscar[i]] - 13
            if num < 1:
                num = num + 26
            let = index2[num]
            cypher13 += let
    return cypher13

print(decrypt(phrase))



# index = list(ascii_lowercase)
# print(index)
# phrase = list(input('Enter a phase to convert: ')).lower()
# print(phrase)

# out = []
# output = ''.join(out)

# while True:
#     for i in range(len(phrase)):
#         ni = phrase.pop(0)
#         if ni in ascii_lowercase:
#             out[i] = []
    
#         if ascii_lowercase in phrase:
#             out[i] = [i + 13]
#         elif i + 13 > 25:
#             out[i] = i + 13 - 25}
