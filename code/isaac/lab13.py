'''Tic-Tac-Toe'''
# Create the Player and Game classes
class Player:
    def __init__(self, player, token):  # build the player and token base
        self.player = player
        self.token = token


class Game:
    def __init__(self):  # construct the board
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',                                         
                      '1': ' ', '2': ' ', '3': ' '}
    
    def __repr__(self):  # this function will display the game board
        tac_board = f"{self.board['7']}|{self.board['8']}|{self.board['9']}\n{self.board['4']}|{self.board['5']}|{self.board['6']}\n{self.board['1']}|{self.board['2']}|{self.board['3']}"
        return tac_board
    
    def move(self, key, player): # define the move the player will make on the board
        self.board[key] = player.token
    
    def calc_winner(self, player):  # calculate the winner if the move[key] matches
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

    def is_full(self):  # define when the board is full
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True

    def game_over(self, player):  # define when the game will be over whether a player matches three or the board is full
        if self.calc_winner(player):
            return True
        elif self.is_full():
            return True
        else:
            return False


def main():  # define the main game
    print("Welcome to tic-tac-toe!")

    # Create players
    player_one_name = input("Player 1 enter your name: ")
    player_two_name = input("Player 2 enter your name: ")
    # Create tokens
    player_one_token = "X"
    player_two_token = "O"

    player_1 = Player(player_one_name, player_one_token)
    player_2 = Player(player_two_name, player_two_token)
        
    # create the instance of the game and board
    full_game = Game()
    # board display
    full_game.__repr__()

    while True:

        # create move variable
        move_one = input(f"{player_1.player} enter your move: ")
        full_game.move(move_one, player_1)
        print(full_game.__repr__())

        if full_game.game_over(player_1) == True:
            if full_game.is_full() == True:
                print("Tie Game")
            elif full_game.calc_winner(player_1):
                print(f"{player_1.player} wins!")
            break


        move_two = input(f"{player_2.player} enter your move: ")
        full_game.move(move_two, player_2)
        print(full_game.__repr__())

        if full_game.game_over(player_2) == True:
            if full_game.is_full() == True:
                print("Tie Game")
            elif full_game.calc_winner(player_2):
                print(f"{player_2.player} wins!")
            break

main()














# full_game.move("7", player_1)
# full_game.move("5", player_2)


