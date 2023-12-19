import urllib.request
import json

url = input("Enter URL: ")
response = urllib.request.urlopen(url)
data = response.read().decode()

jsonData = json.loads(data)

commentCounts = [item['count'] for item in jsonData['comments']]


totalComments = sum(commentCounts)

print("Total sum of comment counts:", totalComments)