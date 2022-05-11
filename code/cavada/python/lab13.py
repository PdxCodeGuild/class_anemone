import re
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
    def calc_winner(self):
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
        1\t{0}|{1}|{2}
        \t-----------
        2\t{3}|{4}|{5}
        \t-----------
        3\t{6}|{7}|{8}
        \t"""

cont = ''
s = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}

s1_x = {0:'X',1:'X',2:'X',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
# 1 [0,1,2]
s2_x = {0:'-',1:'-',2:'-',3:'X',4:'X',5:'X',6:'-',7:'-',8:'-'}
# 2 [3,4,5]
s3_x = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'X',7:'X',8:'X'}
# 3 [6,7,8]
s4_x = {0:'X',1:'-',2:'-',3:'X',4:'-',5:'-',6:'X',7:'-',8:'-'}
# 4 [0,3,6]
s5_x = {0:'-',1:'X',2:'-',3:'-',4:'X',5:'-',6:'-',7:'X',8:'-'}
# 5 [1,4,7]
s6_x = {0:'-',1:'-',2:'X',3:'-',4:'-',5:'X',6:'-',7:'-',8:'X'}
# 6 [2,5,8]
s7_x = {0:'X',1:'-',2:'-',3:'X',4:'-',5:'-',6:'-',7:'X',8:'-'}
# 7 [0,3,7]
s8_x = {0:'-',1:'X',2:'-',3:'-',4:'X',5:'-',6:'X',7:'-',8:'-'}
# 8 [1,4,6]

s1_o = {0:'O',1:'O',2:'O',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
s2_o = {0:'-',1:'-',2:'-',3:'O',4:'O',5:'O',6:'-',7:'-',8:'-'}
s3_o = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'O',7:'O',8:'O'}
s4_o = {0:'O',1:'-',2:'-',3:'O',4:'-',5:'-',6:'O',7:'-',8:'-'}
s5_o = {0:'-',1:'O',2:'-',3:'-',4:'O',5:'-',6:'-',7:'O',8:'-'}
s6_o = {0:'-',1:'-',2:'O',3:'-',4:'-',5:'X',6:'-',7:'-',8:'O'}
s7_o = {0:'O',1:'-',2:'-',3:'O',4:'-',5:'-',6:'-',7:'O',8:'-'}
s8_o = {0:'-',1:'O',2:'-',3:'-',4:'O',5:'-',6:'O',7:'-',8:'-'}
x = 2
s1x={0:'X',1:'X',2:'X',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
xs1='0:2:1'
slice = s1x[xs1]
print(slice)
xs2='3:5:1'
xs3='0:2:1'
xs3='6:8:1'
xs4='0:6:3'
xs5='1:7:3'
xs6='2:8:3'
xs7_a='0:3:3'
xs7_b='7'

xs8_a='1:4:3'
xs8_b='6'

shell = []
blank = ['X', 'X', 'X', '-', '-', '-', '-', '-', '-']
x1 = [i for i in enumerate(blank)]

print(x1)

win_x = []
win_x.append(xs1)
win_x.append(xs2)
win_x.append(xs3)
win_x.append(xs4)
win_x.append(xs5)
win_x.append(xs6)
win_x.append(xs7)
win_x.append(xs8)

# print(win_x)
win_o = []
win_o.append(s1_o)
win_o.append(s2_o)
win_o.append(s3_o)
win_o.append(s4_o)
win_o.append(s5_o)
win_o.append(s6_o)
win_o.append(s7_o)
win_o.append(s8_o)

counter = 0
used = []
breakout = [{1:1},{2:1},{3:1},{1:2},{2:2},{3:2},{1:3},{2:3},{3:3}]
breakout_avail = [{1:1},{2:1},{3:1},{1:2},{2:2},{3:2},{1:3},{2:3},{3:3}]

breakout_pair = [{1: 1}, {2: 1}, {3: 1}, {3: 2}, {2: 2}, {2: 3}, {3: 3}, {1: 3}, {1: 2}]
attempt = ''
trip = 0
used = {0:'X',1:'X',2:'X',3:'O',4:'-',5:'O',6:'O',7:'X',8:'O'} 

while len(used) != 9:
    option = {'x':'X', 'o':'O'}
    print("before for loop")
    for o in option: 
        counter += 1   
        print(f"Turn: {counter}")
        if counter < 10:
            # print(board)
            
            
            # print(s)
            board = f"""
                            TIC-TAC-TOE
                 ___________________________________________
                |                                           |
                |                x  - a x i s               |
                |        ___________________________________|     
                |       |                                   |
                |       |         1)       2)       3)      |
                |   y   |             |         |           |
                |       |  1)     {s[0]}   |    {s[1]}    |   {s[2]}\t    |
                |   -   |     ________|_________|_________  |
                |       |             |         |           |
                |   a   |  2)     {s[3]}   |    {s[4]}    |   {s[5]}\t    |
                |   x   |     ________|_________|_________  |
                |   i   |             |         |           |
                |   s   |  3)     {s[6]}   |    {s[7]}    |   {s[8]}\t    |
                |       |             |         |           |
                |_______|___________________________________|                        
            """
            print(board)
            while attempt != 'wrong choice' or attempt != 'worked' and counter <9:

                if trip == 1:
                    trip -= 1
                    counter -=1
                    break

                elif trip == 0:
                    print(f"Turn {counter} - player: {o}")
                    x_pos,y_pos = (int(input("enter 'x-axis' position: "))),(int(input("enter 'y-axis' position: ")))
                    player = o
                    value = option[player]
                    print(x_pos,y_pos)
                    code = breakout.index({x_pos:y_pos})
                    if s[code] == '-':
                        s[code]=value
                        save = breakout.pop(code)
                        breakout_avail.pop
                        used.append(save)
                        breakout.insert(code,save)
                        attempt = 'worked'
                        break
                    else:
                        print(f"{breakout[code]} not in {breakout_pair} " )
                        attempt = 'wrong choice'
                        counter -= 1
                        trip +=1
                        break
                print(s)
                print(f"code: {code}")
                print(f"used: {used}") 
                print(f"remainiing available: {breakout_pair}")
                board = f"""
                                TIC-TAC-TOE
                    ___________________________________________
                    |                                           |
                    |                x  - a x i s               |
                    |        ___________________________________|     
                    |       |                            
                    |       |         1)       2)       3)
                    |   y   |             |         |
                    |       |  1)     {s[0]}   |    {s[1]}    |   {s[2]}
                    |   -   |     ________|_________|________
                    |       |             |         |
                    |   a   |  2)     {s[3]}   |    {s[4]}    |   {s[5]}
                    |   x   |     ________|_________|________
                    |   i   |             |         |
                    |   s   |  3)     {s[6]}   |    {s[7]}    |   {s[8]}
                    |       |             |         |
                    |_______|                        
                """
                print(board)
            else:
                print("game over" )
            print(s)
            print(f"code: {code}")
            print(f"used: {used}") 
            # print(f"next avail: {breakout_pair[code]}")
            print(f"remainiing available: {breakout_pair}")
            # print(code,type(code), value)
        elif counter > 100: 
            break
if counter > 8:
    print(s)
    board = f"""
                                TIC-TAC-TOE
                     ___________________________________________
                    |                                           |
                    |                x  - a x i s               |
                    |        ___________________________________|     
                    |       |                            
                    |       |         1)       2)       3)
                    |   y   |             |         |
                    |       |  1)     {s[0]}   |    {s[1]}    |   {s[2]}
                    |   -   |     ________|_________|________
                    |       |             |         |
                    |   a   |  2)     {s[3]}   |    {s[4]}    |   {s[5]}
                    |   x   |     ________|_________|________
                    |   i   |             |         |
                    |   s   |  3)     {s[6]}   |    {s[7]}    |   {s[8]}
                    |       |             |         |
                    |_______|                        
               """
    print(board)
        
# print(used)



# for use in used:
#     for u in use:
#         print(u)
        # blank.append(u)
def test_winner(s):
    blank = []
    pair = []
    s1_x = {0:'X',1:'X',2:'X',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
    test = {0:'X',1:'X',2:'X',3:'O',4:'-',5:'O',6:'O',7:'X',8:'O'} 
    pair.append(s1_x)
    pair.append(test)
    tester = []
    for win in win_x:
        for p in pair:
            for i, each in enumerate(p):
                # print(p[each])
                blank.append(p[each])
            x=(blank[win])
            tester.append(x)
        
        print(tester)
        for test in tester:
            if test == test:
                print('yes')
                break
            else:
                print('no')
                break
        return True


# print(blank[3:5])
s2_x = {0:'-',1:'-',2:'-',3:'X',4:'X',5:'X',6:'-',7:'-',8:'-'}

# print(blank[6:8])
s3_x = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'X',7:'X',8:'X'}

# print(blank[0:6:3])
s4_x = {0:'X',1:'-',2:'-',3:'X',4:'-',5:'-',6:'X',7:'-',8:'-'}

# print(blank[1:7:3])
s5_x = {0:'-',1:'X',2:'-',3:'-',4:'X',5:'-',6:'-',7:'X',8:'-'}

# print(blank[2:8:3])
s6_x = {0:'-',1:'-',2:'X',3:'-',4:'-',5:'X',6:'-',7:'-',8:'X'}

# print(blank[0])
s7_x = {0:'X',1:'-',2:'-',3:'X',4:'-',5:'-',6:'-',7:'X',8:'-'}

# print(blank[0])
s8_x = {0:'-',1:'X',2:'-',3:'-',4:'X',5:'-',6:'X',7:'-',8:'-'}

win_x.append(s1_x)
win_x.append(s2_x)
win_x.append(s3_x)
win_x.append(s4_x)
win_x.append(s5_x)
win_x.append(s6_x)
win_x.append(s7_x)
win_x.append(s8_x)
