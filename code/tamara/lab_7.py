def ROT13(user_string): # define ROT13 function

    number_values = { # create a number values dictionary
        1 : 'a', 
        2: 'b', 
        3: 'c', 
        4: 'd', 
        5: 'e', 
        6: 'f', 
        7: 'g', 
        8: 'h', 
        9 :'i', 
        10: 'j', 
        11: 'k', 
        12: 'l', 
        13: 'm', 
        14: 'n', 
        15: 'o', 
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z',
        }

    alphabet = { # create an alphabet dictionary
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,
        'j' : 10,
        'k' : 11,
        'l' : 12,
        'm' : 13,
        'n' : 14,
        'o' : 15,
        'p' : 16,
        'q' : 17,
        'r' : 18,
        's' : 19,
        't' : 20,
        'u' : 21,
        'v' : 22,
        'w' : 23,
        'x' : 24,
        'y' : 25,
        'z' : 26
        }

    # create a list that uses the letters input by the user and converts them to lowercase and then uses them as keys for the number values
    user_list_number_values = [alphabet[letter.lower()] for letter in user_string] 

    # define an empty string
    encryption = ''

    # rotate through the list of numbers and add 13 to them or subtract 13 to get the key that is 13 away
    # then convert to a string and add it to the empty encryption string
    for number in user_list_number_values:
        if number > 14:
            number += 13
            encryption = encryption + number_values[number]
        else:
            number -= 13
            encryption = encryption + number_values[number]
    
    return encryption

# test out the function
user_string = input("Enter a word or letters to have them returned to you as an encryption: ")

print(f'Your encryption is {ROT13(user_string)}')
