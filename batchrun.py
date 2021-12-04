"""This script contains the pf_batchrun() and md_batchrun() functions."""

import os


def pf_batchrun():
    os.system(
        # Insert new python commands below this line

        'python main.py < '
        'C:/LWF/BayDetect/batch_commands/Wolf_Intense/pf1_VF_txtcmds/pf1_VF_91_D_Session_1_20201102.txt '

    )
    return print('Finished !!')


def md_batchrun():
    os.system(
        'cd cameratraps '
        '&& '
        # Insert new python commands below this line

        'python run_tf_detector_batch.py md_v4.1.0.pb '
        '../metadata/Wolf_Intense/JSON/BatchInput/VF_102_A_Session_1_20201102_BI.json '
        '../metadata/Wolf_Intense/JSON/MegaDetected/VF_102_A_Session_1_20201102_MD.json '

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
