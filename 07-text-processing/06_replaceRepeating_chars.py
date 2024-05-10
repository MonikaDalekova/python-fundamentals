text = input()
last_string = ""
new_text = ""
for index in range(len(text)):
    if text[index] != last_string:
        new_text += text[index]
        last_string = text[index]
    else:
        continue
print(new_text)