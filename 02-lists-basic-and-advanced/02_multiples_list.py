#1
# factor = int(input())
# count = int(input())
#
# current_list = []
# for el in range(factor, (factor * count) + 1, factor):
#     current_list.append(el)
# print(current_list)

#2
# factor = int(input())
# count = int(input())
# result = []
#
# for num in range(1, count + 1):
#     result.append(num * factor)
# print(result)

#3
def multiply(a, b):
    result = []
    for num in range(1, b + 1):
        result.append(num * a)
    last_result = sorted(result)
    return last_result


factor = int(input())
count = int(input())
res = multiply(factor, count)
print(res)