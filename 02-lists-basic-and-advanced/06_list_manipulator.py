def exchange(command, list_of_integers):
    index = int(command[1])
    if not 0 <= index < len(list_of_integers):
        print("Invalid index")
    else:
        list_of_integers = list_of_integers[index+1:] + list_of_integers[:index+1]
    return list_of_integers


def max_number(command, list_of_integers):
    side = command[1]
    even_list = [int(x) for x in list_of_integers if x % 2 == 0]
    odd_list = [int(x) for x in list_of_integers if x % 2 != 0]
    if side == "even" and even_list:
        print((len(list_of_integers) - list_of_integers[::-1].index(max(even_list)) - 1))
    elif side == "odd" and odd_list:
        print((len(list_of_integers) - list_of_integers[::-1].index(max(odd_list)) - 1))
    else:
        print("No matches")


def min_number(command, list_of_integers):
    side = command[1]
    even_list = [int(x) for x in list_of_integers if x % 2 == 0]
    odd_list = [int(x) for x in list_of_integers if x % 2 != 0]
    if side == "even" and even_list:
        print((len(list_of_integers) - list_of_integers[::-1].index(min(even_list)) - 1))
    elif side == "odd" and odd_list:
        print((len(list_of_integers) - list_of_integers[::-1].index(min(odd_list)) - 1))
    else:
        print("No matches")


def first(command, list_of_integers):
    even_list = [int(x) for x in list_of_integers if x % 2 == 0]
    odd_list = [int(x) for x in list_of_integers if x % 2 != 0]
    if 0 < int(command[1]) <= len(list_of_integers):
        if command[2] == "even":
            print(even_list[0:int(command[1])])
        else:
            print(odd_list[0:int(command[1])])
    else:
        print(f"Invalid count")


def last(command, list_of_integers):
    even_list = [int(x) for x in list_of_integers if x % 2 == 0]
    odd_list = [int(x) for x in list_of_integers if x % 2 != 0]
    if 0 < int(command[1]) <= len(list_of_integers):
        if command[2] == "even":
            print(even_list[-int(command[1]):])
        else:
            print(odd_list[-int(command[1]):])
    else:
        print(f"Invalid count")



list_of_integers = [int(x) for x in input().split()]
while True:
    command = input().split()
    action = command[0]
    if action == "end":
        break
    if action == "exchange":
        list_of_integers = exchange(command, list_of_integers)
    elif action == "max":
        max_number(command, list_of_integers)
    elif action == "min":
        min_number(command, list_of_integers)
    elif action == "first":
        first(command, list_of_integers)
    elif action == "last":
        last(command, list_of_integers)
print(list_of_integers)
