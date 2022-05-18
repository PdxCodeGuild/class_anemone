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
