# create the dictionary and assign the unit key to the equivalent distance in meters
meter_conversion = {'ft': .3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'y': .9144, 'in': .0254}

# make it repeatable
while True:
    print("\n\n\nYour unit choices are ft, mi, m, km")

#ask the user for the unit they would like to use and assign it to a variable
    unit_input = input("\nPlease enter the unit you would like converted or type 'done' to quit: ")

#end the game if done
    if unit_input == 'done':
        break

#ask the user to enter the amount of unit they want converted and assign it to a variable
    unit_amount = input(f"\nHow many {unit_input} do you want converted?: ")

# convert the number of unit from a string to a float
    unit_amount = float(unit_amount)

#determine the amount of meters by using the dictionary pair for unit input
    total_meters = meter_conversion[unit_input] * unit_amount

# ask the user for the type of unit output
    unit_output = input(f"\nWhat unit would you like {unit_amount} {unit_input} converted to?: ")

#convert the total_meters of the orignal unit into the desired output
    conversion_output = total_meters / meter_conversion[unit_output]

#print the amount of meters the unit is
    print(f"\n{unit_amount} {unit_input} is: {conversion_output} {unit_output}")
