#! write_f() will rewrite entire .csv file
def write_f():  # TODO: Figure out a use for this
    with open('contacts.csv', 'w') as f:
        results = []
        for contact in contact_info:
            for cat, info in zip(contact_org, contact):
                print(cat, ':', info)
                # * 'name':'matthew','favorite fruit':'blackberries','favorite_color':'purple',....
                f.writelines(f'\'{ cat }\':\'{ info }\',')
            f.writelines('\n')
        f.close()
    return


def init_contacts():
    with open('contacts.csv', 'r') as f:
        data_csv = f.read()
        data_csv = [line.split(',') for line in data_csv.split('\n')]
        keys = data_csv[0]
        contacts = [dict(zip(keys, values)) for values in data_csv[1::]]
        f.close()
    return contacts


def add_contacts():
    return


def del_contacts():
    return


def main():
    # REPL loop for user_input and application navigation and control

    contact_list = init_contacts()
    print(type(contact_list[0]))
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
            add_contacts()
        elif user_input == 'remove':
            del_contacts()
        else:
            print('input not recognized... \n')
    return


if __name__ == '__main__':
    main()
