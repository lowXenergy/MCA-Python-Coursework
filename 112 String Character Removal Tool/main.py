# def remove_at_position():
#     # Step 1: Input string
#     s = input("Enter a string: ")

#     # Step 2: Input position (1-based)
#     pos = int(input("Enter position to remove (starting from 1): "))

#     # Convert to 0-based index
#     index = pos - 1

#     # Step 3: Validate
#     if index < 0 or index >= len(s):
#         print("Invalid position")
#         return

#     # Step 4: Remove character
#     result = s[:index] + s[index+1:]

#     # Step 5: Output
#     print("Updated string:", result)


# remove_at_position()



# Step 1: Input string
# s = input("Enter a string: ")

# # Step 2: Input position (1-based)
# pos = int(input("Enter position to remove (starting from 1): "))

# # Convert to 0-based index
# index = pos - 1

# # Step 3: Validate position
# if index < 0 or index >= len(s):
#     print("Invalid position")
# else:
#     # Step 4: Remove character manually
#     result = ""

#     for i in range(len(s)):
#         if i != index:
#             result += s[i]

#     # Step 5: Output
#     print("Updated string:", result)


# Input
s = input("Enter a string: ")
ch = input("Enter the character to remove: ")
k = int(input("Enter which occurrence to remove: "))

# Edge case 1: invalid k
if k <= 0:
    print("Invalid occurrence number (must be >= 1)")
else:
    count = 0
    result = ""

    for i in range(len(s)):
        if s[i] == ch:
            count += 1
            if count == k:
                continue
        result += s[i]

    # Edge case 2: occurrence not found
    if count < k:
        print("Character not found or occurrence does not exist")
    else:
        print("Updated string:", result)