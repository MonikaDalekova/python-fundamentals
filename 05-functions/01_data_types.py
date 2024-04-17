def data_types(a, b):
    if a == "int":
        result = int(b) * 2
        print(f"{result}")
    elif a == "real":
        result = float(b) * 1.5
        print(f"{result:.2f}")
    elif a == "string":
        result = b
        print(f"${result}$")


string = input()
string_two = input()
data_types(string, string_two)