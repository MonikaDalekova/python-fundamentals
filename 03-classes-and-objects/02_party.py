class Party:               # създавам схемата на обекта
    def __init__(self):
        self.people = []


party = Party()           # инициализирам обект party


name = input()            # вкарвам съдържанието на параметъра
while name != "End":
    party.people.append(name)
    name = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")