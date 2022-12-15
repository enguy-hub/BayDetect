"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_02_12_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_03_12_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_04_13_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_06_09_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_07_09_02_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_07_13_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_08_10_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_08_13_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_10_11_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_10_13_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_11_10_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_11_11_Session_1_18102022_100_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_11_11_Session_1_18102022_101_BTCF.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Project_Hoehengradient/Schrofen/SF_BatchCmds/pf4_sortImages/pf4_sortImages_63_11_11_Session_1_18102022_102_BTCF.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        # Insert new python commands below these two lines:
        'cd cameratraps/detection '
        '&& '
        
        # Below here:      
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_02_12_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_02_12_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_03_12_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_03_12_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_04_13_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_04_13_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_06_09_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_06_09_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_07_09_02_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_07_09_02_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_07_13_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_07_13_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_08_10_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_08_10_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_08_13_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_08_13_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_10_11_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_10_11_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_10_13_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_10_13_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_11_10_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_11_10_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_11_11_100_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_11_11_100_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_11_11_Session_1_18102022_101_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_11_11_Session_1_18102022_101_BTCF_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_BatchInput/63_11_11_Session_1_18102022_102_BTCF_BI.json ' 
        '../../metadata/Project_Hoehengradient/Schrofen/SF_JSON/SF_MegaDetected/63_11_11_Session_1_18102022_102_BTCF_MD.json '

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
