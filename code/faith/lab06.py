def stringnum(cardnum):
    cardnum = cardnum.split()
    for x in range(len(cardnum)):
        cardnum[x] = int(cardnum[x])
    return cardnum

