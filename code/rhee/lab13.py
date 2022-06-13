class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.name


class Game:
    def __init__(self):
        self.board = {"1": " ", "4": " ", "7": " ",
                      "2": " ", "5": " ", "8": " ",
                      "3": " ", "6": " ", "9": " "
                      }

    def __repr__(self):
        print(self.board["1"] + "|" + self.board["4"] + "|" + self.board["7"])
        print("-----")
        print(self.board["2"] + "|" + self.board["5"] + "|" + self.board["8"])
        print("-----")
        print(self.board["3"] + "|" + self.board["6"] + "|" + self.board["9"])

    def board_spot(self, player):
        while True:
            print("1|4|7")
            print("2|5|8")
            print("3|6|9")
            number = input("Choose a spot: ")
            if self.board[number] != " ":
                print("Spot taken! Select another spot! ")
                continue
            else:
                self.board[number] = player.token
                break

    def check_winner(self):

        # Check board horizontal
        if self.board["1"] == self.board["4"] == self.board["7"] != " ":
            return self.board["1"]
        elif self.board["2"] == self.board["5"] == self.board["8"] != " ":
            return self.board["2"]
        elif self.board["3"] == self.board["6"] == self.board["9"] != " ":
            return self.board["3"]

        # Check board vertical
        elif self.board["1"] == self.board["2"] == self.board["3"] != " ":
            return self.board["1"]
        elif self.board["4"] == self.board["5"] == self.board["6"] != " ":
            return self.board["4"]
        elif self.board["7"] == self.board["8"] == self.board["9"] != " ":
            return self.board["7"]

        # check board diagonal
        elif self.board["1"] == self.board["5"] == self.board["9"] != " ":
            return self.board["1"]
        elif self.board["3"] == self.board["5"] == self.board["7"] != " ":
            return self.board["3"]
        else:
            return None

    # Check game board
    def board_full(self):
        game_full = 0
        if game_full == "1":
            print("Game board is full.")
        if game_full == "0":
            print("Game board is not full.")
        for i in self.board:
            if self.board[i] == ' ':
                return False
        return True

    # Checks winner or if any spots open
    def end_game(self):
        winner = self.check_winner()
        full = self.board_full()
        if winner or full:
            return True



# Player 2 selection.
def selection_2():
    if selection_1 == "X":
        return "O"
    elif selection_1 == "O":
        return "X"



while True:
    game = Game()
    selection = input("Do you want to play? Y or N: ").upper()
    if selection == "Y":
        user_1 = input("Enter a name for Player 1: ")
        while True:
            selection_1 = input("Please select 'X' or 'O':\n").upper()
            if selection_1 == "X":
                print("You selected 'X'!")
                print("Player 2 will be 'O'.\n")
            elif selection_1 == "O":
                print("You selected 'O'!")
                print("Player 2 will be 'X'.\n")
            if selection_1 != "X" and selection_1 != "O":
                print("Please select again.\n")
            elif selection_1 == "X" or selection_1 == "O":
                break
            else:
                continue

        user_2 = input("Enter a name for Player 2: ")
        selection_2 = selection_2()

        player1 = Player(user_1, selection_1)
        player2 = Player(user_2, selection_2)
        turn = 0

        for i in range(10):
            turn += 1
            game.__repr__()

            if turn % 2 == 1:
                print("Player 1 turn")
                game.board_spot(player1)
                game_player = user_1

            else:
                print("Player 2 turn")
                game.board_spot(player2)
                game_player = user_2

            if game.end_game():
                game.__repr__()
                print(f"{game.check_winner()} wins!")
                break

    else:
        print("Goodbye!")
        break
