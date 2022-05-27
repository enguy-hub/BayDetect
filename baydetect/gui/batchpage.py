from pathlib import Path
from tkinter import ttk, filedialog
from baydetect.gui.scrollpage import ScrolledPage

import os
import fnmatch
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

        batc1_btn = ttk.Button(self.sw.scrollwindow, text="1/ Create `.txt` files needed to batch-run one of the "
                                                          "`Processing\nFunction` except for the `Run MegaDetector` "
                                                          "function",
                               command=lambda: master.switch_frame("Batchrun Processing Functions"))
        batc1_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        batc2_btn = ttk.Button(self.sw.scrollwindow,
                               text="2/ Create a combined '.txt' file for all the `.txt` files created, which"
                                    " has\n the commands needed to execute `pf_batchrun()` from `batchrun.py`",
                               command=lambda: master.switch_frame("Batchrun Create Combined TXT"))
        batc2_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        batc3_btn = ttk.Button(self.sw.scrollwindow,
                               text="3/ Create the `.txt` file needed for executing MegaDetector repeatedly",
                               command=lambda: master.switch_frame("Batchrun Run MegaDetector"))
        batc3_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)


"""
------------------------------------------------------------------------------------------------------------------------
BatchRun Processing Functions Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_ProcessingFunctions(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        # -------------------------------------- #
        # Common variables | To keep
        self.inputDirPath = None
        self.org_img_dirpath = []
        self.img_paths = []
        self.dataset_station = []
        self.station = []
        self.session = []
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
        self.inputDirLabel = None

        self.yesPFChoiceLabel = None
        self.yesJSONCreator_btn = None
        self.yesCSVConverter_btn = None
        self.yesSortImages_btn = None

        self.noPFChoiceLabel = None
        self.noJSONCreator_btn = None
        self.noCSVConverter_btn = None
        self.noSortImages_btn = None

        self.successLabel = None

        # -------------------------------------- #
        # Variables for JSON Creator `batch-run`
        self.yesInputJSONDirPath = None
        self.yesOutputTxtDirPath1 = None

        self.noInputJSONDirPath = None
        self.noOutputTxtDirPath1 = None

        # To destroy | JSON Creator `batch-run` widget variables
        self.yesInputJSONDirButton = None
        self.yesInputJSONDirLabel = None
        self.yesOutputTxtDirButton1 = None
        self.yesOutputTxtDirLabel1 = None
        self.yesCreateJSONTxtButton = None

        self.noInputJSONDirButton = None
        self.noInputJSONDirLabel = None
        self.noOutputTxtDirButton1 = None
        self.noOutputTxtDirLabel1 = None
        self.noCreateJSONTxtButton = None

        # -------------------------------------- #
        # Variables for CSV Convertor `batch-run`
        self.yesMDJSONDirPath = None
        self.yesOutputCSVDirPath = None
        self.yesOutputTxtDirPath2 = None

        self.noMDJSONDirPath = None
        self.noOutputCSVDirPath = None
        self.noOutputTxtDirPath2 = None

        # To destroy | CSV Convertor `batch-run` widget variables
        self.yesMDJSONDirButton = None
        self.yesMDJSONDirLabel = None
        self.yesOutputCSVDirButton = None
        self.yesOutputCSVDirLabel = None
        self.yesOutputTxtDirButton2 = None
        self.yesOutputTxtDirLabel2 = None
        self.yesConvertCSVTxtButton = None

        self.noMDJSONDirButton = None
        self.noMDJSONDirLabel = None
        self.noOutputCSVDirButton = None
        self.noOutputCSVDirLabel = None
        self.noOutputTxtDirButton2 = None
        self.noOutputTxtDirLabel2 = None
        self.noConvertCSVTxtButton = None

        # -------------------------------------- #
        # Variables for Image Sorter `batch-run`
        self.yesInputCSVDirPath = None
        self.yesOutputTxtDirPath3 = None

        self.noInputCSVDirPath = None
        self.noOutputTxtDirPath3 = None

        # To destroy | CSV Convertor `batch-run` widget variables
        self.yesInputCSVDirButton = None
        self.yesInputCSVDirLabel = None
        self.yesSortedLabel = None
        self.yesSortedEntry = None
        self.yesOutputTxtDirButton3 = None
        self.yesOutputTxtDirLabel3 = None
        self.yesSortImagesTxtButton = None

        self.noInputCSVDirButton = None
        self.noInputCSVDirLabel = None
        self.noSortedLabel = None
        self.noSortedEntry = None
        self.noOutputTxtDirButton3 = None
        self.noOutputTxtDirLabel3 = None
        self.noSortImagesTxtButton = None

        inputDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select the `parent-folder` where "
                                                               "all the `station-folders` are located in.",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='n')

        pattern1Label = ttk.Label(self.sw.scrollwindow,
                                  text="2/ Please enter the common pattern in the names of the folders where "
                                       "all the image\nare stored in (please ends with an asterisk like so: "
                                       "`2020*`, ``Session*` or `100CU*`): ")
        pattern1Label.grid(row=2, sticky='n')

        self.pattern1Entry = ttk.Entry(self.sw.scrollwindow)
        self.pattern1Entry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='n')

        pattern2CheckLabel = ttk.Label(self.sw.scrollwindow,
                                       text="3/ Is there a second common pattern in the names of the"
                                            "\nsub-folders in the above-mentioned folders? (`Y` or `N`): ")
        pattern2CheckLabel.grid(row=4, sticky='')

        self.pattern2CheckYes_btn = ttk.Button(self.sw.scrollwindow, text="Yes", command=self.secondPattern)
        self.pattern2CheckYes_btn.grid(row=5, ipady=5, ipadx=5, sticky='n')

        self.pattern2CheckNo_btn = ttk.Button(self.sw.scrollwindow, text="No", command=self.clickedNo)
        self.pattern2CheckNo_btn.grid(row=6, ipady=5, ipadx=5, sticky='n')

        batch_btn = ttk.Button(self.sw.scrollwindow, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=21, ipady=5, ipadx=5, pady=4, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=22, ipady=5, ipadx=5, pady=4, sticky='n')

    def inputDir(self):

        inputDir = filedialog.askdirectory(title='Please select the image folder')
        self.inputDirPath = str(inputDir) + "/"
        # self.inputDirPath.replace("\\", "/")

        print(self.inputDirPath)

        self.inputDirLabel = ttk.Label(self.sw.scrollwindow, text=self.inputDirPath)
        self.inputDirLabel.grid(row=1, pady=4, sticky='n')

    """
        NO @ Question 3 | Batch Run | Initial functions
    """

    def clickedNo(self):

        self.pattern2CheckYes_btn['state'] = 'disabled'

        self.pattern1 = self.pattern1Entry.get()

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for dirname in fnmatch.filter(dirs, self.pattern1):
                self.org_img_dirpath.append(os.path.join(path, dirname).replace("\\", "/"))

        for idirpaths in self.org_img_dirpath:
            for dirpath, dirnames, files in os.walk(idirpaths):
                if files:
                    self.img_paths.append(''.join(idirpaths.split()[-1]))
                    self.dataset_station.append(''.join(idirpaths.split('/')[9]))
                    self.session.append(''.join(idirpaths.split('/')[10]))
                if not files:
                    pass

        for name in self.dataset_station:
            self.dataset = ''.join(name.split('_')[0])
            self.station.append('_'.join(name.split('_')[1:]))

        print(self.dataset)
        print(self.station)
        print(self.session)

        self.noPFChoiceLabel = ttk.Label(self.sw.scrollwindow, text="4/ Which `processing function` would you like "
                                                                    "to create the `batch-run` `.txt` files for?")
        self.noPFChoiceLabel.grid(row=7, sticky='n')

        self.noJSONCreator_btn = ttk.Button(self.sw.scrollwindow, text="`Batch-input` JSON Creator",
                                            command=self.noJSONCreator)
        self.noJSONCreator_btn.grid(row=8, ipady=5, ipadx=5, sticky='n')

        self.noCSVConverter_btn = ttk.Button(self.sw.scrollwindow,
                                             text="Convert `Mega-detected` JSON to CSV `Metadata` Files",
                                             command=self.noCSVConvertor)
        self.noCSVConverter_btn.grid(row=9, ipady=5, ipadx=5, sticky='n')

        self.noSortImages_btn = ttk.Button(self.sw.scrollwindow,
                                           text="Sort the images using CSV `Metadata` files",
                                           command=self.noImageSorter)
        self.noSortImages_btn.grid(row=10, ipady=5, ipadx=5, sticky='n')

    """
        NO @ Question 3 | Batch Run | JSON Creator
    """

    def noJSONCreator(self):

        self.noCSVConverter_btn['state'] = 'disabled'
        self.noSortImages_btn['state'] = 'disabled'

        self.noInputJSONDirButton = ttk.Button(self.sw.scrollwindow,
                                               text="5/ Please select the folder where you want all "
                                                    "the '*_BatchInput.json' files to be saved at",
                                               command=self.noInputJSONDir)
        self.noInputJSONDirButton.grid(row=11, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noOutputTxtDirButton1 = ttk.Button(self.sw.scrollwindow, text="6/ Please select the folder where you "
                                                                           "want all the '.txt' files to be saved at",
                                                command=self.noOutputTxtDir1)
        self.noOutputTxtDirButton1.grid(row=13, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noCreateJSONTxtButton = ttk.Button(self.sw.scrollwindow,
                                                text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` JSON CREATOR",
                                                command=self.noCreateJSONTxt)
        self.noCreateJSONTxtButton.grid(row=15, ipadx=10, ipady=10, pady=4, sticky='n')

    def noInputJSONDir(self):
        noInputJSONDir = filedialog.askdirectory(title='Please select the output folder for `batch-input` JSON files')
        self.noInputJSONDirPath = str(noInputJSONDir) + "/"
        self.noInputJSONDirPath.replace("\\", "/")

        self.noInputJSONDirLabel = ttk.Label(self.sw.scrollwindow,
                                             text=self.noInputJSONDirPath)
        self.noInputJSONDirLabel.grid(row=12, pady=4, sticky='n')

        print('SELECTED JSON FOLDER: ' + self.noInputJSONDirPath)

    def noOutputTxtDir1(self):
        noOutputTxtDir1 = filedialog.askdirectory(title='Please select the folder for the `.txt` files')
        self.noOutputTxtDirPath1 = str(noOutputTxtDir1) + "/"
        self.noOutputTxtDirPath1.replace("\\", "/")

        self.noOutputTxtDirLabel1 = ttk.Label(self.sw.scrollwindow,
                                              text=self.noOutputTxtDirPath1)
        self.noOutputTxtDirLabel1.grid(row=14, pady=4, sticky='n')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.noOutputTxtDirPath1)

    def noCreateJSONTxt(self):

        jsonInputDir = self.noInputJSONDirPath
        txtOutputDir = self.noOutputTxtDirPath1

        for ista, isess, ipaths in zip(self.station, self.session, self.img_paths):
            create = open(f"{txtOutputDir}{self.dataset}_createBIJSON_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}{self.dataset}_{ista}_{isess}_BI.json\n")
            create.close()

            self.successLabel = ttk.Label(self.sw.scrollwindow, text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                                     "\nPlease adjust the previous steps for a new run")
            self.successLabel.grid(row=23, sticky='n', pady=4)  #

            destroy_these = [self.inputDirLabel,
                             self.noPFChoiceLabel, self.noJSONCreator_btn,
                             self.noCSVConverter_btn,  # self.noSortImages_btn,
                             self.noInputJSONDirButton, self.noInputJSONDirLabel,
                             self.noOutputTxtDirButton1, self.noOutputTxtDirLabel1,
                             self.noCreateJSONTxtButton]

            for widget in destroy_these:
                widget.destroy()

            self.pattern2CheckYes_btn['state'] = 'normal'

    """
        NO @ Question 3 | Batch Run | CSV Convertor
    """

    def noCSVConvertor(self):

        self.noJSONCreator_btn['state'] = 'disabled'
        self.noSortImages_btn['state'] = 'disabled'

        self.noMDJSONDirButton = ttk.Button(self.sw.scrollwindow, text="5/ Please select the folder where all the "
                                                                       "'*_MegaDetected.json' files are currently "
                                                                       "saved at",
                                            command=self.noMDJSONDir)
        self.noMDJSONDirButton.grid(row=11, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noOutputCSVDirButton = ttk.Button(self.sw.scrollwindow, text="6/ Please select the folder where all "
                                                                          "the '*_Meta.csv' files will be saved at",
                                               command=self.noOutputCSVDir)
        self.noOutputCSVDirButton.grid(row=13, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noOutputTxtDirButton2 = ttk.Button(self.sw.scrollwindow, text="7/ Please select the folder where "
                                                                           "all the '.txt' files will be saved at",
                                                command=self.noOutputTxtDir2)
        self.noOutputTxtDirButton2.grid(row=15, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noConvertCSVTxtButton = ttk.Button(self.sw.scrollwindow,
                                                text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` CSV CONVERTOR",
                                                command=self.noConvertCSVTxt)
        self.noConvertCSVTxtButton.grid(row=17, ipadx=10, ipady=10, pady=4, sticky='n')

    def noMDJSONDir(self):
        noMDJSONDir = filedialog.askdirectory(title='Please select the folder contains `MegaDetected` JSON files')
        self.noMDJSONDirPath = str(noMDJSONDir) + "/"
        self.noMDJSONDirPath.replace("\\", "/")

        self.noMDJSONDirLabel = ttk.Label(self.sw.scrollwindow, text=self.noMDJSONDirPath)
        self.noMDJSONDirLabel.grid(row=12, pady=4, sticky='n')

        print('SELECTED JSON FOLDER: ' + self.noMDJSONDirPath)

    def noOutputCSVDir(self):
        noOutputCSVDir = filedialog.askdirectory(title='Please select the output folder for the `*_Meta.csv` files')
        self.noOutputCSVDirPath = str(noOutputCSVDir) + "/"
        self.noOutputCSVDirPath.replace("\\", "/")

        self.noOutputCSVDirLabel = ttk.Label(self.sw.scrollwindow,
                                             text=self.noOutputCSVDirPath)
        self.noOutputCSVDirLabel.grid(row=14, pady=4, sticky='n')

        print('SELECTED FOLDER FOR CSV FILES: ' + self.noOutputCSVDirPath)

    def noOutputTxtDir2(self):
        noOutputTxtDir2 = filedialog.askdirectory(title='Please select the output folder for the `.txt` files')
        self.noOutputTxtDirPath2 = str(noOutputTxtDir2) + "/"
        self.noOutputTxtDirPath2.replace("\\", "/")

        self.noOutputTxtDirLabel2 = ttk.Label(self.sw.scrollwindow,
                                              text=self.noOutputTxtDirPath2)
        self.noOutputTxtDirLabel2.grid(row=16, pady=4, sticky='n')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.noOutputTxtDirPath2)

    def noConvertCSVTxt(self):

        mdJSONDir = self.noMDJSONDirPath
        csvDir = self.noOutputCSVDirPath
        txtOutputDir = self.noOutputTxtDirPath2

        md_json_paths = []
        md_json_names = []
        csv_woMeta = []

        for (dirpath, dirnames, filenames) in os.walk(mdJSONDir):
            for ifilenames in filenames:
                md_json_paths.append(os.path.join(dirpath, ifilenames))

            for ifilenames in range(len(filenames)):
                fullnames = filenames[ifilenames]
                json_names, extension = os.path.splitext(fullnames)
                md_json_names.append(json_names)

        for iname in md_json_names:
            icsv_names = '_'.join(iname.split('_')[0:5])
            csv_woMeta.append(icsv_names)

        for ista, isess, iorg_dirpath, imd_json_paths, icsv_woMeta in zip(self.station, self.session,
                                                                          self.org_img_dirpath, md_json_paths,
                                                                          csv_woMeta):
            create = open(f"{txtOutputDir}{self.dataset}_mdJSONToCSV_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"2\n"
                         f"{iorg_dirpath}/\n"
                         f"{imd_json_paths}\n"
                         f"{csvDir}{icsv_woMeta}_Meta.csv\n")
            create.close()

            self.successLabel = ttk.Label(self.sw.scrollwindow, text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                                     "\nPlease adjust the previous steps for a new run")
            self.successLabel.grid(row=23, sticky='n', pady=4)  #

            self.successLabel.after(2000, lambda: self.successLabel.destroy())

            destroy_these = [self.inputDirLabel,
                             self.noPFChoiceLabel, self.noJSONCreator_btn,
                             self.noCSVConverter_btn,  # self.noSortImages_btn,
                             self.noMDJSONDirButton, self.noMDJSONDirLabel,
                             self.noOutputCSVDirButton, self.noOutputCSVDirLabel,
                             self.noOutputTxtDirButton2, self.noOutputTxtDirLabel2,
                             self.noConvertCSVTxtButton]

            for widget in destroy_these:
                widget.destroy()

            self.pattern2CheckYes_btn['state'] = 'normal'

    """
        NO @ Question 3 | Batch Run | Image Sorter
    """

    def noImageSorter(self):

        self.noJSONCreator_btn['state'] = 'disabled'
        self.noCSVConverter_btn['state'] = 'disabled'

        self.noInputCSVDirButton = ttk.Button(self.sw.scrollwindow,
                                              text="5/ Please select the folder where all the "
                                                   "'*_Meta.csv' files are currently saved at: ",
                                              command=self.noInputCSVDir)
        self.noInputCSVDirButton.grid(row=11, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noSortedLabel = ttk.Label(self.sw.scrollwindow,
                                       text="6/ Would you like the 'sorted-images' to be saved in a separate "
                                            "folder called `*_Sorted`? (please answer with 'Y' or 'N') ")
        self.noSortedLabel.grid(row=13, sticky='n')

        self.noSortedEntry = ttk.Entry(self.sw.scrollwindow)
        self.noSortedEntry.grid(row=14, ipady=10, ipadx=10, pady=4, sticky='n')

        self.noOutputTxtDirButton3 = ttk.Button(self.sw.scrollwindow, text="7/ Please select the folder where you "
                                                                           "want all the '.txt' files to be saved at",
                                                command=self.noOutputTxtDir3)
        self.noOutputTxtDirButton3.grid(row=15, ipadx=10, ipady=10, pady=4, sticky='n')

        self.noSortImagesTxtButton = ttk.Button(self.sw.scrollwindow,
                                                text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` IMAGE SORTER",
                                                command=self.noSortImageTxt)
        self.noSortImagesTxtButton.grid(row=17, ipadx=10, ipady=10, pady=4, sticky='n')

    def noInputCSVDir(self):
        noInputCSVDir = filedialog.askdirectory(title='Please select the output folder for `batch-input` JSON files')
        self.noInputCSVDirPath = str(noInputCSVDir) + "/"
        self.noInputCSVDirPath.replace("\\", "/")

        self.noInputCSVDirLabel = ttk.Label(self.sw.scrollwindow, text=self.noInputCSVDirPath)
        self.noInputCSVDirLabel.grid(row=12, pady=4, sticky='n')

        print('SELECTED CSV FOLDER: ' + self.noInputCSVDirPath)

    def noOutputTxtDir3(self):
        noOutputTxtDir3 = filedialog.askdirectory(title='Please select the folder for the `.txt` files')
        self.noOutputTxtDirPath3 = str(noOutputTxtDir3) + "/"
        self.noOutputTxtDirPath3.replace("\\", "/")

        self.noOutputTxtDirLabel3 = ttk.Label(self.sw.scrollwindow, text=self.noOutputTxtDirPath3)
        self.noOutputTxtDirLabel3.grid(row=16, pady=4, sticky='n')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.noOutputTxtDirPath3)

    def noSortImageTxt(self):

        csvInputDir = self.noInputCSVDirPath
        txtOutputDir = self.noOutputTxtDirPath3
        sortedInput = self.noSortedEntry.get()

        CSV_paths = []

        for (dirpath, dirnames, filenames) in os.walk(csvInputDir):
            for ifilenames in filenames:
                CSV_paths.append(os.path.join(dirpath, ifilenames))

        for ista, isess, iorg_dirpath, icsv in zip(self.station, self.session, self.org_img_dirpath, CSV_paths):
            create = open(f"{txtOutputDir}{self.dataset}_sortImages_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"3\n"
                         f"{iorg_dirpath}/\n"
                         f"{icsv}\n"
                         f"{sortedInput}\n")
            create.close()

            self.successLabel = ttk.Label(self.sw.scrollwindow, text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                                     "\nPlease adjust the previous steps for a new run")
            self.successLabel.grid(row=23, sticky='n', pady=4)  #

            destroy_these = [self.inputDirLabel,
                             self.noPFChoiceLabel, self.noJSONCreator_btn,
                             self.noCSVConverter_btn, self.noSortImages_btn,
                             self.noInputCSVDirButton, self.noInputCSVDirLabel,
                             self.noSortedLabel, self.noSortedEntry,
                             self.noOutputTxtDirButton3, self.noOutputTxtDirLabel3,
                             self.noSortImagesTxtButton]

            for widget in destroy_these:
                widget.destroy()

            self.pattern2CheckYes_btn['state'] = 'normal'

    """
        YES @ Question 3 | Batch Run | Initial functions
    """

    def secondPattern(self):

        self.pattern2CheckNo_btn['state'] = 'disable'

        self.pattern1 = self.pattern1Entry.get()

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for dirname_p1 in fnmatch.filter(dirs, self.pattern1):
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
        self.confirmPattern2.grid(row=9, ipadx=10, ipady=10, pady=4, sticky='n')

    def clickedYes(self):

        self.pattern2 = self.pattern2Entry.get()

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for dirname_p2 in fnmatch.filter(dirs, self.pattern2):
                self.pattern2_list.append(dirname_p2)

        for ip1, ip2 in zip(self.pattern1_list, self.pattern2_list):
            self.org_img_dirpath.append(os.path.join(ip1, ip2).replace("\\", "/"))

        for idirpaths in self.org_img_dirpath:
            for dirpath, dirnames, files in os.walk(idirpaths):
                if files:
                    self.img_paths.append(''.join(idirpaths.split()[-1]))
                    self.dataset_station.append(''.join(idirpaths.split('/')[9]))
                    self.session.append(''.join(idirpaths.split('/')[10]))
                if not files:
                    pass

        for name in self.dataset_station:
            self.dataset = ''.join(name.split('_')[0])
            self.station.append('_'.join(name.split('_')[1:]))

        print(self.dataset)
        print(self.station)
        print(self.session)

        self.yesPFChoiceLabel = ttk.Label(self.sw.scrollwindow, text="4/ Which `processing function` would you like "
                                                                     "to create the batch-run's `*.txt` files for?")
        self.yesPFChoiceLabel.grid(row=10, sticky='')

        self.yesJSONCreator_btn = ttk.Button(self.sw.scrollwindow, text="`Batch-input` JSON Creator",
                                             command=self.yesJSONCreator)
        self.yesJSONCreator_btn.grid(row=11, ipady=5, ipadx=5, sticky='n')

        self.yesCSVConverter_btn = ttk.Button(self.sw.scrollwindow,
                                              text="Convert `Mega-detected` JSON to CSV `Metadata` Files",
                                              command=self.yesCSVConvertor)
        self.yesCSVConverter_btn.grid(row=12, ipady=5, ipadx=5, sticky='n')

        self.yesSortImages_btn = ttk.Button(self.sw.scrollwindow, text="Sort the images using CSV `metadata` files",
                                            command=self.yesImageSorter)
        self.yesSortImages_btn.grid(row=13, ipady=5, ipadx=5, sticky='n')

    """
        YES @ Question 3 | Batch Run | JSON Creator
    """

    def yesJSONCreator(self):

        self.yesCSVConverter_btn['state'] = 'disabled'
        self.yesSortImages_btn['state'] = 'disabled'

        self.yesInputJSONDirButton = ttk.Button(self.sw.scrollwindow, text="5/ Please select the folder where all the "
                                                                           "'*_BatchInput.json' files will be saved at",
                                                command=self.yesInputJSONDir)
        self.yesInputJSONDirButton.grid(row=14, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesOutputTxtDirButton1 = ttk.Button(self.sw.scrollwindow, text="6/ Please select the folder where "
                                                                            "all the '.txt' files will be saved at",
                                                 command=self.yesOutputTxtDir)
        self.yesOutputTxtDirButton1.grid(row=16, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesCreateJSONTxtButton = ttk.Button(self.sw.scrollwindow,
                                                 text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` JSON CREATOR",
                                                 command=self.yesCreateJSONTxt)
        self.yesCreateJSONTxtButton.grid(row=18, ipadx=10, ipady=10, pady=4, sticky='n')

    def yesInputJSONDir(self):
        yesInputJSONDir = filedialog.askdirectory(title='Please select the folder contains `batch-input` JSON files')
        self.yesInputJSONDirPath = str(yesInputJSONDir) + "/"
        self.yesInputJSONDirPath.replace("\\", "/")

        self.yesInputJSONDirLabel = ttk.Label(self.sw.scrollwindow,
                                              text=self.yesInputJSONDirPath)
        self.yesInputJSONDirLabel.grid(row=15, pady=4, sticky='n')

        print('SELECTED JSON FOLDER: ' + self.yesInputJSONDirPath)

    def yesOutputTxtDir(self):
        yesOutputTxtDir1 = filedialog.askdirectory(title='Please select the folder for the `.txt` files')
        self.yesOutputTxtDirPath1 = str(yesOutputTxtDir1) + "/"
        self.yesOutputTxtDirPath1.replace("\\", "/")

        self.yesOutputTxtDirLabel1 = ttk.Label(self.sw.scrollwindow, text=self.yesOutputTxtDirPath1)
        self.yesOutputTxtDirLabel1.grid(row=17, pady=4, sticky='n')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.yesOutputTxtDirPath1)

    def yesCreateJSONTxt(self):

        jsonInputDir = self.yesInputJSONDirPath
        txtOutputDir = self.yesOutputTxtDirPath1

        for ista, isess, ipaths in zip(self.station, self.session, self.img_paths):
            create = open(f"{txtOutputDir}{self.dataset}_createBIJSON_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}/{self.dataset}_{ista}_{isess}_BI.json\n")
            create.close()

            self.successLabel = ttk.Label(self.sw.scrollwindow, text="`.TXT` FILE(S) CREATED SUCCESSFULLY !!!"
                                                                     "\nPlease adjust the previous steps for a new run")
            self.successLabel.grid(row=23, pady=4, sticky='n')

            destroy_these = [self.inputDirLabel,
                             self.pattern2Label, self.pattern2Entry, self.confirmPattern2,
                             self.yesPFChoiceLabel, self.yesJSONCreator_btn,
                             self.yesCSVConverter_btn,  self.yesSortImages_btn,
                             self.yesInputJSONDirButton, self.yesInputJSONDirLabel,
                             self.yesOutputTxtDirButton1, self.yesOutputTxtDirLabel1,
                             self.yesCreateJSONTxtButton]

            for widget in destroy_these:
                widget.destroy()

            self.pattern2CheckNo_btn['state'] = 'normal'

    """
         YES @ Question 3 | Batch Run | CSV Convertor
     """

    def yesCSVConvertor(self):

        self.yesJSONCreator_btn['state'] = 'disabled'
        self.yesSortImages_btn['state'] = 'disabled'

        self.yesMDJSONDirButton = ttk.Button(self.sw.scrollwindow, text="5/ Please select the folder where all the "
                                                                        "'*_MegaDetected.json' files are currently "
                                                                        "saved at",
                                             command=self.yesMDJSONDir)
        self.yesMDJSONDirButton.grid(row=14, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesOutputCSVDirButton = ttk.Button(self.sw.scrollwindow, text="6/ Please select the folder where all "
                                                                           "the '*_Meta.csv' files will be saved at",
                                                command=self.yesOutputCSVDir)
        self.yesOutputCSVDirButton.grid(row=16, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesOutputTxtDirButton2 = ttk.Button(self.sw.scrollwindow, text="7/ Please select the folder where "
                                                                            "all the '.txt' files will be saved at",
                                                 command=self.yesOutputTxtDir2)
        self.yesOutputTxtDirButton2.grid(row=18, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesConvertCSVTxtButton = ttk.Button(self.sw.scrollwindow,
                                                 text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` CSV CONVERTOR",
                                                 command=self.yesConvertCSVTxt)
        self.yesConvertCSVTxtButton.grid(row=20, ipadx=10, ipady=10, pady=4, sticky='n')

    def yesMDJSONDir(self):
        yesMDJSONDir = filedialog.askdirectory(title='Please select the folder contains `MegaDetected` JSON files')
        self.yesMDJSONDirPath = str(yesMDJSONDir) + "/"
        self.yesMDJSONDirPath.replace("\\", "/")

        self.yesMDJSONDirLabel = ttk.Label(self.sw.scrollwindow,
                                           text=self.yesMDJSONDirPath)
        self.yesMDJSONDirLabel.grid(row=15, pady=4, sticky='n')

        print('SELECTED JSON FOLDER: ' + self.yesMDJSONDirPath)

    def yesOutputCSVDir(self):
        yesOutputCSVDir = filedialog.askdirectory(title='Please select the output folder for the `*_Meta.csv` files')
        self.yesOutputCSVDirPath = str(yesOutputCSVDir) + "/"
        self.yesOutputCSVDirPath.replace("\\", "/")

        self.yesOutputCSVDirLabel = ttk.Label(self.sw.scrollwindow, text=self.yesOutputCSVDirPath)
        self.yesOutputCSVDirLabel.grid(row=17, pady=4, sticky='n')

        print('SELECTED FOLDER FOR CSV FILES: ' + self.yesOutputCSVDirPath)

    def yesOutputTxtDir2(self):
        yesOutputTxtDir2 = filedialog.askdirectory(title='Please select the output folder for the `.txt` files')
        self.yesOutputTxtDirPath2 = str(yesOutputTxtDir2) + "/"
        self.yesOutputTxtDirPath2.replace("\\", "/")

        self.yesOutputTxtDirLabel2 = ttk.Label(self.sw.scrollwindow, text=self.yesOutputTxtDirPath2)
        self.yesOutputTxtDirLabel2.grid(row=19, pady=4, sticky='n')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.yesOutputTxtDirPath2)

    def yesConvertCSVTxt(self):
        mdJSONDir = self.yesMDJSONDirPath
        csvDir = self.yesOutputCSVDirPath
        txtOutputDir = self.yesOutputTxtDirPath2

        md_json_paths = []
        md_json_names = []
        csv_woMeta = []

        for (dirpath, dirnames, filenames) in os.walk(mdJSONDir):
            for ifilenames in filenames:
                md_json_paths.append(os.path.join(dirpath, ifilenames))

            for ifilenames in range(len(filenames)):
                fullnames = filenames[ifilenames]
                json_names, extension = os.path.splitext(fullnames)
                md_json_names.append(json_names)

        for iname in md_json_names:
            icsv_names = '_'.join(iname.split('_')[0:5])
            csv_woMeta.append(icsv_names)

        for ista, isess, iorg_dirpath, imd_json_paths, icsv_woMeta in zip(self.station, self.session,
                                                                          self.org_img_dirpath, md_json_paths,
                                                                          csv_woMeta):
            create = open(f"{txtOutputDir}{self.dataset}_mdJSONToCSV_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"2\n"
                         f"{iorg_dirpath}/\n"
                         f"{imd_json_paths}\n"
                         f"{csvDir}{icsv_woMeta}_Meta.csv\n")
            create.close()

            self.successLabel = ttk.Label(self.sw.scrollwindow, text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                                     "\nPlease adjust the previous steps for a new run")
            self.successLabel.grid(row=23, sticky='n', pady=4)  #

            # self.successLabel.after(2000, lambda: self.successLabel.destroy())

            destroy_these = [self.inputDirLabel,
                             self.pattern2Label, self.pattern2Entry, self.confirmPattern2,
                             self.yesPFChoiceLabel, self.yesJSONCreator_btn,
                             self.yesCSVConverter_btn,  self.yesSortImages_btn,
                             self.yesMDJSONDirButton, self.yesMDJSONDirLabel,
                             self.yesOutputCSVDirButton, self.yesOutputCSVDirLabel,
                             self.yesOutputTxtDirButton2, self.yesOutputTxtDirLabel2,
                             self.yesConvertCSVTxtButton]

            for widget in destroy_these:
                widget.destroy()

            self.pattern2CheckNo_btn['state'] = 'normal'

    """
        YES @ Question 3 | Batch Run | Image Sorter
    """

    def yesImageSorter(self):
        self.yesJSONCreator_btn['state'] = 'disabled'
        self.yesCSVConverter_btn['state'] = 'disabled'

        self.yesInputCSVDirButton = ttk.Button(self.sw.scrollwindow,
                                               text="5/ Please select the folder where all the "
                                                    "'*_Meta.csv' files are currently saved at: ",
                                               command=self.yesInputCSVDir)
        self.yesInputCSVDirButton.grid(row=14, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesSortedLabel = ttk.Label(self.sw.scrollwindow,
                                        text="6/ Would you like the 'sorted-images' to be saved in a separate "
                                             "folder called `*_Sorted`? (please answer with 'Y' or 'N') ")
        self.yesSortedLabel.grid(row=16, sticky='n')

        self.yesSortedEntry = ttk.Entry(self.sw.scrollwindow)
        self.yesSortedEntry.grid(row=17, ipady=10, ipadx=10, pady=4, sticky='n')

        self.yesOutputTxtDirButton3 = ttk.Button(self.sw.scrollwindow, text="7/ Please select the folder where you "
                                                                            "want all the '.txt' files to be saved at",
                                                 command=self.yesOutputTxtDir3)
        self.yesOutputTxtDirButton3.grid(row=18, ipadx=10, ipady=10, pady=4, sticky='n')

        self.yesSortImagesTxtButton = ttk.Button(self.sw.scrollwindow,
                                                 text="CREATE TXT FILE(S) FOR `BATCH-RUNNING` IMAGE SORTER",
                                                 command=self.yesSortImageTxt)
        self.yesSortImagesTxtButton.grid(row=20, ipadx=10, ipady=10, pady=4, sticky='n')

    def yesInputCSVDir(self):
        yesInputCSVDir = filedialog.askdirectory(title='Please select the output folder for `batch-input` JSON files')
        self.yesInputCSVDirPath = str(yesInputCSVDir) + "/"
        self.yesInputCSVDirPath.replace("\\", "/")

        self.yesInputCSVDirLabel = ttk.Label(self.sw.scrollwindow, text=self.yesInputCSVDirPath)
        self.yesInputCSVDirLabel.grid(row=15, pady=4, sticky='n')

        print('SELECTED CSV FOLDER: ' + self.yesInputCSVDirPath)

    def yesOutputTxtDir3(self):
        yesOutputTxtDir3 = filedialog.askdirectory(title='Please select the folder for the `.txt` files')
        self.yesOutputTxtDirPath3 = str(yesOutputTxtDir3) + "/"
        self.yesOutputTxtDirPath3.replace("\\", "/")

        self.yesOutputTxtDirLabel3 = ttk.Label(self.sw.scrollwindow, text=self.yesOutputTxtDirPath3)
        self.yesOutputTxtDirLabel3.grid(row=19, pady=4, sticky='n')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.yesOutputTxtDirPath3)

    def yesSortImageTxt(self):
        csvInputDir = self.yesInputCSVDirPath
        txtOutputDir = self.yesOutputTxtDirPath3
        sortedInput = self.yesSortedEntry.get()

        CSV_paths = []

        for (dirpath, dirnames, filenames) in os.walk(csvInputDir):
            for ifilenames in filenames:
                CSV_paths.append(os.path.join(dirpath, ifilenames))

        print(CSV_paths)

        for ista, isess, iorg_dirpath, icsv in zip(self.station, self.session, self.org_img_dirpath, CSV_paths):
            create = open(f"{txtOutputDir}{self.dataset}_sortImages_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"3\n"
                         f"{iorg_dirpath}/\n"
                         f"{icsv}\n"
                         f"{sortedInput}\n")
            create.close()

            self.successLabel = ttk.Label(self.sw.scrollwindow, text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                                     "\nPlease adjust the previous steps for a new run")
            self.successLabel.grid(row=23, sticky='n', pady=4)  #

            destroy_these = [self.inputDirLabel,
                             self.pattern2Label, self.pattern2Entry, self.confirmPattern2,
                             self.yesPFChoiceLabel, self.yesJSONCreator_btn,
                             self.yesCSVConverter_btn, self.yesSortImages_btn,
                             self.yesInputCSVDirButton, self.yesInputCSVDirLabel,
                             self.yesSortedLabel, self.yesSortedEntry,
                             self.yesOutputTxtDirButton3, self.yesOutputTxtDirLabel3,
                             self.yesSortImagesTxtButton]

            for widget in destroy_these:
                widget.destroy()

            self.pattern2CheckNo_btn['state'] = 'normal'


"""
------------------------------------------------------------------------------------------------------------------------
BatchRun Create Combined TXT Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_CombinedTXT(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.txtDirPath = None
        self.txtDirPathLabel = None

        txtDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select the folder where all "
                                                             "`*.txt` files are located in",
                                  command=self.txtInputDir)
        txtDirButton.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='')

        self.createCombinedTxtButton = ttk.Button(self.sw.scrollwindow, text="CREATE THE COMBINED TXT FILE",
                                                  command=self.createCombinedTXT)
        self.createCombinedTxtButton.grid(row=2, ipadx=10, ipady=10, pady=4, sticky='')

        batch_btn = ttk.Button(self.sw.scrollwindow, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=4, ipadx=10, ipady=10, pady=4, sticky='')

    def txtInputDir(self):
        txtDir = filedialog.askdirectory(title='Please select the folder contains all the `*.txt` files')
        self.txtDirPath = str(txtDir) + "/"

        self.txtDirPathLabel = ttk.Label(self.sw.scrollwindow, text=self.txtDirPath)
        self.txtDirPathLabel.grid(row=1, ipadx=10, ipady=10, sticky='')

    def createCombinedTXT(self):

        path_txtcmd_dir = self.txtDirPath
        path_txtcmd_dir = path_txtcmd_dir.replace("\\", "/")

        output_txtfile_dir = "/".join(list(path_txtcmd_dir.split('/')[:-2])) + "/"

        for (dirpath, dirnames, filenames) in os.walk(path_txtcmd_dir):

            txtcmd_dir_name = ''.join(dirpath.split('/')[-2])
            chosenFunction = ''.join(txtcmd_dir_name.split('_')[1])
            dataset_name = ''.join(txtcmd_dir_name.split())[:2]

            for ifilenames in filenames:
                fullpaths = Path(os.path.join(dirpath, ifilenames))
                new_fullpath = str(fullpaths).replace("\\", "/")

                f = open(f"{output_txtfile_dir}{dataset_name}_{chosenFunction}_combinedCmds.txt", "a")
                f.write(f"'python main.py < '\n'{new_fullpath} '\n"
                        f"'&& '\n")
                f.close()

                self.txtDirPathLabel.destroy()

                self.createCombinedTxtButton.config(text="THE COMBINED `.TXT` FILE WAS CREATED SUCCESSFULLY !!!"
                                                         "\nPlease adjust the previous steps for the "
                                                         "new run then CLICK this button to run again")


"""
------------------------------------------------------------------------------------------------------------------------
BatchRun Run MegaDetector Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_RunMegaDetector(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.jsonDirPath = None
        self.jsonDirPathLabel = None

        self.outputTxtDirPath = None
        self.outputTxtDirPathLabel = None

        jsonDirButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select the folder where all "
                                                              "`*_BatchInput.json` files are located in",
                                   command=self.jsonInputDir)
        jsonDirButton.grid(row=0, ipadx=10, ipady=10, pady=4, sticky='ew')

        outputTxtDirButton = ttk.Button(self.sw.scrollwindow, text="2/ Please select the folder where the "
                                                                   "output `.txt` file will be saved at",
                                        command=self.outputTxtDir)
        outputTxtDirButton.grid(row=2, ipadx=10, ipady=10, pady=4, sticky='ew')

        datasetNameLabel = ttk.Label(self.sw.scrollwindow, text="3/ What is the name of the dataset? ")
        datasetNameLabel.grid(row=4, sticky='')

        self.datasetNameEntry = ttk.Entry(self.sw.scrollwindow)
        self.datasetNameEntry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='n')

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

    def jsonInputDir(self):
        jsonDir = filedialog.askdirectory(title='Please select the folder contains `batch-input` JSON files')
        self.jsonDirPath = str(jsonDir) + "/"

        self.jsonDirPathLabel = ttk.Label(self.sw.scrollwindow, text=self.jsonDirPath)
        self.jsonDirPathLabel.grid(row=1, ipadx=10, ipady=10, sticky='')

    def outputTxtDir(self):
        outputTxtDir = filedialog.askdirectory(title='Please select the output folder for the `.txt` files')
        self.outputTxtDirPath = str(outputTxtDir) + "/"

        self.outputTxtDirPathLabel = ttk.Label(self.sw.scrollwindow, text=self.outputTxtDirPath)
        self.outputTxtDirPathLabel.grid(row=3, ipadx=10, ipady=10, sticky='')

    def runMDTxtButton(self):

        json_dir_input = self.jsonDirPath
        output_txtdir = self.outputTxtDirPath
        datasetName = self.datasetNameEntry.get()

        for (dirpath, dirnames, filenames) in os.walk(json_dir_input):
            root_path = dirpath.split("BayDetect")[1]
            root_path = root_path.replace("\\", "/")
            path_withoutBI = root_path.split("BatchInput")[0]

            for ifilenames in range(len(filenames)):
                fullnames = filenames[ifilenames]
                names_withBI, extension = os.path.splitext(fullnames)
                name_withoutBI = '_'.join(names_withBI.split('_')[:-1])

                with open(output_txtdir + datasetName + "_runMD_cmds.txt", "a") as f:
                    f.write(f"'python run_detector_batch.py md_v4.1.0.pb ' \n"
                            f"'..{root_path}{names_withBI}.json ' \n"
                            f"'..{path_withoutBI}MegaDetected/{name_withoutBI}_MD.json ' \n"
                            f"'&& '\n")

                self.jsonDirPathLabel.destroy()
                self.outputTxtDirPathLabel.destroy()

                self.runMDTxtButton.config(text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                "\nPlease adjust the previous steps for the "
                                                "new run then CLICK this button to run again")


if __name__ == "__main__":
    page = BatchPage()
    page.mainloop()
