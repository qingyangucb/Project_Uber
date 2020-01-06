import json
import pprint
import os
from pymongo import MongoClient
import pprint

path = os.path.join('..', 'Data', 'san_francisco_censustracts.json')
with open(path) as json_file:
    data = json.load(json_file)

features = data['features']

client = MongoClient('localhost', 27017)
db = client['map_tile']
db.bay_area.drop()
bay_area = db['bay_area']
bay_area.insert_many(features)
# type(bay_area)

def find_id(address):
	x = db.bay_area.find({'properties.DISPLAY_NAME':f'{address}'})
	return (x[0]['properties']['MOVEMENT_ID'])

# print(find_id('500 20th Street, Downtown Oakland, Oakland'))
# x = db.bay_area.find({'properties.DISPLAY_NAME':'Sargent Creek, San Ardo'})
# print(x[0]['properties']['MOVEMENT_ID'])