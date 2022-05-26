import pygame
from pygame.locals import *

pygame.init()

# window setup
window_height = 300
window_width = 300
lines_width = 3
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tic Tac Toe')

#colors or RBG
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# font
font = pygame.font.SysFont('times new roman', 30)

# variables
markers = []
game_over = False
win = 0
click = False
player = 1
pos = (0,0)


#setup a rectangle for "Play Again"
play_again_rect = Rect(window_width // 2 - 80, window_height // 2, 160, 50)

#create empty 3 x 3 list to represent the grid
for x in range (3):
	row = [0] * 3
	markers.append(row)

    # [
    # [0,0,0]
    # [0,0,0]
    # [0,0,0]
    # ]


# board grid
def grid():
	bg = (235, 162, 250)
	grid = (0, 0, 50)
	window.fill(bg)
	for x in range(1,3):
		pygame.draw.line(window, grid, (0, 100 * x), (window_width,100 * x), lines_width)
		pygame.draw.line(window, grid, (100 * x, 0), (100 * x, window_height), lines_width)

# x and 0
def create_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(window, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), lines_width)
				pygame.draw.line(window, green, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), lines_width)
			if y == -1:
				pygame.draw.circle(window, blue, (x_pos * 100 + 50, y_pos * 100 + 50), 38, lines_width)
			y_pos += 1
		x_pos += 1	


def gameover_ch():
	global game_over
	global win

	x_pos = 0
	for x in markers:
		# columns
		if sum(x) == 3:
			win = 1
			game_over = True
		if sum(x) == -3:
			win = 2
			game_over = True
		#rows
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			win = 1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			win = 2
			game_over = True
		x_pos += 1

	# cross
	if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3:
		win = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3:
		win = 2
		game_over = True

	#tie
	if game_over == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		#if it is a tie, then call game over and set win to 0 (no one)
		if tie == True:
			game_over = True
			win = 0



def draw_game_over(win):

	if win != 0:
		end_text = "Player " + str(win) + " wins!"
	elif win == 0:
		end_text = "You have tied!"

	end_img = font.render(end_text, True, blue)
	pygame.draw.rect(window, green, (window_width // 2 - 100, window_height // 2 - 60, 200, 50))
	window.blit(end_img, (window_width // 2 - 100, window_height // 2 - 50))

	again_text = 'Play Again?'
	again_img = font.render(again_text, True, blue)
	pygame.draw.rect(window, green, play_again_rect)
	window.blit(again_img, (window_width // 2 - 80, window_height // 2 + 10))


#main loop
run = True
while run:

	#draw board and markers first
	grid()
	create_markers()

	#handle events
	for event in pygame.event.get():
		#handle game exit
		if event.type == pygame.QUIT:
			run = False
		#run new game
		if game_over == False:
			#check for mouseclick
			if event.type == pygame.MOUSEBUTTONDOWN and click == False:
				click = True
			if event.type == pygame.MOUSEBUTTONUP and click == True:
				click = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0] // 100
				cell_y = pos[1] // 100
				if markers[cell_x][cell_y] == 0:
					markers[cell_x][cell_y] = player
					player *= -1
					gameover_ch()

	#check if game has been won
	if game_over == True:
		draw_game_over(win)
		#check for mouseclick to see if we click on Play Again
		if event.type == pygame.MOUSEBUTTONDOWN and click == False:
			click = True
		if event.type == pygame.MOUSEBUTTONUP and click == True:
			click = False
			pos = pygame.mouse.get_pos()
			if play_again_rect.collidepoint(pos):
				#reset variables
				game_over = False
				player = 1
				pos = (0,0)
				markers = []
				win = 0
				#create empty 3 x 3 list to represent the grid
				for x in range (3):
					row = [0] * 3
					markers.append(row)

	#update display
	pygame.display.update()

pygame.quit()