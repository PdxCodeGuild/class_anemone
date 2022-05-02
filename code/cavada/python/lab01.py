"""lab01"""

"""convert original unit to meter"""
valid_ft = ['foot', 'feet', 'ft', 'f']
valid_yd = ['yard', 'yd', 'y', 'yards']
valid_in = ['inches', 'inch', 'in']
valid_m = ['meters', 'meter']
valid_km = ['kilometer', 'km', 'k']
valid_mi = ['miles', 'mile', 'mi']
units = ['in', 'ft', 'yd', 'm', 'km', 'mi']
valid_master = []
valid_master.extend(valid_ft)
valid_master.extend(valid_yd)
valid_master.extend(valid_in)
valid_master.extend(valid_m)
valid_master.extend(valid_km)
valid_master.extend(valid_mi)

x = 0
y = 0
# import random
# orig = random.choice(units)


# dist = random.randint(1,99)

while x != 1:
    z = 0
    orig = input("original unit to convert from: ")
    # end = random.choice(units)
    end = input("unit to convert distance to: ")
    dist = (float(input("distance to convert: ")))
    # print(f"\nYou chose to convert {dist} {orig} into {end}")
    y = 0
    if orig in valid_in:
        conv = dist / 39.37
    elif orig in valid_ft:
        conv = dist / 3.281
    elif orig in valid_yd:
        conv = dist / 1.094
    elif orig in valid_m:
        conv = dist / 1
    elif orig in valid_km:
        conv = dist / (1/1000)
    elif orig in valid_mi:
        conv = dist / (1/1609.334)
        # print(conv)
    else:
        conv = "error1"
        z-=1

        # print(conv)
        # y -= 1
        break
    while y != 1:
            # conv = round(conv, 4)
            if end in valid_in:
                conv *= 39.37
                conv = round(conv,1)
            elif end in valid_ft:
                conv *= 3.281
                conv = round(conv)
            elif end in valid_yd:
                conv *= 1.09361
                conv = round(conv)
            elif end in valid_m:
                conv *= 1
            elif end in valid_km:
                conv *= 1/1000
            elif end in valid_mi:
                conv *= 1/1609
            # conv += .005        
            else: 
                conv = "error2"
                z-=1
                # y -= 1
                # print(conv)
                break
            y += 1
            z += 1
            # print("hello")
    # print(conv)  
    #    
    #     
    x += 1       
    # print(dist)
# conv = round(conv, 1)
    # print(conv)
    print(f"\nYou chose to convert {dist} {orig} into {end}")

    if z == 0:
        print(f"\n{dist} {orig} = ~{conv} {end}??? ")                 
    else:
        print(f"\n{dist} {orig} = ~{round(conv, 4)} {end} ")                 
