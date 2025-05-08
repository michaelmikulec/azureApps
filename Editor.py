import tkinter as tk

class Editor(tk.Frame):
  def __init__(self, master=None, theme={}):
    super().__init__(master, **theme.frame)
    self.grid()
    self.label = tk.Label(self, text="Editor", **theme.label)
    self.label.grid(row=0, column=0, sticky="nsew")