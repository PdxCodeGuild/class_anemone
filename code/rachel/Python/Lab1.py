#Version 1
#Ask user for number of ft and print equivalent distance in meters
#Hint: 1 ft = 0.3048 m

##num_of_feet = int(input("What is the distance in feet? "))
##meter = 0.3048

##print (num_of_feet, "ft is ", num_of_feet * meter, "m.")


#Version 2
#Allow the user to enter the units; convert the distance to meters (ft, miles, meters, km)

num_of_dist = int(input("What is the distance? "))
units = input("What are the units? ")

feet = .3048
miles = 1609.34
meters = 1
kilometers = 1000

print (num_of_dist)
print (units)

if units == "feet" or units == "ft":
    print (num_of_dist, units, "is", num_of_dist * feet, "m.")

elif units == "miles" or units == "mi":
    print (num_of_dist, units, "is", num_of_dist * miles, "m.")

elif units == "meters" or units == "m":
    print (num_of_dist, units, "is", num_of_dist * meters, "m.")

elif units == "kilometers" or units == "km":
    print (num_of_dist, units, "is", num_of_dist * kilometers, "m.")

else:
    print ("Invalid unit entered.")