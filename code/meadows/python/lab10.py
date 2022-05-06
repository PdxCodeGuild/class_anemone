import math
#-------------------------------------------------VERSION 1 ---------------------------------------------------------------#
contact = []
play = True
while play:
    contacts = {}
    name = input('Name: ').lower()
    contacts['name'] = name
    state = input('state: ').lower()
    contacts['state'] = state
    number = input(r'enter phone number: ')
    contacts['number'] = number
    contact.append(contacts)
    more = input('add more contacts? ( yes or no ): ').lower()
    yes = ['yes','y','yeah','si']
    no = ['no', 'nah','nay','nope','n']
    if more in yes:
        play = True
    if more in no:
        print('generating contact list...')
        break
print(contact)