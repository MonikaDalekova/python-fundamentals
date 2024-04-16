# current_version = [int(number) for number in input().split(".")]
# current_version[-1] += 1
# for index in range(len(current_version)-1, 0, -1):
#     if current_version[index] > 9:
#         current_version[index] = 0
#         current_version[index-1] += 1
# print(*current_version, sep=".")



def next(a):
    a[-1] += 1
    for index in range(len(a)-1, 0, -1):
        if a[index] > 9:
            a[index] = 0
            a[index-1] += 1
    print(*a, sep=".")


current_version = [int(x) for x in input().split(".")]
next(current_version)