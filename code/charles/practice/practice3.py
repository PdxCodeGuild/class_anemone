# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def double_numbers(nums):
    i = 0
    x2 = []
    while i <= len(nums) -1:
        x2.append(nums[i] * 2)
        i +=1
    return x2

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]

print(test_double_numbers())
# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):
    i= 0
    x = ''
    while i <= n - 1:
        x += '*'
        i += 1
    return x

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'

print(test_stars)
# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    i = 0
    x = []
    while i <= len(nums) -1:
        if nums[i] < 10:
            i += 1
            x.append(nums[i])
        else:
            i += 1
            pass
    return x

def test_extract_less_than_ten():
    extract_less_than_ten([2, 8, 12, 18]) == [2, 8]

print(test_extract_less_than_ten)