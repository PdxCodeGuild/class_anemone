import pygame
import sys
import os # to import the photos from Assets

#---------------------------------MY I GOT AHEAD OF MY SELF, GO TO GAME.. Orginal parts down in lower notes--------------------------------#

pygame.font.init() # calling the font.init() to use pygame.font

CLOCK = pygame.time.Clock() # for Frames per second
SCREEN = pygame.display.set_mode((500,900)) # display size of SCREEN
pygame.display.set_caption('COUNT YOUR JUMPS..GAME!') # naming the window of the game

keys_pressed = pygame.key.get_pressed()

JUMP_FONT = pygame.font.SysFont('comicsans', 75) # calling the type of font we want to add to the screen
JUMP_COUNT = pygame.font.SysFont('comicsans', 75) # ( type of lettering, font size)

CHAR_IMAGE = pygame.image.load(os.path.join('Assets', 'sussy_naruto.png')) # images imported into the game 
CHAR = pygame.transform.scale(CHAR_IMAGE, (120, 145))  # rescaling the image ( hieght, width )
BG_IMAGE = pygame.image.load(os.path.join('Assets', 'field.png'))
BACKGROUND = pygame.transform.scale(BG_IMAGE, (500, 900))
JUMP_IMAGE = pygame.image.load(os.path.join('Assets', 'pika.png'))
CHAR_JUMP = pygame.transform.scale(JUMP_IMAGE, (105, 115))

i = 0 # the jump counter part

while True:

    for event in pygame.event.get(): # event created to ensure the game is quit and can be quit properly
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((0,0,0))
    SCREEN.blit(BACKGROUND, (0, 0))

    CHAR_X, CHAR_Y = 240, 700 # characters X, y postitions
    jumping = False
    Y_GRAVITY = 25          # explained below
    JUMP_HEIGHT = 250
    Y_VELOCITY = JUMP_HEIGHT
    
    keys_pressed = pygame.key.get_pressed() # dict of all keys

    if keys_pressed[pygame.K_w]:   # checking to see if w key is pressed by checking the key value from get.pressed() dict
        jumping = True
        
    if jumping:
        CHAR_Y -= Y_VELOCITY            # taking the char position and giving it a distance to go up
        Y_VELOCITY -= Y_GRAVITY         # gravity is used to control the speed of the decent.. 1/10th of velocity or it gets bonkers
        if Y_VELOCITY < -JUMP_HEIGHT:   # basically sstating the if CHAR jumps and hits the height it says your at your limit
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT    # Then says let go back to your ORIGINALLY SPOT but taking away to jump height

        naruto = CHAR_JUMP.get_rect(center=(CHAR_X, CHAR_Y)) # get.rect is turning the .png into a obstaclt ( rectangle )
        SCREEN.blit(CHAR_JUMP, naruto)

    else:
        naruto = CHAR.get_rect(center=(CHAR_X, CHAR_Y)) # just to see something else then when jumping ( diffent png added )
        SCREEN.blit(CHAR, naruto)
    
    for event in pygame.event.get():       # only counting IF the key was pressed and not held for count accuarcy
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                i +=1

    JUMP_TXT = JUMP_FONT.render('JUMPS', 1, (240,0,240))    # adding the headers to the screen to know what jump your at 
    JUMP_COUNT = JUMP_FONT.render(str(i), 1, (240,0,200))       

    SCREEN.blit(JUMP_TXT, (100, 0))                            # (0,0,0) is RGB and (0, 0) is x,y posaitions
    SCREEN.blit(JUMP_COUNT, (200,125))    

    pygame.display.update() # updates the display every rotation
    CLOCK.tick(200)  # higher the tick rate the more power it uses and longer it takes to close BUT more accurate

# CLOCK.tick(200) probably wont close fast BUT is very accurate.. 

# USE CLOCK.tick(60) or less for quicker game close but less accurate jump count

# TRUST I tested alot 


# ------------------------------------- NEEDS SO MUCH WORK ( collision ) MAVE have to create a full Class system------------------------------- #

#                                                 Making a running jump game.. with an enemy shooting at me...
#                                                        Issues with bullet collisions working correctly and a few more things to work on

#-----------------------------------------------------------------------------------------------------------------------------------------------#
# WIDTH_SCREEN = 1200

# char = CHAR.get_rect()
# i = 0

    # SCREEN.fill((0,0,0))
    # SCREEN.blit(BACKGROUND, (i, 0))
    # SCREEN.blit(BACKGROUND, (WIDTH_SCREEN+i, 0))
    # if i == -WIDTH_SCREEN:
    #     SCREEN.blit(BACKGROUND, (WIDTH_SCREEN+i, 0))   # moves screen and repeats itself
    #     sad.x -= 5
    #     i=0
    # i-=2

    # if bullet.colliderect(char):  # detects collision
    #     print('you lose')

# bullet = pygame.Rect(1200,510,50,6)
# x_speed, y_speed = 25, 8
# def enemy():
#     bullet.x -= x_speed
#     pygame.draw.rect(SCREEN, (255,0,0), bullet) # creates a bullet from a rectantagnle

# BULLET_SHOT = pygame.USEREVENT + 1

# def jump():
#     CHAR_X, CHAR_Y = 240, 700
#     jumping = False
#     Y_GRAVITY = 13
#     JUMP_HEIGHT = 250
#     Y_VELOCITY = JUMP_HEIGHT
    
#     keys_pressed = pygame.key.get_pressed()

#     if keys_pressed[pygame.K_w]:
#         jumping = True
        
#     if jumping:
#         CHAR_Y -= Y_VELOCITY
#         Y_VELOCITY -= Y_GRAVITY
#         if Y_VELOCITY < -JUMP_HEIGHT:
#             jumping = False
#             Y_VELOCITY = JUMP_HEIGHT
#         naruto = CHAR_JUMP.get_rect(center=(CHAR_X, CHAR_Y))
#         SCREEN.blit(CHAR_JUMP, naruto)
#     else:
#         naruto = CHAR.get_rect(center=(CHAR_X, CHAR_Y))
#         SCREEN.blit(CHAR, naruto)
#     return jump

# bullet = pygame.Rect(1200,510,50,6)