# def repeated(word, counter):
#     result = word * counter
#     return result
#
#
# string = input()
# counter_n = int(input())
# res = repeated(string, counter_n)
# print(res)

repeated = lambda string, counter: (string * counter)


word = input()
n = int(input())
result = repeated(word, n)
print(result)