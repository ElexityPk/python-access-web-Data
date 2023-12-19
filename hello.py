import re

text = "Hello, this is a sample 567 text with numbers 12345 and s 8890 ymbols !@#$"

# Search for digits in the text
matches = re.findall(r'\d', text)
print("Digits found:", matches)

# Replace symbols with spaces
new_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
print("New text without symbols:", new_text)
new = new_text.split()
print(new)





print("Hey its Abdul Wahab, And this is my first python script!")

