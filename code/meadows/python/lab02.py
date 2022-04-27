import math
import random
import string

nums = [5, 0, 8, 3, 4, 1, 6] # List of numbers needed to avg

for i in range(len(nums)): #using i as the numbers in nums to get the range + length of nums
    sums = (sum(nums)) #using sum to sum the list of nums
    avg = sums / len(nums) # taking the sum and dividing it by the len of nums
    print(f'\nThe numbers {nums} equal {sums} and they average {round(avg, 2)}\n') # saying outcome
    break # i don't want it to do the full list of nums.. just want 1 itteration not 6

    
    


#player = int(input('\nEnter a number: ')
