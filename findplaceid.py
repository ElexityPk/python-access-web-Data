import urllib.request
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    location = input('Enter location: ')
    if len(location) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': location})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except json.JSONDecodeError as e:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place_id = js['results'][0]['place_id']
    print('Place ID:', place_id)
    break
