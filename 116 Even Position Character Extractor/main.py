# s = input("Enter a string: ")

# result = ""
# #👉 Final output store karne ke liye empty string

# word = ""
# # 👉 Temporary variable  
# # 👉 Ek-ek character jod ke **current word bana rahe ho**

# word_index = 0   # tracks word position (1-based)
# # 👉 Word ka position track karega

# for ch in s:
# # 👉 Agar current character space nahi hai
# # 👉 Matlab word abhi ban raha hai
#     if ch != " ":
#         word += ch
#         # 👉 Space mila → word khatam
#     else:
#         if word != "":
# # 👉 Check: kya actually koi word bana hai?  
# # 👉 Multiple spaces ko ignore karne ke liye
#             word_index += 1

#             # Keep only even-position words
#             if word_index % 2 == 0:
#                 result += word + " "

#             word = ""
#             # 👉 Reset kar do → next word banana start

# # Handle last word (no trailing space case)
# # 👉 Last word ka index count karo

# if word != "":
#     word_index += 1
#     if word_index % 2 == 0:
#         result += word

# # Output
# print("Result:", result)

s = input("Enter a string: ")

result = ""

for i in range(len(s)):
    
    if i % 2 == 0:
        result = result + s[i]

print("Even position characters:", result)