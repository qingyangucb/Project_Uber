import Set_SF_Addresses
import json
import pprint
import os
from pymongo import MongoClient
import pprint

path = os.path.join('..', 'Data', 'san_francisco_censustracts.json')
with open(path) as json_file:
    data = json.load(json_file)

features = data['features']

id_list = []
SF_Features = []
for address in Set_SF_Addresses.SF_Addresses:
	for i in range(len(features)):
		if features[i]['properties']['DISPLAY_NAME'] == address:
			SF_Features.append(features[i])
			id_list.append(int(features[i]['properties']['MOVEMENT_ID']))

SF_dict = {}
for i in range(len(id_list)):
	SF_dict[Set_SF_Addresses.SF_Addresses[i]] = id_list[i]

with open('../Data/SF_Dict.json', 'w') as f:
    json.dump(SF_dict, f)

with open('../Data/SF_Features.json', 'w') as f:
    json.dump(SF_Features, f)

with open('../Data/SF_ID.json', 'w') as f:
    json.dump(id_list, f)


# print(len(SF_dict))
# print(len(SF_Features))
print(id_list)