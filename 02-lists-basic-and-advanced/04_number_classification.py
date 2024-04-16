def positive(a):
    return ", ".join([number for number in a if int(number) >= 0])


def negative(a):
    return ", ".join([number for number in a if int(number) < 0])


def even(a):
    return ", ".join([number for number in a if int(number) % 2 == 0])


def odd(a):
    return ", ".join([number for number in a if 0 != int(number) % 2])


sequence_of_numbers = input().split(", ")
print(f"Positive: {positive(sequence_of_numbers)}")
print(f"Negative: {negative(sequence_of_numbers)}")
print(f"Even: {even(sequence_of_numbers)}")
print(f"Odd: {odd(sequence_of_numbers)}")