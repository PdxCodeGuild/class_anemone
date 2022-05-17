class Player: 
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game(Player): 
    def __init__(self, board):
        self.board = board

    def __repr__(self): ### ask how to move this to multiple lines for easier reading
        return f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}\n"

    def move(self, x, y, player): # places the players given token at a specific x, y coordinate on the board
        self.x = x
        self.y = y
        self.player = player 

        self.board[self.y][self.x] = player.token

    def calc_winner(self): # determines what character token/character has won or returns none if noone has

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
        return self.board[0][0] != '_' and self.board[0][1] != '_' and self.board[0][2] != '_' and self.board[1][0] != '_' and self.board[1][1] != '_' and self.board[1][2] != '_' and self.board[2][0] != '_' and self.board[2][1] != '_' and self.board[2][2] != '_'
        
    def is_game_over(self): # returns True if the board is full or a player has won otherwise returns False
        return self.is_full() == True or self.calc_winner != None

def main():

    board = [{0: '_', 1: '_', 2: '_'}, {0: '_', 1: '_', 2: '_'}, {0: '_', 1: '_', 2: '_'}]
    tick_tac_toe = Game(board) # create an instance of the board class

    player_1 = input("Player 1 please enter your name: ") # use these for the name variable of the Player class
    player_1_token = 'O' # use this for the token property
    player_2 = input("Player 2 please enter your name: ")
    player_2_token = 'X'
    player_1_properties = Player(player_1, player_1_token) #### this variable will be used for the move method in the player property (player_1_properties.name, player_1_properties.token)
    player_2_properties = Player(player_2, player_2_token) ### (player_2_properties.name, player_2_properties.token)
            # these are the two instances of the player class
    player_turn_counter = 0

    while True:
        player_turn_counter += 1

        if player_turn_counter % 2 != 0:
            player = player_1_properties
        else:
            player = player_2_properties

        print(f'\nIt\'s your turn {player.name}!\n')

        print(tick_tac_toe)

        while True:
            user_move = input("\nYour options are:\ntop left, top middle, top right,\nmiddle left, middle middle, middle right,\nbottom left, bottom middle, bottom right\n\nWhere would you like to put your token? ").lower()
            if user_move == 'top left':
                if tick_tac_toe.board[0][0] == 'X' or tick_tac_toe.board[0][0] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 0
                    y = 0
                    break
            elif user_move == 'top middle':
                if tick_tac_toe.board[0][1] == 'X' or tick_tac_toe.board[0][1] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 1
                    y = 0
                    break
            elif user_move == 'top right':
                if tick_tac_toe.board[0][2] == 'X' or tick_tac_toe.board[0][2] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 2 
                    y = 0
                    break
            elif user_move == 'middle left':
                if tick_tac_toe.board[1][0] == 'X' or tick_tac_toe.board[1][0] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 0
                    y = 1
                    break
            elif user_move == 'middle middle':
                if tick_tac_toe.board[1][1] == 'X' or tick_tac_toe.board[1][1] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 1
                    y = 1
                    break
            elif user_move == 'middle right':
                if tick_tac_toe.board[1][2] == 'X' or tick_tac_toe.board[1][2] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 2
                    y = 1
                    break
            elif user_move == 'bottom left':
                if tick_tac_toe.board[2][0] == 'X' or tick_tac_toe.board[2][0] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 0
                    y = 2
                    break
            elif user_move == 'bottom middle':
                if tick_tac_toe.board[2][1] == 'X' or tick_tac_toe.board[2][1] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 1
                    y = 2
                    break
            elif user_move == 'bottom right':
                if tick_tac_toe.board[2][2] == 'X' or tick_tac_toe.board[2][2] == 'O':
                    print('\nThat position is already full! Please try again.')
                else:
                    x = 2
                    y = 2
                    break
            else: 
                print("\nThat was not a valid position.")
        
        tick_tac_toe.move(x, y, player)

        if tick_tac_toe.is_game_over() == True:
            if tick_tac_toe.calc_winner() != None:
                print(f"\nCongratulations {player.name} you won!!\n")
                print(tick_tac_toe)
                break
            elif tick_tac_toe.is_full() == True:
                print("\nOh to bad, looks like a draw!\n")
                print(tick_tac_toe)
                break
    
main()