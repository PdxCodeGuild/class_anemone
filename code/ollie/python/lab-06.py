' Lab 6 - Ollie Callanan '

card_num = input("Enter credit card number: ")
# nums = [int(num) for num in str(card_num)]
# check_num = nums.pop()

def validate(number):
    nums = [int(num) for num in str(number)]
    check_num = nums.pop()
    nums = nums.reverse()
    nums = [2 * num for num in nums[::2]]
    for num in nums:
        if num > 9:
            num = num - 9
        else:
            return num
    ones_digit = sum(nums) % 10
    if check_num == ones_digit:
        print("Valid")
    else:
        print("Invalid")

validate(card_num)