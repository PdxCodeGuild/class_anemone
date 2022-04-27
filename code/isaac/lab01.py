'''Unit Converter'''

'''Each measurement will be based off of meters.  Example
1 foot == .3048 meters
'''

# VERSION 1

# Create measurement variables starting with 0
# Use feet(ft), miles(mi), kilometers(km), meters(m), yards(yd/s) and inches(inc).
# Set each variable to meter conversion for each measurement

ft = 0.3048 # feet
mi = 1609.34 # miles
km = 1000 # kilometers
m = 1 # meters
yd = 0.9144 # yards
inc = 0.0254 # inches

# Ask for user input and convert the selected UOM (Unit of Measurement)
ask_distance = input("What is the distance in feet? ") # use ft in conditional statements for conversion
meter_distance = int(ask_distance) * ft
print(f"{ask_distance} feet is {round(meter_distance, 5)} meters ")

# ---------------------------------------------------------------------- #

# VERSION 2

# Ask for the distance and the set the distance to the corresponding UOM.

user_distance = int(input("What is the distance? "))
distance_unit = input("What is the unit? ")

if distance_unit == 'feet':
    total_ft = user_distance * ft
    print(f"{user_distance} feet is {total_ft} meters")
elif distance_unit == 'miles':
    total_mi = user_distance * mi
    print(f"{user_distance} miles is {total_mi} meters")
elif distance_unit == 'kilometers':
    total_km = user_distance * km
    print(f"{user_distance} kilometers is {total_km} meters")
elif distance_unit == 'meters':
    total_m = user_distance * m
    print(f"{user_distance} meters is {total_m} meters")

# ------------------------------------------------------------------------- #

# VERSION 3

# Incorporate yards and inches

user_distance = int(input("What is the distance? "))
distance_unit = input("What is the unit? ")

if distance_unit == 'feet':
    total_ft = user_distance * ft
    print(f"{user_distance} foot/feet is {total_ft} meters")
elif distance_unit == 'miles':
    total_mi = user_distance * mi
    print(f"{user_distance} mile/s is {total_mi} meters")
elif distance_unit == 'kilometers':
    total_km = user_distance * km
    print(f"{user_distance} kilometer/s is {total_km} meters")
elif distance_unit == 'meters':
    total_m = user_distance * m
    print(f"{user_distance} meter/s is {total_m} meters")
elif distance_unit == 'yards':
    total_yd = user_distance * yd
    print(f"{user_distance} yard/s is {total_yd} meters")
elif distance_unit == 'inches':
    total_inc = user_distance * inc
    print(f"{user_distance} inches is {total_inc} meters")

# ------------------------------------------------------------------------------------ #

# VERSION 4

# Convert to UOM to meters 

user_distance = int(input("What is the distance? "))
first_unit = input("Enter first unit: ")
if first_unit == 'feet':
    outcome = user_distance * ft
elif first_unit == 'miles':
    outcome = user_distance * mi
elif first_unit == 'kilometers':
    outcome = user_distance * km
elif first_unit == 'meters':
    outcome = user_distance * m

# Convert to new UOM

second_unit = input("Enter second unit: ")
if second_unit == 'miles':
    new_unit_dis = outcome / mi
elif second_unit == 'kilometers':
    new_unit_dis = outcome / km
elif second_unit == 'meters':
    new_unit_dis = outcome / m
elif second_unit == 'feet':
    new_unit_dis = outcome / ft

print(round(new_unit_dis))