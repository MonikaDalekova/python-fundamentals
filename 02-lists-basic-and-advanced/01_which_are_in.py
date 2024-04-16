first_sequence = input().split(", ")
second_sequence = input().split(", ")

final_list = []

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            final_list.append(first_string)
            break

print(final_list)

# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# final_list = [first_string for first_string in first_sequence \
#               if any(first_string in second_string for second_string in second_sequence)]
# print(final_list)