password = input("Enter password: ")

special_chars = "@$!%*?&"

is_valid = (
    len(password) >= 8 and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in special_chars for c in password) and
    all(password[i] != password[i+1] for i in range(len(password) - 1))
)

print("Valid password" if is_valid else "Invalid password")