from tkinter import Frame, ttk, StringVar
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

        batc1_btn = ttk.Button(self, text="1/ Create `.txt` files to `batch-run` one of the processing function",
                               command=lambda: master.switch_frame("PF Batchrun TXTCreator"))
        batc1_btn.pack(ipadx=10, ipady=10, expand=1)

        batc2_btn = ttk.Button(self, text="2/ Create `.txt` files needed to execute `pf_batchrun()` "
                                          "function from the `BayDetect/batchrun.py` python script",
                               command=lambda: master.switch_frame("BatchPage"))
        batc2_btn.pack(ipadx=10, ipady=10, expand=1)

        batc3_btn = ttk.Button(self, text="3/ Create `.txt` files needed to execute `md_batchrun()` "
                                          "function from the `BayDetect/batchrun.py` python script",
                               command=lambda: master.switch_frame("BatchPage"))
        batc3_btn.pack(ipadx=10, ipady=10, expand=1)

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=10, ipady=10, expand=1)

        quit_btn = ttk.Button(self, text="Quit",
                              command=lambda: self.quit())
        quit_btn.pack(ipadx=10, ipady=10, expand=1)


"""
------------------------------------------------------------------------------------------------------------------------
PF BatchRun TXT Creator Page
------------------------------------------------------------------------------------------------------------------------
"""


class PF_Batchrun_TXTCreator(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.inputDirPath = None
        self.checkVar = StringVar()
        self.pattern2Entry = None

        self.org_img_dirpath = None
        self.pattern1_list = None
        self.pattern2_list = None

        inputDirButton = ttk.Button(self, text="1/ Please select the `parent-folder` where "
                                               "all the `station-folders` are located in.",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        pattern1Label = ttk.Label(self, text="2/ Please enter the common pattern in the names of the "
                                             "folders where all the image\nare stored in (please ends with "
                                             "an asterisk like so: `2020*`, ``Session*` or `100CU*`): ")
        pattern1Label.grid(row=2, sticky='')

        self.pattern1Entry = ttk.Entry(self)
        self.pattern1Entry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        patternCheckLabel = ttk.Label(self, text="3/ Is there a second common pattern in the names for the "
                                                 "sub-folders of above-mentioned folders? (`Y` or `N`): ")
        patternCheckLabel.grid(row=4, sticky='')

        self.patternCheckEntry = ttk.Entry(self, textvariable=self.checkVar)
        self.patternCheckEntry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='')

        self.checkVar.trace('w', )

        # self.executeButton = ttk.Button(self, text="EXECUTE !!", command=self.runMD)
        # self.executeButton.grid(row=6, ipady=10, ipadx=10, pady=4, sticky='')

        util_btn = ttk.Button(self, text="Back To Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=8, ipady=10, ipadx=10, pady=4, sticky='')

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipady=10, ipadx=10, pady=4, sticky='')

    def inputDir(self):
        inputDir = filedialog.askdirectory(title='Please select a directory')
        self.inputDirPath = str(inputDir)

        inputDirLabel = ttk.Label(self, text='SELECTED IMAGE FOLDER: \n' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=8, sticky='')

    def capture(self):

        self.org_img_dirpath = []
        self.pattern1_list = []
        self.pattern2_list = []

        if self.patternCheckEntry.get() == 'N':
            for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
                for dirname in fnmatch.filter(dirs, self.pattern1Entry.get()):
                    self.org_img_dirpath.append(os.path.join(path, dirname).replace("\\", "/"))

        elif self.patternCheckEntry.get() == 'Y':

            pattern2Label = ttk.Label(self, text="4/ What is the second common pattern in the names of the "
                                                 "sub-folders?\n(please ends with an asterisk like so: `2020*`, "
                                                 "`Session*` or `100CU*`): ")
            pattern2Label.grid(row=6, sticky='')

            self.pattern2Entry = ttk.Entry(self)
            self.pattern2Entry.grid(row=7, ipady=10, ipadx=10, pady=4, sticky='')

            for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
                for dirname_p1 in fnmatch.filter(dirs, self.pattern1Entry.get()):
                    self.pattern1_list.append(os.path.join(path, dirname_p1).replace("\\", "/"))

            for path, dirs, files in os.walk(os.path.abspath(self.inputDirPath)):
                for dirname_p2 in fnmatch.filter(dirs, self.pattern2Entry.get()):
                    self.pattern2_list.append(dirname_p2)

            for ip1, ip2 in zip(self.pattern1_list, self.pattern2_list):
                self.org_img_dirpath.append(os.path.join(ip1, ip2).replace("\\", "/"))



if __name__ == "__main__":
    app = BatchPage()
    app.mainloop()
