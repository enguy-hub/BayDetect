# from tkinter import *
from pathlib import Path
from tkinter import ttk, filedialog
from baydetect.gui.scrollpage import ScrolledPage

import os
import json
import fnmatch
import pandas as pd
import tkinter as tk

LARGE_FONT = ("Calibri", 12)

"""
------------------------------------------------------------------------------------------------------------------------
Batch Page(s) Section
------------------------------------------------------------------------------------------------------------------------
"""


class BatchPage(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        label = ttk.Label(self.sw.scrollwindow, text="Batch Functions", font=LARGE_FONT)
        label.pack(ipady=5, padx=5, pady=5, expand=1)

        batc1_btn = ttk.Button(self.sw.scrollwindow, text="1/ Create `*.txt` files needed to batch-run the "
                                                          "\nprocess of making the `BatchInput` JSON files",
                               command=lambda: master.switch_frame("Batchrun BatchInput JSON"))
        batc1_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        batc2_btn = ttk.Button(self.sw.scrollwindow,
                               text="2/ Create a `*.txt` file needed for "
                                    "\nexecuting MegaDetector repeatedly",
                               command=lambda: master.switch_frame("Batchrun Run MegaDetector"))
        batc2_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        batc3_btn = ttk.Button(self.sw.scrollwindow, text="3/ Create `*.txt` files needed to batch-run the "
                                                          "\nprocess of making the `Metadata` CSV files",
                               command=lambda: master.switch_frame("Batchrun Metadata CSV"))
        batc3_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        batc4_btn = ttk.Button(self.sw.scrollwindow, text="4/ Create `*.txt` files needed to batch-run the "
                                                          "\nprocess of sorting images into categorical folders",
                               command=lambda: master.switch_frame("Batchrun Sort Images"))
        batc4_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        batc5_btn = ttk.Button(self.sw.scrollwindow,
                               text="5/ Create a combined '.txt' file for all the `.txt` files created, which"
                                    " has\nthe commands needed to execute `pf_batchrun()` from `batchrun.py`",
                               command=lambda: master.switch_frame("Batchrun Create Combined TXT"))
        batc5_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)


"""
------------------------------------------------------------------------------------------------------------------------
#1 Batchrun | BatchInput JSON Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_BatchInputJSON(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        # -------------------------------------- #
        # Common variables | To keep
        self.rootDir = os.path.abspath(os.curdir)
        self.inputDirPath = None
        self.org_img_dirpath = []
        self.img_folderpaths = []
        self.dataset_station = []
        self.station = []
        self.session = []
        self.station_session = []
        self.dataset = str

        self.pattern2Entry = None
        self.pattern2Label = None
        self.confirmPattern2 = None

        self.pattern1 = None
        self.pattern2 = None
        self.pattern1_list = []
        self.pattern2_list = []

        # -------------------------------------- #
        # Common widget variables | To destroy
        self.inputDir_label = None

        self.noSampleFolderPath_label = None
        self.noFolderPathConfirm_btn = None
        self.noSessionName_label = None
        self.noSessionName_entry = None
        self.noStationName_label = None
        self.noStationName_entry = None
        self.noSesStaConfirm_btn = None

        self.yesSampleFolderPath_label = None
        self.yesFolderPathConfirm_btn = None
        self.yesStationName_label = None
        self.yesStationName_entry = None
        self.yesSesName_label = None
        self.yesSesName_entry = None
        self.yesSesStaConfirm_btn = None

        self.success_label = None

        # -------------------------------------- #
        # Variables for JSON Creator `batch-run`
        self.yesInputJSONDirPath = None
        self.noInputJSONDirPath = None
        self.yesOutputTxtDirPath1 = None
        self.noOutputTxtDirPath1 = None

        # To destroy | JSON Creator `batch-run` widget variables
        self.yesInputJSONDir_btn = None
        self.yesInputJSONDir_label = None
        self.yesOutputTxtDir_btn1 = None
        self.yesOutputTxtDir_label1 = None
        self.yesCreateJSONTxt_btn = None

        self.noInputJSONDir_btn = None
        self.noInputJSONDir_label = None
        self.noOutputTxtDir_btn1 = None
        self.noOutputTxtDir_label1 = None
        self.noCreateJSONTxt_btn = None

        # -------------------------------------- #

        inputDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Select the `top-level folder`, in "
                                                               "which all the images\nare being stored inside "
                                                               "sub-folders under this `top-level folder`",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='n')

        pattern1Label = ttk.Label(self.sw.scrollwindow,
                                  text="2/ Please enter the common pattern in the names "
                                       "\nof the folders where all the image are stored in: ")
        pattern1Label.grid(row=2, sticky='n')

        self.pattern1Entry = ttk.Entry(self.sw.scrollwindow)
        self.pattern1Entry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='n')

        pattern2CheckLabel = ttk.Label(self.sw.scrollwindow,
                                       text="3/ Is there a second common pattern in the names of the"
                                            "\nsub-folders in the above-mentioned folders? (`Y` or `N`): ")
        pattern2CheckLabel.grid(row=4, sticky='')

        self.pattern2CheckYes_btn = ttk.Button(self.sw.scrollwindow, text="Yes", command=self.secondPattern)
        self.pattern2CheckYes_btn.grid(row=5, ipady=3, ipadx=3, sticky='n')

        self.pattern2CheckNo_btn = ttk.Button(self.sw.scrollwindow, text="No", command=self.clickedNo)
        self.pattern2CheckNo_btn.grid(row=6, ipady=3, ipadx=3, sticky='n')

        batch_btn = ttk.Button(self.sw.scrollwindow, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=23, ipady=10, ipadx=10, pady=8, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=24, ipady=10, ipadx=10, sticky='n')

    def inputDir(self):

        inputDir = filedialog.askdirectory(initialdir=self.rootDir + "/image_data",
                                           title='Select the `top-level` folder which contains all the images')
        self.inputDirPath = str(inputDir) + "/"
        self.inputDirPath.replace("\\", "/")

        print("\nStarting new image folder selection !!")
        print("\nInput image folder:")
        print(self.inputDirPath)

        self.inputDir_label = tk.Text(self.sw.scrollwindow, height=1, borderwidth=0)
        self.inputDir_label.tag_configure("tag_name", justify='center')
        self.inputDir_label.insert("1.0", "Selected path: " + self.inputDirPath)
        self.inputDir_label.tag_add("tag_name", "1.0", "end")
        self.inputDir_label.grid(row=1, pady=4, sticky='n')

        self.inputDir_label.configure(state="disabled")
        self.inputDir_label.configure(inactiveselectbackground=self.inputDir_label.cget("selectbackground"))

    """
        NO @ Question 3 | Initial functions
    """

    def clickedNo(self):

        self.pattern2CheckYes_btn['state'] = 'disabled'

        pattern1 = self.pattern1Entry.get()

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for dirname in fnmatch.filter(dirs, pattern1):
                self.org_img_dirpath.append(os.path.join(path, dirname).replace("\\", "/"))

        print("\nPath to the first folder: \n" + self.org_img_dirpath[0].split()[-1] + "/" + "\n")

        self.noSampleFolderPath_label = tk.Text(self.sw.scrollwindow, height=2, width=100, borderwidth=0)
        self.noSampleFolderPath_label.tag_configure("tag_name", justify='center')
        self.noSampleFolderPath_label.insert("2.0", "Path to the first folder: " +
                                             str(self.org_img_dirpath[1].split()[-1]) + "/")
        self.noSampleFolderPath_label.tag_add("tag_name", "2.0", "end")
        self.noSampleFolderPath_label.grid(row=7, pady=7, sticky='n')

        self.noSampleFolderPath_label.configure(state="disabled")
        self.noSampleFolderPath_label.configure(
            inactiveselectbackground=self.noSampleFolderPath_label.cget("selectbackground"))

        self.noFolderPathConfirm_btn = ttk.Button(self.sw.scrollwindow, text="Confirm Folder-Path !!!",
                                                  command=self.noFolderPathConfirmed)
        self.noFolderPathConfirm_btn.grid(row=8, sticky='')

    def noFolderPathConfirmed(self):
        self.noSessionName_label = ttk.Label(self.sw.scrollwindow,
                                             text="4/ Which index is the `Session` in the above "
                                                  "\nfolder path when it is split with `/` as separator?")
        self.noSessionName_label.grid(row=9, ipady=5, ipadx=5, sticky='')

        self.noSessionName_entry = ttk.Entry(self.sw.scrollwindow)
        self.noSessionName_entry.grid(row=10, ipady=10, ipadx=10, pady=4, sticky='')

        self.noStationName_label = ttk.Label(self.sw.scrollwindow,
                                             text="5/ Which index is the `Station` in the above "
                                                  "\nfolder path when it is split with `/` as separator?")
        self.noStationName_label.grid(row=11, ipady=5, ipadx=5, sticky='')

        self.noStationName_entry = ttk.Entry(self.sw.scrollwindow)
        self.noStationName_entry.grid(row=12, ipady=10, ipadx=10, pady=4, sticky='')

        self.noSesStaConfirm_btn = ttk.Button(self.sw.scrollwindow, text="Confirm Session and Station Names !!!",
                                              command=self.noSesStaIndexConfirm)
        self.noSesStaConfirm_btn.grid(row=13, sticky='')

    def noSesStaIndexConfirm(self):
        sessionName = int(self.noSessionName_entry.get())
        stationName = int(self.noStationName_entry.get())

        for idirpaths in self.org_img_dirpath:
            for dirpath, dirnames, files in os.walk(idirpaths):
                if files:
                    self.img_folderpaths.append(''.join(idirpaths.split()[-1]))
                    self.session.append(''.join(idirpaths.split('/')[sessionName]))
                    self.dataset_station.append(''.join(idirpaths.split('/')[stationName]))
                if not files:
                    pass

        print("\nList of all image folders matches the above patterns: ")
        print(self.img_folderpaths)

        print("\nList of stations: ")
        print(self.dataset_station)

        for name in self.dataset_station:
            self.dataset = ''.join(name.split('_')[0])
            self.station.append('_'.join(name.split('_')[1:]))

        print("\nDataset name: " + self.dataset)

        print("\nList of stations #: ")
        print(self.station)

        print("\nList of sessions: ")
        print(self.session)

        self.station_session = [a + '_' + b for a, b in zip(self.dataset_station, self.session)]
        print("\nList of file-names for cross-checking later: ")
        print(self.station_session)

        self.noInputJSONDir_btn = ttk.Button(self.sw.scrollwindow,
                                             text="6/ Select the folder where you want "
                                                  "all the '*_BI.json' files to be saved at",
                                             command=self.noInputJSONDir)
        self.noInputJSONDir_btn.grid(row=14, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noOutputTxtDir_btn1 = ttk.Button(self.sw.scrollwindow, text="7/ Select the folder where you "
                                                                         "want all the '.txt' files to be saved at",
                                              command=self.noOutputTxtDir1)
        self.noOutputTxtDir_btn1.grid(row=16, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noCreateJSONTxt_btn = ttk.Button(self.sw.scrollwindow,
                                              text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` JSON CREATOR",
                                              command=self.noCreateJSONTxt)
        self.noCreateJSONTxt_btn.grid(row=18, ipadx=10, ipady=10, pady=4, sticky='n')

    """
        NO @ Question 3 | JSON Creator
    """

    def noInputJSONDir(self):
        noInputJSONDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                                 title='Select the output folder for `BatchInput` JSON files')
        self.noInputJSONDirPath = str(noInputJSONDir) + "/"
        self.noInputJSONDirPath.replace("\\", "/")

        self.noInputJSONDir_label = ttk.Label(self.sw.scrollwindow, text=self.noInputJSONDirPath)
        self.noInputJSONDir_label.grid(row=15, pady=4, sticky='n')

        print('\n`BI` JSON FOLDER: ' + '\n' + self.noInputJSONDirPath)

    def noOutputTxtDir1(self):
        noOutputTxtDir1 = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                                  title='Select the folder for the `.txt` files')
        self.noOutputTxtDirPath1 = str(noOutputTxtDir1) + "/"
        self.noOutputTxtDirPath1.replace("\\", "/")

        self.noOutputTxtDir_label1 = ttk.Label(self.sw.scrollwindow, text=self.noOutputTxtDirPath1)
        self.noOutputTxtDir_label1.grid(row=17, pady=4, sticky='n')

        print('\nTXT FILES FOLDER: ' + '\n' + self.noOutputTxtDirPath1)

    def noCreateJSONTxt(self):
        jsonInputDir = self.noInputJSONDirPath
        txtOutputDir = self.noOutputTxtDirPath1

        for ista, isess, ipaths in zip(self.station, self.session, self.img_folderpaths):
            create = open(f"{txtOutputDir}pf1_createBIJSON_{self.dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}/{self.dataset}_{ista}_{isess}_BI.json\n")
            create.close()

            self.success_label = ttk.Label(self.sw.scrollwindow,
                                           text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                "\nPlease adjust the previous steps for a new run")
            self.success_label.grid(row=19, sticky='n', pady=4)

        destroy_these = [self.inputDir_label,
                         self.noSampleFolderPath_label, self.noFolderPathConfirm_btn,
                         self.noSessionName_label, self.noSessionName_entry,
                         self.noStationName_label, self.noStationName_entry,
                         self.noSesStaConfirm_btn, self.noInputJSONDir_btn,
                         self.noInputJSONDir_label, self.noOutputTxtDir_btn1,
                         self.noOutputTxtDir_label1, self.noCreateJSONTxt_btn]

        for widget in destroy_these:
            widget.destroy()

        self.pattern1Entry.delete(0, 'end')
        self.pattern2CheckYes_btn['state'] = 'normal'

        # Delete existing lists for next round
        self.pattern1_list.clear()
        self.org_img_dirpath.clear()
        self.station.clear()
        self.session.clear()
        self.station_session.clear()
        self.img_folderpaths.clear()

        print("\nTHE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
              "\nPlease adjust the previous steps for a new run")

    """
        YES @ Question 3 | Initial functions
    """

    def secondPattern(self):

        self.pattern2CheckNo_btn['state'] = 'disable'

        pattern1 = self.pattern1Entry.get()
        print("Pattern 1 is: " + pattern1)

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for dirname_p1 in fnmatch.filter(dirs, pattern1):
                self.pattern1_list.append(os.path.join(path, dirname_p1).replace("\\", "/"))

        self.pattern2Label = ttk.Label(self.sw.scrollwindow,
                                       text="4/ What is the second common pattern in the names of the "
                                            "sub-folders?\n(please ends with an asterisk like so: `2020*`, "
                                            "`Session*` or `100CU*`): ")
        self.pattern2Label.grid(row=7, sticky='')

        self.pattern2Entry = ttk.Entry(self.sw.scrollwindow)
        self.pattern2Entry.grid(row=8, ipady=10, ipadx=10, pady=4, sticky='n')

        self.confirmPattern2 = ttk.Button(self.sw.scrollwindow, text="CONFIRM SECOND PATTERN !!",
                                          command=self.clickedYes)
        self.confirmPattern2.grid(row=9, sticky='n')

    def clickedYes(self):

        pattern2 = self.pattern2Entry.get()
        print("Pattern 2 is: " + pattern2)

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for dirname_p2 in fnmatch.filter(dirs, pattern2):
                self.pattern2_list.append(dirname_p2)

        for ip1, ip2 in zip(self.pattern1_list, self.pattern2_list):
            self.org_img_dirpath.append(os.path.join(ip1, ip2).replace("\\", "/"))

        self.yesSampleFolderPath_label = ttk.Label(
            self.sw.scrollwindow, text="\nPath to the FIRST image matches the pattern(s): \n"
                                       + self.org_img_dirpath[0].split()[-1])
        self.yesSampleFolderPath_label.grid(row=10, sticky='')

        print("\nPath to the FIRST image folder matches the pattern(s): \n" + self.org_img_dirpath[0].split()[-1])

        self.yesFolderPathConfirm_btn = ttk.Button(self.sw.scrollwindow, text="Confirm Folder-Path !!!",
                                                   command=self.yesFolderPathConfirmed)
        self.yesFolderPathConfirm_btn.grid(row=11, pady=10, sticky='')

    def yesFolderPathConfirmed(self):
        self.yesSesName_label = ttk.Label(
            self.sw.scrollwindow, text="5/ Which index is the `Session` in the above"
                                       "\nfolder path when it is split with `/` as separator?")
        self.yesSesName_label.grid(row=12, sticky='')

        self.yesSesName_entry = ttk.Entry(self.sw.scrollwindow)
        self.yesSesName_entry.grid(row=13, ipady=10, ipadx=10, pady=4, sticky='')

        self.yesStationName_label = ttk.Label(
            self.sw.scrollwindow, text="6/ Which index is the `Station` in the above"
                                       "\nfolder path when it is split with `/` as separator?")
        self.yesStationName_label.grid(row=14, sticky='')

        self.yesStationName_entry = ttk.Entry(self.sw.scrollwindow)
        self.yesStationName_entry.grid(row=15, ipady=10, ipadx=10, pady=4, sticky='')

        self.yesSesStaConfirm_btn = ttk.Button(self.sw.scrollwindow, text="Confirm Session and Station Names !!!",
                                               command=self.yesSesStaIndexConfirm)
        self.yesSesStaConfirm_btn.grid(row=16, pady=10, sticky='')

    def yesSesStaIndexConfirm(self):
        sessionIndex = int(self.yesSesName_entry.get())
        stationIndex = int(self.yesStationName_entry.get())

        for idirpaths in self.org_img_dirpath:
            for dirpath, dirnames, files in os.walk(idirpaths):
                if files:
                    self.img_folderpaths.append(''.join(idirpaths.split()[-1]))
                    self.session.append(''.join(idirpaths.split('/')[sessionIndex]))
                    self.dataset_station.append(''.join(idirpaths.split('/')[stationIndex]))
                if not files:
                    break

        print("\nList of all image folders matches the above patterns: ")
        print(self.img_folderpaths)

        print("\nList of stations: ")
        print(self.dataset_station)

        for name in self.dataset_station:
            self.dataset = ''.join(name.split('_')[0])
            self.station.append('_'.join(name.split('_')[1:]))

        print("\nDataset name: " + self.dataset)

        print("\nList of stations #: ")
        print(self.station)

        print("\nList of sessions: ")
        print(self.session)

        self.station_session = [a + '_' + b for a, b in zip(self.dataset_station, self.session)]
        print("\nList of file-names for cross-checking later: ")
        print(self.station_session)

        self.yesInputJSONDir_btn = ttk.Button(self.sw.scrollwindow, text="8/ Select the folder where all the"
                                                                         "'*_BI.json' files will be saved at",
                                              command=self.yesInputJSONDir)
        self.yesInputJSONDir_btn.grid(row=17, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesOutputTxtDir_btn1 = ttk.Button(self.sw.scrollwindow, text="9/ Select the folder where all"
                                                                          "the '.txt' files will be saved at",
                                               command=self.yesOutputTxtDir)
        self.yesOutputTxtDir_btn1.grid(row=19, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesCreateJSONTxt_btn = ttk.Button(self.sw.scrollwindow,
                                               text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` JSON CREATOR",
                                               command=self.yesCreateJSONTxt)
        self.yesCreateJSONTxt_btn.grid(row=21, ipadx=10, ipady=10, pady=4, sticky='n')

    """
        YES @ Question 3 | JSON Creator
    """

    def yesInputJSONDir(self):
        yesInputJSONDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                                  title='Select the folder contains `BatchInput` JSON files')
        self.yesInputJSONDirPath = str(yesInputJSONDir) + "/"
        self.yesInputJSONDirPath.replace("\\", "/")

        self.yesInputJSONDir_label = ttk.Label(self.sw.scrollwindow, text=self.yesInputJSONDirPath)
        self.yesInputJSONDir_label.grid(row=18, pady=4, sticky='n')

        print('\n`BI` JSON FOLDER: ' + '\n' + self.yesInputJSONDirPath)

    def yesOutputTxtDir(self):
        yesOutputTxtDir1 = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                                   title='Select the folder for the `.txt` files')
        self.yesOutputTxtDirPath1 = str(yesOutputTxtDir1) + "/"
        self.yesOutputTxtDirPath1.replace("\\", "/")

        self.yesOutputTxtDir_label1 = ttk.Label(self.sw.scrollwindow, text=self.yesOutputTxtDirPath1)
        self.yesOutputTxtDir_label1.grid(row=20, pady=4, sticky='n')

        print('\nTXT FILES FOLDER: ' + '\n' + self.yesOutputTxtDirPath1)

    def yesCreateJSONTxt(self):

        jsonInputDir = self.yesInputJSONDirPath
        txtOutputDir = self.yesOutputTxtDirPath1

        for ista, isess, ipaths in zip(self.station, self.session, self.img_folderpaths):
            create = open(f"{txtOutputDir}pf1_createBIJSON_{self.dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}{self.dataset}_{ista}_{isess}_BI.json\n")
            create.close()

            self.success_label = ttk.Label(self.sw.scrollwindow,
                                           text="`.TXT` FILE(S) CREATED SUCCESSFULLY !!!"
                                                "\nPlease adjust the previous steps for a new run")
            self.success_label.grid(row=22, pady=4, sticky='n')

        destroy_these = [self.inputDir_label, self.pattern2Label,
                         self.pattern2Entry, self.confirmPattern2,
                         self.yesSampleFolderPath_label, self.yesFolderPathConfirm_btn,
                         self.yesSesName_label, self.yesSesName_entry,
                         self.yesStationName_label, self.yesStationName_entry,
                         self.yesSesStaConfirm_btn, self.yesInputJSONDir_btn,
                         self.yesInputJSONDir_label, self.yesOutputTxtDir_btn1,
                         self.yesOutputTxtDir_label1, self.yesCreateJSONTxt_btn]

        for widget in destroy_these:
            widget.destroy()

        self.pattern1Entry.delete(0, 'end')
        self.pattern2CheckNo_btn['state'] = 'normal'

        # Delete existing lists for next round
        self.pattern1_list.clear()
        self.pattern2_list.clear()
        self.org_img_dirpath.clear()
        self.dataset_station.clear()
        self.station.clear()
        self.session.clear()
        self.station_session.clear()
        self.img_folderpaths.clear()

        print("\nTHE `.TXT` FILE(S) CREATED SUCCESSFULLY !!!"
              "\nPlease adjust the previous steps for a new run")


"""
------------------------------------------------------------------------------------------------------------------------
#2 BatchRun | Run MegaDetector Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_RunMegaDetector(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.rootDir = os.path.abspath(os.curdir)
        self.BIJSONDirPath = None
        self.BIJSONDirPathLabel = None

        self.MDJSONDirPath = None
        self.MDJSONDirPathLabel = None

        self.outputTxtDirPath = None
        self.outputTxtDirPathLabel = None

        biJSONDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Select the folder where "
                                                                "all `*_BI.json` files are located in",
                                     command=self.BIJSONDir)
        biJSONDirButton.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='ew')

        mdJSONDirButton = ttk.Button(self.sw.scrollwindow, text="2/ Select the output folder "
                                                                "for all the `*_MD.json` files",
                                     command=self.MDJSONDir)
        mdJSONDirButton.grid(row=2, ipadx=10, ipady=10, pady=4, sticky='ew')

        outputTxtDirButton = ttk.Button(self.sw.scrollwindow, text="3/ Select the folder where the "
                                                                   "output `.txt` file will be saved at",
                                        command=self.outputTxtDir)
        outputTxtDirButton.grid(row=4, ipadx=10, ipady=10, pady=4, sticky='ew')

        self.runMDTxtButton = ttk.Button(self.sw.scrollwindow, text="CREATE TXT FILE(S) FOR "
                                                                    "`BATCH-RUNNING` MEGADETECTOR",
                                         command=self.runMDTxtButton)
        self.runMDTxtButton.grid(row=6, ipadx=10, ipady=10, pady=4, sticky='')

        batch_btn = ttk.Button(self.sw.scrollwindow, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=7, ipady=10, ipadx=10, pady=4, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=8, ipadx=10, ipady=10, pady=4, sticky='')

    def BIJSONDir(self):
        BIJSONDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                            title='Select the folder contains `BatchInput` JSON files')
        self.BIJSONDirPath = str(BIJSONDir) + "/"

        self.BIJSONDirPathLabel = ttk.Label(self.sw.scrollwindow, text=self.BIJSONDirPath)
        self.BIJSONDirPathLabel.grid(row=1, ipadx=10, ipady=10, sticky='')

        print('\nSELECTED FOLDER CONTAINING THE `BATCH-INPUT` JSON FILES: ' + '\n' + str(BIJSONDir))

    def MDJSONDir(self):
        MDJSONDirPath = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                                title='Select the folder for `MegaDetected` JSON files')
        self.MDJSONDirPath = str(MDJSONDirPath) + "/"

        self.MDJSONDirPathLabel = ttk.Label(self.sw.scrollwindow, text=self.MDJSONDirPath)
        self.MDJSONDirPathLabel.grid(row=3, ipadx=10, ipady=10, sticky='')

        print('\nSELECTED FOLDER FOR THE `MEGA-DETECTED` JSON FILES: ' + '\n' + str(MDJSONDirPath))

    def outputTxtDir(self):
        outputTxtDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                               title='Select the output folder for the `.txt` files')
        self.outputTxtDirPath = str(outputTxtDir) + "/"

        self.outputTxtDirPathLabel = ttk.Label(self.sw.scrollwindow, text=self.outputTxtDirPath)
        self.outputTxtDirPathLabel.grid(row=5, ipadx=10, ipady=10, sticky='')

        print('\nSELECTED FOLDER FOR THE TXT FILES: ' + '\n' + str(outputTxtDir))

    def runMDTxtButton(self):

        bi_json_dir_input = self.BIJSONDirPath
        md_json_dir_input = self.MDJSONDirPath
        output_txtdir = self.outputTxtDirPath

        md_dirpath = None

        for dirpath, dirnames, filenames in os.walk(md_json_dir_input):
            md_dirpath = dirpath.split("BayDetect")[1].replace("\\", "/")

        for dirpath, dirnames, filenames in os.walk(bi_json_dir_input):
            bi_dirpath = dirpath.split("BayDetect")[1].replace("\\", "/")
            # root_path = root_path.replace("\\", "/")

            for ifilenames in range(len(filenames)):
                fullnames = filenames[ifilenames]
                names_withBI, extension = os.path.splitext(fullnames)
                name_withoutBI = '_'.join(names_withBI.split('_')[:-1])

                with open(output_txtdir + "startSess1_pf2_runMD_cmds.txt", "a") as f:
                    f.write(f"'python run_detector_batch.py md_v5a.0.0.pt ' \n"
                            f"'../..{bi_dirpath}{names_withBI}.json ' \n"
                            f"'../..{md_dirpath}{name_withoutBI}_MD.json ' \n"
                            f"'&& '\n")

                self.BIJSONDirPathLabel.destroy()
                self.MDJSONDirPathLabel.destroy()
                self.outputTxtDirPathLabel.destroy()

                self.runMDTxtButton.config(text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                "\nPlease adjust the previous steps for the new run")

                print("\nTHE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!! "
                      "\nPlease adjust the previous steps for the new run")


"""
------------------------------------------------------------------------------------------------------------------------
#3 BatchRun | Metadata CSV Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_MetadataCSV(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        # -------------------------------------- #
        # Common variables | To keep
        self.rootDir = os.path.abspath(os.curdir)
        self.org_img_dirpath = []
        self.img_folderpaths = []
        self.dataset_station = []
        self.station = []
        self.session = []
        self.station_session = []
        self.dataset = str

        # -------------------------------------- #
        # Variables for Metadata CSV Convertor
        self.mdJSONDirPath = None
        self.outputCSVDirPath = None
        self.outputTxtDirPath = None

        # To destroy | CSV Convertor `batch-run` widget variables
        self.mdJSONDir_label = None
        self.exampleImgPath_label = None
        self.confirmExampleImgPath_btn = None

        self.sessName_label = None
        self.sessName_entry = None
        self.stationName_label = None
        self.stationName_entry = None
        self.sessStaConfirm_btn = None

        self.outputCSVDir_btn = None
        self.outputTxtDir_btn = None
        self.outputCSVDir_label = None
        self.outputTxtDir_label = None

        self.convertCSVTxt_btn = None
        self.success_label = None

        mdJSONDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Select the folder where all the "
                                                                "'*_MD.json' files are currently saved at",
                                     command=self.mdJSONDir)
        mdJSONDirButton.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='n')

        batch_btn = ttk.Button(self.sw.scrollwindow, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=14, ipady=10, ipadx=10, pady=8, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=15, ipady=10, ipadx=10, sticky='n')

    def mdJSONDir(self):
        mdJSONDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                            title='Select the folder contains `MegaDetected` JSON files')

        self.mdJSONDirPath = str(mdJSONDir) + "/"
        self.mdJSONDirPath.replace("\\", "/")

        self.mdJSONDir_label = ttk.Label(self.sw.scrollwindow, text=self.mdJSONDirPath)
        self.mdJSONDir_label.grid(row=1, pady=4, sticky='n')

        print('\n`MD` JSON FOLDER: ' + '\n' + self.mdJSONDirPath)

        jsonSet = set()
        imgDirSet = set()

        for ijson in os.listdir(self.mdJSONDirPath):
            jsonPaths = os.path.join(self.mdJSONDirPath, ijson)
            jsonSet.add(jsonPaths)

        for j in jsonSet:
            inputJSON = open(j, 'r')
            infoJSON = json.load(inputJSON)

            for i in range(len(list(infoJSON['images']))):
                imagePath = list(infoJSON['images'][i].values())[0]
                imgDir = os.path.dirname(imagePath)
                imgDirSet.add(imgDir)

        self.org_img_dirpath = list(imgDirSet)
        self.org_img_dirpath.sort()
        print("\nList of all the image folders found from `MegaDetected` JSON files:")
        print(self.org_img_dirpath)

        self.exampleImgPath_label = ttk.Label(self.sw.scrollwindow,
                                              text="2/ Is the below path of the image folder correct? \n"
                                                   + self.org_img_dirpath[0])
        self.exampleImgPath_label.grid(row=2, pady=4, sticky='n')

        self.confirmExampleImgPath_btn = ttk.Button(self.sw.scrollwindow, text="CONFIRM FIRST IMAGE PATH !!",
                                                    command=self.confirmPath)
        self.confirmExampleImgPath_btn.grid(row=3, sticky='n')

    def confirmPath(self):

        self.sessName_label = ttk.Label(
            self.sw.scrollwindow, text="3/ Which index is the `Session` in the above folder "
                                       "\npath when it is split with `/` as separator?")
        self.sessName_label.grid(row=4, sticky='')

        self.sessName_entry = ttk.Entry(self.sw.scrollwindow)
        self.sessName_entry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='')

        self.stationName_label = ttk.Label(
            self.sw.scrollwindow, text="4/ Which index is the `Station` in the above folder "
                                       "\npath when it is split with `/` as separator?")
        self.stationName_label.grid(row=6, sticky='')

        self.stationName_entry = ttk.Entry(self.sw.scrollwindow)
        self.stationName_entry.grid(row=7, ipady=10, ipadx=10, pady=4, sticky='')

        self.sessStaConfirm_btn = ttk.Button(self.sw.scrollwindow, text="Confirm Session and Station Names !!!",
                                             command=self.confirmSessSta)
        self.sessStaConfirm_btn.grid(row=8, pady=10, sticky='')

    def confirmSessSta(self):
        sessionIndex = int(self.sessName_entry.get())
        stationIndex = int(self.stationName_entry.get())

        for idirpaths in self.org_img_dirpath:
            for dirpath, dirnames, files in os.walk(idirpaths):
                if files:
                    self.img_folderpaths.append(''.join(idirpaths.split()[-1]))
                    self.session.append(''.join(idirpaths.split('/')[sessionIndex]))
                    self.dataset_station.append(''.join(idirpaths.split('/')[stationIndex]))
                if not files:
                    break

        for name in self.dataset_station:
            self.dataset = ''.join(name.split('_')[0])
            self.station.append('_'.join(name.split('_')[1:]))

        # Sort all the sets
        self.img_folderpaths.sort()
        # self.session.sort()
        # self.station.sort()
        # self.dataset_station.sort()

        # Set of dataset_station
        datasetStationSet = set(self.dataset_station)

        print("\nList of image folders available on the machine matched with the ones on the list above: ")
        print(self.img_folderpaths)

        print("\nDataset name: " + self.dataset)

        print("\nList of stations available on the machine's image folders: ")
        print(sorted(datasetStationSet))

        self.station_session = [a + '_' + b for a, b in zip(self.dataset_station, self.session)]
        print("\nList of sessions from image folders present on the machine for CROSS-CHECKING later: ")
        print(self.station_session)

        self.outputCSVDir_btn = ttk.Button(self.sw.scrollwindow, text="7/ Select the folder where all the "
                                                                      "'*_Meta.csv' files will be saved at",
                                           command=self.outputCSVDir)
        self.outputCSVDir_btn.grid(row=9, ipadx=10, ipady=10, pady=4, sticky='n')

        self.outputTxtDir_btn = ttk.Button(self.sw.scrollwindow, text="8/ Select the folder where all "
                                                                      "the '.txt' files will be saved at",
                                           command=self.outputTxtDir)
        self.outputTxtDir_btn.grid(row=11, ipadx=10, ipady=10, pady=4, sticky='n')

        # Move later
        self.convertCSVTxt_btn = ttk.Button(self.sw.scrollwindow,
                                            text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` CSV CONVERTOR",
                                            command=self.convertCSVTxt)
        self.convertCSVTxt_btn.grid(row=13, ipadx=10, ipady=10, pady=4, sticky='n')

    def outputCSVDir(self):
        outputCSVDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                               title='Select the output folder for the `*_Meta.csv` files')
        self.outputCSVDirPath = str(outputCSVDir) + "/"
        self.outputCSVDirPath.replace("\\", "/")

        self.outputCSVDir_label = ttk.Label(self.sw.scrollwindow, text=self.outputCSVDirPath)
        self.outputCSVDir_label.grid(row=10, pady=4, sticky='n')

        print('\nCSV `METADATA` FILES FOLDER: ' + '\n' + self.outputCSVDirPath)

    def outputTxtDir(self):
        outputTxtDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                               title='Select the output folder for the `.txt` files')
        self.outputTxtDirPath = str(outputTxtDir) + "/"
        self.outputTxtDirPath.replace("\\", "/")

        self.outputTxtDir_label = ttk.Label(self.sw.scrollwindow, text=self.outputTxtDirPath)
        self.outputTxtDir_label.grid(row=12, pady=4, sticky='n')

        print('\nTXT FILES FOLDER: ' + '\n' + self.outputTxtDirPath)

    def convertCSVTxt(self):
        # mdJSONDir = self.mdJSONDirPath
        # csvDir = self.outputCSVDirPath
        # txtOutputDir = self.outputTxtDirPath
        input_iSessionIndex = int(self.sessName_entry.get()) - 1
        input_iStationIndex = int(self.stationName_entry.get()) - 1

        md_withoutExt = []
        iname_list = []

        for dirpath, dirnames, filenames in os.walk(self.mdJSONDirPath):
            for ifilenames in filenames:
                fname, extension = os.path.splitext(ifilenames)
                md_withoutExt.append(fname)

        for inameNoExt in md_withoutExt:
            inameRaw = '_'.join(inameNoExt.split('_')[0:5])
            iname_list.append(inameRaw)
        # Sort the list
        iname_list.sort()

        print("\nList of `MD` JSON files currently in the `MD` folder: ")
        print(md_withoutExt)

        print("\nList of MATCHED sessions in both the image folders and JSON files in the `MD` folder:")
        matchNames_list = list(set(self.station_session).intersection(iname_list))
        matchNames_list.sort()
        print(matchNames_list)

        for ista, isess, iorg_dirpath, imatch_name in zip(self.station, self.session, self.img_folderpaths,
                                                          matchNames_list):
            create = open(f"{self.outputTxtDirPath}pf3_mdJSONToCSV_{self.dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"2\n"
                         f"{self.mdJSONDirPath}{imatch_name}_MD.json\n"
                         f"{self.outputCSVDirPath}{imatch_name}_Meta.csv\n"
                         f"{input_iSessionIndex}\n"
                         f"{input_iStationIndex}")
            create.close()

            self.success_label = ttk.Label(self.sw.scrollwindow, text="`*.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                                      "\nPlease adjust the steps for a new run")
            self.success_label.grid(row=36, sticky='n', pady=4)

        destroy_these = [self.mdJSONDir_label, self.exampleImgPath_label,
                         self.confirmExampleImgPath_btn, self.sessName_label,
                         self.sessName_entry, self.stationName_label,
                         self.stationName_entry, self.sessStaConfirm_btn,
                         self.outputCSVDir_btn, self.outputTxtDir_btn, self.outputCSVDir_label,
                         self.outputTxtDir_label, self.convertCSVTxt_btn, self.success_label]

        for widget in destroy_these:
            widget.destroy()

        # Delete existing lists for next round
        self.org_img_dirpath.clear()
        self.station.clear()
        self.session.clear()
        self.station_session.clear()
        self.img_folderpaths.clear()
        iname_list.clear()
        md_withoutExt.clear()
        matchNames_list.clear()

        print("\nTHE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
              "\nPlease adjust the previous steps for a new run")


"""
------------------------------------------------------------------------------------------------------------------------
#4 BatchRun | Sort Images Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_SortImages(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        # -------------------------------------- #
        # Common variables | To keep
        self.rootDir = os.path.abspath(os.curdir)
        self.org_img_dirpath = []
        self.img_folderpaths = []
        self.dataset_station = []
        self.station = []
        self.session = []
        self.station_session = []
        self.dataset = str

        # -------------------------------------- #
        # Variables for Image Sorter `batch-run`
        self.inputCSVDirPath = None
        self.outputTxtDirPath = None

        # To destroy | CSV Convertor `batch-run` widget variables
        self.inputCSVDir_label = None
        self.exampleImgPath_label = None
        self.confirmExampleImgPath_btn = None

        self.sessName_label = None
        self.sessName_entry = None
        self.stationName_label = None
        self.stationName_entry = None
        self.sessStaConfirm_btn = None

        self.sorted_label = None
        self.sorted_entry = None
        self.outputTxtDir_btn = None
        self.sortImagesTxt_btn = None
        self.outputTxtDir_label = None
        self.success_label = None

        # -------------------------------------- #

        inputCSVDir_btn = ttk.Button(self.sw.scrollwindow, text="1/ Select the folder where all the '*_Meta.csv' "
                                                                "\nfiles are currently saved at: ",
                                     command=self.inputCSVDir)
        inputCSVDir_btn.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='n')

        batch_btn = ttk.Button(self.sw.scrollwindow, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=14, ipady=10, ipadx=10, pady=8, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=15, ipady=10, ipadx=10, sticky='n')

    def inputCSVDir(self):
        inputCSVDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                              title='Select the folder contains CSV `Metadata` files')
        self.inputCSVDirPath = str(inputCSVDir) + "/"
        self.inputCSVDirPath.replace("\\", "/")

        self.inputCSVDir_label = ttk.Label(self.sw.scrollwindow, text=self.inputCSVDirPath)
        self.inputCSVDir_label.grid(row=1, pady=4, sticky='n')

        print('\nSELECTED CSV `METADATA` FOLDER: ' + '\n' + self.inputCSVDirPath)

        csvSet = set()
        imgDirSet = set()

        for iCSV in os.listdir(self.inputCSVDirPath):
            csvPaths = os.path.join(self.inputCSVDirPath, iCSV)
            csvSet.add(csvPaths)
        print(csvSet)

        for c in csvSet:
            csv_file = pd.read_csv(c)
            df_csv = pd.DataFrame(csv_file)
            print(len(list(df_csv['Image Path'])))
            for i in range(len(list(df_csv['Image Path']))):
                imagePath = list(df_csv['Image Path'])[i]
                # print(imagePath)
                imgDir = os.path.dirname(imagePath)
                imgDirSet.add(imgDir)

        self.org_img_dirpath = list(imgDirSet)
        self.org_img_dirpath.sort()
        print("\nList of all the image folders found from CSV `Metadata` files:")
        print(self.org_img_dirpath)

        self.exampleImgPath_label = ttk.Label(self.sw.scrollwindow,
                                              text="2/ Is the below path of the first image correct? \n"
                                                   + self.org_img_dirpath[0])
        self.exampleImgPath_label.grid(row=2, pady=4, sticky='n')

        self.confirmExampleImgPath_btn = ttk.Button(self.sw.scrollwindow, text="CONFIRM FIRST IMAGE PATH !!",
                                                    command=self.confirmPath)
        self.confirmExampleImgPath_btn.grid(row=3, sticky='n')

    def confirmPath(self):
        self.sessName_label = ttk.Label(self.sw.scrollwindow,
                                        text="3/ Which index is the `Session` in the above folder "
                                             "\npath when it is split with `/` as separator?")
        self.sessName_label.grid(row=4, sticky='')

        self.sessName_entry = ttk.Entry(self.sw.scrollwindow)
        self.sessName_entry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='')

        self.stationName_label = ttk.Label(self.sw.scrollwindow,
                                           text="4/ Which index is the `Station` in the above folder "
                                                "\npath when it is split with `/` as separator?")
        self.stationName_label.grid(row=6, sticky='')

        self.stationName_entry = ttk.Entry(self.sw.scrollwindow)
        self.stationName_entry.grid(row=7, ipady=10, ipadx=10, pady=4, sticky='')

        self.sessStaConfirm_btn = ttk.Button(self.sw.scrollwindow, text="Confirm Session and Station Names !!!",
                                             command=self.confirmSessSta)
        self.sessStaConfirm_btn.grid(row=8, pady=10, sticky='')

    def confirmSessSta(self):
        sessionIndex = int(self.sessName_entry.get())
        stationIndex = int(self.stationName_entry.get())

        for idirpaths in self.org_img_dirpath:
            for dirpath, dirnames, files in os.walk(idirpaths):
                if files:
                    self.img_folderpaths.append(''.join(idirpaths.split()[-1]))
                    self.session.append(''.join(idirpaths.split('/')[sessionIndex]))
                    self.dataset_station.append(''.join(idirpaths.split('/')[stationIndex]))
                if not files:
                    break

        for name in self.dataset_station:
            self.dataset = ''.join(name.split('_')[0])
            self.station.append('_'.join(name.split('_')[1:]))

        print("\nList of all the image folders available on the machine that matched matches the list above: ")
        print(self.img_folderpaths)

        print("\nDataset name: " + self.dataset)

        print("\nList of available stations from image folders: ")
        print(self.dataset_station)

        print("\nList of available sessions from image folders: ")
        print(self.session)

        self.station_session = [a + '_' + b for a, b in zip(self.dataset_station, self.session)]
        print("\nList of sessions from image folders on the machine for cross-checking later: ")
        print(self.station_session)

        self.sorted_label = ttk.Label(self.sw.scrollwindow,
                                      text="5/ Would you like the `sorted images` to be saved in a separate "
                                           "\nfolder called `*_Sorted`? (please answer with 'Y' or 'N') ")
        self.sorted_label.grid(row=9, sticky='n')

        self.sorted_entry = ttk.Entry(self.sw.scrollwindow)
        self.sorted_entry.grid(row=10, ipady=10, ipadx=10, pady=4, sticky='n')

        self.outputTxtDir_btn = ttk.Button(self.sw.scrollwindow, text="6/ Select the folder where you want "
                                                                      "all the '.txt' files to be saved at",
                                           command=self.outputTxtDir)
        self.outputTxtDir_btn.grid(row=11, ipadx=10, ipady=10, pady=4, sticky='n')

        self.sortImagesTxt_btn = ttk.Button(self.sw.scrollwindow,
                                            text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` IMAGE SORTER",
                                            command=self.sortImageTxt)
        self.sortImagesTxt_btn.grid(row=13, ipadx=10, ipady=10, pady=4, sticky='n')

    def outputTxtDir(self):
        outputTxtDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                               title='Select the folder for the `.txt` files')
        self.outputTxtDirPath = str(outputTxtDir) + "/"
        self.outputTxtDirPath.replace("\\", "/")

        self.outputTxtDir_label = ttk.Label(self.sw.scrollwindow, text=self.outputTxtDirPath)
        self.outputTxtDir_label.grid(row=12, pady=4, sticky='n')

        print('\nSELECTED FOLDER FOR TXT FILES: ' + '\n' + self.outputTxtDirPath)

    def sortImageTxt(self):
        # csvInputDir = self.inputCSVDirPath
        # txtOutputDir = self.outputTxtDirPath
        sortedInput = self.sorted_entry.get()

        csv_withoutExt = []
        iname_list = []

        for dirpath, dirnames, filenames in os.walk(self.inputCSVDirPath):
            for ifilenames in filenames:
                fname, extension = os.path.splitext(ifilenames)
                csv_withoutExt.append(fname)
                # CSV_paths.append(os.path.join(dirpath, ifilenames))

        for inameNoExt in csv_withoutExt:
            inameRaw = '_'.join(inameNoExt.split('_')[0:5])
            print(inameRaw)
            iname_list.append(inameRaw)
        # Sort the list
        iname_list.sort()

        print("\nList of CSV files currently in the `Metadata` folder: ")
        print(csv_withoutExt)

        print("\nList of MATCHED sessions between image folders and CSV files in `Metadata` folder:")
        matchNames_list = list(set(self.station_session).intersection(iname_list))
        matchNames_list.sort()
        print(matchNames_list)

        for ista, isess, iorg_dirpath, iname in zip(self.station, self.session, self.img_folderpaths, matchNames_list):
            create = open(f"{self.outputTxtDirPath}pf4_sortImages_{self.dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"3\n"
                         f"{iorg_dirpath}/\n"
                         f"{self.inputCSVDirPath}{iname}_Meta.csv\n"
                         f"{sortedInput}\n")
            create.close()

            self.success_label = ttk.Label(self.sw.scrollwindow, text="`*.TXT` FILES CREATED SUCCESSFULLY !!!"
                                                                      "\nPlease adjust the steps for a new run")
            self.success_label.grid(row=36, sticky='n', pady=4)

        destroy_these = [self.inputCSVDir_label, self.exampleImgPath_label,
                         self.confirmExampleImgPath_btn, self.sessName_label,
                         self.sessName_entry, self.stationName_label, self.stationName_entry,
                         self.sessStaConfirm_btn, self.sorted_label, self.sorted_entry,
                         self.outputTxtDir_btn, self.sortImagesTxt_btn,
                         self.outputTxtDir_label, self.success_label]

        for widget in destroy_these:
            widget.destroy()

        # Delete existing lists
        self.org_img_dirpath.clear()
        self.img_folderpaths.clear()
        self.station.clear()
        self.session.clear()
        self.dataset_station.clear()
        self.station_session.clear()
        csv_withoutExt.clear()
        iname_list.clear()
        matchNames_list.clear()

        print("\nTHE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
              "\nPlease adjust the previous steps for a new run")


"""
------------------------------------------------------------------------------------------------------------------------
#5 | BatchRun Create Combined TXT Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_CombinedTXT(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.rootDir = os.path.abspath(os.curdir)
        self.txtDirPath = None
        self.txtDirPathLabel = None
        self.chosenFunctionLabel = None

        txtDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Select the folder where "
                                                             "all `*.txt` files are located in",
                                  command=self.txtInputDir)
        txtDirButton.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='')

        self.chosenFunctionLabel = ttk.Label(self.sw.scrollwindow,
                                             text="2/ Which 'PROCESSING FUNCTION' is this combined\n`.txt`"
                                                  " file for? (please answer with '1', '3', or '4') ")
        self.chosenFunctionLabel.grid(row=2, sticky='n')

        self.chosenFunctionEntry = ttk.Entry(self.sw.scrollwindow)
        self.chosenFunctionEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='n')

        self.createCombinedTxtButton = ttk.Button(self.sw.scrollwindow, text="CREATE THE COMBINED TXT FILE",
                                                  command=self.createCombinedTXT)
        self.createCombinedTxtButton.grid(row=4, ipadx=10, ipady=10, pady=4, sticky='')

        batch_btn = ttk.Button(self.sw.scrollwindow, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=6, ipadx=10, ipady=10, pady=4, sticky='')

    def txtInputDir(self):
        txtDir = filedialog.askdirectory(initialdir=self.rootDir + "/metadata",
                                         title='Select the folder contains all the `*.txt` files')
        self.txtDirPath = str(txtDir) + "/"

        self.txtDirPathLabel = ttk.Label(self.sw.scrollwindow, text=self.txtDirPath)
        self.txtDirPathLabel.grid(row=1, ipadx=10, ipady=10, sticky='')

        print('\nSELECTED FOLDER WHICH CONTAINS ALL THE TXT FILES: ' + '\n' + str(txtDir))

    def createCombinedTXT(self):

        path_txtcmd_dir = self.txtDirPath
        path_txtcmd_dir = path_txtcmd_dir.replace("\\", "/")

        chosenFunction = str(self.chosenFunctionEntry.get())

        output_txtfile_dir = "/".join(list(path_txtcmd_dir.split('/')[:-2])) + "/"

        for (dirpath, dirnames, filenames) in os.walk(path_txtcmd_dir):

            for ifilenames in filenames:
                fullpaths = Path(os.path.join(dirpath, ifilenames))
                new_fullpath = str(fullpaths).replace("\\", "/")

                f = open(f"{output_txtfile_dir}pf{chosenFunction}_combinedCmds.txt", "a")
                f.write(f"'python main.py < '\n'{new_fullpath} '\n"
                        f"'&& '\n")
                f.close()

                self.txtDirPathLabel.destroy()

                self.createCombinedTxtButton.config(text="THE COMBINED `.TXT` FILE WAS CREATED SUCCESSFULLY !!!"
                                                         "\nPlease adjust the previous steps for the new run")

        self.chosenFunctionEntry.delete(0, 'end')

        print("\nTHE COMBINED `.TXT` FILE WAS CREATED SUCCESSFULLY !!!"
              "\nPlease adjust the previous steps for the new run")


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    page = BatchPage()
    page.mainloop()
