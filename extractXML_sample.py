import urllib.request
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_1940869.xml"

response = urllib.request.urlopen(url)
xml_data = response.read()

tree = ET.fromstring(xml_data)

counts = tree.findall('.//count')

total_count = sum(int(count.text) for count in counts)

print("Total sum of comment counts: ", total_count)