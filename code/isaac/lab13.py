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
    
    def calc_winner(self):  # calculate the winner if the move[key] matches
        if self.board['7'] == self.board['8'] == self.board['9'] and self.board != ' ':
            return True
        elif self.board['4'] == self.board['5'] == self.board['6'] and self.board != ' ':
            return True 
        elif self.board['1'] == self.board['2'] == self.board['3'] and self.board != ' ':
            return True 
        elif self.board['7'] == self.board['5'] == self.board['3'] and self.board != ' ':
            return True
        elif self.board['1'] == self.board['5'] == self.board['9'] and self.board != ' ':
            return True
        elif self.board['7'] == self.board['4'] == self.board['1'] and self.board != ' ':
            return True
        elif self.board['8'] == self.board['5'] == self.board['2'] and self.board != ' ':
            return True 
        elif self.board['9'] == self.board['6'] == self.board['3'] and self.board != ' ':
            return True 
        else:
            return False

    def is_full(self):  # define when the board is full
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True

    def game_over(self):  # define when the game will be over whether a player matches three or the board is full
        if self.calc_winner():
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
    
    while full_game.game_over() is False:  # while loop to keep the game playing
        x_move = input(f"{player_one_name} enter your move using the numpad or numbers key (1-9): ")

        # call the move function
        full_game.move(x_move, player_1)
        # display the board
        full_game.__repr__()

        # call the winner if the winner matches three in a row
        if full_game.calc_winner():
            print(f"Player {player_1} wins!")
            break
        
        # call the game is full function if board is full with no winners
        if full_game.is_full():
            print("Game over, no winners")
            break

        o_move = input(f"{player_two_name} enter your move using the numpad or numbers key (1-9): ")

        # call player 2 move
        full_game.move(o_move, player_2)
        
        # Display game board
        full_game.__repr__()

        if full_game.calc_winner():
            print(f"Player {player_2} wins!")
            break

        if full_game.is_full():
            print("Game over, no winners")
            break

main()














# full_game.move("7", player_1)
# full_game.move("5", player_2)


