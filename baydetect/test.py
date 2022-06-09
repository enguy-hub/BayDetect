import json


input_json="C:/Users/HiEN/Documents/BayDetect/example/metadata/Example_Forest/EF_JSON/EF_MegaDetected/EF_001_20201104_MD.json"

usr_input_json = input_json.replace("\\", "/")

input_json = open(usr_input_json, 'r')
json_info = json.load(input_json)

for i in range(len(list(json_info['images']))):
    imageName = list(json_info['images'][i].values())[0].split('/')[-1]
    session = list(json_info['images'][i].values())[0].split('/')[-2]
    station = list(json_info['images'][i].values())[0].split('/')[-3]

    print(session)
    print(station)

