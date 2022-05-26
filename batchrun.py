"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/Hien/Garden/MyGithub/BayDetect/example/metadata/Example_Forest/EF_batch_commands/EF_mdJSONToCSV_txtcmds_CU/EF_mdJSONToCSV_001_20201104.txt '
        '&& '
        'python main.py < '
        'C:/Hien/Garden/MyGithub/BayDetect/example/metadata/Example_Forest/EF_batch_commands/EF_mdJSONToCSV_txtcmds_CU/EF_mdJSONToCSV_002_20201104.txt '
        '&& '
        'python main.py < '
        'C:/Hien/Garden/MyGithub/BayDetect/example/metadata/Example_Forest/EF_batch_commands/EF_mdJSONToCSV_txtcmds_CU/EF_mdJSONToCSV_003_20201104.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        'cd cameratraps '
        '&& '
        # Insert new python commands below this line
                
        'python run_detector_batch.py md_v4.1.0.pb ' 
        '../example/metadata/Example_Forest/EF_JSON/EF_CU_BatchInput/EF_001_20201104_BI.json ' 
        '../example/metadata/Example_Forest/EF_JSON/EF_CU_MegaDetected/EF_001_20201104_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v4.1.0.pb ' 
        '../example/metadata/Example_Forest/EF_JSON/EF_CU_BatchInput/EF_002_20201104_BI.json ' 
        '../example/metadata/Example_Forest/EF_JSON/EF_CU_MegaDetected/EF_002_20201104_MD.json ' 
        '&& '
        'python run_detector_batch.py md_v4.1.0.pb ' 
        '../example/metadata/Example_Forest/EF_JSON/EF_CU_BatchInput/EF_003_20201104_BI.json ' 
        '../example/metadata/Example_Forest/EF_JSON/EF_CU_MegaDetected/EF_003_20201104_MD.json '

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
