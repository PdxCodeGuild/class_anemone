import pprint

class Game:
    def __init__(self,b={1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'},used={}, score={'X':0,'O':0}):
        self.b = b
        self.used = used
        self.score = score

    def check(self, b):
        self.b = b
        test = list(self.b.values())
        winners = {'h1_2_3':''.join(test[0:3]),'h4_5_6':''.join(test[3:6]),'h6_7_9':''.join(test[6:9]),'v1_4_7':''.join(test[0:7:3]),'v2_5_8':''.join(test[1:8:3]),'v3_6_9':''.join(test[2:9:3]),'d1_5_9':''.join(test[0:9:4]),'d3_5_7':''.join(test[2:7:2])}
        win = ([winners[winner] for winner in winners if winners[winner] == 'XXX' or winners[winner] == 'OOO'])
        spaces = ([space for space in b])
        # print(win,spaces)
        if win == []:
            # print("pass")
            return False    
        else:
            # print("win!") 
            return True 

    def score_board(self, check, token):
        if check ==True:
            self.score[token]+=1
            inst = ''
            session = ''
            return self.score        
    def check_tie(self,used):
        self.used = used
        if len(self.used) == 9:
            return True
        else: 
            return False

class Player:
    def __init__(self, tokens = {0:'-',1:'-'}):
        self.tokens = tokens
        self.tokens[0]=input("player 1: 'x' or 'o' \n\n").upper()
        if self.tokens[0]=='X':
            self.tokens[1] = 'O'
        else:
            self.tokens[1] = 'X' 
        # print(self.tokens)

    def move(self, choice, t):
        self.b = inst.b
        self.used = inst.used
        while self.b[int(choice)] == '-' and inst.check(self.b) == False:
            if not self.b[int(choice)] in self.used:
                self.b[int(choice)]= t
                self.used[int(choice)]=t
                inst.check(self.b)
                return self.b
            else:
                return False
  

#=================================================================================

play = 0
inst = Game()
session = Player() # initializes game, prints board
# print(session)
# assigns 1st play
# er as x or o from user input, then assigns the 2nd player the other option
turn = 1 # counter for 9 turns, if necessary
# game.used = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}
test=''

b = ''
while len(inst.used) < 9 and inst.check(inst.b) == False : # while the number of spaces that have been used are less than 9 (0-8)
    i = 0
    
    # print(f'beginning of game')
    if b == None:
        b = ''
        
    for token in session.tokens: # loops twice to permit change of player for each turn using dictionary list game.tokens 
        # secsondary counter for 9 turns
        if inst.check(inst.b) == True or b == None:
            break
        # print(f"player:{session.tokens[token]}, spaces used: {(([inst.used[g] for g in inst.used]))}")
        b=''
        # print(inst.b)
        while inst.check(inst.b) == False and b == '' and len(inst.used) < 9: # should capture win between for loop
            # print(f'1st while loop - turn {turn} - token {session.tokens[token]}')
            # print(session.tokens)
            # print(inst.check(inst.b))
            if session.move != None and inst.check(inst.b) == False and b != None: # makes sure space is available before assignment
                
                # print(inst.b)
                choice = (input(f"""
                
                {inst.b[7]} | {inst.b[8]} | {inst.b[9]}
                ----------      player: {session.tokens[token]}
                {inst.b[4]} | {inst.b[5]} | {inst.b[6]}
                ----------          turn: {turn} - enter place:
                {inst.b[1]} | {inst.b[2]} | {inst.b[3]}        
    _____________________________________________________
                                                          """))
                t = session.tokens[token]
                b = session.move(choice,t)
                # print(b)
                if b == None:

                    continue
                else:
                    # print(b)
                    turn +=1
                    break

        while len(inst.used) == 9 and inst.check(inst.b) == False:
            # print(f'2nd while loop - turn {turn}')
            if inst.check_tie(inst.used) == True:
                # print("tie! ")
                print(f"""

                {inst.b[7]} | {inst.b[8]} | {inst.b[9]}     Tie!!!!
                ----------      player turn: {t}
                {inst.b[4]} | {inst.b[5]} | {inst.b[6]}
                ----------          turn: {turn-1}
                {inst.b[1]} | {inst.b[2]} | {inst.b[3]}        
    _____________________________________________________""")
                break           
           
        while inst.check(inst.b) == True: 
            # print(f'3rd while loop - turn {turn}')
            # print(inst.b,inst.used)
            print(f"{t} wins!")
            print(f"""

                {b[7]} | {b[8]} | {b[9]}
                ----------      Winner: {t}
                {b[4]} | {b[5]} | {b[6]}
                ----------        turn: {turn-1}
                {b[1]} | {b[2]} | {b[3]}        
                                                    """)
            check = inst.check(b)
            score = inst.score_board(check, t)
            break
