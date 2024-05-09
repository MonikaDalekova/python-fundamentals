count_of_words = int(input())
synonyms = {}
for _ in range(count_of_words):
    key = input()
    value = input()
    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(value)

for word, all_synonyms in synonyms.items():
    print(f"{word} - {', '.join(all_synonyms)}")