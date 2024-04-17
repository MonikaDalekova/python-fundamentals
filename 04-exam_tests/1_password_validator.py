password = input()

while True:
    data = input().split()
    action = data[0]
    if action == "Complete":
        break
    if action == "Make":
        if data[1] == "Upper":
            index = int(data[2])
            upper = password[index].upper()
            password = password.replace(password[index], upper, 1)
            print(password)
        elif data[1] == "Lower":
            index = int(data[2])
            lower = password[index].lower()
            password = password.replace(password[index], lower, 1)
            print(password)
    elif action == "Insert":
        index = int(data[1])
        char = data[2]
        if 0 <= index < len(password):
            password = password[:index] + char + password[index:]
            print(password)
    elif action == "Replace":
        char = data[1]
        value = int(data[2])
        if char in password:
            new_symbol = chr(ord(char) + value)
            password = password.replace(char, new_symbol)
            print(password)
    elif action == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        for char in password:
            if not (char.isalnum() or char == "_"):
                print("Password must consist only of letters, digits and _!")
                break
        uppercase = 0
        for char in password:
            if char.isupper():
                uppercase += 1
                break
        if uppercase == 0:
            print("Password must consist at least one uppercase letter!")
        lowercase = 0
        for char in password:
            if char.islower():
                lowercase += 1
        if lowercase == 0:
            print("Password must consist at least one lowercase letter!")
        digit = 0
        for char in password:
            if char.isdigit():
                digit += 1
        if digit == 0:
            print("Password must consist at least one digit!")