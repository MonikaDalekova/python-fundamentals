def valid_password(a):
    errors = []
    if not 6 <= len(a) <= 10:
        errors.append("Password must be between 6 and 10 characters")
    if not a.isalnum():
        errors.append("Password must consist only of letters and digits")
    if sum(char.isdigit() for char in a) < 2:
        errors.append("Password must have at least 2 digits")
    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


password = input()
valid_password(password)