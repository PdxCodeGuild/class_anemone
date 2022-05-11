# Lab13 - Tic Tac Toe
# Fran Kappes

class Player():
    # Define initialization method
    def __init__(self, player_name, token): 
        self.player_name = player_name
        self.token = token

class Game():
    # Define initialization method
    def __init__(self): 
        self.board = []

    # Define method that returns a string representation of the game board
    def __repr__(self):
        pass


    # Define token move method
    def move(self, x, y, player):
        print('moving: ',player)


    # Define calculate winner method to see if anyone has won yet or not
    def calc_winner(self):
        pass


    # Define board status method that determines if board is full
    def is_full(self):
        pass



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

    player1_name = 'Bob'
    player1_token = 'x'
    player2_name = 'Mary'
    player2_token = 'o'


    player1 = Player(player1_name, player1_token) # create an instance of the Player class for player 1
    player2 = Player(player2_name, player2_token) # create an instance of the Player class for player 2
    print("player1: ",player1.player_name)
    print("player1: ",player1.token)
    print("player2: ",player2.player_name)
    print("player2: ",player2.token)

    game = Game() # create an instance of the Game class
    print('instantiated game')

    # Display empty game board
    game.__repr__()

    while game.is_game_over() is False:   
        # Prompt Player 1 to make their move
        command1 = input('Player 1 make your move. Enter coordinates (x,y) for where you want your token to go. Upper left corner is (0,0): ')
       
        # Convert (x,y) to x and y
        # x = 
        # y = 

        # Call move function
        # game.move(self, x, y, player1)  # pass player1 object in
       
        # See if game is over (win or draw)
        game.is_game_over()

        command2 = input('Player 2 make your move. Enter coordinates (x,y) for where you want your token to go. Upper left corner is (0,0): ')

       

main()
