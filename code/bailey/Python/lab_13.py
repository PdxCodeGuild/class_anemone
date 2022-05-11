'''
Class anemone
Lab 13
Bailey Baker
'''

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        # creates 3x3 board for play
        self.board = [[' 'for i in range(3)] for j in range(3)]

    def __repr__(self):
        # changes board and returns new board to be printed
        show = ''
        for i in self.board:
            show += '|'.join(i)
            show += '\n'
        return show
    
    def move(self, x, y, player):
        # checks for valid movement
        if x not in range(0, 3) or y not in range(0, 3):
            print ("Invalid position")
            return False
        elif self.board[y][x] != ' ':
            print("Invalid position")
            return False
        # sets board space equal to players token upon recieving valid input
        else: 
            self.board[y][x] = player
            return True

    def calc_winner(self):
        # horizontal check
        for i in range(3):              
            horizontal = self.board[i]
            if all(item == horizontal[0] and item != ' ' for item in horizontal):
                if horizontal[i] == 'X':
                    return player_1
                elif horizontal[i] == 'O':
                    return player_2

            # vertical check
            vertical = [self.board[j][i] for j in range(3)]         
            if all(item == vertical[0] and item != ' ' for item in vertical):
                if vertical[0] == 'X':
                    return player_1
                if vertical[0] == 'O':
                    return player_2
    
        # Diagonal check
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[1][1] != ' ':   
            if self.board[0][0] == 'X':
                return player_1
            if self.board[0][0] == 'O':
                return player_2

        # Diagonal check  
        if (self.board[2][0] == self.board[1][1] == self.board[0][2]) and self.board[1][1] != ' ':      
            if self.board[2][0] == 'X':
                return player_1
            if self.board[2][0] == 'O':
                return player_2

    def is_full(self):
        # check for any black spaces on board
        for i in self.board:
            if any(check==' ' for check in i):
                return False
        return True

    def is_game_over(self):
        #check if board is full or if anyone has three in a row by calling other methods
        if self.is_full() == True:
            return True
        elif self.calc_winner() == player_1 or self.calc_winner() == player_2:
            return True
        else:
            return False

player_1 = Player(input("Enter name: "), 'X')
player_2 = Player(input("Enter name: "), 'O')


# REPL loop, ends if user chooses to after each game.
while True:
    play = Game()
    print(f'\n\n{Game.__repr__(play)}')
    
    # second loop to be broken out of when game is over
    while True:
        # loop for player_1's move, breaks when they input a valid location
        while True:
            x = int(input(f"{player_1.name} Enter your move's x coordinate: ")) - 1
            y = int(input(f"{player_1.name} Enter your move's y coordinate: ")) - 1
            test = Game.move(play, x, y, player_1.token)
            if test == False:
                print("Try again.")
            elif test == True:
                break
        # shows new board after player_1's move
        print(f'\n\n{Game.__repr__(play)}')
        # check to see if game is over
        if play.is_game_over() == True:
            if play.is_full() == True:
                if play.calc_winner() is None:
                    print(f"Game over! Tie!")
                    break
                elif play.calc_winner() == player_1:
                    print(f'Game over! The Winner is {player_1.name}')
                    break
                elif play.calc_winner() == player_2:
                    print(f'Game over! The Winner is {player_2.name}')
                    break
            elif play.calc_winner() == player_1:
                    print(f'Game over! The Winner is {player_1.name}')
                    break
            elif play.calc_winner() == player_2:
                    print(f'Game over! The Winner is {player_2.name}')
                    break
        # player_2's turn               
        while True:
            x = int(input(f"{player_2.name} Enter your move's x coordinate: ")) - 1
            y = int(input(f"{player_2.name} Enter your move's y coordinate: ")) - 1
            test = Game.move(play, x, y, player_2.token)
            if test == False:
                print("Try again.")
            elif test == True:
                break
        # print after player_2's turn
        print(f'\n\n{Game.__repr__(play)}')
        # check if game is over
        if play.is_game_over() == True:
            if play.is_full() == True:
                if play.calc_winner() is None:
                    print(f"Game over! Tie!")  
                    break     
                elif play.calc_winner() == player_1:
                    print(f'Game over! The Winner is {player_1.name}')
                    break
                elif play.calc_winner() == player_2:
                    print(f'Game over! The Winner is {player_2.name}')
                    break
            elif play.calc_winner() == player_1:
                    print(f'Game over! The Winner is {player_1.name}')
                    break
            elif play.calc_winner() == player_2:
                    print(f'Game over! The Winner is {player_2.name}')
                    break
    # option to play again or end program    
    play_again = input("Would you like to play again?: ").lower()
    if play_again in ['yes', 'y']:
        continue
    elif play_again in ['no', 'n']:
        print("Thank you for playing!")
        break   
        