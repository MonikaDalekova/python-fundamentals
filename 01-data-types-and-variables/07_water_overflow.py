number_of_lines = int(input())
capacity = 255

for _ in range(number_of_lines):
    litres = int(input())
    if capacity - litres < 0:
        print("Insufficient capacity!")
        continue
    capacity -= litres

print(255 - capacity)