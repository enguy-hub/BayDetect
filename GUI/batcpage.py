import tkinter as tk
from tkinter import Tk, Frame, ttk

LARGE_FONT = ("Calibri", 12)

"""
------------------------------------------------------------------------------------------------------------------------
Batch Page(s) Section
------------------------------------------------------------------------------------------------------------------------
"""


class BatchPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = ttk.Label(self, text="Batch Functions", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        batc1_btn = ttk.Button(self, text="Create `pf*.txt` files",
                               command=lambda: master.switch_frame("BatchPage"))
        batc1_btn.pack(ipadx=5, ipady=5, expand=1)

        batc2_btn = ttk.Button(self, text="Create `.txt` files needed to execute `pf_batchrun()` function",
                               command=lambda: master.switch_frame("BatchPage"))
        batc2_btn.pack(ipadx=5, ipady=5, expand=1)

        batc3_btn = ttk.Button(self, text="Create `.txt` files needed to run `md_batchrun()` function",
                               command=lambda: master.switch_frame("BatchPage"))
        batc3_btn.pack(ipadx=5, ipady=5, expand=1)

        home_btn = ttk.Button(self, text="Homepage",
                              command=lambda: master.switch_frame("HomePage"))
        home_btn.pack(ipadx=5, ipady=5, expand=1)

        quit_btn = ttk.Button(self, text="Quit",
                              command=lambda: self.quit())
        quit_btn.pack(ipadx=5, ipady=5, expand=1)


if __name__ == "__main__":
    app = BatchPage()
    app.mainloop()