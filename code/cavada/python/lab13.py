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


cont = ''
s = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
x1,x2,x3,x4,x5,x6,x7,x8 = {0:'X',1:'X',2:'X',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'},{0:'-',1:'-',2:'-',3:'X',4:'X',5:'X',6:'-',7:'-',8:'-'},{0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'X',7:'X',8:'X'},{0:'X',1:'-',2:'-',3:'X',4:'-',5:'-',6:'X',7:'-',8:'-'},{0:'-',1:'X',2:'-',3:'-',4:'X',5:'-',6:'-',7:'X',8:'-'},{0:'-',1:'-',2:'X',3:'-',4:'-',5:'X',6:'-',7:'-',8:'X'},{0:'X',1:'-',2:'-',3:'-',4:'X',5:'-',6:'-',7:'-',8:'X'},{0:'-',1:'-',2:'X',3:'-',4:'X',5:'-',6:'X',7:'-',8:'-'}
xwins=[]
xwins.append(x1)
xwins.append(x2)
xwins.append(x3)
xwins.append(x4)
xwins.append(x5)
xwins.append(x6)
xwins.append(x7)
xwins.append(x8)


o1,o2,o3,o4,o5,o6,o7,o8 = {0:'O',1:'O',2:'O',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'},{0:'-',1:'-',2:'-',3:'O',4:'O',5:'O',6:'-',7:'-',8:'-'},{0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'O',7:'O',8:'O'},{0:'O',1:'-',2:'-',3:'O',4:'-',5:'-',6:'O',7:'-',8:'-'},{0:'-',1:'O',2:'-',3:'-',4:'O',5:'-',6:'-',7:'O',8:'-'},{0:'-',1:'-',2:'O',3:'-',4:'-',5:'O',6:'-',7:'-',8:'O'},{0:'O',1:'-',2:'-',3:'-',4:'O',5:'-',6:'-',7:'-',8:'O'},{0:'-',1:'-',2:'O',3:'-',4:'O',5:'-',6:'O',7:'-',8:'-'}
owins= []
owins.append(o1)
owins.append(o2)
owins.append(o3)
owins.append(o4)
owins.append(o5)
owins.append(o6)
owins.append(o7)
owins.append(o8)


"""these are the slices that make a tic-tac-toe win"""
wins=[]
w1,w2,w3,w4,w5,w6,w7,w8= [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
wins.append(w1)
wins.append(w2)
wins.append(w3)
wins.append(w4)
wins.append(w5)
wins.append(w6)
wins.append(w7)
wins.append(w8)


tictactoe = []
tictactoe.append(owins)
tictactoe.append(xwins)

set = {0:'X',1:'X',2:'X',3:'O',4:'-',5:'O',6:'O',7:'X',8:'O'} 
set_check = []
x=0
options = {'o':'O','x':'X'}

set_a = []
for s in set:
    for win in wins:
        for w in win:
            # print(set[w])
            if len(set_a) < 3:
                set_a.append(set[w])
            else:
                print(set_a, w, win, s, set)
                set_a = []
            


print(set_a)

for tictac in tictactoe: # 2 loops for xwins and owins lists
    for i, option in enumerate(options): #2 loops for each option x and o
        x = 0
        # print(i)
        for tic in tictac: # 10 loops for each dictlist in xwins and owins
            # print(set_check) 
            ct = 0
            set_check=[]
            x+=1

            # print(f"{options[option]} - player win board {x}: {tic}") # each dictlist in both xwins and owins
            for win in wins:
                ct +=1
                for w in win:
                    # print(w)
                    
                    # print(tic[w])
                    if len(set_check) < 3 and tic[w] != '-':
                        set_check.append(tic[w])
                        # print(set_check)
                        # set_check=[]
                    else:
                        # print(set_check)
                        set_check = []
                if x == ct and len(set_check) == 3:
                    print(set_check,ct,win,tic) 

                # elif ct == 7:
                    # print(set_check,win)
                
                
            
            
            
            
            
            
            
            # for win in wins:
            #     for w in win:
            #         set_check = []
            #         for t in tic: # each index in dictlist
            #             a =0
            #             # print('t:',t)
                        
            #             if len(set_check) < 3:
            #                 a+=1
            #                 set_check.append(tic[w])
            #             else:
            #                 # print(set_check,win[w])
            #                 set_check= []
                
            


           
shell = []
blank = ['X', 'X', 'X', '-', '-', '-', '-', '-', '-']
# x1 = [i for i in enumerate(blank)]


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


