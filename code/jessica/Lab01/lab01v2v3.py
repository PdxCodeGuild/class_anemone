 #---Version 2/3---#
#user input
user_input_distance = int(input("What is the distance? "))

user_input_units = input("What are the units? ")

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m

# 1 yard is 0.9144 m
# 1 inch is 0.0254 m

#conversion table
total_feet = user_input_distance * 0.3048
total_mile = user_input_distance * 1609.34
total_meter = user_input_distance * 1
total_kilometer = user_input_distance * 1000

#version 3 
total_yard = user_input_distance * 0.9144
total_inch = user_input_distance * 0.0254


#output statements

if user_input_units == "ft":
   print(f"{user_input_distance} ft is {total_feet} m") 
elif user_input_units == "mi":
    print(f"{user_input_distance} miles is {total_mile} m")
elif user_input_units == "m":
    print(f"{user_input_distance} meters is {total_meter} m")
elif user_input_units == "km":
    print(f"{user_input_distance} kilometers is {total_kilometer} m")
elif user_input_units == "yd":
    print(f"{user_input_distance} yards is {total_yard} m")
elif user_input_units == "in":
    print(f"{user_input_distance} inches is {total_inch} m") 
    
