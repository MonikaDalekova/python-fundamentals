# words_sequence = input().split()
# palindrome = input()
# count_palindromes = 0
# palindromes_list = []
# for word in words_sequence:
#     if word == palindrome:
#         count_palindromes += 1
#     if word == word[::-1]:
#         palindromes_list.append(word)
# print(palindromes_list)
# print(f"Found palindrome {count_palindromes} times")

def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split(' ')
palindrome = input()

palindrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = palindrome_list.count(palindrome)

print(palindrome_list)
print(f'Found palindrome {palindrome_counter} times')
