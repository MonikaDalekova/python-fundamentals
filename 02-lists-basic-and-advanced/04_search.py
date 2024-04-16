# number = int(input())
# word = input()
# text_list = []
# string_containing_word = []
# for _ in range(number):
#     text = input()
#     text_list.append(text)
#     if word in text:
#         string_containing_word.append(text)
# print(text_list)
# print(string_containing_word)



def some_words(a, b):
    current_list = []
    final_list = []
    for _ in range(a):
        current_word = input()
        current_list.append(current_word)
        if b in current_word:
            final_list.append(current_word)
    print(current_list)
    print(final_list)


n = int(input())
word = input()
some_words(n, word)