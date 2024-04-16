# money_as_string = input().split(", ")
# count_of_beggars = int(input())
# money_as_integers = []
# for every_string in money_as_string:
#     money_as_integers.append(int(every_string))
# final_sum = []
# start_index = 0
# for every_beggar in range(count_of_beggars):
#     current_sum = 0
#     for current_index in range(start_index, len(money_as_integers), count_of_beggars):
#         current_sum += money_as_integers[current_index]
#     final_sum.append(current_sum)
#     start_index += 1
# print(final_sum)

money_as_integers = [int(money) for money in input().split(", ")]
count_of_beggars = int(input())

final_sums = []
start_index = 0
for every_beggar in range(count_of_beggars):
    current_sum = 0
    for current_index in range(start_index, len(money_as_integers), count_of_beggars):
        current_sum += money_as_integers[current_index]
    final_sums.append(current_sum)
    start_index += 1
print(final_sums)


