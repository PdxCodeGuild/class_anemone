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

orig = "blank"
end = "blank"

x = 0
y = 0
while orig == "blank":
    orig = input("original unit to convert from: ")

    dist = (float(input("distance to convert: ")))
    if orig in valid_in:
        conv = dist / 39.37
    elif orig in valid_ft:
        conv = dist / 3.281
    elif orig in valid_yd:
        conv = dist / 1.094
    elif orig in valid_m or orig == 'm':

        conv = dist / 1
    elif orig in valid_km:
        conv = dist / (1/1000)
    elif orig in valid_mi:
        conv = dist / (1/1609.334)
    while orig == "blank" or end == "blank":
        end = input("unit to convert distance to: ")
        if end in valid_in:
            conv *= 39.37
            conv = round(conv,1)
        elif end in valid_ft:
            conv *= 3.281
            conv = round(conv)
        elif end in valid_yd:
            conv *= 1.09361
            conv = round(conv)
        elif end in valid_m or orig == 'm':
            conv *= 1
        elif end in valid_km:
            conv *= 1/1000
        elif end in valid_mi:
            conv *= 1/1609

print(f"\n{dist} {orig} = ~{round(conv, 4)} {end} ")                 
