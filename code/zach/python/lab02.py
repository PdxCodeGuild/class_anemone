# function will find the average of the provided number list.
def average(numeric_sum, numeric_list):
    avg = numeric_sum / len(numeric_list)

    return avg

# Function will take a list of numbers and return their sum


def sum(numbers):
    total = 0
    for number in numbers:
        total += int(number)
    return total

# Function will take in a list and a digit to filter. Will return a filtered list with digit removed.


def remove_all(numbers, num_to_delete):
    print(f'Numbers: { numbers } \nRemove: { num_to_delete }')
    results = list(filter(lambda x: x != num_to_delete, numbers))
    print(f'Numbers: { results }')
    input_msg = '0'
    return results


def main():
    numbers = []
    # User input / interactive prompt allowing user access to application's functionality
    input_msg = input(
        "'  #  ' - adds numeric to list \n'  del  ' - remove entry from list \n'  done  ' - print sum and exit \n\nEnter: ' # ',' del ',' done ' \n=> ")

    while input_msg != 'done':
        if input_msg.isnumeric():
            numbers.append(input_msg)
            input_msg = input("Enter: ' # ',' del ',' done ' \n=> ")
        elif input_msg == 'del':
            num_to_delete = input('Input number to be removed: ')
            numbers = remove_all(numbers, num_to_delete)
            input_msg = input("' # ',' del ',' done ' \n=> ")
        else:
            input_msg = input(
                "Incorrect entry!!!\n\nEnter a whole number,'done', or 'del'")
    print(f'User Average: { average(sum(numbers),numbers) }')


main()
