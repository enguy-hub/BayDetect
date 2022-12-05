"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        # 'python main.py < '
        # 'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess1/pf4_sortImages_KW_056_Session_3_26032022.txt '
        # '&& '
        # 'python main.py < '
        # 'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess1/pf4_sortImages_KW_056_Session_4_05102022.txt '
        # '&& '
        # 'python main.py < '
        # 'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess1/pf4_sortImages_KW_058_Session_3_06102022.txt '
        # '&& '
        # 'python main.py < '
        # 'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess1/pf4_sortImages_KW_064_Session_4_12102022.txt '
        # '&& '
        # 'python main.py < '
        # 'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess1/pf4_sortImages_KW_070_Session_4_07102022.txt '
        # '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess1/pf4_sortImages_KW_114_Session_2_05102022.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        'cd cameratraps/detection '
        '&& '
        # Insert new python commands below this line

        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_BatchInput_StartRandom/KW_014_Session_4_12102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_MegaDetected_StartRandom/KW_014_Session_4_12102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_BatchInput_StartRandom/KW_014_Session_5_12052022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_MegaDetected_StartRandom/KW_014_Session_5_12052022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_BatchInput_StartRandom/KW_014_Session_6_09102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_MegaDetected_StartRandom/KW_014_Session_6_09102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_BatchInput_StartRandom/KW_036_Session_10_12052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_MegaDetected_StartRandom/KW_036_Session_10_12052021_MD.json '

    )
    return print('Finished !!')


if __name__ == '__main__':

    intro_choice = input("Enter '1' to execute pf_batchrun() function \n"
                         "Enter '2' to execute md_batchrun() function \n"
                         "\n"
                         "Enter your choice here: ")

    intro_choice = int(intro_choice)

    if intro_choice == 1:
        print("\n'1' Selected! Batch-running processing function ..."
              "\n")
        pf_batchrun()

    elif intro_choice == 2:
        print("\n'2' Selected! Batch-running MegaDetector classification ..."
              "\n")
        md_batchrun()

    else:
        print("\nWrong choice, please re-run the script and follow the instructions !!!"
              "\n")
