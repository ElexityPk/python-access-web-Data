import requests

url = 'http://data.pr4e.org/intro-short.txt'
response = requests.head(url)
print(response.headers)