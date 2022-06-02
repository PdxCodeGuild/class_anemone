import random


def init():
      """
      Initialize game
    
      Outputs:
        * gameStatus
        * magicNumber
      """
      # Generate a random Magic number
      return None, random.randint(1,10)


def processinput():
    while True:
        word = input('What is the magic number? ')
        if word == 'quit':
            return None
        
        try:
            playerNumber = int(word)
            break
        except ValueError:
            print('Please type a number without decimals')
            continue
        
    return playerNumber


def update(gameStatus, magicNumber, playerNumber):

    if playerNumber is None:
        gameStatus = 'end'

    elif playerNumber == magicNumber:
        gameStatus = "win"

    elif magicNumber < playerNumber:
        gameStatus = "lower"

    elif magicNumber > playerNumber:
        gameStatus = "higher"
    
    return gameStatus, magicNumber


def render(gameStatus, magicNumber):
    
    if gameStatus == "win":
        print("This is correct! You win!")
    
    elif gameStatus == "end":
        print("Bye!")
    
    elif gameStatus == "lower":
        print("The magic number is lower")
    
    elif gameStatus == "higher":
        print("The magic number is higher")
        
    else:
        raise RuntimeError("Unexpected game status {}".format(gameStatus))

def runGame():
    gameStatus, magicNumber = init()
    while gameStatus != 'win' and gameStatus != 'end':
        playerNumber = processinput()
        gameStatus, magicNumber, = update(gameStatus, magicNumber, playerNumber)

runGame()