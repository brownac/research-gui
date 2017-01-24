from Tkinter import *

class Application(Frame):
    def addElement(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.inhib = Button(self)
        self.inhib["text"] = "Yes"
        self.inhib["fg"]   = "green"
        self.inhib["command"] =  self.addElement

        self.inhib.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.addElement

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()