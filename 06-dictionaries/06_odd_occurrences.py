sequence_elements = input().lower().split()
default = 0
elements = dict.fromkeys(sequence_elements, default)
for element in sequence_elements:
    elements[element] += 1
for element, count in elements.items():
    if count % 2 != 0:
        print(element, end=" ")