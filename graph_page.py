import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import Tkinter as tk
import ttk

import csv

LARGE_FONT = ("Verdana", 12)


# components

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
        file = csv.reader(open('in.csv'))
        inhibfile = csv.reader(open('inhib.csv'))

        inhib_time = tk.Label(self, text="")
        inhib_time.pack({"side": "top"})

        start_button = tk.Button(self, text="Start",
                                 command=lambda: controller.start_graphing(file, inhibfile, inhib_time))
        start_button.pack({"side":"top"})

        stop_botton = tk.Button(self, text="Stop",
                                command=lambda: controller.quit())
        stop_botton.pack({"side": "bottom"})

        inhib = tk.Label(self, text="Inhibitory?")
        inhib.pack({"side":"left"})

        yes_button = tk.Button(self, text="Yes",
                                command=lambda: controller.do_graphing(file, inhibfile, inhib_time, 1))
        yes_button.pack({"side":"left"})

        no_button = tk.Button(self, text="No",
                              command=lambda: controller.do_graphing(file, inhibfile, inhib_time, 0))
        no_button.pack({"side":"left"})

        # shank stuff

        no_shank = tk.Button(self, text="No",
                                  command=lambda: controller.handle_shank(0))
        no_shank.pack({"side":"right"})


        yes_shank = tk.Button(self, text="Yes",
                                   command=lambda: controller.handle_shank(1))

        yes_shank.pack({"side":"right"})
        shank = tk.Label(self, text="Shank?")
        shank.pack({"side": "right"})