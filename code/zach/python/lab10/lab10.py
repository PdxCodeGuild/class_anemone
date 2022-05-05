
contacts = [
    {'name': 'matthew', 'favorite fruit': 'blackberries', 'favorite color': 'orange'},{'name': 'matthew', 'favorite fruit': 'blackberries', 'favorite color': 'orange'},{'name': 'matthew', 'favorite fruit': 'blackberries', 'favorite color': 'orange'}

]


def main():
    # with open('contacts.csv', 'r') as f:
    #     results = []
    #     for line in f:
    #         words = line.split(',')
    #         results.append((words[0]), words[1:])
    # return
    with open('contacts.csv', 'w') as f:
        results = []
        for contact in contacts:
            for element in contact:
                f.writelines(f'{ contact[element] } ,' )
            f.writelines('\n')
        f.close()
    return

if __name__ == '__main__':
    main()
