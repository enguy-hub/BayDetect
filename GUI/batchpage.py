import tkinter as tk
from tkinter import Tk, Frame, ttk

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
                               command=lambda: master.switch_frame("BatchPage"))
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
PF_BatchRun TXT Creator Page
------------------------------------------------------------------------------------------------------------------------
"""


class PF_Batchrun_TXTCreator(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.inputJSONPath = None
        self.outJSONPath = None

        inputJSONButton = ttk.Button(self, text="1/ Please select a `batch-input` JSON file which "
                                                "will be used to run MegaDetector batch-processing on",
                                     command=self.inputJSON)
        inputJSONButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        outJSONNameLabel = ttk.Label(self, text="2/ Please give a name to the resulted `mega-detected` JSON file."
                                                "Ideally it should be the\nsame as the `batch-input` JSON file but "
                                                "ends with `*_MegaDetected.json` instead")
        outJSONNameLabel.grid(row=2, sticky='')

        self.outJSONNameEntry = ttk.Entry(self)
        self.outJSONNameEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        outputDirButton = ttk.Button(self, text="3/ Please select the `OUTPUT` folder where the "
                                                "`mega-detected` JSON file will be saved at",
                                     command=self.outputJSON)
        outputDirButton.grid(row=4, ipadx=10, ipady=10, pady=8, sticky='')

        self.executeButton = ttk.Button(self, text="RUN MEGADETECTOR !!", command=self.runMD)
        self.executeButton.grid(row=6, ipady=10, ipadx=10, pady=4, sticky='')

        util_btn = ttk.Button(self, text="Back To Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=8, ipady=10, ipadx=10, pady=4, sticky='')

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipady=10, ipadx=10, pady=4, sticky='')

    def inputJSON(self):
        inputJSON = filedialog.askopenfilename(title='Please select a directory')
        self.inputJSONPath = str(inputJSON)

        inputJSONLabel = ttk.Label(self, text='SELECTED IMAGE FOLDER: \n' + self.inputJSONPath)
        inputJSONLabel.grid(row=1, pady=8, sticky='')

    def outputJSON(self):
        outputDir = filedialog.askdirectory(title='Please select a directory')
        outputDirPath = str(outputDir)

        outputJSONName = self.outJSONNameEntry.get()

        self.outJSONPath = os.path.join(outputDirPath, outputJSONName).replace("\\", "/")

        outputDirLabel = ttk.Label(self, text='OUTPUT `MEGA-DETECTED` JSON: \n' + self.outJSONPath)
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
                                           "\nAdjust the steps for the new run "
                                           "then CLICK this button to run again")
        else:
            self.executeButton.config(text="Error, please double check the commands !!")

        return print("MegaDetector was executed successfully !!!")


if __name__ == "__main__":
    app = BatchPage()
    app.mainloop()