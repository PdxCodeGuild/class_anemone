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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for i in range(5):
    #     
    #     break
        






