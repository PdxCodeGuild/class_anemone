class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game(Player):
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return

    def move(self, dx, dy, board):
        return

    def calc_winner(self):
        return

    def is_full(self):
        return

    def is_game_over(self):
        return

