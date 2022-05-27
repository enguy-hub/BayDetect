# Source code: https://stackoverflow.com/a/37861801/17362021

from tkinter.constants import *
from tkinter import ttk

import tkinter as tk


class ScrolledPage(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        self.parent = parent

        # Create a canvas object and a vertical scrollbar for scrolling it.
        self.vscrollbar = ttk.Scrollbar(self.parent, orient=VERTICAL)
        self.vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = tk.Canvas(self.parent, bd=0, highlightthickness=0, yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        self.vscrollbar.config(command=self.canvas.yview)

        # Reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.scrollwindow = ttk.Frame(self.parent)
        self.interior_id = self.canvas.create_window(0, 0, window=self.scrollwindow, anchor=NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
            self.canvas.config(scrollregion="0 0 %s %s" % size)
            if self.scrollwindow.winfo_reqwidth() != self.canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                self.canvas.config(width=self.scrollwindow.winfo_reqwidth())
        self.scrollwindow.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if self.scrollwindow.winfo_reqwidth() != self.canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', _configure_canvas)
