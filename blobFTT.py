import os
import json
import tkinter as tk
from tkinter.filedialog import askopenfilenames
from azure.storage.blob import BlobServiceClient

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Blob Storage File Transfer Tool")
    self.state("zoomed")
    self.grid_columnconfigure(1, weight=5)

    font = ("Arial", 10)
    justify = "left"
    padx = 5
    pady = 5
    anchor = "nw"
    sticky = "nw"

    self.filePaths = []
    self.configPath = [] 
    self.blobName = tk.StringVar(value="")
    self.stgAccName = tk.StringVar(value="")
    self.stgAccKey = tk.StringVar(value="")
    self.containerName = tk.StringVar(value="")

    self.frame0 = tk.Frame(self)
    self.frame0.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
    self.selectFilesButton = tk.Button(self.frame0, text="Select Files", font=font, justify=justify, anchor=anchor, command=self.selectFiles)
    self.selectFilesButton.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)

    self.frame1 = tk.Frame(self)
    self.frame1.grid(row=1, column=0, sticky=sticky, padx=padx, pady=pady)
    self.selectedFilesLabel = tk.Label(self.frame1, text="Selected Files: ", font=font, justify=justify, anchor=anchor)
    self.selectedFilesLabel.grid(row=0, column=1, sticky=sticky, padx=padx, pady=pady)

    self.frame2 = tk.Frame(self)
    self.frame2.grid(row=2, column=0, sticky=sticky, padx=padx, pady=pady)
    self.selectConfigButton = tk.Button(self.frame2, text="Select Config", font=font, justify=justify, anchor=anchor, command=self.selectConfig)
    self.selectConfigButton.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)

    self.frame3 = tk.Frame(self)
    self.frame3.grid(row=3, column=0, sticky=sticky, padx=padx, pady=pady)
    self.selectedConfigLabel = tk.Label(self.frame3, text="Selected Config: ", font=font, justify=justify, anchor=anchor)
    self.selectedConfigLabel.grid(row=0, column=1, sticky=sticky, padx=padx, pady=pady)

    # self.frame2 = tk.Frame(self)
    # self.frame2.grid(row=2, column=0, sticky=sticky, padx=padx, pady=pady)
    # self.stgAccNameLabel = tk.Label(self.frame2, text="Storage Account Name: ", font=font, justify=justify, anchor=anchor)
    # self.stgAccNameLabel.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
    # self.stgAccNameEntry = tk.Entry(self.frame2, textvariable=self.stgAccName, font=font, justify=justify)
    # self.stgAccNameEntry.grid(row=0, column=1, sticky=sticky, padx=padx, pady=pady)

    # self.frame3 = tk.Frame(self)
    # self.frame3.grid(row=3, column=0, sticky=sticky, padx=padx, pady=pady)
    # self.stgAccKeyLabel = tk.Label(self.frame3, text="Storage Account Key: ", font=font, justify=justify, anchor=anchor)
    # self.stgAccKeyLabel.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
    # self.stgAccKeyEntry = tk.Entry(self.frame3, textvariable=self.stgAccKey, font=font, justify=justify)
    # self.stgAccKeyEntry.grid(row=0, column=1, sticky=sticky, padx=padx, pady=pady)

    # self.frame4 = tk.Frame(self)
    # self.frame4.grid(row=4, column=0, sticky=sticky, padx=padx, pady=pady)
    # self.containerNameLabel = tk.Label(self.frame4, text="Container Name: ", font=font, justify=justify, anchor=anchor)
    # self.containerNameLabel.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
    # self.containerNameEntry = tk.Entry(self.frame4, textvariable=self.containerName, font=font, justify=justify)
    # self.containerNameEntry.grid(row=0, column=1, sticky=sticky, padx=padx, pady=pady)

    self.frame5 = tk.Frame(self)
    self.frame5.grid(row=5, column=0, sticky=sticky, padx=padx, pady=pady)
    self.uploadButton = tk.Button(self.frame5, text="Upload Files", font=font, justify=justify, anchor=anchor, command=self.uploadFiles)
    self.uploadButton.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)

    # self.frame6 = tk.Frame(self)
    # self.frame6.grid(row=1, column=1, sticky=sticky, padx=padx, pady=pady)
    # self.blobNameLabel = tk.Label(self.frame6, text="Blob Name: ", font=font, justify=justify, anchor=anchor)
    # self.blobNameLabel.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
    # self.blobNameEntry = tk.Entry(self.frame6, textvariable=self.blobName, font=font, justify=justify)
    # self.blobNameEntry.grid(row=0, column=1, sticky=sticky, padx=padx, pady=pady)

    self.frame8 = tk.Frame(self)
    self.frame8.grid(row=2, column=1, sticky=sticky, padx=padx, pady=pady)
    self.downloadButton = tk.Button(self.frame8, text="Download Blob", font=font, justify=justify, anchor=anchor, command=self.downloadBlob)
    self.downloadButton.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)

  def selectFiles(self):
    self.filePaths = askopenfilenames()
    self.selectedFilesLabel.config(text="Selected Files:\n" + "\n".join(self.filePaths))
  
  def selectConfig(self):
    self.configPath = askopenfilenames()
    self.selectedConfigLabel.config(text="Selected Config:\n" + "\n".join(self.configPath))
    with open(self.configPath[0], "r") as configFile:
      config = json.load(configFile)
    self.connectionString = config["connectionString"]
    self.containerName = config["containerName"]
    self.blobName = config["blobName"]

  def uploadFiles(self):
    containerClient = BlobServiceClient\
      .from_connection_string(self.connectionString)\
      .get_container_client(self.containerName)
    for filePath in self.filePaths:
      fileName = os.path.basename(filePath)
      with open(filePath, "rb") as file:
        containerClient.upload_blob(fileName, file, overwrite=True)
    tk.messagebox.showinfo("Done", f"Uploaded {len(self.filePaths)} file(s) to blob storage container {self.containerName}")

  def downloadBlob(self):
    blobClient = BlobServiceClient\
      .from_connection_string(self.connectionString)\
      .get_container_client(self.containerName)\
      .get_blob_client(self.blobName)
    with open(self.blobName, "wb") as file:
      file.write(blobClient.download_blob().readall())
    tk.messagebox.showinfo("Done", f"Downloaded blob {self.blobName} from storage container {self.containerName}")

  # def uploadFiles(self):
  #   connectionString = (
  #     f"DefaultEndpointsProtocol=https;"
  #     f"AccountName={self.stgAccName.get()};"
  #     f"AccountKey={self.stgAccKey.get()};"
  #     f"EndpointSuffix=core.windows.net"
  #   )
  #   containerClient = BlobServiceClient\
  #     .from_connection_string(connectionString)\
  #     .get_container_client(self.containerName.get())
  #   for filePath in self.filePaths:
  #     fileName = os.path.basename(filePath)
  #     with open(filePath, "rb") as file:
  #       containerClient.upload_blob(fileName, file, overwrite=True)
  #   tk.messagebox.showinfo("Done", f"Uploaded {len(self.filePaths)} file(s) to blob storage container {self.containerName.get()}")

  # def downloadBlob(self):
  #   connectionString = (
  #     f"DefaultEndpointsProtocol=https;"
  #     f"AccountName={self.stgAccName.get()};"
  #     f"AccountKey={self.stgAccKey.get()};"
  #     f"EndpointSuffix=core.windows.net"
  #   )
  #   containerClient = BlobServiceClient\
  #     .from_connection_string(connectionString)\
  #     .get_container_client(self.containerName.get())
  #   blobClient = containerClient.get_blob_client(self.blobName.get())
  #   with open(self.blobName.get(), "wb") as file:
  #     file.write(blobClient.download_blob().readall())
  #   tk.messagebox.showinfo("Done", f"Downloaded blob {self.blobName.get()} from storage container {self.containerName.get()}")

if __name__ == "__main__":
  App().mainloop()