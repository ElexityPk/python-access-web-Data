import urllib.request
import urllib.parse
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    location = input('Enter location: ')
    if len(location) < 1:
        break

    params = {
        'address': location,
        'key': 'AIzaSyA9dR6UeZr9l8DCmuvzat9-Dn9opTYkPgA'  # Replace with your actual API key
    }

    # Encode parameters and construct the URL
    url = serviceurl + urllib.parse.urlencode(params)

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