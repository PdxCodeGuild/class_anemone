' Version 1 '

# value = int(input("What is the distance: "))
# meter_converison = value * 0.3048
# print(f"{value} ft is {meter_converison} m")

' Version 2 & 3'

# value = int(input("What is the distance: "))
# unit = input("What are the units (ft, m, mi, km, in, yd): ")
# if unit == 'ft':
#     print(f"{value} {unit} is {value * 0.3048} m")
# elif unit == 'm':
#     print(f"{value} {unit} is {value * 1} m")
# elif unit == 'mi':
#     print(f"{value} {unit} is {value * 1609.34} m")
# elif unit == 'km':
#     print(f"{value} {unit} is {value * 1000} m")
# elif unit == 'in':
#     print(f"{value} {unit} is {value * 0.0254} m")
# elif unit == 'yd':
#     print(f"{value} {unit} is {value * 0.9144} m")
# else:
#     print("This unit converter does not support that unit of measurement.")

' Version 4 '

value = int(input("What is the distance: "))
input_unit = input("What are the input units (ft, m, mi, km, in, yd): ")
output_unit = input("What are the ouput units: ")
if input_unit == 'ft':
    result = value * 0.3048
elif input_unit == 'm':
    result = value * 1
elif input_unit == 'mi':
    result = value * 1609.34
elif input_unit == 'km':
    result = value * 1000
elif input_unit == 'in':
    result = value * 0.0254
elif input_unit == 'yd':
    result = value * 0.9144
else:
    print("This unit converter does not support that unit of measurement.")

if output_unit == 'ft':
    print(f"{value} {input_unit} is {result / 0.3048} {output_unit}")
elif output_unit == 'm':
    print(f"{value} {input_unit} is {result / 1} {output_unit}")
elif output_unit == 'mi':
    print(f"{value} {input_unit} is {result / 1609.34} {output_unit}")
elif output_unit == 'km':
    print(f"{value} {input_unit} is {result / 1000} {output_unit}")
elif output_unit == 'in':
    print(f"{value} {input_unit} is {result / 0.0254} {output_unit}")
elif output_unit == 'yd':
    print(f"{value} {input_unit} is {result / 0.9144} {output_unit}")
else:
    print("This unit converter does not support that unit of measurement.")
