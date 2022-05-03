'''Jackalope Simulator'''
# Authors: Rachel, Isaac, Bailey

population = 2

jackalope_1 = [5]
jackalope_2 = [9]
new_born = []

def check_age(jackalope_1, jackalope_2):
    for age in jackalope_1 and jackalope_2:
        if age > 4 and age < 8:
            new_born.append(0)

            print("Breedable! YAY!")
        elif age >= 9:
            print("Dead")
        else:
            print("Wait a while")
    return jackalope_1, jackalope_2

check_age(jackalope_1, jackalope_2)
print(new_born)


