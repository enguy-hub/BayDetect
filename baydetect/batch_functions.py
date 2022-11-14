"""This module contains functions that create commands needed to execute `batchrun.py` script."""

import os
import fnmatch
from pathlib import Path

""" Brief description of what each function does """
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#bf1 | pf1_txtcmds_creator(): function to create multiple '.txt' files containing the input commands needed to 
'batch-run' one of the Process function

#bf2 | pf_pycmds_creator(): function to create a '.txt' file containing the python commands needed to start 
`pf_batchrun()` function from `batchrun.py`

#bf3 | md_pycmds_creator(): function to create a '.txt' file containing the python commands needed to start 
`md_batchrun()` function from `batchrun.py`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


# ID: bf1 || pf_txtcmds_creator()
def pf_txtcmds_creator():
    # Input commands for all
    org_img_dir_input = input("Enter the absolute path to the the `top-level folder`, in which all the "
                              "\nimages are being stored inside sub-folders under this `top-level folder`: ")

    common_dirname_input = input("What is the common pattern in the names of the folders where all "
                                 "the image are stored in (eg: `2020*`, ``Session*` or `100CU*`): ")

    second_common_dirname = input("Is there a second common pattern in the names for the sub-folders "
                                  "of above-mentioned folders? (answer with `Y` or `N`): ")

    # org_img_dir_input = org_img_dir_input + "/"

    # Lists for all
    org_img_dirpath = []
    pattern1_list = []
    pattern2_list = []

    img_folderpaths = []
    dataset_station = []
    station = []
    session = []

    dataset = str

    if second_common_dirname == 'N':
        for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
            for dirname in fnmatch.filter(dirs, common_dirname_input):
                org_img_dirpath.append(os.path.join(path, dirname).replace("\\", "/"))

    elif second_common_dirname == 'Y':
        common_dirname_extra = input("What is the second common pattern in the names of the "
                                     "sub-folders? (eg: `2020*`, ``Session*` or `100CU*`): ")

        for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
            for dirname_p1 in fnmatch.filter(dirs, common_dirname_input):
                pattern1_list.append(os.path.join(path, dirname_p1).replace("\\", "/"))

        for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
            for dirname_p2 in fnmatch.filter(dirs, common_dirname_extra):
                pattern2_list.append(dirname_p2)

        for ip1, ip2 in zip(pattern1_list, pattern2_list):
            org_img_dirpath.append(os.path.join(ip1, ip2).replace("\\", "/"))

    print("\nSAMPLE FOLDER-PATH WHERE IMAGES ARE STORED IN: \n" + org_img_dirpath[0].split()[-1] + "/" + "\n")

    input_session = input("Which index order is the `SESSION NAME` located when the "
                          "\nabove FOLDER-PATH string is split with `/` as separator? ")

    input_session = int(input_session)

    input_dataset_station = input("Which index order is the `STATION NAME` located when the "
                                  "\nabove FOLDER-PATH string is split with `/` as separator? ")

    input_dataset_station = int(input_dataset_station)

    for idirpaths in org_img_dirpath:
        for dirpath, dirnames, files in os.walk(idirpaths):
            if files:
                img_folderpaths.append(''.join(idirpaths.split()[-1]))
                session.append(''.join(idirpaths.split('/')[input_session]))
                dataset_station.append(''.join(idirpaths.split('/')[input_dataset_station]))
            if not files:
                pass

    for name in dataset_station:
        dataset = ''.join(name.split('_')[0])
        station.append('_'.join(name.split('_')[1:]))

    txtcmds_choice = input("Which `processing function` would you like to create "
                           "the 'pf*.txt' files for? (answer with `1`, `2`, or `3`) ")
    txtcmds_choice = int(txtcmds_choice)

    if txtcmds_choice == 1:
        print("\n'1' Selected ! Follow the prompted questions to create "
              "the '.txt' files for processing function `1` !!\n")

        input_BI_json_dir = input("Enter the absolute path of the directory where you want "
                                  "all the '*_BatchInput.json' files to be saved at: ")

        input_txtcmds_dir = input("Enter the absolute path of the directory where you "
                                  "want all the 'pf1_*.txt' files to be saved at: ")

        jsonInputDir = input_BI_json_dir.replace("\\", "/") + "/"
        txtcmds_dir_input = input_txtcmds_dir.replace("\\", "/") + "/"

        for ista, isess, ipaths in zip(station, session, img_folderpaths):
            create = open(f"{txtcmds_dir_input}pf1_createBIJSON_{dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}{dataset}_{ista}_{isess}_BI.json\n")
            create.close()

    elif txtcmds_choice == 2:
        print("\n'2' Selected ! Follow the prompted questions to create "
              "the '.txt' files for processing function `3` !!\n")

        sampleImgPath = []

        for dirpath, dirnames, filenames in os.walk(img_folderpaths[0]):
            print(filenames)
            for ifilenames in filenames:
                sampleImgPath.append(os.path.join(dirpath, ifilenames))

        samplePath = sampleImgPath[0].replace("\\", "/")
        print("\nSample IMAGE-PATH to the very first image: \n" + samplePath)

        input_sessionIndex = input("\nWhich index order is the `SESSION NAME` located when the "
                                   "above sample IMAGE-PATH is split with `/` as separator? ")
        input_sessionIndex = int(input_sessionIndex)

        input_stationIndex = input("Which index order is the `STATION NAME` located when the "
                                   "above sample IMAGE-PATH string is split with `/` as separator? ")
        input_stationIndex = int(input_stationIndex)

        md_json_fullpaths = []
        md_json_withMD = []
        csv_woMeta = []

        input_MD_json_dir = input("Enter the absolute path of the directory where all "
                                  "the '*_MD.json' files are currently saved at: ")

        input_csv_dir = input("Enter the absolute path of the directory where you "
                              "want all the '*_Meta.csv' files to be saved at: ")

        input_txtcmds_dir = input("Enter the absolute path of the directory where "
                                  "you want all the '.txt' files to be saved at: ")

        MD_json_dir_input = input_MD_json_dir.replace("\\", "/") + "/"
        csv_dir_input = input_csv_dir.replace("\\", "/") + "/"
        txtcmds_dir_input = input_txtcmds_dir.replace("\\", "/") + "/"

        for dirpath, dirnames, filenames in os.walk(MD_json_dir_input):
            for ifilenames in filenames:
                md_json_fullpaths.append(os.path.join(dirpath, ifilenames))
                json_names, extension = os.path.splitext(ifilenames)
                md_json_withMD.append(json_names)

        print("\nMegaDetected JSON filenames WITHOUT `.json`: ")
        print(md_json_withMD)

        for iname in md_json_withMD:
            icsv_names = '_'.join(iname.split('_')[0:5])
            csv_woMeta.append(icsv_names)

        print("\nPaths to IMAGE FOLDERS contains Images: ")
        print(img_folderpaths)

        print("\nPaths to MegaDetected JSON files: ")
        print(md_json_fullpaths)

        print("\nFirst part of CSV filenames: ")
        print(csv_woMeta)

        # Sort the two lists so they are in ordered
        md_json_fullpaths.sort()
        csv_woMeta.sort()

        for ista, isess, iorg_idirpath, imd_json_paths, icsv_woMeta in zip(station, session, img_folderpaths,
                                                                           md_json_fullpaths, csv_woMeta):
            create = open(f"{txtcmds_dir_input}pf3_mdJSONToCSV_{dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"2\n"
                         f"{iorg_idirpath}/\n"
                         f"{imd_json_paths}\n"
                         f"{csv_dir_input}{icsv_woMeta}_Meta.csv\n"
                         f"{input_sessionIndex}\n"
                         f"{input_stationIndex}\n")
            create.close()

    elif txtcmds_choice == 3:
        print("\n'3' Selected ! Follow the prompted questions to create the '.txt' files for processing function `3` !!"
              "\n")

        input_CSV_dir = input("Enter the absolute path to the directory where all "
                              "the '*_Meta.csv' files are currently saved at: ")

        sorted_input = input("Would you like the 'sorted images' to be saved in a separate sub-folder called "
                             "`*_Sorted`, located inside where the directory of the `original images`? "
                             "(answer with 'Y' or 'N') ")

        input_txtcmds_dir = input("Enter the absolute path of the directory where "
                                  "you want all the '.txt' files to be saved at: ")

        CSV_dir_input = input_CSV_dir.replace("\\", "/") + "/"
        txtcmds_dir_input = input_txtcmds_dir.replace("\\", "/") + "/"

        CSV_paths = []

        for dirpath, dirnames, filenames in os.walk(CSV_dir_input):
            for ifilenames in filenames:
                CSV_paths.append(os.path.join(dirpath, ifilenames))

        # Sort the two lists so they are in ordered
        img_folderpaths.sort()
        CSV_paths.sort()

        for ista, isess, iorg_dirpath, icsv in zip(station, session, img_folderpaths, CSV_paths):
            create = open(f"{txtcmds_dir_input}pf4_sortImages_{dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"3\n"
                         f"{iorg_dirpath}/\n"
                         f"{icsv}\n"
                         f"{sorted_input}\n")
            create.close()

    else:
        print("\nWrong choice, please re-run the script and follow the instructions !!!"
              "\n")

    return print('\n Done !!! \n')


# ID: bf2 || pf_pycmds_creator
def pf_pycmds_creator():
    input_path_txtcmd_dir = input("Enter the absolute path of the folder where "
                                  "all the '.txt' files are currently saved at: ")

    path_txtcmd_dir = input_path_txtcmd_dir.replace("\\", "/") + "/"

    output_txtfile_dir = "/".join(list(path_txtcmd_dir.split('/')[:-2])) + "/"

    for (dirpath, dirnames, filenames) in os.walk(path_txtcmd_dir):

        txtcmd_dir_name = ''.join(dirpath.split('/')[-2])
        chosenFunction = ''.join(txtcmd_dir_name.split('_')[1])

        for ifilenames in filenames:
            fullpaths = Path(os.path.join(dirpath, ifilenames))
            new_fullpath = str(fullpaths).replace("\\", "/")

            f = open(f"{output_txtfile_dir}pf{chosenFunction}_combinedCmds.txt", "a")
            f.write(f"'python main.py < '\n'{new_fullpath} '\n"
                    f"'&& '\n")
            f.close()

    return print('\n Done !!! \n')


# ID: bf3 || md_pycmds_creator()
def md_pycmds_creator():
    input_bijson_dir = input("Enter the absolute path of the 'BatchInput' JSON directory: ")

    input_mdjson_dir = input("Enter the absolute path for the output 'MegaDetected' JSON directory: ")

    input_output_txtdir = input("Enter the absolute path for the `.txt` file: ")

    bijson_dir_input = input_bijson_dir.replace("\\", "/") + "/"
    mdjson_dir_input = input_mdjson_dir.replace("\\", "/") + "/"
    output_txtdir = input_output_txtdir.replace("\\", "/") + "/"

    md_dirpath = None

    for dirpath, dirnames, filenames in os.walk(mdjson_dir_input):
        md_dirpath = dirpath.split("BayDetect")[1].replace("\\", "/")

    for dirpath, dirnames, filenames in os.walk(bijson_dir_input):
        bi_dirpath = dirpath.split("BayDetect")[1].replace("\\", "/")

        for ifilenames in range(len(filenames)):
            fullnames = filenames[ifilenames]
            names_withBI, extension = os.path.splitext(fullnames)
            name_withoutBI = '_'.join(names_withBI.split('_')[:-1])

            with open(output_txtdir + "startSess1_pf2_runMD_cmds.txt", "a") as f:
                f.write(f"'python run_detector_batch.py md_v5a.0.0.pt ' \n"
                        f"'../..{bi_dirpath}{names_withBI}.json ' \n"
                        f"'../..{md_dirpath}{name_withoutBI}_MD.json ' \n"
                        f"'&& '\n")

    return print('\nDone !!! \n')

# if __name__ == '__main__':
