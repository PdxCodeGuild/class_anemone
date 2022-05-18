import pygame

WIDTH, HEIGHT = 1200, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # creating the screen size with the input added
pygame.display.set_caption('Jump Game') # naming the screen ( pop up )

COLOR = (240,240,240) # currently white ( R, G, B )

def draw_window():
    SCREEN.fill(COLOR)
    pygame.display.update()

def main():  # main function for game to run

    run = True        # Loop created to close the pygame window and game.. IE quit function
    while run:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                run = False

        draw_window() # calling the draw function to creat the window and fill it with colo

    pygame.quit()


if __name__ == "__main__": # making sure we only run this file if we run it directly ( also makes screen pop up and draw)
    main()




# side scrolling jumping game.. NEED to import back round and character models