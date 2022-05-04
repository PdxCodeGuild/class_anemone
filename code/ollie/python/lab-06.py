' Lab 6 - Ollie Callanan '

def validate():
    card_num = input("Enter credit card number: ")
    nums = [int(num) for num in str(card_num)]
    check_num = nums.pop()
    nums == nums.reverse()
    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = nums[i] * 2
    nums = [i - 9 if i > 9 else i for i in nums]
    ones_digit = sum(nums) % 10
    if check_num == ones_digit:
        print("Valid")
    else:
        print("Invalid")
    # return card_num, nums, sum(nums), ones_digit, check_num

validate()