# Lab13 - Tic Tac Toe
# Fran Kappes

# Define Player and Game classes


class Player():
    # Define initialization method
    def __init__(self, player_name, token): 
        self.player_name = player_name
        self.token = token

class Game():
    # Define initialization method
    def __init__(self, board=[['*','x','x'],['*','*','x'],['x','x','*']]): 
        self.board = board


    # Define method that returns a string representation of the game board
    def __repr__(self):
    
        for row in self.board:
            for column in row:
                print(column,"|",end = " ")
            print()

        return self.board


    # Define token move method
    def move(self, x, y, player):
        print('moving... ',player.player_name)        ### TEST

        self.board[int(x)][int(y)] = player.token

   
    # Define calculate winner method to see if anyone has won yet or not
    def calc_winner(self):
       
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != '*':
            print('Winner!')
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != '*':
            print('Winner!')
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != '*':
            print('Winner!')
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != '*':
            print('Winner!')
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != '*':
            print('Winner!')
            # print(self.board[0][1], ' wins!')
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != '*':
            print('Winner!')
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '*':
            print('Winner!')
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '*':
            print('Winner!')
            # print(self.board[0][2], ' diagonal wins!')
            return True
        else:
            print('no winner')
            return False


    # Define board status method that determines if board is full
    def is_full(self):

        for row in self.board:
            # print('row: ',row)        ### TEST
            for column in row:
                #print('column: ',column)    ### TEST
                if column == '*':
                    #print('before return False')   ### TEST
                    return False
        #print('before return True')        ### TEST
        return True


    # Define game status method that determines if game is over yet
    def is_game_over(self):

        if calc_winner():
            return True
        else:           # no winner yet; check to see if board is full (draw)
            if is_full():
                return True
            else:
                return False
           


# Define main function that manages game play
def main():

    print('Welcome to Tic Tac Toe!')

    # Collect name and token for both players
    # player1_name = input('Player 1 enter your name: ')
    # player1_token = input('Player 1 enter your token, "x" or "o": ')
    # player2_name = input('Player 2 enter your name: ')
    # player2_token = input('Player 2 enter your token, "x" or "o": ')

    player1_name = 'Bob'      ### TEST
    player1_token = 'x'       ### TEST
    player2_name = 'Mary'     ### TEST
    player2_token = 'o'       ### TEST

    player1 = Player(player1_name, player1_token) # create an instance of the Player class for player 1
    player2 = Player(player2_name, player2_token) # create an instance of the Player class for player 2
    # print("player1: ",player1.player_name)      ### TEST
    # print("player1: ",player1.token)            ### TEST
    # print("player2: ",player2.player_name)      ### TEST
    # print("player2: ",player2.token)            ### TEST

    game = Game() # create an instance of the Game class
    #print('instantiated game')      ### TEST

    # Display game board
    board = game.__repr__()
    #print(board)

    print('Before while loop')
    print(game.is_full())

    # while game.is_game_over() is False:   
    while game.is_full() is False:   ### FOR TESTING; REPLACE THIS WITH is_game_over()
        # Prompt Player 1 to make their move
        p1_x = input(f"\n{player1.player_name}, begin your move. Enter the X-coordinate for where you want your token to go. Upper left corner is (0,0): ")
        p1_y = input(f"{player1.player_name}, finish your move. Enter the Y-coordinate for where you want your token to go. Upper left corner is (0,0): ")
        
        print('p1_x: ',(p1_x))
        print('p1_y: ',(p1_y))
        
        # Call move function
        game.move(p1_x, p1_y, player1)  # pass player1 object in
        
        # Display game board
        board = game.__repr__()

        # Did player 2 win?
        if game.calc_winner():
            print(player1.player_name,' wins!')
            exit

        # See if it's a draw
        if game.is_full():
            print('Draw')
            exit

        # Prompt Player 2 to make their move
        p2_x = input(f"\n{player2.player_name}, make your X move. Enter the x-coordinate for where you want your token to go. Upper left corner is (0,0): ")
        p2_y = input(f"{player2.player_name}, make your Y move. Enter the y-coordinate for where you want your token to go. Upper left corner is (0,0): ")
        
        print('p2_x: ',(p2_x))
        print('p2_y: ',(p2_y))
        
        # Call move function
        game.move(p2_x, p2_y, player2)  # pass player2 object in

        # Display game board
        board = game.__repr__()

        # Did player 2 win?
        if game.calc_winner():
            print(player2.player_name,' wins!')
            exit
    
        # See if it's a draw
        if game.is_full():
            print('Draw')
            exit

# Call main function
main()
