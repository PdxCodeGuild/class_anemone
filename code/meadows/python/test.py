meter_convert_dict = {'ft': 0.3048, 'mile': 1609.34, 'meter': 1, 'km': 1000, 'yard': 0.9144, 'inch': 0.0254}
print('\nCONVERT UNIT MEASUREMENT TO METER!')
distance = int(input('\nwhat is the distance in digits?: '))
print(f"\nYou can choose {', '.join(meter_convert_dict)}")
unit = input('\nWhat are the units?: ').lower()
unit = meter_convert_dict[unit]
b = unit * distance

print(f'\nis = {round(b, 2)} meters\n')

 meters = ['meter', 'meters']
    feets = ['ft', 'feet']
    kilos = ['km', 'kilo', 'kilometer']
    miles = ['mi', 'mile', 'miles']
    yards = ['yard', 'yards', 'yrd']
    inchs = ['inch', 'in', 'inches']


    elif ref[4] in units:
    b = dist(units_dist, yards)
    len_feet = b / feet
    print(len_feet)
    print(f'{a} meters')
elif ref[3] in units:
    c = dist(units_dist, miles)
    print(f'{a} meters')
elif ref[2] in units:
    d = dist(units_dist, kilos)
    print(f'{a} meters')
elif ref[1] in units:
    e = dist(units_dist, feet)
    print(f'{a} meters')
elif ref[0] in units:
    f = dist(units_dist, meters)
    print(f'{a} meters')

    if ref[5] in units:
    a = dist(units_dist, inchs)
    if ref[1] in unit_con:
        len_feet = a / feet
        print(f'{units_dist} {units} is {len_feet} feet')
    elif ref[2] in unit_con:
        len_kilos = a / kilos
        print(f'{units_dist} {units} is {len_kilos} kilos')
    elif ref[3] in unit_con:
        len_miles = a / miles
        print(f'{units_dist} {units} is {len_miles} miles')
    elif ref[4] in unit_con:
        len_yards = a / yards
        print(f'{units_dist} {units} is {len_feet} yards')
    elif ref[0] in unit_con:
        len_meters = a / meters
        print(f'{units_dist} {units} is {len_feet} meters')