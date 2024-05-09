# characters = input().split(", ")
# my_dict = {}
# for character in characters:
#     key = character
#     value = ord(character)
#     my_dict[key] = value
# print(my_dict)

characters = input().split(", ")
print({char: ord(char) for char in characters}) # ключ: стойност за всеки елемент от листа