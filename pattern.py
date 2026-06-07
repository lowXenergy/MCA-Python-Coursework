import re
# import requests 

# Step 1: Read data from a file OR from internet

# OPTION A: Read from local file
with open("data.txt", "r") as file:
    text = file.read()

# OPTION B: Read from URL (Google or any raw text site)
# url = "https://example.com/sample.txt"
# response = requests.get(url)
# text = response.text


# Step 2: Define Regex Patterns

# Email pattern
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Phone number pattern (supports multiple formats)
phone_pattern = r'(\+91[-\s]?|0)?[6-9]\d{9}|\(?\d{3,4}\)?[-\s]?\d{6,8}'


# Step 3: Find matches

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)


# Step 4: Display results

print("Emails Found:")
for email in emails:
    print(email)

print("\nPhone Numbers Found:")
for phone in phones:
    print(phone)



# import re
# import requests

# # Public raw text file (GitHub raw content or any open dataset)
# url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

# response = requests.get(url)
# text = response.text

# # Example patterns (for demo, since this file has no emails)
# email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# phone_pattern = r'(\+91[-\s]?|0)?[6-9]\d{9}'

# emails = re.findall(email_pattern, text)
# phones = re.findall(phone_pattern, text)

# print("Emails:", emails[:5])
# print("Phones:", phones[:5])