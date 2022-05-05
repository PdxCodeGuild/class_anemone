import re

def keys(put):
    i = 0
    keys = []
    while i == 0:
        keys.extend(put[i].split(','))
        i += 1
    return keys 

def values(puts):
    i = len(puts) - 1
    vlist = []
    while i > 0:
        vlist.extend([puts[i].split(',')])  
        i -= 1 
    return vlist

def new(put, puts):
    cld = {}
    i = 0
    y = 1
    while i != len(put):
        cld.update({put[i]: puts[i][y]})
        i += 1
        y += 1
    return cld


with open('contacts.csv', 'r') as file:
    clist = file.read().split('\n')
    print(clist)
    print(new(keys(clist), values(clist)))

    
    
    
    
    # print(clsit)    ['name,favorite fruit,favorite color', 'charles,none,red', 'jona,nothing,black']
    # print(keys(clist))   ['name', 'favorite fruit', 'favorite color'] 
    # print(values(clist)) [['jona', 'nothing', 'black'], ['charles', 'none', 'red']]
    # print(new(keys(clist, values(clist))))   {'name': ['jona', 'nothing', 'black'], 'favorite fruit': ['jona', 'nothing', 'black'], 'favorite color': ['jona', 'nothing', 'black']}
    
    
    
    
    
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