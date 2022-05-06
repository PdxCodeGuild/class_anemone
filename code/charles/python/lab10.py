from itertools import zip_longest
import re 
name = ['name', 'n']
ff =['favorite food', 'favorite fruit', 'favorite snack', 'food']
fc =['favorite color', 'favorite dye', 'favorite shade', 'color']
commands = ['list', 'new', 'update', 'search', 'delete']                        # list of strings for laters
yes = ['y', 'yes', 'yes', 'ye', 'ya']
no = ['n', 'no', 'na', 'nada', 'nope']

def read():                                                                     # loads and breaks down csv file
    with open('contacts.csv') as f:
        info = f.read().split('\n')                                             
    contacts = []
    keys = info[0].split(',')                                                   # takes inputs from 0th line and creates a list of keys 
    for i in range(1, len(info)):
        pinfo = info[i].split(',')                                              # creates two list with contact info
        contacts.append(dict(zip(keys, pinfo)))                                 # combines key and info into tuples to be put into a dict
    return contacts, keys                                                       # returns contacts listdict and keys
contacts, keys = read()                                                         # opens the contacts and keys to be edited globally... but not the actual global just like everything access global

def search():
    search = input('Who are you looking for? ').lower()                         # takes input from user and process through each contact til match
    for i, contact in enumerate(contacts):                                      # and returns the list[int] dict to user
        if contact['name'] == search:
            return contacts[i]
        else:
           return 'Contact not in list'


def delete():
    remove = input('What contact would you like to get rid of? ').lower()       # same as search just with the del function
    for i, contact in enumerate(contacts):
        if contact['name'] == remove:
            del contacts[i]
            return contacts
        else:
            return print('Person not in list or spelling incorrect.')


def update():
    replace = input('What contact would you like to change? ').lower()                          # same as search/del at first
    for i, contact in enumerate(contacts):                                                      # repleaces information based of user input and would 
        if contact['name'] == replace:                                                          # have to be accessed again for additional
            name                                                                                # while loop would fix
            key = input(f'What would you like to change about {replace}\n{keys}: ').lower()
            if key in name:
                val = input('What will be the new name? ').lower()
                contacts[i]['name'] = val
                return contacts
            elif key in ff:
                val = input('What will be the new favorite fruit? ').lower()
                contacts[i]['favorite fruit'] = val
                return contacts
            elif key in fc:
                val = input('What will be the new favorite color? ').lower()
                contacts[i]['favorite color'] = val
                return contacts
            return contacts 
        else:
            return 'Contact not in list'
    return contacts, 
         


def create():                                                                                   # creates new contact to be appended to the list
    contact = {}    
    for key in keys:
        value = input(f'{key}: ').title()                                                       # rotates through each key to be printed and input for
        contact[key] = value                                                                    # each value entered
    return contact




def save(contacts, keys):                                                           # inports updated contacts and keys to be saved into new file
    nf = [','.join(keys)]                                                           # joins the keys back to the base of name,favorite,favorite
    for contact in contacts:                                                        
        contact = contact.values()                                                  # process through each contact dict to join values like keys
        contact = [','.join(contact)]   
        # contact = ['\n'.join(contact)]
        nf.extend(contact)                                                          # adds each listed contact to the nf variable to be save
    nf = '\n'.join(nf)
    
    with open('contacts2.csv', 'w') as file:                                        # saves the information onto new file opening to be written on with
            file.write(nf)                                                          # 'w' and .wwrite
    return

def sys():
    phone_book = True
    while phone_book:
        print('Welcome to your Off-brand phone book.')
        direct = input(f"{', '.join(commands)}"'\n What is it that you would like to do? ').lower()
        
        if direct in commands:
            if direct == 'list':                                                    # if/elifs to run through each command based on user input
                direct = None
                print(contacts)
            elif direct == 'new':
                direct = None
                contact = create()
                contacts.append(contact)
            elif direct == 'update':
                direct == None
                contact = update()
                if contact == 'Contact not in list':
                    print(contact)  
                    print(contacts)
                    pass
                contacts.append(contact)
            elif direct == 'search':
                direct == None
                print(search())
            elif direct == 'delete':
                direct == None
                delete()
                print(contacts)
     
        redo = input('Is there more you would like to do? Y/N: ').lower()                   # user can loop to modify the file to liking
        if redo in yes:
            phone_book= True
        elif redo in no:
            phone_book = False
            print('Goodbye')
    save(contacts, keys)  


# print(ucontacts)        
        
sys()        





# def keys(put):
#     i = 0
#     keys = []
#     while i == 0:
#         keys.extend(put[i].split(','))
#         i += 1
#     return keys 

# def values(puts):
#     i = len(puts) - 1
#     vlist = []
#     while i > 0:
#         vlist.extend(puts[i].split(','))  
#         i -= 1 
#     return vlist

# def new(put, puts):
#     cld ={}
#     # i = puts[-1]
#     # while i in puts:
#     x = 0
#     for key in put:
#         cld.update({key: None})
#         if x < len(puts):
#             cld.update({key : x})
            
            # if i in puts:
            #     cld.update({key : '' + value})
                
                
                

#     return cld

    
#     # cld = []
#     # i = 0
#     # x = 0
#     # while i != len(puts):
#     #     while i != len(puts):
#     #         cld.extend({put[i]: puts[x]})
#     #         x+=1
#     #     i += 1
        
#     return cld


# with open('contacts.csv', 'r') as file:
#     clist = file.read().split('\n')
    
#     print(new(keys(clist), values(clist)))

    
    
    
    
    # print(clist)    #['name,favorite fruit,favorite color', 'charles,none,red', 'jona,nothing,black']
    # print(keys(clist))   #['name', 'favorite fruit', 'favorite color'] 
    # print(values(clist)) #[['jona', 'nothing', 'black'], ['charles', 'none', 'red']]
    # print(new(keys(clist, values(clist))))   {'name': ['jona', 'nothing', 'black'], 'favorite fruit': ['jona', 'nothing', 'black'], 'favorite color': ['jona', 'nothing', 'black']}
    
# def new(put, puts):
#     cld = {}
#     m = 0
#     while m < len(puts):
#         for x in enumerate(put):   {(0, 'name'): (5, 'red'), (1, 'favorite fruit'): (5, 'red'), (2, 'favorite color'): (5, 'red')}
#             n = x
#             print(x)
#             for y in enumerate(puts):
#                 s = y 
#                 print(y)
#                 cld.update({x : y})
#                 m+=1
    
#     return cld


# def new(put, puts):
#     cld = []
#     y = 0
#     i = len(puts) - 1
#     for x in enumerate(puts):           #[{'jona': 'red'}, {'jona': 'none'}, {'jona': 'charles'}, {'jona': 'black'}, {'jona': 'nothing'}]                     
#         clist2 = puts[i].split(',')                               
#         i -= 1                                               
#     while y == 0:                                              
#         cld.append({put[y]:puts[i]})
#         y-=1
    
#     return cld



    # cld = {}
    # i = 0
    # x = 0
    # while i != len(puts):                         # cld.update({put[i]: puts[x]})
    #     while i != len(puts):                     # TypeError: unhashable type: 'list'
    #         cld.update({put[i]: puts[x]})
    #         x+=1
    #     i += 1                                           
    
    
    
    
    # cld = []
    # y = len(clist) - 1
    # i = len(clist) - 1
    # for x in enumerate(clist):                                # [{'favorite color': 'jona,nothing,black'}, {'favorite color': 'charles,none,red'}]
    # clist2 = clist[i].split(',')                              # 
    #      i -= 1                                               # ['name', 'favorite fruit', 'favorite color'] 
    # while y > 0:                                              # 'name', 'favorite fruit', 'favorite color'
    #    cld.append({clist2[i] : clist[y]})
    #       y-=1
    # print(f'{cld}\n{clist}\n{clist2}')
        
    
    # i = len(clist) - 1
    # for i in clist:
    #     clist2 = clist[i].split(',')
    #     i -= 1
    #     while enumerate(clist):                                   # clist2 = clist[i].split(',')
    #         cdict = {}                                            # TypeError: list indices must be integers or slices, not str
    #         p = len(clist) -1
    #         while p > 0:
    #             cdict.update[clist2(0): clist(p)]
    # print(cdict)
    
    # i = len(clist) - 1
    # while i > 0:
    #     myList = [item[i].split(",") for item in clist]           # [['n'], ['c'], ['j']]
    #     i -= 1
    # print(myList)
    
    
    
    # i = len(clist) - 1
    # for x in enumerate(clist):
    #     clist2 = clist[i].split(',')                              # 'name', 'favorite fruit', 'favorite color'
    #     i -= 1
    # print(clist, clist2)
    
    
    
    # cdict = {}
    # i = len(clist) -1
    # while i > 0:
    #     cdict.update(clist[0][clist[i]])
    #     i -= 1
    # print(cdict)
    # bline = {}
    # for line in file:
    #     bline.update((line.split(',')(line.split(','))))
    # print(bline)
      
    
    # contact_list = {}
    # contact_list.update(line[0].split())
    # i = len(line) - 1
    # while i > -1:
    #     nc= line[i].split(',')
    #     print(nc)
    #     contact_list.update(nc)
    # print(contact_list)


    # lines = file.read().split('\n')
    # for i in lines:
    #     lines = lines[i].split()
    # print(lines)