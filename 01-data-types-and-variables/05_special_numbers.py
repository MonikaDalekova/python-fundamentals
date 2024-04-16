n = int(input())

for current_number in range(1, n+1):
    current_number_as_str = str(current_number)
    digit_sum = 0
    is_special = False
    for digit in current_number_as_str:
        digit_sum += int(digit)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True
    print(f"{current_number} -> {is_special}")