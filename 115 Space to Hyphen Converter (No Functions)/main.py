# Input string
s = input("Enter a string: ")

result = ""

# Traverse string manually
for ch in s:
    if ch == " ":
        result += "-"
    else:
        result += ch

# Output
print("Updated string:", result)