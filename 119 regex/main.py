import re

# Open and read file
with open("data.txt", "r") as file:
    data = file.read()

# Regex pattern for emails
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Regex pattern for phone numbers
phone_pattern = r'\b[6-9]\d{9}\b'

# Extract emails
emails = re.findall(email_pattern, data)

# Extract phone numbers
phones = re.findall(phone_pattern, data)

# Print results
print("Emails Found:")
for email in emails:
    print(email)

print("\nPhone Numbers Found:")
for phone in phones:
    print(phone)