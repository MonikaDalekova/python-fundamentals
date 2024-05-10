while True:
    data = input()
    if data == "end":
        break
    reversed_word = data[::-1]
    print(f"{data} = {reversed_word}")