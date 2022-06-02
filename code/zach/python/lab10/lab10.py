#! write_f() will rewrite entire .csv file
def write_f(data_list):  # TODO: Figure out a use for this
    f_out = []
    for row in data_list:
        f_out.append(list(row))
    f_out = [','.join(item) for item in f_out]
    f_out = '\n'.join(f_out)
    with open('contacts.csv', 'w') as f:
        f.write(f_out)
        f.close()
    return


def init_contacts():
    with open('contacts.csv', 'r') as f:
        data_csv = f.read()
        csv_list = [line.split(',') for line in data_csv.split('\n')]
        keys = csv_list[0]
        contacts = [dict(zip(keys, values)) for values in csv_list[1::]]
        f.close()
    return csv_list, contacts


def add_contacts(data, name, fav_fruit, fav_color):
    new_contact = {'name': name, 'favorite fruit': fav_fruit,
                   'favorite color': fav_color}
    data.append(new_contact)
    return data


def del_contacts(data, csv_data, name):
    for i in range(len(data)):
        if name == data[i].get('name'):
            csv_data.remove(csv_data[i+1])
            data.remove(data[i])
            return data, csv_data
    return print(f'{ name.capitalize() } not found in contacts')

def update_contacts(data,csv_data,name):
    for i in range(len(data)):
        if name == data[i].get('name'):
            csv_data.pop(i+1)
            data[i]['favorite fruit'] = input(f"Enter { name }'s favorite fruit: ")
            data[i]['favorite color'] = input(f"Enter { name }'s favorite color: ")
            csv_data.append([data[i]['name'], data[i]['favorite fruit'], data[i]['favorite color']])
            name =""
    return data, csv_data
            
    


def main():
    # REPL loop for user_input and application navigation and control

    csv_list, contact_list = init_contacts()
    while True:
        user_input = input('User Enter: read, add, edit, remove, or quit: ')
        if user_input == 'quit':
            write_f(csv_list)
            break
        elif user_input == 'read':
            name = str(input('enter contact name: '))
            for i in range(len(contact_list)):
                if name == contact_list[i].get('name'):
                    print('\nName: ', contact_list[i].get('name').capitalize())
                    print('Favorite Fruit: ',
                          contact_list[i].get('favorite fruit'))
                    print('Favorite Color: ',
                          contact_list[i].get('favorite color'))
                    print('______________________________________________')
        elif user_input == 'add':
            print('Enter info of contact to add.')
            name = input('Name: ')
            fruit = input('Favorite Fruit: ')
            color = input('Favorite Color: ')
            add_contacts(contact_list, name, fruit, color)
            csv_list.append([name, fruit, color])
        elif user_input == 'remove':
            name = input('Enter name of contact you wish to remove\nName: ')
            del_contacts(contact_list, csv_list, name)
        elif user_input == 'edit':
            print('Enter Name of Contact you wish to edit.')
            name = input('Name:').lower().strip()
            update_contacts(contact_list,csv_list, name)
        else:
            print('input not recognized... \n')

    

    return


if __name__ == '__main__':
    main()
