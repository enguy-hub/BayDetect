"""
This script contains the `user_input` interactive commands for BayDetect.
"""

import baydetect.process_functions as pf
import baydetect.batch_functions as bf
import baydetect.utility_functions as uf


def main():

    intro_choice = input("Enter '1' to use processing functions \n"
                         "Enter '2' to use utility functions \n"
                         "Enter '3' to use batch functions \n"
                         "\n"
                         "Enter your choice here: ")

    intro_choice = int(intro_choice)

    # -----------------------------------------------
    # Processing Functions for PRE/POST MegaDetection
    # -----------------------------------------------

    if intro_choice == 1:

        print("\n'1' Selected ! Please choose one processing function to start from the list of options below ..."
              "\n")

        pf_choice = input("Enter '1' to create the `BatchInput` JSON file require to execute `run_detector_batch.py`\n"
                          "Enter '2' to convert the `MegaDetected` JSON file into an organized CSV `Metadata` file\n"
                          "Enter '3' to sort the images into separate folder based on their `MegaDetected` classes "
                          "using the CSV `Metadata` file\n"
                          "\n"
                          "Enter your choice here: ")

        pf_choice = int(pf_choice)

        if pf_choice == 1:
            print("\n'1' Selected ! Creating the `BatchInput` JSON file needed to execute `run_detector_batch.py` .."
                  "\n")
            pf.md_json_creator()

        elif pf_choice == 2:
            print("\n'2' Selected ! Converting the `MegaDetected` JSON file into an organized CSV `Metadata` file .."
                  "\n")
            pf.md_csv_converter()

        elif pf_choice == 3:
            print("\n'3' Selected ! Sorting the images into separate folder based on their `MegaDetected` classes "
                  "using the CSV `Metadata` file .."
                  "\n")
            pf.sort_images_csv()

        else:
            print("\nWrong choice, please re-run the script and follow the instructions !!!"
                  "\n")

    # -------------------------------------------------------------------------------------
    # Utility Functions: Help automate repetitive tasks when using the processing functions
    # -------------------------------------------------------------------------------------

    elif intro_choice == 2:

        print("\n'2' Selected ! Please choose one utility function to start from the list of options below .."
              "\n")

        uf_choice = input("Enter '1' to find and replace the names of multiple folders at once\n"
                          "Enter '2' to find and replace the names of multiple files at once\n"
                          "Enter '3' to find and replace the text-content inside multiple files at once\n"
                          "\n"
                          "Enter your choice here: ")

        uf_choice = int(uf_choice)

        if uf_choice == 1:
            print("\n'1' Selected ! Find and replace the names of multiple folders at once .."
                  "\n")
            uf.find_replace_dirname()

        elif uf_choice == 2:
            print("\n'2' Selected ! Find and replace the names of multiple files at once .."
                  "\n")
            uf.find_replace_filename()

        elif uf_choice == 3:
            print("\n'3' Selected ! Find and replace the text-content inside multiple files at once .."
                  "\n")
            uf.find_replace_text()

        else:
            print("\nWrong choice, please re-run the script and follow the instructions !!!"
                  "\n")

    # ----------------------------------------------------------------------
    # Batch Functions: Create commands needed to execute `batchrun.py` script
    # ----------------------------------------------------------------------

    elif intro_choice == 3:

        print("\n'3' Selected ! Please choose one batch function to start from the list of options below .."
              "\n")

        bf_choice = input("Enter '1' to create multiple '.txt' files needed to 'batch-run' one of the Processing "
                          "Functions,\nexcept for `Run MegaDetector` function \n"
                          "Enter '2' to create a combined '.txt' file contains the commands needed to start "
                          "`pf_batchrun()` from `batchrun.py`\n"
                          "Enter '3' to create a '.txt' file contains the commands needed to start `md_batchrun()` "
                          "from `batchrun.py`\n"
                          "\n"
                          "Enter your choice here: ")

        bf_choice = int(bf_choice)

        if bf_choice == 1:
            print("\n'1' Selected ! Create '.txt' files needed to 'batch-run' one of the processing functions"
                  "\n")
            bf.pf_txtcmds_creator()

        elif bf_choice == 2:
            print("\n'2' Selected ! Create a combined `.txt` file contains the commands needed to start `pf_batchrun()`"
                  " from `batchrun.py` .."
                  "\n")
            bf.pf_pycmds_creator()

        elif bf_choice == 3:
            print("\n'3' Selected ! Create a `.txt` file contains the commands needed to start `md_batchrun()` from "
                  "`batchrun.py` .."
                  "\n")
            bf.md_pycmds_creator()

        else:
            print("\nWrong choice, please re-run the script and follow the instructions !!!"
                  "\n")

    else:
        print("\nWrong choice, please re-run the script and follow the instructions !!!"
              "\n")


if __name__ == '__main__':
    main()
