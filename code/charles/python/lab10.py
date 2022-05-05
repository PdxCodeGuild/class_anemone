from itertools import zip_longest
import re 

def read():
    with open('contacts.csv') as f:
        info = f.read().split('\n')
    contacts = []
    keys = info[0].split(',')
    for i in range(1, len(info)):
        pinfo = info[i].split(',')
        contacts.append(dict(zip(keys, pinfo)))


def find(contacts, input):
    for i, contact in enumerate(contacts):
        if contact['name'] == input:
            return contacts[i]
        else:
           return print('Contact not in list')

def create(contacts):
    
    name = input('Enter their name: ').lower()
    ff = input('Enter their favorite fruit: ').lower()
    fc = input('Enter their favorite color: ').lower()
    ninfo = {'name': name, 'favorite fruit': ff, 'favorite color': fc}
    for ninfo in contacts:
        contacts.append(ninfo)

print(create(read()))





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