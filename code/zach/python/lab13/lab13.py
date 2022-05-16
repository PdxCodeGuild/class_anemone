class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.prompt = f'Player - { name } enter row and column [r,c]: '

    def get_move(self):
        message = input(self.prompt)
        row, col = [int(x) for x in message.split(',')]
        return row, col

    def __repr__(self):
        return self.name


class GameBoard:
    def __init__(self, size = 3, blank_space = '_' ):
        self.size = size
        self.data = [[blank_space for i in range (size)] for j in range(size)]




# class Game:
#     def __init__(self, board):
#         self.board = []

#     def __repr__(self):
#         for i in range(3):

#         return

#     def move(self, dx, dy, player):
#         return

#     def calc_winner(self):
#         return

#     def is_full(self):
#         return

#     def is_game_over(self):
#         return

        
