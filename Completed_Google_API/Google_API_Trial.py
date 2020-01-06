import requests
from config import gkey

params = {'origins':'18 alder road sf ca 94134',
'destinations': '618 ansel street burlingame ca 94010',
'key': gkey,
'units': 'imperial'}

base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'


response = requests.get(base_url, params)


print(response.text)