import os
import pygame
from pygame import rect
from pygame import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Player():
    
    def __init__(self):
        self.cplayersxo = []
        self.xplayer = pygame.image.load('x.jpg')
        self.yplayer = pygame.image.load('y.jpg')
    
    def nplayer(self, person, piece):
        self.cplayersxo.append([person, piece])


    def validation(self, x, y):
        pass
    
    def move(self, x, y, player):
        piece = player
        # if 

class Board():

    def __init__(self):
        self.boardsize = Vector2(640,480)

class userinterface():

    def __init__(self):
        pygame.init()

        self.no = ['n', 'no', 'na', 'nada', 'nope']
        self.yes = ['y', 'yes', 'yes', 'ye', 'ya']
        self.turns = 1
        self.cellsize = Vector2(640, 480)
        self.xplayer = pygame.image.load('x.jpg')
        self.yplayer = pygame.image.load('y.jpg')
        self.xplayer = pygame.transform.scale(self.xplayer, (80, 80))
        self.yplayer = pygame.transform.scale(self.yplayer, (80, 80))
        self.gamestate = Board()
        self.player = Player()
        self.pieces = ['X', 'O']

        boardsize = self.gamestate.boardsize.elementwise() * self.cellsize
        self.window = pygame.display.set_mode((int(boardsize.x), int(boardsize.y)))
        pygame.display.set_caption('Now onto TicTacToe... I Think')
        pygame.display.set_icon(pygame.image.load('charlotte 3.png'))

        self.clock = pygame.time.Clock()
        self.running = True

    
    def processinput(self):
        
        playon = True
        while playon:
            self.gamestate
            self.player
            while len(self.player.cplayersxo) != 2:
                player = input('Please enter your name. ').title()
                piece = input(f'select a piece{self.pieces}. ').upper()
                if piece == 'X':
                   pass 
                
                self.pieces.remove(piece)
                self.player.cplayersxo.append([player, piece])

            while self.gamestate.calc_win() == False and self.gamestate.full() == False:

                if self.turns % 2 == 1:                                                                                                  
                    pass                                                                                    
                elif self.turns % 2 == 0:         
                    pass
    
    
    def renderbackground(self):
        board = self.gamestate.elementwise()* self.cellsize
        self.window.blit()
        pass

    def renderplayer(self):
        self.window.fill((0,0,0))

        

        

    def update():
        pass


    def run(self):
        while self.running:
            self.processinput()
            self.update()
            self.render()
            self.clock.tick(60)

game = userinterface()
game.run()
            
            

       
        