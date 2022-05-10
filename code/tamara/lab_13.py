class Player: ## this is done for now see commented out code below for name and token input
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game(Player): ## consider going over and seeing if you should make private variables or static methods (may not need them because probaby use them all in the repl loop)
    def __init__(self, board):
        self.board = board
        # self.board = [{0: '_', 1: '_', 2: '_'}, {0: '_', 1: '_', 2: '_'}, {0: '_', 1: '_', 2: '_'}]

    def __repr__(self): ### ask how to move this to multiple lines for easier reading
        return f"{self.board[0].get(0)} | {self.board[0].get(1)} | {self.board[0].get(2)}\n{self.board[1].get(0)} | {self.board[1].get(1)} | {self.board[1].get(2)}\n{self.board[2].get(0)} | {self.board[2].get(1)} | {self.board[2].get(2)}\n"

    def move(self, x, y, player): # places the players given token at a specific x, y coordinate on the board
        self.x = x
        self.y = y
        self.player = player # not sure if this is needed with player_properties variable
                            # try self.name also?
        for x_value in self.board[self.y]: 
            if x_value == self.x: # if the key is equal to the x value input
                self.board[self.y][x_value] = self.token     # check and make sure this works not sure what the player.token variable should be called yet      
                                                                # maybe use self.token or player.token
                                # will use the player_properties variable for the player spot?
                       
            
                                        # will use the user_move input for the x and y
                                        # the user_move input will then have to do an if, elif, else loop to create the x and y variables
                                  # the x and y coordinate will be given by the player
                                  # Top left: 0, 0      [board[0](0)]     Middle left: 0, 1     [board[1](0)]       bottom left: 0, 2       [board[2](0)]
                                  # Top middle: 1, 0    [board[0](1)]     middle middle: 1, 1   [board[1](1)]       bottom middle: 1, 2     [board[2](1)]
                                  # Top right: 2, 0     [board[0](2)]      middle right: 2, 1    [board[1](2)]       bottom right: 2, 2      [board[2](2)]

    def calc_winner(self): # determines what character token/character has won or returns none if noone has

            ## maybe go back thru and get rid of tru/false and instead return none under else
        if self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X':
            return 'X'
        elif self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O':
            return 'O'
        elif self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X':
            return 'X'
        elif self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O':
            return 'O'
        elif self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X':
            return 'X'
        elif self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O':
            return 'O'
        
        elif self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O':
            return 'O'
        elif self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
            return 'X'
        elif self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O':
            return 'O'
        elif self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
            return 'X'
        elif self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O':
            return 'O'
        elif self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
            return 'X'

        elif self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            return 'X'
        elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            return 'O'

        elif self.board[2][0] == 'X' and self.board[1][1] == 'X' and self.board[0][2] == 'X':
            return 'X'
        elif self.board[2][0] == 'O' and self.board[1][1] == 'O' and self.board[0][2] == 'O':
            return 'O'
        
        else:
            return None
        
    def is_full(self): 
        if self.board[0][0] == 'X' or 'O' and  self.board[0][1] == 'X' or 'O' and self.board[0][2] == 'X' or 'O' and self.board[1][0] == 'X' or 'O' and self.board[1][1] == 'X' or 'O' and self.board[1][2] == 'X' or 'O' and self.board[2][0] == 'X' or 'O' and self.board[2][1] == 'X' or 'O' and self.board[2][2] == 'X' or 'O':
            return True
        else:
            return False
        
    def is_game_over(self): # returns True if the board is full or a player has won otherwise returns False
        if self.is_full() == True or self.calc_winner != None:
            return True
        else:
            return False

# ------------ testing the Game class methods

# -------- checking repr method -------

# visual_board = Game(board) ## variable that checks the __repr__ method, the __repr__ method is called automatically when Game class is used?

# print(visual_board)

# ------------ # Repl function

# def main():

board = [{0: '_', 1: '_', 2: '_'}, {0: '_', 1: '_', 2: '_'}, {0: '_', 1: '_', 2: '_'}]
tick_tac_toe = Game(board)

player_1 = input("Player 1 please enter your name: ") # use these for the name variable of the Player class
player_1_token = 'O' # use this for the token property
player_2 = input("Player 2 please enter your name: ")
player_2_token = 'X'
player_1_properties = Player(player_1, player_1_token) #### this variable will be used for the move method in the player property (player_1_properties.name, player_1_properties.token)
player_2_properties = Player(player_2, player_2_token) ### (player_2_properties.name, player_2_properties.token)

while True:
    print(tick_tac_toe)
        
    user_move = input("Your options are: top left, top middle, top right,\nmiddle left, middle middle, middle right,\nbottom left, bottom middle, bottom right\nWhere would you like to put your token? ").lower()
    if user_move == 'top left' or 'middle left' or 'bottom left':
        x = 0
        if user_move == 'top left' or 'top middle' or 'top right':
            y = 0
        elif user_move == 'middle left' or 'middle middle' or 'middle right':
            y = 1
        elif user_move == 'bottom left' or 'bottom middle' or 'bottom right':
            y = 2
    elif user_move == 'top middle' or 'middle middle' or 'bottom middle':
        x = 1
        if user_move == 'top left' or 'top middle' or 'top right':
            y = 0
        elif user_move == 'middle left' or 'middle middle' or 'middle right':
            y = 1
        elif user_move == 'bottom left' or 'bottom middle' or 'bottom right':
            y = 2
    elif user_move == 'top right' or 'middle right' or 'bottom right':
        x = 2
        if user_move == 'top left' or 'top middle' or 'top right':
            y = 0
        elif user_move == 'middle left' or 'middle middle' or 'middle right':
            y = 1
        elif user_move == 'bottom left' or 'bottom middle' or 'bottom right':
            y = 2
        
    tick_tac_toe.move(x, y, player_1_properties)

    if tick_tac_toe.is_game_over() == True:
        print(tick_tac_toe)
        if tick_tac_toe.calc_winner() != None:
            print(f"Congratulations there are 3 {tick_tac_toe.calc_winner()}'s in a row! You're a winner!")
            break
        
    print(tick_tac_toe)
        
    user_move = input("Your options are:\ntop left, top middle, top right,\nmiddle left, middle middle, middle right,\nbottom left, bottom middle, bottom right\n\nWhere would you like to put your token? ").lower()
    if user_move == 'top left' or 'middle left' or 'bottom left':
        x = 0
        if user_move == 'top left' or 'top middle' or 'top right':
            y = 0
        elif user_move == 'middle left' or 'middle middle' or 'middle right':
            y = 1
        elif user_move == 'bottom left' or 'bottom middle' or 'bottom right':
            y = 2
    elif user_move == 'top middle' or 'middle middle' or 'bottom middle':
        x = 1
        if user_move == 'top left' or 'top middle' or 'top right':
            y = 0
        elif user_move == 'middle left' or 'middle middle' or 'middle right':
            y = 1
        elif user_move == 'bottom left' or 'bottom middle' or 'bottom right':
            y = 2
    elif user_move == 'top right' or 'middle right' or 'bottom right':
        x = 2
        if user_move == 'top left' or 'top middle' or 'top right':
            y = 0
        elif user_move == 'middle left' or 'middle middle' or 'middle right':
            y = 1
        elif user_move == 'bottom left' or 'bottom middle' or 'bottom right':
            y = 2
    

    tick_tac_toe.move(x, y, player_2_properties)

    if tick_tac_toe.is_game_over() == True:
        print(tick_tac_toe)
        if tick_tac_toe.calc_winner() != None:
            print(f"Congratulations there are 3 {tick_tac_toe.calc_winner()}'s in a row! You're a winner!")
                
            break

########### LINE 21 error self.token
################### how do I get the player class data into the game class? how do I move back and forth between the players via a loop
##################### without reasking for their names?