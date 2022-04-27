# Lab01 - Unit Conversions
# Fran Kappes

# Define unit conversion variables:
feet_to_meters = 0.3048  # 1 ft is 0.3048 m
miles_to_meters = 1609.34   # 1 mi is 1609.34 m
meters_to_meters = 1
kilometers_to_meters = 1000   # 1 km is 1000 m
yards_to_meters = 0.9144  # 1 yd is 0.9144 m
inches_to_meters = 0.0254  # 1 in is 0.0254 m

# Collect info from user
user_distance = int(input("What is the distance? "))
user_units = (input("What are the units? (ft/mi/m/km/yd/in) ")).lower()

# Convert distance
if user_units == 'ft':
    distance_meters = round((feet_to_meters * user_distance),4)
elif user_units == 'mi':
    distance_meters = round((miles_to_meters * user_distance),4)
elif user_units == 'm':
    distance_meters = round((meters_to_meters * user_distance),4)
elif user_units == 'km':
    distance_meters = round((kilometers_to_meters * user_distance),4)
elif user_units == 'yd':
    distance_meters = round((yards_to_meters * user_distance),4)
elif user_units == 'in':
    distance_meters = round((inches_to_meters * user_distance),4)

# Print results back to user
print(f"{user_distance} {user_units} is {distance_meters} m")
