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

class Board:
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
        
    def __getitem__(self, x, o)

    def __len__(self):
        return self.board









# print(Board().__repr__())

# test = input('enter name: ')
# toke = input(' x or o: ')
# print(player(test, toke))
       