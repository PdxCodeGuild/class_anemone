'''Tic-Tac-Toe'''
# Create the game class
class Game:
    def __init__(self):
        self.board = {'7': '', '8': '', '9': '',
                    '4': '', '5': '', '6': '',                                         
                    '1': '', '2': '', '3': ''}
    
    def __repr__(self, board):  # this function will display the game board
        self.board['7'] + '|' + self.board['8'] + '|' + self.board['9']
        self.board['4'] + '|' + self.board['5'] + '|' + self.board['6']
        self.board['1'] + '|' + self.board['2'] + '|' + self.board['3']
        return repr(board)
     
    # def move(self, x, y, player):
    #     x = 0
    #     y = 0 
    #     return x, y, player

game_board = (repr(['7']) + '|' + repr(['8']) + '|' + repr(['9']),
              repr(['4']) + '|' + repr(['5']) + '|' + repr(['6']),
              repr(['1']) + '|' + repr(['2']) + '|' + repr(['3']))


full_game = Game()
print(full_game.__repr__(game_board))


