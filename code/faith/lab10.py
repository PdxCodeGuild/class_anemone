with open('code/faith/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

   
list= []
for line in lines:
    list.append(line.split(','))

key = list[0]

contact = [dict(zip(key,values))for values in list[1::]]

for values in list[1::]:
    contact.append(dict(zip(key, values)))


def new_contacts(data, key):
    new_contacts = {}
    for x in key:
        new_contacts[key] = input(f'What is the new contacts {x}?')
        data.append(new_contacts) 

def check_contact(data, key):
    name = input('Whats the new name?: ')
    for contact in data:
        if contact['name'] == name:
            for key in contact:
                print(f'{key}: {contact[key]}')
            return contact


    key_string = "\n" + "\n".join(key) + "\n"
    key_input = input(f"What would you like to search by? Choose from: {key_string} ")
    contact_input = input("What is your search term? ")



    data_results = []
    for contact in values:
        if contact[key_input] == contact_input:
            data_results.append(contact)
            print(data_results)
    return data_results


def update_contact(data,keys):
    result = check_contact(data, keys)
    
    key_update = input(f"What key would you like to update? {keys} ")
    value_update = input(f"What do you want to change {key_update} to? ")
    result[key_update] = value_update
    print(result[key_update])


def delete_contact(data, keys):
    result = check_contact(data,keys)
    check = input(f"do you want to delete {result['name']}")
    if check == 'yes':
        data.remove(result)

data_results = check_contact(values, key)

while True:
    # print(contacts)
    user_input = input("What would you like to do? (c)reate, (r)ead, (u)pdate, (d)elete, (q)uit ")
    if user_input.lower() in ['q', 'quit', 'exit', 'stop']:
        break
    elif user_input == 'c':
        new_contacts(values, key)
    elif user_input == 'r':
        check_contact(values, key)
    elif user_input == 'u':
        update_contact(values, key)
    elif user_input == 'd':
        delete_contact(values, key)


    value_csv = []
    value_csv.append(key)
    for value in values:
        value_csv.append(list(value.values()))

    value_csv = "\n".join([",".join(row) for row in value_csv])

    with open('contacts.csv' , 'w') as w:
        w.write(value_csv)

