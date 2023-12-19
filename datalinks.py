import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1  

# Repeat the process 'count' number of times
for _ in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    tags = soup('a')
    print('Retrieving:', url)

    # Navigate to the specified position relative to the first link
    url = tags[position].get('href', None)

# Print the last name found after the iterations
print('Last name found:', tags[position].contents[0])