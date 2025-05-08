from tkinter import ttk
import tkinter as tk

class Theme(ttk.Style):
  def __init__(self, root):
    super().__init__(root)
    self.theme_use('clam')
    self.font = ("Arial", 12)
    self.monoFont = ("Consolas", 12)
    self.justify = "left"
    self.anchor = "center"
    self.background = "#002b36"
    self.foreground = "#2aa198"
    self.activebackground = "#2aa198"
    self.activeforeground = "#002b36"
    self.disabledforeground = "#657b83"
    self.highlightbackground = "#002b36"
    self.highlightcolor = "#2aa198"
    self.highlightthickness = 1
    self.borderwidth = 1
    self.relief = "solid"
    self.configure(
      'Menubar.TButton',

      
    )


root = tk.Tk()
style = ttk.Style(root)
print(style.configure('TButton'))
