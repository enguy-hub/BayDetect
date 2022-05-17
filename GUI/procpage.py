import tkinter as tk
from tkinter import Tk, Frame, ttk

from tkinter import filedialog

import os
import time
import json
import PIL.Image
import pandas as pd

from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

LARGE_FONT = ("Calibri", 12)


"""
------------------------------------------------------------------------------------------------------------------------
Processing Page(s) Section
------------------------------------------------------------------------------------------------------------------------
"""


class ProcessingPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = ttk.Label(self, text="Processing Functions", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        proc1_btn = ttk.Button(self, text="Create the `*_BatchInput.json` file needed to execute MegaDetector",
                               command=lambda: master.switch_frame("JSON Creator Page"))
        proc1_btn.pack(ipadx=5, ipady=5, expand=1)

        proc2_btn = ttk.Button(self, text="Execute MegaDetector to create the `*_MegaDetected.json` file",
                               command=lambda: master.switch_frame("Run MegaDetector Page"))
        proc2_btn.pack(ipadx=5, ipady=5, expand=1)

        proc3_btn = ttk.Button(self, text="Convert the `*_MegaDetected.json` file into a `*_Metadata.csv` file",
                               command=lambda: master.switch_frame("CSV Convertor Page"))
        proc3_btn.pack(ipadx=5, ipady=5, expand=1)

        proc4_btn = ttk.Button(self, text="Sort the images into separate folders based on their "
                                          "\n`MEGA`-detected classes using the `*_Metadata.csv` file",
                               command=lambda: master.switch_frame("ProcessingPage"))
        proc4_btn.pack(ipadx=5, ipady=5, expand=1)

        home_btn = ttk.Button(self, text="Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=5, ipady=5, expand=1)

        quit_btn = ttk.Button(self, text="Quit",
                              command=lambda: self.quit())
        quit_btn.pack(ipadx=5, ipady=5, expand=1)


"""
------------------------------------------------------------------------------------------------------------------------
JSON Creator Page
------------------------------------------------------------------------------------------------------------------------
"""


class JSONCreator(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.inputDirPath = None
        self.finalOutputDir = None

        inputDirButton = ttk.Button(self, text="Please select the `INPUT` image directory which contains all "
                                               "\nthe images that you would like to run MegaDetector on",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, sticky='')

        jsonNameLabel = ttk.Label(self, text="Please give a name for the JSON file which will be created "
                                             "\nfrom this process (e.g: end with `*_BatchInput.json`)")
        jsonNameLabel.grid(row=2, sticky='')

        self.jsonNameEntry = ttk.Entry(self)
        self.jsonNameEntry.grid(row=3, ipady=5, ipadx=5, sticky='')

        outputDirButton = ttk.Button(self, text="Please select the `OUTPUT` directory for which the `*_BatchInput.json`"
                                                "\nfile created from this process will be saved at",
                                     command=self.outputDir)
        outputDirButton.grid(row=4, ipadx=10, ipady=10, sticky='')

        self.createJSONButton = ttk.Button(self, text="Create `*_BatchInput.json` file !!", command=self.createJSON)
        self.createJSONButton.grid(row=6, ipady=5, ipadx=5, sticky='')

        util_btn = ttk.Button(self, text="Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=8, ipady=5, ipadx=5, pady=10, sticky='')

        home_btn = ttk.Button(self, text="Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipady=5, ipadx=5, sticky='')

    def inputDir(self):
        inputDirectory = filedialog.askdirectory(title='Please select a directory')
        self.inputDirPath = str(inputDirectory)

        inputDirLabel = ttk.Label(self, text='INPUT IMAGE DIRECTORY: \n' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=10, sticky='')

    def outputDir(self):
        outputDir = filedialog.askdirectory(title='Please select a directory')
        outputDirPath = str(outputDir)

        jsonFilename = self.jsonNameEntry.get()

        self.finalOutputDir = os.path.join(outputDirPath, jsonFilename).replace("\\", "/")

        outputDirLabel = ttk.Label(self, text='OUTPUT DIRECTORY AND JSON FILENAME: \n' + self.finalOutputDir)
        outputDirLabel.grid(row=5, pady=10, sticky='')

    def createJSON(self):
        """

        """
        self.createJSONButton.config(text="Creating `*_BatchInput.json` file, please wait ......")
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

            self.createJSONButton.config(text="`*_BatchInput.json` file created successfully, click "
                                              "this button to create another `*_BatchInput.json` file")

        return print("`*_BatchInput.json` file created successfully !!!")


"""
------------------------------------------------------------------------------------------------------------------------
Run MegaDetector Page
------------------------------------------------------------------------------------------------------------------------
"""


class RunMegaDetector(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.inputJSONPath = None
        self.outJSONPath = None

        inputJSONButton = ttk.Button(self, text="Please select the `*_BatchInput.json` file that you"
                                                "\nwould like to run MegaDetector batch-processing on",
                                     command=self.inputJSON)
        inputJSONButton.grid(row=0, ipadx=10, ipady=10, sticky='')

        outJSONNameLabel = ttk.Label(self, text="Please give a name for the resulted JSON file from MegaDetector. "
                                                "Ideally it should be\nthe same as the`*_BatchInput.json` file "
                                                "but ends with `*_MegaDetected.json`")
        outJSONNameLabel.grid(row=2, sticky='')

        self.outJSONNameEntry = ttk.Entry(self)
        self.outJSONNameEntry.grid(row=3, ipady=5, ipadx=5, sticky='')

        outputDirButton = ttk.Button(self, text="Please select the `OUTPUT` directory for which"
                                                "\nthe `*_MegaDetected.json` file will be saved at",
                                     command=self.outputJSON)
        outputDirButton.grid(row=4, ipadx=10, ipady=10, sticky='')

        self.executeButton = ttk.Button(self, text="Execute MegaDetector !!", command=self.runMD)
        self.executeButton.grid(row=6, ipady=5, ipadx=5, sticky='')

        util_btn = ttk.Button(self, text="Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=8, ipady=5, ipadx=5, pady=10, sticky='')

        home_btn = ttk.Button(self, text="Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipady=5, ipadx=5, sticky='')

    def inputJSON(self):
        inputJSON = filedialog.askopenfilename(title='Please select a directory')
        self.inputJSONPath = str(inputJSON)

        inputJSONLabel = ttk.Label(self, text='INPUT IMAGE DIRECTORY: \n' + self.inputJSONPath)
        inputJSONLabel.grid(row=1, pady=10, sticky='')

    def outputJSON(self):
        outputDir = filedialog.askdirectory(title='Please select a directory')
        outputDirPath = str(outputDir)

        outputJSONName = self.outJSONNameEntry.get()

        self.outJSONPath = os.path.join(outputDirPath, outputJSONName).replace("\\", "/")

        outputDirLabel = ttk.Label(self, text='OUTPUT DIRECTORY AND JSON FILENAME: \n' + self.outJSONPath)
        outputDirLabel.grid(row=5, pady=10, sticky='')

    def runMD(self):
        """

        """
        self.executeButton.config(text="MegaDetector is running, please wait ......")
        self.executeButton.update_idletasks()

        inputDir = str(self.inputJSONPath)
        outputDir = str(self.outJSONPath)

        exeMD = 'cd .. && cd cameratraps && ' \
                'python run_detector_batch.py md_v4.1.0.pb ' + inputDir + ' ' + outputDir + ' '

        if os.system(exeMD) == 0:
            self.executeButton.config(text="Executed MegaDetector successfully !! Click this "
                                           "button to execute MegaDetector again")
        else:
            self.executeButton.config(text="Error, please double check the commands !!")

        return print("Executed MegaDetector successfully !!!")


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
    lst_dict = []
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
            lst_dict.append(exif_data)

    df_exif = pd.DataFrame.from_dict(lst_dict)

    return df_exif


class CSVConvertor(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.inputDirPath = None
        self.jsonFilePath = None
        self.csvOutputDir = None

        inputDirButton = ttk.Button(self, text="Please select the `INPUT` image directory which "
                                               "\nyou have a `*_MegaDetected.json` file for",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, sticky='')

        sessionNameLabel = ttk.Label(self, text="When the above directory path is split with `/` as separator, what is "
                                                "the index order of the `SESSION NAME`?")
        sessionNameLabel.grid(row=2, sticky='')

        self.sessionNameEntry = ttk.Entry(self)
        self.sessionNameEntry.grid(row=3, ipady=5, ipadx=5, sticky='')

        stationNameLabel = ttk.Label(self, text="When the above directory path is split with `/` as separator, what is "
                                                "the index order of the `STATION NAME`?")
        stationNameLabel.grid(row=4, sticky='')

        self.stationNameEntry = ttk.Entry(self)
        self.stationNameEntry.grid(row=5, ipady=5, ipadx=5, sticky='')

        inputJSONButton = ttk.Button(self, text="Please select the `*_MegaDetected.json` file which "
                                                "\ncorrespond to the `INPUT` image folder selected above",
                                     command=self.jsonFile)
        inputJSONButton.grid(row=6, ipadx=10, ipady=10, sticky='')

        csvNameLabel = ttk.Label(self, text="Please give a name for the CSV metadata file. Ideally should be the"
                                            "\nsame as the `*_MegaDetected.json` file but ends with `*_Meta.csv`")
        csvNameLabel.grid(row=8, sticky='')

        self.csvNameEntry = ttk.Entry(self)
        self.csvNameEntry.grid(row=9, ipady=5, ipadx=5, sticky='')

        outputDirButton = ttk.Button(self, text="Please select the `OUTPUT` directory where "
                                                "\nthe `*_Meta.csv` file will be saved at",
                                     command=self.outputDir)
        outputDirButton.grid(row=10, ipadx=10, ipady=10, sticky='')

        self.createCSVButton = ttk.Button(self, text="Create `*_Meta.csv` file", command=self.convertCSV)
        self.createCSVButton.grid(row=12, ipady=5, ipadx=5, sticky='')

        util_btn = ttk.Button(self, text="Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=13, ipady=5, ipadx=5, pady=10, sticky='')

        home_btn = ttk.Button(self, text="Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=14, ipady=5, ipadx=5, sticky='')

    def inputDir(self):
        inputDirectory = filedialog.askdirectory(title='Please select a directory')
        self.inputDirPath = str(inputDirectory)

        inputDirLabel = ttk.Label(self, text='INPUT IMAGE DIRECTORY: \n' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=10, sticky='')

    def jsonFile(self):
        jsonFile = filedialog.askopenfilename(title='Please select the JSON file')
        self.jsonFilePath = str(jsonFile)

        jsonFileLabel = ttk.Label(self, text='JSON PATH: \n' + self.jsonFilePath)
        jsonFileLabel.grid(row=7, pady=10, sticky='')

    def outputDir(self):
        outputDir = filedialog.askdirectory(title='Please select a directory')
        outputDirPath = str(outputDir)

        csvFilename = self.csvNameEntry.get()

        self.csvOutputDir = os.path.join(outputDirPath, csvFilename).replace("\\", "/")

        outputDirLabel = ttk.Label(self, text='OUTPUT DIRECTORY AND CSV FILENAME: \n' + self.csvOutputDir)
        outputDirLabel.grid(row=11, pady=10, sticky='')

    def convertCSV(self):
        """

        """
        self.createCSVButton.config(text="Creating `*_Meta.csv` file, please wait ......")
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

            self.createCSVButton.config(text="`*_Meta.csv` file created successfully, click "
                                             "this button to create another `*_Meta.csv` file")

        return print("`*_Meta.csv` file created successfully !!!")


if __name__ == "__main__":
    app = ProcessingPage()
    app.mainloop()
