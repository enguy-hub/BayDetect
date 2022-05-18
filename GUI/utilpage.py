from tkinter.ttk import *
from tkinter import filedialog
from tkinter import ttk, Frame, Label

import os
import fnmatch

LARGE_FONT = ("Calibri", 20)

"""
------------------------------------------------------------------------------------------------------------------------
Utility Page
------------------------------------------------------------------------------------------------------------------------
"""


class UtilityPage(Frame):
    def __init__(self, master):
        super().__init__(master)

        label = Label(self, text="Utility Functions", font=LARGE_FONT)
        label.pack(ipady=10, padx=10, pady=10)

        util1_btn = ttk.Button(self, text="1/ Find & replace the names of multiple folders at once",
                               command=lambda: master.switch_frame("Find & Replace Folder Names"))
        util1_btn.pack(ipadx=10, ipady=10, expand=1)

        util2_btn = ttk.Button(self, text="2/ Find & replace the names of multiple files at once",
                               command=lambda: master.switch_frame("Find & Replace File Names"))
        util2_btn.pack(ipadx=10, ipady=10, expand=1)

        util3_btn = ttk.Button(self, text="3/ Find & replace the content inside multiple"
                                          "files with the same file-extension at once",
                               command=lambda: master.switch_frame("Find & Replace Content in File"))
        util3_btn.pack(ipadx=10, ipady=10, expand=1)

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=10, ipady=10, expand=1)


"""
------------------------------------------------------------------------------------------------------------------------
Find & Replace | Folder Names
------------------------------------------------------------------------------------------------------------------------
"""


class FindReplaceFolderNames(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.chosenDir = None
        self.dirPath = None

        dirButton = ttk.Button(self, text="1/ Please select the folder which contains all the sub-folders "
                                          "\nthat you wish to collectively change their FOLDER-NAMES with",
                               command=self.selectDir)
        dirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        findLabel = ttk.Label(self, text="2/ Find: ")
        findLabel.grid(row=2, sticky='')

        self.findEntry = ttk.Entry(self)
        self.findEntry.grid(row=3, ipadx=10, ipady=10, pady=4, sticky='')

        replaceLabel = ttk.Label(self, text="3/ Replace with: ")
        replaceLabel.grid(row=4, sticky='')

        self.replaceEntry = ttk.Entry(self)
        self.replaceEntry.grid(row=5, ipadx=10, ipady=10, pady=4, sticky='')

        self.exeButton = ttk.Button(self, text="EXECUTE !!!", command=self.replaceAll)
        self.exeButton.grid(row=6, ipadx=10, ipady=10, pady=8, sticky='')

        util_btn = ttk.Button(self, text="Back To Utility Functions Page",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.grid(row=8, ipadx=10, ipady=10, pady=4, sticky='')

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipadx=10, ipady=10, pady=4, sticky='')

    def selectDir(self):
        directory = filedialog.askdirectory(title='Please select a directory')
        self.chosenDir = str(directory)

        dirTitleLabel = ttk.Label(self, text='SELECTED FOLDER: ' + self.chosenDir)
        dirTitleLabel.grid(row=1, ipadx=10, ipady=10, sticky='')

    def replaceAll(self):
        """
            Replaces all occurrences of `key` with `repl`.
        """
        inputDir = self.chosenDir
        key = self.findEntry.get()
        repl = self.replaceEntry.get()

        for (dirpath, dirnames, filenames) in os.walk(inputDir):
            for idirnames in range(len(dirnames)):
                newname = dirnames[idirnames].replace(key, repl)
                os.rename(os.path.join(dirpath, dirnames[idirnames]), os.path.join(dirpath, newname))
                dirnames[idirnames] = newname

                self.exeButton.config(text="FIND/REPLACE FOLDER-NAMES SUCCESSFULLY !!!"
                                           "\nAdjust the steps for the new run then CLICK this button to run again")


"""
------------------------------------------------------------------------------------------------------------------------
Find & Replace | Files Names
------------------------------------------------------------------------------------------------------------------------
"""


class FindReplaceFileNames(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.chosenDir = None
        self.dirPath = None

        dirButton = ttk.Button(self, text="1/ Please select the folder which contains all the files "
                                          "that\nyou wish to collectively change their FILE-NAMES with",
                               command=self.selectDir)
        dirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='')

        findLabel = ttk.Label(self, text="2/ Find: ")
        findLabel.grid(row=2, sticky='')

        self.findEntry = ttk.Entry(self)
        self.findEntry.grid(row=3, ipadx=10, ipady=10, pady=4, sticky='')

        replaceLabel = ttk.Label(self, text="3/ Replace with: ")
        replaceLabel.grid(row=4, sticky='')

        self.replaceEntry = ttk.Entry(self)
        self.replaceEntry.grid(row=5, ipadx=10, ipady=10, pady=4, sticky='')

        self.exeButton = ttk.Button(self, text="EXECUTE !!!", command=self.replaceAll)
        self.exeButton.grid(row=6, ipadx=10, ipady=10, pady=4, sticky='')

        util_btn = ttk.Button(self, text="Back To Utility Functions Page",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.grid(row=8, ipadx=10, ipady=10, pady=4, sticky='')

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipadx=10, ipady=10, pady=4, sticky='')

    def selectDir(self):
        directory = filedialog.askdirectory(title='Please select a directory')
        self.chosenDir = str(directory)

        dirTitleLabel = ttk.Label(self, text='SELECTED FOLDER: ' + self.chosenDir)
        dirTitleLabel.grid(row=1, ipadx=10, ipady=10, sticky='')

    def replaceAll(self):
        """
            Replaces all occurences of `key` with `repl`.
        """
        inputDir = self.chosenDir
        key = self.findEntry.get()
        repl = self.replaceEntry.get()

        for (dirpath, dirnames, filenames) in os.walk(inputDir):
            for ifilenames in range(len(filenames)):
                newname = filenames[ifilenames].replace(key, repl)
                os.rename(os.path.join(dirpath, filenames[ifilenames]), os.path.join(dirpath, newname))
                filenames[ifilenames] = newname

                self.exeButton.config(text="FIND/REPLACE FILE-NAMES SUCCESSFULLY !!!"
                                           "\nAdjust the steps for the new run then CLICK this button to run again")


"""
------------------------------------------------------------------------------------------------------------------------
Find & Replace | Content in Files
------------------------------------------------------------------------------------------------------------------------
"""


class FindReplaceContentInFiles(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.chosenDir = None
        self.dirPath = None

        dirButton = ttk.Button(self, text="1/ Please select the folder which contains all the files with the same"
                                          "\nfile-extension that you wish to change their inside content with",
                               command=self.selectDir)
        dirButton.grid(row=0, ipady=10, ipadx=10, pady=8, sticky='')

        commonLabel = ttk.Label(self, text="2/ Common file-extension (e.g: txt | csv): ")
        commonLabel.grid(row=2, sticky='')

        self.extensionEntry = ttk.Entry(self)
        self.extensionEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='')

        findLabel = ttk.Label(self, text="3/ Find: ")
        findLabel.grid(row=4, sticky='')

        self.findEntry = ttk.Entry(self)
        self.findEntry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='')

        replaceLabel = ttk.Label(self, text="4/ Replace with: ")
        replaceLabel.grid(row=6, sticky='')

        self.replaceEntry = ttk.Entry(self)
        self.replaceEntry.grid(row=7, ipady=10, ipadx=10, pady=8, sticky='')

        self.exeButton = ttk.Button(self, text="EXECUTE !!!", command=self.replaceAll)
        self.exeButton.grid(row=8, ipady=10, ipadx=4, sticky='')

        util_btn = ttk.Button(self, text="Back To Utility Functions Page",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.grid(row=10, ipady=10, ipadx=10, pady=4, sticky='')

        home_btn = ttk.Button(self, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=11, ipady=10, ipadx=10, pady=4, sticky='')

    def selectDir(self):
        directory = filedialog.askdirectory(title='Please select a directory')
        self.chosenDir = str(directory)

        dirTitleLabel = ttk.Label(self, text='SELECTED FOLDER: ' + self.chosenDir)
        dirTitleLabel.grid(row=1, ipady=10, ipadx=10, sticky='')

    def replaceAll(self):
        """
            Replaces all occurences of `key` with `repl`.
        """
        inputDir = self.chosenDir
        ext = self.extensionEntry.get()
        key = self.findEntry.get()
        repl = self.replaceEntry.get()

        for path, dirs, files in os.walk(os.path.abspath(inputDir)):
            for filename in fnmatch.filter(files, "*." + ext):
                # for filename in files:
                filepath = os.path.join(path, filename)
                with open(filepath) as f:
                    text = f.read()
                    text = text.replace(key, repl)
                with open(filepath, "w") as f:
                    f.write(text)

                self.exeButton.config(text="FIND/REPLACE FILE CONTENT SUCCESSFULLY !!!"
                                           "\nAdjust the steps for the new run then CLICK this button to run again")


if __name__ == "__main__":
    app = UtilityPage()
    app.mainloop()
