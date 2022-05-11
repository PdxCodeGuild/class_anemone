import random
import math
import string

class Player:  # input for top/middle/bottom then for left/middle/right
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        if self.token == 'x':
            return str(self.token)
        elif self.token == 'o':
            return str(self.token)

class Game:
    def __init__(self):
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
    def __repr__(self):
        a = ''
        for x in self.board:
            a += ("|".join(x))
            a += ('\n')
        return a
        
    def move(self, player, spot1):
        q=self.board[0][1]
        w=self.board[0][2]
        e=self.board[0][0]

        r=self.board[1][0]
        t=self.board[1][1]
        y=self.board[1][2]

        u=self.board[2][0]
        i=self.board[2][1]
        o=self.board[2][2]
        
        if spot1 != ' ':
            return 'Spot Already in use'
        else:
            spot1 = player.token

        
     
    def __len__(self):
        if len(self.board) != ' ':
            return 'Board full'
    
    
    # def calc_winner(self, spot1):


# game = Game()
# name1 = input('enter name: ')
# token1 = input(' x or o: ')
# name2 = input('enter name: ')
# token2 = input(' x or o: ')
# player1 = Player(name1,token1)
# player2 = Player(name2,token2)

while True:
    game = Game()
    name1 = input('enter name: ')
    token1 = input(' x or o: ')
    name2 = input('enter name: ')
    token2 = input(' x or o: ')
    player1 = Player(name1,token1)
    player2 = Player(name2,token2)
    print(f"'Q'|'W'|'E'\n'R'|'T'|'Y'\n'U'|'I'|'O'")
    choose = input('select spot by using letters above | Enter spot: ').lower()
    game.move(player1, choose)
    print(game.__repr__())    



# a = [
# ['Q','W','E'],
# ['R','T','Y'],
# ['U','I','O']
#         ]

# q= a[0][1]
# w= a[0][2]
# e= a[0][0]

# r= a[1][0]
# t= a[1][1]
# y= a[1][2]

# u= a[2][0]
# i= a[2][1]
# o= a[2][2]



# print(e,w,q)
# print(r,t,y)
# print(u,i,o)





       