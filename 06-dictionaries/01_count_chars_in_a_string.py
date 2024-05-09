# data = [character for character in input() if character != " "]
# some_dict = {}
# for letter in data:
#     if letter not in some_dict.keys():
#         some_dict[letter] = 0
#     some_dict[letter] += 1
# for letter, occurences in some_dict.items():
#     print(f"{letter} -> {some_dict[letter]}")

#2
def chars(a):
    some_dict = {}
    for char in a:
        if char not in some_dict:
            some_dict[char] = 0
        some_dict[char] += 1
    for char, occurences in some_dict.items():
        print(f"{char} -> {some_dict[char]}")


text = [char for char in input() if char != ' ']
chars(text)