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



def main():
    winning = pick6()
    ticket = pick6()

    wins = num_matches(winning, ticket)

    print(winning, ticket, wins)

main()