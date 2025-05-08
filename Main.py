import tkinter as tk
from Menubar import Menubar
from Sidebar import Sidebar
from Editor import Editor
from SecondarySidebar import SecondarySidebar
from Panel import Panel
from Statusbar import Statusbar
from Theme import Theme 

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("MPM")
    self.state('zoomed')
    self.theme = Theme() 

    self.rowconfigure(0, weight=1)
    self.rowconfigure(1, weight=70)
    self.rowconfigure(2, weight=28)
    self.rowconfigure(3, weight=1)
    self.columnconfigure(0, weight=10)
    self.columnconfigure(1, weight=80)
    self.columnconfigure(2, weight=10)

    self.initMenubar()
    self.initSidebar()
    self.initEditor()
    self.initSecondarySidebar()
    self.initPanel()
    self.initStatusbar()

  def initMenubar(self):
    self.menubar = Menubar(self, self.theme)
    self.menubar.grid(row=0, column=0, columnspan=3, sticky="nsew")

  def initSidebar(self):
    self.sidebar = Sidebar(self, self.theme)
    self.sidebar.grid(row=1, rowspan=2, column=0, sticky="nsew")

  def initEditor(self):
    self.editor = Editor(self, self.theme)
    self.editor.grid(row=1, column=1, sticky="nsew")

  def initSecondarySidebar(self):
    self.secondarySidebar = SecondarySidebar(self, self.theme)
    self.secondarySidebar.grid(row=1, rowspan=2, column=2, sticky="nsew")

  def initPanel(self):
    self.panel = Panel(self, self.theme)
    self.panel.grid(row=2, column=1, sticky="nsew")

  def initStatusbar(self):
    self.statusbar = Statusbar(self, self.theme)
    self.statusbar.grid(row=3, column=0, columnspan=3, sticky="nsew")

if __name__ == "__main__":
  App().mainloop()
