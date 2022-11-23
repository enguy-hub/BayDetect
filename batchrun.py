"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/BayDetect/metadata/KW_BatchCmds/pf4_sortImages/pf4_sortImages_KW_001_Session_6_02052021.txt '
        '&& '
        'python main.py < '
        'C:/BayDetect/metadata/KW_BatchCmds/pf4_sortImages/pf4_sortImages_KW_002_Session_6_07052021.txt '
        '&& '
        'python main.py < '
        'C:/BayDetect/metadata/KW_BatchCmds/pf4_sortImages/pf4_sortImages_KW_013_Session_6_11052021.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        'cd cameratraps/detection '
        '&& '
        # Insert new python commands below this line
                                                                                        
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_032_Session_11_12102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_032_Session_11_12102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_032_Session_8_11052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_032_Session_8_11052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_032_Session_9_08102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_032_Session_9_08102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_037_Session_10_17052022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_037_Session_10_17052022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_037_Session_11_06102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_037_Session_11_06102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_037_Session_8_12052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_037_Session_8_12052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_037_Session_9_07102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_037_Session_9_07102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_049_Session_10_24052022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_049_Session_10_24052022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_049_Session_11_06102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_049_Session_11_06102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_049_Session_8_12052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_049_Session_8_12052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput_StartSess8/KW_049_Session_9_06102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected_StartSess8/KW_049_Session_9_06102021_MD.json '

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
