s = input("Enter a string: ")

words = []
word = ""

# build words manually
for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

# swap adjacent pairs
for i in range(0, len(words)-1, 2):
    words[i], words[i+1] = words[i+1], words[i]

# build result manually
result = ""
for w in words:
    result += w + " "

print("Result:", result)