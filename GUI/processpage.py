from tkinter import ttk, filedialog
from scrollpage import ScrolledPage

from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

import os
import json
import shutil
import PIL.Image
import pandas as pd
import tkinter as tk

LARGE_FONT = ("Calibri", 12)

"""
------------------------------------------------------------------------------------------------------------------------
Processing Page(s) Section
------------------------------------------------------------------------------------------------------------------------
"""


class ProcessingPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.sw = ScrolledPage(self)

        label = ttk.Label(self.sw.scrollwindow, text="Processing Functions", font=LARGE_FONT)
        label.pack(ipady=5, padx=5, pady=5, expand=1)

        proc1_btn = ttk.Button(self.sw.scrollwindow, text="1/ Create the `batch-input` JSON file needed to execute "
                                                          "MegaDetector",
                               command=lambda: master.switch_frame("JSON Creator Page"))
        proc1_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        proc2_btn = ttk.Button(self.sw.scrollwindow, text="2/ Run MegaDetector using a `batch-input` JSON file as input"
                                                          ",\nsubsequently, a `mega-detected` JSON will be produced",
                               command=lambda: master.switch_frame("Run MegaDetector Page"))
        proc2_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        proc3_btn = ttk.Button(self.sw.scrollwindow,
                               text="3/ Convert the `mega-detected` JSON file into a `metadata` CSV file",
                               command=lambda: master.switch_frame("CSV Convertor Page"))
        proc3_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        proc4_btn = ttk.Button(self.sw.scrollwindow, text="4/ Sort the images into separate folders based on their "
                                                          "\n`mega-detected` classes using a `metadata` CSV file",
                               command=lambda: master.switch_frame("Image Sorter Page"))
        proc4_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)


"""
------------------------------------------------------------------------------------------------------------------------
JSON Creator Page
------------------------------------------------------------------------------------------------------------------------
"""


class JSONCreator(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.inputDirPath = None
        self.finalOutputDir = None

        inputDirButton = ttk.Button(self.sw.scrollwindow,
                                    text="1/ Please select an image folder which contains all the images "
                                         "that will be classified using MegaDetector are located in",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        jsonNameLabel = ttk.Label(self.sw.scrollwindow,
                                  text="2/ Please give a name to the `batch-input` JSON file that will be "
                                       "created from this process. Ideally, it should ends with "
                                       "`*_BatchInput.json`")
        jsonNameLabel.grid(row=2, sticky='')

        self.jsonNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.jsonNameEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        outputDirButton = ttk.Button(self.sw.scrollwindow, text="3/ Please select the `OUTPUT` folder where "
                                                                "the `batch-input` JSON file will be saved at",
                                     command=self.outputDir)
        outputDirButton.grid(row=4, ipadx=10, ipady=10, pady=8, sticky='')

        self.createJSONButton = ttk.Button(self.sw.scrollwindow, text="CREATE `BATCH-INPUT` JSON !!",
                                           command=self.createJSON)
        self.createJSONButton.grid(row=6, ipady=10, ipadx=10, pady=4, sticky='')

        util_btn = ttk.Button(self.sw.scrollwindow, text="Back To Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=8, ipady=10, ipadx=10, pady=4, sticky='')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipady=10, ipadx=10, pady=4, sticky='')

    def inputDir(self):
        inputDirectory = filedialog.askdirectory(title='Please select the image folder')
        self.inputDirPath = str(inputDirectory)

        inputDirLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED IMAGE FOLDER: \n' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=8, sticky='')

    def outputDir(self):
        outputDir = filedialog.askdirectory(title='Please select the folder where the `batch-input` JSON will be saved')
        outputDirPath = str(outputDir)

        jsonFilename = self.jsonNameEntry.get()

        self.finalOutputDir = os.path.join(outputDirPath, jsonFilename).replace("\\", "/")

        outputDirLabel = ttk.Label(self.sw.scrollwindow, text='OUTPUT `BATCH-INPUT` JSON: \n' + self.finalOutputDir)
        outputDirLabel.grid(row=5, pady=8, sticky='')

    def createJSON(self):
        """

        """
        self.createJSONButton.config(text="CREATING `BATCH-INPUT` JSON FILE, PLEASE WAIT ......")
        self.createJSONButton.update_idletasks()

        inputDir = self.inputDirPath
        outputDir = self.finalOutputDir

        ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

        files = []
        # p = path, d = dirs, f = files
        for p, d, f in os.walk(inputDir):
            for name in f:
                if name.endswith(ext):
                    files.append(os.path.join(p, name).replace("\\", "/"))

        with open(outputDir, 'w') as f:
            print(json.dump(files, f, indent=4))

            self.createJSONButton.config(text="THE `BATCH-INPUT` JSON WAS CREATED SUCCESSFULLY !!!"
                                              "\nPlease adjust the previous steps for the "
                                              "new run then CLICK this button to run again")

        return print("The `batch-input` JSON file was created successfully !!!")


"""
------------------------------------------------------------------------------------------------------------------------
Run MegaDetector Page
------------------------------------------------------------------------------------------------------------------------
"""


class RunMegaDetector(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.inputJSONPath = None
        self.outJSONPath = None

        inputJSONButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select a `batch-input` JSON file which "
                                                                "will be used to run MegaDetector batch-processing on",
                                     command=self.inputJSON)
        inputJSONButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        outJSONNameLabel = ttk.Label(self.sw.scrollwindow,
                                     text="2/ Please give a name to the resulted `mega-detected` JSON file."
                                          "Ideally it should be the\nsame as the `batch-input` JSON file but "
                                          "ends with `*_MegaDetected.json` instead")
        outJSONNameLabel.grid(row=2, sticky='')

        self.outJSONNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.outJSONNameEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        outputDirButton = ttk.Button(self.sw.scrollwindow, text="3/ Please select the `OUTPUT` folder where the "
                                                                "`mega-detected` JSON file will be saved at",
                                     command=self.outputJSON)
        outputDirButton.grid(row=4, ipadx=10, ipady=10, pady=8, sticky='')

        self.executeButton = ttk.Button(self.sw.scrollwindow, text="RUN MEGADETECTOR !!", command=self.runMD)
        self.executeButton.grid(row=6, ipady=10, ipadx=10, pady=4, sticky='')

        util_btn = ttk.Button(self.sw.scrollwindow, text="Back To Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=8, ipady=10, ipadx=10, pady=4, sticky='')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipady=10, ipadx=10, pady=4, sticky='')

    def inputJSON(self):
        inputJSON = filedialog.askopenfilename(title='Please select the image folder')
        self.inputJSONPath = str(inputJSON)

        inputJSONLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED IMAGE FOLDER: \n' + self.inputJSONPath)
        inputJSONLabel.grid(row=1, pady=8, sticky='')

    def outputJSON(self):
        outputDir = filedialog.askdirectory(title='Please select where the `mega-detected` JSON will be saved')
        outputDirPath = str(outputDir)

        outputJSONName = self.outJSONNameEntry.get()

        self.outJSONPath = os.path.join(outputDirPath, outputJSONName).replace("\\", "/")

        outputDirLabel = ttk.Label(self.sw.scrollwindow, text='OUTPUT `MEGA-DETECTED` JSON: \n' + self.outJSONPath)
        outputDirLabel.grid(row=5, pady=8, sticky='')

    def runMD(self):
        """

        """
        self.executeButton.config(text="MEGADETECTOR IS RUNNING, PLEASE WAIT ......")
        self.executeButton.update_idletasks()

        inputDir = str(self.inputJSONPath)
        outputDir = str(self.outJSONPath)

        exeMD = 'cd .. && cd cameratraps && ' \
                'python run_detector_batch.py md_v4.1.0.pb ' + inputDir + ' ' + outputDir + ' '

        if os.system(exeMD) == 0:
            self.executeButton.config(text="MEGADETECTOR WAS EXECUTED SUCCESSFULLY !!!"
                                           "\nPlease adjust the previous steps for the "
                                           "new run then CLICK this button to run again")
        else:
            self.executeButton.config(text="Error, please double check the commands !!")

        return print("MegaDetector was executed successfully !!!")


"""
------------------------------------------------------------------------------------------------------------------------
CSV Convertor Page
------------------------------------------------------------------------------------------------------------------------
"""


# Supporting function for CSVConvertor
def get_exif(source_images_path):
    """
    This function takes the original images as input and returns the exif cameratrap_data of the corresponding images.

    Parameters:
        source_images_path (str): the path of the images folder

    Returns:
        df_exif: A dataframe containing the exif cameratrap_data of the images in the given folder

    """
    lstDict = []
    ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

    for image_name in os.listdir(source_images_path):
        if image_name.endswith(ext):
            image = PIL.Image.open(os.path.join(source_images_path, image_name))
            exif = image.getexif()
            if exif is None:
                return
            exif_data = {'Image Name': image_name}
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        gps_tag = GPSTAGS.get(t, t)
                        gps_data[gps_tag] = value[t]
                    exif_data[tag] = gps_data
                else:
                    exif_data[tag] = value
            lstDict.append(exif_data)

    df_exif = pd.DataFrame.from_dict(lstDict)

    return df_exif


class CSVConvertor(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.inputDirPath = None
        self.jsonFilePath = None
        self.csvOutputDir = None

        inputDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select an image folder which has a "
                                                               "`mega-detected` JSON file associated with it",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        sessionNameLabel = ttk.Label(self.sw.scrollwindow,
                                     text="2/ What is the index order of the `SESSION NAME`, when the"
                                          "\nfolder-path displayed above is split with `/` as separator?")
        sessionNameLabel.grid(row=2, sticky='')

        self.sessionNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.sessionNameEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        stationNameLabel = ttk.Label(self.sw.scrollwindow,
                                     text="3/ What is the index order of the `STATION NAME`, when the"
                                          "\nfolder-path displayed above is split with `/` as separator?")
        stationNameLabel.grid(row=4, sticky='')

        self.stationNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.stationNameEntry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='')

        inputJSONButton = ttk.Button(self.sw.scrollwindow, text="4/ Please select the `mega-detected` JSON file "
                                                                "associated with the above-chosen image folder",
                                     command=self.inputJSON)
        inputJSONButton.grid(row=6, ipadx=10, ipady=10, pady=8, sticky='')

        csvNameLabel = ttk.Label(self.sw.scrollwindow,
                                 text="5/ Please give a name to the `metadata` CSV file. Ideally it should be"
                                      "\nthe same as the `mega-detected` JSON file but ends with `*_Meta.csv`")
        csvNameLabel.grid(row=8, sticky='')

        self.csvNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.csvNameEntry.grid(row=9, ipady=10, ipadx=10, pady=4, sticky='')

        outputDirButton = ttk.Button(self.sw.scrollwindow, text="6/ Please select the `OUTPUT` folder where "
                                                                "the `metadata` CSV file will be saved at",
                                     command=self.outputDir)
        outputDirButton.grid(row=10, ipadx=10, ipady=10, pady=8, sticky='')

        self.createCSVButton = ttk.Button(self.sw.scrollwindow, text="CREATE CSV `METADATA` FILE",
                                          command=self.convertCSV)
        self.createCSVButton.grid(row=12, ipady=10, ipadx=10, pady=4, sticky='')

        util_btn = ttk.Button(self.sw.scrollwindow, text="Back To Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=13, ipady=10, ipadx=10, pady=4, sticky='')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=14, ipady=10, ipadx=10, pady=4, sticky='')

    def inputDir(self):
        inputDirectory = filedialog.askdirectory(title='Please select the image folder')
        self.inputDirPath = str(inputDirectory)

        inputDirLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED IMAGE FOLDER: \n' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=8, sticky='')

    def inputJSON(self):
        jsonFile = filedialog.askopenfilename(title='Please select the `mega-detected` JSON file')
        self.jsonFilePath = str(jsonFile)

        jsonFileLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED `MEGA-DETECTED` JSON: \n' + self.jsonFilePath)
        jsonFileLabel.grid(row=7, pady=8, sticky='')

    def outputDir(self):
        outputDir = filedialog.askdirectory(title='Please select the folder where the CSV file will be saved at')
        outputDirPath = str(outputDir)

        csvFilename = self.csvNameEntry.get()

        self.csvOutputDir = os.path.join(outputDirPath, csvFilename).replace("\\", "/")

        outputDirLabel = ttk.Label(self.sw.scrollwindow, text='OUTPUT CSV FILE: \n' + self.csvOutputDir)
        outputDirLabel.grid(row=11, pady=8, sticky='')

    def convertCSV(self):
        """

        """
        self.createCSVButton.config(text="CREATING CSV `METADATA` FILE, PLEASE WAIT ......")
        self.createCSVButton.update_idletasks()

        input_json = open(self.jsonFilePath, 'r')
        json_info = json.load(input_json)

        df_exif = get_exif(self.inputDirPath)
        df_json = pd.DataFrame()

        sessionIndex = int(self.sessionNameEntry.get())
        stationIndex = int(self.stationNameEntry.get())

        for i in range(len(list(json_info['images']))):

            imageName = list(json_info['images'][i].values())[0].split('/')[-1]
            session = list(json_info['images'][i].values())[0].split('/')[sessionIndex]
            station = list(json_info['images'][i].values())[0].split('/')[stationIndex]

            imagePath = list(json_info['images'][i].values())[0]

            trigger = imageName[2:7]

            detection_box = list(json_info['images'][i].values())[2]
            bb_numbers = len(detection_box)

            pred_category, confidence, bb_locations, y_lower = [], [], [], []

            if bb_numbers != 0:
                for b in range(bb_numbers):
                    pred_category.append(list(detection_box[b].values())[0])
                    confidence.append(list(detection_box[b].values())[1])
                    bb_locations.append(list(detection_box[b].values())[2])
            else:
                pred_category.append('0')

            for loc in bb_locations:
                # y_lower.append(max(loc[3] for loc in bb_locations))
                y_lower.append(loc[3] + loc[1])

            y_lower = list(set(y_lower))

            data = imageName, trigger, station, session, str(bb_numbers), \
                   pred_category, confidence, bb_locations, y_lower, imagePath
            data = [list(data)]

            df_single = pd.DataFrame(data, columns=['Image Name', 'Trigger', 'Station', 'Session',
                                                    'Number of BBs', 'Predicted Category', 'Confidence',
                                                    'Location of BBs', 'Y Lower', 'Image Path'])

            df_json = pd.concat([df_json, df_single])

            df_final = pd.merge(df_exif[['Image Name', 'DateTime']], df_json, on='Image Name')

            df_final.to_csv(self.csvOutputDir, index=False)

            self.createCSVButton.config(text="THE CSV `METADATA` FILE WAS CREATED SUCCESSFULLY !!!"
                                             "\nPlease adjust the previous steps for the "
                                             "new run then CLICK this button to run again")

        return print("THE `metadata` CSV file was created successfully !!!")


"""
------------------------------------------------------------------------------------------------------------------------
Image Sorter Page
------------------------------------------------------------------------------------------------------------------------
"""


class ImageSorter(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.inputDirPath = None
        self.inputCSVPath = None

        inputDirButton = ttk.Button(self.sw.scrollwindow,
                                    text="1/ Please select the image folder which has an associated "
                                         "`metadata` CSV file, and this image\nfolder is also where you want "
                                         "the images inside it to be sorted by their `Mega-Detected` classes",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        inputCSVButton = ttk.Button(self.sw.scrollwindow,
                                    text="2/ Please select the `metadata` CSV file associated with "
                                         "the chosen image folder",
                                    command=self.inputCSV)
        inputCSVButton.grid(row=2, ipadx=10, ipady=10, pady=8, sticky='')

        sortedLabel = ttk.Label(self.sw.scrollwindow, text="3/ Sorted images to be saved in a separate "
                                                           "`*_Sorted` directory (`Y` or `N`)? ")
        sortedLabel.grid(row=4, sticky='')

        self.sortedEntry = ttk.Entry(self.sw.scrollwindow)
        self.sortedEntry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='')

        self.sortButton = ttk.Button(self.sw.scrollwindow, text="START SORTING IMAGES !!", command=self.sortImages)
        self.sortButton.grid(row=6, ipady=10, ipadx=10, pady=4, sticky='')

        util_btn = ttk.Button(self.sw.scrollwindow, text="Back To Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=7, ipady=10, ipadx=10, pady=4, sticky='')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=8, ipady=10, ipadx=10, pady=4, sticky='')

    def inputDir(self):
        inputDir = filedialog.askdirectory(title='Please select the image folder')
        self.inputDirPath = str(inputDir)

        inputDirLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED IMAGE FOLDER: \n' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=8, sticky='')

    def inputCSV(self):
        inputCSV = filedialog.askopenfilename(title='Please select CSV `metadata` file')
        self.inputCSVPath = str(inputCSV)

        inputCSVLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED CSV FILE: \n' + self.inputCSVPath)
        inputCSVLabel.grid(row=3, pady=8, sticky='')

    def sortImages(self):
        """

        """
        global predclass

        self.sortButton.config(text="IMAGES ARE BEING SORTED, PLEASE WAIT ......")
        self.sortButton.update_idletasks()

        inputDir = self.inputDirPath
        inputCSV = self.inputCSVPath
        sortedInput = str(self.sortedEntry.get())

        old_path = []  # Old - full original paths of where the image files are currently stored
        parent_path = []  # First half of the o_path (parent path) without the image name
        parent_path_sorted = []

        ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

        for root, dirs, files in os.walk(inputDir):
            for fname in files:
                if fname.endswith(ext):
                    org_path = os.path.join(root, fname)
                    org_path = os.path.normpath(org_path)
                    old_path.append(org_path)

                    p_path = os.path.split(org_path)[0]
                    p_path = os.path.normpath(p_path)
                    parent_path.append(p_path)

        csv_file = pd.read_csv(inputCSV)
        df_csv = pd.DataFrame(csv_file)

        classified_folder = []  # Classified categories of each image

        list_numbbs = df_csv['Number of BBs'].tolist()
        list_predcategory = df_csv['Predicted Category'].tolist()

        for num_bbs, category in zip(list_numbbs, list_predcategory):
            if num_bbs > 1:
                checking = all(element == category[0] for element in category)
                if checking:
                    print("Same category for all bounding boxes")
                else:
                    predclass = 'Assistant Required'
            else:
                if '0' in category:
                    predclass = 'Empty'
                elif '1' in category:
                    predclass = 'Animal'
                elif '2' in category:
                    predclass = 'Person'
                elif '3' in category:
                    predclass = 'Vehicle'
                else:
                    predclass = None
            classified_folder.append(predclass)

        new_path = []  # New - new path where the image files will be move to
        new_path_sorted = []

        for i in parent_path:
            new_parent_path = i + '_Sorted'
            parent_path_sorted.append(new_parent_path)

        if sortedInput == 'Y':
            for ps, ss in zip(parent_path_sorted, classified_folder):
                new_img_path_sorted = os.path.join(ps, ss)
                new_img_path_sorted = os.path.normpath(new_img_path_sorted)
                os.makedirs(new_img_path_sorted, exist_ok=True) if not os.path.exists(new_img_path_sorted) else None
                new_path_sorted.append(new_img_path_sorted)

            # Make copy of the image and sorted them in categories
            for o, ns in zip(old_path, new_path_sorted):
                shutil.copy(o, ns)

            self.sortButton.config(text="THE IMAGES WERE SORTED SUCCESSFULLY !!!"
                                        "\nPlease adjust the previous steps for the "
                                        "new run then CLICK this button to run again")

        elif sortedInput == 'N':
            for p, s in zip(parent_path, classified_folder):
                new_img_path = os.path.join(p, s)
                new_img_path = os.path.normpath(new_img_path)
                os.makedirs(new_img_path, exist_ok=True) if not os.path.exists(new_img_path) else None
                new_path.append(new_img_path)

            # Make copy of the image and sorted them in categories
            for o, n in zip(old_path, new_path):
                shutil.copy(o, n)

            self.sortButton.config(text="THE IMAGES WERE SORTED SUCCESSFULLY !!!"
                                        "\nPlease adjust the previous steps for the "
                                        "new run then CLICK this button to run again")

        else:
            self.sortButton.config(text="Error !! Please re-check the input for the previous steps")

            print("\nWrong choice, please re-run the script and follow the instructions !!!"
                  "\n")

        return print("The images were sorted successfully !!!")


if __name__ == "__main__":
    page = ProcessingPage()
    page.mainloop()
