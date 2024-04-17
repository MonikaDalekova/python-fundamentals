def factorial_division(a, b):
    factorial_one = 1
    for number in range(a, 0, -1):
        factorial_one *= number
    factorial_two = 1
    for number in range(b, 0, -1):
        factorial_two *= number
    division = factorial_one / factorial_two
    return division


integer_one = int(input())
integer_two = int(input())
print(f"{factorial_division(integer_one, integer_two):.2f}")

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# def factorial_division_function(num1, num2):
#     result1 = factorial(num1)
#     result2 = factorial(num2)
#     division_result = result1 / result2
#     return f'{division_result:.2f}'
#
#
# first_number = int(input())
# second_number = int(input())
# print(factorial_division_function(first_number, second_number))