import pygame
import sys
import os

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('poop')

WIDTH_SCREEN = 1200

SAD_X, SAD_Y = 1100, 495

CHAR_IMAGE = pygame.image.load(os.path.join('Assets', 'sussy_naruto.png'))
CHAR = pygame.transform.scale(CHAR_IMAGE, (75, 95))
BG_IMAGE = pygame.image.load(os.path.join('Assets', 'field.png'))
BACKGROUND = pygame.transform.scale(BG_IMAGE, (1200, 700))
SAD_IMAGE = pygame.image.load(os.path.join('Assets', 'sad.png'))
SAD_BOY = pygame.transform.scale(SAD_IMAGE, (50, 70))

sad = SAD_BOY.get_rect(center=(SAD_X, SAD_Y))

def jump():
    CHAR_X, CHAR_Y = 180, 520
    jumping = False
    Y_GRAVITY = 13
    JUMP_HEIGHT = 135
    Y_VELOCITY = JUMP_HEIGHT
    
    keys_pressed = pygame.key.get_pressed()
    pygame.time.delay(20)

    if keys_pressed[pygame.K_w]:
        jumping = True
        
    if jumping:
        CHAR_Y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        naruto = CHAR.get_rect(center=(CHAR_X, CHAR_Y))
        SCREEN.blit(CHAR, naruto)
    else:
        naruto = CHAR.get_rect(center=(CHAR_X, CHAR_Y))
        SCREEN.blit(CHAR, naruto)
    return jump

# sad = pygame.Rect(SAD_X, SAD_Y, 50, 70)
# SAD = SAD_BOY.get_rect(center=(SAD_X, SAD_Y))
bullet = pygame.Rect(1200,510,50,6)
x_speed, y_speed = 25, 8


def enemy():
    bullet.x -= x_speed
    pygame.draw.rect(SCREEN, (255,0,0), bullet)


i=0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((0,0,0))
    SCREEN.blit(BACKGROUND, (i, 0))
    SCREEN.blit(BACKGROUND, (WIDTH_SCREEN+i, 0))
    # if i == -WIDTH_SCREEN:
    #     SCREEN.blit(BACKGROUND, (WIDTH_SCREEN+i, 0))
    #     sad.x -= 5
    #     i=0
    # i-=8
    
    enemy()
    jump()


    
    

    pygame.display.update()
    CLOCK.tick(60)