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
    org_img_dir_input = input("Enter the absolute path to the `parent-folder` where all the `station folders` are "
                              "located in. In this `parent-folder` the images are being stored in sub-folders inside "
                              "each `station-folder` (end with `/`): ")

    common_dirname_input = input("What is the common pattern in the names of the folders where all "
                                 "the image are stored in (eg: `2020*`, ``Session*` or `100CU*`): ")

    second_common_dirname = input("Is there a second common pattern in the names for the sub-folders "
                                  "of above-mentioned folders? (answer with `Y` or `N`): ")

    # Lists for all
    org_img_dirpath = []
    pattern1_list = []
    pattern2_list = []

    img_paths = []
    dataset_station = []
    dataset = str
    station = []
    session = []

    if second_common_dirname == 'N':
        for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
            for dirname in fnmatch.filter(dirs, common_dirname_input):
                org_img_dirpath.append(os.path.join(path, dirname).replace("\\", "/"))

    elif second_common_dirname == 'Y':
        common_dirname_extra = input("What is the second common pattern in the names of the sub-folders ? "
                                     "(eg: `2020*`, ``Session*` or `100CU*`): ")

        for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
            for dirname_p1 in fnmatch.filter(dirs, common_dirname_input):
                pattern1_list.append(os.path.join(path, dirname_p1).replace("\\", "/"))

        for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
            for dirname_p2 in fnmatch.filter(dirs, common_dirname_extra):
                pattern2_list.append(dirname_p2)

        for ip1, ip2 in zip(pattern1_list, pattern2_list):
            org_img_dirpath.append(os.path.join(ip1, ip2).replace("\\", "/"))

    for idirpaths in org_img_dirpath:
        for dirpath, dirnames, files in os.walk(idirpaths):
            if files:
                img_paths.append(''.join(idirpaths.split()[-1]))
                dataset_station.append(''.join(idirpaths.split('/')[9]))
                session.append(''.join(idirpaths.split('/')[10]))
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
              "the 'pf1_*.txt' files for processing function `1` !!"
              "\n")

        BI_json_dir_input = input("Enter the absolute path of the directory where you want all "
                                  "the '*_BatchInput.json' files to be saved at (end with `/`): ")

        txtcmds_dir_input = input("Enter the absolute path of the directory where you want "
                                  "all the 'pf1_*.txt' files to be saved at (end with `/`): ")

        jsonInputDir = BI_json_dir_input.replace("\\", "/")

        for ista, isess, ipaths in zip(station, session, img_paths):
            create = open(f"{txtcmds_dir_input}pf{txtcmds_choice}_{dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}{dataset}_{ista}_{isess}_BI.json\n")
            create.close()

    elif txtcmds_choice == 2:
        print("\n'2' Selected ! Follow the prompted questions to create "
              "the 'pf2_*.txt' files for processing function `2` !!"
              "\n")

        MD_json_dir_input = input("Enter the absolute path of the directory where all the "
                                  "'*_MegaDetected.json' files are currently saved at (end with `/`): ")

        csv_dir_input = input("Enter the absolute path of the directory where you want "
                              "all the '*_Meta.csv' files to be saved at (end with `/`): ")

        txtcmds_dir_input = input("Enter the absolute path of the directory where you want "
                                  "all the 'pf2_*.txt' files to be saved at (end with `/`): ")

        md_json_paths = []
        md_json_names = []
        csv_woMeta = []

        for (dirpath, dirnames, filenames) in os.walk(MD_json_dir_input):
            for ifilenames in filenames:
                md_json_paths.append(os.path.join(dirpath, ifilenames))

            for ifilenames in range(len(filenames)):
                fullnames = filenames[ifilenames]
                json_names, extension = os.path.splitext(fullnames)
                md_json_names.append(json_names)

        for iname in md_json_names:
            icsv_names = '_'.join(iname.split('_')[0:5])
            csv_woMeta.append(icsv_names)

        for ista, isess, iorg_dirpath, imd_json_paths, icsv_woMeta in zip(station, session, org_img_dirpath,
                                                                          md_json_paths, csv_woMeta):
            create = open(f"{txtcmds_dir_input}pf{txtcmds_choice}_{dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"2\n"
                         f"{iorg_dirpath}/\n"
                         f"{imd_json_paths}\n"
                         f"{csv_dir_input}{icsv_woMeta}_Meta.csv\n")
            create.close()

    elif txtcmds_choice == 3:
        print("\n'3' Selected ! Follow the prompted questions to create the 'pf3_*.txt' files for processing "
              "function `3` !!"
              "\n")

        CSV_dir_input = input("Enter the absolute path to the directory where all the '*_Meta.csv' files are "
                              "currently saved at (end with `/`): ")

        sorted_input = input("Would you like the 'sorted images' to be saved in a separate sub-folder called "
                             "`*_Sorted`, located inside where the directory of the `original images`? "
                             "(answer with 'Y' or 'N') ")

        txtcmds_dir_input = input("Enter the absolute path of the directory where you want all the 'pf3_*.txt' "
                                  "files to be saved at (end with `/`): ")

        CSV_paths = []

        for (dirpath, dirnames, filenames) in os.walk(CSV_dir_input):
            for ifilenames in filenames:
                CSV_paths.append(os.path.join(dirpath, ifilenames))

        for ista, isess, iorg_dirpath, icsv in zip(station, session, org_img_dirpath, CSV_paths):
            create = open(f"{txtcmds_dir_input}pf{txtcmds_choice}_{dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"3\n"
                         f"{iorg_dirpath}/\n"
                         f"{icsv}\n"
                         f"{sorted_input}\n")
            create.close()

    else:
        print("\nWrong choice, please re-run the script and follow the instructions !!!"
              "\n")

    return print('Done!')


# ID: bf2 || pf_pycmds_creator
def pf_pycmds_creator():

    path_txtcmd_dir = input("Enter the absolute path of the folder where all the "
                            "'pf*.txt' files are currently saved at (end with `/`): ")

    output_txtfile_dir = input("Enter the absolute path of the 'parent-folder' "
                               "of the above-entered folder (end with '/'): ")

    path_txtcmd_dir_new = path_txtcmd_dir.replace("\\", "/")

    for (dirpath, dirnames, filenames) in os.walk(path_txtcmd_dir_new):

        txtcmd_dir_name = ''.join(dirpath.split('/')[-2])
        txtcmd_choice = ''.join(txtcmd_dir_name.split())[2]
        dataset_name = ''.join(txtcmd_dir_name.split())[4:6]

        for ifilenames in filenames:
            fullpaths = Path(os.path.join(dirpath, ifilenames))

            f = open(f"{output_txtfile_dir}pf{txtcmd_choice}_{dataset_name}_pycmds.txt", "a")
            f.write(f"'python main.py < '\n'{fullpaths} '\n"
                    f"'&& '\n")
            f.close()

    return print('Done!')


# ID: bf3 || md_pycmds_creator()
def md_pycmds_creator():
    json_dir_input = input("Enter the absolute path of the 'JSON/BatchInput' directory (end with `/`): ")

    output_txtfile = input("Enter the absolute path and name for the python commands `.txt` file "
                           "(end with '*dataset_name*_MD_pycmds.txt'): ")

    for (dirpath, dirnames, filenames) in os.walk(json_dir_input):
        root_path = dirpath.split("BayDetect")[1]
        root_path = root_path.replace("\\", "/")
        path_withoutBI = root_path.split("BatchInput")[0]

        for ifilenames in range(len(filenames)):
            fullnames = filenames[ifilenames]
            names_withBI, extension = os.path.splitext(fullnames)
            name_withoutBI = '_'.join(names_withBI.split('_')[:-1])

            with open(output_txtfile, "a") as f:
                f.write(f"'python run_detector_batch.py md_v4.1.0.pb ' \n"
                        f"'..{root_path}{names_withBI}.json ' \n"
                        f"'..{path_withoutBI}MegaDetected/{name_withoutBI}_MD.json ' \n"
                        f"'&& '\n")

    return print('Done!')


# if __name__ == '__main__':
