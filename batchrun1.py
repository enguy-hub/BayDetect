"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Jakelberg/JA_BatchCmds/pf4_sortImages/pf4_sortImages_JA_018_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_06_05_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_08_03_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_08_05_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_09_04_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_09_04_Session_1_18102022_101_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_09_04_Session_1_18102022_102_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_10_04_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_10_05_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_10_06_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_10_07_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_10_08_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_Z_01_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_Z_02_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_Z_03_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Wetterstein/WS_BatchCmds/pf4_sortImages/pf4_sortImages_73_Z_04_Session_1_18102022_100_BTCF.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        # Insert new python commands below these two lines:
        'cd cameratraps/detection '
        '&& '
        
        # Below here:      
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_06_05_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_06_05_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_08_03_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_08_03_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_08_05_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_08_05_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_09_04_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_09_04_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_09_04_101_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_09_04_101_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_09_04_Session_1_18102022_102_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_09_04_Session_1_18102022_102_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_10_04_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_10_04_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_10_05_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_10_05_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_10_06_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_10_06_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_10_07_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_10_07_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_10_08_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_10_08_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_Z_01_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_Z_01_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_Z_02_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_Z_02_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_Z_03_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_Z_03_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_BatchInput/73_Z_04_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Wetterstein/WS_JSON/WS_MegaDetected/73_Z_04_100_BTCF_MD.json '

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
