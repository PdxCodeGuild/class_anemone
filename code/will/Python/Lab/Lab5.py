from ast import Return
import random
temp_set = []

winning_set = []

player_set = []

player_cash = 10000

#Winning number selection
i = 0
while i < 6:
     winning = random.randint(1,99)
     winning_set.append(winning)
     i += 1


#Player Number Selection 
i = 0
while i < 6:
     Temp = random.randint(1,99)
     player_set.append(Temp)
     i += 1
     


def newset():
    i = 0
    while i < 6:
         Temp = random.randint(1,99)
         temp_set.append(Temp)
         i += 1




newset()

print(f'The winning numbers are as follows: {winning_set}')
print(f'Your numbers are as follows: {player_set}')
print(temp_set)
temp_set.clear() 
newset()

print(temp_set)