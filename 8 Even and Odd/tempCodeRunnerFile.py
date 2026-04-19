num = int(input("Enter a number: "))

result = ["Even" if x % 2 == 0 else "Odd" for x in [num]]
print(result[0])