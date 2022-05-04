import random



def pick6():    # generates 6 random numbers to put out as a list
    dpick6 = []
    while len(dpick6) < 6:
        add = random.choice(range(1, 100))
        dpick6.append(add)
    return dpick6


def winnings(counter):  # takes the input of the matching number to give winnings
    if counter == 0:
        winnings = 0
    elif counter == 1:
        winnings = 4
    elif counter == 2:
        winnings = 7
    elif counter == 3:
        winnings = 100
    elif counter == 4:
        winnings = 50000
    elif counter == 5:
        winnings = 1000000
    elif counter == 6:
        winnings = 25000000
    return winnings

def compare(list1, list2):  # compares two inputted list and modifys counter if list are equal.
    counter = 0
    i = 0
    while i < 6:                # small fix 5 to 6 to compare full list
        u = list1[i] - list2[i]
        if u == 0:
            counter += 1
            i +=1
        elif u != 0:
            i += 1
            
    return counter

def lotto():       # plays the lottery 100,000 times... 100,000,000 basicaly bricks the program cause of run time... down by a 10th per digit
    invest = 0 
    winning = 0
    i = 0
    
    while i < 100000:
        i += 1
        winning += winnings(compare(pick6(), pick6()))
        invest += -2
    
    ROI = (winning + invest) / invest #ROI after the while to allow it to run the amount of times before calculating (also add a negative to subtract... duh)
    
    return winning, invest, ROI    
    

print(lotto()) # average loss is roughly -180000


# print(compare(f, k))