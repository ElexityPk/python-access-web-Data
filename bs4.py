from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
number_tags = soup.find_all('span')
total_sum = 0
for tag in number_tags:
    try:
        number = int(tag.get_text())  # Extract the number from the tag
        total_sum += number  # Add the number to the total sum
    except ValueError:
        pass  

print("Sum of numbers in the file:", total_sum)