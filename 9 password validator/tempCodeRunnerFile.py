password = input("Enter password: ")

special_chars = "@$!%*?&"

is_valid = (
    len(password) >= 8 and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in special_chars for c in password)
)

print("Valid password" if is_valid else "Invalid password")