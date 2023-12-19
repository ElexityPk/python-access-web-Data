import json

input_data = '''
[
    {
        "id": "001",
        "x": "2",
        "name": "Abdul"
    },
    {
        "id": "002",
        "x": "3",
        "name": "Wahab"
    }
]
'''

info = json.loads(input_data)

print('User Count: ', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
