# """create a dictionary list for population to exist"""
# # population = {
# #     "1": 0,
# #     "2": 0,
# # }
# """create a while loop to fill the dictionary with tuples representing individual jackalopes with pop id and age as value pair"""
# # def birth(population, counter):
# #     for key in population:
# #         if population[key] >=4:
# #             population[counter+1] = 0
       
# #         print(population)
# jacks = [0,0]
# # def life_cycle(population):
# x = 0
# while len(jacks) <1000:
#     for i in jacks:
#         jacks[i] += 1
#         print(type(jacks[i]),jacks[i])
#     counter = len(jacks)
#     x += 1
#     print(jacks)
#     print(jacks)
# # life_cycle(population)
# """"""
# population = 0
# def birth():
#     for key in population:
#         if population[key] >=4:
#             population[-1] += 1
#         print(population)
# # life_cycle(population)
# # def life_cycle(population):
# #     pop = len(list(population))
# #     age = 0
# #     while True:
# #         age = age + 1
# #         if age > 4:
# #             pop + 1
# #         print(pop)
# """"""
# """"""
# """"""
# """"""
counter = 0
jacks = [0,0] # this is our list starting with two jacks
years = 0 # setting year 0 to count upwards
while len(jacks) < 1000:
    # age jacks
    for i in range(len(jacks)):
        jacks[i] += 1
        # print(f"jacks: {jacks}") # [0,0]
    # birth jacks
    for jack in jacks:
        if jack >= 4 and jack <= 8:
            jacks.append(0)
    d_list =[]
    print(f"jacks:{jacks}")
    for i in range(len(jacks)):
        if jacks[i] > 9:
            # jacks.pop(i)
            dead = jacks.pop(i)
            d_list.append(dead)
            # d_list.append(dead)
            print(f"jacks cemetary: {d_list}")
            # jacks.remove(jacks[i])
        else:
            break
    print(f"jacks cemetary: {d_list}")    
    for jack in jacks:
        if jack > 10:
            jacks.remove(jack)        
      
    # print(jacks[jack],jacks[jack])
    # print(jacks)
    years += 1    
    counter = len(jacks)
    print(f"year: {years}, pop: {counter}")
print(jacks)
    # print(jacks)