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
    base03      = "#002b36"
    base02      = "#073642"
    base01      = "#586e75"
    base00      = "#657b83"
    base0       = "#839496"
    base1       = "#93a1a1"
    yellow      = "#b58900"
    orange      = "#cb4b16"
    red         = "#dc322f"
    magenta     = "#d33682"
    violet      = "#6c71c4"
    blue        = "#268bd2"
    cyan        = "#2aa198"
    green       = "#859900"

    style = ttk.Style()
    style.theme_use("clam") 

    self.title("ETL Tool")
    self.state("zoomed")
    self.grid_columnconfigure(1, weight=5)
    self.configure(background=base03)

    style.configure("Custom.TFrame",
      background=base02,
      sticky="nw",
      anchor="nw",
      padding=5,
      borderwidth=0
    )
    style.configure("right.TFrame",
      background=base02,
      sticky="ne",
      anchor="ne",
      padding=5,
      borderwidth=0
    )
    style.configure("h1.TLabel",
      background=base02,
      foreground=base1,
      font=("Arial", 20, "italic"),
      justify="left",
      sticky="nw",
      anchor="nw",
      padding=5,
      borderwidth=0
    )
    style.configure("h2.TLabel",
      background=base02,
      foreground=base1,
      font=("Arial", 15),
      justify="left",
      sticky="nw",
      anchor="nw",
      padding=5,
      borderwidth=0
    )
    style.configure("body.TLabel",
      background=base02,
      foreground=base1,
      font=("Arial", 10),
      justify="left",
      sticky="nw",
      anchor="nw",
      padding=5,
      borderwidth=0
    )
    style.configure("Custom.TButton",
      background=base03,
      foreground=base1,
      font=("Arial", 10),
      justify="left",
      sticky="nw",
      anchor="nw",
      padding=5,
      borderwidth=0
    )
    style.map("Custom.TButton",
      background=[("pressed", magenta), ("disabled", magenta), ("active", magenta)],
      foreground=[("disabled", magenta), ("pressed", magenta), ("active", magenta)]
    )
    style.configure("Custom.TCombobox",
      fieldbackground=base03,
      background=base03,
      foreground=base1,
      arrowcolor=cyan,
      bordercolor=base03
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

    self.titleFrame = ttk.Frame(self, style="Custom.TFrame")
    self.titleFrame.grid(row=0, column=0)
    self.titleLabel = ttk.Label(self.titleFrame, text="ETL Tool", style="h1.TLabel")
    self.titleLabel.grid(row=0, column=0)

    self.configFrame = ttk.Frame(self, style="Custom.TFrame")
    self.configFrame.grid(row=1, column=0)
    self.configFrameTitle = ttk.Label(self.configFrame, text="Configuration", style="h2.TLabel")
    self.configFrameTitle.grid(row=0, column=0)
    self.selectFileButton = ttk.Button(self.configFrame, text="Select File", style="Custom.TButton", command=self.selectFile)
    self.selectFileButton.grid(row=1, column=0)
    self.selectedFileLabel = ttk.Label(self.configFrame, text="", style="body.TLabel")
    self.selectedFileLabel.grid(row=1, column=1)
    self.selectProjectLabel = ttk.Label(self.configFrame, text="Select Project: ", style="body.TLabel")
    self.selectProjectLabel.grid(row=2, column=0)
    self.projectDropDown = ttk.Combobox(self.configFrame, textvariable=self.project, values=projects, state="readonly", style="Custom.TCombobox", width=30)
    self.projectDropDown.grid(row=2, column=1)
    self.selectEtlLabel = ttk.Label(self.configFrame, text="Select ETL Pipeline: ", style="body.TLabel")
    self.selectEtlLabel.grid(row=3, column=0)
    self.etlDropDown = ttk.Combobox(self.configFrame, textvariable=self.etl, values=etl, state="readonly", style="Custom.TCombobox", width=30)
    self.etlDropDown.grid(row=3, column=1)
    self.selectTaskLabel = ttk.Label(self.configFrame, text="Select Task: ", style="body.TLabel")
    self.selectTaskLabel.grid(row=4, column=0)
    self.taskDropDown = ttk.Combobox(self.configFrame, textvariable=self.task, values=tasks, state="readonly", style="Custom.TCombobox", width=30)
    self.taskDropDown.grid(row=4, column=1)
    self.runButton = ttk.Button(self.configFrame, text="Run Task", style="Custom.TButton", command=self.runTask)
    self.runButton.grid(row=5, column=0)

    self.outputFrame = ttk.Frame(self, style="right.TFrame")
    self.outputFrame.grid(row=1, column=1)
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