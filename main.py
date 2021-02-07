#!/usr/bin/python3
from tkinter import Toplevel, Button, Tk, Menu, Canvas, Text, WORD, INSERT, TRUE, Label
from tkinter import colorchooser, simpledialog
from tkinter import messagebox
import webbrowser



top = Tk()
top.title('Axolotl Studio')


# Globals
bgcolor = 'white'
bgsize = {'x': 100, 'y': 100}
scale = 10


def showAbout():
    title = "Axolotl Studio"
    msg = """Open Source Pixel Art and Animation.
Cross platform graphical pixel art and animation software.
Written in Python 3.
This is free and Open Source Software (MIT License)
    """
    messagebox.showinfo(title, msg)

def openLink():
    webbrowser.open("https://google.com") # Change for Documentation URL

def showFile():
    window = Toplevel()
    window.title('Offline Help')

    configfile = Text(window, wrap=WORD, width=50, height= 20)
    filename='localhelp.txt'
    file = open(filename,'r')
    configfile.insert(INSERT, file.read())
    configfile.pack(fill="none", expand=TRUE)

    button_close = Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')

    

def setScale():
    answer = simpledialog.askstring(title="Set Pixel Scale",
                                    prompt="Pixel Scale (Integer)")
    try:
        global scale
        scale = int(answer)
    except Exception as e:
        print(e)


def setSize():
    answer = simpledialog.askstring(title="Set Image Size",
                                    prompt="Width and Height (Comma separated)")
    try:
        answer = answer.split(',')
        global bgsize
        bgsize['x'] = int(answer[0])*scale
        bgsize['y'] = int(answer[1])*scale

    except Exception as e:
        print(e)


def chooseColor():
    color_code = colorchooser.askcolor(title="Choose Background Colour")
    global bgcolor
    bgcolor = color_code[-1]


def newFile():
    setSize()
    setScale()
    chooseColor()
    canvas = Canvas(top, width=bgsize['x'], height=bgsize['y'], bg=bgcolor)
    canvas.pack()


menubar = Menu(top)
file = Menu(menubar, tearoff=0)
mode = Menu(file, tearoff=0)

mode.add_command(label="Single Image (Color Mode)")
mode.add_command(label="Single Image (TTY Mode)")
mode.add_command(label="Animation (Color Mode)")
mode.add_command(label="Animation (TTY Mode)")

file.add_cascade(label="New", menu=mode)

file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Export to...")
file.add_command(label="Close")

file.add_separator()

file.add_command(label="Exit", command=top.quit)

menubar.add_cascade(label="File", menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=edit)

#background = Menu(menubar, tearoff=0)

#background.add_command(label="Background Color", command=chooseColor)
#background.add_command(label="Image Size (Pixels)", command=setSize)
#background.add_command(label="Square to Pixel scale", command=setScale)

#menubar.add_cascade(label="Options", menu=background)

halp = Menu(menubar, tearoff=0)
halp.add_command(label="About", command=showAbout)
halp.add_command(label="Online Documentation", command=openLink)
halp.add_command(label="Offline Documentation", command=showFile)
menubar.add_cascade(label="Help", menu=halp)


top.attributes('-zoomed', True)
top.config(menu=menubar)
top.mainloop()
