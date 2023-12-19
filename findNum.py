import re

# Open the text file for reading
with open("sampleText.txt", "r") as file:
    text = file.read()  # Read the entire file content

numbers = re.findall(r"\d+", text)  # Find all sequences of digits

# Convert the list of strings to a list of integers
number_integers = [int(number) for number in numbers]

print(numbers)
print(len(numbers))
print(sum(number_integers))  # Print the sum of the numbers