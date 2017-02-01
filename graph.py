"""
TODO: add the functionality to either
    1. export the vector once the reader reaches the bottom of the line
    2. add functionality for showing time of inhibition
"""


import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import Tkinter as tk
import ttk

import csv

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
        self.shank_vec = []
        self.inhib_val = []

        for F in (StartPage, GraphPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def do_graphing(self, file, inhibfile, inhibtime, *args):
        self.vec.extend(args)

        with open('out.csv', 'w') as csvfile:
            create = csv.writer(csvfile)
            create.writerow(self.vec)

        inhib = inhibfile.next()
        v = [int(q) for q in inhib]

        # show the actual value
        inhibtime.config(text=v)

        plt.clf()
        y = file.next()
        # cast to string
        num = [int(x) for x in y]
        N = len(num)
        x = range(N)
        width = 1 / 1.5

        plt.bar(x, num, width)
        plt.show()


    def start_graphing(self, file, inhibfile, inhibtime):
        # grab the contents of the inhib file
        inhib = inhibfile.next()
        v = [int(q) for q in inhib]

        # show the actual value
        inhibtime.config(text=v)

        # get ready to plot
        y = file.next()
        # cast to string
        num = [int(x) for x in y]
        N = len(num)
        x = range(N)
        width = 1 / 1.5

        plt.bar(x, num, width)
        plt.show()

    def handle_shank(self, *args):
        self.shank_vec.extend(args)
        with open('shanks.csv', 'w') as csvfile:
            create = csv.writer(csvfile)
            create.writerow(self.shank_vec)


    def quit(self):
        app.destroy()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        instructions = tk.Label(self, text="Usage: press 'Start' to start. Determine if there is a shank first, then whether there is an inhibitory period.")
        instructions.pack(pady=10, padx=10)

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



app = research_gui()
app.mainloop()