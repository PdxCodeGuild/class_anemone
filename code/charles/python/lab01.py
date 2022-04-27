# distance_dict = {'ft': 0.3048, 
#                 'mi': 1609.34, 
#                 'km': 1000, 
#                 'yd': 0.9144, 
#                 'in': 0.0254,
#                 'm': 1}


mi = ['mi', 'miles', 'mile']
m = ['meter', 'm', 'meters']
ft = ['ft', 'foot', 'feet']
km = ['kilo', 'kilometers', 'kilos', 'kilometer', 'km']
yd = ['yd', 'yards', 'yard']
inch = ['in', 'inches', 'inch']

valid_units = []
valid_units.extend(mi)
valid_units.extend(m)
valid_units.extend(ft)
valid_units.extend(km)
valid_units.extend(yd)
valid_units.extend(inch)



from_distance = int(input('What is the numerical distance? '))
from_unit = input(f'Valid units are: {", ".join(valid_units)} \nWhat are the units to convet from? ').lower()
to = input('What are the units to convet to? ').lower()

print(f"{from_distance}{from_unit} to {to}")




if from_unit in km and to in mi:
    print(from_distance * 1000 / 1609.34)
elif from_unit in km and to in m:
    print(from_distance * 1000)
elif from_unit in km and to in yd:
    print(from_distance * 1000 / 0.9144)
elif from_unit in km and to in ft:
    print(from_distance * 1000 / 0.3048)
elif from_unit in km and to in inch:
    print(from_distance * 1000 / 0.0254)

if from_unit in mi and to in km:
    print(from_distance * 1609.34 / 1000)
elif from_unit in mi and to in m:
    print(from_distance * 1609.34)
elif from_unit in mi and to in ft:
    print(from_distance * 1609.34 / 0.3048)
elif from_unit in mi and to in yd:
    print(from_distance * 1609.34 / 0.9144)
elif from_unit in mi and to in inch:
    print(from_distance * 1609.34 / 0.0254)

if from_unit in yd and to in mi:
    print(from_distance * 0.9144 / 1609.34)
elif from_unit in yd and to in m:
    print(from_distance * 0.9144)
elif from_unit in yd and to in ft:
    print(from_distance * 0.9144 / 0.3048)
elif from_unit in yd and to in inch:
    print(from_distance * 0.9144 / 0.0254)
elif from_unit in yd and to in km:
    print(from_distance * 0.9144 / 1000)

if from_unit in ft and to in mi:
    print(from_distance * 0.3048 / 1609.34)
elif from_unit in ft and to in m:
    print(from_distance * 0.3048)
elif from_unit in ft and to in yd:
    print(from_distance * 0.3048 / 0.9144)
elif from_unit in ft and to in km:
    print(from_distance * 0.3048 / 1000)
elif from_unit in ft and to in inch:
    print(from_distance * 0.3048 / 0.0254)

if from_unit in inch and to in mi:
    print(from_distance * 0.0254 / 1609.34)
elif from_unit in inch and to in m:
    print(from_distance * 0.0254)
elif from_unit in inch and to in yd:
    print(from_distance * 0.0254 / 0.9144)
elif from_unit in inch and to in km:
    print(from_distance * 0.0254 / 1000)
elif from_unit in inch and to in ft:
    print(from_distance * 0.0254 / 0.3048)

if from_unit in m and to in mi:
    print(from_distance / 1609.34)
elif from_unit in m and to in km:
    print(from_distance / 1000)
elif from_unit in m and to in yd:
    print(from_distance / 0.9144)
elif from_unit in m and to in ft:
    print(from_distance / 0.3048)
elif from_unit in m and to in inch:
    print(from_distance / 0.0254)

