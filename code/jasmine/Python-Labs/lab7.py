

#ROT 13 Cipher

# dict index of alphabets

dict_1 = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q':16,
'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

dict_2 = {0: 'N', 1: 'O', 2: 'P', 3: 'Q', 4: 'R', 5: 'S', 6: 'T', 7: 'U', 8: 'V', 9: 'W', 10: 'X', 11: 'Y', 12:'Z', 13: 'A', 14: 'B', 15: 'C', 16: 'D', 
17: 'E', 18: 'F', 19: 'G', 20: 'H', 21: 'I', 22: 'J', 23: 'K', 24: 'L', 25: 'M' }


user_input = input("Enter a string to encrypt: ")

#function to encrypt the string 

def encrypt(user_input):
    cipher = ''
    
