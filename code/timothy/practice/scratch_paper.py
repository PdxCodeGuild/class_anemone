# def double_digit(num):
#     tens = abs(num//10)
#     huns = abs(num//100)
#     print(tens)
#     print(huns)
#     if huns==0 and tens > 0 or tens < 0:
#         print(True)
#     else:
#         print(False)


# double_digit(-19)

# def double_digit_solution(num):
#     x = abs(num//10)
#     print(x)
#     if x >=1 and x <10:
#         print(True)
#     else:
#         print(False)

# double_digit_solution(6)
# double_digit_solution(67)
# double_digit_solution(678)
# double_digit_solution(-6)
# double_digit_solution(-67)
# double_digit_solution(-167)

def double_digit(num):
    tens = abs(num//10)
    if tens >= 1 and tens <10:
        print(True)
    else: print(False)

double_digit(6)
double_digit(67)
double_digit(678)
double_digit(-6)
double_digit(-67)
double_digit(-678)