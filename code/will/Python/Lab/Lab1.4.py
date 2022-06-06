

ft = 0.3048
mi = 1609.34
m = 1
km = 1000
yd = 0.9144
inch = 0.0254




user_units = input('Please enter which unit you wish to convert from. Supported Units: ft / miles / meters / km / yards / inches ')

user_output = input(' Please enter which unit you wish to convert to. Supported Units: ft / miles / meters / km/ yards/ inches  ')

user_value = input(' Please enter the distance value for conversion  ')


if user_units == 'ft':
    intermediate = int(user_value) * ft
elif user_units == 'miles':
    intermediate = int(user_value) * mi
elif user_units == 'meters':
    intermediate = int(user_value) * m
elif user_units == "km":
    intermediate = int(user_value) * km
elif user_units == 'yards':
    intermediate = int(user_value) * yd
elif user_value == 'inches':
    intermediate = int(user_value) * inch


if user_output == user_units:
    final = user_value
else:
    if user_output == 'ft':
        final = int(intermediate) / 0.3048
    elif user_output == 'miles':
        final = int(intermediate) / 1609.34
    elif user_output == 'meters':
        final = int(intermediate) / 1 
    elif user_output == 'km' :
        final = int(intermediate) / 1000
    elif user_output == 'yards':
        final = int(intermediate) / .9144
    elif user_output == 'inches':
        final = int(intermediate) / .0254

print(f'Your final value is {final} and the units are {user_output}')


