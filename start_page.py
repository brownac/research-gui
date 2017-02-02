import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import Tkinter as tk
import ttk

import csv

from graph_page import *

LARGE_FONT = ("Verdana", 12)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        instructions = tk.Label(self, text="Usage: press 'Start' to start. Determine if there is a shank first, then whether there is an inhibitory period.")
        instructions.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Graph Page", command=lambda: controller.show_frame(GraphPage))
        button.pack()