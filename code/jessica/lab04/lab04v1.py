
#--------Lab04----------#

#Getting the players input
first_card = input('What\'s your first card? ')
second_card = input('What\'s your second card? ')
third_card = input('What\'s your third card? ')

#A function for each card input
def card_num_1():
    if first_card == 'A':
        return 1
    elif first_card == '2':
        return 2
    elif first_card == '3':
        return 3
    elif first_card == '4':
        return 4
    elif first_card == '5':
        return 5
    elif first_card == '6':
        return 6
    elif first_card == '7':
        return 7
    elif first_card == '8':
        return 8
    elif first_card == '9':
        return 9
    elif first_card == '10':
        return 10
    elif first_card == 'j':
        return 10
    elif first_card == 'q':
        return 10
    elif first_card == 'k':
        return 10

def card_num_2():
    if second_card == 'A':
        return 1
    elif second_card == '2':
        return 2
    elif second_card == '3':
        return 3
    elif second_card == '4':
        return 4
    elif second_card == '5':
        return 5
    elif second_card == '6':
        return 6
    elif second_card == '7':
        return 7
    elif second_card == '8':
        return 8
    elif second_card == '9':
        return 9
    elif second_card == '10':
        return 10
    elif second_card == 'j':
        return 10
    elif second_card == 'q':
        return 10
    elif second_card == 'k':
        return 10

def card_num_3():
    if third_card == 'A':
        return 1
    elif third_card == '2':
        return 2
    elif third_card == '3':
        return 3
    elif third_card == '4':
        return 4
    elif third_card == '5':
        return 5
    elif third_card == '6':
        return 6
    elif third_card == '7':
        return 7
    elif third_card == '8':
        return 8
    elif third_card == '9':
        return 9
    elif third_card == '10':
        return 10
    elif third_card == 'j':
        return 10
    elif third_card == 'q':
        return 10
    elif third_card == 'k':
        return 10

##Assigned each input a value from the cars through the functions. Print statements nonetype the value. DO NOT do too much on one line
first_card_val = card_num_1()
second_card_val = card_num_2()
third_card_val = card_num_3()

total = first_card_val + second_card_val + third_card_val

###Checking the type
#print(type(first_card_val))

if total < 17 and total < 21:
    print(f"{total} Hit")
elif total >= 17:
    print(f"{total} Stay")
elif total == 21:
    print(f"{total} Blackjack!")
elif total > 21:
    print(f"{total} Already Busted!")