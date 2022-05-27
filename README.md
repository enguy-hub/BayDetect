# BayDetect

BayDetect is a stack of functions aim to help streamline the pre- and post-processing of camera trap images via Microsoft's
[MegaDetector](https://github.com/Microsoft/CameraTraps#megadetector).
This project was developed within the 
[Biodiversity, Conservation and Wildlife Management Department @ the Bavarian State Institute of Forestry](https://www.lwf.bayern.de/en/221946/index.php). 

#### What does this project hope to achieve?
 
1. Partially removing the costly and intensive manual labor process of classifying images containing animals vs those without.

2. Reducing the repetitive steps encountered when using [MegaDetector batch processing](https://github.com/microsoft/CameraTraps/blob/master/megadetector.md#2-run_tf_detector_batchpy)
for large datasets.

#### Why BayDetect?

The project was created help scientists from the Wildlife Monitoring and Management Team at LWF to detect different 
animal species in forests in and around Bavaria, Germany. Hence, the name `BayDetect` was chosen.

---

## **Important Notes**

- There are two ways to use BayDetect:
  - Via a Graphical User Interface (GUI) with was built using `tkinter` library from Python
  - Via the command line, for which users can give BayDetect instructions using the built-in 
  [`input()` functions from Python](https://docs.python.org/3/library/functions.html#input).


- Both Microsoft's MegaDetector [CameraTraps](https://github.com/microsoft/CameraTraps) and [ai4eutils](https://github.com/microsoft/ai4eutils) 
  are added to BayDetect as `git submodules`, which allows users to track the most update-to-date version of these two repositories.
- 

- The [MegaDetector's model](https://github.com/microsoft/CameraTraps/blob/master/megadetector.md#downloading-the-model)
exceeds GitHub's file size limit of 100.00 MB. Thus, please download it to your computer before running.

---

## Prerequisites / Installation Guide

#### 1. Clone the repo

    git clone --recursive https://github.com/enguy-hub/BayDetect.git

#### 2. Fetch the latest changes for `cameratraps` and `ai4eutils` submodules

- For ai4eutils, cd into `/ai4eutils` directory and run the following command:

      `git checkout master`; then `git pull`

- For cameratraps, cd into `/cameratraps` directory and run the following command:

      `git checkout main`; then `git pull`

#### 3. Download MegaDetector model file

- The easiest way is to download it directly from the link shown in the [CameraTraps's Github page](https://github.com/microsoft/CameraTraps/blob/master/megadetector.md#downloading-the-model)
- Or via `wget`

      wget https://lilablobssc.blob.core.windows.net/models/Camera_traps/megadetector/md_v4.1.0/md_v4.1.0.pb


**VERY IMPORTANT**: 
- Please save the model file (`md_v4.1.0.pb`) inside the `/cameratraps` folder, and also copy the 
`run_detector_batch.py` file from the `/cameratraps/detection/` folder to the `/cameratraps` folder as well. 

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

**Once all the above steps are complete, you are ready to use BayDetect !!!**

---

## Features in BayDetect

There are three sets of functions in BayDetect: 

#### Processing Functions
- 1/ Create the `BatchInput` JSON file needed to execute `run_detector_batch.py`.
- 2/ Run MegaDetector with `run_detector_batch.py` script using the `BatchInput` JSON file create from 
`Processing Function 1` as input file, and produce a `MegaDetected` JSON file as the result.
- 3/ Convert the output `MegaDetected` JSON file created from `Processing Function 2` into a `CSV metadata` file.
- 4/ Sort the images into separated folders based on their `megadetected classes` using the `CSV metadata` file created
from `Processing Function 3`.

#### Utility Functions
- 1/ Find and replace the names of multiple folders at once.
- 2/ Find and replace the names of multiple files at once.
- 3/ Find and replace the text-content inside multiple files at once.

#### Batch Functions
- 1/ Create multiple '.txt' files containing the commands needed to `batch-run` one of the `Processing Function`.
- 2/ Create a combined ".txt" file containing the commands needed to start the `pf_batchrun()` function from `batchrun.py`.
- 3/ Create ".txt" file containing the commands needed to `batch-run` the process of executing MegaDetector via the 
  `md_batchrun()` function from `batchrun.py`

**IMPORTANT**

- Before using BayDetect, please always makesure that the `cameratraps-detector` conda environment is activated. 
Activate it with the following command:

      conda activate cameratraps-detector

- Optional: if you want MegaDetector to only save `detection boxes` that are 85% confidence or above in the output 
JSON file, open the `cameratraps/detection/run_detector.py` file and change the value in `line 73` to `0.85` as follows:

      DEFAULT_OUTPUT_CONFIDENCE_THRESHOLD = 0.85

---

## How To Run BayDetect

#### Processing Function 1 | Create the `batch-input` JSON file needed to execute `run_detector_batch.py`

1/ Run `app.py` script via the command below:

    python app.py

2/ Enter the prompted steps and the instruction to create the `batch-input` JSON file needed to run MegaDetector

- Optional: For better organizing file names and folder structure, we suggest the `batch-input` JSON filename to end it 
with `*_BatchInput.json` and the file to be saved in a similar folder structure as the example below:

      /example/metadata/Example_Forest/JSON/BatchInput/*_BatchInput.json

- Additionally, when working with a large dataset that has many stations and sessions, we suggest that each JSON file 
should be named corresponding to its station and session. See example in the directory stated below:

      /example/metadata/Example_Forest/JSON/BatchInput/EF_001_20201104_BatchInput.json
      /example/metadata/Example_Forest/JSON/BatchInput/EF_002_20201104_BatchInput.json
      /example/metadata/Example_Forest/JSON/BatchInput/EF_003_20201104_BatchInput.json

#### Executing `run_detector_batch.py` script

1/ Navigate to the "cameratraps" folder via the following command:

    cd cameratraps

2/ Run `run_detector_batch.py` using the BatchInput JSON file created from above. An example is demonstrated below:

- Windows command

      python run_detector_batch.py md_v4.1.0.pb
      ../example/metadata/Example_Forest/JSON/BatchInput/EF_007_20201104_BatchInput.json 
      ../example/metadata/Example_Forest/JSON/MegaDetected/EF07_20201104_MegaDetected.json
       
- Linux command

      python run_detector_batch.py md_v4.1.0.pb 
      ../example/metadata/Example_Forest/JSON/BatchInput/EF_007_20201104_BatchInput.json 
      ../example/metadata/Example_Forest/JSON/MegaDetected/EF07_20201104_MegaDetected.json

- For better organizing file names and folder structure, we suggest that the output JSON files should be saved in the 
`/example/metadata/*dataset_name*/JSON/MegaDetected/` directory, and ends it with `*_MegaDetected.json`. See the example
JSON files in the directory stated below:

      /example/metadata/Example_Forest/JSON/BatchInput/EF_007_20201104_BI.json
      /example/metadata/Example_Forest/JSON/MegaDetected/EF_007_20201104_MD.json

3/ Navigate back to root directory via the following command:

    cd ..

4/ **For Windows users only** - Change the path delimiter of the JSON files to forward slashes instead of backward 
slashes using function `3` from the **Batch Utility Functions** set.

    python main.py

- Enter number `2` then number `3`, and follow the instructions prompted and change the backward slashes to forward 
slashes for the JSON files.

- Alternatively, you can also change the path delimiter in the JSON files using the built-in Find/Replace tool in Notepad too

---

#### Processing Function 2 - Convert the output JSON file produced from `run_detector_batch.py` into an organized CSV metadata file.

1/ Run `main.py` script via the command below:

    python main.py

2/ Enter number `1` then number `2`, and follow the prompted instruction to convert the output JSON file produced 
from `run_detector_batch.py` into an organized CSV metadata file.

- For better organizing file names and folder structure, we suggest that the output JSON files should be 
saved in the `/example/metadata/*dataset_name*/CSV/` directory, and ends it with `*_Meta.csv`. 
See example below:

      /example/metadata/Example_Forest/CSV/*_Meta.csv

- Additionally, when working with a large dataset that has many stations and sessions, we suggest that each JSON file 
should be named corresponding to its station and session. For example, checkout the files in the directory stated below:

      /example/metadata/Example_Forest/CSV/EF_007_20201104_Meta.csv
      /example/metadata/Example_Forest/CSV/EF_008_20201104_Meta.csv
      /example/metadata/Example_Forest/CSV/EF_009_20201104_Meta.csv

**Important**: The CSV metadata file organizes the `Name`, `Station`, and `Session` of the image files based on their 
images' filepath in the `*_MegaDetected.json` file. Hence, you will need to change the values for `imageName`, `station`
, and `session` variables in lines `124-126` in the `process_functions.py` script. The script can edit at:

    /baydetect/process_functions.py

  - The values inside the squared brackets at the end of lines `124-126` should be changed accordingly to the paths shown 
  in your respective `*_MegaDetected.json` file:

        124|   imageName = list(json_info['image'][i].values())[0].split('/')[9] <-- Change this value
        125|   session = list(json_info['image'][i].values())[0].split('/')[8] <-- Change this value
        126|   station = list(json_info['image'][i].values())[0].split('/')[7] <-- Change this value

---

#### Processing Function 3 - Sort the classified images produced from `run_detector_batch.py` into folders of their 'detected' classes using the CSV metadata file

1/ Run `main.py` script via the command below:

    python main.py

2/ Enter number `1` then number `3`, and follow the prompted instruction to sort the classified images after running 
`run_detector_batch.py` into their 'detected' classes using the `*_Meta.csv` created from function 2.

- For better organizing the images and keep the directory of the original images undisturbed, we suggest that new sorted
images to be saved in a separate directory but on the same level as the original images' directory. We suggest to name 
the directory containing the sorted images as `*_Sorted`. See example below:

      Original image directory:  
      /example/image_data/Example_Forest/Bilder_Rohten/EF_007/20201104/*.JPG
      
      New sorted image directories:
      /example/image_data/Example_Forest/Bilder_Rohten/EF_007/20201104_Sorted/Animal/*.JPG
      /example/image_data/Example_Forest/Bilder_Rohten/EF_007/20201104_Sorted/Empty/*.JPG
      /example/image_data/Example_Forest/Bilder_Rohten/EF_007/20201104_Sorted/Person/*.JPG


**Note**: If you would like to save space on your computer and want to perform the sorting directly on the original 
images' directory, you can use the original image directory for the first prompted question when running function. However
, only copies of the original images will be sorted inside `Animal`, `Human`, `Vehicle`, or `Empty` folders. Thus, if
you wish to move the original images, you can change the `shutil.copy()` function to `shutil.move()` in line `291` 
inside the `/baydetect/process_functions.py` script

  - Line `291` in `/baydetect/process_functions.py` script should be as follow:

        291|   shutil.move(o, n)

---

## Utility Functions

#### Utility Function 1 - Find and replace multiple folders' name at once

1/ Run `main.py` script via the command below:
    
    python main.py

2/ Enter number `2` then number `1`, and follow the prompted instruction to find and replace multiple folders' name at 
once.

---

#### Utility Function 2 - Find and replace multiple files' name at once

1/ Run `main.py` script via the command below:

    python main.py

2/ Enter number `2` then number `2`, and follow the prompted instruction to find and replace multiple files' name at
once.

---

#### Utility Function 3 - Find and replace multiple files' text-content at once

1/ Run `main.py` script via the command below:
    
    python main.py

2/ Enter number `2` then number `3`, and follow the prompted instruction to find and replace multiple files' 
text-content at once.

---

#### Utility Function 4 - Find and delete one line of text in multiple files at once

1/ Run `main.py` script via the command below:
    
    python main.py

2/ Enter number `2` then number `4`, and follow the prompted instruction to find and delete one line of text in 
multiple files at once.

---

## Batch Functions

#### Batch Function 1 - Create multiple 'text-command' files needed to 'batch-run' one of the Processing Functions

1/ Run `main.py` script via the command below:
    
    python main.py

2/ Enter number `3` then number `1`, and follow the prompted instruction to create 'text-command' files needed to 
'batch-run' one of the Processing Functions.

- For better organizing the `.txt files`. We suggest to first create new directories inside 
`/metadata/*dataset_name*/batch_commands/` directory with the following naming convention `pf*_*dataset_name*_txtcmds`
and have the new `text-command files` saved in there. Checkout the example directories and text-command files below:

      /example/metadata/Example_Forest/batch_commands/pf1_EF_txtcmds/pf1_EF_007_20201104.txt
      /example/metadata/Example_Forest/batch_commands/pf2_EF_txtcmds/pf2_EF_007_20201104.txt
      /example/metadata/Example_Forest/batch_commands/pf3_EF_txtcmds/pf3_EF_007_20201104.txt

**IMPORTANT**: This function derives the `Station`, and `Session` names of from the original directory paths of where the 
images are saved (inside the `/image_data/Example_Forest/` directory). Therefore, to make sure that the names of the
new `text-command files` and the text-content inside them are correct, you will need to change the values for 
`dataset_station`, and `session` variables in lines `54-55` for Windows users and lines in the `159-160` for Linux users 
in `batch_functions.py` script. For more details, see below:

  - *Windows users* - The following values in lines `54-55` in `/baydetect/batch_functions.py` script should be changed:

        54|   dataset_station.append(''.join(idirpaths.split('//')[9])) <-- Change this value
        55|   session.append(''.join(idirpaths.split('//')[10])) <-- Change this value

  - *Linux users* - The following values in lines `159-160` in `/baydetect/batch_functions.py` script should be changed:

        159|   dataset_station.append(''.join(idirpaths.split('/')[9])) <-- Change this value
        160|   session.append(''.join(idirpaths.split('/')[10])) <-- Change this value

---

#### Batch Function 2 - Create a text-file (`.txt`) containing the python commands needed to start `pf_batchrun()` function from `batchrun.py`

1/ Run `main.py` script via the command below:
    
    python main.py

2/ Enter number `3` then number `2`, and follow the prompted instruction to create a `.txt` file containing the python 
commands needed to start the `pf_batchrun()` function from `batchrun.py`.

- In regards to saving the `python-command files`, we suggest to save them inside the `/metadata/*dataset_name*/batch_commands/` 
directory with following naming format `pf*_*dataset_name*_pycmds.txt`. Checkout the example `python-command .txt files`
for used for 'batch-running' Processing function below:

      /example/metadata/Example_Forest/batch_commands/pf1_EF_pycmds.txt
      /example/metadata/Example_Forest/batch_commands/pf2_EF_pycmds.txt
      /example/metadata/Example_Forest/batch_commands/pf3_EF_pycmds.txt
      
#### Executing `pf_batchrun()` function from `/batchrun.py` script

1/ Copy the python commands (the text-content) from the newly created `pf*_*dataset_name*_pycmds.txt` into the 
`pf_batchrun()` function in the `batchrun.py` script, and make sure that they are below line `6` 

2/ Run `batchrun.py` script via the command below:
    
    python batchrun.py
    
3/ Enter number `1` to execute the 'batch-run' python commands

**Note**: If you have a large dataset with many stations and sessions, you will receive an "error" saying that your 
commands are too long. When this happen, just commented out a portion of the python commands and execute them in 
multiple small executions.

---

#### Batch Function 3 - Create a text-file (`.txt`) containing the python commands needed to start `md_batchrun()` function from `batchrun.py`

1/ Run `main.py` script via the command below:
    
    python main.py

2/ Enter number `3` then number `3`, and follow the prompted instruction to create a `.txt` file containing the python 
commands needed to start the `md_batchrun()` function from `batchrun.py`.

- Regarding saving and naming for the `python-commands file`, we suggest to save it inside the 
`/metadata/*dataset_name*/batch_commands/` directory and name the file with the following format 
`*dataset_name*_MD_pycmds.txt`. Checkout the example directory and `python-commands file` below:

      /example/metadata/Example_Forest/batch_commands/EF_MD_pycmds.txt

#### Executing `md_batchrun()` function from `/batchrun.py` script

1/ Copy the python commands from the newly created `*dataset_name*_MD_pycmds.txt` into the `md_batchrun()` 
function in the `batchrun.py` script, and make sure that they are below line `18` 

2/ Run `batchrun.py` script via the command below:
    
    python batchrun.py
    
3/ Enter number `2` to start 'batch-running' the process of image classification via `run_tf_detector_batch.py` script 
from `/CameraTraps` directory

**Note**: If you have a large dataset with many stations and sessions, you will receive an "error" saying that your 
commands are too long. When this happen, just commented out a portion of the python commands and execute them in multiple
small executions.

---

# License
Distributed under the MIT License. See `LICENSE.txt` for more information.
