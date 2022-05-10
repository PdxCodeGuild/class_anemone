'''
Class anemone
Lab 13
Bailey Baker
'''

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        self.board = [[' 'for i in range(3)] for j in range(3)]

    def __repr__(self):
        show = ''
        for i in self.board:
            show += '|'.join(i)
            show += '\n'
        return show
    
    def move(self, x, y, player):
        if self.board[x][y] != ' ':
            print("Invalid position")
            return False
        else: 
            self.board[x][y] = player
            return True

    def calc_winner(self):
        pass

    def is_full():
        pass

    def is_game_over():
        pass

play = Game()
player_1 = Player(input("Enter name: "), 'X')
player_2 = Player(input("Enter name: "), 'O')

while True:
    print(Game.__repr__(play))

    while True:
        x = int(input(f"{player_1.name} Enter your move's x coordinate: "))
        y = int(input(f"{player_1.name} Enter your move's y coordinate: "))
        test = Game.move(play, x, y, player_1.token)
        if test == False:
            print("Try again.")
        elif test == True:
            break
    Game.calc_winner(play)
    print(Game.__repr__(play))
