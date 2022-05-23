import pygame
import time
from pygame.locals import *

class Screen():                                                 # sets base values for the game appart from the lines for the board dont in loading()
                                                                # initiates pygame and calls forth the pictures for pieces and screen size and picture
    def __init__(self):
        self.board = [[None] * 3, [None] * 3, [None] * 3]
        self.width = 1080
        self.height = 960
        self.white = (255, 255, 255)
        self.linered = (10, 10, 10)
        self.winner = None
        self.draw = False
        self.turn = 1
        self.pieces = 'x'
            
        pygame.init()
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height+100), 0, 32)
        pygame.display.set_caption('Tic Tac Toe Final')

        self.opening = pygame.image.load('opening.jpg')
        self.ximg = pygame.image.load('x.jpg')
        self.oimg = pygame.image.load('o.jpg')

        self.opening = pygame.transform.scale(self.opening, (self.width, self.height+100))
        self.ximg = pygame.transform.scale(self.ximg, (160, 160))
        self.oimg = pygame.transform.scale(self.oimg, (160, 160))

kren = Screen()


def loading():
    
    kren.screen.blit(kren.opening, (0, 0))              # loads the screen and displays the set picture during loading
    pygame.display.update()                             # calls the screen to update with new datat
    time.sleep(1)
    kren.screen.fill(kren.white)                        # fills the screen with a white background before the lines are called and pasted atop

    pygame.draw.line(kren.screen, kren.linered, (kren.width/3, 0), (kren.width/3, kren.height), 14)
    pygame.draw.line(kren.screen, kren.linered, (kren.width/3 * 2, 0), (kren.width/3 * 2, kren.height), 14)

    pygame.draw.line(kren.screen, kren.linered, (0, kren.height/3), (kren.width, kren.height/3), 14)
    pygame.draw.line(kren.screen, kren.linered, (0, kren.height/3 * 2), (kren.width, kren.height/3 * 2), 14)
    
    drawsome()


def drawsome():
       
    if kren.winner is None:                                         # defines messages to be displayed in the bottom box
        message = (f"{kren.pieces.upper()}'s Turn") 
    else:
        message = (f"{kren.winner.upper()} has won the game!")
    if kren.draw:
        message = 'Neither of you could outsmart the other.'

    font = pygame.font.Font(None, 60)                               # sets the font size to be used
    text = font.render(message, 1, (255, 0, 0))                     # sets the font/message be displaye with the color

    kren.screen.fill((0,0,0), (0, 960, 1080, 100))                  # sets the message box on the screen with a color of black
    textrect = text.get_rect(center = (kren.width/2, 1080 - 75))    # sets the location of the message box
    kren.screen.blit(text, textrect)                                # paste the message box and text on to the screen
    pygame.display.update()                                         # updates the screen with the message box


def wwcd():
    
                                                                                    # test rows for a winner  
    for row in range(0,3):
        if ((kren.board[row][0] == kren.board[row][1] == kren.board[row][2]) and \
            (kren.board[row][0] is not None)):
            
            kren.winner = kren.board[row][0]                                        # changes winner if True
                        
            pygame.draw.line(kren.screen, (250, 0, 0),\
                (0, (row + 1) * kren.height/3 - kren.height/6),\
                (kren.width, (row + 1) * kren.height/3 - kren.height/6), 10)        # draws winning line over pieces if True
            
            break

                                                                                    # test columns for a winner
    for col in range(0, 3):
        if (kren.board[0][col] == kren.board[1][col] == kren.board[2][col]) and \
            (kren.board[0][col] is not None):
            
            kren.winner = kren.board[0][col]                                        
            
            pygame.draw.line (kren.screen, (250,0,0),\
                ((col + 1)* kren.width/3 - kren.width/6, 0),\
                ((col + 1)* kren.width/3 - kren.width/6, kren.height), 10)
            
            break

                                                                                    # test board for a bottom top left bottom right diag winner
    if (kren.board[0][0] == kren.board[1][1] == kren.board[2][2]) and \
        (kren.board[0][0] is not None):
        
        kren.winner = kren.board[0][0]                                              
        
        pygame.draw.line (kren.screen, (250,0,0), (0, 0), (1080, 960), 10)          
    
                                                                                    # test board for a bottom left to top right diag winner
    if (kren.board[0][2] == kren.board[1][1] == kren.board[2][0]) and \
        (kren.board[0][2] is not None):                                               
        
        kren.winner = kren.board[0][2]                                              
        
        pygame.draw.line (kren.screen, (250,0,0), (1080, 0), (0, 960), 10)          


    if (all([all(row) for row in kren.board]) and kren.winner is None):   # test the board for a draw status if neither x or o has won
        kren.draw = True
    drawsome()

def piece(row, col):                                # passed into click() and defines where on the screen piece shall be placed base          
                                                    # off of row and col
    if row == 1:
        posx = 75
    elif row == 2:
        posx = kren.width/3 + 40
    elif row == 3:
        posx = kren.width/3 * 2 
    
    if col == 1:
        posy = 100
    elif col == 2:
        posy = kren.height/3 + 140
    elif col == 3:
        posy = kren.height/3 * 2 + 180
    
    kren.board[row - 1][col -1] = kren.pieces       # stops a single game from running infinitely

    if kren.turn % 2 == 1:
        kren.screen.blit(kren.ximg, (posy, posx))   # paste an Ximg onto the screen at input loaction, adds one to turn, sets pieces to o
        kren.turn += 1
        kren.pieces = 'o'
    else:
        kren.screen.blit(kren.oimg, (posy, posx))   # paste an Oimg onto the screen at input loaction, adds one to turn, sets pieces to x
        kren.turn += 1
        kren.pieces = 'x'
    
    pygame.display.update()

def click():                                        # calls in x and y positions from .mouse.get_pos() to be compared to the screen width and height
                                                    # based on return gives row and column data to be passed into piece
    x,y = pygame.mouse.get_pos()

    if (x < kren.width/3):
        col = 1
    elif (x < kren.width/3 * 2):
        col = 2
    elif (x < kren.width):
        col = 3
    else:
        col = None
    
    if (y < kren.height/3):
        row = 1
    elif (y < kren.height/3 * 2):
        row = 2
    elif (y < kren.height):
        row = 3
    else:
        row = None
    
    if (row and col and kren.board[row - 1][col - 1] is None):  # validates to move to make sure that the board is empty and will not accept a click
        kren.pieces                                             # if the board space is already filled

        piece(row, col)
        wwcd()


def reset_game():               # resets to default values again so the game runs continuously until a quit is triggered
    kren.pieces = 'x'
    time.sleep(1)
    kren.turn = 1
    kren.draw = False
    loading()
    kren.winner = None
    kren.board = [[None]*3,[None]*3,[None]*3]

loading()

while (True):
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            pygame.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                pygame.exit()
        elif event.type == MOUSEBUTTONDOWN:
            click()
            if (kren.winner or kren.draw):
                reset_game()

    pygame.display.update()
    kren.clock.tick(kren.fps)







# SCRAPPED

# os.environ['SDL_VIDEO_CENTERED'] = '1'


# class Player():
    
#     def __init__(self):
#         self.cplayersxo = []
#         self.xplayer = pygame.image.load('x.jpg')
#         self.yplayer = pygame.image.load('y.jpg')
#         self.xplayer = pygame.transform.scale(self.xplayer, (80, 80))
#         self.yplayer = pygame.transform.scale(self.yplayer, (80, 80))


#     def nplayer(self, person, piece):
#         self.cplayersxo.append([person, piece])


#     def validation(self, x, y):
#         pass
    
#     def move(self, x, y, player):
#         piece = player
#         if self.validation == True:
#             pass




# class Board():

#     def __init__(self):
#         self.boardsize = Vector2(640,480)

#     def update(self, player):
#         if Player.validation() == False:
#             return
#         elif Player.validation() == True:
#             Player.move()


    


# class userinterface():

#     def __init__(self):
#         pygame.init()

#         self.no = ['n', 'no', 'na', 'nada', 'nope']
#         self.yes = ['y', 'yes', 'yes', 'ye', 'ya']
#         self.turns = 1
#         self.cellsize = Vector2(640, 480)
#         self.gamestate = Board()
#         self.player = Player()
#         self.pieces = ['X', 'O']

#         boardsize = self.gamestate.boardsize.elementwise() * self.cellsize
#         self.window = pygame.display.set_mode((int(boardsize.x), int(boardsize.y)))
#         pygame.display.set_caption('Now onto TicTacToe... I Think')
#         pygame.display.set_icon(pygame.image.load('charlotte 3.png'))

#         self.clock = pygame.time.Clock()
#         self.running = True

    
#     def processinput(self):
#         self.place = Vector2(0,0)
#         playon = True
#         while playon:
#             self.gamestate
#             self.player
#             while len(self.player.cplayersxo) != 2:
#                 player = input('Please enter your name. ').title()
#                 piece = input(f'select a piece{self.pieces}. ').upper()
#                 if piece == 'X':
#                    pass 
                
#                 self.pieces.remove(piece)
#                 self.player.cplayersxo.append([player, piece])

#             while self.gamestate.calc_win() == False and self.gamestate.full() == False:

#                 if self.turns % 2 == 1:                                                                                                  
#                     place = input(f'{Player.cplayersxo[0][0]} Turn: ')

#                 elif self.turns % 2 == 0:         
#                     pass
#     def update(self):
#         self.gamestate.update()
    
#     def renderbackground(self):
#         board = self.gamestate.elementwise()* self.cellsize
#         self.window.blit()
#         pass

#     def renderplayer(self):
#         playerpic = 's'

#     def render(self):
#         self.window.fill((0,0,0))
#         pygame.display.update()

        

    


#     def run(self):
#         while self.running:
#             self.processinput()
#             self.update()
#             self.render()
#             self.clock.tick(60)

# game = userinterface()
# game.run()
            
            

       
        