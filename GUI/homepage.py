import tkinter as tk

from tkinter import ttk
from scrollpage import ScrolledPage

LARGE_FONT = ("Calibri", 12)


"""
------------------------------------------------------------------------------------------------------------------------
Home Page Section
------------------------------------------------------------------------------------------------------------------------
"""


class HomePage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.sw = ScrolledPage(self)

        label = ttk.Label(self.sw.scrollwindow, text="BayDetect App", font=LARGE_FONT)
        label.pack(ipady=5, padx=5, pady=5, expand=1)

        proc_btn = ttk.Button(self.sw.scrollwindow, text="Processing Functions",
                              command=lambda: master.switch_frame("ProcessingPage"))
        proc_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        util_btn = ttk.Button(self.sw.scrollwindow, text="Utility Functions",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        batc_btn = ttk.Button(self.sw.scrollwindow, text="Batch Functions",
                              command=lambda: master.switch_frame("BatchPage"))
        batc_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)

        quit_btn = ttk.Button(self.sw.scrollwindow, text="Quit",
                              command=lambda: self.quit())
        quit_btn.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    page = HomePage()
    page.mainloop()