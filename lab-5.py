# Task 1.1
# word = input("Enter the word: ")
# print(tuple(word))

## Task 1.2
# def counter(letters):
#     occurence = []
#     for char in letters:
#         pass

# def letterify(word):
#     letters = []
#     for char in word:
#         letters.append(char)
#     return letters

# word = input("Enter the word: ")
# occurences = []

# for char in word:
#     count = word.count(char)
#     occurences.append(count)

# finalList = list(zip(letterify(word), occurences))

# print(finalList)

# # Taks 1.3
# def vowelOrConsonant(x):
#     if x in 'aeiouAEIOU':
#         return 1 #vowel
#     elif x.isalpha():
#         return 2 #consonant
#     else:
#         return 3 #symbol, neither of them

# word = input("Enter the word: ")
# list_vow = []
# list_cons = []
# list_sym = []

# checker = 0
# for char in word:
#     checker = vowelOrConsonant(char)
#     if checker == 1:
#         list_vow.append((char, word.count(char)))
#     elif checker == 2:
#         list_cons.append((char, word.count(char)))
#     else:
#         list_sym.append((char, word.count(char)))

# print(f"list_vow = {list_vow}")
# print(f"list_cons = {list_cons}")
# print(f"list_sym = {list_sym}")

