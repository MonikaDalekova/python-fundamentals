current_text = input()
encrypted_text = ""
for index in range(len(current_text)):
    searched_chr_ord = ord(current_text[index]) + 3
    encrypted_text += chr(searched_chr_ord)
print(encrypted_text)