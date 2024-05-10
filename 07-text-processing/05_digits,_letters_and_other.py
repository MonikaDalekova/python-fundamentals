text = input()
digits = ""
letters = ""
characters = ""
for smth in text:
    if smth.isdigit():
        digits += smth
    elif smth.isalpha():
        letters += smth
    else:
        characters += smth
print(digits)
print(letters)
print(characters)