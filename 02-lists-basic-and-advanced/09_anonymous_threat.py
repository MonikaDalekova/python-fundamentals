def merge(command, my_list):
    startIndex = int(command[1])
    endIndex = int(command[2])
    if startIndex < 0:
        startIndex = 0
    elif endIndex > len(my_list)-1:
        endIndex = len(my_list)-1
    merged_part = ''.join(my_list[startIndex:endIndex+1])
    my_list[startIndex:endIndex+1] = [merged_part]
    return my_list


def divide(command, my_list):
    index = int(command[1])
    partitions = int(command[2])
    divided_partitions = []
    element = my_list[index]
    partition_length = len(element) // partitions
    for current_element_index in range(partitions):
        if current_element_index != partitions - 1:
            divided_partitions.append(element[current_element_index * partition_length: (current_element_index + 1)\
                                                                                        * partition_length])
        else:
            divided_partitions.append(element[current_element_index * partition_length:])
    my_list[index:index + 1] = divided_partitions
    return my_list


initial_string = input().split()
command = input()
while command != "3:1":
    command = command.split()
    if command[0] == "merge":
        initial_string = merge(command, initial_string)
    elif command[0] == "divide":
        initial_string = divide(command, initial_string)
    command = input()
print(*initial_string, sep=" ")
