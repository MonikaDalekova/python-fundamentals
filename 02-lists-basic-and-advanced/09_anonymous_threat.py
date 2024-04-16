initial_string = input().split()

while True:
    current_command = input().split()

    if current_command[0] == "3:1":
        break

    if current_command[0] == "merge":
        startIndex = int(current_command[1])
        endIndex = int(current_command[2])
        if startIndex < 0:
            startIndex = 0
        if endIndex > len(initial_string) - 1:
            endIndex = len(initial_string) - 1
        merged_parts = "".join(initial_string[startIndex:endIndex+1])
        initial_string[startIndex:endIndex+1] = [merged_parts]
    elif current_command[0] == "divide":
        index = int(current_command[1])
        partitions = int(current_command[2])
        element = initial_string[index]


            print(current_string)

