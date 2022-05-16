class TicTacToe:
    def __init__(self, wins):
        self.wins = wins
        self.board = f"""
        {b[7]} | {b[8]} | {b[9]} 
        ---------
        {b[4]} | {b[5]} | {b[6]} 
        ---------
        {b[1]} | {b[2]} | {b[3]} 
        """
        self.p1 = ''
        self.p2 = ''
        print(self.board)

    def check(self,b):
        self.b = b
        self.x = 0
        self.winners = ['OOO', 'XXX']
        # self.wins = TicTacToe.wins
        self.container = []
        self.start,self.stop,self.step,self.inc = -2,1,1,3
        for i in range(1,4): # loops 3 times to get 3 horiz wins
            self.start+=self.inc # 4,7,1 (4,5,6)
            self.stop+=self.inc 
            self.bin = {}
            for i in range(self.start,self.stop,self.step): # 1,4,1 (1,2,3)
                self.t = self.b[i]
                self.bin[i]=self.t   
            self.container.append(self.bin)
        self.start,self.stop,self.step,self.inc = 0,7,3,1
        for i in range(1,4): # loops 3 times to get 
            self.start+=1
            self.stop+=1
            bin = {}
            for i in range(self.start,self.stop,self.step):
                self.t = b[i]
                bin[i]=self.t
            self.container.append(bin)
        self.bin = {}
        for i in range(1,10,4): 
            self.t = self.b[i]
            self.bin[i]=self.t
        self.container.append(self.bin)
        self.bin = {}
        for i in range(3,8,2): 
            self.t = self.b[i]
            self.bin[i]=self.t
        self.container.append(bin)
        self.string_list = []
        for cont in self.container:
            self.string = ''
            for c in cont:
                self.string += cont[c]   
            self.string_list.append(self.string)
        for self.string in self.string_list:
            for winner in self.winners:
                if self.string in winner:
                    self.x += 1
                else:
                    self.x += 0
        if self.x > 0:
            return True
        else:
            return False
        
class Game(TicTacToe):
    def __init__(self, tokens = {0:'-', 1:'-'}, b = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}, used = {}):
        self.tokens = tokens
        self.wins = wins
        self.b = b
        self.used = used
        self.tokens[0]=input("player 1: 'x' or 'o' \n\n").upper()
        if self.tokens[0]=='X':
            self.tokens[1] = 'O'
        else:
            self.tokens[1] = 'X' 

    def move(self, choice, tok):
        self.b = game.b
        while game.b[choice] == '-' and game.check(game.b)==False:
            if not game.b[choice] in game.used:
                game.b[choice]= tok
            # game.used.update({game.b[choice]:tok})
                game.used[choice]=tok
                # print(game.used)
                game.check(game.b)
                # print(game.b)
                # print(game.used)
                return game.b
            else:
                return False
        return game.b
    
    def declare_win(self, wins, tok):
        # self.token = game.token
        # self.wins = wins
        for win in wins:
            if tok == win:
                win[tok]+=1
        return wins
        

#=================================================================================
x_score,o_score = 0,0

# while input("Play TicTacToe? 'n' to quit ") != 'n':
again = 'y'
wins = {'X':x_score,'O':o_score}
# print(game.tokens)
while input('Play Tic Tac Toe!' ) != 'n' and again == 'y' and again != 'exit':
    
    b = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}
    print("wins:")
    for win in wins:
        print(f"\t{win} - {wins[win]}")
    play = 0
    session = TicTacToe(wins)
    game = Game()
    turn = 0
    # for win in wins:
    #     for w in win:
    #         print(f"win: {wins[win]}")
    while game.check(b) != True and len(game.used) < 9:
        
        if game.check(b) == True:
            break
        else:
            for token in game.tokens:
                print(game.used)
                print(game.check(b))
                if game.check(b) != False:
                    # game.declare_win(b)
                    break
                
                elif game.move != False:
                    choice = int(input(f"""

        {b[7]} | {b[8]} | {b[9]}
        ----------      player: {game.tokens[token]}
        {b[4]} | {b[5]} | {b[6]}
        ----------          turn: {turn} - enter place:
        {b[1]} | {b[2]} | {b[3]}        
                                                        """))
                    tok = game.tokens[token]
                    b = game.move(choice,tok)
                    # print(b)
                    turn +=1
                    
                elif len(game.used)==9 and game.check(b) == True:
                    again = input(f"{token} WON!, play again? 'y' or 'exit' to quit ")
                    # print(f'for token in game.tokens: 2nd elif')
                    break
                else:
                    break
                            # print(x, chec)
                print(f"Turn:{turn}")
                game.check(b)
            # print(f'after else')
            # print(game.used)
            # print(wins)
    if game.check(b)==True:
        wins[game.tokens[token]]+=1
        # print(wins[game.tokens[token]])
        game.used = {}
        print(tok)
        print(game.declare_win(wins, tok))
        # print(wins)
        # wins[token]+=1  
    elif len(game.used) == 9:
        print('tie!')
        break
    print(game.used)
# def check(b):
#     x =0
#     wins = ['OOO', 'XXX']
#     container = []
#     start,stop,step,inc = -2,1,1,3
#     for i in range(1,4): # loops 3 times to get 3 horiz wins
#         start+=inc # 4,7,1 (4,5,6)
#         stop+=inc 
#         bin = {}
#         for i in range(start,stop,step): # 1,4,1 (1,2,3)
#             t = b[i]
#             bin[i]=t   
#         container.append(bin)
#     start,stop,step,inc = 0,7,3,1
#     for i in range(1,4): # loops 3 times to get 
#         start+=1
#         stop+=1
#         bin = {}
#         for i in range(start,stop,step):
#             t = b[i]
#             bin[i]=t
#         container.append(bin)
#     bin = {}
#     for i in range(1,10,4): 
#         t = b[i]
#         bin[i]=t
#     container.append(bin)
#     bin = {}
#     for i in range(3,8,2): 
#         t = b[i]
#         bin[i]=t
#     container.append(bin)
#     string_list = []
#     for cont in container:
#         string = ''
#         for c in cont:
#             string += cont[c]   
#         string_list.append(string)
#     for string in string_list:
#         for win in wins:
#             if string in win:
#                 x += 1
#             else:
#                 x = x
#     if x > 0:
#         return True
#     else:
#         return False


# def add_win(player):
#     wins[player]+=1
#     return wins

# string=check(b)
# print(string)

# b = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}

# x = input("Tic Tac Toe Game - enter 'n' to exit \n\n")
# # """player assignment"""
# while x != 'n':
#     b = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}

#     used = {}
#     players = {0:tokens[tokens.index(input("player 1: 'x' or 'o' \n\n").upper())],1:''}
#     if players[0]=='X':
#         players[1] = 'O'
#     else:
#         players[1] = 'X'
#     # print(players)    
#     x = 0
#     while check(b) == False or x < 9 :
#         for i, player in enumerate(players) :
#             if check(b)==False:
#                 choice = int(input(f"""
#                 \n{b[7]} | {b[8]} | {b[9]}
#                 \n---------\tplayer: {players[i]}
#                 \n{b[4]} | {b[5]} | {b[6]}
#                 \n---------\t{used}\tplay: {x} - enter place:
#                 \n{b[1]} | {b[2]} | {b[3]} 
            
#              """))
                
#                 if check(b)==True:
#                     break
#             while b[choice] == '-' and check(b)==False:
#                 b[choice]= players[i]
#                 used.update({b[choice]:players[i]})
#                 chec = check(b)
#                 # print(b)
#                 if len(used)==9 or chec == True:
#                     print(f"{players[i]} won!")
#                     input(f"\n{b[7]} | {b[8]} | {b[9]}\n---------\n{b[4]} | {b[5]} | {b[6]}\n---------\n{b[1]} | {b[2]} | {b[3]}\n\n Winnner {players[i]}\n{used}\n play: {x} - press enter to see player board stats... ")
#                     # print(b,chec, players[i],used,x)
#                     wins[players[i]]+=1
#                     print(wins)
#                     for i, win in enumerate(wins):
#                         print(wins[player])            
#                 else:
#                     x += 1
#                     # print(x, chec)
#                     break 
#             check(b)       
#             if check(b)== True:
#                 break

#         check(b)
#         if check(b)== True:
#             break    
#         else:
#             "tie!"


        # print(p1, p2, board)


# b[input('space')]=p1


# print(board)
# b[7]='X'
# print(b[7])
# b[int(input('space: '))]=p[0]
# print(board)

# print(board)




