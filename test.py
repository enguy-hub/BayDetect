import os
import json
import pandas as pd
import shutil
import ast


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

    # csv_input = "C:\Garden\MyGithub\BayDetect\metadata\KW_Metadata_StartSess6" + "/"
    # csv_input = csv_input.replace("\\", "/")
    #
    # txt_input = "C:\Garden\MyGithub\BayDetect\metadata\Batch_test" + "/"
    # txt_input = txt_input.replace("\\", "/")
    #
    # org_img_dirpath = []
    # img_folderpaths = []
    # session = []
    # dataset_station = []
    # station = []
    # dataset = str
    #
    # csvSet = set()
    # imgDirSet = set()
    #
    # # for iCSV in os.listdir(csv_input):
    # #     jsonPaths = os.path.join(usr_input_json, ijson)
    # #     jsonSet.add(jsonPaths)
    # # print(jsonSet)
    #
    # for iCSV in os.listdir(csv_input):
    #     csvPaths = os.path.join(csv_input, iCSV)
    #     csvSet.add(csvPaths)
    # print(csvSet)
    #
    # for c in csvSet:
    #     csv_file = pd.read_csv(c)
    #     df_csv = pd.DataFrame(csv_file)
    #     print(len(list(df_csv['Image Path'])))
    #     for i in range(len(list(df_csv['Image Path']))):
    #         imagePath = list(df_csv['Image Path'])[i]
    #         # print(imagePath)
    #         imgDir = os.path.dirname(imagePath)
    #         imgDirSet.add(imgDir)
    #
    # org_img_dirpath = list(imgDirSet)
    # org_img_dirpath.sort()
    # print("\nList of all the image folders found from CSV `Metadata` files:")
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
    # print("\nList of all the image folders available on the machine that matched the ones on the list above: ")
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
    # sortedInput = "N"
    # input_iSessionIndex = int(-3)
    # input_iStationIndex = int(-4)
    #
    # csv_withoutExt = []
    # iname_list = []
    #
    # for dirpath, dirnames, filenames in os.walk(csv_input):
    #     for ifilenames in filenames:
    #         fname, extension = os.path.splitext(ifilenames)
    #         csv_withoutExt.append(fname)
    #
    # for inameNoExt in csv_withoutExt:
    #     inameRaw = '_'.join(inameNoExt.split('_')[0:5])
    #     iname_list.append(inameRaw)
    #
    # # Sort the two lists in ordered
    # iname_list.sort()
    #
    # print("\nList of CSV files currently in the `Metadata` folder: ")
    # print(iname_list)
    #
    # print("\nList of sessions matched between image folders and JSON files in `MD` folder:")
    # matchNames_list = list(set(station_session).intersection(iname_list))
    # matchNames_list.sort()
    # print(matchNames_list)
    #
    # for ista, isess, iorg_dirpath, iname in zip(station, session, img_folderpaths, matchNames_list):
    #     create = open(f"{txt_input}pf4_sortImages_{dataset}_{ista}_{isess}.txt", "a")
    #     create.write(f"1\n"
    #                  f"3\n"
    #                  f"{iorg_dirpath}/\n"
    #                  f"{csv_input}{iname}_Meta.csv\n"
    #                  f"{sortedInput}\n")
    #     create.close()

    # ----------------------------------------------------------------------------------

    # input_img_dir = 'Z:/Wildtier_Monitoring/Karwendel/Bilder/Rohdaten/KW_004/Session_9_13052021/100CUDDY'
    input_img_dir = 'C:/LWF/BayDetect/image_data/Karwendel/Start21Sess9/KW_004/Session_9_13052021/100CUDDY'

    # input_csv_file = 'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_CSV_sv47/StartSess9/KW_004_Session_9_13052021_Meta.csv'
    input_csv_file = 'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_CSV_KIServer/StartSess9/KW_004_Session_9_13052021_Meta.csv'

    sorted_input = "N"

    img_input_dir = input_img_dir.replace("\\", "/") + "/"

    org_imgPath = []  # Old - full original paths of where the image files are currently stored
    org_imgName = []

    ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

    for image_name in os.listdir(img_input_dir):
        imgPath = str(os.path.join(img_input_dir, image_name))
        imgStat = os.stat(imgPath).st_size

        if image_name.endswith(ext) and imgStat == 0:
            print("\nThe following image is broken and not included in the sorting:")
            print(image_name)
            continue
        else:
            org_imgPath.append(imgPath)
            org_imgName.append(image_name)

    org_imgPath.sort()
    org_imgName.sort()

    print("Image paths")
    print(org_imgName)
    print("\n")
    # print(len(org_imgPath))

    parent_imgPath = []  # First half of the o_path (parent path) without the image name

    for p in org_imgPath:
        p_path = os.path.split(p)[0]
        p_path = os.path.normpath(p_path)
        parent_imgPath.append(p_path)

    csv_file = pd.read_csv(input_csv_file)
    df_csv = pd.DataFrame(csv_file)

    classified_folder = []  # Classified categories of each image

    list_numbbs = df_csv['Number of BBs'].tolist()

    list_predcategory = df_csv['Predicted Category'].tolist()
    intList_predcategory = [list(map(int, ast.literal_eval(i))) for i in list_predcategory]
    # print(type(intList_predcategory))
    # print(intList_predcategory)

    predclass = None

    for num_bbs, category in zip(list_numbbs, intList_predcategory):
        # print(category)
        if num_bbs > 1:
            checking = all(element == category[0] for element in category)
            # print(checking)
            if checking:
                # print("All bounding boxes have the same category")
                # print(category)
                if category[0] == 1:
                    predclass = 'Animal'
                elif category[0] == 2:
                    predclass = 'Person'
                elif category[0] == 3:
                    predclass = 'Vehicle'
            else:
                # print("More than one class detected among the bounding boxes --> Assistant required")
                predclass = 'Assistant Required'
        else:
            # print(category)
            if category[0] == 0:
                predclass = 'Empty'
            elif category[0] == 1:
                predclass = 'Animal'
            elif category[0] == 2:
                predclass = 'Person'
            elif category[0] == 3:
                predclass = 'Vehicle'
            else:
                predclass = None
        classified_folder.append(predclass)

    print("Class of each image")
    print(classified_folder)

    parent_imgPath_sorted = []
    new_path = []  # New - new path where the image files will be moved to
    new_path_sorted = []

    for i in parent_imgPath:
        new_parent_path = i + '_Sorted'
        parent_imgPath_sorted.append(new_parent_path)

    # if sorted_input == 'Y':
    #     for ps, ss in zip(parent_imgPath_sorted, classified_folder):
    #         new_img_path_sorted = os.path.join(ps, ss)
    #         new_img_path_sorted = os.path.normpath(new_img_path_sorted)
    #         os.makedirs(new_img_path_sorted, exist_ok=True) if not os.path.exists(new_img_path_sorted) else None
    #         new_path_sorted.append(new_img_path_sorted)
    #
    #     # Make copy of the image and sorted them in categories
    #     for o, ns in zip(org_imgPath, new_path_sorted):
    #         shutil.copy(o, ns)
    #
    if sorted_input == 'N':
        for p, s in zip(parent_imgPath, classified_folder):
            new_img_path = os.path.join(p, s)
            new_img_path = os.path.normpath(new_img_path)
            os.makedirs(new_img_path, exist_ok=True) if not os.path.exists(new_img_path) else None
            new_path.append(new_img_path)

        # Move the images into their sorted categories
        for o, n in zip(org_imgPath, new_path):
            shutil.move(o, n)



