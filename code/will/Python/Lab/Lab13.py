'''
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

The Player class has the following properties:

name = player name
token = 'X' or 'O'
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples, or dictionary.

The Game class has the following methods:

__repr__() Returns a pretty string representation of the game board

>>> print(board)
print( Y             )
print('0 |__|__|__|' )
print('1 |__|__|__|' )
print('2 |  |  |  |' )
print('X  0   1  2  ')


'''


'''

move(x, y, player)
calc_winner()
is_full()
is_game_over()

'''

#submission time




class Player:


    def __init__(self, name, token):
       self.name = name
       self.token = token 
      

 


class Board:

    def __init__(self):
     #  self.board = [[" "for i in range(3)]for j in range(3)]
      self.board = [[' ',' ',' '],
                    [' ',' ',' '],
                    [' ',' ',' ']]
               



     
    def __repr__(self):
        ret =""
        for row in self.board:
            ret += '|'.join(row)
            ret += '\n'
        return ret

    

 
       
    def move(self, x, y, token):
    #    possible_moves = {1:(0,0), 2:(1,0),3:(2,0),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
        if self.board[y][x] != " ":
            return "This space is already taken"
        else:
            self.board[y][x] = token 
        
        
    def calc_winner(self, player):
        
        #for i in range(3):
        #    row = self.board[i]
        #    if all(item == row[0] and item != " " for item in row):
        #        return 
        if self.board[0][0] == self.board[1][0] == self.board[2][0]== player.token:
            return player.token
        elif self.board[0][0] == self.board[0][1] == self.board[0][2]== player.token:
            return player.token
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]== player.token:
            return player.token
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]== player.token:
            return player.token
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]== player.token:
            return player.token
        elif self.board[2][0] == self.board[1][1] == self.board[0][2]== player.token:
            return player.token
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]== player.token:
            return player.token
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]== player.token:
            return player.token



    def is_full(self):
        pass
    def is_game_over(self):
        pass

board = Board()
print(board)
