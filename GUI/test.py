import json

jsonFilePath = "C:/Hien/Garden/MyGithub/BayDetect/example/metadata/Example_Forest/EF_JSON/EF_MegaDetected/EF_001_20201104_MD.json"

input_json = open(jsonFilePath, 'r')
json_info = json.load(input_json)

for i in range(len(list(json_info['images']))):

    imageName = list(json_info['images'][i].values())[0].split('/')[-1]
    session = list(json_info['images'][i].values())[0].split('/')[-2]
    station = list(json_info['images'][i].values())[0].split('/')[-3]

    print(imageName)
    print(session)
    print(station)
