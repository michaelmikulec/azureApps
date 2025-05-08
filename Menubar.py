import tkinter as tk 
from tkinter import ttk 

class Menubar(tk.Frame):
  def __init__(self, parent, theme=None):
    super().__init__(parent, **theme.frame)

    self.fileButton = tk.Button(self, text="File", **theme.button)
    self.fileButton.grid(row=0, column=0, sticky="nsew")

    self.editButton = tk.Button(self, text="Edit", **theme.button)
    self.editButton.grid(row=0, column=1, sticky="nsew")

    self.selectionButton = tk.Button(self, text="Selection", **theme.button)
    self.selectionButton.grid(row=0, column=2, sticky="nsew")

    self.viewButton = tk.Button(self, text="View", **theme.button)
    self.viewButton.grid(row=0, column=3, sticky="nsew")

    self.goButton = tk.Button(self, text="Go", **theme.button)
    self.goButton.grid(row=0, column=4, sticky="nsew")

    self.runButton = tk.Button(self, text="Run", **theme.button)
    self.runButton.grid(row=0, column=5, sticky="nsew")

    self.terminalButton = tk.Button(self, text="Terminal", **theme.button)
    self.terminalButton.grid(row=0, column=6, sticky="nsew")

    self.helpButton = tk.Button(self, text="Help", **theme.button)
    self.helpButton.grid(row=0, column=7, sticky="nsew")

    # root.config(menu=self)

    # self.fileMenu = tk.Menu(self, tearoff=0, **theme.menu)
    # self.add_cascade(label="File", menu=self.fileMenu)
    # self.fileMenu.add_command(label="New Text File", command=lambda: print("New Text File"))
    # self.fileMenu.add_command(label="Open", command=lambda: print("Open File"))
    # self.fileMenu.add_separator()
    # self.fileMenu.add_command(label="Save", command=lambda: print("Save File"))
    # self.fileMenu.add_command(label="Save As", command=lambda: print("Save As"))
    # self.fileMenu.add_separator()
    # self.fileMenu.add_command(label="Exit", command=root.quit)

    # self.editMenu = tk.Menu(self, tearoff=0, **theme.menu)
    # self.add_cascade(label="Edit", menu=self.editMenu)
    # self.editMenu.add_command(label="Undo", command=lambda: print("Undo"))
    # self.editMenu.add_command(label="Redo", command=lambda: print("Redo"))
    # self.editMenu.add_separator()
    # self.editMenu.add_command(label="Cut", command=lambda: print("Cut"))
    # self.editMenu.add_command(label="Copy", command=lambda: print("Copy"))
    # self.editMenu.add_command(label="Paste", command=lambda: print("Paste"))
    # self.editMenu.add_separator()
    # self.editMenu.add_command(label="Find", command=lambda: print("Find"))
    # self.editMenu.add_command(label="Replace", command=lambda: print("Replace"))
    # self.editMenu.add_separator()
    # self.editMenu.add_command(label="Find in Files", command=lambda: print("Find in Files"))
    # self.editMenu.add_command(label="Replace in Files", command=lambda: print("Replace in Files"))