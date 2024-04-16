text = input()
sorted_text = [el for el in text if el.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(sorted_text))