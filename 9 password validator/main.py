import re  # re = regular expression module in Python.

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

password = input("Enter password: ")

if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")

# Regex (Regular Expression) is a pattern-matching language used to search, validate, and manipulate text.
# “A formula that describes what a valid string looks like.”
# Core Idea

# Instead of checking text character-by-character manually, you define a pattern, and the regex engine checks whether a string matches that pattern.
# The import re statement is used in Python to import the built-in re module, which provides support for working with regular expressions (regex) for searching, matching, and manipulating strings.  Once imported, you can use functions like re.search(), re.findall(), and re.sub() to perform pattern matching and text processing tasks. 

# Key Usage Points
# Raw Strings: Regex patterns should typically be prefixed with r (e.g., r'\d+') to create raw strings, ensuring backslashes are treated literally. 
# Common Functions:
# re.search(): Finds the first occurrence of a pattern.
# re.findall(): Returns a list of all non-overlapping matches.
# re.sub(): Replaces occurrences of a pattern with a specified string.
# re.compile(): Compiles a pattern for reuse, improving performance in loops.

# password = input("Enter password: ")

# special_chars = "@$!%*?&"

# is_valid = (
#     len(password) >= 8 and
#     any(c.islower() for c in password) and
#     any(c.isupper() for c in password) and
#     any(c.isdigit() for c in password) and
#     any(c in special_chars for c in password)
# )

# print("Valid password" if is_valid else "Invalid password")