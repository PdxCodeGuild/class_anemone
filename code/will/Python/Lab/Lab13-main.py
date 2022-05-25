#Creating the board display and list of positions for pieces

class Board:

    def __init__(self):
  
      self.cells = [' ',' ',' ',
                    ' ',' ',' ',
                    ' ',' ',' ']
               


#Board display and cell value assignment 
     
    def __repr__(self):
        print ("%s | %s | %s "%(self.cells[0], self.cells[1], self.cells[2]))
        print("----------")
        print ("%s | %s | %s "%(self.cells[3], self.cells[4], self.cells[5]))
        print("----------")
        print ("%s | %s | %s "%(self.cells[6], self.cells[7], self.cells[8]))

    
    def update_cell(self, cell_no, player):
        self.cells[cell_no] = player
 

        
        
    def calc_winner(self, player):
        if self.cells[0]==player and self.cells[1]==player and self.cells[2]==player:
            return True
        if self.cells[3]==player and self.cells[4]==player and self.cells[5]==player:
            return True
        if self.cells[6]==player and self.cells[7]==player and self.cells[8]==player:
            return True
        if self.cells[0]==player and self.cells[4]==player and self.cells[8]==player:
            return True
        if self.cells[6]==player and self.cells[4]==player and self.cells[2]==player:
            return True
        if self.cells[0]==player and self.cells[3]==player and self.cells[6]==player:
            return True
        if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            return True
        if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
            return True

    def game_over(self):
        self.cells ==["","","",
                      "","","",
                      "","",""]

        


    def is_full(self):
        used_cells = 0
        for cell in self.cells:
            if cell !=" ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

board = Board()

board.__repr__()

while True: 
    x_choice = int(input("\nX) Please choose a space 0-8: 0 is top left, 8 is bottom right "))

    board.update_cell(x_choice, "X")
    board.__repr__()

    if board.calc_winner("X"):
        print ("\n X Wins!!!\n")
        play_again = input("Would you like to play again? Y/N? ").upper
        if play_again == "Y":
            board.is_full()
            continue
        else:
            break

    if board.is_game_over():
        print ("Game over! It's a tie!")
        play_again = input("Would you like to play again? Y/N? ").upper
        if play_again == "Y":
            board.is_full()
            continue
        else:
            break


    o_choice = int(input("\nO) Please choose a space 0-8: 0 is top left, 8 is bottom right"))

    board.update_cell(o_choice, "O")
    board.__repr__()

    if board.calc_winner("O"):
        print ("\n O Wins!!!\n")
        play_again = input("Would you like to play again? Y/N? ").upper
        if play_again == "Y":
            board.is_full()
            continue
        else:
            break

    if board.is_game_over():
        print ("Game over! It's a tie!")
        play_again = input("Would you like to play again? Y/N? ").upper
        if play_again == "Y":
            board.is_full()
            continue
        else:
            break


