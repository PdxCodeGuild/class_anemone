import random
import string
import math

def dealer(total):
    if total in range(0, 18):
        return total
    elif total in range(18, 21):
        return total
    elif total == 21:
        x = print(f'{total}..BLACK JACK!')
        return
    # else:
    #     print(f'{total}.. BUST')
    #     return

def rando(numbers):
    poo = []
    letters = ['a', 'q', 'j', 'k']
    letters[0] = 1
    poo.append(letters[0])
    letters[1] = 10
    poo.append(letters[1])
    letters[2] = 10
    poo.append(letters[2])
    letters[3] = 10
    poo.append(letters[3])
    nums = [2,3,4,5,6,7,8,9,10]
    poo.extend(nums)
    random.shuffle(poo)
    poo = poo*4
    grave_yard = []
    for i in range(3):
        random.randint(0,len(poo)-1)
        #grave_yard = poo.pop(random.randint(0,len(poo)-1))
        grave_yard.append(poo.pop(random.randint(0,len(poo)-1)))
    print(grave_yard)
    return [grave_yard, poo]


results = dealer(rando(1))







# player = int(input('HIT or STAY: ')






