
# print(user)
# convert = [u+1 for u in user]
# convert = [for u ]

# user = list(user[13::])
# print(user)
# 
a_list2 = ['a','b','c','d','e','f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
}
# conv =0
# shell = []
# phrase = input("Code Phrase: ".strip())
# print(phrase.strip(" "))

# shell = []
# shell = [alpha[u] for u in user_str]
# conv = [alpha[u] for u in user_str] 
# print(shell, conv)
# shell.extend([alpha[u]-13 for u in user_str if alpha[u] > 12])
# conv = [alpha[s] for s in shell]
# print(type(shell),shell)
# for number in shell:
#     if 

# conv = [(a_list2[num+x]) for num in shell]
# conv = [a_list[s] for s in shell]
# print(conv)
# print(''.join(conv))
# conv = [a_list[s] for s in shell]
# encrypt = [a_list[s] for s in conv]
# print("".join(conv))
# for letter in user_str:
#     value = 0
#     conv = 0
#     value = alpha[(letter)]
#     # print(value)

#     if value <= 12:
#         conv += 13 + value
#         # print(f"encrypted index(a-m): {conv}")
#     elif 13 <= value <= 26: 
#         conv += value - 13
#         # print(f"encrypted index(n-z): {conv}")
#     # shell=[]
#     shell.append(str(conv))

#     # print(shell)
# print(shell)    
# encrypt = []
# for letter in shell:
#     e = (a_list[int(letter)])
#     encrypt.append(e)
#     # print(''.join(encrypt))
# key = (''.join(encrypt))
# print(f"""
# original: {user} 
#      key: {key} """)
import random
ticker = 0
hightower = []
user = input("enter word to ROT13 encrypt/decrypt: ")

while ticker < 100:
    x = int(input("enter ROT number"))
    user_str = list(user)
    ticker += 1
    conv =0
    shell = []
    # print(x)
    shell = []
    shell = [alpha[u] for u in user_str]
    # print(type(shell),shell)
    conv = [(a_list2[num+x]) for num in shell]
    print(''.join(conv),x,ticker)
    code = ''.join(conv)
    code += f'{x}'
    if code not in hightower:
        hightower.append(code)
        # print(hightower)

print(hightower)

"""
kbdl 1 1
enter ROT number2
lcem 2 2
enter ROT number3
mdfn 3 3
enter ROT number4
nego 4 4
enter ROT number5
ofhp 5 5
enter ROT number6
pgiq 6 6
enter ROT number7
qhjr 7 7
enter ROT number8
riks 8 8
enter ROT number9
sjlt 9 9
enter ROT number10
tkmu 10 10
enter ROT number11
ulnv 11 11
enter ROT number12
vmow 12 12
enter ROT number13
wnpx 13 13
enter ROT number14
xoqy 14 14
enter ROT number15
yprz 15 15
enter ROT number16
zqsa 16 16
enter ROT number17
artb 17 17
enter ROT number18
bsuc 18 18
enter ROT number19
ctvd 19 19
enter ROT number20
duwe 20 20
enter ROT number21
evxf 21 21
enter ROT number22
fwyg 22 22
enter ROT number23
gxzh 23 23
enter ROT number24
hyai 24 24
enter ROT number25
izbj 25 25
enter ROT number26
jack 26 26
enter ROT number-1
izbj -1 27
enter ROT number-2
hyai -2 28
enter ROT number-3
gxzh -3 29
enter ROT number-4
fwyg -4 30
enter ROT number-5
evxf -5 31
enter ROT number-6
duwe -6 32
enter ROT number-7
ctvd -7 33
enter ROT number-8
bsuc -8 34
enter ROT number-9
artb -9 35
enter ROT number-10
zqsa -10 36
enter ROT number-11
yprz -11 37
enter ROT number-12
xoqy -12 38
enter ROT number-13
wnpx -13 39
enter ROT number-14
vmow -14 40
enter ROT number-15
ulnv -15 41
enter ROT number-16
tkmu -16 42
enter ROT number-17
sjlt -17 43
enter ROT number-18
riks -18 44
enter ROT number-19
qhjr -19 45
enter ROT number-20
pgiq -20 46
enter ROT number-21
ofhp -21 47
enter ROT number-22
nego -22 48
enter ROT number-23
mdfn -23 49
enter ROT number-24
lcem -24 50
enter ROT number-25
kbdl -25 51
enter ROT number-26
jack -26 52
"""