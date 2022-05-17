class Player():
       
    def __init__(self):
        self.cplayersxo = []                        # creates a blank list for players and their pieces
        
    
    def nplayer(self, person, piece):
        self.cplayersxo.append([person, piece])     # creats a list list of players and their pieces

    # def reset(self):                              # resets the player list for another game
    #     self.cplayersxo = []                      # turns out I dont need it if i just put the calls in the loop... great  
        


class Board():
    
    def __init__(self):                             # creats a blank board from a list list
        self.board = [
            [' ', ' ', ' '], 
            [' ', ' ', ' '], 
            [' ', ' ', ' ']
            ]
    
    
    def __repr__(self):                             # joins the board with | to make it look something like a tictactoe board
        nb = ' |1|2|3|\n'
        y = 1
        sl = '|'
        for x in self.board:
            nb += str(y)
            nb += sl
            nb += '|'.join(x)
            nb += '|'
            nb += ('\n')
            y += 1
        return nb
        
    
    def validation(self, x, y):                     # test whether or not he spot attempting to be played is enpty
        if self.board[x][y] != ' ':
            return False
        else:
            return True

    
    def move(self, x, y, player):                   # places a piece on the board from inputs and player turn
        
        piece = player       
        if self.board[x][y] != ' ':
            return 
        else:
            self.board[x][y] = piece
            return 
        # if play in self.board[0]:
        #     self.board[0][play] == [w.replace(play, piece) for w in self.board[0]]
        # elif play in self.board[1]:
        #     self.board[1][play] == [w.replace(play, piece) for w in self.board[1]]
        # elif play in self.board[2]:
        #     self.board[2][play] == [w.replace(play, piece) for w in self.board[2]]
        # return


    def calc_winner(self):
        winner = ''                                             # okay this might be the hard coded way but test for winner conditions
        
        if winner == '':
            if self.board[0] == ['X', 'X', 'X']:
                winner = 'X'
                return winner
            elif self.board[1] == ['X', 'X', 'X']:   
                winner = 'X'
                return winner
            elif self.board[2] == ['X', 'X', 'X']:   
                winner += 'X'
                return winner
            elif [self.board[0][0], self.board[1][0], self.board[2][0]] == ['X', 'X', 'X']:   # had + at first instead of ,'s but that didn't match the ==
                winner = 'X'
                return winner
            elif [self.board[0][1], self.board[1][1], self.board[2][1]] == ['X', 'X', 'X']:   
                winner = 'X'
                return winner
            elif [self.board[0][2], self.board[1][2], self.board[2][2]] == ['X', 'X', 'X']:   
                winner = 'X'
                return winner
            elif [self.board[0][0], self.board[1][1], self.board[2][2]] == ['X', 'X', 'X']:   
                winner = 'X'
                return winner
            elif [self.board[0][2], self.board[1][1], self.board[2][0]] == ['X', 'X', 'X']:   
                winner = 'X'
                return winner
            elif self.board[0] == ['O', 'O', 'O']:
                winner = 'O'
                return winner
            elif self.board[1] == ['O', 'O', 'O']:   
                winner = 'O'
                return winner
            elif self.board[2] == ['O', 'O', 'O']:   
                winner = 'O'
                return winner
            elif [self.board[0][0], self.board[1][0], self.board[2][0]] == ['O', 'O', 'O']:   
                winner = 'O'
                return winner
            elif [self.board[0][1], self.board[1][1], self.board[2][1]] == ['O', 'O', 'O']:   
                winner = 'O'
                return winner
            elif [self.board[0][2], self.board[1][2], self.board[2][2]] == ['O', 'O', 'O']:   
                winner = 'O'
                return winner
            elif [self.board[0][0], self.board[1][1], self.board[2][2]] == ['O', 'O', 'O']:   
                winner = 'O'
                return winner
            elif [self.board[0][2], self.board[1][1], self.board[2][0]] == ['O', 'O', 'O']:   
                winner = 'O'
                return winner
            elif winner == '':                                     
                return False
            
            elif winner == 'X' or winner == 'O':
                return winner
         
        elif winner == 'X' or winner == 'O':
            return str(f'{winner}')
         

    def full(self):                                         # test the board list by list for an empty spot
        full = ' '                                          # if not returns True
        for i in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[i][y] == ' ':
                    return False
        else:
            return True

    
    def is_game_over(self):                                 # ask for winner and full and if either returns True it return True
        if self.full() == False and self.calc_winner() == False:
            return False 
        else:
            return True


    # def reset(self):                                          # resets the board to a blank one...
    #     if self.is_game_over == True:                         # turns out I dont need it if i just put the calls in the loop... great
    #         self.board = [
    #         [' ', ' ', ' '], 
    #         [' ', ' ', ' '], 
    #         [' ', ' ', ' ']
    #         ]



# board = xo.board()


yes = ['y', 'yes', 'yes', 'ye', 'ya']
no = ['n', 'no', 'na', 'nada', 'nope']
pieces = ['X', 'O']    
playon = True
turns = 1

while playon:                                                   # initiates a while loop for the game to be played
    xo = Board()   
    pl = Player()
    while len(pl.cplayersxo) != 2:
        player = input('Please enter your name. ').lower()      # request players names and pieces to add to the list
        piece = input(f'Select a piece {pieces}. ').upper()
        pieces.remove(piece)                                    # removes the piece from the list
        pl.cplayersxo.append([player, piece])                   # adds them to the list in Player()
    
    while xo.calc_winner() == False and xo.full() == False:                 # similar to is game over but it just wasn't working
        
        if turns % 2 == 1:                                                                                                  # ask for turns cause if not a valid place on the board turns will remain the same
            print(xo.__repr__())                                                                                            # prints the current board
            xint = int(input(f'{pl.cplayersxo[0]}) its you turn choose a row by entering a number bewtween 1 - 3. ')) - 1   # inputs for specific rows and coloums
            yint = int(input('Now choose a column by entering a number bewtween 1 - 3. ')) - 1
            
            if xint not in range(0, 3) or yint not in range(0, 3):
                print('Your input was not a correct option please try again.')
                
            elif xint in range(0, 3) and yint in range(0, 3):
                
                if xo.validation(xint, yint) == True:           # test if placement if capable and if not returns the play to try again
                    xo.move(xint, yint, pl.cplayersxo[0][1])    # if so places the piece and adds one to turn
                    turns += 1
            
                elif xo.validation(xint, yint) == False:
                    print('That space has been taken')
            
                        
        elif turns % 2 == 0:                                # if turns is 0 moves to player 2s turn
            print(xo.__repr__())
            xint = int(input(f'{pl.cplayersxo[1]} its your turn choose a row by entering a number bewtween 1 - 3. ')) - 1
            yint = int(input('Now choose a column by entering a number bewtween 1 - 3. ')) - 1 
                        
            if xint not in range(0, 3) or yint not in range(0, 3):
                print('Your input was not a correct option please try again.')
                
            elif xint in range(0, 3) and yint in range(0, 3):
                
                if xo.validation(xint, yint) == True:
                    xo.move(xint, yint, pl.cplayersxo[1][1])
                    turns += 1
                
                elif xo.validation(xint, yint) == False:
                    print('That space has been taken')
        
    
    
    if xo.calc_winner() != False:                           # test the board for a winner though it already did in the above while loop
        winner = xo.calc_winner()                           # should change to winner but is saying None... so each winning condition has a return winner now
        print(xo.__repr__())                                # prints the final board for players to see
        print(winner, 'has won the game')                   # prints winner of the game
        again = input('Would you like to play again? Y/N. ').lower()        # ask if they want to play again
        
        if again in yes:
            playon = True
            turns = 1
            # xo.reset()
            # pl.reset()
            pieces = ['X', 'O']
            pass
        
        elif again in no:                                           # breaks the loop if they do not want to play again
            print('I hope you had fun and it worked well enough.')
            break