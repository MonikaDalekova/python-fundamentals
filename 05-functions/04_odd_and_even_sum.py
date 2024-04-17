def even_or_odd(a):
    sum_even = 0
    sum_odd = 0
    for digit in str(a):
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = int(input())
print(even_or_odd(number))

