def total_price(food, n):
    price = 0
    if food == "coffee":
        price = n * 1.50
    elif food == "water":
        price = n * 1.00
    elif food == "coke":
        price = n * 1.40
    elif food == "snacks":
        price = n * 2.00
    return price


product = input()
quantity = int(input())
res = total_price(product, quantity)
print(f"{res:.2f}")