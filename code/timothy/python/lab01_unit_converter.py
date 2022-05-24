# ....Lab01 Version 1

# m = 0.3048
# ft = int(input("What is the distance in feet? "))
# result = m * ft
# print(f"{ft} ft is {result} m.")

# ....Lab01 Version 2

# distance = int(input("What is the distance? "))
# units = input("What are the units? (ft, mi, m, km) ")
# if units == "ft":
#     m = 0.3048
# elif units == "mi":
#     m = 1609.34
# elif units == "m":
#     m = 1
# elif units == "km":
#     m = 1000

# result = distance * m

# print(f"{distance} {units} is {result} m")

# ....Lab01 Version 3

# distance = int(input("What is the distance? "))
# units = input("What are the units? (in, yd, ft, mi, m, km,) ")
# if units == "ft":
#     m = 0.3048
# elif units == "mi":
#     m = 1609.34
# elif units == "m":
#     m = 1
# elif units == "km":
#     m = 1000
# elif units == "in":
#     m = 0.0254
# elif units == "yd":
#     m = 0.9144

# result = distance * m

# print(f"{distance} {units} is {result} m")

# ....Lab01 Version 4

distance = int(input("What is the distance? "))
input_units = input("What are the input units? (in, yd, ft, mi, m, km,) ")
if input_units == "ft":
    m_input = 0.3048
elif input_units == "mi":
    m_input = 1609.34
elif input_units == "m":
    m_input = 1
elif input_units == "km":
    m_input = 1000
elif input_units == "in":
    m_input = 0.0254
elif input_units == "yd":
    m_input = 0.9144

input_result = distance * m_input

output_units = input("What are the output units? (in, yd, ft, mi, m, km,) ")
if output_units == "ft":
    m_output = 0.3048
elif output_units == "mi":
    m_output = 1609.34
elif output_units == "m":
    m_output = 1
elif output_units == "km":
    m_output = 1000
elif output_units == "in":
    m_output = 0.0254
elif output_units == "yd":
    m_output = 0.9144

result = input_result / m_output

print(f"{distance} {input_units} is {result} {output_units}")