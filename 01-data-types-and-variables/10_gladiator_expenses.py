number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // (2*3)
total_armor_broken = total_shield_broken // 2
expenses = total_helmet_broken * helmet_price + \
           total_sword_broken * sword_price + \
           total_shield_broken * shield_price + \
           total_armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")

# number_of_lost_fights = int(input())
# expenses = 0
# shield_broken = 0
# for every_fight in range(1, number_of_lost_fights):
#     helmet_price = float(input())
#     sword_price = float(input())
#     shield_price = float(input())
#     armor_price = float(input())
#     if every_fight % 2 == 0:
#         expenses += helmet_price
#     if every_fight % 3 == 0:
#         expenses += sword_price
#     if every_fight % 6 == 0:
#         expenses += shield_price
#         shield_broken += 1
#         if shield_broken % 2 == 0:
#             expenses += armor_price
# print(f"Gladiator expenses: {expenses} aureus")
