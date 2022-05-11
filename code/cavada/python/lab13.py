from multiprocessing.sharedctypes import Value
import random


class TicTacToe:
    pass

class Player(TicTacToe):
    def __init__(self, name, token):
        self.name = name
        self.token = token
    pass

class Game(TicTacToe):
    def __init__(self, board):
        self.board = board
        

    def __repr__(self):
        print(self.board)
    
    def move(self, x, y, player):
        pass
    def calc_winnder(self):
        pass
    def is_full(self):
        pass
    def is_game_over(self):
        pass
class Board(TicTacToe):
    def __init__(self, board):
        self.spaces = ['','']
        self.board = board
        board = f"""
        \t\t 1   2   3
        1\t{x}|{x}|{x}
        \t-----------
        2\t{x}|{x}|{x}
        \t-----------
        3\t{x}|{x}|{x}
        \t"""

# x = ['-','-', '-', '-', '-', '-', '-', '-', '-']
# x_pos = int(input("enter 'x' position"))
# y_pos = int(input("enter 'y' position"))

# print(x)

option = {'x':'X', 'o':'O'}
# position_x = {0:1,1:2,2:3,3:1,4:2,5:3,6:1,7:2,8:3}
# position_y = {0:1,1:1,2:1,3:2,4:2,5:2,6:3,7:3,8:3}
# breakout_pair = [{1:1},{2:1},{3:1},{1:2},{2:2},{3:2},{1:3},{2:3},{3:3}]
# x = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
# o = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}


# player = input("player selection - choose 'x' or 'o': ")
# value = option[player]
# print(x_id,y_id
# code = breakout_pair.index({x_pos:y_pos})
# print(code,type(code), value)
# x[code]=value
# x[4]='X'
# for pair in x:
    # print(pair)
    # print(x[0])
# print(x)
# print(code)
# x[0]=option[token]
# for i, breakout in enumerate(breakout_pair):
#     for b in breakout:
#         print(breakout[i+1])
# r = random.randint(1,9)

# def rand_pos(x,y):
#     x_val = int(x)
#     y_val = int(y)
#     dict_tac_toe[x]= x_val
#     dict_tac_toe[y]= y_val
cont = ''
s = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
while cont != 'n':
    
    
    x_pos,y_pos = (int(input("enter 'x' position: "))),(int(input("enter 'y' position: ")))
    # print(x)
    option = {'x':'X', 'o':'O'}
    # position_x = {0:1,1:2,2:3,3:1,4:2,5:3,6:1,7:2,8:3}
    # position_y = {0:1,1:1,2:1,3:2,4:2,5:2,6:3,7:3,8:3}
    breakout_pair = [{1:1},{2:1},{3:1},{1:2},{2:2},{3:2},{1:3},{2:3},{3:3}]
    player = input("player selection - choose 'x' or 'o': ")
    value = option[player]
    # print(x_id,y_id
    code = breakout_pair.index({x_pos:y_pos})
    print(code,type(code), value)
    s[code]=value
    print(s)
    board = f"""
                    TIC-TAC-TOE
         ________________________________________
        |             x  - a x i s               |
        |    ____________________________________|     
        |   |       
        |   |         1        2        3
        | y |             |         |
        |   |  1      {s[0]}   |    {s[1]}    |   {s[2]}
        | - |     ________|_________|________
        |   |             |         |
        | a |  2      {s[3]}   |    {s[4]}    |   {s[5]}
        | x |     ________|_________|________
        | i |             |         |
        | s |  3      {s[6]}   |    {s[7]}    |   {s[8]}
        |   |             |         |
        |___|                        
    """
    print(board)
    cont = input("continue? ")
    if cont == 'n':
        break
    