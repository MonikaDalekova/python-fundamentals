sequence_of_numbers = list(map(int, input().split(", ")))
even_or_not = map(lambda num: num if sequence_of_numbers[num] % 2 == 0 else "no", range(len(sequence_of_numbers)))
even_indicates = list(filter(lambda a: a != "no", even_or_not))
print(even_indicates)
