string_input = input().split(" ")

decipher_string_1 = []
final_decipher_string = []

number = ''
for word in string_input:
    for char in word:
        if char.isdigit():
            number += char
        else:
            decipher_string_1.append(char)

    # find letter on the current number
    letter = chr(int(number))
    # insert letter in the beginning of string
    decipher_string_1.insert(0, letter)
    number = ''
    # swap second and last letter
    sec_letter = decipher_string_1[1]
    last_letter = decipher_string_1[-1]
    decipher_string_1[1] = last_letter
    decipher_string_1[-1] = sec_letter
    final_decipher_string.extend(decipher_string_1)
    final_decipher_string.extend(' ')
    decipher_string_1 = []

print(''.join(final_decipher_string))



