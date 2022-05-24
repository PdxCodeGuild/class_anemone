
from turtle import window_height, window_width
import pygame
import random
from lab16tile import Tile
from lab16level import Level
from lab16map import map1
# Formatting pygame
pygame.init()

# create window
window = pygame.display.set_mode((1600,800))
level = Level(map1,window)


#Title 
pygame.display.set_caption('Welda')


# ROWS = 16
# MAX_COL = 150
# TILESIZE = 800 //ROWS

# # # Background
# sky = pygame.image.load("nicesky.png").convert_alpha()
# sky = pygame.transform.scale(sky, (1600,800))
# scroll_left = False
# scroll_right = False
# scroll = 0
# scroll_speed = 1


#test_tile = pygame.sprite.Group(Tile((100,100),200))



#Player
playerImg = pygame.image.load('avatar.png')
playerImg = pygame.transform.scale(playerImg, (64,64))
playerX =  0
playerY = 400
player_move = 0
player_move2 = 0

# Enemy
enemyImg = pygame.image.load('ghost.png')
enemyImg = pygame.transform.scale(enemyImg, (24,24))
enemyX = random.randint(0,1600)
enemyY = random.randint(300,800)
enemy_move = 0
enemy_move2 = 0
12
def player(x,y):
    window.blit(playerImg, (x, y))

def enemy(x,y):
    window.blit(enemyImg, (x, y))


# def bg(x,y):
#     width = sky.get_width()
#     for x in range(4):
#         window.blit(sky,((x *width)-scroll,0))


# def grid():
#     for c in range(MAX_COL + 1):
#         pygame.draw.line(window, (c * TILESIZE, 0),(c * TILESIZE, 800))
#     for r in range(ROWS + 1):
#         pygame.draw.line(window, (0,r * TILESIZE, 0),(1600, c *TILESIZE))





# Looping the game window to keep it from shutting down
run = True
while run:
    window.fill((0,0,0))
    playerX += 0
    playerY += 0
    #test_tile.draw(window)

    # if scroll_left == True:
    #     scroll -= 2
    # if scroll_right == True:
    #     scroll += 2


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        
        
        #scroll map
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            
    
    #RBG
    
    # keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move = -1
            if event.key == pygame.K_RIGHT:
                player_move = 1
            if event.key == pygame.K_UP:
                player_move2 = -1
            if event.key == pygame.K_DOWN:
                player_move2 = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_move = 0
                player_move2 = 0

            # playerX += player_move
    playerY += player_move2 
    playerX += player_move
    
    
    # Boundries
    if playerX <= 0:
        playerX <=0
    elif playerX >= 1536:
        playerX = 1536

    if playerY <= 0:
        playerY <= 0
    elif playerY >= 736:
        playerY = 736

    if playerX >= 1600:
        playerX >= 1600
    elif playerX <= 0:
        playerX = 0

    if playerY >= 800:
        playerY >= 800
    elif playerY <= 0:
        playerY = 0

    # playerY += player_move
    # bg(0,0)
    # grid()
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    # window.blit(grass, (grass_rect))
    pygame.display.update()



