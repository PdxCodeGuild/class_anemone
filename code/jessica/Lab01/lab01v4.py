"""
## Version 4

Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).



|  | ft  | mi  | m  | km  |
|---|----|----|----|---|
|ft|1||0.3048||
|mi||1|1609.34||
|m|1/0.3048|1/1609.34|1|1/1000|
|km|||1000|1|

But instead of filling out that matrix, and checking for each pair of units (`if from_units == 'mi' and to_units == 'km'`), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units **_to_** meters, then convert **_from_** meters to the output units.



Below is some sample input/output:

```
> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
```
"""

user_input_distance = int(input("What is the distance? "))
user_input_units = input("What are the input units? ")
user_output_units = input("What are the output units? ")

print(f"What is the distance? {user_input_distance}")
print(f"What is the input units? {user_input_units}")

# converting from ft to m
"""1 foot = 0.3048 meter"""
# converting from m to m
"""1 meter = 1 meter"""
# converting from mi to m
"""1 mile = 1609.34 meters"""
# converting from km to m
"""1 km = 1000 meters"""

## convert input to meters

if user_input_units == "ft":
    total_meters = user_input_distance * 0.3048
elif user_input_units == "m":
    total_meters = user_input_distance * 1
elif user_input_units == "mi":
    total_meters = user_input_distance * 1609.34
elif user_input_units == "km":
    total_meters = user_input_distance * 1000

## convert meters to output
if user_output_units == "ft":
    total_output = total_meters / 0.3048
elif user_output_units == "mi":
    total_output = total_meters / 1609.34
elif user_output_units == "km":
    total_output = total_meters / 1000
elif user_output_units == "m":
    total_output = total_meters
    



print(f"{user_input_distance} {user_input_units} is {total_output} {user_output_units}")