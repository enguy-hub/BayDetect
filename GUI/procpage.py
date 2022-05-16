import tkinter as tk
from tkinter import Tk, Frame, ttk

from tkinter import filedialog

import os
import json

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

        proc1_btn = ttk.Button(self, text="Create the `BatchInput` JSON needed to execute MegaDetector",
                               command=lambda: master.switch_frame("JSON Creator Page"))
        proc1_btn.pack(ipadx=5, ipady=5, expand=1)

        proc2_btn = ttk.Button(self, text="Convert the `MegaDetected` JSON to a CSV Metadata",
                               command=lambda: master.switch_frame("ProcessingPage"))
        proc2_btn.pack(ipadx=5, ipady=5, expand=1)

        proc3_btn = ttk.Button(self, text="Sort images into separate folders based"
                                          "\non detected classes from MegaDetector",
                               command=lambda: master.switch_frame("ProcessingPage"))
        proc3_btn.pack(ipadx=5, ipady=5, expand=1)

        home_btn = ttk.Button(self, text="Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=5, ipady=5, expand=1)

        quit_btn = ttk.Button(self, text="Quit",
                              command=lambda: self.quit())
        quit_btn.pack(ipadx=5, ipady=5, expand=1)


"""
------------------------------------------------------------------------------------------------------------------------
Find & Replace | Folder Names
------------------------------------------------------------------------------------------------------------------------
"""


class JSONCreator(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.inputDirPath = None
        self.finalOutputDir = None

        inputDirButton = ttk.Button(self, text="Please select the `INPUT` directory which contains all the"
                                               "\nimages which you would like to run MegaDetector on",
                                    command=self.inputDir)
        inputDirButton.grid(row=0, ipadx=10, ipady=10, sticky='')

        jsonNameLabel = ttk.Label(self, text="Please give a name for the `OUTPUT` JSON file from\nthis process"
                                             " (e.g: end with `*_BatchInput.json`)")
        jsonNameLabel.grid(row=2, sticky='')

        self.jsonNameEntry = ttk.Entry(self)
        self.jsonNameEntry.grid(row=3, ipady=5, ipadx=5, sticky='')

        outputDirButton = ttk.Button(self, text="Please select the `OUTPUT` directory that you would like"
                                                "\nthe JSON file created from this process to be saved at",
                                     command=self.outputDir)
        outputDirButton.grid(row=4, ipadx=10, ipady=10, sticky='')

        createJSONButton = ttk.Button(self, text="Create JSON File(s)", command=self.createJSON)
        createJSONButton.grid(row=6, ipady=5, ipadx=5, sticky='')

        util_btn = ttk.Button(self, text="Processing Functions Page",
                              command=lambda: master.switch_frame("ProcessingPage"))
        util_btn.grid(row=8, ipady=5, ipadx=5, pady=10, sticky='')

        home_btn = ttk.Button(self, text="Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipady=5, ipadx=5, sticky='')

    def inputDir(self):
        inputDirectory = filedialog.askdirectory(title='Please select a directory')
        self.inputDirPath = str(inputDirectory)

        inputDirLabel = ttk.Label(self, text='INPUT DIRECTORY: ' + self.inputDirPath)
        inputDirLabel.grid(row=1, pady=10, sticky='')

    def outputDir(self):
        outputDir = filedialog.askdirectory(title='Please select a directory')
        outputDirPath = str(outputDir)

        jsonFilename = self.jsonNameEntry.get()

        self.finalOutputDir = os.path.join(outputDirPath, jsonFilename).replace("\\", "/")

        outputDirLabel = ttk.Label(self, text='OUTPUT DIRECTORY AND FILENAME: ' + self.finalOutputDir)
        outputDirLabel.grid(row=5, pady=10, sticky='')

    def createJSON(self):
        """
            Replaces all occurrence of `key` with `repl`.
        """
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

            successLabel = ttk.Label(self, text='JSON files created successfully !!!! ')
            successLabel.grid(row=7, ipady=10, sticky='')

        return print("JSON file(s) created successfully !!!")


if __name__ == "__main__":
    app = ProcessingPage()
    app.mainloop()
