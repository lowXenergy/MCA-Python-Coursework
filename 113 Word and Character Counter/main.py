# # Input string
# s = input("Enter a string: ")

# char_count = 0
# word_count = 0
# in_word = False   # flag to track word boundaries

# # Traverse manually
# i = 0
# while i < len(s):
#     # Count characters excluding spaces
#     if s[i] != " ":
#         char_count += 1

#         # Detect start of a new word
#         if in_word == False:
#             word_count += 1
#             in_word = True
#     else:
#         # Space means word ended
#         in_word = False

#     i += 1

# # Output
# print("Number of characters (excluding spaces):", char_count)
# print("Number of words:", word_count)
s = input("Enter a string: ")

char_count = 0
word_count = 0
in_word = False

for i in range(len(s)):
    if s[i] != " ":
        char_count += 1

        if in_word == False:
            word_count += 1
            in_word = True
    else:
        in_word = False

print("Characters (excluding spaces):", char_count)
print("Words:", word_count)
