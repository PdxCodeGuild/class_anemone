#Lab16.py - Mini Capston: Cards Aginst Humanity Game

import pygame
from sys import exit
import random

#Open prompts/bluecareds csv file and convert into list of prompts
with open ('CAH_Family_Edition-prompts.csv', encoding="utf-8-sig") as file:
    lines = file.read().split('\n')

prompts = []

for line in lines:
    prompts.append(line.split('.,\n'))

key = prompts.pop(0)

bluecards = [prompt[0] for i, prompt in enumerate(prompts)]

#Open responses/pinkcards csv file and convert into list of responses
with open ('CAH_Family_Edition-responses.csv', encoding="utf-8-sig") as file2:
    rows = file2.read().split('\n')

responses = []

for row in rows:
    responses.append(row.split('.,\n'))

key = responses.pop(0)

pinkcards = [response[0] for i, response in enumerate(responses)]

#Pick random card from bluecard pile
random_prompt = random.choice(bluecards)


#Pygame Code
pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill('mintcream')
pygame.display.set_caption('Cards Against Humanity - Family Edition')
clock = pygame.time.Clock()
header_font = pygame.font.Font(None, 50)
card_font = pygame.font.Font(None, 25)

bluecard = pygame.Surface((145, 195))
bluecard.fill('paleturquoise3')

pinkcard = pygame.Surface((0,0))
pinkcard.fill('lightpink2')

header = header_font.render('Cards Against Humanity', True, 'black')
prompt = card_font.render(random_prompt, True, 'black') #Need to wrap font

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Add bluecard stack to game
    screen.blit(bluecard, (325,75))
    screen.blit(header, (200,20))
    screen.blit(prompt, (330, 100))

    pygame.display.update()
    clock.tick(60)
