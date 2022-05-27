#Lab16.py - Mini Capston: Cards Aginst Humanity Game

import pygame
from sys import exit
import random

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

        'Player 1:' : 0,
        'Player 2:' : 0,
        'Player 3:' : 0,
        'Player 4:' : 0,
        'Player 5:' : 0,

        }
    
    #print('Welcome to Cards Against Humanity - Family Edition!\nTo exit the pick_card_page at any time enter "quit".')

    while True:
        #Empty Lists
        random_responses_list = []

        #Pick random card from blackcards pile and show to player
        random_prompt = random.choice(blackcards)
        #print (f'\nBlackcard:\n{random_prompt}\n')


        #Show the player their 5 whitecards (responses)
        #print("Your whitecards are the following: ")

        for i,response in enumerate(range(5)):
            i += 1
            random_response= random.choice(whitecards)
            random_responses_list.append(random_response)
            # print (i, random_response)
    
        #Ask user which card they would like to play; pop() answer and append to list
        # selected_card = input("\nSelect your funniest answer (1, 2, 3, 4, or 5): ")
        selected_card = '1'
        if selected_card == "quit":
            break
        funniest_responses = []
        selected_card_index = funny_card[selected_card]
        funniest_card = random_responses_list[selected_card_index]
        funniest_responses.append(funniest_card)
        funniest_responses.pop()
        # print(funniest_card)

        #Add 4 more whitecards/responses to funniest_responses list for card Czar to choose from (*posing as 4 other players*)
        #print ("\nThe whitecards chosen for this round are: ")
        for card in range(4):
            random_computer_responses = random.choice(whitecards)
            funniest_responses.append(random_computer_responses)
        for i, card in enumerate(funniest_responses):
            i += 1
            # print ('fr', i, card)

        #Have the card Czar pick the funniest card
        winning_card = random.choice(funniest_responses)
        winning_card_index = funniest_responses.index(winning_card)
        # print ("\nThe winning card is...")
        # print (f'{winning_card}\n')
        

        #Add points to the winner of that round
        if winning_card_index == 0:
            players['Player 1:'] += 1
        elif winning_card_index == 1:
            players['Player 2:'] += 1
        elif winning_card_index == 2:
            players['Player 3:'] += 1
        elif winning_card_index == 3:
            players['Player 4:'] += 1
        elif winning_card_index == 4:
            players['Player 5:'] += 1
        # print(f'Player Points:\n-Player 1: {players["Player 1"]}\n-Player 2: {players["Player 2"]}\n-Player 3: {players["Player 3"]}\n-Player 4: {players["Player 4"]}\n-Player 5: {players["Player 5"]}')

        #End pick_card_page once one player reaches 5 points
        game_done = False
        for player in players:
            if players[player] == 5:
                #print(f'\n{player} wins!')
                game_done = True
        if game_done == True:
            break
    #Ask player if they would like to play again
    # play_again = input('Would you like to start a new game? yes or no? ')
    play_again = 'no'
    if play_again == 'yes':
        continue
    elif play_again == 'no':
        #print('Thank you for playing Cards Against Humanity - Family Edition')
        break
    break

#Pygame Code
player_info = {input('Enter your name to play game: ') : 0}

#Display Setup
pygame.init()
screen = pygame.display.set_mode((1100, 650))
pygame.display.set_caption('Cards Against Humanity - Family Edition')
clock = pygame.time.Clock()

#Text Setup
header_font = pygame.font.Font('basic_light.ttf', 50)
card_font = pygame.font.Font('basic_light.ttf', 25)
score_font = pygame.font.Font('basic_light.ttf', 20)
top = pygame.Surface((1100, 325))
top.fill('black')
header = header_font.render('Cards Against Humanity', True, 'white')
prompt = card_font.render(random_prompt, True, 'white')
winning_card = card_font.render(winning_card, True, 'black')
player_score = score_font.render('Player Scores:', True, 'white')
player_1 = card_font.render('1: ', True, 'black')
player_2 = card_font.render('2: ', True, 'black')
player_3 = card_font.render('3: ', True, 'black')
player_4 = card_font.render('4: ', True, 'black')
<<<<<<< HEAD
player_5 = card_font.render('Player 5: ', True, 'black')
=======
player_5 = card_font.render('5: ', True, 'black')
>>>>>>> 0dcac4f9f250e1793785b869e1907f960be613e2

#Button Setup
new_game_img = pygame.image.load('new_game_img.png').convert_alpha()
one_img = pygame.image.load('one.png').convert_alpha()
two_img = pygame.image.load('two.png').convert_alpha()
three_img = pygame.image.load('three.png').convert_alpha()
four_img = pygame.image.load('four.png').convert_alpha()
five_img = pygame.image.load('five.png').convert_alpha()
winning_card_img = pygame.image.load('winning_card.png').convert_alpha()
next_round_img = pygame.image.load('next_round.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        #self.image = image
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
            self.clicked = False

        #Add image on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return click

new_game_button = Button (325, 300, new_game_img, 1)
one_button = Button(20, 350,  one_img, 0.35)
two_button = Button(20, 390, two_img, 0.35)
three_button = Button(23, 430, three_img, 0.35)
four_button = Button(19, 468, four_img, 0.35)
five_button = Button(24, 510, five_img, 0.35)
winning_card_button = Button(425, 600, winning_card_img, 0.35)
next_round_button = (Button(425, 600, next_round_img, 0.35))

#Next Screen Setup
class GamePlay ():
    def __init__(self):
        self.play = 'intro'
    
    def intro (self):
        #Allow game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            screen.fill('black')
            if new_game_button.draw():
                self.play = 'pick_card_page'
                #print(self.play)
        screen.blit(header, (290,150))

        pygame.display.update()

    def pick_card_page(self):
        #Add game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            screen.fill('white')
            if one_button.draw():
                funniest_responses.append(random_responses_list[0])
                self.play = 'funniest_card_page'
            if two_button.draw():
                funniest_responses.append(random_responses_list[1])
                self.play = 'funniest_card_page'
            if three_button.draw():
                funniest_responses.append(random_responses_list[2])
                self.play = 'funniest_card_page'
            if four_button.draw():
                funniest_responses.append(random_responses_list[3])
                self.play = 'funniest_card_page'
            if five_button.draw():
                funniest_responses.append(random_responses_list[4])
                self.play = 'funniest_card_page'
        #Add header, prompt, and whitecards to page
        
        screen.blit(top, (0,0))
        screen.blit(header, (290,20))
        screen.blit(prompt, (10, 185))
        
        x = 70
        y = 350
        for response in random_responses_list:
            response_position = (x, y)
            response_display = card_font.render(response, True, 'black')
            screen.blit(response_display, (response_position))
            y += 40

        pygame.display.update()
    
    def funniest_card_page(self):
        #Add game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            screen.fill('white')
            if winning_card_button.draw():
                self.play = 'winning_card_page'
        
        #Add header, prompt, and funniest cards to page
        screen.blit(top, (0,0))
        screen.blit(header, (290,20))
        screen.blit(prompt, (10, 185))
        screen.blit(player_1, (20, 350))
        screen.blit(player_2, (20, 390))
        screen.blit(player_3, (20, 430))
        screen.blit(player_4, (20, 470))
        screen.blit(player_5, (20, 510))

<<<<<<< HEAD
        x = 150
=======
        x = 75
>>>>>>> 0dcac4f9f250e1793785b869e1907f960be613e2
        y = 350
        for funny_response in funniest_responses:
            funny_response_position = (x, y)
            funny_response_display = card_font.render(funny_response, True, 'black')
            screen.blit(funny_response_display, (funny_response_position))
            y += 40
            
        pygame.display.update()
    
    def winning_card_page(self):
        players = {

        'Player 1' : 0,
        'Player 2' : 0,
        'Player 3' : 0,
        'Player 4' : 0,

        }
        #Adds in player name
        players.update(player_info)

        #Add game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            screen.fill('white')
            if next_round_button.draw():
                self.play = 'next_round'
        #Add header, prompt, and winning card to page
        screen.blit(top, (0,0))
        screen.blit(header, (290,20))
        screen.blit(prompt, (10, 185))
        screen.blit(winning_card, (20, 350))
        screen.blit(player_score, (950 ,10)) 

        #Add player scores
        if winning_card_index == 0:
            players['Player 1'] += 1
        elif winning_card_index == 1:
            players['Player 2'] += 1
        elif winning_card_index == 2:
            players['Player 3'] += 1
        elif winning_card_index == 3:
            players['Player 4'] += 1
        elif winning_card_index == 4:
            players['Player 5'] += 1

        x = 950
        y = 40
        for player in players:
            player_score_position = (x, y)
            player_score_display = score_font.render(player, True, 'white')
            screen.blit(player_score_display, (player_score_position))
            y += 30
        
        score_x = 1050
        score_y = 40
        for player in players:
            score_position = (score_x, score_y)
            score_display = score_font.render(str(players[player]), True, 'white')
            screen.blit(score_display, (score_position))
            score_y += 30

        pygame.display.update()

game_play = GamePlay()
while True:

    while True:
        if game_play.play == 'intro':
            game_play.intro()
        if game_play.play == 'pick_card_page':
            game_play.pick_card_page()
        if game_play.play == 'funniest_card_page':
            game_play.funniest_card_page()
        if game_play.play == 'winning_card_page':
            game_play.winning_card_page()
        if game_play.play == 'next_round':
            break
    game_play.__init__()

    clock.tick(60)
