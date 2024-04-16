deck_of_cards = input().split()
count_of_shuffles = int(input())

for every_shuffle in range(count_of_shuffles):
    final_shuffle_list = []
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    for card_index in range(len(left_part)):
        final_shuffle_list.append(left_part[card_index])
        final_shuffle_list.append(right_part[card_index])
    deck_of_cards = final_shuffle_list
print(deck_of_cards)