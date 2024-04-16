# year = int(input())
# while True:
#     year += 1
#     year_as_str = str(year)
#     if len(year_as_str) == len(set(year_as_str)):
#         break
# print(year)

year = int(input())

while True:
    year += 1
    happy_year = True
    already_has_digit = ""
    for digit in str(year):
        if digit in already_has_digit:
            happy_year = False
            break
        already_has_digit += digit
    if happy_year:
        break
print(year)

