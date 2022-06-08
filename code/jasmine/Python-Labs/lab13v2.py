## Tic Tac Toe Game Lab 13

from audioop import getsample


#initialize the player and token
class Player:
    def __init__(self, player, token):  
        self.player = player
        self.token = token

## empty game board
class Game:
    def __init__(self): 
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',                                         
                      '1': ' ', '2': ' ', '3': ' '}
    
    ## return empty game board
    def __repr__(self): 
        tac_board = f"{self.board['7']}|{self.board['8']}|{self.board['9']}\n{self.board['4']}|{self.board['5']}|{self.board['6']}\n{self.board['1']}|{self.board['2']}|{self.board['3']}"
        return tac_board
    

    ## create player token
    def move(self, key, player): 
        self.board[key] = player.token
    

    ## match token with key in board to find winner
    def calc_winner(self, player):  
        if self.board['7'] == self.board['8'] == self.board['9'] == player.token:
            return player.token
        elif self.board['4'] == self.board['5'] == self.board['6'] == player.token:
            return player.token 
        elif self.board['1'] == self.board['2'] == self.board['3'] == player.token:
            return player.token 
        elif self.board['7'] == self.board['5'] == self.board['3'] == player.token:
            return player.token
        elif self.board['1'] == self.board['5'] == self.board['9'] == player.token:
            return player.token
        elif self.board['7'] == self.board['4'] == self.board['1'] == player.token:
            return player.token
        elif self.board['8'] == self.board['5'] == self.board['2'] == player.token:
            return player.token 
        elif self.board['9'] == self.board['6'] == self.board['3'] == player.token:
            return player.token 
        else:
            return None

    ## board is full function
    def is_full(self):  
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True

## if the board is full.. end the game
    def game_over(self, player):  
        if self.calc_winner(player):
            return True
        elif self.is_full():
            return True
        else:
            return False


## begin the game in main
def main(): 
    print("Welcome to tictactoe!")

    # Create players
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    # Create tokens
    player1_token = "X"
    player2_token = "O"

    player_1 = Player(player_1, player1_token)
    player_2 = Player(player_2, player2_token)
        
    # create the instance of the game and board
    game = Game()
    # board display
    game.__repr__()

    while True:

        ## player picks key on board to move 
        move_one = input(f"{player_1.player} pick your next move: ")
        game.move(move_one, player_1)
        print(game.__repr__())

        if game.game_over(player_1) == True:
            if game.is_full() == True:
                print("Tie Game")
            elif game.calc_winner(player_1):
                print(f"{player_1.player} wins!")
            break


        move_two = input(f"{player_2.player} pick your next move: ")
        game.move(move_two, player_2)
        print(game.__repr__())

        if game.game_over(player_2) == True:
            if game.is_full() == True:
                print("It's a Tie!")
            elif game.calc_winner(player_2):
                print(f"{player_2.player} is the winner!")
            break

main()



