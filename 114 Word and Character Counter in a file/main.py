# Open file in read mode
f = open("input.txt", "r")

char_count = 0
word_count = 0
line_count = 0

in_word = False  # track word boundaries

# Read file line by line
for line in f:
    line_count += 1   # count lines

    i = 0
    while i < len(line):
        ch = line[i]

        # Count characters (excluding spaces and newline if you want)
        if ch != " " and ch != "\n":
            char_count += 1

            # Word start detection
            if in_word == False:
                word_count += 1
                in_word = True
        else:
            # Space or newline ends a word
            in_word = False

        i += 1

# Close file
f.close()

# Output
print("Number of characters (excluding spaces):", char_count)
print("Number of words:", word_count)
print("Number of lines:", line_count)