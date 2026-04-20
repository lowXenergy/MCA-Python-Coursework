import re

# Simple email checker
def check_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w{2,}$'
    return re.match(pattern, email)

# List with mix of valid + invalid emails
emails = [
    # Valid
    "user@gmail.com",
    "john.doe@yahoo.com",
    "alice123@outlook.com",
    "name@company.org",
    "user_name@test.co.in",
    "hello.world@gmail.com",

    # Invalid
    "RR",
    "nogmail.com",
    "user@domain",
    "user@.com",
    "user@@gmail.com",
    ".test@gmail.com",
    "user gmail.com",
    "user@domain.c"
]

print("\n=== Email Checker ===\n")

valid = []
invalid = []

# Process emails
for e in emails:
    if check_email(e):
        valid.append(e)
    else:
        invalid.append(e)

# Print valid emails
print("Valid Emails:")
for v in valid:
    print(" ", v)

# Print invalid emails
print("\nInvalid Emails:")
for i in invalid:
    print(" ", i)

# Summary
print("\nTotal Emails:", len(emails))
print("Valid:", len(valid))
print("Invalid:", len(invalid))