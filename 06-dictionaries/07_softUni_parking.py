# registered = {}
# number_of_registrations = int(input())
#
# for registration in range(number_of_registrations):
#     data = input().split()
#     command = data[0]
#     name = data[1]
#     if command == "register":
#         license_plate_number = data[2]
#         if name in registered.keys():
#             print(f"ERROR: already registered with plate number {registered[name]}")
#         else:
#             registered[name] = license_plate_number
#             print(f"{name} registered {license_plate_number} successfully")
#
#     else:
#         if name in registered.keys():
#             registered.pop(name)
#             print(f"{name} unregistered successfully")
#         else:
#             print(f"ERROR: user {name} not found")
# for username, license_plate_number in registered.items():
#     print(f"{username} => {license_plate_number}")

#2
def registered_cars(command):
    username = command[1]
    license_plate_number = command[2]
    if username not in parked_cars:
        parked_cars[username] = license_plate_number
        print(f'{username} registered {license_plate_number} successfully')
    else:
        print(f"ERROR: already registered with plate number {license_plate_number}")


def unregistered_cars(command):
    username = command[1]
    if username not in parked_cars.keys():
        print(f"ERROR: user {username} not found")
    else:
        parked_cars.pop(username)
        print(f"{username} unregistered successfully")


def printed_cars():
    for username, plate_number in parked_cars.items():
        print(f"{username} => {plate_number}")


parked_cars = {}
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "register":
        registered_cars(command)
    elif command[0] == "unregister":
        unregistered_cars(command)
printed_cars()