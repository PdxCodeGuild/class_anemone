#Lab16.py - Mini Capston: Cards Aginst Humanity Game

import pygame
from sys import exit
import random
import textwrap

#Open prompts/blackcards csv file and convert into list of prompts
with open ('CAH_Family_Edition-prompts.csv', encoding="utf-8-sig") as file:
    lines = file.read().split('\n')

prompts = []
for line in lines:
    prompts.append(line.split('.,\n'))

key = prompts.pop(0)

blackcards = [prompt[0] for i, prompt in enumerate(prompts)]

#Open responses/whitecards csv file and convert into list of responses
with open ('CAH_Family_Edition-responses.csv', encoding="utf-8-sig") as file2:
    rows = file2.read().split('\n')

responses = []
for row in rows:
    responses.append(row.split('.,\n'))

key = responses.pop(0)

whitecards = [response[0] for i, response in enumerate(responses)]

#Dictionary for picking cards
funny_card = {

    '1' : 0,
    '2' : 1,
    '3' : 2,
    '4' : 3,
    '5' : 4,
}

#Game Code
while True:
    #Player Points Dictionary
    players = {

        'player1' : 0,
        'player2' : 0,
        'player3' : 0,
        'player4' : 0,
        'player5' : 0,

        }
    print('Welcome to Cards Against Humanity - Family Edition!\nTo exit the game at any time enter "quit".')

    while True:
        #Empty Lists
        random_responses_list = []
        funniest_responses = []

        #Pick random card from blackcards pile and show to player
        random_prompt = random.choice(blackcards)
        print (f'\nBlackcard:\n{random_prompt}\n')


        #Show the player their 5 whitecards (responses)
        print("Your whitecards are the following: ")

        for i,response in enumerate(range(5)):
            i += 1
            random_response= random.choice(whitecards)
            random_responses_list.append(random_response)
            print (i, random_response)
    
        #Ask user which card they would like to play; pop() answer and append to list
        selected_card = input("\nSelect your funniest answer (1, 2, 3, 4, or 5): ")
        if selected_card == "quit":
            break
        selected_card_index = funny_card[selected_card]
        funniest_card = random_responses_list.pop(selected_card_index)
        funniest_responses.append(funniest_card)
        print(funniest_card)

        #Add 3 more whitecards/responses to funniest_responses list for card Czar to choose from (*posing as 3 other players*)
        print ("\nThe whitecards chosen for this round are: ")
        for card in range(4):
            random_computer_responses = random.choice(whitecards)
            funniest_responses.append(random_computer_responses)
        for i, card in enumerate(funniest_responses):
            i += 1
            print (i, card)

        #Have the card Czar pick the funniest card
        winning_card = random.choice(funniest_responses)
        winning_card_index = funniest_responses.index(winning_card)
        print ("\nThe winning card is...")
        print (f'{winning_card}\n')
        

        #Add points to the winner of that round
        if winning_card_index == 0:
            players['player1'] += 1
        elif winning_card_index == 1:
            players['player2'] += 1
        elif winning_card_index == 2:
            players['player3'] += 1
        elif winning_card_index == 3:
            players['player4'] += 1
        elif winning_card_index == 4:
            players['player5'] += 1
        print(f'Player Points:\n-Player 1: {players["player1"]}\n-Player 2: {players["player2"]}\n-Player 3: {players["player3"]}\n-Player 4: {players["player4"]}\n-Player 5: {players["player5"]}')

        #End game once one player reaches 5 points
        game_done = False
        for player in players:
            if players[player] == 5:
                print(f'\n{player} wins!')
                game_done = True
        if game_done == True:
            break
    #Ask player if they would like to play again
    play_again = input('Would you like to start a new game? yes or no? ')
    if play_again == 'yes':
        continue
    elif play_again == 'no':
        print('Thank you for playing Cards Against Humanity - Family Edition')
        break
    break

#Pygame Code

#Display Setup
pygame.init()
screen = pygame.display.set_mode((1100, 650))
pygame.display.set_caption('Cards Against Humanity - Family Edition')
clock = pygame.time.Clock()

#Text Setup
header_font = pygame.font.Font('basic_light.ttf', 50)
card_font = pygame.font.Font('basic_light.ttf', 25)
blackcard = pygame.Surface((1100, 325))
blackcard.fill('black')
header = header_font.render('Cards Against Humanity', True, 'white')
prompt = card_font.render(random_prompt, True, 'white')
response = card_font.render(random_response, True, 'black')

#Button Setup
new_game_img = pygame.image.load('new_game_img.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        #Allow for mouse clicks
        click = False
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                click = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked == False

        #Add image on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return click

new_game_button = Button (325, 300, new_game_img, 0.5)

#Next Screen Setup
class GamePlay ():
    def __init__(self):
        self.play = 'game'
    
    def intro (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #Add header and start button
        screen.fill('black')
        screen.blit(header, (290,150))
        if new_game_button.draw():
            #go to next screen
            pass

        pygame.display.update()

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #Add header, prompts, and responses to game
        screen.fill('white')
        screen.blit(blackcard, (0,0))
        screen.blit(header, (290,20))
        screen.blit(prompt, (10, 150))
        screen.blit(response, (10, 350))

        pygame.display.update()
    
    def game_manager(self):
        if self.play == 'intro':
            self.intro
        if self.play == 'game':
            self.game


game_play = GamePlay()
while True:
    game_play.intro()



    
    clock.tick(60)
