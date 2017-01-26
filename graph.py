"""
TODO: add the functionality to either
    1. stop the graphing at any time and export the vector or
    2. export the vector once the reader reaches the bottom of the line
"""


import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import Tkinter as tk
import ttk

import csv
import itertools

LARGE_FONT = ("Verdana", 12)


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

        for F in (StartPage, GraphPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def do_graphing(self, file, *args):
        self.vec.extend(args)

        out = open('out.txt', 'w')
        for item in self.vec:
            print>>out, item
        out.close()

        plt.clf()
        y = file.next()
        # cast to string
        num = [int(x) for x in y]
        N = len(num)
        x = range(N)
        width = 1 / 1.5

        plt.bar(x, num, width)
        plt.show()


    def start_graphing(self, file):
        # get ready to plot
        y = file.next()
        # cast to string
        num = [int(x) for x in y]
        N = len(num)
        x = range(N)
        width = 1 / 1.5

        plt.bar(x, num, width)
        plt.show()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Graph Page", command=lambda: controller.show_frame(GraphPage))
        button.pack()


class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        # read the file
        file = csv.reader(open('out.csv'))

        start_button = tk.Button(self, text="Start",
                                 command=lambda: controller.start_graphing(file))
        start_button.pack({"side":"top"})

        stop_botton = tk.Button(self, text="Stop",
                                command=lambda: parent.quit())
        stop_botton.pack({"side": "bottom"})

        yes_button = tk.Button(self, text="Yes",
                                command=lambda: controller.do_graphing(file, 1))
        yes_button.pack({"side":"left"})

        no_button = tk.Button(self, text="No",
                              command=lambda: controller.do_graphing(file, 0))
        no_button.pack({"side":"right"})


app = research_gui()
app.mainloop()