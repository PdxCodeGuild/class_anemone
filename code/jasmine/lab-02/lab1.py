# user input feet
#distance = input("What is the distance in feet? ")
#convert feet to meters
#meters = int(distance) * 0.30408
#print statement showing conversion
#print(f'{distance} ft is {meters} m. ')


#distance_two = input("What is the distance? ")
#distance_two = int(distance_two)
#units = input("What are the units? ")

#if units == 'ft' or units == 'feet':
 #   print(f'{distance_two * 0.30408} m')

#elif units == 'mi' or units == 'miles':
 #   print(f'{distance_two * 1609.34} m')

#elif units == 'm' or units == 'meters':
 #   print(f'{distance_two * 1} m')

#elif units == 'km' or units =='kilometers':
 #   print(f'{distance_two * 1000} m')

#elif units == 'in' or units == 'inches':
 #   print(f'{distance_two * 0.0254} m')

#elif units =='yd' or units =='yards':
 #   print(f'{distance_two * 0.9144} m')


distance_three = input("What is the distance? ")
distance_three = float(distance_three)

input_unit = input("What are the input units? ")

output_unit = input("What are the output units? ")

meters_convert = distance_three * 0.30408
#print(miles_convert)

if input_unit == 'ft':
    new_input = 

if output_unit == 'ft':
    new_output = meters_convert/ 0.30408

elif output_unit == 'mi':
    new_output = meters_convert * 1609.34

elif output_unit == 'm':
    new_output = meters_convert / 1

elif output_unit == 'in':
    new_output = meters_convert / 0.0254

elif output_unit == 'yd':
    new_output = meters_convert / 0.9144

elif output_unit == 'km':
    new_output = meters_convert / 1000

print(f'{distance_three} {input_unit} is {new_output} {output_unit}')