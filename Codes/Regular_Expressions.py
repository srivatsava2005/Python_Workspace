import re

# Sample text
text = "Contact us at support@example.com or sales@company.org. Call +91-9876543210."

# 1. Find all email addresses
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("Emails found:", emails)

# 2. Find phone numbers (Indian format example)
phone_numbers = re.findall(r'\+91-\d{10}', text)
print("Phone numbers found:", phone_numbers)

# 3. Check if a string starts with a pattern
pattern = r'^Contact'
if re.match(pattern, text):
    print("Text starts with 'Contact'")

# 4. Replace email addresses with a placeholder
masked_text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL HIDDEN]', text)
print("Masked text:", masked_text)

# 5. Split text by spaces using regex
words = re.split(r'\s+', text)
print("Words:", words)
