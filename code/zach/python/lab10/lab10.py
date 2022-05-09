#! write_f() will rewrite entire .csv file 
def write_f():#TODO: Figure out a use for this
    with open('contacts.csv', 'w') as f:
        results = []
        for contact in contact_info:
            for cat, info in zip(contact_org, contact):
                print(cat,':', info)
                #* 'name':'matthew','favorite fruit':'blackberries','favorite_color':'purple',....
                f.writelines(f'\'{ cat }\':\'{ info }\',')
            f.writelines('\n')
        f.close()
    return


def read_contacts():
    with open('contacts.csv', 'r') as f:
        data_csv = f.read()
        data_csv = [line.split(',') for line in data_csv.split('\n')]
        keys = data_csv[0]
        contacts = [dict(zip(keys, values)) for values in data_csv[1::]]
        f.close()
        print(contacts)
    return contacts

def add_contacts():
    return
def main():
    # REPL loop for user_input and application navigation and control
    while True:
        user_input = input('User Enter: read, add, remove, or quit: ')
        if user_input == 'quit':
            break
        elif user_input == 'read':
            read_contacts()
    return


if __name__ == '__main__':
    main()
