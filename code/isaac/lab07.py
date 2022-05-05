'''ROT Cipher'''
# Create a cipher function
# Import string module
import string

# Build a cipher function containing
# two string variables with full alphabet 
def cipher(message):
    alpha = 'abcdefghijklmnopqrstuvwxyz' # built a lowercase alphabet string
    bravo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # build an uppercase alphabet string
    cipher = str.maketrans(alpha + bravo, alpha[13:] + alpha[:13] + bravo[13:] + bravo[:13]) # use str.maketrans method to translate and shift strings
    # return shifted message
    return str.translate(message, cipher)

# Create user input for a message
user_input = input("Enter message: ")

print(cipher(user_input))


'''String variables and print functions for testing purposes'''
# alpha = 'abcdefghijklmnopqrstuvwxyz' # built a lowercase alphabet string
# bravo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # build an uppercase alphabet string
# print(alpha, bravo)
# print(type(alpha), type(bravo))  