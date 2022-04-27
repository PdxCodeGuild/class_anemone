def distance_converter(distance, original_unit, conversion_unit):
    print(
        f'...Converting { distance } { original_unit } to { conversion_unit }')
    # switch dictionary that contains all supported units in meters for conversion calculations
    switch = {
        'in': 0.0254,   # 1 inch is 0.0254 m
        'ft': 0.3048,   # 1 ft is 0.3048 m
        'yd': 0.9144,   # 1 yard is 0.9144 m
        'mi': 1609.34,  # 1 mi is 1609.34 m
        'm': 1,         # 1 m is 1 m
        'km': 1000      # 1 km is 1000 m
    }

    float_distance = float(distance)

    # conversion_value = (original_distance*original_unit_meters)/ conversion_unit_meters
    conversion = float_distance * \
        switch.get(original_unit, "Invalid input") / \
        switch.get(conversion_unit, "Invalid input")
    print(
        f'\n    => { distance } { original_unit } is { conversion } { conversion_unit }')


def main():
    supported_units = ['in', 'ft', 'yd', 'mi', 'm', 'km']

    # user-inputs
    print('...initializing...')
    run = input(
        f'Would you like to convert a distance?\nSupported Conversions: { supported_units }?\n    y/n: ').lower()
    while run == 'y':
        distance = input('What is the distance? \n    => ')
        if not distance.isnumeric():
            while not distance.isnumeric():
                print('...error distance must be numeric')
                distance = input('What is the distance? \n    => ')

        original_unit = input('What is the input units? \n    => ').lower()
        if original_unit not in supported_units:
            while original_unit not in supported_units:
                original_unit = input(
                    "...error enter supported units\nImperial: 'in','ft','yd' and 'mi'\nMetric: 'm' and 'km'\n    => ").lower()

        conversion_unit = input('What are the output units? \n    => ').lower()
        if conversion_unit not in supported_units:
            while conversion_unit not in supported_units:
                conversion_unit = input(
                    "...error enter supported units\nImperial: 'in','ft','yd' and 'mi'\nMetric: 'm' and 'km'\n    => ").lower()

        distance_converter(distance, original_unit, conversion_unit)
        run = input(
            "-----------------------------------------------\nTo convert to another value enter 'y', exit program with anyother key:\n    => ")
    print('\n\nThanks for converting with me!!!')


main()