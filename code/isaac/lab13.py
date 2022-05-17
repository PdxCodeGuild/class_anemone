'''Tic-Tac-Toe'''
# Create the game class
class Player:
    def __init__(self, player, token):
        self.player = player
        self.token = token


class Game:
    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',                                         
                      '1': ' ', '2': ' ', '3': ' '}
    
    def __repr__(self):  # this function will display the game board
        tac_board = f"{self.board['7']}|{self.board['8']}|{self.board['9']}\n{self.board['4']}|{self.board['5']}|{self.board['6']}\n{self.board['1']}|{self.board['2']}|{self.board['3']}"
        return tac_board
    
    def move(self, key, player):
        self.board[key] = player.token
    
    # def calc_winner(self)

    def is_full(self):
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True





full_game = Game()
player_1 = Player("Isaac", "X")
full_game.move("7", player_1)
print(full_game.__repr__())


