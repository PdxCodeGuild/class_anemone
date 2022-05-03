jacklist = [0, 0]




def grow(age):                                              # Fucnction for testing age# Kill Switch function
    i = 0                                                  # Jackodict key 1
    for i in range(0, len(age)):
        age[i] += 1
    return age

def told_test(age):
    i = len(age) - 1                                                # Jackodict key 1
    while i > -1:
        if age[i] == 10:
            del age[i]
        i -= 1
    return age

def repop(age):
    for i in range(0, len(age)):
        if age[i] in range(4, 9):
            jacklist.append(0)
    return 




year = 0
while len(jacklist) < 1000:
    
    grow(jacklist)
    told_test(jacklist)
    repop(jacklist)
    print(year, len(jacklist))
    year += 1
print(year, len(jacklist))



































# jackodict = { 1: 0, 2: 0}                                   # dictonary to track the jackolopes


# def grow(age):                                              # Fucnction for testing age# Kill Switch function
#     i = 1                                                   # Jackodict key 1
#     for i in age:
#         if i in age and age[i] in range(0, 11):
#             age[i] += 1
#     return age

# def told_test(age):
#     i = min(age.keys())                                                   # Jackodict key 1
#     print(age.keys())
#     while i <= max(age.keys()):
#         if age[i] == 10:
#             del age[i]
#         i += 1
#     return age

# def repop(age):
#     i = min(age.keys())                                                 # Jackodict key 1
#     mates = 0
#     ospring = 0
#     if i in age and age[i] in range(4, 9):
#         mates += len(age) // 2
#         ospring += mates * 2
#     return ospring


# def name(age, news):
#     babies = {}
#     maxk = max(age.keys())
#     i = 1
#     for i in range(0, news + 1):
#             nextk = maxk + 1 + i
#             babies[nextk] = 0
#             i += 1
        
#     return babies

# # print(told_test(jackodict))

# year = 0
# while len(jackodict) < 1000:
    
#     grow(jackodict)
#     told_test(jackodict)
#     name(jackodict, repop(jackodict))
#     print(year, len(jackodict))
#     year += 1
# print(year, len(jackodict))
    

# Function for reproducing

# 

# While sum(len(list(jackodict))) < 1000:
#       pop = 