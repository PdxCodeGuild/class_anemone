# Lab07.py ROT Cipher
# Fran Kappes


# Define ROT cipher function
def rot_cipher(letter, rotation):

    # Define alphabet list
    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    # Determine ROTn character
    rot_index = 0
    rot_index += 13 if alphabet_list.index(letter) < 14 else alphabet_list.index(letter)-13
    
    # if alphabet_list.index(letter) < 14:
    #     rot_index += 13
    # else:
    #     rot_index -=13
    
    rot_char = alphabet_list[rot_index]

    print(f"letter: {letter}")      ### TEST
    char_index = alphabet_list.index(letter)    ### TEST
    print(f"char_index: {char_index}")  ### TEST
    print(f"rot_index: {rot_index}")    ### TEST
    print(f"rot_char: {rot_char}")      ### TEST
    return rot_char

# Prompt user for a string
user_string = input("Enter a string: ")

# Define rotation factor
rotation = 13


# Break string up into a list of individual characters
user_char_list = []
i = 0

user_char_list = [user_string[i] for user_string in user_string]

print(f"user_char_list: {user_char_list}")   ### TEST


# Loop through the user character list and call ROT Cipher function
encrypted_string = ''

for char in user_char_list:
        encrypted_string += rot_cipher(char,rotation)

# Print encrypted string
print(f"Encrypted string: {encrypted_string}")