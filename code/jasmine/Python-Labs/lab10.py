
# Contact List Lab
# Class Example

import re

with open ('contact.csv', 'r') as f:
    data_csv = f.read()

csv_lines = data_csv.split("\n")
# list_of_lists = []
# for line in csv_lines:
#     list_of_lists.append(line.split(','))
list_of_lists = [line.split(',') for line in data_csv.split('\n')]

keys = list_of_lists[0]
## empty ist
contacts = []
# for row in list_of_lists[1::]:
#     #empty dict for each row
#     row_dict = {}
#     for i in range(len(row)):
        
#         row_dict[keys[i]] = row[i]
        # row_dict['name'] = 'jasmine'
        # row_dict['favorite color'] = 'purple'
        # row_dict['favorite fruit'] = 'mango'
    # print(row_dict)
for values in list_of_lists[1::]:
    contacts.append(dict(zip(keys,values)))
print(contacts)