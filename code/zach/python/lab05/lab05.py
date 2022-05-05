import random

def pick6():
    numbers = []
    for i in range(0,6):
        numbers.append(random.randint(1,99))
    
    return numbers

def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

def play_lotto():
    prizes = {
        1 : 4,
        2 : 7,
        3 : 100,
        4 : 50000,
        5 : 1000000,
        6 : 25000000,
        0 : 0
    }
    winning = pick6()
    ticket = pick6()

    winning_numbers = num_matches(winning, ticket)
    
    return prizes[winning_numbers]

def main():
    print('running...')
    expenses = 0
    earnings = 0
    for i in range(0,100000):
        expenses = expenses + 2 
        earnings = earnings + play_lotto()
    balance = earnings - expenses
    ROI = (earnings - expenses)/expenses
    print(f'balance : { balance }\nexpenses : ${ -1*expenses } \nearnings: ${ earnings } \nROI: { ROI * 100 }%') 

main()