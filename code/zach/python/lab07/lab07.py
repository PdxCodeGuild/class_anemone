def encryption(string, function, rotation_num):
    english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    orig_list = list(string)
    rot_string = []
    if function[0] == 'e':
        for char in orig_list:
            if char in english:
                if english.index(char) <= 13:
                    rot_string.append(english[english.index(char)+rotation_num])
                else:
                    rot_string.append(english[english.index(char)-rotation_num])
    else:
        for char in orig_list:
            if char in english:
                if english.index(char) >= 13:
                    rot_string.append(english[english.index(char)-rotation_num])
                else:
                    rot_string.append(english[english.index(char)+rotation_num])
        
    print('Output: ',str(rot_string))





def main():
    user_input = str(input('input desired encryption: ')).lower().strip()
    function_input = str(input('encrypt/decrypt: ')).lower().strip()
    rotation_input = int(input('number of rotations: '))
    encryption(user_input, function_input, rotation_input)
main()