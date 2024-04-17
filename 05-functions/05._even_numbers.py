current_integers = input().split()
current_integers_int = []
for element in current_integers:
    element = int(element)
    current_integers_int.append(element)
result = filter(lambda a: a % 2 == 0, current_integers_int)
print(list(result))