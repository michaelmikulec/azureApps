fonts = {
  "h1": ("Arial", 24),
  "h1i": ("Arial", 24, "italic"),
  "h1b": ("Arial", 24, "bold"),
  "h2": ("Arial", 20),
  "h2i": ("Arial", 20, "italic"),
  "h2b": ("Arial", 20, "bold"),
  "b": ("Arial", 10),
  "bi": ("Arial", 10, "italic"),
  "bb": ("Arial", 10, "bold"),
  "m": ("Consolas", 12),
  "mi": ("Consolas", 12, "italic"),
  "mb": ("Consolas", 12, "bold"),
}
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
  "green"   : "#859900",
  "white"   : "#ffffff",
  "black"   : "#000000",
}
background = colors['bg3']
foreground = colors['cyan']
activebackground =  colors['cyan']
activeforeground = colors['bg3']
disabledforeground = colors['bg0']
highlightbackground = colors['bg3']
highlightcolor = colors['cyan']
highlightthickness = borderwidth = 1
relief = "solid"

frameTheme = {
  "background"  : background,
  "borderwidth" : borderwidth,
  "relief"      : relief,
}
labelTheme = {
  "background"  : background,
  "foreground"  : foreground,
  "font"        : fonts['b'],
  "justify"     : "left",
  "anchor"      : "center",
  "borderwidth" : borderwidth,
  "relief"      : relief,
}
buttonTheme = {
  "background"  : background,
  "foreground"  : foreground,
  "font"        : fonts['b'],
  "justify"     : "left",
  "anchor"      : "center",
  "borderwidth" : borderwidth,
  "relief"      : relief,
}

# h1Kwargs = {
#   **labelTheme,
#   "font": fonts['h1i'],
# }
# h2Kwargs = {
#   **labelTheme,
#   "font": fonts['h2i'],
# }
# menuButtonTheme = {
#   "background": bg,
#   "bg": bg,
#   "activebackground": colors['cyan'],
#   "disabledforeground": colors['bg0'],
#   "foreground": fg,
#   "fg": fg,
#   "activeforeground": colors['bg3'],
#   # "bitmap": ,
#   "cursor": "hand2",
#   "direction": "below",
#   "highlightbackground": colors['bg3'],
#   "highlightcolor": colors['cyan'],
#   "highlightthickness": bd,
#   # "image": ,
#   "indicatoron": True,
#   # "anchor": ,
#   "padx": padx,
#   "pady": pady,
#   "borderwidth": bd,
#   "bd": bd,
#   "relief": relief,
#   "font": fonts['b'],
#   # "text": "",
#   # "textvariable": "",
#   # "underline": ,
#   # "justify": ,
#   # "height": ,
#   # "width": 30,
#   # "wraplength": 40,
#   # "menu": ,
#   # "compound": ,
#   # "state": ,
#   # "takefocus": ,
# }
# menuTheme = { 
#   "activebackground": colors['cyan'],
#   "background": bg,
#   "bg": bg,
#   "activeforeground": colors['bg3'],
#   "disabledforeground": colors['violet'],
#   "foreground": fg,
#   "fg": fg,
#   "borderwidth": bd,
#   "bd": bd,
#   "activeborderwidth": bd,
#   # "cursor": ,
#   "font": fonts['b'],
#   "relief": relief,
#   "selectcolor": colors['bg1'],
#   # "title": "",
#   "type": "normal",
#   # "takefocus": True,
#   # "tearoff": True,
#   # "tearoffcommand": True,
#   # "postcommand": ,
# }
# sTextKwargs = {
#   "state"       : 'disabled',
#   "background"  : colors['bg3'],
#   "foreground"  : colors['cyan'],
#   "font"        : fonts['m'],
#   "height"      : 30,
#   "width"       : 80,
#   "borderwidth" : 1,
#   "relief"      : "solid"
# }