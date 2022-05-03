# dictonary to track the jackolopes
jackodict = { 1: 0, 2: 0}


def grow(age):                                              # Fucnction for testing age
    i = 1                                                   # Jackodict key 1
    for i in age:
        if i in age and age[i] in range(0, 11):
            age[i] += 1
    return age

def told_test(age):
    told= {}
    i = 1                                                   # Jackodict key 1
    for i in age:
        if age[i] >= 10:
            told.update(age)
    return told

def repop(age):
    i = 1                                                   # Jackodict key 1
    mates = 0
    ospring = 0
    if i in age and age[i] in range(4, 9):
        mates += len(age) // 2
        ospring += mates * 2
    return ospring







print(repop(jackodict))



year = 0
while len(jackodict) < 1000:
    year += 1
    i = len(jackodict) 
    i = i * i 
    print(i)
    if i not in jackodict and len(jackodict) < 1000:
        
        ospring = repop(jackodict)
        while i <= ospring:           
#                       
    

# Function for reproducing
# Kill Switch function
# 

# While sum(len(list(jackodict))) < 1000:
#       pop = 