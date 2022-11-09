"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_001_Session_6_02052021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_002_Session_6_07052021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_013_Session_6_11052021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_015_Session_6_29062021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_016_Session_6_22102020.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_030_Session_6_05072021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_035_Session_6_01072021.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Karwendel_Rohdaten/KW_BatchCmds/pf3_mdJSONToCSV/pf3_mdJSONToCSV_KW_038_Session_6_07052021.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        'cd cameratraps/detection '
        '&& '
        # Insert new python commands below this line
                                                                
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_001_Session_6_02052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_001_Session_6_02052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_001_Session_7_12102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_001_Session_7_12102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_001_Session_8_26052022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_001_Session_8_26052022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_001_Session_9_06102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_001_Session_9_06102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_002_Session_6_07052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_002_Session_6_07052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_002_Session_7_11102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_002_Session_7_11102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_002_Session_8_10042022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_002_Session_8_10042022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_002_Session_9_11102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_002_Session_9_11102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_013_Session_6_11052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_013_Session_6_11052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_013_Session_8_29052022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_013_Session_8_29052022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_013_Session_9_12102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_013_Session_9_12102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_015_Session_6_29062021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_015_Session_6_29062021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_015_Session_7_19122021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_015_Session_7_19122021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_015_Session_8_12052022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_015_Session_8_12052022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_015_Session_9_12082022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_015_Session_9_12082022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_016_Session_6_22102020_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_016_Session_6_22102020_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_016_Session_7_11052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_016_Session_7_11052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_016_Session_8_12102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_016_Session_8_12102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_016_Session_9_10052022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_016_Session_9_10052022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_030_Session_6_05072021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_030_Session_6_05072021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_030_Session_7_05102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_030_Session_7_05102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_030_Session_8_29112021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_030_Session_8_29112021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_030_Session_9_07102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_030_Session_9_07102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_035_Session_6_01072021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_035_Session_6_01072021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_035_Session_7_04102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_035_Session_7_04102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_035_Session_8_04012022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_035_Session_8_04012022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_035_Session_9_05102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_035_Session_9_05102022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_038_Session_6_07052021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_038_Session_6_07052021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_038_Session_7_11102021_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_038_Session_7_11102021_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_038_Session_8_01042022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_038_Session_8_01042022_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_BatchInput/KW_038_Session_9_11102022_BI.json ' 
        '../../metadata/Karwendel_Rohdaten/KW_JSON/KW_MegaDetected/KW_038_Session_9_11102022_MD.json ' 

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
