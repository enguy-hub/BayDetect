"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_036_Session_7_20220803.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_040_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_042_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_043_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_044_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_045_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_046_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_047_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_048_Session_7_20220802.txt '
        '&& '
        'python main.py < '
        'C:/LWF/BayDetect/metadata/Wolf/Trail/VFTrail_BatchCmds/pf4_sortImages/pf4_sortImages_VFT_051_Session_7_20220802.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        # Insert new python commands below these two lines:
        'cd cameratraps/detection '
        '&& '
        
        # Below here:
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_031_Session_7_20220801_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_031_Session_7_20220801_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_032_Session_7_20220801_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_032_Session_7_20220801_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_033_Session_7_20220801_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_033_Session_7_20220801_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_034_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_034_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_035_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_035_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_036_Session_7_20220803_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_036_Session_7_20220803_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_040_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_040_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_042_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_042_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_043_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_043_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_044_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_044_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_045_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_045_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_046_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_046_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_047_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_047_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_048_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_048_Session_7_20220802_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v5a.0.0.pt ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_BatchInput_S7/VFT_051_Session_7_20220802_BI.json ' 
        '../../metadata/Wolf/Trail/VFTrail_JSON/VFTrail_MegaDetected_S7/VFT_051_Session_7_20220802_MD.json '

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
