current_string = input().split()
total_sum = 0

for string in current_string:
    first_letter = string[0]
    last_letter = string[-1]
    first_place = ord(first_letter)
    last_place = ord(last_letter)
    number = int(string[1:-1])
    if first_letter.isupper():
        total_sum += number / (first_place - 64)
    else:
        total_sum += number * (first_place - 96)
    if last_letter.isupper():
        total_sum -= (last_place - 64)
    else:
        total_sum += (last_place - 96)
print(f"{total_sum:.2f}")