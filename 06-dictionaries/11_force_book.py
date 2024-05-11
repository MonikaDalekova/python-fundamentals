# side_dictionary = {}
# while True:
#     data = input()
#     if data == "Lumpawaroo":
#         break
#
#     if " | " in data:
#         force_side, force_user = data.split(" | ")
#         user_part_of_the_force = False
#
#         for value in side_dictionary.values():
#             if force_user in value:
#                 user_part_of_the_force = True
#                 break
#         if not user_part_of_the_force:
#             if force_side not in side_dictionary.keys():
#                 side_dictionary[force_side] = []
#             side_dictionary[force_side].append(force_user)
#     elif " -> " in data:
#         force_user, force_side = data.split(" -> ")
#         for value in side_dictionary.values():
#             if force_user in value:
#                 value.remove(force_user)
#                 break
#         if force_side not in side_dictionary.keys():
#             side_dictionary[force_side] = []
#         side_dictionary[force_side].append(force_user)
#         print(f"{force_user} joins the {force_side} side!")
# for force_side, force_users in side_dictionary.items():
#     if len(force_users) > 0:
#         print(f"Side: {force_side}, Members: {len(force_users)}")
#         for users in force_users:
#             print(f"! {users}")

#2
def user_existence(force_user):
    for value in sides_dict.values():
        if force_user in value:
            user_in_side = True
            return user_in_side


def first_option(command):
    force_side, force_user = command.split(" | ")
    user_in_side = user_existence(force_user)
    if not user_in_side:
        if force_side not in sides_dict.keys():
            sides_dict[force_side] = []
        sides_dict[force_side].append(force_user)
    return sides_dict


def second_option(command):
    force_user, force_side = command.split(" -> ")
    for value in sides_dict.values():
        if force_user in value:
            value.remove(force_user)
            break
    if force_side not in sides_dict.keys():
        sides_dict[force_side] = []
    sides_dict[force_side].append(force_user)
    print(f"{force_user} joins the {force_side} side!")
    return sides_dict


user_in_side = False
sides_dict = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        sides_dict = first_option(command)
    elif "->" in command:
        sides_dict = second_option(command)
    command = input()
for key, value in sides_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")