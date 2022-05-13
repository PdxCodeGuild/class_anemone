
metrics = {
    'feet': 0.3048,
    'meter': 1,
    'miles': 1609.344,
    'kilometers': 1000,
}

distance = float(input("What is the distance? "))
c_in = input("Enter the unit to convert from: \nPlease select feet, meter, miles or kilometers: ").lower()
c_out = input("Enter the unit to convert to: \nPlease select feet, meter, miles or kilometers: ").lower()

if c_in == 'feet':
    answer = distance * 0.3048
elif c_in == 'meter':
    answer = distance * 1
elif c_in == 'miles':
    answer = distance * 1609.344
elif c_in == 'kilometers':
    answer = distance * 1000

if c_out == 'feet':
    convert = answer / 0.3048
elif c_out == 'meter':
    convert = answer / 1
elif c_out == 'miles':
    convert = answer / 1609.344
elif c_out == 'kilometers':
    convert = answer / 1000

print(f"{distance} {c_in} is converted to {round(convert, 4)} {c_out}.")
