# BayDetect

BayDetect is a stack of functions aims to help streamline the pre- and post-processing of camera trap images via Microsoft's
[MegaDetector](https://github.com/Microsoft/CameraTraps#megadetector).
This project was developed within the 
[Biodiversity, Conservation and Wildlife Management Department @ Bavarian State Institute of Forestry](https://www.lwf.bayern.de/en/221946/index.php). 

------------------------------------------------------------------------------------------------------------------------
## What does this project hope to achieve?
 
1. Partially removing the costly and intensive manual labor process of classifying images containing animals vs those without.

2. Reducing the repetitive steps encountered when using [MegaDetector batch processing](https://github.com/microsoft/CameraTraps/blob/master/megadetector.md#2-run_tf_detector_batchpy)
for large datasets.

## Why BayDetect?

The project was created help scientists from the Wildlife Monitoring and Management Team at LWF to detect different 
animal species in forests in and around Bavaria, Germany. Hence, the name `BayDetect` was chosen.

------------------------------------------------------------------------------------------------------------------------
## **Important notes**

There are two ways to use BayDetect:
- Via a Graphical User Interface (GUI) with was built using `tkinter` library from Python
- Via the command line, for which users can give BayDetect instructions using the built-in 
[`input()` functions from Python](https://docs.python.org/3/library/functions.html#input).

Both Microsoft's MegaDetector [CameraTraps](https://github.com/microsoft/CameraTraps) and [ai4eutils](https://github.com/microsoft/ai4eutils) 
are added to BayDetect as `git submodules`, which allows users to track the most update-to-date version of these two repositories.

The [MegaDetector's model](https://github.com/microsoft/CameraTraps/blob/master/megadetector.md#downloading-the-model)
exceeds GitHub's file size limit of 100.00 MB. Thus, please download it to your computer before running.

------------------------------------------------------------------------------------------------------------------------
## Prerequisites / Installation guide

#### 1. Clone the repo

    git clone --recursive https://github.com/enguy-hub/BayDetect.git

#### 2. Fetch the latest changes for `cameratraps` and `ai4eutils` submodules

- For ai4eutils, cd into `/ai4eutils` directory and run the following command:

      `git checkout master`; then `git pull`

- For cameratraps, cd into `/cameratraps` directory and run the following command:

      `git checkout main`; then `git pull`

#### 3. Download MegaDetector model file

- The easiest way is to download it directly from the link shown in the [CameraTraps's GitHub page](https://github.com/microsoft/CameraTraps/blob/master/megadetector.md#downloading-the-model)
- Or via `wget`

      wget https://lilablobssc.blob.core.windows.net/models/Camera_traps/megadetector/md_v4.1.0/md_v4.1.0.pb

- **VERY IMPORTANT**: Please save the model file (`md_v4.1.0.pb`) inside the `/cameratraps` folder, and also copy 
the `run_detector_batch.py` file from the `/cameratraps/detection/` folder to the `/cameratraps` folder as well. 

#### 4. Download and Install Miniconda

- Go to [Miniconda page](https://docs.conda.io/en/latest/miniconda.html) and follow the instruction on how to download and install Miniconda based on your own OS.

#### 5. Create `cameratraps-detector` conda environment by running this command at root folder (`/BayDetect`):

    conda env create --file environment-detector-lwf.yml

#### 6. Activate `cameratraps-detector` conda environment

    conda activate cameratraps-detector

#### 7. Putting the images that you want to be classified inside `/image_data` directory

- When there are multiple camera-trap stations and sessions, we suggest to arrange them as shown below:

      /example/image_data/Example_Forest/Raw_Photos/EF_001/20201104/*.jpg
      /example/image_data/Example_Forest/Raw_Photos/EF_002/20201104/*.jpg
      /example/image_data/Example_Forest/Raw_Photos/EF_003/20201104/*.jpg

### Once all the above steps are complete, you are ready to use BayDetect !!!

------------------------------------------------------------------------------------------------------------------------
## Features in BayDetect

#### Processing Functions (PF)
- 1/ Create the `BatchInput` JSON file needed to execute `MegaDetector` via `run_detector_batch.py` script.
- 2/ Run MegaDetector via `run_detector_batch.py` script using the `BatchInput` JSON file as input, 
and produce a `MegaDetected` JSON file as the output.
- 3/ Convert the output `MegaDetected` JSON file into an organized CSV `Metadata` file.
- 4/ Sort the images into separated folders based on their `MegaDetected` classes indicated in the CSV `Metadata` file.

#### Utility Functions (UF)
- 1/ Find and replace the names of multiple folders at once.
- 2/ Find and replace the names of multiple files at once.
- 3/ Find and replace the text-content inside multiple files at once.

#### Batch Functions (BF)
- 1/ Create '.txt' files containing the commands needed to 'batch-run' one of the Processing Function (except for 
Processing Function #2 | Run MegaDetector)
- 2/ Create a combined ".txt" file containing the commands needed to start the `pf_batchrun()` from `batchrun.py`.
- 3/ Create ".txt" file containing the commands needed to 'batch-run' the process of executing MegaDetector via the 
`md_batchrun()` from `batchrun.py`. ('batch-run` function for Processing Function #2 | Run MegaDetector)

------------------------------------------------------------------------------------------------------------------------
## **Extra Note**

Before using BayDetect, always makesure that the `cameratraps-detector` conda environment is activated. 
Activate it with the following command:

    conda activate cameratraps-detector

Optional: if you want MegaDetector to only save `detection boxes` that are 85% confidence or above in the output 
JSON file, open the `cameratraps/detection/run_detector.py` file and change the value in `line 73` to `0.85` as follows:

    DEFAULT_OUTPUT_CONFIDENCE_THRESHOLD = 0.85

------------------------------------------------------------------------------------------------------------------------
## How to run BayDetect

- 1/ Run `app.py` script at root folder (`/BayDetect`) via the command below:

      python app.py

- 2/ Choose the function that you would like to like use

- 3/ Follow the prompted steps and instruction to execute the desired function

------------------------------------------------------------------------------------------------------------------------
## Suggestions & notes for when executing the functions

------------------------------------------------------------------------------------------------------------------------
### Processing Function (PF)

###### =================================================================================================================
#### PF 1 | Create the `BatchInput` JSON file

- We suggest the `BatchInput (BI)` JSON file should be saved in a `*_BatchInput/` folder, 
and the filename should end it with `*_BI.json`, similar to the example below:

      /BayDetect/example/metadata/Example_Forest/EF_JSON/EF_BatchInput/*_BI.json

- Additionally, when working with a large dataset which has many stations and sessions, we suggest that each JSON file 
should be named corresponding to its station and session. See the example JSON files in the directory stated below:

      /BayDetect/example/metadata/Example_Forest/JSON/EF_BatchInput/EF_007_20201104_BI.json

###### =================================================================================================================
#### PF 2 | Run MegaDetector 

- We suggest that the output `MegaDetected (MD)` JSON files should be saved in a `*_MegaDetected/` folder, and the 
filenames to end with `*_MD.json` similar to our example below:

      /BayDetect/example/metadata/Example_Forest/EF_JSON/EF_MegaDetected/EF_007_20201104_MD.json

###### =================================================================================================================
#### PF 3 | Convert output `MegaDetected (MD)` JSON file into an organized CSV `Metadata (Meta)` file.

- We suggest that the output CSV `Metadata (Meta)` files should be saved in a `*_CSV/` folder, and the filename to 
end with `*_Meta.csv`, similar to the example below:

      /BayDetect/example/metadata/Example_Forest/EF_CSV/*_Meta.csv

- Additionally, when working with a large dataset that has many stations and sessions, we suggest that each CSV file 
should be named corresponding to its station and session. See the example files in the directory stated below:

      /BayDetect/example/metadata/Example_Forest/EF_CSV/EF_007_20201104_Meta.csv

###### =================================================================================================================
#### PF 4 | Sort images into folders based on their `MegaDetected` classes indicated in the CSV `Meta` file

- By default, only copies of the original images will be sorted inside `Animal`, `Human`, `Vehicle`, or `Empty` folders. 
Thus, if you want to save space and to directly move the original images into 'sorted folders', you can change the 
`shutil.copy()` function to `shutil.move()` in line `323` in the `/baydetect/process_functions.py` script

- Line `323` in `/baydetect/process_functions.py` script should be as follows:

      322|  for o, n in zip(old_path, new_path):
      323|     shutil.move(o, n)

------------------------------------------------------------------------------------------------------------------------
### Batch Function (BF)

###### =================================================================================================================
#### BF 1 | Create `.txt` files needed to 'batch-run' one of the Processing Functions (except for `Run MegaDetector`)

- For better organizing the output `.txt` files, we suggest to store the files similar to our folder structure 
as shown in the `EF_batch_commands/` example folder. For reference, please check out the folder structure and how the 
`.txt` files are saved in the `EF_batch_commands/` example folder. Path to `EF_batch_commands/` folder is listed below:

      /example/metadata/Example_Forest/EF_batch_commands/

- **For PF 3 Only**: The CSV metadata file organizes the `Name`, `Station`, and `Session` of the image files based on 
the file paths in `*_MD.json` file. Hence, you will need to change the values for `imageName`, `station`, and `session` 
variables in lines `169-171` in the `process_functions.py` script (*path shown below*) according to whichever index 
order would the `imageName`, `station`, and `session` be in an array when the file path in the `*_MD.json` is split 
with `/` as separator:

      /baydetect/process_functions.py

  - The values inside the squared brackets at the end of lines `169-171` should be changed accordingly depending on 
  users' specific situation:

        169|   imageName = list(json_info['image'][i].values())[0].split('/')[12] <-- Change this value
        170|   session = list(json_info['image'][i].values())[0].split('/')[10] <-- Change this value
        171|   station = list(json_info['image'][i].values())[0].split('/')[9] <-- Change this value

###### =================================================================================================================
#### BF 2 | Create a combined `.txt` file containing the commands needed to start `pf_batchrun()` from `batchrun.py`

- With regard to saving the `.txt` file, we suggest to save the file with the following naming format 
`*dataset_id*_*pf_name*_combinedCmds`. For reference, please check out the `*dataset_id*_*pf_name*_combinedCmds` files
in our example `EF_batch_commands` folder. Paths to the folder/files are listed below:

      /example/metadata/Example_Forest/EF_batch_commands/EF_createBIJSON_combinedCmds.txt
      /example/metadata/Example_Forest/EF_batch_commands/EF_mdJSONtoCSV_combinedCmds.txt
      /example/metadata/Example_Forest/EF_batch_commands/EF_sortImages_combinedCmds.txt
      
#### Extra - BF 2 | How to execute `pf_batchrun()` function from `/batchrun.py` script

- 1/ Copy the commands (the text-content) from the newly created `*dataset_id*_*pf_name*_combinedCmds.txt` file 
into the `pf_batchrun()` function in the `batchrun.py` script, and make sure that they are below line `6`

- 2/ Run `batchrun.py` script via the command below:
    
      python batchrun.py
    
- 3/ Enter number `1` to execute the function

- **Note**: If you have a large dataset with many stations and sessions, you will receive an 
"error" saying that your commands are too long. When this happens, just commented out a portion 
of the commands and execute them in multiple smaller executions.

###### =================================================================================================================
#### BF 3 - Create a `.txt` file containing the commands needed to start `md_batchrun()` from `batchrun.py` ('batch-run' function for `PF 2 | Run MegaDetector`)

- With regard to saving the `.txt` file, we suggest to save the file with the following naming format 
`*dataset_name*_runMD_cmds`. For reference, please check out the `*dataset_name*_runMD_cmds` file in our 
example `EF_batch_commands` folder. Path to the folder/file is listed below:

      /example/metadata/Example_Forest/EF_batch_commands/EF_runMD_cmds.txt

#### Extra - BF 3 | How to execute `md_batchrun()` function from `/batchrun.py` script

- 1/ Copy the commands (the text-content) from the newly created `*dataset_name*_runMD_cmds` into the 
`md_batchrun()` function in the `batchrun.py` script, and make sure that they are below line `18` 

- 2/ Run `batchrun.py` script via the command below:
    
      python batchrun.py
    
- 3/ Enter number `2` to execute the `md_batchrun()` function

- **Note**: If you have a large dataset with many stations and sessions, you will receive an "error" saying that your 
commands are too long. When this happens, just commented out a portion of the commands and execute them in multiple
smaller executions.

---

# License
Distributed under the MIT License. See `LICENSE.txt` for more information.
