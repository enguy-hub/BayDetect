from tkinter import ttk, filedialog, Label
from baydetect.gui.scrollpage import ScrolledPage

import os
import fnmatch
import tkinter as tk

LARGE_FONT = ("Calibri", 12)

"""
------------------------------------------------------------------------------------------------------------------------
Utility Page
------------------------------------------------------------------------------------------------------------------------
"""


class UtilityPage(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        label = Label(self.sw.scrollwindow, text="Utility Functions", font=LARGE_FONT)
        label.pack(ipady=5, padx=5, pady=5, expand=1)

        util1_btn = ttk.Button(self.sw.scrollwindow, text="1/ Find & replace the names of multiple folders at once",
                               command=lambda: master.switch_frame("Find & Replace Folder Names"))
        util1_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        util2_btn = ttk.Button(self.sw.scrollwindow, text="2/ Find & replace the names of multiple files at once",
                               command=lambda: master.switch_frame("Find & Replace File Names"))
        util2_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        util3_btn = ttk.Button(self.sw.scrollwindow, text="3/ Find & replace the content inside multiple"
                                                          "\nfiles with the same file-extension at once",
                               command=lambda: master.switch_frame("Find & Replace Content in File"))
        util3_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)


"""
------------------------------------------------------------------------------------------------------------------------
Find & Replace | Folder Names
------------------------------------------------------------------------------------------------------------------------
"""


class FindReplaceFolderNames(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.chosenDir = None
        self.dirPath = None

        dirButton = ttk.Button(self.sw.scrollwindow,
                               text="1/ Please select the folder which contains all the sub-folders "
                                    "\nthat you wish to collectively change their FOLDER-NAMES with",
                               command=self.selectDir)
        dirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='n')

        findLabel = ttk.Label(self.sw.scrollwindow, text="2/ Find: ")
        findLabel.grid(row=2, sticky='n')

        self.findEntry = ttk.Entry(self.sw.scrollwindow)
        self.findEntry.grid(row=3, ipadx=10, ipady=10, pady=4, sticky='n')

        replaceLabel = ttk.Label(self.sw.scrollwindow, text="3/ Replace with: ")
        replaceLabel.grid(row=4, sticky='n')

        self.replaceEntry = ttk.Entry(self.sw.scrollwindow)
        self.replaceEntry.grid(row=5, ipadx=10, ipady=10, pady=4, sticky='n')

        self.exeButton = ttk.Button(self.sw.scrollwindow, text="EXECUTE !!!", command=self.replaceAll)
        self.exeButton.grid(row=6, ipadx=10, ipady=10, pady=8, sticky='n')

        util_btn = ttk.Button(self.sw.scrollwindow, text="Back To Utility Functions Page",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.grid(row=8, ipadx=10, ipady=10, pady=4, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipadx=10, ipady=10, pady=4, sticky='n')

    def selectDir(self):
        directory = filedialog.askdirectory(title='Please select a directory')
        self.chosenDir = str(directory)

        dirTitleLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED FOLDER: ' + self.chosenDir)
        dirTitleLabel.grid(row=1, ipadx=10, ipady=10, sticky='n')

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

                self.findEntry.delete(0, 'end')
                self.replaceEntry.delete(0, 'end')


"""
------------------------------------------------------------------------------------------------------------------------
Find & Replace | Files Names
------------------------------------------------------------------------------------------------------------------------
"""


class FindReplaceFileNames(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.chosenDir = None
        self.dirPath = None

        dirButton = ttk.Button(self.sw.scrollwindow, text="1/ Please select the folder which contains all the files "
                                                          "that\nyou wish to collectively change their FILE-NAMES with",
                               command=self.selectDir)
        dirButton.grid(row=0, ipadx=10, ipady=10, pady=8, sticky='n')

        findLabel = ttk.Label(self.sw.scrollwindow, text="2/ Find: ")
        findLabel.grid(row=2, sticky='n')

        self.findEntry = ttk.Entry(self.sw.scrollwindow)
        self.findEntry.grid(row=3, ipadx=10, ipady=10, pady=4, sticky='n')

        replaceLabel = ttk.Label(self.sw.scrollwindow, text="3/ Replace with: ")
        replaceLabel.grid(row=4, sticky='n')

        self.replaceEntry = ttk.Entry(self.sw.scrollwindow)
        self.replaceEntry.grid(row=5, ipadx=10, ipady=10, pady=4, sticky='n')

        self.exeButton = ttk.Button(self.sw.scrollwindow, text="EXECUTE !!!", command=self.replaceAll)
        self.exeButton.grid(row=6, ipadx=10, ipady=10, pady=4, sticky='n')

        util_btn = ttk.Button(self.sw.scrollwindow, text="Back To Utility Functions Page",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.grid(row=8, ipadx=10, ipady=10, pady=4, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=9, ipadx=10, ipady=10, pady=4, sticky='n')

    def selectDir(self):
        directory = filedialog.askdirectory(title='Please select a directory')
        self.chosenDir = str(directory)

        dirTitleLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED FOLDER: ' + self.chosenDir)
        dirTitleLabel.grid(row=1, ipadx=10, ipady=10, sticky='n')

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

                self.findEntry.delete(0, 'end')
                self.replaceEntry.delete(0, 'end')


"""
------------------------------------------------------------------------------------------------------------------------
Find & Replace | Content in Files
------------------------------------------------------------------------------------------------------------------------
"""


class FindReplaceContentInFiles(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sw = ScrolledPage(self)

        self.chosenDir = None
        self.dirPath = None

        dirButton = ttk.Button(self.sw.scrollwindow,
                               text="1/ Please select the folder which contains all the files with the same"
                                    "\nfile-extension that you wish to change their inside content with",
                               command=self.selectDir)
        dirButton.grid(row=0, ipady=10, ipadx=10, pady=8, sticky='n')

        commonLabel = ttk.Label(self.sw.scrollwindow, text="2/ Common file-extension (e.g: txt | csv): ")
        commonLabel.grid(row=2, sticky='n')

        self.extensionEntry = ttk.Entry(self.sw.scrollwindow)
        self.extensionEntry.grid(row=3, ipady=10, ipadx=10, pady=4, sticky='n')

        findLabel = ttk.Label(self.sw.scrollwindow, text="3/ Find: ")
        findLabel.grid(row=4, sticky='n')

        self.findEntry = ttk.Entry(self.sw.scrollwindow)
        self.findEntry.grid(row=5, ipady=10, ipadx=10, pady=4, sticky='n')

        replaceLabel = ttk.Label(self.sw.scrollwindow, text="4/ Replace with: ")
        replaceLabel.grid(row=6, sticky='n')

        self.replaceEntry = ttk.Entry(self.sw.scrollwindow)
        self.replaceEntry.grid(row=7, ipady=10, ipadx=10, pady=8, sticky='n')

        self.exeButton = ttk.Button(self.sw.scrollwindow, text="EXECUTE !!!", command=self.replaceAll)
        self.exeButton.grid(row=8, ipady=10, ipadx=4, sticky='n')

        util_btn = ttk.Button(self.sw.scrollwindow, text="Back To Utility Functions Page",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.grid(row=10, ipady=10, ipadx=10, pady=4, sticky='n')

        home_btn = ttk.Button(self.sw.scrollwindow, text="Back To Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.grid(row=11, ipady=10, ipadx=10, pady=4, sticky='n')

    def selectDir(self):
        directory = filedialog.askdirectory(title='Please select a directory')
        self.chosenDir = str(directory)

        dirTitleLabel = ttk.Label(self.sw.scrollwindow, text='SELECTED FOLDER: ' + self.chosenDir)
        dirTitleLabel.grid(row=1, ipady=10, ipadx=10, sticky='n')

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

                self.extensionEntry.delete(0, 'end')
                self.findEntry.delete(0, 'end')
                self.replaceEntry.delete(0, 'end')


if __name__ == "__main__":
    page = UtilityPage()
    page.mainloop()
