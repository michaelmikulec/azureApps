import tkinter as tk
from Menubar import Menubar
from Sidebar import Sidebar
from Editor import Editor
from SecondarySidebar import SecondarySidebar
from Panel import Panel
from Statusbar import Statusbar
from Theme import * 

class App(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.grid(sticky="nsew")
    self.rowconfigure(0, weight=1)
    self.rowconfigure(1, weight=48)
    self.rowconfigure(2, weight=48)
    self.rowconfigure(3, weight=1)
    for i in range(100):
      self.columnconfigure(i, weight=1)
    self.initMenubar()
    self.initSidebar()
    self.initEditor()
    self.initSecondarySidebar()
    self.initPanel()
    self.initStatusbar()

  def initMenubar(self):
    menubar = Menubar(self, **frameTheme)
    menubar.grid(row=0, column=0, columnspan=100, sticky="ew")

  def initSidebar(self):
    sidebar = Sidebar(self)
    sidebar.grid(row=1, column=0, columnspan=10, sticky="nsw")

  def initEditor(self):
    editor = Editor(self)
    editor.grid(row=1, column=10, columnspan=80, sticky="nsew")

  def initSecondarySidebar(self):
    secondarySidebar = SecondarySidebar(self)
    secondarySidebar.grid(row=1, column=90, columnspan=10, sticky="nse")

  def initPanel(self):
    panel = Panel(self)
    panel.grid(row=2, column=0, columnspan=100, sticky="ew")

  def initStatusbar(self):
    statusbar = Statusbar(self)
    statusbar.grid(row=3, column=0, columnspan=100, sticky="ew")

if __name__ == "__main__":
  root = tk.Tk()
  root.rowconfigure(0, weight=1)
  root.columnconfigure(0, weight=1)
  app = App(root)
  root.title("My App")
  root.state('zoomed')
  root.mainloop()

