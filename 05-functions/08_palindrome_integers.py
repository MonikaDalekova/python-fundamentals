def palindrome_number(a):
    result = ""
    for number in a:
        if str(number) == str(number)[::-1]:
            result += "True\n"
        else:
            result += "False\n"
    return result


current_list = list(map(int, input().split(", ")))
print(palindrome_number(current_list))