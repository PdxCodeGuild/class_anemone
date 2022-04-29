import random
import string
import math

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
        if len(check(player)) == 2:             # if the length of check() is 2 then they won 7 dollars and so on
            money = money +m                        
        if len(check(player)) == 3:
            m=50000
            money = money +m             
        elif len(check(player)) == 4:
            m=100000
            money = money +m               
        elif len(check(player)) == 5:
            m=1000000
            money = money +m              
        elif len(check(player)) == 6:
            m=2500000
            money = money +m  
    tickets = tickets + 1
    
winnings = money
tick_cost = 2                                   # the END for the viewer to see what they won 
roi = (winnings - tick_cost)/200000
print(f'\nYour Return on investment is {round(roi, 2)} %')
print(f'\n YOU bought $200,000 worth of ticket AND won a TOTAL of ${winnings-200000}\n')  # not sure why we are buying 200K tickets with 1 in 99 chance of ..1.. number matching up not counting the other 6.. TERRIBLE investment
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for i in range(5):
    #     
    #     break
        






