
contacts = [
    {'name': 'matthew', 'favorite fruit': 'blackberries', 'favorite color': 'orange'}, {'name': 'matthew', 'favorite fruit': 'blackberries',
                                                                                        'favorite color': 'orange'}, {'name': 'matthew', 'favorite fruit': 'blackberries', 'favorite color': 'orange'}

]
contact_org = ['name', 'favorite fruit', 'favorite_color']
contact_info = [['matthew', 'blackberries', 'purple'], ['jill','bananas', 'purple']]
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

def read_f():
    with open('contacts.csv', 'r') as f:
        results = []
        f.readline() # ignores header row
        for line in f:
            contact = line.split(',\n')
            results.append(contact)
        print(contact[0::-1])
    # answer = {}
    # with open('path/to/file') as infile:
    #     infile.readline()  # we don't care about the header row
    #     for line in infile:
    #         year, gender, name, count = (s.strip('"') for s in line.split(','))
    #         key = (name, gender)
    #         if key not in answer: answer[key] = {}
    #         answer[key][int(year)] = (int(count), None)
    return
def main():
    #         words = line.split(',')
    #         results.append((words[0]), words[1:])
    # return
    write_f()
    #read_f()
    return


if __name__ == '__main__':
    main()
