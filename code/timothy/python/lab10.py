import re

with open('C:/users/johns/desktop/contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

contacts = dict()

header = lines[0]
header = re.split(',', header)


print(header)

# SUPERCALICOMPLICATED way to do it:
# dict_one = dict()
# dict_two = dict()

# header = lines[0]
# header = re.split(',', header)
# key1 = header.pop(0)
# key2 = header.pop(0)
# key3 = header.pop(0)
# contact_one = lines[1]
# contact_one = re.split(',', contact_one)
# value1 = contact_one.pop(0)
# value2 = contact_one.pop(0)
# value3 = contact_one.pop(0)

# dict_one[key1] = value1
# dict_one[key2] = value2
# dict_one[key3] = value3
# print(dict_one)
# contacts[1] = dict_one
# print(contacts)