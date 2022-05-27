# License: http://creativecommons.org/licenses/by-sa/3.0/
from tkinter import Tk

from homepage import HomePage
from processpage import ProcessingPage, JSONCreator, RunMegaDetector, CSVConvertor, ImageSorter
from utilpage import UtilityPage, FindReplaceFolderNames, FindReplaceFileNames, FindReplaceContentInFiles
from batchpage import BatchPage, Batchrun_ProcessingFunctions, Batchrun_CombinedTXT, Batchrun_RunMegaDetector

pages = {
    "HomePage": HomePage,
    "ProcessingPage": ProcessingPage,
    "JSON Creator Page": JSONCreator,
    "Run MegaDetector Page": RunMegaDetector,
    "CSV Convertor Page": CSVConvertor,
    "Image Sorter Page": ImageSorter,
    "UtilityPage": UtilityPage,
    "Find & Replace Folder Names": FindReplaceFolderNames,
    "Find & Replace File Names": FindReplaceFileNames,
    "Find & Replace Content in File": FindReplaceContentInFiles,
    "BatchPage": BatchPage,
    "Batchrun Processing Functions": Batchrun_ProcessingFunctions,
    "Batchrun Create Combined TXT": Batchrun_CombinedTXT,
    "Batchrun Run MegaDetector": Batchrun_RunMegaDetector
}

LARGE_FONT = ("Calibri", 12)


"""
------------------------------------------------------------------------------------------------------------------------
Main window for the Bay Detect App
------------------------------------------------------------------------------------------------------------------------
"""


class BayDetectApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.iconbitmap(self, default='./resources/lwf_icon.ico')
        Tk.title(self, "Bay Detect App")

        self._frame = None
        self.switch_frame("HomePage")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master=self)

        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(padx=10, pady=10, expand=1) #


if __name__ == "__main__":
    app = BayDetectApp()
    app.mainloop()
