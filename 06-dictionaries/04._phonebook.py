# phonebook = {}
# while True:
#     entry = input()
#     if "-" not in entry:
#         break
#     name, number = entry.split("-")
#     phonebook[name] = number
# searches = int(entry)
# for _ in range(searches):
#     searched_name = input()
#     if searched_name not in phonebook.keys():
#         print(f"Contact {searched_name} does not exist.")
#     else:
#         print(f"{searched_name} -> {phonebook[searched_name]}")

#2
def phonebook(name, number):
    phonebook_dict[name] = number
    return phonebook_dict


def searched_names(name):
    if name not in phonebook_dict.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook_dict[name]}")


phonebook_dict = {}
entry = input()
while "-" in entry:
    name, number = entry.split('-')
    phonebook_dict = phonebook(name, number)
    entry = input()

for _ in range(int(entry)):
    name = input()
    searched_names(name)