from Tkinter import *

class Application(Frame):
    # write to a list
    def write_to_list(self, *args):
        self.vec.extend(args)

    # inhibitory response
    def is_inhib(self):
        self.write_to_list(1)
        print self.vec

    # not an inhibitory response
    def no_inhib(self):
        self.write_to_list(0)
        print self.vec


    def createWidgets(self):
        # yes button
        self.inhib = Button(self)
        self.inhib["text"] = "Yes"
        self.inhib["fg"]   = "green"
        self.inhib["command"] =  self.is_inhib
        self.inhib.pack({"side": "left"})

        # no button
        self.not_inhib = Button(self)
        self.not_inhib["text"] = "No",
        self.not_inhib["command"] = self.no_inhib
        self.not_inhib.pack({"side": "right"})

    def __init__(self, master=None):
        self.vec = []
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("Research GUI")
app = Application(master=root)
app.mainloop()
root.destroy()