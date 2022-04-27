#Version 1
#Ask user for number of ft and print equivalent distance in meters
#Hint: 1 ft = 0.3048 m

num_of_feet = int(input("What is the distance in feet? "))
meter = 0.3048

print (num_of_feet, "ft is ", num_of_feet * meter, "m.")


#Version 2
#Allow the user to enter the units; convert the distance to meters (ft, miles, meters, km)

num_of_dist = int(input("What is the distance? "))
units = input("What are the units? ")

feet = .3048
miles = 1609.34
meters = 1
kilometers = 1000
yards = .9144                   #Version 3: Add yards and inches
inches = .0254

if units == "feet" or units == "ft":
    print (num_of_dist, units, "is", num_of_dist * feet, "m.")

elif units == "miles" or units == "mi":
    print (num_of_dist, units, "is", num_of_dist * miles, "m.")

elif units == "meters" or units == "m":
    print (num_of_dist, units, "is", num_of_dist * meters, "m.")

elif units == "kilometers" or units == "km":
    print (num_of_dist, units, "is", num_of_dist * kilometers, "m.")

elif units == "yards" or units == "yd":
    print (num_of_dist, units, "is", num_of_dist * yards, "m.")

elif units == "inches" or units =="in":
    print (num_of_dist, units, "is", num_of_dist * inches, "m.")

else:
    print ("Invalid unit entered.")

#Version 4
#Ask user for distance, starting units, and units to convert to

distance = int(input("What is the distance? "))
input_units = input("What are the input units? ")
output_units = input ("What are the output units? ")

feet = .3048
miles = 1609.34
meters = 1
kilometers = 1000
yards = .9144
inches = .0254

if input_units == "feet" or input_units == "ft":
    ft_meters = distance * feet
    if output_units == "feet" or output_units == "ft":
        dist_in_feet = ft_meters / feet
        print (distance, input_units, "is", dist_in_feet, output_units)
    elif output_units == "miles" or output_units == "mi":
        dist_in_miles = ft_meters / miles
        print (distance, input_units, "is", dist_in_miles, output_units)
    elif output_units == "meters" or output_units == "m":
        dist_in_meters = ft_meters / meters
        print (distance, input_units, "is", dist_in_meters, output_units)
    elif output_units == "kilometers" or output_units == "km":
        dist_in_kilometers = ft_meters / kilometers
        print (distance, input_units, "is", dist_in_kilometers, output_units)
    elif output_units == "yards" or output_units == "yds":
        dist_in_yards = ft_meters / yards
        print (distance, input_units, "is", dist_in_yards, output_units)
    elif output_units == "inches" or output_units == "in":
        dist_in_inches = ft_meters / inches
        print (distance, input_units, "is", dist_in_inches, output_units)
    else:
        print ("Invalid units entered.")

if input_units == "miles" or input_units == "mi":
    mi_meters = distance * miles
    if output_units == "feet" or output_units == "ft":
        dist_in_feet = mi_meters / feet
        print (distance, input_units, "is", dist_in_feet, output_units)
    elif output_units == "miles" or output_units == "mi":
        dist_in_miles = mi_meters / miles
        print (distance, input_units, "is", dist_in_miles, output_units)
    elif output_units == "meters" or output_units == "m":
        dist_in_meters = mi_meters / meters
        print (distance, input_units, "is", dist_in_meters, output_units)
    elif output_units == "kilometers" or output_units == "km":
        dist_in_kilometers = mi_meters / kilometers
        print (distance, input_units, "is", dist_in_kilometers, output_units)
    elif output_units == "yards" or output_units == "yds":
        dist_in_yards = mi_meters / yards
        print (distance, input_units, "is", dist_in_yards, output_units)
    elif output_units == "inches" or output_units == "in":
        dist_in_inches = mi_meters / inches
        print (distance, input_units, "is", dist_in_inches, output_units)
    else:
        print ("Invalid units entered.")

if input_units == "meters" or input_units == "m":
    m_meters = distance * meters
    if output_units == "feet" or output_units == "ft":
        dist_in_feet = m_meters / feet
        print (distance, input_units, "is", dist_in_feet, output_units)
    elif output_units == "miles" or output_units == "mi":
        dist_in_miles = m_meters / miles
        print (distance, input_units, "is", dist_in_miles, output_units)
    elif output_units == "meters" or output_units == "m":
        dist_in_meters = m_meters / meters
        print (distance, input_units, "is", dist_in_meters, output_units)
    elif output_units == "kilometers" or output_units == "km":
        dist_in_kilometers = m_meters / kilometers
        print (distance, input_units, "is", dist_in_kilometers, output_units)
    elif output_units == "yards" or output_units == "yds":
        dist_in_yards = m_meters / yards
        print (distance, input_units, "is", dist_in_yards, output_units)
    elif output_units == "inches" or output_units == "in":
        dist_in_inches = m_meters / inches
        print (distance, input_units, "is", dist_in_inches, output_units)
    else:
        print ("Invalid units entered.")

if input_units == "kilometers" or input_units == "km":
    km_meters = distance * kilometers
    if output_units == "feet" or output_units == "ft":
        dist_in_feet = km_meters / feet
        print (distance, input_units, "is", dist_in_feet, output_units)
    elif output_units == "miles" or output_units == "mi":
        dist_in_miles = km_meters / miles
        print (distance, input_units, "is", dist_in_miles, output_units)
    elif output_units == "meters" or output_units == "m":
        dist_in_meters = km_meters / meters
        print (distance, input_units, "is", dist_in_meters, output_units)
    elif output_units == "kilometers" or output_units == "km":
        dist_in_kilometers = km_meters / kilometers
        print (distance, input_units, "is", dist_in_kilometers, output_units)
    elif output_units == "yards" or output_units == "yds":
        dist_in_yards = km_meters / yards
        print (distance, input_units, "is", dist_in_yards, output_units)
    elif output_units == "inches" or output_units == "in":
        dist_in_inches = km_meters / inches
        print (distance, input_units, "is", dist_in_inches, output_units)
    else:
        print ("Invalid units entered.")

if input_units == "yards" or input_units == "yds":
    yd_meters = distance * yards
    if output_units == "feet" or output_units == "ft":
        dist_in_feet = yd_meters / feet
        print (distance, input_units, "is", dist_in_feet, output_units)
    elif output_units == "miles" or output_units == "mi":
        dist_in_miles = yd_meters / miles
        print (distance, input_units, "is", dist_in_miles, output_units)
    elif output_units == "meters" or output_units == "m":
        dist_in_meters = yd_meters / meters
        print (distance, input_units, "is", dist_in_meters, output_units)
    elif output_units == "kilometers" or output_units == "km":
        dist_in_kilometers = yd_meters / kilometers
        print (distance, input_units, "is", dist_in_kilometers, output_units)
    elif output_units == "yards" or output_units == "yds":
        dist_in_yards = yd_meters / yards
        print (distance, input_units, "is", dist_in_yards, output_units)
    elif output_units == "inches" or output_units == "in":
        dist_in_inches = yd_meters / inches
        print (distance, input_units, "is", dist_in_inches, output_units)
    else:
        print ("Invalid units entered.")

if input_units == "inches" or input_units == "in":
    in_meters = distance * inches
    if output_units == "feet" or output_units == "ft":
        dist_in_feet = in_meters / feet
        print (distance, input_units, "is", dist_in_feet, output_units)
    elif output_units == "miles" or output_units == "mi":
        dist_in_miles = in_meters / miles
        print (distance, input_units, "is", dist_in_miles, output_units)
    elif output_units == "meters" or output_units == "m":
        dist_in_meters = in_meters / meters
        print (distance, input_units, "is", dist_in_meters, output_units)
    elif output_units == "kilometers" or output_units == "km":
        dist_in_kilometers = in_meters / kilometers
        print (distance, input_units, "is", dist_in_kilometers, output_units)
    elif output_units == "yards" or output_units == "yds":
        dist_in_yards = in_meters / yards
        print (distance, input_units, "is", dist_in_yards, output_units)
    elif output_units == "inches" or output_units == "in":
        dist_in_inches = in_meters / inches
        print (distance, input_units, "is", dist_in_inches, output_units)
    else:
        print ("Invalid units entered.")