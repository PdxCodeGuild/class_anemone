import math
import string  
# created a def to multiply the ref and dist together
def dist(a, b):
    return (a * b)

ref = ['meters', 'feet', 'kilos', 'miles', 'yards', 'inchs']
units = input(f'\nWhat Measurement do you want to convert:\n{ref}: ').lower()
units_dist = float(input(f'\nWhat is distance of {units}: \n'))
unit_con = input(f'\nWhat do you want to convert {units} to?:\n{ref}: \n').lower()
#using Ref[] to get the point chosen by input and then converting that to its meters form
inchs = ref[5]
inchs = 0.0254
feet = ref[1]
feet = 0.3048 
miles = ref[3]
miles = 1609.34
meters = ref[0]
meters = 1
kilos = ref[2]
kilos = 1000
yards = ref[4]
yards = 0.9144
#len_feet = a / feet
#take output a and divide by whats needed to convert ( ex take unit_dist * ref then take
# ex. a and divide it by ref)
if ref[5] in units:
    a = dist(units_dist, inchs)
    if ref[1] in unit_con:
        len_feet = a / feet
        print(f'\n{units_dist} {units} is {len_feet} feet\n')
    elif ref[2] in unit_con:
        len_kilos = a / kilos
        print(f'\n{units_dist} {units} is {len_kilos} kilos\n')
    elif ref[3] in unit_con:
        len_miles = a / miles
        print(f'\n{units_dist} {units} is {len_miles} miles\n')
    elif ref[4] in unit_con:
        len_yards = a / yards
        print(f'\n{units_dist} {units} is {len_feet} yards\n')
    elif ref[0] in unit_con:
        len_meters = a / meters
        print(f'\n{units_dist} {units} is {len_feet} meters\n')
if ref[4] in units:
    a = dist(units_dist, yards)
    if ref[1] in unit_con:
        len_feet = a / feet
        print(f'\n{units_dist} {units} is {len_feet} feet\n')
    elif ref[2] in unit_con:
        len_kilos = a / kilos
        print(f'\n{units_dist} {units} is {len_kilos} kilos\n')
    elif ref[3] in unit_con:
        len_miles = a / miles
        print(f'\n{units_dist} {units} is {len_miles} miles\n')
    elif ref[5] in unit_con:
        len_inchs = a / inchs
        print(f'\n{units_dist} {units} is {len_inchs} inchs\n')
    elif ref[0] in unit_con:
        len_meters = a / meters
        print(f'\n{units_dist} {units} is {len_feet} meters\n')
if ref[3] in units:
    a = dist(units_dist, miles)
    if ref[1] in unit_con:
        len_feet = a / feet
        print(f'\n{units_dist} {units} is {len_feet} feet\n')
    elif ref[2] in unit_con:
        len_kilos = a / kilos
        print(f'\n{units_dist} {units} is {len_kilos} kilos\n')
    elif ref[4] in unit_con:
        len_yards = a / yards
        print(f'\n{units_dist} {units} is {len_yards} yards\n')
    elif ref[5] in unit_con:
        len_inchs = a / inchs
        print(f'\n{units_dist} {units} is {len_inchs} inchs\n')
    elif ref[0] in unit_con:
        len_meters = a / meters
        print(f'\n{units_dist} {units} is {len_feet} meters\n')
if ref[2] in units:
    a = dist(units_dist, kilos)
    if ref[1] in unit_con:
        len_feet = a / feet
        print(f'\n{units_dist} {units} is {len_feet} feet\n')
    elif ref[4] in unit_con:
        len_yards = a / yards
        print(f'\n{units_dist} {units} is {len_yards} yards\n')
    elif ref[3] in unit_con:
        len_miles = a / miles
        print(f'\n{units_dist} {units} is {len_miles} miles\n')
    elif ref[5] in unit_con:
        len_inchs = a / inchs
        print(f'\n{units_dist} {units} is {len_inchs} inchs\n')
    elif ref[0] in unit_con:
        len_meters = a / meters
        print(f'\n{units_dist} {units} is {len_feet} meters\n')        
if ref[1] in units:
    a = dist(units_dist, feet)
    if ref[2] in unit_con:
        len_kilos = a / kilos
        print(f'\n{units_dist} {units} is {len_kilos} kilos\n')
    elif ref[4] in unit_con:
        len_yards = a / yards
        print(f'\n{units_dist} {units} is {len_yards} yards\n')
    elif ref[3] in unit_con:
        len_miles = a / miles
        print(f'\n{units_dist} {units} is {len_miles} miles\n')
    elif ref[5] in unit_con:
        len_inchs = a / inchs
        print(f'\n{units_dist} {units} is {len_inchs} inchs\n')
    elif ref[0] in unit_con:
        len_meters = a / meters
        print(f'\n{units_dist} {units} is {len_feet} meters\n')
if ref[0] in units:
    a = dist(units_dist, meters)
    if ref[2] in unit_con:
        len_kilos = a / kilos
        print(f'\n{units_dist} {units} is {len_kilos} kilos\n')
    elif ref[4] in unit_con:
        len_yards = a / yards
        print(f'\n{units_dist} {units} is {len_yards} yards\n')
    elif ref[3] in unit_con:
        len_miles = a / miles
        print(f'\n{units_dist} {units} is {len_miles} miles\n')
    elif ref[5] in unit_con:
        len_inchs = a / inchs
        print(f'\n{units_dist} {units} is {len_inchs} inchs\n')
    elif ref[1] in unit_con:
        len_feet = a / feet
        print(f'\n{units_dist} {units} is {len_feet} feet\n')       

    



    

