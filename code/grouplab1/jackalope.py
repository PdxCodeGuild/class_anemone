

"""create a dictionary list for population to exist"""

population = {
    "1": 0,
    "2": 0,
}
"""create a while loop to fill the dictionary with tuples representing individual jackalopes with pop id and age as value pair"""
x = 0
while x < 11:
    for key in population:
        population[key] += 1
        print(type(population[key]),(population[key]))
        
    x += 1
    print(population)
print(population)
""""""





""""""





""""""





""""""





""""""