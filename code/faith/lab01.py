distance = float(input('What is the distance?  '))
unit = input('What is the starting unit?  ')
unit2 = input('What unit do you want to convert to?  ')

if unit == 'ft':
    ft = distance * 0.3048
elif unit == 'mi':
    mi = distance * 1609.34
elif unit == 'm':
    m = distance
elif unit == 'km':
    km = distance * 1000
elif unit == 'yard':
    yard = distance * 0.9144
elif unit == 'inch':
    inch = distance * 0.0254

    trannum = distance*unit/unit2


if unit2 == 'ft':
    print(trannum)
elif unit == 'mi':
    print(trannum)
elif unit == 'm':
    print(trannum)
elif unit == 'km':
    print(trannum)
elif unit == 'yard':
    print(trannum)
elif unit == 'inch':
    print(trannum)
