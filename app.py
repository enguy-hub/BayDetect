# License: http://creativecommons.org/licenses/by-sa/3.0/
from tkinter import Tk
from tkinter import *

from baydetect.gui.homepage import HomePage
from baydetect.gui.processpage import ProcessingPage, JSONCreator, RunMegaDetector, CSVConvertor, ImageSorter
from baydetect.gui.utilpage import UtilityPage, FindReplaceFolderNames, FindReplaceFileNames, FindReplaceContentInFiles
from baydetect.gui.batchpage import BatchPage, Batchrun_ProcessingFunctions, Batchrun_CombinedTXT, \
    Batchrun_RunMegaDetector

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

        favico = PhotoImage(file="./baydetect/gui/resources/lwf_icon-1.png")

        # self.iconbitmap(self, default='./baydetect/gui/resources/lwf_icon.ico')
        self.iconphoto(False, favico)
        Tk.title(self, "Bay Detect App")

        w = Tk.winfo_reqwidth(self)
        h = Tk.winfo_reqheight(self)
        ws = Tk.winfo_screenwidth(self)
        hs = Tk.winfo_screenheight(self)
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        Tk.geometry(self, '+%d+%d' % (x, y))

        self._frame = None
        self.switch_frame("HomePage")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master=self)

        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(padx=10, pady=10, expand=1)


if __name__ == "__main__":
    app = BayDetectApp()
    app.mainloop()
