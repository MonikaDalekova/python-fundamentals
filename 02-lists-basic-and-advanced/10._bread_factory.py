# event_list = input().split("|")
#
# total_energy = 100
# initial_coins = 100
# open_bakery = True
#
# for every_event in event_list:
#     event_type, value_of_event = every_event.split("-")
#     value_of_event = int(value_of_event)
#     if event_type == "rest":
#         initial_energy = total_energy
#         total_energy += value_of_event
#         if total_energy > 100:
#             total_energy = 100
#         gained_energy = total_energy - initial_energy
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {total_energy}.")
#     elif event_type == "order":
#         if total_energy >= 30:
#             total_energy -= 30
#             initial_coins += value_of_event
#             print(f"You earned {value_of_event} coins.")
#         else:
#             total_energy += 50
#             print("You had to rest!")
#     else:
#         if initial_coins >= value_of_event:
#             initial_coins -= value_of_event
#             print(f"You bought {event_type}.")
#         else:
#             open_bakery = False
#             break
#
# if open_bakery:
#     print("Day completed!")
#     print(f"Coins: {initial_coins}")
#     print(f"Energy: {total_energy}")
# else:
#     print(f"Closed! Cannot afford {event_type}.")

def rest(a, int_number):
    initial_energy = a
    a += int_number
    if a > 100:
        a = 100
    gained_energy = a - initial_energy
    print(f"You gained {gained_energy} energy.")
    print(f"Current energy: {a}.")
    return a


def order(a, b, int_number):
    if a >= 30:
        a -= 30
        b += int_number
        print(f"You earned {int_number} coins.")
    else:
        a += 50
        print(f"You had to rest!")
    return a, b


def ingredient(b, int_number, open_bakery):
    if b >= int_number:
        b -= int_number
        print(f"You bought {event}.")
    else:
        open_bakery = False
    return b, open_bakery


total_energy = 100
initial_coins = 100
events = input().split("|")
open_bakery = True

for every_event in events:
    event, number = every_event.split("-")
    int_number = int(number)
    if event == "rest":
        total_energy = rest(total_energy, int_number)
    elif event == "order":
        total_energy, initial_coins = order(total_energy, initial_coins, int_number)
    else:
        initial_coins, open_bakery = ingredient(initial_coins, int_number, open_bakery)
        if not open_bakery:
            print(f"Closed! Cannot afford {event}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {total_energy}")