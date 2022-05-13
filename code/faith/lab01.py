distance = float(input('What is the distance?  '))
unit = input('What is the starting unit?  ')
unit2 = input('What unit do you want to convert to?  ')

if unit == 'ft':
    result = distance * 0.3048
elif unit == 'mi':
    result = distance * 1609.34
elif unit == 'm':
    result = distance
elif unit == 'km':
    result = distance * 1000
elif unit == 'yard':
    result = distance * 0.9144
elif unit == 'inch':
    result = distance * 0.0254
    
 
print(result)

if unit2 == 'ft':
    print(result/0.3048)
elif unit2 == 'mi':
    print(result/1609.34)
elif unit2 == 'm':
    print(result)
elif unit2 == 'km':
    print(result/1000)
elif unit2 == 'yard':
    print(result/0.9144)
elif unit2 == 'inch':
    print(result/0.0254)
