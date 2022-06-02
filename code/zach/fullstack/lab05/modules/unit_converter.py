def unit_converter(distance, original_unit, conversion_unit):
    to_meters = {
        'in': 0.0254,   # 1 inch is 0.0254 m
        'ft': 0.3048,   # 1 ft is 0.3048 m
        'yd': 0.9144,   # 1 yard is 0.9144 m
        'mi': 1609.34,  # 1 mi is 1609.34 m
        'm': 1,         # 1 m is 1 m
        'km': 1000      # 1 km is 1000 m
    }
    float_distance = float(distance)
    conversion = float_distance * \
        to_meters.get(original_unit, "Invalid input") / \
        to_meters.get(conversion_unit, "Invalid input")

    print(
        f'\n    => { distance } { original_unit } is { conversion } { conversion_unit }')
    return conversion
