class Player():
    
    
    
    def __init__(self):
        self.cplayersxo = []
        

    
    def nplayer(self, person, piece):
        for i in enumerate(person):
            self.cplayersxo.append(i)
        x = 0
        for i in enumerate(piece):
            self.cplayersxo.append(x[i])
            x +=1
        


class Board():
    
    def __init__(self):
        self.board = [
            [' ', ' ', ' '], 
            [' ', ' ', ' '], 
            [' ', ' ', ' ']
            ]
        
        
    def __repr__(self):
        nb = ''
        for x in self.board:
            nb += '|'.join(x)
            nb += ('\n')
        return nb
        


    def move(self, x, y, player):
        
        piece = player       
        if self.board[x][y] != ' ':
            return 'Space has already been taken'
        else:
            self.board[x][y] = piece
        # if play in self.board[0]:
        #     self.board[0][play] == [w.replace(play, piece) for w in self.board[0]]
        # elif play in self.board[1]:
        #     self.board[1][play] == [w.replace(play, piece) for w in self.board[1]]
        # elif play in self.board[2]:
        #     self.board[2][play] == [w.replace(play, piece) for w in self.board[2]]
        return


    def calc_winner(self):
        winner = ''
        
        
        if self.board[0] == ['X', 'X', 'X']:
            winner += 'X'
            return
        elif self.board[1] == ['X', 'X', 'X']:   
            winner += 'X'
            return
        elif self.board[2] == ['X', 'X', 'X']:   
            winner += 'X'
            return
        elif [self.board[0][0] + self.board[1][0] + self.board[2][0]] == ['X', 'X', 'X']:   
            winner += 'X'
            return
        elif [self.board[0][1] + self.board[1][1] + self.board[2][1]] == ['X', 'X', 'X']:   
            winner += 'X'
            return
        elif [self.board[0][2] + self.board[1][2] + self.board[2][2]] == ['X', 'X', 'X']:   
            winner += 'X'
            return
        elif [self.board[0][0] + self.board[1][1] + self.board[2][2]] == ['X', 'X', 'X']:   
            winner += 'X'
            return
        elif [self.board[0][2] + self.board[1][1] + self.board[2][0]] == ['X', 'X', 'X']:   
            winner += 'X'
            return
        elif self.board[0] == ['O', 'O', 'O']:
            winner += 'O'
            return
        elif self.board[1] == ['O', 'O', 'O']:   
            winner += 'O'
            return
        elif self.board[2] == ['O', 'O', 'O']:   
            winner += 'O'
            return
        elif [self.board[0][0] + self.board[1][0] + self.board[2][0]] == ['O', 'O', 'O']:   
            winner += 'O'
            return
        elif [self.board[0][1] + self.board[1][1] + self.board[2][1]] == ['O', 'O', 'O']:   
            winner += 'O'
            return
        elif [self.board[0][2] + self.board[1][2] + self.board[2][2]] == ['O', 'O', 'O']:   
            winner += 'O'
            return
        elif [self.board[0][0] + self.board[1][1] + self.board[2][2]] == ['O', 'O', 'O']:   
            winner += 'O'
            return
        elif [self.board[0][2] + self.board[1][1] + self.board[2][0]] == ['O', 'O', 'O']:   
            winner += 'O'
            return
        elif winner == '':
            return False
        else:
            return True, winner
               
        

        

    def full(self):
        full = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in full:
            if i in self.board:
                return False
            else:
                return True

    def is_game_over(self):
        if self.full() == False and self.calc_winner() == False:
            return True 
        else:
            return False    

xo = Board()   
pl = Player()

# board = xo.board()



pieces = ['X', 'O']    
playon = True
turns = 0
while playon:
    while len(pl.cplayersxo) != 2:
        player = input('Please enter your name. ').lower()
        piece = input(f'Select a piece {pieces}. ').upper()
        pieces.remove(piece)
        pl.cplayersxo.append([player, piece])
    while xo.calc_winner() == False and xo.is_game_over() == False:
        print(Board().__repr__())
        xint = int(input(f'{pl.cplayersxo[0]}) its you turn choose a row. '))
        yint = int(input('Now choose a column. '))
        xo.move(xint, yint,  pl.cplayersxo[0][1])
            
        
        print(Board().__repr__())
        xint = int(input(f'{pl.cplayersxo[1]} its your turn choose a row. '))
        yint = int(input('Now choose a column. '))
        xo.move(xint, yint, pl.cplayersxo[1][1])
        
        
        
        pass









