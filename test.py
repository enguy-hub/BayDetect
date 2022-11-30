import os
import json
import pandas as pd


if __name__ == '__main__':

    # usr_input_json = "C:\Garden\MyGithub\BayDetect\metadata\KW_MegaDetected_StartSess6" + "/"
    # usr_input_json = usr_input_json.replace("\\", "/")
    #
    # csv_input = "C:\Garden\MyGithub\BayDetect\metadata\CSV_test" + "/"
    # csv_input = csv_input.replace("\\", "/")
    #
    # txt_input = "C:\Garden\MyGithub\BayDetect\metadata\Batch_test" + "/"
    # txt_input = txt_input.replace("\\", "/")
    #
    # # exampleJSON = str(jsonList[0])
    # # input_json = open(exampleJSON, 'r')
    # # json_info = json.load(input_json)
    #
    # # sampleImagePath = list(json_info['images'][0].values())[0]
    # # print(sampleImagePath)
    #
    # org_img_dirpath = []
    # img_folderpaths = []
    # session = []
    # dataset_station = []
    # station = []
    # dataset = str
    #
    # jsonSet = set()
    # imgDirSet = set()
    #
    # for ijson in os.listdir(usr_input_json):
    #     jsonPaths = os.path.join(usr_input_json, ijson)
    #     jsonSet.add(jsonPaths)
    # print(len(jsonSet))
    #
    # for j in jsonSet:
    #     openJSON = open(j, 'r')
    #     infoJSON = json.load(openJSON)
    #     # print(len(list(infoJSON['images'])))
    #     for i in range(len(list(infoJSON['images']))):
    #         imagePath = list(infoJSON['images'][i].values())[0]
    #         print(imagePath)
    #         imgDir = os.path.dirname(imagePath)
    #         imgDirSet.add(imgDir)
    #
    # org_img_dirpath = list(imgDirSet)
    # org_img_dirpath.sort()
    # print("\nList of all the image folders found from `MegaDetected` JSON files:")
    # print(org_img_dirpath)
    #
    # for idirpaths in org_img_dirpath:
    #     for dirpath, dirnames, files in os.walk(idirpaths):
    #         if files:
    #             img_folderpaths.append(''.join(idirpaths.split()[-1]))
    #             session.append(''.join(idirpaths.split('/')[-2]))
    #             dataset_station.append(''.join(idirpaths.split('/')[-3]))
    #         if not files:
    #             break
    #
    # for name in dataset_station:
    #     dataset = ''.join(name.split('_')[0])
    #     station.append('_'.join(name.split('_')[1:]))
    #
    # # Sort all the sets
    # img_folderpaths.sort()
    # # session.sort()
    # # station.sort()
    # # dataset_station.sort()
    #
    # print("\nList of all the image folders on the machine matched the ones on the list above: ")
    # print(img_folderpaths)
    #
    # print("\nDataset name: " + dataset)
    #
    # print("\nList of available stations from image folders: ")
    # print(dataset_station)
    #
    # print("\nList of available sessions from image folders: ")
    # print(session)
    #
    # station_session = [a + '_' + b for a, b in zip(dataset_station, session)]
    # print("\nList of sessions from image folders on the machine for cross-checking later: ")
    # print(station_session)
    #
    # # mdJSONDir = mdJSONDirPath
    # # csvDir = outputCSVDirPath
    # # txtOutputDir = outputTxtDirPath
    # input_iSessionIndex = int(-3)
    # input_iStationIndex = int(-4)
    #
    # md_withoutExt = []
    # iname_list = []
    #
    # for dirpath, dirnames, filenames in os.walk(usr_input_json):
    #     for ifilenames in filenames:
    #         fname, extension = os.path.splitext(ifilenames)
    #         md_withoutExt.append(fname)
    #
    # for inameNoExt in md_withoutExt:
    #     inameRaw = '_'.join(inameNoExt.split('_')[0:5])
    #     iname_list.append(inameRaw)
    #
    # # Sort the two lists in ordered
    # iname_list.sort()
    #
    # print("\nList of `MD` JSON files currently in the `MD` folder: ")
    # print(iname_list)
    #
    # print("\nList of sessions matched between image folders and JSON files in `MD` folder:")
    # matchNames_list = list(set(station_session).intersection(iname_list))
    # matchNames_list.sort()
    # print(matchNames_list)
    #
    # for ista, isess, iorg_dirpath, imatch_name in zip(station, session, img_folderpaths,
    #                                                   matchNames_list):
    #     create = open(f"{txt_input}pf3_mdJSONToCSV_{dataset}_{ista}_{isess}.txt", "a")
    #     create.write(f"1\n"
    #                  f"2\n"
    #                  f"{usr_input_json}{imatch_name}_MD.json\n"
    #                  f"{csv_input}{imatch_name}_Meta.csv\n"
    #                  f"{input_iSessionIndex}\n"
    #                  f"{input_iStationIndex}")
    #     create.close()

    # ----------------------------------------------------------------------------------

    csv_input = "C:\Garden\MyGithub\BayDetect\metadata\KW_Metadata_StartSess6" + "/"
    csv_input = csv_input.replace("\\", "/")

    txt_input = "C:\Garden\MyGithub\BayDetect\metadata\Batch_test" + "/"
    txt_input = txt_input.replace("\\", "/")

    org_img_dirpath = []
    img_folderpaths = []
    session = []
    dataset_station = []
    station = []
    dataset = str

    csvSet = set()
    imgDirSet = set()

    # for iCSV in os.listdir(csv_input):
    #     jsonPaths = os.path.join(usr_input_json, ijson)
    #     jsonSet.add(jsonPaths)
    # print(jsonSet)

    for iCSV in os.listdir(csv_input):
        csvPaths = os.path.join(csv_input, iCSV)
        csvSet.add(csvPaths)
    print(csvSet)

    for c in csvSet:
        csv_file = pd.read_csv(c)
        df_csv = pd.DataFrame(csv_file)
        print(len(list(df_csv['Image Path'])))
        for i in range(len(list(df_csv['Image Path']))):
            imagePath = list(df_csv['Image Path'])[i]
            # print(imagePath)
            imgDir = os.path.dirname(imagePath)
            imgDirSet.add(imgDir)

    org_img_dirpath = list(imgDirSet)
    org_img_dirpath.sort()
    print("\nList of all the image folders found from CSV `Metadata` files:")
    print(org_img_dirpath)

    for idirpaths in org_img_dirpath:
        for dirpath, dirnames, files in os.walk(idirpaths):
            if files:
                img_folderpaths.append(''.join(idirpaths.split()[-1]))
                session.append(''.join(idirpaths.split('/')[-2]))
                dataset_station.append(''.join(idirpaths.split('/')[-3]))
            if not files:
                break

    for name in dataset_station:
        dataset = ''.join(name.split('_')[0])
        station.append('_'.join(name.split('_')[1:]))

    # Sort all the sets
    img_folderpaths.sort()
    # session.sort()
    # station.sort()
    # dataset_station.sort()

    print("\nList of all the image folders available on the machine that matched the ones on the list above: ")
    print(img_folderpaths)

    print("\nDataset name: " + dataset)

    print("\nList of available stations from image folders: ")
    print(dataset_station)

    print("\nList of available sessions from image folders: ")
    print(session)

    station_session = [a + '_' + b for a, b in zip(dataset_station, session)]
    print("\nList of sessions from image folders on the machine for cross-checking later: ")
    print(station_session)

    sortedInput = "N"
    input_iSessionIndex = int(-3)
    input_iStationIndex = int(-4)

    csv_withoutExt = []
    iname_list = []

    for dirpath, dirnames, filenames in os.walk(csv_input):
        for ifilenames in filenames:
            fname, extension = os.path.splitext(ifilenames)
            csv_withoutExt.append(fname)

    for inameNoExt in csv_withoutExt:
        inameRaw = '_'.join(inameNoExt.split('_')[0:5])
        iname_list.append(inameRaw)

    # Sort the two lists in ordered
    iname_list.sort()

    print("\nList of CSV files currently in the `Metadata` folder: ")
    print(iname_list)

    print("\nList of sessions matched between image folders and JSON files in `MD` folder:")
    matchNames_list = list(set(station_session).intersection(iname_list))
    matchNames_list.sort()
    print(matchNames_list)

    for ista, isess, iorg_dirpath, iname in zip(station, session, img_folderpaths, matchNames_list):
        create = open(f"{txt_input}pf4_sortImages_{dataset}_{ista}_{isess}.txt", "a")
        create.write(f"1\n"
                     f"3\n"
                     f"{iorg_dirpath}/\n"
                     f"{csv_input}{iname}_Meta.csv\n"
                     f"{sortedInput}\n")
        create.close()