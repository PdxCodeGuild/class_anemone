import math
#-------------------------------------------------VERSION 1 ? ---------------------------------------------------------------#
# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)
#prints ['name,state,number', 'jon,ne,6556556555', 'sav,ne,5665665666', 'tim,ct,7887887888', '']

names = []
states = []
numbers =[]
play = True
while play:
    name = input('Name: ')
    names.append(name)
    state = input('state: ')
    states.append(state)
    number = input(r'enter phone number: ')
    numbers.append(number)
    more = input('add more contacts? ( yes or no ): ')
    yes = ['yes','y','yeah','si']
    no = ['no', 'nah','nay','nope']
    if more in yes:
        play = True
    if more in no:
        print('generating contact list...')
        break
contacts = zip(names,states,numbers)
print(tuple(contacts))