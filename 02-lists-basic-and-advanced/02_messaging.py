# 1
# sequence_of_numbers = input().split()
# string = input()
# string_list = []
# for element in string:
#     string_list.append(element)
# final_message = []
#
# for number in sequence_of_numbers:
#     sum_digits = 0
#     for digit in number:
#         number = int(number)
#         sum_digits += int(digit)
#     if sum_digits < len(string_list):
#         final_message.append(string_list[sum_digits])
#         string_list.remove(string_list[sum_digits])
#     else:
#         new_sum = sum_digits % len(string_list)
#         final_message.append(string_list[new_sum])
#         string_list.remove(string_list[new_sum])
# print("".join(final_message))


# 2
# numbers = [list(int(y) for y in x) for x in input().split(" ")]
# string = input()
# message = ""
#
# for number in numbers:
#     index = sum(number)
#     if index >= len(string):
#         index %= len(string)
#     message += string[index]
#     string = string[:index] + string[index + 1:]
#
# print(message)


#3
def messaging(a, b):
    message = ""
    for el in a:
        index = sum(el)
        if index >= len(b):
            index %= len(b)
        message += b[index]
        b = b[:index] + b[index + 1:]
    print(message)
    return a, b


sequence_of_integers = [list(int(y) for y in x) for x in input().split(' ')]
string = input()
sequence_of_integers, string = messaging(sequence_of_integers, string)