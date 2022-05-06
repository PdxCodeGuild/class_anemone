

card = []
nums = [2,3,4,5,6,7,8,9,10]
# cards = {'a':1, 'q':10, 'j':10, 'k':10, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}
letters = ['a', 'q', 'j', 'k']
for i in letters:
    player = input('if card: ')
    if 'a' in player:
        letters[0] = 1
        card.append(letters[0])
    elif 'q' in player:
        letters[1] = 10
        card.append(letters[1])
    elif 'j' in player:
        letters[1] = 10
        card.append(letters[2])
    elif 'k' in player:
        letters[1] = 10
        card.append(letters[3])
    # elif len(nums) in player:
    #     card.append(nums)
print(card)