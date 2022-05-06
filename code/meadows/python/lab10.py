import math
#-------------------------------------------------VERSION 2 ---------------------------------------------------------------#
contact = []
graveyard = []
yes = ['yes','y','yeah','si']
no = ['no', 'nah','nay','nope','n']
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
    more = input('\nadd more contacts? ( yes or no ): \n').lower()
    if more in yes:
        play = True
    if more in no:
        print('generating contact list...')
        break
for x in no:
    enter = input('\nEnter Name for contact "INFO" or no to stop: ').lower()
    if enter in no:
            break
    for person in contact:
        if person['name'] == enter:
            print(f'\n{person}')
for x in no:
    enter = input('\nEnter Name for contact "UPDATE" or NO to stop: ')
    if enter in no:
        break
    update = input('''\nwhat do you want to update? 
            NAME , STATE , NUMBER ?: \n''').lower()
    for person in contact:
        if person['name'] == enter:
            print(f'\n{person}')
            if 'number' in update:
                n = input('enter new number: ')
                person['number'] = n
                print(f'\n{person}')
                break
            if 'state' in update:
                s = input('enter new state: ')
                person['state'] = s
                print(f'\n{person}')
                break
            if 'name' in update:
                nm = input('update name: ')
                person['name'] = nm
                print(f'\n{person}')
                break
for x in no: 
    enter_2 = input('\nDELETE a contact?: (yes, or no): ')
    if enter_2 in no:
        break
    del_enter = input('\nEnter contact to destroy: ')
    for person in contact:
        if person['name'] == del_enter:
            del person['name']
            del person['state']
            del person['number']
            print('\nPOOF.. gone')
            break

print(contact)
# for x in range(len(contact)):
#     enter = input('Enter Name for contact Info or no to stop: ').lower()
#     for person in contact:
#         if person['name'] == enter:
#             print(person)
#         if enter in no:
#             break