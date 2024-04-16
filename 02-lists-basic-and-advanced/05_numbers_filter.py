# 1
# n = int(input())
# positive_list = []
# negative_list = []
# even_list = []
# odd_list = []
#
# for _ in range(n):
#     current_number = int(input())
#     if current_number % 2 == 0:
#         even_list.append(current_number)
#     else:
#         odd_list.append(current_number)
#     if current_number >= 0:
#         positive_list.append(current_number)
#     else:
#         negative_list.append(current_number)
# command = input()
# if command == "even":
#     print(even_list)
# elif command == "odd":
#     print(odd_list)
# elif command == "positive":
#     print(positive_list)
# elif command == "negative":
#     print(negative_list)

#2
# n = int(input())
# first_list = []
# current_list = []
# for _ in range(n):
#     current_number = int(input())
#     first_list.append(current_number)
#
# command = input()
# for element in first_list:
#     if command == "even" and element % 2 == 0:
#         current_list.append(element)
#     if command == "odd" and element % 2 != 0:
#         current_list.append(element)
#     if command == "positive" and element >= 0:
#         current_list.append(element)
#     if command == "negative" and element < 0:
#         current_list.append(element)
# print(current_list)

#3
def commands(a, command):
    result = 0
    if command == "even":
        result = list(filter(lambda x: x % 2 == 0, a))
    if command == "odd":
        result = list(filter(lambda x: x % 2 != 0, a))
    if command == "positive":
        result = list(filter(lambda x: x >= 0, a))
    if command == "negative":
        result = list(filter(lambda x: x < 0, a))
    return result


n = int(input())
sequence = []
for _ in range(n):
    number = int(input())
    sequence.append(number)
command = input()
res = commands(sequence, command)
print(res)
