# num = int(input("Enter the number "))

# if num%2 != 0:
#     print("Odd number")
# else:
#     print("Even number")

# # nums = list(map(int, input("Enter numbers separated by space: ").split()))

# # even = [x for x in nums if x % 2 == 0]
# # odd = [x for x in nums if x % 2 != 0]

# # print("Even numbers:", even)
# # print("Odd numbers:", odd)

# # nums = list(map(int, input().split()))

# # result = ["Even" if x % 2 == 0 else "Odd" for x in nums]

# # print(result)


# num = int(input("Enter a number: "))

# result = "Even" if num % 2 == 0 else "Odd"
# print(result)


# num = int(input("Enter a number: "))

# result = ["Even" if x % 2 == 0 else "Odd" for x in [num]]
# print(result[0])


# nums = list(map(int, input().split()))

# result = ["Even" if x % 2 == 0 else "Odd" for x in nums]
# print(result)

num = int(input("Enter the number: "))

result = ["Odd number" if x % 2 != 0 else "Even number" for x in [num]]
print(result[0])