num = int(input("Enter a number: "))

for i in range(11):
    print(f"{num} X {i} = {num*i}")

# table = [f"{num} x {i} = {num*i}" for i in range(1, 11)]

# print("\n".join(table))

# range(1, 11) → generates 1 to 10
# Each element is formatted as a string
# Entire table is generated in one line