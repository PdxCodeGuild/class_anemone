import random


def pick6():
    return [random.randint(1,99) for _ in range(6)]

    # ticket= []
    # for _ in range(6):
    #     ticket.append(random.randint(1,99))
    #     return ticket

print(pick6())