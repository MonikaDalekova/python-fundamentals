first, second = input().split()
final_sum = 0

if len(first) > len(second):
    for index in range(len(second)):
        final_sum += ord(first[index]) * ord(second[index])
    for index in range(len(second), len(first)):
        final_sum += ord(first[index])

elif len(first) < len(second):
    for index in range(len(first)):
        final_sum += ord(second[index]) * ord(first[index])
    for index in range(len(first), len(second)):
        final_sum += ord(second[index])

else:
    for index in range(len(second)):
        final_sum += ord(first[index]) * ord(second[index])
print(final_sum)