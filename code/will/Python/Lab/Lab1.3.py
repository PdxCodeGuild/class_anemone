



program_units = {
    'ft': .3048,
    'miles': 1609.34,
    'meters': 1,
    'km' : 1000,
    'yards' : .9144,
    'inches' : .0254
}

user_request = input('Please enter which unit you wish to convert to Meters. ft/miles/meters/km/yards/inches ')
conversion = program_units[user_request] 

value = input(' Please enter the units value for your conversion ')

solution = float(conversion) * int(value) 

print(f'The value you entered is {solution} Meters!') 

