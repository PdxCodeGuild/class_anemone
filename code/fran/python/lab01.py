# Lab01 - Unit Conversions
# Fran Kappes

# Programming Note: We've been asked to not use dictionaries for this lab.
# Define unit conversion variables:
feet_to_meters = 0.3048  # 1 ft is 0.3048 meters

# Collect info from user
user_distance = input("What is the distance in feet? ")

# Convert distance
distance_meters = round((feet_to_meters * int(user_distance)),4)

# Print results back to user
print(f"{user_distance} ft is {distance_meters} m")