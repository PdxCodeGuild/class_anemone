'''Jackalope Simulator'''
# Authors: Rachel, Isaac, Bailey

jackalope = [0,0]

year = 0

while len(jackalope) < 1000:
    for i in range(len(jackalope)-1, -1, -1):
        if jackalope[i] == 10:
            jackalope.pop(i)
    
    for i in range(len(jackalope)):
        if 4 <= jackalope[i] <= 8:
            jackalope.append(0)
            #print ("breedable!")
    for i in range(len(jackalope)):
        jackalope[i] += 1
    
    year += 1


print (f'Years: {year}')

