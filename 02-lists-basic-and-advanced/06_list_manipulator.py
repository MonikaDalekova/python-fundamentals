# не е вярна

def exchange(command, list_of_integers):
    index = int(command[1])
    if index > len(list_of_integers) or index < 0:
        print("Invalid index")
    else:
        list_of_integers = list_of_integers[index+1:] + list_of_integers[:index+1]
    return list_of_integers


def max_number(command, list_of_integers):
    side = command[1]
    list_index = []
    if side == "even":
        for index, number in enumerate(list_of_integers):
            if number % 2 == 0 and number == max(list_of_integers):
                if list_of_integers.count(max(list_of_integers)) > 0:
                    list_index.append(index)
        if len(list_index) >= 0:
            print(list_index[-1])
        else:
            print("No matches")
    elif side == "odd":
        for index, number in enumerate(list_of_integers):
            if number % 2 != 0 and number == max(list_of_integers):
                if list_of_integers.count(max(list_of_integers)) > 0:
                    list_index.append(index)
        if len(list_index) > 0:
            print(list_index[-1])
        else:
            print("No matches")


def min_number(command, list_of_integers):
    side = command[1]
    list_index = []
    if side == "even":
        for index, number in enumerate(list_of_integers):
            if number % 2 == 0 and number == min(list_of_integers):
                if list_of_integers.count(min(list_of_integers)) > 0:
                    list_index.append(index)
        if len(list_index) > 0:
            print(list_index[-1])
        else:
            print("No matches")
    elif side == "odd":
        for index, number in enumerate(list_of_integers):
            if number % 2 != 0 and number == min(list_of_integers):
                if list_of_integers.count(min(list_of_integers)) > 0:
                    list_index.append(index)
        if len(list_index) > 0:
            print(list_index[-1])
        else:
            print("No matches")


def first(command, list_of_integers):
    count = int(command[1])

    if command[2] == "even":
        if count > len(list_of_integers):
            print("Invalid count")
        else:
            even_list = list(filter(lambda x: x % 2 == 0, list_of_integers))
            if len(even_list) < count:
                print(even_list)
            elif len(even_list) == 0:
                print("[]")
            else:
                while len(even_list) > count:
                    even_list.pop()
                print(even_list)

    elif command[2] == "odd":
        if count > len(list_of_integers):
            print("Invalid count")
        else:
            odd_list = list(filter(lambda x: x % 2 != 0, list_of_integers))
            if len(odd_list) < count:
                print(odd_list)
            elif len(odd_list) == 0:
                print("[]")
            else:
                while len(odd_list) > count:
                    odd_list.pop()
                print(odd_list)


def last(command, list_of_integers):
    count = int(command[1])
    if command[2] == "even":
        if count > len(list_of_integers):
            print("Invalid count")
        else:
            even_list = list(filter(lambda x: x % 2 == 0, list_of_integers))
            if len(even_list) < count:
                print(even_list)
            elif len(even_list) == 0:
                print("[]")
            else:
                print(even_list[-count])
    elif command[2] == "odd":
        if count > len(list_of_integers):
            print("Invalid count")
        else:
            odd_list = list(filter(lambda x: x % 2 != 0, list_of_integers))
            if len(odd_list) < count:
                print(odd_list)
            elif len(odd_list) == 0:
                print("[]")
            else:
                print(odd_list[-count])


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