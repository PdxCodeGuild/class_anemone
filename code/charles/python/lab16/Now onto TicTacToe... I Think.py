import pygame
import time
from pygame.locals import *

class Screen():
    board = [[None] * 3, [None] * 3, [None] * 3]
    width = 1080
    height = 960
    white = (255, 255, 255)
    linered = (10, 10, 10)
    winner = None
    draw = False
    pieces = 'x'
        
    pygame.init()
    fps = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption('Tic Tac Toe Final')

    opening = pygame.image.load('opening.jpg')
    ximg = pygame.image.load('x.jpg')
    oimg = pygame.image.load('x.jpg')

    opening = pygame.transform.scale(opening, (width, height))
    ximg = pygame.transform.scale(ximg, (160, 160))
    oimg = pygame.transform.scale(oimg, (160, 160))

kren = Screen()


def loading():
    
    kren.screen.blit(kren.opening, (0, 0))
    pygame.display.update()
    time.sleep(3)
    kren.screen.fill(kren.white)

    pygame.draw.line(kren.screen, kren.linered, (kren.width/3, 0), (kren.width/3, kren.height), 7)
    pygame.draw.line(kren.screen, kren.linered, (kren.width/3 * 2, 0), (kren.width/3 * 2, kren.height), 7)

    pygame.draw.line(kren.screen, kren.linered, (0, kren.height/3), (kren.width, kren.height/3), 7)
    pygame.draw.line(kren.screen, kren.linered, (0, kren.height/3 * 2), (kren.width, kren.height/3 * 2), 7)
    
    drawsome()


def drawsome():
       
    if kren.winner is None:
        message = (f"{kren.pieces.upper()}'s Turn") 
    else:
        message = (f"{kren.winner.upper()} has won the game!")
    if kren.draw:
        message = 'Neither of you could outsmart the other.'

    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (255, 0, 0))

    kren.screen.fill((0,0,0), (0, 400, 600, 100))
    textrect = text.get_rect(center = (kren.width/2, 500 - 50))
    kren.screen.blit(text, textrect)
    pygame.display.update()


def wwcd():
       
    for row in range(0,3):
        if ((kren.board[row][0] == kren.board[row][1] == kren.board[row][2]) and \
            (kren.board[row][0] is not None)):
            
            kren.winner = kren.board[row][0]
            
            pygame.draw.line(kren.screen, (250, 0, 0), (0, \
                (row + 1) * kren.height/3 - kren.height/6),\
                (kren.width, (row + 1) * kren.height/3 - kren.height/6), 4)
            
            break


    for col in range(0, 3):
        if (kren.board[0][col] == kren.board[1][col] == kren.board[2][col]) and \
            (kren.board[0][col] is not None):
            
            kren.winner = kren.board[0][col]
            
            pygame.draw.line (kren.screen, (250,0,0),\
                ((col + 1)* kren.width/3 - kren.width/6, 0),\
                ((col + 1)* kren.width/3 - kren.width/6, kren.height), 4)
            
            break


    if (kren.board[0][0] == kren.board[1][1] == kren.board[2][2]) and \
        (kren.board[0][0] is not None):
        
        kren.winner = kren.board[0][0]
        
        pygame.draw.line (kren.screen, (250,70,70), (50, 50), (350, 350), 4)
    
    
    if (kren.board[0][2] == kren.board[1][1] == kren.board[2][0]) and \
        (kren.board[0][2] is not None):
        kren.winner = kren.board[0][2]
        pygame.draw.line (kren.screen, (250,70,70), (350, 50), (50, 350), 4)


    if (all((all(row) for row in kren.board)) and kren.winner is None):
        kren.draw = True
    drawsome()

def piece(row, col):
    
    if row == 1:
        posx = 30
    elif row == 2:
        posx = kren.width/3 + 30
    elif row == 3:
        posx = kren.width/3 * 2 + 30 
    
    if col == 1:
        posy = 30
    elif col == 2:
        posy = kren.height/3 + 30
    elif col == 3:
        posy = kren.height/3 * 2 + 30
    
    kren.board[row - 1][col -1] = kren.pieces

    if (kren.pieces == 'x'):
        kren.screen.blit(kren.ximg, (posy, posx))
        kren.pieces = 'o'
    else:
        kren.screen.blit(kren.oimg, (posy, posx))
        kren.pieces = 'x'
    
    pygame.display.update()

def click():
    
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
    
    if (row and col and kren.board[row- 1][col - 1] is None):
        kren.pieces

        piece(row, col)
        wwcd()


def reset_game():
  
    time.sleep(3)
    kren.pieces = 'x'
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
        elif event.type == MOUSEBUTTONDOWN:
            click()
            if (kren.winner or kren.draw):
                reset_game()

    pygame.display.update()
    kren.clock.tick(kren.fps)








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
            
            

       
        