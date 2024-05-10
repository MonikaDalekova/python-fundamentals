first_character_ord = ord(input())
second_character_ord = ord(input())
text = input()
total_sum = 0
for character in text:
    character_ord = ord(character)
    if first_character_ord < character_ord < second_character_ord:
        total_sum += character_ord
print(total_sum)