data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    max_num = 0
    peaks = []
    for num in range(1, len(data)-1):
        max_num = (data[num] if data[num] > max_num else max_num)
        if data[num] > data[num+1] and data[num] > data[num-1]:
            peaks.append(num)
    return peaks, max_num


def valleys(data_list):
    valleys = []
    for num in range(1, len(data)-1):
        if data[num] < data[num+1] and data[num] < data[num-1]:
            valleys.append(num)
    return valleys


def peaks_and_valleys(data):

    peak_vals, max_int = peaks(data)
    valley_vals = valleys(data)
    poi = peak_vals + valley_vals
    poi.sort()

    return poi



print('peaks: ', peaks(data)[0])
print('valleys: ', valleys(data))
print('peaks & valleys', peaks_and_valleys(data))