
contacts = [
    {'name': 'matthew', 'favorite fruit': 'blackberries', 'favorite color': 'orange'}, {'name': 'matthew', 'favorite fruit': 'blackberries',
                                                                                        'favorite color': 'orange'}, {'name': 'matthew', 'favorite fruit': 'blackberries', 'favorite color': 'orange'}

]
contact_org = ['name', 'favorite fruit', 'favorite_color']
contact_info = [['matthew', 'blackberries', 'purple'], ['jill','bananas', 'purple']]
#! write_f() will rewrite entire .csv file 

def write_f():
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

def main():
    # with open('contacts.csv', 'r') as f:
    #     results = []
    #     for line in f:
    #         words = line.split(',')
    #         results.append((words[0]), words[1:])
    # return
    write_f()
    return


if __name__ == '__main__':
    main()
