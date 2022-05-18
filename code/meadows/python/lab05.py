import random
import string
import math

def loto_num():
    loto_num = []
    for nums in range(6):
        apples = random.randint(1,99) #creating a random number and append that to loto_num until range 6 is met
        loto_num.append(apples)    #giving us a list of 6 random int
        random.shuffle(loto_num)  #shuffling the int to make it more unknown
    return loto_num

def lottery(winning, ticket):     # used the lab over view from friday to fix my intial .append[0] crisis that wasn't working 
    matchs = 0                  # creating a varible to save the amount of matchs made through out the loops
    for i in range(len(winning)):   # using range(len) to check each spot in the list
        if winning[i] == ticket[i]: # from there using x[i] == x[i] to check if anyspots match and saving how many to matchs 
            matchs += 1  
    return matchs

winner = loto_num() # creating a list of lotto_num() to use latter as a comparison to see if the winner is a winner or loser

m = 0 # for money made during ticket checks ( also is the winnings )
money = 0  # current money to ref how much we lose from buying 100k 2$ tickets
tickets = 0   #keeping track of tickets to create the while loop below so it will always loop until 0 becomes <= 100000

while tickets <= 100000: 

    player = loto_num() # second variable from lotto_num() to use for the def lottery() later
    money -= 2 # subtract 2 from money every loop
    tickets += 1   # add 1 ticket every loop so while knows when tickets is <=100000     
    matchs = lottery(winner, player) #used to create a varible to check how many matches a ticket has and then add the m += amount to m

    if matchs == 6:    # starting with 6 to ensure it doesn't stop if a lower number hits first OR uses multiple and adds it to the M ( had this issue in first version )
        m += 25000000

    elif matchs == 5:
        m += 1000000   # m += is for if the tickets hits then it will always add that amount to m for what ever loop it got hit on

    elif matchs == 4:
        m += 50000 

    elif matchs == 3:
        m += 100

    elif matchs == 2:
        m += 7

    elif matchs == 1:
        m += 4


   # m = winnings.. removed the variable because it was a waste of a line and didn't want to go back and change all the m to winning... Ahh jeez rick                           
roi = (m - money)/money # giving the % of return on investment
print(f'\nYour Return on investment is {round(roi, 2)} %') # using round to get rid of needles decimal points
print(f'\n YOU bought $200,000 worth of ticket AND won a TOTAL of ${m}\n')


def loto_num(num):
    loto_num = []
    for nums in range(6):
        apples = random.randint(1,99) # changes the value of number that are randomly given IE: can pick up to 99 but if i change 1,99 [1,88,43,12,99] to 1,14[1,5,12,9,14] ( helps to test if winnings work ) it gives my numbers a range of 1-14 to be pick. 
        loto_num.append(apples) 
        random.shuffle(loto_num)  #just shuffles the random numbers picked that where placed in list loto_num
    return loto_num

pick6 = loto_num(1)    # created a variable out of the def to use for other function to have a random number set of 6 numbers
player = loto_num(2)    # second variable for 2 seperate lists

def check(tickets):          # function to see if the value in the list is in the value of other list IE: [0,1,2,3,4,5] 
    cat = []
    for i in range(1):
        if player[0] == pick6[0]:
            cat.append(player[0])          #it will keep checking to see if the values are in the list then append it to itself
        if player[1] == pick6[1]:
            cat.append(player[1])
        if player[2] == pick6[2]:
            cat.append(player[2])
        if player[3] == pick6[3]:
            cat.append(player[3])
        if player[4] == pick6[4]:
            cat.append(player[4])
        if player[5] == pick6[5]:
            cat.append(player[5])
        return cat

winning = []
money = 0
tickets = 0
while tickets < 100000:        #while ticket counts less then 100k it will loop and ADD 1 ( tickets = tickets + 1 ) as shown at end of while loop 
    for i in player:
        random.shuffle(pick6)    #making sure both don't end up being same sets over and over for more of a gamble
        random.shuffle(player)
        if len(check(player)) == 1:    
            m = 4
            money = money +m                   
        if len(check(player)) == 2:
            m =7             # if the length of check() is 2 then they won 7 dollars and so on
            money = money +m                        
        if len(check(player)) == 3:
            m=50000
            money = money +m             
        elif len(check(player)) == 4:
            m=275000
            money = money +m               
        elif len(check(player)) == 5:
            m=1000000
            money = money +m              
        elif len(check(player)) == 6:
            m=25000000
            money = money +m  
    tickets = tickets + 1
    
winnings = money
tick_cost = 2                                   # the END for the viewer to see what they won 
roi = (winnings - tick_cost)/200000
print(f'\nYour Return on investment is {round(roi, 2)} %')
print(f'\n YOU bought $200,000 worth of ticket AND won a TOTAL of ${winnings-200000}\n')  # not sure why we are buying 200K tickets with 1 in 99 chance of ..1.. number matching up not counting the other 6.. TERRIBLE investment