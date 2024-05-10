# current_dict = {}
# while True:
#     data = input()
#     if data == "buy":
#         break
#     product_name, product_price, product_quantity = data.split()
#     product_quantity = int(product_quantity)
#     product_price = float(product_price)
#     if product_name not in current_dict:
#         current_dict[product_name] = {"price": product_price, "quantity": product_quantity}
#
#     else:
#         current_dict[product_name]["quantity"] += product_quantity
#         if current_dict[product_name]["price"] != product_price:
#             current_dict[product_name]["price"] = product_price
#
# for name, info in current_dict.items():
#     total_price = info["price"] * info["quantity"]
#     print(f"{name} -> {total_price:.2f}")

#2
def products(product, price, quantity):
    if product not in products_dict:
        products_dict[product] = {}
        products_dict[product]['quantity'] = quantity
        products_dict[product]['price'] = price
    else:
        products_dict[product]['quantity'] += quantity
        products_dict[product]['price'] = price


def printer():
    for name, data in products_dict.items():
        total_price = data['quantity'] * data['price']
        print(f'{name} -> {total_price:.2f}')


command = input()
products_dict = {}

while command != 'buy':
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    products(product, price, quantity)
    command = input()
printer()