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

    style = ttk.Style()
    style.theme_use("clam") 

    colors = {
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
      "green"   : "#859900"
    }

    # relief options:  
      # "flat" 
      # "raised" 
      # "sunken" 
      # "ridge" 
      # "groove" 
      # "solid"

    self.title("ETL Tool")
    self.state("zoomed")
    self.configure(background=colors["bg3"])
    self.rowconfigure(0, weight=1)
    self.rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    style.configure("TFrame",
      background=colors['bg2'],
      borderwidth=10,
      relief="raised",
      padding=10,
      # width=300,
      # height=300
    )
    style.configure("TLabel",
      background=colors["bg2"],
      foreground=colors["cyan"],
      font=("Arial", 10),
      anchor="w",
      justify="left",
      padding=10,
      relief=relief,
      borderwidth=0,
      # wraplength=200
    )
    style.configure("h2.TLabel",
      font=("Arial", 15),
    )
    style.configure("h1.TLabel",
      font=("Arial", 20, "italic"),
    )
    style.configure("TButton",
      background=colors['bg0'],   # color
      foreground=colors['fg0'],   # text color
      font=("Arial", 10),         # tuple like ("Arial", 10)
      relief="flat",              # border style
      borderwidth=0,              # border size
      padding=10,                 # internal padding
      # width=100,                # preferred width in text units
      # height=100,               # preferred height
      anchor="w",                 # content alignment
      justify="left",             # text align (for multi-line)
      # image=,                   # tk.PhotoImage
      # compound=,                # text+image layout
      # takefocus=,               # focusable (0 or 1)
      # focuscolor=,              # color when focused (theme-specific)
      # highlightthickness=       # focus ring size (theme-specific)
    )

    style.configure("TButton",
      background=colors["bg3"],
      foreground=colors["fg1"],
      font=("Arial", 10),
      anchor="nw",
      padding=5,
      borderwidth=5
    )
    style.map("TButton",
      background=[
        ("active", colors["bg3"]),
        ("alternate", colors["bg3"]),
        ("disabled", colors["bg3"]), 
        ("focus", colors["bg3"]),
        ("hover", colors["bg3"]),
        ("invalid", colors["bg3"]),
        ("pressed", colors["bg3"]),
        ("readonly", colors["bg3"]),
        ("selected", colors["bg3"])
      ],
      foreground=[
        ("active", colors["cyan"]),
        ("alternate", colors["cyan"]),
        ("disabled", colors["cyan"]), 
        ("focus", colors["cyan"]),
        ("hover", colors["cyan"]),
        ("invalid", colors["cyan"]),
        ("pressed", colors["cyan"]),
        ("readonly", colors["cyan"]),
        ("selected", colors["cyan"])
      ],
    )
    style.configure("TCombobox",
      fieldbackground=colors["bg3"],
      background=colors["bg3"],
      foreground=colors["fg0"],
      arrowcolor=colors["cyan"],
      bordercolor=colors["bg3"],
      width=30
    )

    projects = [
      "36001-2 Sunrise - Las Olas", 
      "36001-2 Jupiter Bridge", 
      "36001-2 North Causeway",
      "36001-2 Town of Palm Beach",
      "36001-2 A1A-Hollywood",
      "36001-2 Loxahatchee Road",
      "36001-4 Beeline Highway"
    ]
    etl = [
      "Safety Data ETL", 
      "Secondary Crash Data ETL",
      "Mobility Data ETL",
      "Drive Test Data ETL"
    ]
    tasks = [
      "Initial Setup", 
      "Monthly ETL process",
      "Data Validation",
      "Process Validation"
    ]

    self.filePath = tk.StringVar(value="")
    self.project = tk.StringVar(value="") 
    self.etl = tk.StringVar(value="")
    self.task = tk.StringVar(value="")

    self.titleFrame = ttk.Frame(self, style="TFrame")
    self.titleFrame.grid(row=0, column=0, rowspan=1, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky="we")
    self.titleLabel = ttk.Label(self.titleFrame, text="ETL Tool", style="h1.TLabel")
    self.titleLabel.grid(row=0, column=0)

    self.configFrame = ttk.Frame(self, style="TFrame")
    self.configFrame.grid(row=1, column=0, rowspan=1, columnspan=1, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsw")
    self.configFrameTitle = ttk.Label(self.configFrame, text="Configuration", style="h2.TLabel")
    self.configFrameTitle.grid(row=0, column=0)

    self.selectFileButton = ttk.Button(self.configFrame, text="Select File", style="TButton", command=self.selectFile)
    self.selectFileButton.grid(row=1, column=0)
    self.selectedFileLabel = ttk.Label(self.configFrame, text="", style="TLabel")
    self.selectedFileLabel.grid(row=1, column=1)
    self.selectProjectLabel = ttk.Label(self.configFrame, text="Select Project: ", style="TLabel")
    self.selectProjectLabel.grid(row=2, column=0)
    self.projectDropDown = ttk.Combobox(self.configFrame, textvariable=self.project, values=projects, state="readonly", style="TCombobox")
    self.projectDropDown.grid(row=2, column=1)
    self.selectEtlLabel = ttk.Label(self.configFrame, text="Select ETL Pipeline: ", style="TLabel")
    self.selectEtlLabel.grid(row=3, column=0)
    self.etlDropDown = ttk.Combobox(self.configFrame, textvariable=self.etl, values=etl, state="readonly", style="TCombobox")
    self.etlDropDown.grid(row=3, column=1)
    self.selectTaskLabel = ttk.Label(self.configFrame, text="Select Task: ", style="TLabel")
    self.selectTaskLabel.grid(row=4, column=0)
    self.taskDropDown = ttk.Combobox(self.configFrame, textvariable=self.task, values=tasks, state="readonly", style="TCombobox")
    self.taskDropDown.grid(row=4, column=1)
    self.runButton = ttk.Button(self.configFrame, text="Run Task", style="TButton", command=self.runTask)
    self.runButton.grid(row=5, column=0)

    self.outputFrame = ttk.Frame(self, style="TFrame")
    self.outputFrame.grid(row=1, column=1, rowspan=1, columnspan=1, padx=10, pady=10, ipadx=10, ipady=10, sticky="nse")
    self.outputFrameTitle = ttk.Label(self.outputFrame, text="Output", style="h2.TLabel")
    self.outputFrameTitle.grid(row=0, column=0)

    self.output = ScrolledText(self.outputFrame, height=30, width=80, state='disabled', font=("Consolas", 10))
    self.output.grid(row=1, column=0)

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