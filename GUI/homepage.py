import tkinter as tk
from tkinter import Tk, Frame, ttk


LARGE_FONT = ("Calibri", 12)


"""
------------------------------------------------------------------------------------------------------------------------
Home Page Section
------------------------------------------------------------------------------------------------------------------------
"""


class HomePage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = ttk.Label(self, text="BayDetect App", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        proc_btn = ttk.Button(self, text="Processing Functions",
                              command=lambda: master.switch_frame("ProcessingPage"))
        proc_btn.pack(ipadx=5, ipady=5, expand=1)

        util_btn = ttk.Button(self, text="Utility Functions",
                              command=lambda: master.switch_frame("UtilityPage"))
        util_btn.pack(ipadx=5, ipady=5, expand=1)

        batc_btn = ttk.Button(self, text="Batch Functions",
                              command=lambda: master.switch_frame("BatchPage"))
        batc_btn.pack(ipadx=5, ipady=5, expand=1)

        quit_btn = ttk.Button(self, text="Quit",
                              command=lambda: self.quit())
        quit_btn.pack(ipadx=5, ipady=5, expand=1)


if __name__ == "__main__":
    app = HomePage()
    app.mainloop()