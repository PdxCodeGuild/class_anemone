import random
import math
import string

class Player:  # input for top/middle/bottom then for left/middle/right
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        if self.token == 'x':                # Making the 2 token so player1 can = x and player 2 = o
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
    def __repr__(self):       # taking the board layout as above and joining them with | to create the splits and then \n for new lines
        a = ''
        for x in self.board:
            a += ("|".join(x))
            a += ('\n')
        return a
        
    def move(self, player, spot1):   # Referr to bottom notes Also.. but its checking EACH SPOT

            if spot1 == 'q':
                if self.board[0][0] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[0][0] = player.token

            if spot1 == 'w': 
                if self.board[0][1] != ' ':
                    return print('\nSpot Already in use\n')   
                self.board[0][1] = player.token

            if spot1 == 'e':
                if self.board[0][2] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[0][2] = player.token

            if spot1 == 'r':
                if self.board[1][0] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[1][0] = player.token

            if spot1 == 't':
                if self.board[1][1] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[1][1] = player.token

            if spot1 == 'y':
                if self.board[1][2] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[1][2] = player.token
                
            if spot1 == 'u':
                if self.board[2][0] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[2][0] = player.token
                
            if spot1 == 'i':
                if self.board[2][1] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[2][1] = player.token

            if spot1 == 'o':
                if self.board[2][2] != ' ':
                    return print('\nSpot Already in use\n')
                self.board[2][2] = player.token

    def calc_winner(self):         # determing the winner by checking EACH postion in their respected order.. bottom notes explain daignal

        # side to side winner
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != ' ':
            return self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != ' ':
            return self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != ' ':
            return self.board[1][0]

        # up / down winner
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != ' ':
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != ' ':
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != ' ':
            return self.board[0][2]

        # diagnal winner
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
            return self.board[2][0]
       
    def is_full(self):              # checking the lists in self.board for and ' ' left and if there is none it returns false full a TIE!
        for list in self.board:
            for item in list:
                if item == ' ':
                    return False
        print("BORED IS FULL!\n")
        return True
    
    def is_game_over(self):
        return self.calc_winner or self.is_full  # used as a ref to make checking game over is true or false


        
yes = True   
while yes:          # loop in a loopm so the game wont ALWAYS ask for your name and reset
    game = Game()        # pulling the board class
    game.is_game_over()
    name1 = input('\nenter "player 1" name: ')
    token1 = 'x'
    name2 = input('\nenter "player 2" name: ')
    token2 = 'o'
    player1 = Player(name1,token1)
    player2 = Player(name2,token2)
    
    while True:
        print(f"\n'Q'|'W'|'E'\n'R'|'T'|'Y'\n'U'|'I'|'O'\n")
        choose = input(f'select spot by using letters above "{name1}" |{token1}| Enter spot: ').lower()
        print('\n')
        game.move(player1, choose)
        print(game.__repr__())
        
        if game.calc_winner():
            rematch_1 = input(f'\nWINNER is! {name1}!!!\n \n New game?: ( Y or N ): ') # if this works move to player 2 also
            print(rematch_1)
            break
        if game.is_full():
            rematch_1 = input('TIE GAME.. Re Match?: ( Y or N ):').lower()            # just a loop if they wanna keep playing or not
            break
        
        print(f"\n'Q'|'W'|'E'\n'R'|'T'|'Y'\n'U'|'I'|'O'\n") 
        choose = input(f'select spot by using letters above "{name2}" |{token2}| Enter spot: ').lower()
        print('\n')
        game.move(player2, choose)
        print(game.__repr__())
        if game.calc_winner():
            rematch_1 = input(f'\nWINNER is! {name1}!!!\n \n New game?: ( Y or N ): ') # if this works move to player 2 also
            print(rematch_1)
            break

    yeah = ['yes', 'y', 'yeh', 'sure', 'si']
    no = ['no','nah','nope', 'nay', 'n']
    if rematch_1 in yeah:
        yes = True    
    elif rematch_1 in no:
        print('\nBYE!')
        break
    else:
        print(f'Choose either {yeah} or {no} words')
    



#qto [0,0] [1,1] [2,2] for diagnal

#ute [2,0] [1,1] [0,2] for diagnal

# a = [
# ['Q','W','E'],
# ['R','T','Y'],
# ['U','I','O']
#         ]

# q= a[0][0]
# w= a[0][1]
# e= a[0][2]

# r= a[1][0]
# t= a[1][1]
# y= a[1][2]

# u= a[2][0]
# i= a[2][1]
# o= a[2][2]



# print(e,w,q)
# print(r,t,y)
# print(u,i,o)

# winner = game.calc_winner()
#     if winner:
#         rematch_1 = input(f'\nWINNER is! {name1}!!! New game?: ( Y or N ): ') # if this works move to player 2 also
#         print(rematch_1)
#         break
#     board_full = game.is_full
#     if board_full:
#         print(input('TIE GAME.. Re Match?: ( Y or N ):')).lower()
#         break



       