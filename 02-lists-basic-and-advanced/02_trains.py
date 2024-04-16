# wagons = [0] * int(input())
#
# command = input().split()
# while command[0] != "End":
#     if command[0] == "add":
#         wagons[-1] += int(command[1])
#     elif command[0] == "insert":
#         index = int(command[1])
#         wagons[index] += int(command[2])
#     elif command[0] == "leave":
#         index = int(command[1])
#         wagons[index] -= int(command[2])
#     command = input().split()
# if command[0] == "End":
#     print(wagons)


def add_command(command):
    people = int(command[1])
    wagons[-1] += people
    return wagons


def insert_command(command):
    index = int(command[1])
    people = int(command[2])
    wagons[index] += people
    return wagons


def leave_command(command):
    index = int(command[1])
    people = int(command[2])
    wagons[index] -= people
    return wagons


wagons = [0] * int(input())
while True:
    command = input().split()
    if command[0] == "End":
        break
    if command[0] == "add":
        wagons = add_command(command)
    elif command[0] == "insert":
        wagons = insert_command(command)
    elif command[0] == "leave":
        wagons = leave_command(command)
print(wagons)




