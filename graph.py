"""
TODO: add the functionality to either
    1. export the vector once the reader reaches the bottom of the line
    2. more cleaning up
"""


import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import Tkinter as tk
import ttk

import csv

from graph_page import *
from start_page import *

LARGE_FONT = ("Verdana", 12)


# actions that will execute on button presses
class research_gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Research Gui")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.vec = []
        self.inhib_val = []

        for F in (StartPage, GraphPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def do_graphing(self, file, inhibfile, inhibtime, shankfile, shankval, *args):
        self.vec.extend(args)

        with open('out.csv', 'w') as csvfile:
            create = csv.writer(csvfile)
            create.writerow(self.vec)

        inhib = inhibfile.next()
        v = [int(q) for q in inhib]

        # show the actual value
        inhibtime.config(text=v)

        shank = shankfile.next()
        z = [int(t) for t in shank]
        if z[2] == z[3]:
            shankval.config(text="Y")
        else:
            shankval.config(text="N")

        plt.clf()
        y = file.next()
        # cast to string
        num = [int(x) for x in y]
        N = len(num)
        x = range(N)
        width = 1 / 1.5

        plt.bar(x, num, width)
        plt.show()


    def start_graphing(self, file, inhibfile, inhibtime, shankfile, shankval):
        # grab the contents of the inhib file
        inhib = inhibfile.next()
        v = [int(q) for q in inhib]

        # show the actual value
        inhibtime.config(text=v)

        # shank stuff
        shank = shankfile.next()
        z = [int(t) for t in shank]
        if z[2] == z[3]:
            shankval.config(text="Y")
        else:
            shankval.config(text="N")

        # get ready to plot
        y = file.next()
        # cast to string
        num = [int(x) for x in y]
        N = len(num)
        x = range(N)
        width = 1 / 1.5

        plt.bar(x, num, width)
        plt.show()


    def quit(self):
        app.destroy()






app = research_gui()
app.mainloop()
