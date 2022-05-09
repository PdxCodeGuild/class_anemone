import string

translate = False

while not translate:
    alphabets = string.ascii_lowercase + string.ascii_lowercase
    conversion = input("Do you want to encrypt your list 'yes' or 'no':\n").lower()
    if conversion == 'yes':
        user_input = list(input("enter your text: \n").lower())
        shift_number = int(input("enter your shift number from 1 to 25: \n"))
        for i in range(len(user_input)):
            if user_input[i] == ' ':
                user_input[i] = ' '
            else:
                new_letter = alphabets.index(user_input[i]) + shift_number
                user_input[i] = alphabets[new_letter]
        print(''.join(map(str, user_input)))
        translate = True
    elif conversion == 'no':
        print("Ending program. ")
        break
