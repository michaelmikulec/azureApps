import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename
from azure.storage.blob import BlobServiceClient


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    def _init_style():
      self.fonts = {
        "h1": ("Arial", 20),
        "h1i": ("Arial", 20, "italic"),
        "h1b": ("Arial", 20, "bold"),
        "h2": ("Arial", 16),
        "h2i": ("Arial", 16, "italic"),
        "h2b": ("Arial", 16, "bold"),
        "b": ("Arial", 10),
        "bi": ("Arial", 10, "italic"),
        "bb": ("Arial", 10, "bold"),
        "m": ("Consolas", 12),
        "mi": ("Consolas", 12, "italic"),
        "mb": ("Consolas", 12, "bold"),
      }
      self.colors = {
        "bg3"     : "#002b36",
        "bg2"     : "#073642",
        "bg1"     : "#586e75",
        "bg0"     : "#657b83",
        "fg0"     : "#839496",
        "fg1"     : "#93a1a1",
        "yellow"  : "#b58900",
        "orange"  : "#cb4b16",
        "red"     : "#dc322f",
        "magenta" : "#d33682",
        "violet"  : "#6c71c4",
        "blue"    : "#268bd2",
        "cyan"    : "#2aa198",
        "green"   : "#859900",
        "white"   : "#ffffff",
        "black"   : "#000000",
      }
      self.reliefs = { 
        "flat"   : "flat",
        "raised" : "raised",
        "sunken" : "sunken",
        "ridge"  : "ridge",
        "groove" : "groove",
        "solid"  : "solid",
      }
      self.gridKwargs = {
        "padx"   : 10,
        "pady"   : 10,
        "ipadx"  : 10,
        "ipady"  : 10,
        "sticky" : "nsew",
      }
      self.frameKwargs = {
        "background"  : self.colors['bg2'],
        "borderwidth" : 1,
        "relief"      : "solid"
      }
      self.labelKwargs = {
        "background"  : self.colors["bg3"],
        "foreground"  : self.colors["cyan"],
        "font"        : self.fonts['b'],
        "justify"     : "left",
        "anchor"      : "center",
        "borderwidth" : 1,
        "relief"      : "solid",
      }
      self.h1Kwargs = {
        **self.labelKwargs,
        "font": self.fonts['h1i'],
      }
      self.h2Kwargs = {
        **self.labelKwargs,
        "font": self.fonts['h2i'],
      }
      self.buttonKwargs = {
        "background"  : self.colors['bg3'],
        "foreground"  : self.colors['cyan'],
        "font"        : ("Arial", 10),
        "justify"     : "left",
        "anchor"      : "center",
        "borderwidth" : 1,
        "relief"      : "solid",
      }
      self.menuButtonKwargs = {
        # "activebackground": ,
        # "activeforeground": ,
        # "anchor": ,
        "background": self.colors['bg3'],
        # "bd": ,
        # "bg": ,
        # "bitmap": ,
        "borderwidth": 1,
        # "cursor": ,
        # "direction": ,
        # "disabledforeground": ,
        # "fg": ,
        "font": self.fonts['b'],
        "foreground": self.colors['cyan'],
        # "height": ,
        # "highlightbackground": ,
        # "highlightcolor": ,
        # "highlightthickness": ,
        # "image": ,
        # "indicatoron": ,
        # "justify": ,
        # "menu": ,
        # "padx": ,
        # "pady": ,
        "relief": "solid",
        # "compound": ,
        # "state": ,
        # "takefocus": ,
        # "text": ,
        # "textvariable": ,
        # "underline": ,
        # "width": ,
        # "wraplength": ,
      }
      self.menuKwargs = { 
        # "activebackground": ,
        # "activeborderwidth": ,
        # "activeforeground": ,
        "background": self.colors['bg3'],
        # "bd": ,
        # "bg": ,
        "borderwidth": 1,
        # "cursor": ,
        # "disabledforeground": ,
        # "fg": ,
        "font": self.fonts['b'],
        "foreground": self.colors['cyan'],
        # "postcommand": ,
        "relief": "solid",
        # "selectcolor": ,
        # "takefocus": ,
        # "tearoff": ,
        # "tearoffcommand": ,
        # "title": ,
        # "type": ,
      }
      self.sTextKwargs = {
        "state"       : 'disabled',
        "background"  : self.colors['bg3'],
        "foreground"  : self.colors['cyan'],
        "font"        : self.fonts['m'],
        "height"      : 30,
        "width"       : 80,
        "borderwidth" : 1,
        "relief"      : "solid"
      }
      self.sTextBarKwargs = {

      }
    _init_style()

    def _init_vars():
      self.filePath = tk.StringVar(value="")
      self.project = tk.StringVar(value="") 
      self.projects = [
        "36001-2 Sunrise - Las Olas", 
        "36001-2 Jupiter Bridge", 
        "36001-2 North Causeway",
        "36001-2 Town of Palm Beach",
        "36001-2 A1A-Hollywood",
        "36001-2 Loxahatchee Road",
        "36001-4 Beeline Highway"
      ]
      self.etl = tk.StringVar(value="")
      self.etls = [
        "Safety Data ETL", 
        "Secondary Crash Data ETL",
        "Mobility Data ETL",
        "Drive Test Data ETL"
      ]
      self.task = tk.StringVar(value="")
      self.tasks = [
        "Initial Setup", 
        "Monthly ETL process",
        "Data Validation",
        "Process Validation"
      ]
    _init_vars()

    self.title("ETL Tool")
    self.state("zoomed")
    self.configure(background=self.colors["bg3"])
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=9)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    def _init_title_frame():
      self.titleFrame = tk.Frame(self, **self.frameKwargs)
      self.titleFrame.grid(row=0, column=0, columnspan=2, **self.gridKwargs)
      self.titleFrame.grid_rowconfigure(0, weight=1)
      self.titleFrame.grid_columnconfigure(0, weight=1)

      self.titleLabel = tk.Label(self.titleFrame, text="ETL Tool", **self.h1Kwargs) 
      self.titleLabel.grid(row=0, column=0, columnspan=2, **self.gridKwargs)
    _init_title_frame()

    def _init_config_frame():
      self.configFrame = tk.Frame(self, **self.frameKwargs)
      self.configFrame.grid(row=1, column=0, **self.gridKwargs)
      self.configFrame.grid_columnconfigure(0, weight=1)
      self.configFrame.grid_columnconfigure(1, weight=1)

      self.configFrameTitle = tk.Label(self.configFrame, text="Configuration", **self.h2Kwargs)
      self.configFrameTitle.grid(row=0, column=0, columnspan=2, **self.gridKwargs)

      self.selectFileButton = tk.Button(self.configFrame, text="Select File", command=self.selectFile, **self.buttonKwargs)
      self.selectFileButton.grid(row=1, column=0, **self.gridKwargs)

      self.selectedFileLabel = tk.Label(self.configFrame, text="", **self.labelKwargs)
      self.selectedFileLabel.grid(row=1, column=1, **self.gridKwargs)

      self.selectProjectLabel = tk.Label(self.configFrame, text="Select Project: ", **self.labelKwargs)
      self.selectProjectLabel.grid(row=2, column=0, **self.gridKwargs)

      self.projectOptMenu = tk.OptionMenu(self.configFrame, self.project, *self.projects)
      self.projectOptMenu.config(**self.menuButtonKwargs)
      self.projectOptMenu['menu'].config(**self.menuKwargs)
      self.projectOptMenu.grid(row=2, column=1, **self.gridKwargs)

      self.selectEtlLabel = tk.Label(self.configFrame, text="Select ETL Pipeline: ", **self.labelKwargs)
      self.selectEtlLabel.grid(row=3, column=0, **self.gridKwargs)

      self.etlOptMenu = tk.OptionMenu(self.configFrame, self.etl, *self.etls)
      self.etlOptMenu.grid(row=3, column=1, **self.gridKwargs)

      self.selectTaskLabel = tk.Label(self.configFrame, text="Select Task: ", **self.labelKwargs)
      self.selectTaskLabel.grid(row=4, column=0, **self.gridKwargs)

      self.taskOptMenu = tk.OptionMenu(self.configFrame, self.task, *self.tasks)
      self.taskOptMenu.grid(row=4, column=1, **self.gridKwargs)

      self.runButton = tk.Button(self.configFrame, text="Run Task", command=self.runTask, **self.buttonKwargs)
      self.runButton.grid(row=5, column=0, **self.gridKwargs)
    _init_config_frame()

    def _init_output_frame():
      self.outputFrame = tk.Frame(self, **self.frameKwargs)
      self.outputFrame.grid(row=1, column=1, **self.gridKwargs)
      self.outputFrame.grid_rowconfigure(1, weight=1)
      self.outputFrame.grid_columnconfigure(0, weight=1)
      
      self.outputFrameTitle = tk.Label(self.outputFrame, text="Output", **self.h2Kwargs)
      self.outputFrameTitle.grid(row=0, column=0, **self.gridKwargs)

      self.output = ScrolledText(self.outputFrame, **self.sTextKwargs)
      self.output.grid(row=1, column=0, **self.gridKwargs)
      self.output.vbar.config(**self.sTextBarKwargs)
    _init_output_frame()

  def selectFile(self):
    self.filePath = askopenfilename()
    self.selectedFileLabel.config(text=self.filePath)

  def writeOutput(self, text):
    self.output.configure(state='normal')
    self.output.insert(tk.END, text + '\n')
    self.output.see(tk.END)
    self.output.configure(state='disabled')

  def clearOutput(self):
    self.output.configure(state='normal')
    self.output.delete(1.0, tk.END)
    self.output.configure(state='disabled')

  def runTask(self):
    self.clearOutput()
    self.writeOutput(f"{self.project.get()} | {self.etl.get()} | {self.task.get()}")
    self.writeOutput("Running task...")
    self.writeOutput("Task finished.")

if __name__ == "__main__":
  App().mainloop()