

from ast import Return
import random

#newset function
def newset():
     ticket = []
     for i in range(6):
         Temp = random.randint(1,99)
         ticket.append(Temp)
     return ticket


def counter():
     player_cash_counter = 0
     counter_total = player_cash_counter +(-2) 
     return counter_total

#Comparison function
def comparison(winning_set, player_set):
     matches = 0
     for i in range(len(winning_set)):
          if winning_set[i] == player_set[i]:
               matches += 1 
     
     return matches


temp_set = []

winning_set = []

player_set = []

player_cash = [10000]

total_matches = [] 

earnings = 0

expenses = 0 

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
     



print(f'The winning numbers are as follows: {winning_set}')
print(f'Your numbers are as follows:        {player_set}')

temp_set.clear() 
newset()




#Logic to track total number of matches
if comparison(winning_set, player_set) >=1:
     total_matches.append(comparison(winning_set, player_set))

comparison(winning_set, player_set)

print (comparison(winning_set, player_set))

#For logic to run program as often as is necessary 
for i in range(100000):
     
     newset()
     player_set.clear()
     player_set.extend(newset())
     print(f' Your new numbers are {player_set}')
     nummatch = comparison(winning_set, player_set)
     if nummatch == 1:
          earnings += 4 
     elif nummatch == 2: 
          earnings += 7
     elif nummatch == 3:
          earnings += 100
     elif nummatch == 4:
          earnings += 50000
     elif nummatch == 5:
          earnings += 1000000
     elif nummatch == 6:
          earnings += 25000000
     expenses -= 2 
     print(comparison(winning_set, player_set))
     counter()
     player_cash.append(counter())
     running_total = sum(player_cash)
     
     
     if comparison(winning_set, player_set) >=1:
          total_matches.append(comparison(winning_set, player_set))


print(expenses)
print(earnings)
matches_sum = sum(total_matches)
print(running_total)
print(matches_sum)
print(total_matches)