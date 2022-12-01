"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_004_Session_9_13052021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_009_Session_10_13102021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_009_Session_11_13022022.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_009_Session_12_06102022.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_009_Session_9_12052021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_011_Session_10_05102021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_011_Session_11_30052022.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_011_Session_12_08102022.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_011_Session_9_13052021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_020_Session_10_07102021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_020_Session_11_01042022.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_020_Session_12_10102022.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/BatchRun_sv47/pf4_sortImages_StartSess9/pf4_sortImages_KW_020_Session_9_13052021.txt '

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
