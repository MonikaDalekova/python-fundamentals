number = int(input())
positive_numbers = []
negative_numbers = []
sum_negatives = 0
for _ in range(number):
    current_number = int(input())
    if current_number > 0:
        positive_numbers.append(current_number)
    else:
        sum_negatives += current_number
        negative_numbers.append(current_number)
print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum_negatives}")