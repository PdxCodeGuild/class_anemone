
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



"""so you can see that I wrote a lot of code 
to realize I could accomplish the same in much 
less using lis comprehensions at line 112 and 114"""

# i am setting up a while loop to go through a user 
# input string to convert to a numerical code that 
# will be converted to a ROT encryption of that original 
# letter that will be then converted into a new letter 
# replacing the original essentially creating the actual
# encryption desired, user has option to choose ROT encryption
# and the ability to choose a different word. User also has 
# option to view the key for a given ROT encrpytion
user = ''
while user != 'done':
    ticker = 0
    hightower = []
    user = input("\nenter 'word' to ROT encrypt/decrypt, 'done' to quit: ")
    x = 0
    while ticker < 100 and not x == 'back' and user != 'done' and -25 < x < 25: # set this because I had him an issue looping through a diminshing list
        x = (input("enter ROT encryption, 'back' to input other word, or quit: "))
        if x == 'done':
            break
        user_str = list(user) # convert user input into list
        x = int(x)
        ticker += 1
        conv =0
        shell = []
        # print(x)
        shell = []
        shell = [alpha[u] for u in user_str] # list comprehension used to create a new list that represents the encoded words original code that will eventually be converted to ROT13 or otherwise
        # print(type(shell),shell)
        conv = [(a_list2[num+x]) for num in shell] # list comprehension used to create list of letters the step-wise encrpyption based on desired encryption (ROT13, ROT4, etc.)
        print(f"code: ({''.join(conv)}) encryption:({x}) key: ({26-x})") # this tells the user the code, it's encryption, and the key to decrypt it
        


