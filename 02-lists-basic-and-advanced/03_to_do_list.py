def to_do_list():
    final_list = []
    notes_list = []

    while True:
        command = input()
        if command == "End":
            break

        notes_list.append(command)

    sorted_notes = sorted(notes_list, key=lambda x: int(x.split("-")[0]))
    final_list = [command.split("-")[1] for command in sorted_notes]
    return final_list


result = to_do_list()
print(result)