# def characters_between(a, b):
#     string_list = []
#     for el in range(ord(a) + 1, ord(b)):
#         el_str = chr(el)
#         string_list.append(el_str)
#     return string_list
#
#
# character_one = input()
# character_two = input()
# print(" ".join(characters_between(character_one, character_two)))

def characters_between(a, b):
    result = ""
    for i in range(ord(a) + 1, ord(b)):
        result += chr(i) + ' '
    return result


character_one = input()
character_two = input()
print(characters_between(character_one, character_two))