def calculator(operator, first_num, second_num):
    result = 0
    if operator == "multiply":
        result = first_num * second_num
    elif operator == "divide":
        result = first_num // second_num
    elif operator == "add":
        result = first_num + second_num
    elif operator == "subtract":
        result = first_num - second_num
    return result


op = input()
num1 = int(input())
num2 = int(input())
res = calculator(op, num1, num2)
print(res)