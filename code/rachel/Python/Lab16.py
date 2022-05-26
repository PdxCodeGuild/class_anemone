#Lab16.py - Mini Capston: Cards Aginst Humanity Game

# Game Rules:
#     One Player Option:
#     - Player who pooped most recently goes first as card Czar (yes or no?)
#     - The card Czar will draw a blackcard(prompt) and read it allowed (computer randomly draws card)
#     - The player will draw 5 whitecards(responses) and choose which whitecard they want to play (5 cards randomly drawn; player will use index to pick a card)
#     - The card Czar will decide which whitecard is the funniest (use random.choice and have computer pick between players card and 3 other random cards)
#     - Winning player for that round gets a point added to their total card count (counter); first player to 5 points wins!
#     - After each round ends, the next player becomes the card Czar

#     Multiplayer Option:
#     - Player who pooped most recently goes first as card Czar (last few minutes, hours, days - most recent goes first)
#     - The card Czar will draw a blackcard(prompt) and read it allowed (computer randomly draws card)
#     - The other players will draw 5 whitecards(responses) and choose which whitecard they want to play (5 cards randomly drawn; player will use index to pick a card)
#     - The card Czar will decide which white card is the funniest (list out whitecards and allow user input to pick index for winning card)
#     - Winning player for that round gets a point added to their total card count (counter); first player to 5 points wins!
#     - After each round ends, the next player becomes the card Czar


# import pygame
# from sys import exit
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

#Open responses/whitecards
# csv file and convert into list of responses
with open ('CAH_Family_Edition-responses.csv', encoding="utf-8-sig") as file2:
    rows = file2.read().split('\n')

responses = []
for row in rows:
    responses.append(row.split('.,\n'))

key = responses.pop(0)

whitecards = [response[0] for i, response in enumerate(responses)]

#Pick random card from blackcards pile
random_prompt = random.choice(blackcards)

#Dictionary for picking cards

funny_card = {

    '1' : 0,
    '2' : 1,
    '3' : 2,
    '4' : 3,
    '5' : 4,

}

players = {

    'player1' : 0,
    'player2' : 0,
    'player3' : 0,
    'player4' : 0,
    'player5' : 0,

}


#Empty Lists
random_responses_list = []
funniest_responses = []

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

        x = 75
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
    print("Welcome to Cards Against Humanity - Family Edition!\n")
    
    #Show the player the blackcard (prompt)
    print (f'Blackcard:\n{random_prompt}\n')


    #Show the player their 5 whitecards (responses)
    print("Your whitecards are the following: ")

    for i,response in enumerate(range(5)):
        i += 1
        random_response= random.choice(whitecards)
        random_responses_list.append(random_response)
        print (i, random_response)
    
    #Ask user which card they would like to play; pop() answer and append to list
    selected_card = input("\nSelect your funniest answer (1, 2, 3, 4, or 5): ")
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
    print ("\nThe winning card is...\n")
    print (winning_card)

    #Add points to the winner of that round
    if winning_card == 0:
        players['player1'] + 1
    elif winning_card == 1:
        players['player2'] + 1
    elif winning_card == 2:
        players['player3'] + 1
    elif winning_card == 3:
        players['player4'] + 1
    elif winning_card == 4:
        players['player5'] + 1

#NOT WORKING):
    print(f'Player Points:\n-Player 1: {players["player1"]}\n-Player 2: {players["player2"]}\n-Player 3: {players["player3"]}\n-Player 4: {players["player4"]}\n-Player 5: {players["player5"]}')

    break

    






# #Pygame Code
# pygame.init()
# screen = pygame.display.set_mode((800,600))
# screen.fill('mintcream')
# pygame.display.set_caption('Cards Against Humanity - Family Edition')
# clock = pygame.time.Clock()
# header_font = pygame.font.Font(None, 50)
# card_font = pygame.font.Font(None, 25)

# bluecard = pygame.Surface((145, 195))
# bluecard.fill('paleturquoise3')

# pinkcard = pygame.Surface((0,0))
# pinkcard.fill('lightpink2')

# header = header_font.render('Cards Against Humanity', True, 'black')
# # prompt = card_font.render(random_prompt, True, 'black') #Need to wrap font

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     #Add game header/title
#     screen.blit(header, (200,20))

#     #Add bluecard stack to game
#     screen.blit(bluecard, (325,75))
#     screen.draw.text(random_prompt, (330, 100), width=30)

#     pygame.display.update()
#     clock.tick(60)
