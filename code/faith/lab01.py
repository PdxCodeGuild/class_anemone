distance = float(input('What is the distance?  '))
unit = input('What is the starting unit?  ')
unit2 = input('What unit do you want to convert to?  ')

if unit == 'ft':
    print(distance * 0.3048)
elif unit == 'mi':
    print(distance * 1609.34)
elif unit == 'm':
    print(distance)
elif unit == 'km':
    print(distance * 1000)
elif unit == 'yard':
    print(distance * 0.9144)
elif unit == 'inch':
    print(distance * 0.0254)
