'''Tic-Tac-Toe'''
# Create the game class
class Player:
    def __init__(self, player, token):
        self.player = player
        self.token = token


class Game:
    def __init__(self):
        self.board = {'7': '', '8': '', '9': '',
                    '4': '', '5': '', '6': '',                                         
                    '1': '', '2': '', '3': ''}
    
    def __repr__(self):  # this function will display the game board
        tac_board = ' | | \n | | \n | |'
        return tac_board
     
    # def move(self, x, y, player):
    #     x = 0
    #     y = 0 
    #     return x, y, player

game_board = (repr(['7']) + '|' + repr(['8']) + '|' + repr(['9']),
              repr(['4']) + '|' + repr(['5']) + '|' + repr(['6']),
              repr(['1']) + '|' + repr(['2']) + '|' + repr(['3']))


full_game = Game()
print(full_game.__repr__())


