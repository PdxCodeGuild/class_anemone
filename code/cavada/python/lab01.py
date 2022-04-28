# # version 1
# input("press any key to proceed")
# print("==================\nversion1")
# user = float(input("how tall are you in feet? "))
# if user:
#     user *= .3048
#     conversion = round(user, 2)
#     print(f"you are {conversion} meters tall")

# # version 2 & 3
# input("press any key to proceed")
# print("==================\nversion2")
# user = (input("""
# Enter the unit of measurement to convert to meters"
# options:
#     -inches
#     -feet
#     -yards
#     -miles
#     -kilometers
#     -meters 
# """))

# if "feet" in user or "ft" in user or "f" in user:
#     measure = float(input("enter value: "))
#     convert = measure * .3048
#     x = round(convert, 2)
#     print(f"Conversion: {measure} {user} = {x} meters\n==================")
# elif "inches" in user or "in" in user or "inch" in user or "'" or "i" in user:
#     measure = float(input("enter value: "))
#     convert = measure * .0254
#     x = round(convert, 2)
#     print(f"Conversion: {measure} {user} = {x} meters\n==================")
# elif "yards" in user or "yard" in user or "y" in user:
#     measure = float(input("enter value: "))
#     convert = measure * .9144
#     x = round(convert, 2)
#     print(f"Conversion: {measure} {user} = {x} meters\n==================")
# elif "miles" in user or "mile" in user or "mi" in user or "m" in user:
#     measure = float(input("enter value: "))
#     convert = measure * 1609.34
#     x = round(convert, 2)
#     print(f"Conversion: {measure} {user} = {x} meters\n==================")
# elif "kilometers" in user or "kilo" in user or "km" in user or "k" in user:
#     measure = float(input("enter value: "))
#     convert = measure * 1000
#     x = round(convert, 2)
#     print(f"Conversion: {measure} {user} = {x} meters\n==================")    
# elif "meters" in user or "m" in user:
#     measure = float(input("enter value: "))
#     convert = measure * 1
#     x = round(convert, 2)
#     print(f"Conversion: {measure} {user} = {x} meters\n==================")    
# else: 
#     print("error: program terminated")
valid_ft = ['f', 'ft', 'fet', 'foot', 'feet']
valid_in = ['i', 'in', 'inch', 'inches', 'inc']
valid_yd = ['y', 'yd', 'ya', 'yar', 'yard', 'yards']
valid_m = ['m', 'me', 'met', 'mete', 'meter', 'meters']
valid_km = ['km', 'ki', 'kil', 'kilo', 'kilom', 'kilome', 'kilomete', 'kilometer', 'kilometers']
valid_mi = ['mi', 'mil', 'mile', 'miles']

# version 4
while True:
    input("press any key to proceed")
    print("""
List of conversion options:
    -inch
    -feet
    -yard
    -meter
    -km
    -mile""")
    orig = input("what unit to convert from? ")
    end = input("What unit to convert to? ")
    dist = float(input("enter the distance to convert: "))
    if orig in valid_in:
        print(orig, "inch")
        if end in valid_in:
            conv = (round(dist * 1, 3))
            print(f"{dist} {orig}es = {conv} {end}es")
        elif end in valid_ft:
            conv = (round(dist / 12, 3))
            print(f"{dist} {orig}es = {conv} {end}")
        elif end in valid_yd:
            conv = (round(dist / 36, 3))
            print(f"{dist} {orig}es = {conv} {end}s")
        elif end in valid_m:    
            conv = (round(dist / 39.37, 3))
            print(f"{dist} {orig}es = {conv} {end}s")
        elif end in valid_km:
            conv = (round(dist / 39370, 3))
            print(f"{dist} {orig}es = {conv} {end}")
        elif end in valid_mi:
            conv = (round(dist / 63360, 3))
            print(f"{dist} {orig}es = {conv} {end}s")  
        else:
            print("error: program terminated")  
    elif orig in valid_ft:
        print(orig, "feet")
        if end in valid_in:
            conv = (round(dist * 12, 3))
            print(f"{dist} {orig} = {conv} {end}es")
            print(orig)
        elif end in valid_ft:
            conv = (round(dist * 1, 3))
            print(f"{dist} {orig} = {conv} {end}")
        elif end in valid_yd:
            conv = (round(dist / 3, 3))
            print(f"{dist} {orig} = {conv} {end}s")    
        elif end in valid_m:    
            conv = (round(dist / 3.281, 3))
            print(f"{dist} {orig} = {conv} {end}s")
        elif end in valid_km:
            conv = (round(dist / 3281, 3))
            print(f"{dist} {orig} = {conv} {end}")
            print("end is in km")
        elif end in valid_mi:
            conv = (round(dist / 5280, 3))
            print(f"{dist} {orig}es = {conv} {end}s")   
        else:
            print("error: program terminated")
    elif orig in valid_yd:
        print(orig, "yard")
        if end in valid_in:
            conv = (round(dist * 36, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
            print(orig)
        elif end in valid_ft:
            conv = (round(dist * 3, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_yd:
            conv = (round(dist * 1, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif end in valid_m:    
            conv = (round(dist / 1.094, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif end in valid_km:
            conv = (round(dist / 1094, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_mi:
            conv = (round(dist / 1760, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        else:
            print("error: program terminated")
    elif orig in valid_m:
        print(orig, "meter")
        if end in valid_in:
            conv = (round(dist * 39.37, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
        elif end in valid_ft:
            conv = (round(dist * 3.281, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_yd:
            conv = (round(dist * 1.094, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif end in valid_m:    
            conv = (round(dist / 1, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif end in valid_km:
            conv = (round(dist / 1000, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_mi:
            conv = (round(dist / 1609, 2))
            print(f"{dist} {orig}s = {conv} {end}s") 
        else:
            print("error: program terminated")
    elif orig in valid_km:
        print(orig, "km")
        if end in valid_in:
            conv = (round(dist * 39370, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
        elif end in valid_ft:
            conv = (round(dist * 3281, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_yd:
            conv = (round(dist * 1094, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif end in valid_m:    
            conv = (round(dist / 1000, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif end in valid_km:
            conv = (round(dist / 1, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_mi:
            conv = (round(dist / 1.609, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        else:
            print("error: program terminated")
    elif orig in valid_mi:
        print(orig, "mile")
        if end in valid_:
            conv = (round(dist * 63360, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
        elif end in valid_in:
            conv = (round(dist * 5280, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_yd:
            conv = (round(dist * 1760, 3))
            print(f"{dist} {orig}es = {conv} {end}s")
        elif end in valid_m:    
            conv = (round(dist / 1609, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif end in valid_km:
            conv = (round(dist / 1.609, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif end in valid_mi:
            conv = (round(dist / 1, 3))
            print(f"{dist} {orig}s = {conv} {end}s")  
        else:
            print("error: program terminated")


