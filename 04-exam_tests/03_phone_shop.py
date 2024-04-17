storage_list_of_phones = input().split(", ")

command = input()
while command != "End":
    action, phone = command.split(" - ")

    if action == "Add":
        if phone not in storage_list_of_phones:
            storage_list_of_phones.append(phone)

    elif action == "Remove":
        if phone in storage_list_of_phones:
            storage_list_of_phones.remove(phone)

    elif action == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in storage_list_of_phones:
            old_phone_index = storage_list_of_phones.index(old_phone)
            storage_list_of_phones.insert(old_phone_index + 1, new_phone)

    elif action == "Last":
        if phone in storage_list_of_phones:
            storage_list_of_phones.remove(phone)
            storage_list_of_phones.append(phone)

    command = input()

print(*storage_list_of_phones, sep=", ")