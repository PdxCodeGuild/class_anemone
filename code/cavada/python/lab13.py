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
        pass


"""this is outside of the class info"""

"""these are the slices that make a tic-tac-toe win"""
def check(set):
    set_check = []
    x=0
    options = {'o':'O','x':'X'}
    # set = {0:'X',1:'O',2:'X',3:'O',4:'-',5:'O',6:'O',7:'O',8:'O'} 
    set_l = [set[s] for s in set]                
    # print(set_list)       
    # s_list= []            
    s1,s2,s3,s4,s5,s6,s7,s8=(set_l[0:3]),(set_l[3:6]),(set_l[6:]),(set_l[0:7:3]),(set_l[1:8:3]),(set_l[2::3]),(set_l[0::4]),(set_l[2:7:2])
    set_check.append(s1) 
    set_check.append(s2) 
    set_check.append(s3) 
    set_check.append(s4) 
    set_check.append(s5) 
    set_check.append(s6) 
    set_check.append(s7) 
    set_check.append(s8) 
    # print(set_check) # list used to check for win
    # win = [['X', 'X', 'X'], ['X', 'X', 'O'], ['X', 'X', 'X'], ['X', 'X', 'O'], ['X', '-', 'X'], ['X', 'X', 'X'], ['X', 'X', 'O'], ['X', 'X', 'X']]     
    # print(s3)
    xwin = ['X', 'X', 'X']
    owin = ['O', 'O', 'O']
    x=0
    while x == 0:
        for set in set_check:
            if set == owin and set != xwin:
                print("win", options['o'])
                x+=1
                break
            elif set == xwin and set !=owin:
                print('win', options['x'])
                x+=1
                break
            elif set != xwin or set != owin:
                # print("none")
                x+=10
    return x
s = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'} 
    
shell = []
blank = ['X', 'X', 'X', '-', '-', '-', '-', '-', '-']
# x1 = [i for i in enumerate(blank)]

ct =0
counter = 0
used = []#{0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
breakout = [{1:1},{2:1},{3:1},{1:2},{2:2},{3:2},{1:3},{2:3},{3:3}]
breakout_avail = [{1:1},{2:1},{3:1},{1:2},{2:2},{3:2},{1:3},{2:3},{3:3}]
digit = [1,2,3,'1','2','3']
breakout_pair = [{1:1},{2:1},{3:1},{3:2},{2:2},{2:3},{3:3},{1:3},{1:2}]
attempt = ''
trip = 0
# s = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'} 
win = ''
skip = 'no'
while len(used) < 9:
    option = {'x':'X', 'o':'O'}
    # print("before for loop")
    for o in option: 
        if win == 'win' or check(s) ==1:
            print("it should've worked???")
            skip = 'yes'
            break
        
        # print(f"Turn: {counter}")
        if counter < 10 and win != 'win' and skip == 'no':
            counter += 1   
            # print(board)
            print(s)
            if win == 'win' and check(s) != 1:
                ct = 1
                pass
            board = f"""
                            TIC-TAC-TOE
                 ___________________________________________
                |                                           |
                |                x  - a x i s               |
                |        ___________________________________|   Current Player:  
                |       |                                   |       {o}  
                |       |         1)       2)       3)      |   
                |   y   |             |         |           |    Turn:{counter}
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
            
            check(s) 
             
            print(board)
            
            while attempt == '' and counter <9 and win == '' and check(s) != 1 and ct == 0:

                if trip == 1:
                    trip -= 1
                    counter -=1
                    break
                elif check(s) == 1:
                    print(s,option)
                    used = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
                    win = 'win'
                    skip = 'yes'
                    trip +=1
                    ct += 1
                    pass

                elif trip == 0 and win != 'win' and check(s) != 1 :
                    trip_a = 0
                    print(f"Turn {counter} - player: {o}")
                    while trip_a == 0 and win != 'win' and check(s) != 1:
                        x_pos,y_pos = (input("enter 'x-axis' position: ")),(input("enter 'y-axis' position: "))
                        if x_pos in digit or y_pos in digit:
                            trip_a += 1
                        else:
                            trip_a == 0

                    player = o
                    value = option[player]
                    # print(x_pos,y_pos)
                    code = breakout.index({int(x_pos):int(y_pos)})
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
                # print(f"code: {code}")
                print(f"used: {used}") 
                print(f"remaining available: {breakout_avail}")
                print(board)
            if win == 'win' or counter > 8:
                print("game over" )
            print(s)
            print(f"code: {code}")
            print(f"used: {used}") 
            # print(f"next avail: {breakout_pair[code]}")
            print(f"remaining available: {breakout_pair}")
            # print(code,type(code), value)
        elif counter > 100: 
            break
    if counter > 8 or win == 'win' or check(s) ==1:
        print(s)
        ct +=1
        used = [1,2,3,4,5,6,7,8,9]
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
# def test_winner(s):
#     blank = []
#     pair = []
#     s1_x = {0:'X',1:'X',2:'X',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
#     test = {0:'X',1:'X',2:'X',3:'O',4:'-',5:'O',6:'O',7:'X',8:'O'} 
#     pair.append(s1_x)
#     pair.append(test)
#     tester = []
#     for win in win_x:
#         for p in pair:
#             for i, each in enumerate(p):
#                 # print(p[each])
#                 blank.append(p[each])
#             x=(blank[win])
#             tester.append(x)
        
#         print(tester)
#         for test in tester:
#             if test == test:
#                 print('yes')
#                 break
#             else:
#                 print('no')
#                 break
#         return True


