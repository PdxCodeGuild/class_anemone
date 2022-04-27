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
user_input_units = input("What are the input units? (ft/mi/m/km/yd/in) ")
user_output_units = input("What are the output units? (ft/mi/m/km/yd/in) ")

# Convert input distance to meters
if user_input_units == 'ft':
    distance_meters = round((feet_to_meters * user_distance),4)
elif user_input_units == 'mi':
    distance_meters = round((miles_to_meters * user_distance),4)
elif user_input_units == 'm':
    distance_meters = user_distance
elif user_input_units == 'km':
    distance_meters = round((kilometers_to_meters * user_distance),4)
elif user_input_units == 'yd':
    distance_meters = round((yards_to_meters * user_distance),4)
elif user_input_units == 'in':
    distance_meters = round((inches_to_meters * user_distance),4)

# Now convert meters to output units
if user_output_units == 'ft':
    output_distance = round((distance_meters/feet_to_meters),4)
elif user_output_units == 'mi':
    output_distance = round((distance_meters/miles_to_meters),4)
elif user_output_units == 'm':
    output_distance = distance_meters
elif user_output_units == 'km':
    output_distance = round((distance_meters/kilometers_to_meters),4)
elif user_output_units == 'yd':
    output_distance = round((distance_meters/yards_to_meters),4)
elif user_output_units == 'in':
    output_distance = round((distance_meters/inches_to_meters),4)

# Print results back to user
print(f"{user_distance} {user_input_units} is {output_distance} {user_output_units}")
