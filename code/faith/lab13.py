class player:
    def __init__(self, name, token): 
        self.name = name
        self.token = token


class game:
    def __init__(self, board):
        self.board = board
        board = [
            [0,1,2]
            [3,4,5]
            [6,7,8]
        ]

        

    def __repr__(self, gameboard):
        self.gameboard = gameboard
        
    def move(x,y,player):
    