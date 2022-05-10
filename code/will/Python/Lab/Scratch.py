
phonebook = {'David': '5551234', 'Alice': '6662345'}
with open('phonebook.txt', 'w') as phone_book_file:
    for name, number in phonebook.items():
        line = f'{name} {number}\n'
        phone_book_file.write(line)

names = []
for item in list_of_list:
    names.append(item[0].split(","))
print(names)

colors = []
for item in list_of_list:
    colors.append(item[1].split(","))
print(colors)

state = []
for item in list_of_list:
    state.append(item[2].split(","))
print(state)

names_length = len(names)

for i in range(1, names_length) :
    test = zip(names[0], names[i])
        
print(list(test))
    
