# resources = {}
# while True:
#     current_resource = input()
#     if current_resource == "stop":
#         break
#     current_quantity = int(input())
#     if current_resource not in resources.keys():
#         resources[current_resource] = 0
#     resources[current_resource] += current_quantity
#
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")

#2
def resources(a, b):
    resources_dict = {}
    if a not in resources_dict:
        resources_dict[a] = 0
    resources_dict[a] += b
    for resource, quantity in resources_dict.items():
        print(f"{resource} -> {quantity}")


while True:
    command = input()
    if command == 'stop':
        break
    current_quantity = int(input())
    resources(command, current_quantity)