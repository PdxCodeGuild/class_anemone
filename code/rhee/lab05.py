import random

ticket_price = 2
jackpot = {"1": 4, "2": 7, "3": 100, "4": 50000, "5": 1000000, "6": 25000000}


def draw6(list_length=6):
    ticket_numbers = []
    generated_numbers = 0
    while generated_numbers < list_length:
        ticket_number = random.randrange(1, 99)
        ticket_numbers.append(ticket_number)
        generated_numbers += 1
    return ticket_numbers


def num_matches(winner: list, ticket: list) -> int:
    winners = []
    # winnings = 0
    match_count = 0
    balance = 0
    balance -= ticket_price
    for i in range(len(winner)):
        if winner[i] == ticket[i]:
            winners.append(winner[i])
            match_count += 1
            winnings = jackpot.get(str(len(winners)))
            balances = balance + winnings

    return balance


if __name__ == "__main__":
    rounds = input(">>> How many times do you want to play?: ")
    counter = 0
    final_number = 0
    while counter < int(rounds):
        cpu_ticket = draw6(6)
        player_ticket = draw6(6)
        final_number += num_matches(cpu_ticket, player_ticket)
        counter += 1
        expenses = counter * -2
        earnings = expenses - final_number
        ROI = ((earnings - expenses) / expenses) * 100
        
    print(f"Your final balance is: {final_number}\n")
    print(f"Earnings: {abs(final_number - expenses)}\n")
    print(f"Expenses: {expenses}\n")
    print(f"Return on Investment: {round(ROI, 2)}%\n")
    print(f"Your ending balance is: {final_number}\n")
