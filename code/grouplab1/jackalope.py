

"""create a dictionary list for population to exist"""

population = {
    "1": 0,
    "2": 0,
}
"""create a while loop to fill the dictionary with tuples representing individual jackalopes with pop id and age as value pair"""

def birth(x):
    for key in population:
        if population[key] >=4:
            population[-1] += 1
        print(population)

def life_cycle(population):
    x = 0
    while x < 11:
        for key in population:
            population[key] += 1
            print(type(population[key]),(population[key]))
        birth(population)
        x += 1
        print(population)
    print(population)

life_cycle(population)
""""""
population = 0

def birth():
    for key in population:
        if population[key] >=4:
            population[-1] += 1
        print(population)


life_cycle(population)









""""""





""""""





""""""





""""""