#! write_f() will rewrite entire .csv file
def write_f(data_list):  # TODO: Figure out a use for this
    with open('contacts.csv', 'w') as f:
        for row in data_list:
            for item in row:
                f.writelines(f'{ item },')
            f.writelines('\n')
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


def del_contacts(data, name):
    for i in range(len(data)):
        if name == data[i].get('name'):
            data.remove(data[i])
            return data
    return print(f'{ name.capitalize() } not found in contacts')


def main():
    # REPL loop for user_input and application navigation and control

    csv_list, contact_list = init_contacts()
    while True:
        user_input = input('User Enter: read, add, remove, or quit: ')
        if user_input == 'quit':
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
            del_contacts(contact_list, name)
        else:
            print('input not recognized... \n')

    write_f(csv_list)

    return


if __name__ == '__main__':
    main()
