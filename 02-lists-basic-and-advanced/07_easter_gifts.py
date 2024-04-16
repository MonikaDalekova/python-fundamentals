# received_gifts = input().split()
# command = input()
#
# while command != "No Money":
#     command_new = command.split()
#
#     if "OutOfStock" in command:
#         for i in range(len(received_gifts)):
#             if command_new[1] in received_gifts[i]:
#                 received_gifts[i] = "None"
#     elif "Required" in command:
#         for i in range(len(received_gifts)):
#             if i == int(command_new[2]):
#                 received_gifts[i] = command_new[1]
#     elif "JustInCase" in command:
#         received_gifts[-1] = command_new[1]
#
#     command = input()
#
# while "None" in received_gifts:
#     received_gifts.remove("None")
#
# for i in received_gifts:
#     print(i, end=" ")



def outofstock(gifts_list, command):
    gift = command[1]
    for i in range(len(gifts_list)):
        if gift == gifts_list[i]:
            gifts_list[i] = "None"
    return gifts_list


def required(gifts_list, command):
    gift = command[1]
    index = int(command[2])
    if 0 <= index < len(gifts_list):
        gifts_list[index] = gift
    return gifts_list


def justincase(gifts_list, command):
    gift = command[1]
    gifts_list[-1] = gift
    return gifts_list


def final_print(gifts_list):
    for i in gifts_list:
        if i != "None":
            print(i, end=" ")


gifts_list = input().split()
command = input()
while command != "No Money":
    new_command = command.split()
    if new_command[0] == "No Money":
        break
    if new_command[0] == "OutOfStock":
        gifts_list = outofstock(gifts_list, new_command)
    elif new_command[0] == "Required":
        gifts_list = required(gifts_list, new_command)
    elif new_command[0] == "JustInCase":
        gifts_list = justincase(gifts_list, new_command)
    command = input()

final_print(gifts_list)