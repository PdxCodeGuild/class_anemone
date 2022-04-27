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
    if "in" in orig or "inch" in orig or "inches" in orig:
        print(orig, "inch")
        if "in" in end or "inch" in end or "inches" in end:
            conv = (round(dist * 1, 3))
            print(f"{dist} {orig}es = {conv} {end}es")
        elif "f" in end or "ft" in end or "feet" in end or "fet" in end or "foot" in end:
            conv = (round(dist / 12, 3))
            print(f"{dist} {orig}es = {conv} {end}")
        elif "y" in end or "yard" in end or "yd" in end:
            conv = (round(dist / 36, 3))
            print(f"{dist} {orig}es = {conv} {end}s")
        elif "me" in end or "meter" in end or "met" in end or "mete" in end:    
            conv = (round(dist / 39.37, 3))
            print(f"{dist} {orig}es = {conv} {end}s")
        elif "k" in end or "km" in end in "kilometer" in end or "kilo" in end or "kilom" in end:
            conv = (round(dist / 39370, 3))
            print(f"{dist} {orig}es = {conv} {end}")
        elif "mi" in end or "mile" in end or "mil" in end:
            conv = (round(dist / 63360, 3))
            print(f"{dist} {orig}es = {conv} {end}s")  
        else:
            print("error: program terminated")  
    elif "f" in orig or "ft" in orig or "feet" or "f" in orig or "foot" in orig:
        print(orig, "feet")
        if "in" in end or "inch" in end or "inches" in end:
            conv = (round(dist * 12, 3))
            print(f"{dist} {orig} = {conv} {end}es")
            print(orig)
        elif "f" in end or "ft" in end or "feet" in end or "fet" in end or "foot" in end:
            conv = (round(dist * 1, 3))
            print(f"{dist} {orig} = {conv} {end}")
        elif "y" in end or "yard" in end or "yd" in end:
            conv = (round(dist / 3, 3))
            print(f"{dist} {orig} = {conv} {end}s")    
        elif "me" in end or "meter" in end or "met" in end or "mete" in end:    
            conv = (round(dist / 3.281, 3))
            print(f"{dist} {orig} = {conv} {end}s")
        elif "k" in end or "km" in end in "kilometer" in end or "kilo" in end or "kilom" in end:
            conv = (round(dist / 3281, 3))
            print(f"{dist} {orig} = {conv} {end}")
        elif "mi" in end or "mile" in end or "mil" in end:
            conv = (round(dist / 5280, 3))
            print(f"{dist} {orig}es = {conv} {end}s")   
        else:
            print("error: program terminated")
    elif "y" in orig or "yard" in orig or "yd" in orig:
        print(orig, "yard")
        if "in" in end or "inch" in end or "inches" in end:
            conv = (round(dist * 36, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
            print(orig)
        elif "f" in end or "ft" in end or "feet" in end or "fet" in end or "foot" in end:
            conv = (round(dist * 3, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "y" in end or "yard" in end or "yd" in end:
            conv = (round(dist * 1, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif "me" in end or "meter" in end or "met" in end or "mete" in end:    
            conv = (round(dist / 1.094, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif "k" in end or "km" in end in "kilometer" in end or "kilo" in end or "kilom" in end:
            conv = (round(dist / 1094, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "mi" in end or "mile" in end or "mil" in end:
            conv = (round(dist / 1760, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        else:
            print("error: program terminated")
    elif "m" in orig or "me" in orig or "meter" in orig or "met" in orig or "mete" in orig:
        print(orig, "meter")
        if "in" in end or "inch" in end or "inches" in end:
            conv = (round(dist * 39.37, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
        elif "f" in end or "ft" in end or "feet" in end or "fet" in end or "foot" in end:
            conv = (round(dist * 3.281, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "y" in end or "yard" in end or "yd" in end:
            conv = (round(dist * 1.094, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif "me" in end or "meter" in end or "met" in end or "mete" in end:    
            conv = (round(dist / 1, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif "k" in end or "km" in end in "kilometer" in end or "kilo" in end or "kilom" in end:
            conv = (round(dist / 1000, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "mi" in end or "mile" in end or "mil" in end:
            conv = (round(dist / 1609, 2))
            print(f"{dist} {orig}s = {conv} {end}s") 
        else:
            print("error: program terminated")
    elif "k" in orig or "km" in orig in "kilometer" in orig or "kilo" in orig or "kilom" in orig:
        print(orig, "km")
        if "in" in end or "inch" in end or "inches" in end:
            conv = (round(dist * 39370, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
        elif "f" in end or "ft" in end or "feet" in end or "fet" in end or "foot" in end:
            conv = (round(dist * 3281, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "y" in end or "yard" in end or "yd" in end:
            conv = (round(dist * 1094, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif "me" in end or "meter" in end or "met" in end or "mete" in end:    
            conv = (round(dist / 1000, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif "k" in end or "km" in end in "kilometer" in end or "kilo" in end or "kilom" in end:
            conv = (round(dist / 1, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "mi" in end or "mile" in end or "mil" in end:
            conv = (round(dist / 1.609, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        else:
            print("error: program terminated")
    elif "mi" in orig or "mile" in orig or "mil" in orig:
        print(orig, "mile")
        if "in" in end or "inch" in end or "inches" in end:
            conv = (round(dist * 63360, 3))
            print(f"{dist} {orig}s = {conv} {end}es")
        elif "f" in end or "ft" in end or "feet" in end or "fet" in end or "foot" in end:
            conv = (round(dist * 5280, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "y" in end or "yard" in end or "yd" in end:
            conv = (round(dist * 1760, 3))
            print(f"{dist} {orig}es = {conv} {end}s")
        elif "me" in end or "meter" in end or "met" in end or "mete" in end:    
            conv = (round(dist / 1609, 3))
            print(f"{dist} {orig}s = {conv} {end}s")
        elif "k" in end or "km" in end in "kilometer" in end or "kilo" in end or "kilom" in end:
            conv = (round(dist / 1.609, 3))
            print(f"{dist} {orig}s = {conv} {end}")
        elif "mi" in end or "mile" in end or "mil" in end:
            conv = (round(dist / 1, 3))
            print(f"{dist} {orig}s = {conv} {end}s")  
        else:
            print("error: program terminated")


