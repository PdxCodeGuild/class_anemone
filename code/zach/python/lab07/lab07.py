def encryption(string, function, rotation_num):
    english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    orig_list = list(string)
    rot_string = []
    for char in orig_list:
        if char in english:
            if english.index(char) <= 12:
                rot_string.append(english[english.index(char)+13])
            else:
                rot_string.append(english[english.index(char)-13])
    
    print(rot_string)





def main():
    user_input = str(input('input desired encryption')).lower().strip()
    function_input = str(input(''))
    rotation_input = str(input())
    encryption(user_input)
main()