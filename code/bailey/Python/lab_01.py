'''
class_anemone
Lab 1
Baiely Baker
'''
# Setup units for conversion
ft = 0.3048
mi = 1609.34
m = 1
km = 1000,
yd = 0.9144,
inch = 0.0254

# Get inputs from user
distance = int(input("What is the distance? "))
input_unit = input("What are the input units? ").lower()
output_unit= input("what are the output units? ").lower()

# Convert to input distance to meters
if input_unit == 'ft' or input_unit == 'feet':
    output = distance * ft
elif input_unit == 'mi' or input_unit == 'miles':
    output = distance * mi
elif input_unit == 'km' or input_unit == 'kilometers':
    output = distance * km
elif input_unit == 'm' or input_unit == 'meter':
    output = distance * m
elif input_unit == 'yd' or input_unit == 'yard':
    output = distance * yd
elif input_unit == 'in' or input_unit == 'inch':
    output = distance * inch

# Convert from meters to output unit

if input_unit == output_unit:
    output = distance
elif output_unit == 'ft' or output_unit == 'feet':
    output = distance * 3.28084
elif output_unit == 'mi' or output_unit == 'miles':
    output = distance / mi
elif output_unit == 'km' or output_unit == 'kilometers':
    output = distance / km
elif output_unit == 'yd' or output_unit == 'yard':
    output = distance * 1.094
elif output_unit == 'in' or output_unit == 'inch':
    output = distance * 39.37


# print the conversion
print(f"{distance} {input_unit} is {round(output, 5)} {output_unit}")  
