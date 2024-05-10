text = input()
final_string = ""
repetition = ""
current_symbol = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index].upper()
    else:
        for next_symbol in range(index, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetition += text[next_symbol]
        final_string += current_symbol*int(repetition)
        repetition = ""
        current_symbol = ""
print(f"Unique symbols used: {len(''.join(set(final_string)))}")
print(final_string)