




program_units = {
    'ft': .3048,
    'miles': 1609.34,
    'meters': 1,
    'km' : 1000,
    'yards' : .9144,
    'inches' : .0254
}

user_units = input('Please enter which unit you wish to convert from. Supported Units: ft / miles / meters / km / yards / inches ')

user_output = input(' Please enter which unit you wish to convert to. Supported Units: ft / miles / meters / km/ yards/ inches  ')

user_value = input(' Please enter the distance value for conversion  ')

if user_units ==  user_output:
    print(f"***You have selected the same units! The Answer to your calculation is {user_value}***")
    solution = int(user_value) * 1 
elif user_units == 'ft':
    solution = int(user_value) * .3048 
elif user_units == 'miles':
    solution = int(user_value) * 1609.34
elif user_units == 'meters':
    solution = int(user_value) * 1 
elif user_units == "km":
    solution = int(user_value) * 1000
elif user_units == 'yards':
    solution = int(user_value) * .9144
elif user_value == 'inches':
    solution = int(user_value) *.0254


if user_output == "ft":
    final = int(solution) / 0.3048
elif user_output == 'miles':
    final = int(solution) / 1609.34
elif user_output == 'meters':
    final = int(solution) / 1 
elif user_output == 'km' :
    final = int(solution) / 1000
elif user_output == 'yards':
    final = int(solution) / .9144
elif user_output == 'inches':
    final = int(solution) / .0254

print(f'Your final value is {final} and the units are {user_output}')


#I believe I have fixed the issue that Liz pointed out on slack!