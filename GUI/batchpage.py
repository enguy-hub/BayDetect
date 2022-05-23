from tkinter import Frame, ttk
from tkinter import filedialog

import os
import fnmatch
from pathlib import Path

LARGE_FONT = ("Calibri", 20)

"""
------------------------------------------------------------------------------------------------------------------------
Batch Page(s) Section
------------------------------------------------------------------------------------------------------------------------
"""


class BatchPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = ttk.Label(self, text="Batch Functions", font=LARGE_FONT)
        label.pack(ipady=10, pady=10, padx=10)

        batc1_btn = ttk.Button(self, text="1/ Create the `.txt` files needed to repeatedly create "
                                          "multiple 'batch-input' JSON files for MegaDetector ",
                               command=lambda: master.switch_frame("Batchrun JSON Creator"))
        batc1_btn.pack(ipadx=10, ipady=10, expand=1)

        batc2_btn = ttk.Button(self, text="2/ Create the `.txt` file needed for executing MegaDetector repeatedly",
                               command=lambda: master.switch_frame("Batchrun Run MegaDetector"))
        batc2_btn.pack(ipadx=10, ipady=10, expand=1)

        batc3_btn = ttk.Button(self, text="3/ Create the `.txt` files needed to create "
                                          "multiple CSV 'metadata' files repeatedly",
                               command=lambda: master.switch_frame("Batchrun CSV Convertor"))
        batc3_btn.pack(ipadx=10, ipady=10, expand=1)

        batc4_btn = ttk.Button(self, text="4/ Create the `.txt` files needed to repeatedly sort images"
                                          "\nof multiple image folders using CSV 'metadata' files ",
                               command=lambda: master.switch_frame("Batchrun Image Sorter"))
        batc4_btn.pack(ipadx=10, ipady=10, expand=1)

        batc5_btn = ttk.Button(self, text="5/ Create a single '.txt' file for one of the function above, this file has "
                                          "the\npython commands needed to execute `pf_batchrun()` from `batchrun.py`",
                               command=lambda: master.switch_frame("Batchrun PyCommands"))
        batc5_btn.pack(ipadx=10, ipady=10, expand=1)

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=10, ipady=10, expand=1)


"""
------------------------------------------------------------------------------------------------------------------------
BatchRun JSON Creator Page
------------------------------------------------------------------------------------------------------------------------
"""


class Batchrun_JSONCreator(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # For clickedNo() and clickedYes()
        self.inputDirPath = None
        self.org_img_dirpath = []
        self.img_paths = []
        self.dataset_station = []
        self.station = []
        self.session = []
        self.dataset = str

        # For secondPattern()
        self.pattern2Entry = None
        self.pattern2Label = None
        self.confirmPattern2 = None

        # For afterYes()
        self.pattern1 = None
        self.pattern2 = None
        self.pattern1_list = []
        self.pattern2_list = []

        # For clickedNo()
        self.noInputJSONDirPath = None
        self.noOutputTxtDirPath = None
        self.noCreateJSONTxtButton = None

        # For clickedYes()
        self.yesInputJSONDirPath = None
        self.yesOutputTxtDirPath = None
        self.yesCreateJSONTxtButton = None

        # To destroy later
        self.yesPFChoiceLabel = None
        self.yesJSONCreatorButton = None
        self.yesOutputTxtDirButton = None
        self.yesOutputTxtDirLabel = None
        self.yesInputJSONDirButton = None
        self.yesInputJSONDirLabel = None

        self.noPFChoiceLabel = None
        self.noJSONCreatorButton = None
        self.noInputJSONDirButton = None
        self.noInputJSONDirLabel = None
        self.noOutputTxtDirButton = None
        self.noOutputTxtDirLabel = None

        inputDirButton = ttk.Button(self, text="1/ Please select the `parent-folder` where "
                                               "all the `station-folders` are located in.",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='ns')

        pattern1Label = ttk.Label(self, text="2/ Please enter the common pattern in the names of the "
                                             "folders where all the image\nare stored in (please ends with "
                                             "an asterisk like so: `2020*`, ``Session*` or `100CU*`): ")
        pattern1Label.grid(row=2, sticky='ew')

        self.pattern1Entry = ttk.Entry(self)
        self.pattern1Entry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='ns')

        pattern2CheckLabel = ttk.Label(self, text="3/ Is there a second common pattern in the names of the"
                                                  "\nsub-folders in the above-mentioned folders? (`Y` or `N`): ")
        pattern2CheckLabel.grid(row=4, sticky='')

        pattern2CheckYes_btn = ttk.Button(self, text="Yes", command=self.secondPattern)
        pattern2CheckYes_btn.grid(row=5, ipady=5, ipadx=5, sticky='ns')

        pattern2CheckNo_btn = ttk.Button(self, text="No", command=self.clickedNo)
        pattern2CheckNo_btn.grid(row=6, ipady=5, ipadx=5, sticky='ns')

        batch_btn = ttk.Button(self, text="Back To Batch Functions Page",
                               command=lambda: master.switch_frame("BatchPage"))
        batch_btn.grid(row=19, ipady=10, ipadx=10, pady=4, sticky='ns')

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=20, ipady=10, ipadx=10, pady=4, sticky='ns')

    def inputDir(self):

        inputDir = filedialog.askdirectory(title='Please select the image folder')
        self.inputDirPath = str(inputDir)

        print(self.inputDirPath)

        inputDirLabel = ttk.Label(self, text='SELECTED FOLDER: \n' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=8, sticky='ns')

    """
        Section for when `question 3/` is answered with `No` 
    """

    def clickedNo(self):

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

        self.noPFChoiceLabel = ttk.Label(self, text="4/ Which `processing function` would you like "
                                                    "to create the `batch-run` `pf*.txt` files for?")
        self.noPFChoiceLabel.grid(row=7, sticky='')

        self.noJSONCreatorButton = ttk.Button(self, text="Create `batch-input` JSON files", command=self.noJSONCreator)
        self.noJSONCreatorButton.grid(row=8, ipady=5, ipadx=5, sticky='ns')

        # self.noCSVConverter_btn = ttk.Button(self, text="Convert `mega-detected` JSON to CSV `metadata` files",
        #                                    command=self.)
        # self.noCSVConverter_btn.grid(row=9, ipady=5, ipadx=5, sticky='ns')
        #
        # self.noSortImages_btn = ttk.Button(self, text="Sort the images using CSV `metadata` files",
        #                                    command=self.)
        # self.noSortImages_btn.grid(row=10, ipady=5, ipadx=5, sticky='ns')

    """
        Section for creating the `pf*.txt` files needed to `batch-run` the process 
        of creating `batch-input` JSON files when `question 3/` is answered with `No` 
    """

    def noJSONCreator(self):

        self.noInputJSONDirButton = ttk.Button(self, text="5/ Please enter the absolute path of the directory where "
                                                          "you want all the '*_BatchInput.json' files to be saved at",
                                               command=self.noInputJSONDir)
        self.noInputJSONDirButton.grid(row=11, ipadx=10, ipady=10, pady=8, sticky='ns')

        self.noOutputTxtDirButton = ttk.Button(self, text="6/ Enter the absolute path of the directory where "
                                                          "you want all the 'pf1_*.txt' files to be saved at",
                                               command=self.noOutputTxtDir)
        self.noOutputTxtDirButton.grid(row=13, ipadx=10, ipady=10, pady=8, sticky='ns')

        self.noCreateJSONTxtButton = ttk.Button(self, text="CREATE TXT FILE(S) FOR JSON CREATOR",
                                                command=self.noCreateJSONTxt)
        self.noCreateJSONTxtButton.grid(row=15, ipadx=10, ipady=10, pady=8, sticky='ns')

    def noInputJSONDir(self):
        noInputJSONDir = filedialog.askdirectory(title='Please select `batch-input` JSON folder')
        self.noInputJSONDirPath = str(noInputJSONDir)
        self.noInputJSONDirPath.replace("\\", "/")

        self.noInputJSONDirLabel = ttk.Label(self, text='SELECTED JSON FOLDER: \n' + self.noInputJSONDirPath)
        self.noInputJSONDirLabel.grid(row=12, pady=8, sticky='ns')

        print('SELECTED JSON FOLDER: ' + self.noInputJSONDirPath)

    def noOutputTxtDir(self):
        noOutputTxtDir = filedialog.askdirectory(title='Please select the folder for the `.txt` files')
        self.noOutputTxtDirPath = str(noOutputTxtDir)
        self.noOutputTxtDirPath.replace("\\", "/")

        self.noOutputTxtDirLabel = ttk.Label(self, text='SELECTED FOLDER FOR TXT FIlES: \n' + self.noOutputTxtDirPath)
        self.noOutputTxtDirLabel.grid(row=14, pady=8, sticky='ns')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.noOutputTxtDirPath)

    def noCreateJSONTxt(self):

        jsonInputDir = self.noInputJSONDirPath
        txtOutputDir = self.noOutputTxtDirPath

        for ista, isess, ipaths in zip(self.station, self.session, self.img_paths):
            create = open(f"{txtOutputDir}/pf1_{self.dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}/{self.dataset}_{ista}_{isess}_BI.json\n")
            create.close()

            self.noCreateJSONTxtButton.config(text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                   "\nPlease adjust the previous steps for the "
                                                   "new run then CLICK this button to run again")

            destroy_these = [self.noInputJSONDirButton, self.noInputJSONDirLabel,
                             self.noOutputTxtDirButton, self.noOutputTxtDirLabel]

            for widget in destroy_these:
                widget.destroy()

    """
        Section for creating the `pf*.txt` files needed to `batch-run` the process 
        of creating CSV `metadata` files when `question 3/` is answered with `No` 
    """

    def noCSVConvertor(self):

        self.noInputMDJSONDirButton = ttk.Button(self, text="5/ Please enter the absolute path of the folder where all "
                                                            "the '*_MegaDetected.json' files are currently saved at",
                                                 command=self.noInputJSONDir)
        self.noInputMDJSONDirButton.grid(row=11, ipadx=10, ipady=10, pady=8, sticky='ns')



        self.noOutputTxtDirButton = ttk.Button(self, text="7/ Enter the absolute path of the directory where "
                                                          "you want all the 'pf2_*.txt' files to be saved at",
                                               command=self.noOutputTxtDir)
        self.noOutputTxtDirButton.grid(row=13, ipadx=10, ipady=10, pady=8, sticky='ns')

        self.noCreateJSONTxtButton = ttk.Button(self, text="CREATE TXT FILE(S) FOR JSON CREATOR",
                                                command=self.noCreateJSONTxt)
        self.noCreateJSONTxtButton.grid(row=15, ipadx=10, ipady=10, pady=8, sticky='ns')

    def noInputJSONDir(self):
        noInputJSONDir = filedialog.askdirectory(title='Please select `batch-input` JSON folder')
        self.noInputJSONDirPath = str(noInputJSONDir)
        self.noInputJSONDirPath.replace("\\", "/")

        self.noInputJSONDirLabel = ttk.Label(self, text='SELECTED JSON FOLDER: \n' + self.noInputJSONDirPath)
        self.noInputJSONDirLabel.grid(row=12, pady=8, sticky='ns')

        print('SELECTED JSON FOLDER: ' + self.noInputJSONDirPath)

    def noOutputTxtDir(self):
        noOutputTxtDir = filedialog.askdirectory(title='Please select the folder for the `.txt` files')
        self.noOutputTxtDirPath = str(noOutputTxtDir)
        self.noOutputTxtDirPath.replace("\\", "/")

        self.noOutputTxtDirLabel = ttk.Label(self, text='SELECTED FOLDER FOR TXT FIlES: \n' + self.noOutputTxtDirPath)
        self.noOutputTxtDirLabel.grid(row=14, pady=8, sticky='ns')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.noOutputTxtDirPath)

    def noCreateJSONTxt(self):

        jsonInputDir = self.noInputJSONDirPath
        txtOutputDir = self.noOutputTxtDirPath

        for ista, isess, ipaths in zip(self.station, self.session, self.img_paths):
            create = open(f"{txtOutputDir}/pf1_{self.dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}/{self.dataset}_{ista}_{isess}_BI.json\n")
            create.close()

            self.noCreateJSONTxtButton.config(text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                   "\nPlease adjust the previous steps for the "
                                                   "new run then CLICK this button to run again")

            destroy_these = [self.noInputJSONDirButton, self.noInputJSONDirLabel,
                             self.noOutputTxtDirButton, self.noOutputTxtDirLabel]

            for widget in destroy_these:
                widget.destroy()

    """
        Section for when `question 3/` is answered with `Yes` 
    """

    def secondPattern(self):

        self.pattern1 = self.pattern1Entry.get()

        for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
            for dirname_p1 in fnmatch.filter(dirs, self.pattern1):
                self.pattern1_list.append(os.path.join(path, dirname_p1).replace("\\", "/"))

        self.pattern2Label = ttk.Label(self, text="4/ What is the second common pattern in the names of the "
                                                  "sub-folders?\n(please ends with an asterisk like so: `2020*`, "
                                                  "`Session*` or `100CU*`): ")
        self.pattern2Label.grid(row=7, sticky='')

        self.pattern2Entry = ttk.Entry(self)
        self.pattern2Entry.grid(row=8, ipady=10, ipadx=10, pady=4, sticky='ns')

        self.confirmPattern2 = ttk.Button(self, text="CONFIRM SECOND PATTERN !!",
                                          command=self.clickedYes)
        self.confirmPattern2.grid(row=9, ipadx=10, ipady=10, pady=8, sticky='ns')

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

        self.yesPFChoiceLabel = ttk.Label(self, text="4/ Which `processing function` would you like "
                                                     "to create the `batch-run` `pf*.txt` files for?")
        self.yesPFChoiceLabel.grid(row=10, sticky='')

        self.yesJSONCreatorButton = ttk.Button(self, text="Create `batch-input` JSON files",
                                               command=self.yesJSONCreator)
        self.yesJSONCreatorButton.grid(row=11, ipady=5, ipadx=5, sticky='ns')

        # self.yesCSVConverter_btn = ttk.Button(self, text="Convert `mega-detected` JSON to CSV `metadata` files",
        #                                    command=self.)
        # self.yesCSVConverter_btn.grid(row=12, ipady=5, ipadx=5, sticky='ns')
        #
        # self.yesSortImages_btn = ttk.Button(self, text="Sort the images using CSV `metadata` files",
        #                                    command=self.)
        # self.yesSortImages_btn.grid(row=13, ipady=5, ipadx=5, sticky='ns')

    def yesJSONCreator(self):

        self.yesInputJSONDirButton = ttk.Button(self, text="5/ Please enter the absolute path of the directory where "
                                                           "you want all the '*_BatchInput.json' files to be saved at",
                                                command=self.yesInputJSONDir)
        self.yesInputJSONDirButton.grid(row=14, ipadx=10, ipady=10, pady=8, sticky='ns')

        self.yesOutputTxtDirButton = ttk.Button(self, text="6/ Enter the absolute path of the directory where "
                                                           "you want all the 'pf1_*.txt' files to be saved at",
                                                command=self.yesOutputTxtDir)
        self.yesOutputTxtDirButton.grid(row=16, ipadx=10, ipady=10, pady=8, sticky='ns')

        self.yesCreateJSONTxtButton = ttk.Button(self, text="CREATE TXT FILE(S) FOR JSON CREATOR",
                                                 command=self.yesCreateJSONTxt)
        self.yesCreateJSONTxtButton.grid(row=18, ipadx=10, ipady=10, pady=8, sticky='ns')

    """
        Section for creating the `pf*.txt` files needed to `batch-run` the process 
        of creating `batch-input` JSON files when `question 3/` is answered with `Yes` 
    """

    def yesInputJSONDir(self):
        yesInputJSONDir = filedialog.askdirectory(title='Please select the `batch-input` JSON folder')
        self.yesInputJSONDirPath = str(yesInputJSONDir)
        self.yesInputJSONDirPath.replace("\\", "/")

        self.yesInputJSONDirLabel = ttk.Label(self, text='SELECTED JSON FOLDER: \n' + self.yesInputJSONDirPath)
        self.yesInputJSONDirLabel.grid(row=15, pady=8, sticky='ns')

        print('SELECTED JSON FOLDER: ' + self.yesInputJSONDirPath)

    def yesOutputTxtDir(self):
        yesOutputTxtDir = filedialog.askdirectory(title='Please select the folder for the `.txt` files')
        self.yesOutputTxtDirPath = str(yesOutputTxtDir)
        self.yesOutputTxtDirPath.replace("\\", "/")

        self.yesOutputTxtDirLabel = ttk.Label(self, text='SELECTED FOLDER FOR TXT FIlES: \n' + self.yesOutputTxtDirPath)
        self.yesOutputTxtDirLabel.grid(row=17, pady=8, sticky='ns')

        print('SELECTED FOLDER FOR TXT FILES: ' + self.yesOutputTxtDirPath)

    def yesCreateJSONTxt(self):

        jsonInputDir = self.yesInputJSONDirPath
        txtOutputDir = self.yesOutputTxtDirPath

        for ista, isess, ipaths in zip(self.station, self.session, self.img_paths):
            create = open(f"{txtOutputDir}/pf1_{self.dataset}_{ista}_{isess}.txt", "a")
            create.write(f"1\n"
                         f"1\n"
                         f"{ipaths}/\n"
                         f"{jsonInputDir}/{self.dataset}_{ista}_{isess}_BI.json\n")
            create.close()

            self.yesCreateJSONTxtButton.config(text="THE `.TXT` FILE(S) WERE CREATED SUCCESSFULLY !!!"
                                                    "\nPlease adjust the previous steps for the "
                                                    "new run then CLICK this button to run again")

            destroy_these = [self.pattern2Label, self.pattern2Entry, self.confirmPattern2,
                             self.yesPFChoiceLabel, self.yesJSONCreatorButton,
                             self.yesInputJSONDirButton, self.yesInputJSONDirLabel,
                             self.yesOutputTxtDirButton, self.yesOutputTxtDirLabel]

            for widget in destroy_these:
                widget.destroy()


if __name__ == "__main__":
    app = BatchPage()
    app.mainloop()
