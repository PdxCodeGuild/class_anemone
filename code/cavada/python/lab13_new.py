


class TicTacToe:
    def __init__(self):
        self.index = 0
        self.counter = 0
        self.used = []
        self.token = {'x':'X', 'o':'O'}
        self.s = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-'}
        self.board = f"""
                                TIC-TAC-TOE
                    ___________________________________________
                    |                                           |
                    |                x  - a x i s               |
                    |        ___________________________________|   Current Player:  
                    |       |                                   |       {self.token[self.index]}  
                    |       |         1)       2)       3)      |   
                    |   y   |             |         |           |    Turn:{self.counter}
                    |       |  1)     {self.s[0]}   |    {self.s[1]}    |   {self.s[2]}\t    |
                    |   -   |     ________|_________|_________  |
                    |       |             |         |           |
                    |   a   |  2)     {self.s[3]}   |    {self.s[4]}    |   {self.s[5]}\t    |
                    |   x   |     ________|_________|_________  |
                    |   i   |             |         |           |
                    |   s   |  3)     {self.s[6]}   |    {self.s[7]}    |   {self.s[8]}\t    |
                    |       |             |         |           |
                    |_______|___________________________________|                        
                """
        

class Player(TicTacToe):
    def __init__(self, name, token):
        self.name = name
        self.token = token
    pass

class Board(TicTacToe):
    def __init__(self, s, board):
        self.s = s
        self.board = board
        
         
        
        pass

class Game(TicTacToe):
    def __init__(self, board, used, s):
        self.board = board
        self.used = used
        self.s = s
        
    def __repr__(self):
        print(self.board)
        print(self.s)
        print(self.used)
    
    def move(self, x_pos, y_pos, token):
        __repr__(self)


        pass

    def calc_winner(self):
        pass

    def is_full(self):
        pass

    def is_game_over(self):
        pass
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
                msg = f"winner: {options['o']}"
                x+=1
                break
            elif set == xwin and set !=owin:
                msg = f"winner: {options['x']}"
                x+=1
                break
            elif set != xwin or set != owin:
                msg = ''
                # print("none")
                x+=10
    return msg






while True:
 play = input("play? 'y' or 'n' ")
 while play == "y":


  b_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
  token = {'x':'X', 'o':"O"} 
  b_dict = {7:'-',8:'-',9:'-',4:'-',5:'-',6:'-',1:'-',2:'-',3:'-'}
  b_list_ref = [0,1,2,3,4,5,6,7,8]
  counter = 1
  player = input("choose player 1: 'x' or 'o' ")
  used = {}
  win = check(b_dict)
  trip = 0   
  while trip == 0:  
    breakout = [7,8,9,4,5,6,1,2,3]
    while True and counter <= 8 and win == '':
        # print(b_list)``
        choice = input(f"""
                                    
                                 _________________________________
                                |                                 |
                                |           TIC-TAC-TOE           |    Current Player:
            [use to make move]  |_________________________________|    ___________  
               _____________    |                                 |         
              | N U M P A D |   |                                 |      {token[player]}
              |    K E Y    |   |           |         |           |    
             [use to make move] |       {b_dict[7]}   |    {b_dict[8]}    |   {b_dict[9]}       |    _____
              ---------------   |   ________|_________|_________  |  
                 7 | 8 | 9      |           |         |           |    Turn:  
                -----------     |       {b_dict[4]}   |    {b_dict[5]}    |   {b_dict[6]}       |
                 4 | 5 | 6      |   ________|_________|_________  |         {counter}
                -----------     |           |         |           |
                 1 | 2 | 3      |       {b_dict[1]}   |    {b_dict[2]}    |   {b_dict[3]}       |
                                |           |         |           |   Enter
                                |_________________________________|   choice:              
               
                                                                                """)  
        win = check(b_dict)
        # print(b_list)                                                                
        # print(b_list[breakout.index(int(choice))])    
        if b_list[breakout.index(int(choice))] == '-':
            b_dict[int(choice)]=token[player]
            used[int(choice)]=token[player]
            b_list = [b_dict[b] for b in b_dict]
            if player == 'x':
                player = 'o'
                counter+=1
                # print(b_dict)
                win = check(b_dict)
            else:
                player = 'x'    
                counter+=1
                # print(b_dict)
                win = check(b_dict)
            # win = check(b_dict)
        else:
            if player == 'x':
                player = 'x'
                # print(b_dict)
                
            else:
                player = 'o'
                # print(b_dict)
            break    
        
        if check(b_dict) != '':
            # print(b_dict)
            break    
                
    
    
    print(token[player])               
    print(player)               
    print(choice)
        # choice = input(f"enter space to place {token[player]}")
    if win == 'win':
        trip+=1
        # print('trip')
        break       
    else:
        # print("wtf??")
        break
  print(f"""end
                                     
                                  _________________________________
                                 |                                 |
                                 |           TIC-TAC-TOE           |    
             [use to make move]  |_________________________________|     
                _____________    |                                 |       {win}  
               | N U M P A D |   |                                 |   _____________________
               |    K E Y    |   |           |         |           |     
              [use to make move] |       {b_dict[7]}   |    {b_dict[8]}    |   {b_dict[9]}       |     Turn:    {counter-1}   
               ---------------   |   ________|_________|_________  |         
                  7 | 8 | 9      |           |         |           |         G A M E   O V E R
                 -----------     |       {b_dict[4]}   |    {b_dict[5]}    |   {b_dict[6]}       |          
                  4 | 5 | 6      |   ________|_________|_________  |
                 -----------     |           |         |           |
                  1 | 2 | 3      |       {b_dict[1]}   |    {b_dict[2]}    |   {b_dict[3]}       |
                                 |           |         |           |   
                                 |_________________________________|    این فارسی""")
  print("after game over")
  play = ''  
  break       
 

