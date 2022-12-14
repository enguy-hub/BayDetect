"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_004_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_004_101_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_004_102_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_016_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_016_101_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_019_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_019_101_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf1_createBIJSON/pf1_createBIJSON_JA_019_102_BTCF.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        'cd cameratraps/detection '
        '&& '
        # Insert new python commands below this line
                
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_BatchInput/JA_011_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_MegaDetected/JA_011_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_BatchInput/JA_013_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_MegaDetected/JA_013_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_BatchInput/JA_014_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_MegaDetected/JA_014_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_BatchInput/JA_017_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Jakelberg/JA_JSON/JA2_MegaDetected/JA_017_100_BTCF_MD.json '

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
