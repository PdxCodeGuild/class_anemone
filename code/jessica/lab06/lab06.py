credit_card = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"
credit_card_split = credit_card.split()
credit_card_map = map(int, credit_card_split)
list_of_integers = list(credit_card_map)
print(list_of_integers)

#Removing check digit
list_of_integers.pop()
print(list_of_integers)

#Reversing the list
list_of_integers.reverse()
print(list_of_integers)

#Double every other element in the reversed list
reversed_list = [ele + ele for ele in list_of_integers]
print(reversed_list)

