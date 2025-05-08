import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Tkinter App with Terminal Output")

    self.output = ScrolledText(self, height=20, width=80, state='disabled', font=('Courier', 10))
    self.output.pack(padx=10, pady=10)

    self.run_button = tk.Button(self, text="Run Task", command=self.run_task)
    self.run_button.pack(pady=5)

  def write_to_output(self, text):
    self.output.configure(state='normal')
    self.output.insert(tk.END, text + '\n')
    self.output.see(tk.END)
    self.output.configure(state='disabled')

  def run_task(self):
    self.write_to_output("Running task...")
    # You can print anything here
    self.write_to_output("Task finished.")

# app = App()
# app.mainloop()

root = tk.Tk() 
# menubar = tk.Menu(root)
# root.config(menu=menubar)
# file_menu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="Open", command=...)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
root.mainloop()