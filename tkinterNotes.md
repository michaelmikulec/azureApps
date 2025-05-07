# Notes from Tkinter 8.5 reference: a GUI for Python
**Author**: John W. Shipman</br>
**Link**: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

## Sample Application
```
import tkinter as tk

class App(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
    self.createWidgets()

  def createWidgets(self):
    top=self.winfo_toplevel()                
    top.rowconfigure(0, weight=1)            
    top.columnconfigure(0, weight=1)         
    self.rowconfigure(0, weight=1)           
    self.columnconfigure(0, weight=1)        
    self.quit = tk.Button(self, text='Quit', command=self.quit)
    self.quit.grid(row=0, column=0,          
      sticky=tk.N+tk.S+tk.E+tk.W)

app = App()
app.master.title('Sample application')
app.mainloop()
```

## 3. Definitions
* window
* top-level window
* widget
* frame
* child, parent

## 4.
### 4.1. The .grid() method
w.grid()</br>
args:
* column
* columnspan
* in_
* ipadx
* ipady
* padx
* pady
* row
* rowspan
* sticky
### 4.2. Other grid management methods
w.grid_bbox()</br>
w.grid_forget()</br>
w.grid_info()</br>
w.grid_location()</br>
w.propogate()</br>
w.grid_remove()</br>
w.grid_size()</br>
w.grid_slaves()</br>
### 4.3. Configuring column and row sizes
w.columnconfigure()</br>
w.rowconfigure()</br>
### 4.4. Making the root window resizeable
.winfo_toplevel()</br>

## 5. Standard attributes
widgets have common attributes</br>
each widget has a set of **options** that determine its behavior and appearance</br>
**option** values are specified in the widget's constructor</br>
**option** values can be changed after creation of the widget using the widgets .config() method</br>
use .cget() method to see the currunt **option** values</br>
### 5.1. Dimensions
units: 
* if unspecified: pixels
* c: centimeters
* i: inches
* m: millimeters
* p: printer's points
### 5.2 The coordinate system
* positive x-dir is right
* positive y-dir is down
### 5.3 Colors
* two methods: 
1. specify colors with #rgb, #rrggbb, or #rrrgggbbb in hexadecimal
2. use locally defined standard color names: The colors 'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', and 'magenta' will always be available. Other names may work, depending on your local installation.
### 5.4 Type Fonts
* up to 3 ways to specify type style:
1. as a tuple (\<font family>, \<font size>, \<one space-separated string of modifiers>)
2. create font object by importing tkFont
### 5.5 Anchors
determines where items are placed relative to their context</br>
9 anchor values:
1. tk.NW
2. tk.N
3. tk.NE
4. tk.E
5. tk.SE
6. tk.S
7. tk.SW
8. tk.W
9. tk.CENTER
### 5.6 Relief Styles
determines the 3-d effects of the border around the edge of a widget</br>
default borderwidth = 2</br>
5 relief values:
1. flat
2. raise
3. sunken
4. groove
5. ridge
### 5.7 Bitmaps
bitmap values:
1.  'error' 
2.  'gray75'
3.  'gray50'
4.  'gray25'
5.  'gray12'
6.  'hourglass'
7.  'info'
8.  'questhead'
9.  'question'
10. 'warning'
### 5.8 Cursors
### 5.9 Images
### 5.10 Geometry
A geometry string is a standard way of describing the size and location of a top-level window on a desktop.</br>
A geometry string has this general form: 
```
'w*h±x±y'
```
### 5.11 Window Names
top-level or **root** window: '.'</br>
child window of root window: '.n' where n is an integer</br>
child window of parent window: 'p.n' where p is the integer name of the parent window and n is the integer name of the child window</br>
relative name of a window: 'n' without any prefix</br>
### 5.12 Cap and Join Styles
### 5.13 Dash Patterns
### 5.14 Matching Stipple Patterns

## 6. Exception Handling
The exception raised by most programming errors is tk.TclError.</br>

## 7. The Button Widget
### Button Options
**activebackground**      : color of **widget background** when under **cursor**

**activeforeground**      : color of **widget foreground** when under **cursor**

**anchor**                : where the **text** is positioned within the **widget**

**bd** or **borderwidth** : **width** of the **border** around the **widget**

**bg** or **background**  : color of the **widget background**

**bitmap**                : name of **bitmap** to display on **widget**

**command**               : **function()** or **method()** to call when **widget** is clicked

**cursor**                : **cursor** to display when **cursor** is over the **widget**

**default**               : **tk.NORMAL** by default. **tk.DISABLED** if the **widget** should be initially disabled

**disabledforeground**    : foreground color when **widget** is disabled

**fg** or **foreground**  : foreground color of **widget**

**font**                  : **text font** on **widget**

**height**                : height of **widget** in text lines

**highlightbackground**   : color of **focus highlight** when **widget** does not have focus

**highlightcolor**        : color of **focus highlight** when **widget** has focus

**highlightthickness**    : thickness of **focus highlight**

**image**                 : **image** to be displayed on **widget**

**justify**               : how to **justify** multiple lines of **text** on **widget**

**overrelief**            : **relief** while **cursor** is over **widget**

**padx**                  : additional **x-padding** for **widget text**

**pady**                  : additional **y-padding** for **widget text**

**relief**                : **relief** of **widget**

**repeatdelay**           :

**repeatinterval**        :

**state**                 :

**takefocus**             : set to zero to not allow keyboard to focus **widget**

**text**                  : **text** to be displayed on **widget**

**textvariable**          : **StringVar()** associated with **widget text**

**underline**             : string indicies of **text** characters to be underlined. -1 for no underline

**width**                 : **width** of **widget** in characters

**wraplength**            : positive values set the **wrap length**

### methods

**.flash()**: causes button to flash several times between active and normal colors

**.invoke()**: calls the button's command callback, and returns what that function returns.

## 8. The Canvas Widget
## 9. The Checkbutton Widget

A checkbutton is either **on** or **off**

The checkbutton *box* that shows its **state** is called the **indicator**

The **label** is the **text** that appears next to the **indicator**

Requires **control variables**, instances of **IntVar()**, to interact with the program

**Event bindings** may be tied to **Checkbuttons**

**Checkbutton indicator** may be removed to make the widget a **push-push button**

### Checkbutton Options

**activebackground**      : color of **widget background** when under **cursor**

**activeforeground**      : color of **widget foreground** when under **cursor**

**anchor**                : where the **text** is positioned within the **widget**

**bd** or **borderwidth** : **width** of the **border** around the **widget**

**bg** or **background**  : color of the **widget background**

**bitmap**                : name of **bitmap** to display on **widget**

**command**               : **function()** or **method()** to call when **widget** is clicked

**cursor**                : **cursor** to display when **cursor** is over the **widget**

**default**               : **tk.NORMAL** by default. **tk.DISABLED** if the **widget** should be initially disabled

**disabledforeground**    : foreground color when **widget** is disabled

**fg** or **foreground**  : foreground color of **widget**

**font**                  : **text font** on **widget**

**height**                : height of **widget** in text lines

**highlightbackground**   : color of **focus highlight** when **widget** does not have focus

**highlightcolor**        : color of **focus highlight** when **widget** has focus

**highlightthickness**    : thickness of **focus highlight**

**image**                 : **image** to be displayed on **widget**

**indicatoron**           : whether or not to display **indicator**. can be 0 or 1

**justify**               : how to **justify** multiple lines of **text** on **widget**

**overrelief**            : **relief** while **cursor** is over **widget**

**padx**                  : additional **x-padding** for **widget text**

**pady**                  : additional **y-padding** for **widget text**

**relief**                : **relief** of **widget**

**repeatdelay**           :

**repeatinterval**        :

**state**                 :

**takefocus**             : set to zero to not allow keyboard to focus **widget**

**text**                  : **text** to be displayed on **widget**

**textvariable**          : **StringVar()** associated with **widget text**

**underline**             : string indicies of **text** characters to be underlined. -1 for no underline

**variable**              : **control variable** that tracks the **widget's state**

**width**                 : **width** of **widget** in characters

**wraplength**            : positive values set the **wrap length**

## 10. The Entry widget
## 11. The Frame Widget
## 12. The Label Widget
## 13. The LabelFrame Widget
## 14. The Listbox Widget
## 15. The Menu Widget
## 16. The Menubutton Widget
## 17. The Message Widget
## 18. The OptionMenu Widget
## 19. The PanedWindow Widget
## 20. The Radiobutton Widget
## 21. The Scale Widget
## 22. The Scrollbar Widget
## 23. The Spinbox Widget
## 24. The Text Widget
## 25. Toplevel: Top-level window methods
## 26. Universal Widget Methods
## 27. Standardizing Appearance and the Option Database