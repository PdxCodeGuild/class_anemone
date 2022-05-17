

values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 }

player_score = []

input_1 = input('What is your first card?').upper()
input_2 = input(' What is your second card?').upper()
input_3 = input('What is your third card?').upper()




player_score.append(values[input_1])
player_score.append(values[input_2])
player_score.append(values[input_3])

final = sum(player_score)

if final > 21:
    print('Busted')
elif final == 21 :
    print('BLACKJACK!')
elif final >= 17 :
    print(f'Your score is {final}, you should stay')
elif final < 17:
    print(f'Your score is {final} you should hit')






