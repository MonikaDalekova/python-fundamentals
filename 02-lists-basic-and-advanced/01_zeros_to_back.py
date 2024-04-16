# list_str = input().split(", ")
# new_list = []
#
# for every_element in list_str:
#     if every_element != "0":
#         new_list.append(every_element)
# count = list_str.count("0")
# for _ in range(count):
#     new_list.append("0")
# new_list_int = [int(number) for number in new_list]
# print(new_list_int)

# list_of_numbers = [int(x) for x in input().split(", ")]
#
# count = list_of_numbers.count(0)
# list_of_numbers = [x for x in list_of_numbers if x != 0]
# list_of_numbers.extend([0] * count)
#
# print(list_of_numbers)


def zeros(a):
    counter = a.count(0)
    a = [x for x in a if x != 0]
    a.extend([0] * counter)
    return a


list_of_el = [int(x) for x in input().split(", ")]
result = zeros(list_of_el)
print(result)

