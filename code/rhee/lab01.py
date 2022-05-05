
metrics = {
    'feet': 0.3048,
    'meter': 1,
    'miles': 1609.344,
    'kilometers': 1000,
}

distance = float(input("What is the distance? "))
c_in = input("Enter the unit to convert from: \nPlease select feet, meter, miles or kilometers: ").lower()
c_out = input("Enter the unit to convert to: \nPlease select feet, meter, miles or kilometers: ").lower()

if c_in == 'miles' and c_out == 'meter':
    answer = distance / 1609.344
if c_in == 'feet' and c_out == 'meter':
    answer = distance / 0.3048
elif c_in == 'meter' and c_out == 'meter':
    answer = distance / 1
elif c_in == 'kilometers' and c_out == 'meter':
    answer = distance / 1000

if c_in == 'meter' and c_out == 'miles':
    answer = distance * 0.0006213712
elif c_in == 'meter' and c_out == 'feet':
    answer = distance * 3.28084
elif c_in == 'meter' and c_out == 'meter':
    answer = distance * 1
elif c_in == 'meter' and c_out == 'kilometers':
    answer = distance * 1000

print(f"{distance} {c_in} is converted to {round(answer, 4)} {c_out}.")
