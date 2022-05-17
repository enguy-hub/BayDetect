# License: http://creativecommons.org/licenses/by-sa/3.0/

from tkinter import Tk

from homepage import HomePage
from procpage import ProcessingPage, JSONCreator, CSVConvertor, RunMegaDetector
from utilpage import UtilityPage, FindReplaceFolderNames, FindReplaceFileNames, FindReplaceContentInFiles
from batcpage import BatchPage

pages = {
    "HomePage": HomePage,
    "ProcessingPage": ProcessingPage,
    "JSON Creator Page": JSONCreator,
    "CSV Convertor Page": CSVConvertor,
    "Run MegaDetector Page": RunMegaDetector,
    "UtilityPage": UtilityPage,
    "Find & Replace Folder Names": FindReplaceFolderNames,
    "Find & Replace File Names": FindReplaceFileNames,
    "Find & Replace Content in File": FindReplaceContentInFiles,
    "BatchPage": BatchPage
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

        Tk.title(self, "Bay Detect App")
        self.iconbitmap(self, default='./resources/lwf_icon.ico')

        # set window and screen width and height
        window_width = 800
        window_height = 700
        screen_width = Tk.winfo_screenwidth(self)
        screen_height = Tk.winfo_screenheight(self)

        # find the center point, and centered the app window
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, center_x, center_y))

        self._frame = None
        self.switch_frame("HomePage")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(ipadx=5, ipady=5, expand=1)


if __name__ == "__main__":
    app = BayDetectApp()
    app.mainloop()
