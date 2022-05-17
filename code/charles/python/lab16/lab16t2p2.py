import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pygame.time.Clock()


pygame.init()
window = pygame.display.set_mode((640,480))

x = 120
y = 120

running = True
while running:

    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running == False
                break
            elif event.key == pygame.K_RIGHT:
                x += 8
            elif event.key == pygame.K_LEFT:
                x -= 8
            elif event.key == pygame.K_DOWN:
                y += 8
            elif event.key == pygame.K_UP:
                y -= 8
            elif event.key == pygame.K_d:
                x += 8
            elif event.key == pygame.K_a:
                x -= 8
            elif event.key == pygame.K_s:
                y += 8
            elif event.key == pygame.K_w:
                y -= 8

    window.fill((0,0,0))
    pygame.draw.rect(window,(0,0,255), (x,y,400,240))
            
    # pygame.draw.rect(window,(0,0,255),(120,120,400,240))
    # pygame.draw.circle(window,(255, 0, 255), (250, 250), (20))            # pygame.draw circle(window to draw, (color r,g,b), (location x,y), (width x))
    # pygame.draw.circle(window,(255, 0, 255), (400, 400), (20))
    # pygame.draw.line(window, (255, 0, 255), (300, 300), (320, 320), (10)) # pygame.draw.line(window to draw,(color r,g,b,), (location x,y start), (x,y end), (width x)
    # pygame.draw.line(window, (255, 0, 255), (200, 200), (100, 100), (10))
    clock.tick(120)
    pygame.display.update()

pygame.quit()