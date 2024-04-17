notebook = {}
words = input().split(" | ")
for index in range(len(words)):
    word, definition = words[index].split(": ")
    if word not in notebook.keys():
        notebook[word] = []
    notebook[word].append(definition)

test_words = input().split(" | ")
command = input()

if command == "Test":
    for word in test_words:
        if word in notebook.keys():
            print(f"{word}:")
            print(f"  -" + "\n  -".join(notebook[word]))
elif command == "Hand Over":
    for key in notebook.keys():
        print(key, end=" ")





