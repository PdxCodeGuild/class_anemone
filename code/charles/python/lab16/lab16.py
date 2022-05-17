# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Game Name WIP")
     
    # create a surface on screen that has the size of 240 x 180
    screen_hight = 240
    screen_width = 180
    
    screen = pygame.display.set_mode((screen_hight,screen_width))
    background = pygame.image.load('background.png')
    screen.blit(background, (0, 0))
    image = pygame.image.load('01_image.png')
    image.set_colorkey((255,0,255))
    screen.blit(image, (50,50))
    pygame.display.flip()

    # movement
    xpos = 50
    ypos = 50
    # pixel steps
    step_x = 10
    step_y = 10

    if xpos > screen_width - 64 or xpos < 0:
        step_x = -step_x
    if ypos > screen_hight - 64 or ypos < 0:
        step_y = -step_y

    xpos += step_x
    ypos += step_y
    screen.blit(image, (xpos, ypos))
    pygame.display.flip()
    screen.blit(background, (0,0))
    screen.blit(image, (xpos, ypos))
    pygame.display.flip()
    
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # movement
          
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()