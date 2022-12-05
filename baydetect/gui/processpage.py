from tkinter import ttk, filedialog
from baydetect.gui.scrollpage import ScrolledPage

from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

import os
import ast
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

        proc1_btn = ttk.Button(self.sw.scrollwindow, text="1/ Create the `BatchInput` JSON "
                                                          "file needed to execute MegaDetector",
                               command=lambda: master.switch_frame("JSON Creator Page"))
        proc1_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        proc2_btn = ttk.Button(self.sw.scrollwindow, text="2/ Run MegaDetector using a `BatchInput` JSON file as input"
                                                          "\nsubsequently, a `MegaDetected` JSON file will be produced",
                               command=lambda: master.switch_frame("Run MegaDetector Page"))
        proc2_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        proc3_btn = ttk.Button(self.sw.scrollwindow,
                               text="3/ Convert the `MegaDetected` JSON file into a CSV `Metadata` file",
                               command=lambda: master.switch_frame("CSV Convertor Page"))
        proc3_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        proc4_btn = ttk.Button(self.sw.scrollwindow, text="4/ Sort the images into separate folders based on their "
                                                          "\n`MegaDetected` classes using a CSV `Metadata` file",
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

        self.rootDir = os.path.abspath(os.curdir)
        self.inputDirPath = None
        self.finalOutputDir = None

        # To destroy later
        self.inputDirLabel = None
        self.outputDirLabel = None

        inputDirButton = ttk.Button(self.sw.scrollwindow,
                                    text="1/ Please select an IMAGE FOLDER which you "
                                         "want to create the `BatchInput` JSON file for",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        jsonNameLabel = ttk.Label(self.sw.scrollwindow,
                                  text="2/ Please give a name to the `BatchInput` JSON "
                                       "file. Ideally, it should ends with `*_BI.json`")
        jsonNameLabel.grid(row=2, sticky='')

        self.jsonNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.jsonNameEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        outputDirButton = ttk.Button(self.sw.scrollwindow, text="3/ Please select the output folder where "
                                                                "the `BatchInput` JSON file will be saved at",
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
        inputDirectory = filedialog.askdirectory(initialdir=self.rootDir + "/image_data",
                                                 title='Please select the image folder')
        self.inputDirPath = str(inputDirectory) + "/"

        self.inputDirLabel = tk.Text(self.sw.scrollwindow, height=2, width=100, borderwidth=0)
        self.inputDirLabel.tag_configure("tag_name", justify='center')
        self.inputDirLabel.insert("2.0", "FOLDER PATH: " + str(inputDirectory))
        self.inputDirLabel.tag_add("tag_name", "2.0", "end")
        self.inputDirLabel.grid(row=1, pady=8, sticky='n')

        self.inputDirLabel.configure(state="disabled")
        self.inputDirLabel.configure(inactiveselectbackground=self.inputDirLabel.cget("selectbackground"))

    def outputDir(self):
        outputDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                            title='Please select the folder where the `BatchInput` JSON will be saved')
        outputDirPath = str(outputDir) + "/"

        jsonFilename = self.jsonNameEntry.get()

        self.finalOutputDir = os.path.join(outputDirPath, jsonFilename).replace("\\", "/")

        self.outputDirLabel = ttk.Label(self.sw.scrollwindow, text='OUTPUT `BATCH-INPUT` JSON: \n' +
                                                                   str(outputDir) + "/")
        self.outputDirLabel.grid(row=5, pady=8, sticky='')

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
                imgPath = str(os.path.join(inputDir, name))
                imgStat = os.stat(imgPath).st_size

                if name.endswith(ext) and imgStat == 0:
                    print("\nThe following image is broken and not included in the JSON list:")
                    print(name + "\n")
                    continue
                else:
                    files.append(os.path.join(p, name).replace("\\", "/"))

        with open(outputDir, 'w') as f:
            print(json.dump(files, f, indent=4))

            self.createJSONButton.config(text="CREATED `BATCH-INPUT` JSON SUCCESSFULLY !!!"
                                              "\nPlease adjust the steps for the new "
                                              "run then CLICK this button to run again")
            self.jsonNameEntry.delete(0, 'end')

            # Destroy
            self.inputDirLabel.destroy()
            self.outputDirLabel.destroy()

        return print("Created `BatchInput` JSON file successfully !!!")


"""
------------------------------------------------------------------------------------------------------------------------
Run MegaDetector Page
------------------------------------------------------------------------------------------------------------------------
"""


class RunMegaDetector(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.rootDir = os.path.abspath(os.curdir)
        self.inputJSONPath = None
        self.outJSONPath = None

        # To destroy later
        self.inputJSONLabel = None
        self.outputDirLabel = None

        inputJSONButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select a `BatchInput` JSON file",
                                     command=self.inputJSON)
        inputJSONButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        outJSONNameLabel = ttk.Label(self.sw.scrollwindow,
                                     text="2/ Please give a name to the output `MegaDetected` JSON file."
                                          "Ideally it should be the\nsame as the `BatchInput` JSON file but "
                                          "ends with `*_MD.json` instead")
        outJSONNameLabel.grid(row=2, sticky='')

        self.outJSONNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.outJSONNameEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        outputDirButton = ttk.Button(self.sw.scrollwindow, text="3/ Please select the output folder where the "
                                                                "`MegaDetected` JSON file will be saved at",
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
        inputJSON = filedialog.askopenfilename(initialdir=self.rootDir + "/metadata",
                                               title='Please select the `BatchInput` JSON file')
        self.inputJSONPath = str(inputJSON)

        self.inputJSONLabel = tk.Text(self.sw.scrollwindow, height=2, width=100, borderwidth=0)
        self.inputJSONLabel.tag_configure("tag_name", justify='center')
        self.inputJSONLabel.insert("2.0", "`BI` JSON PATH: " + str(inputJSON))
        self.inputJSONLabel.tag_add("tag_name", "2.0", "end")
        self.inputJSONLabel.grid(row=1, pady=8, sticky='n')

        self.inputJSONLabel.configure(state="disabled")
        self.inputJSONLabel.configure(inactiveselectbackground=self.inputJSONLabel.cget("selectbackground"))

    def outputJSON(self):
        outputDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                            title='Please select the output folder for the `MegaDetected` JSON file')
        outputDirPath = str(outputDir) + "/"

        outputJSONName = self.outJSONNameEntry.get()

        self.outJSONPath = os.path.join(outputDirPath, outputJSONName).replace("\\", "/")

        self.outputDirLabel = ttk.Label(self.sw.scrollwindow, text='Output `MegaDetected` JSON: \n' + outputDirPath)
        self.outputDirLabel.grid(row=5, pady=8, sticky='')

    def runMD(self):
        """

        """
        self.executeButton.config(text="MEGADETECTOR IS RUNNING, PLEASE WAIT ......")
        self.executeButton.update_idletasks()

        inputDir = str(self.inputJSONPath)
        outputDir = str(self.outJSONPath)

        exeMD = 'cd cameratraps/detection ' \
                '&& ' \
                'python run_detector_batch.py md_v5a.0.0.pt ' \
                + inputDir + ' ' \
                + outputDir + ' '
        # '--output_relative_filenames --recursive ' #  --checkpoint_frequency 10000'

        if os.system(exeMD) == 0:
            self.executeButton.config(text="MEGADETECTOR WAS EXECUTED SUCCESSFULLY !!!"
                                           "\nPlease adjust the previous steps for the "
                                           "new run then CLICK this button to run again")
            self.outJSONNameEntry.delete(0, 'end')

            self.inputJSONLabel.destroy()
            self.outputDirLabel.destroy()

        else:
            self.executeButton.config(text="Error, please double check the commands !!")

        return print("MegaDetector was executed successfully !!!")


"""
------------------------------------------------------------------------------------------------------------------------
CSV Convertor Page
------------------------------------------------------------------------------------------------------------------------
"""


# Supporting function for CSVConvertor
def get_exif(input_imageDir):
    """
    This function takes the original images as input and returns the exif cameratrap_data of the corresponding images.

    Parameters:
        input_imageDir (str): the path of the images folder

    Returns:
        df_exif: A dataframe containing the exif cameratrap_data of the images in the given folder

    """
    lstDict = []
    ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

    for image_name in os.listdir(input_imageDir):
        imgPath = str(os.path.join(input_imageDir, image_name))
        # print(imgPath)
        imgStat = os.stat(imgPath).st_size
        # print(imgStat)

        if image_name.endswith(ext) and imgStat == 0:
            print("\nThe following image is broken:")
            print(image_name)
            continue

        else:
            image = PIL.Image.open(imgPath)
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

    # df_exif = pd.DataFrame.from_dict(lstDict)
    df_exif = pd.DataFrame(lstDict)

    return df_exif


class CSVConvertor(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.rootDir = os.path.abspath(os.curdir)
        self.inputDirPath = None
        self.jsonFilePath = None
        self.csvOutputDir = None
        self.org_img_dirpath = []

        # To destroy later
        self.outputDirLabel = None
        self.jsonFileLabel = None
        self.inputDirLabel = None

        inputDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select the IMAGE FOLDER that has a "
                                                               "`MegaDetected` JSON file 'associated' with it",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        sessionNameLabel = ttk.Label(self.sw.scrollwindow,
                                     text="2/ Which index is the `Session` in the above image "
                                          "\npath when it is split with `/` as separator?")
        sessionNameLabel.grid(row=2, sticky='')

        self.sessionNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.sessionNameEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        stationNameLabel = ttk.Label(self.sw.scrollwindow,
                                     text="3/ Which index is the `Station` in the above image "
                                          "\npath when it is split with `/` as separator?")
        stationNameLabel.grid(row=4, sticky='')

        self.stationNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.stationNameEntry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='')

        inputJSONButton = ttk.Button(self.sw.scrollwindow, text="4/ Please select the `MegaDetected` JSON file "
                                                                "associated with the above image folder",
                                     command=self.inputJSON)
        inputJSONButton.grid(row=6, ipadx=10, ipady=10, pady=8, sticky='')

        csvNameLabel = ttk.Label(self.sw.scrollwindow,
                                 text="5/ Please give a name to the CSV `Metadata` file. Ideally it should be"
                                      "\nthe same as the `MegaDetected` JSON file but ends with `*_Meta.csv`")
        csvNameLabel.grid(row=8, sticky='')

        self.csvNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.csvNameEntry.grid(row=9, ipady=10, ipadx=10, pady=4, sticky='')

        outputDirButton = ttk.Button(self.sw.scrollwindow, text="6/ Please select the output folder where "
                                                                "the CSV `Metadata` file will be saved at",
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
        inputDirectory = filedialog.askdirectory(initialdir=self.rootDir + "/image_data",
                                                 title='Please select the image folder')
        self.inputDirPath = str(inputDirectory) + "/"

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for file in files:
                self.org_img_dirpath.append(os.path.join(path, file).replace("\\", "/"))

        self.inputDirLabel = tk.Text(self.sw.scrollwindow, height=2, width=100, borderwidth=0)
        self.inputDirLabel.tag_configure("tag_name", justify='center')
        self.inputDirLabel.insert("2.0", "FIRST IMAGE: " + self.org_img_dirpath[0])
        self.inputDirLabel.tag_add("tag_name", "2.0", "end")
        self.inputDirLabel.grid(row=1, pady=8, sticky='n')

        self.inputDirLabel.configure(state="disabled")
        self.inputDirLabel.configure(inactiveselectbackground=self.inputDirLabel.cget("selectbackground"))

    def inputJSON(self):
        jsonFile = filedialog.askopenfilename(initialdir=self.rootDir + "/metadata",
                                              title='Please select the `MegaDetected` JSON file')
        self.jsonFilePath = str(jsonFile)

        self.jsonFileLabel = tk.Text(self.sw.scrollwindow, height=2, width=100, borderwidth=0)
        self.jsonFileLabel.tag_configure("tag_name", justify='center')
        self.jsonFileLabel.insert("2.0", "`MD` JSON PATH: " + self.jsonFilePath)
        self.jsonFileLabel.tag_add("tag_name", "2.0", "end")
        self.jsonFileLabel.grid(row=7, pady=8, sticky='n')

        self.jsonFileLabel.configure(state="disabled")
        self.jsonFileLabel.configure(inactiveselectbackground=self.jsonFileLabel.cget("selectbackground"))

    def outputDir(self):
        outputDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                            title='Please select the output folder for '
                                                  'which the CSV file will be saved at')
        outputDirPath = str(outputDir) + "/"

        csvFilename = self.csvNameEntry.get()

        self.csvOutputDir = os.path.join(outputDirPath, csvFilename).replace("\\", "/")

        self.outputDirLabel = ttk.Label(self.sw.scrollwindow, text='OUTPUT CSV FILE: \n' + self.csvOutputDir)
        self.outputDirLabel.grid(row=11, pady=8, sticky='')

    def convertCSV(self):
        self.createCSVButton.config(text="CREATING CSV `METADATA` FILE, PLEASE WAIT ......")
        self.createCSVButton.update_idletasks()

        input_json = open(self.jsonFilePath, 'r')
        json_info = json.load(input_json)

        sampleImagePath = list(json_info['images'][0].values())[0]
        # imgDir = os.path.dirname(sampleImagePath)  # get path only
        # print(imgDir)

        print("\nSample path to the FIRST image: \n" + sampleImagePath)

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

            valLength = len(list(json_info['images'][i].values()))

            if valLength == 3:

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

            elif valLength != 3:
                print("\nThe following image is broken: ")
                print(imagePath)
                continue

            self.createCSVButton.config(text="CREATED CSV `METADATA` FILE SUCCESSFULLY !!!"
                                             "\nPlease adjust the steps for the new "
                                             "run then CLICK this button to run again")
            self.csvNameEntry.delete(0, 'end')
            self.sessionNameEntry.delete(0, 'end')
            self.stationNameEntry.delete(0, 'end')

            # Destroy
            self.org_img_dirpath.clear()
            self.inputDirLabel.destroy()
            self.outputDirLabel.destroy()
            self.jsonFileLabel.destroy()

        return print("Created `Metadata` CSV file successfully !!!")


"""
------------------------------------------------------------------------------------------------------------------------
Image Sorter Page
------------------------------------------------------------------------------------------------------------------------
"""


class ImageSorter(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.rootDir = os.path.abspath(os.curdir)
        self.inputDirPath = None
        self.inputCSVPath = None

        # To destroy
        self.inputCSVLabel = None
        self.inputDirLabel = None

        inputDirButton = ttk.Button(self.sw.scrollwindow,
                                    text="1/ Please select the IMAGE FOLDER with an associated `Metadata` CSV file",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        inputCSVButton = ttk.Button(self.sw.scrollwindow,
                                    text="2/ Please select the CSV `Metadata` file",
                                    command=self.inputCSV)
        inputCSVButton.grid(row=2, ipadx=10, ipady=10, pady=8, sticky='')

        sortedLabel = ttk.Label(self.sw.scrollwindow, text="3/ Do you want the sorted images to be saved in "
                                                           "a separate `*_Sorted` directory (`Y` or `N`)? ")
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
        inputDir = filedialog.askdirectory(initialdir=self.rootDir + "/image_data",
                                           title='Please select the image folder')
        self.inputDirPath = str(inputDir) + "/"

        self.inputDirLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED IMAGE FOLDER: \n' + self.inputDirPath)
        self.inputDirLabel.grid(row=1, pady=8, sticky='')

    def inputCSV(self):
        inputCSV = filedialog.askopenfilename(initialdir=self.rootDir + "/metadata",
                                              title='Please select the CSV `metadata` file')
        self.inputCSVPath = str(inputCSV)

        self.inputCSVLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED CSV FILE: \n' + self.inputCSVPath)
        self.inputCSVLabel.grid(row=3, pady=8, sticky='')

    def sortImages(self):
        """

        """
        self.sortButton.config(text="IMAGES ARE BEING SORTED, PLEASE WAIT ......")
        self.sortButton.update_idletasks()

        img_input_dir = self.inputDirPath
        inputCSV = self.inputCSVPath
        sortedInput = str(self.sortedEntry.get())

        org_imgPath = []  # Old - full original paths of where the image files are currently stored
        parent_imgPath = []  # First half of the o_path (parent path) without the image name
        parent_imgPath_sorted = []

        ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

        for image_name in os.listdir(img_input_dir):
            imgPath = str(os.path.join(img_input_dir, image_name))
            imgStat = os.stat(imgPath).st_size

            if image_name.endswith(ext) and imgStat == 0:
                print("\nThe following image is broken and not included in the sorting:")
                print(image_name)
                continue
            else:
                org_imgPath.append(imgPath)

        org_imgPath.sort()

        for p in org_imgPath:
            p_path = os.path.split(p)[0]
            p_path = os.path.normpath(p_path)
            parent_imgPath.append(p_path)

        csv_file = pd.read_csv(inputCSV)
        df_csv = pd.DataFrame(csv_file)

        classified_folder = []  # Classified categories of each image

        list_numbbs = df_csv['Number of BBs'].tolist()
        list_predcategory = df_csv['Predicted Category'].tolist()
        intList_predcategory = [list(map(int, ast.literal_eval(i))) for i in list_predcategory]
        # print(intList_predcategory)

        predclass = None

        for num_bbs, category in zip(list_numbbs, intList_predcategory):
            if num_bbs > 1:
                checking = all(element == category[0] for element in category)
                if checking:
                    # print("All bounding boxes have the same category")
                    # print(category)
                    if category[0] == 1:
                        predclass = 'Animal'
                    elif category[0] == 2:
                        predclass = 'Person'
                    elif category[0] == 3:
                        predclass = 'Vehicle'
                else:
                    # print("More than one class detected among the bounding boxes --> Assistant required")
                    predclass = 'Assistant Required'
            else:
                # print(category)
                if category[0] == 0:
                    predclass = 'Empty'
                elif category[0] == 1:
                    predclass = 'Animal'
                elif category[0] == 2:
                    predclass = 'Person'
                elif category[0] == 3:
                    predclass = 'Vehicle'
                else:
                    predclass = None
            classified_folder.append(predclass)

        new_path = []  # New - new path where the image files will be moved to
        new_path_sorted = []

        for i in parent_imgPath:
            new_parent_path = i + '_Sorted'
            parent_imgPath_sorted.append(new_parent_path)

        if sortedInput == 'Y':
            for ps, ss in zip(parent_imgPath_sorted, classified_folder):
                new_img_path_sorted = os.path.join(ps, ss)
                new_img_path_sorted = os.path.normpath(new_img_path_sorted)
                os.makedirs(new_img_path_sorted, exist_ok=True) if not os.path.exists(new_img_path_sorted) else None
                new_path_sorted.append(new_img_path_sorted)

            # Make copy of the image and sorted them in categories
            for o, ns in zip(org_imgPath, new_path_sorted):
                shutil.copy(o, ns)

            self.sortButton.config(text="THE IMAGES WERE SORTED SUCCESSFULLY !!!"
                                        "\nPlease adjust the previous steps for the "
                                        "new run then CLICK this button to run again")
            self.sortedEntry.delete(0, 'end')
            self.inputCSVLabel.destroy()
            self.inputDirLabel.destroy()

        elif sortedInput == 'N':
            for p, s in zip(parent_imgPath, classified_folder):
                new_img_path = os.path.join(p, s)
                new_img_path = os.path.normpath(new_img_path)
                os.makedirs(new_img_path, exist_ok=True) if not os.path.exists(new_img_path) else None
                new_path.append(new_img_path)

            # Make copy of the image and sorted them in categories
            for o, n in zip(org_imgPath, new_path):
                shutil.move(o, n)

            self.sortButton.config(text="THE IMAGES WERE SORTED SUCCESSFULLY !!!"
                                        "\nPlease adjust the previous steps for the "
                                        "new run then CLICK this button to run again")
            self.sortedEntry.delete(0, 'end')
            self.inputCSVLabel.destroy()
            self.inputDirLabel.destroy()

        else:
            self.sortButton.config(text="Error !! Please re-check the input for the previous steps")

            print("\nWrong choice, please re-run the script and follow the instructions !!!"
                  "\n")

        return print("The images were sorted successfully !!!")


if __name__ == "__main__":
    page = ProcessingPage()
    page.mainloop()
