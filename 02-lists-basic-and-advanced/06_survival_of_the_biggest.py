# integer_numbers = [int(integer_number) for integer_number in input().split()]
# to_remove = int(input())
#
# for deleted_num in range(to_remove):
#     integer_numbers.remove(min(integer_numbers))
# final_result = ", ".join(map(str, integer_numbers))
# print(final_result)
#
# на ред 5 получавам лист от инт [10, 9, 8], превръщам ги във str чрез map и от
# лист със стр ги превръщам в просто стр чрез join

integer_numbers = [int(number) for number in input().split()]
to_remove = int(input())

for _ in range(to_remove):
    integer_numbers.remove((min(integer_numbers)))

result = ", ".join([str(number) for number in integer_numbers])
print(result)

# integer_numbers = [int(number) for number in input().split()]
# to_remove = int(input())
#
# for _ in range(to_remove):
#     integer_numbers.remove((min(integer_numbers)))
# list_str = []
# for every_number in integer_numbers:
#     every_number_str = str(every_number)
#     list_str.append(every_number_str)
# result = ", ".join(list_str)
# print(result)


# def minimum_number(a, b):
#     for _ in range(b):
#         a.remove(min(a))
#     return ', '.join([str(num) for num in a])
#
#
# integers = [int(num) for num in input().split()]
# n = int(input())
# result = minimum_number(integers, n)
# print(result)