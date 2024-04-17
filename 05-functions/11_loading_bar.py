# def loading_bar(num):
#     result = ""
#     percentages = ""
#     dots = ""
#     if num < 100:
#         result += ((str(num)) + "%")
#         percentages = "%"*(num // 10)
#         dots = "."*(10 - num // 10)
#         print(f"{result} [{percentages + dots}] ")
#         print("Still loading...")
#     elif num == 100:
#         print("100% Complete!")
#         print("[%%%%%%%%%%]")
#
#
# integer_number = int(input())
# loading_bar(integer_number)

def loading_bar(num):
    percentage_list = []
    dot_list = []
    if num < 100:
        for _ in range(num // 10):
            percentage_list.append("%")
        for _ in range(10 - num // 10):
            dot_list.append(".")
        final_list = percentage_list + dot_list
        print(f"{num}% [{''.join(final_list)}]")
        print("Still loading...")
    elif num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


integer_number = int(input())
loading_bar(integer_number)