import os
import json
import pandas as pd


if __name__ == '__main__':

    # usr_input_json = "C:\LWF\BayDetect\metadata\Karwendel_Rohdaten\KW_JSON\KW_MegaDetected\KW_MegaDetected_StartSess9/"
    #
    # usr_input_json = usr_input_json.replace("\\", "/")
    #
    # jsonList = []
    #
    # for ijson in os.listdir(usr_input_json):
    #     jsonPaths = os.path.join(usr_input_json, ijson)
    #     jsonList.append(jsonPaths)
    # jsonList.sort()
    #
    # exampleJSON = str(jsonList[0])
    # input_json = open(exampleJSON, 'r')
    # json_info = json.load(input_json)
    #
    # sampleImagePath = list(json_info['images'][0].values())[0]
    # print(sampleImagePath)

    # ----------------------------------------------------------------------------------

    usr_csv = "C:\LWF\BayDetect\metadata\Karwendel_Rohdaten\KW_CSV\KW_Metadata_StartSess9"

    csvList = []

    for iCSV in os.listdir(usr_csv):
        csvPaths = os.path.join(usr_csv, iCSV)
        csvList.append(csvPaths)
    csvList.sort()

    exampleCSV = str(csvList[0])
    print(exampleCSV)

    csv_file = pd.read_csv(exampleCSV)
    df_csv = pd.DataFrame(csv_file)

    sampleImagePath = df_csv['Image Path'].iloc[0]
    print(sampleImagePath)
