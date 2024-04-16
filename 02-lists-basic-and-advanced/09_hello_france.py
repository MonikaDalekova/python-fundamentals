def clothes(a, b, c, d):
    if c >= b:
        if b <= 50:
            d.append(b)
            c -= b
    return c, d


def shoes(a, b, c, d):
    if c >= b:
        if b <= 35:
            d.append(b)
            c -= b
    return c, d


def accessories(a, b, c, d):
    if c >= b:
        if b <= 20.50:
            d.append(b)
            c -= b
    return c, d


train_ticket = 150
collection_of_items = input().split("|")
budget = float(input())
bought_items = []

for every_collection in collection_of_items:
    type_item, price = every_collection.split("->")
    price = float(price)
    if type_item == "Clothes":
        budget, bought_items = clothes(type_item, price, budget, bought_items)
    elif type_item == "Shoes":
        budget, bought_items = shoes(type_item, price, budget, bought_items)
    elif type_item == "Accessories":
        budget, bought_items = accessories(type_item, price, budget, bought_items)

sold_items = ([(x*1.4) for x in bought_items])
budget_after_selling = budget + sum(sold_items)
profit = budget_after_selling - (budget + sum(bought_items))
new_sold_items = ["%.2f" % num for num in sold_items] # форматира до втория знак и прави всичко в стринг
print(f"{' '.join(new_sold_items)}")
print(f"Profit: {profit:.2f}")
if budget_after_selling >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
