import requests

base_url = 'https://dobrain-pro.firebaseio.com/drag_data/iOS/'

target_url = base_url + '000123DB-6507-424D-86A2-770DB247D396.json'

print (target_url)

resp = requests.get(url=target_url)

print(resp)

data = resp.json()

print(data)