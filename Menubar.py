import tkinter as tk 

class Menubar(tk.Frame):
  def __init__(self, master=None, **kwargs):
    super().__init__(master, **kwargs)
    self.grid(sticky="nsew")
    self.fileButton = tk.Button(self, text="File")
    self.fileButton.grid(row=0, column=0, sticky="nsew")
    self.editButton = tk.Button(self, text="Edit")
    self.editButton.grid(row=0, column=1, sticky="nsew")
    self.selectionButton = tk.Button(self, text="Selection")
    self.selectionButton.grid(row=0, column=2, sticky="nsew")
    self.viewButton = tk.Button(self, text="View")
    self.viewButton.grid(row=0, column=3, sticky="nsew")
    self.goButton = tk.Button(self, text="Go")
    self.goButton.grid(row=0, column=4, sticky="nsew")
    self.runButton = tk.Button(self, text="Run")
    self.runButton.grid(row=0, column=5, sticky="nsew")
    self.terminalButton = tk.Button(self, text="Terminal")
    self.terminalButton.grid(row=0, column=6, sticky="nsew")
    self.helpButton = tk.Button(self, text="Help")
    self.helpButton.grid(row=0, column=7, sticky="nsew")
