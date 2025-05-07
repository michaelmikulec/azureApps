import tkinter as tk

class Panel(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master, background="#002b36", borderwidth=2, relief="solid")
    self.grid(sticky="nsew")
    self.label = tk.Label(self, text="Panel", anchor="center")
    self.label.grid(row=0, column=0, sticky="nsew")
