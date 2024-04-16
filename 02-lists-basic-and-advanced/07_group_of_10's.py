def group_of_tens(numbers_in_current_group):
    sequence_as_int = [int(x) for x in sequence_of_number]
    current_group = 10
    while sequence_as_int:
        numbers_in_current_group = [x for x in sequence_as_int if x <= current_group]
        print(f"Group of {current_group}'s: {numbers_in_current_group}")
        sequence_as_int = [y for y in sequence_as_int if y not in numbers_in_current_group]
        current_group += 10


sequence_of_number = input().split(", ")
group_of_tens(sequence_of_number)