import re

text = input()
# pattern = r"(@|#)+[a-z]{3,}(@|#)+.[^[:alnum:]]*\/+\d+\/+"
pattern = r"[@#]+([a-z]{3,})[@#]+\W*\/+(\d+)\/+"

eggs = re.findall(pattern, text)
for match in eggs:
    print(f"You found {match[1]} {match[0]} eggs!")