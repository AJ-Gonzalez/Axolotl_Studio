#!/usr/bin/python3
from tkinter import Button, Tk, Menu, Canvas
from tkinter import colorchooser, simpledialog
from tkinter import messagebox


top = Tk()
top.title('Axolotl Studio')


# Globals
bgcolor = 'white'
bgsize = {'x': 100, 'y': 100}
scale = 10

def showAbout():
    messagebox.showinfo("Information","Informative message")
    
def setScale():
    answer = simpledialog.askstring(title="Set image size",
                                    prompt="Width and Height(Comma separated)")
    try:
        global scale
        scale = int(answer)
    except Exception as e:
        print(e)


def setSize():
    answer = simpledialog.askstring(title="Set image size",
                                    prompt="Width and Height(Comma separated)")
    try:
        answer = answer.split(',')
        global bgsize
        bgsize['x'] = int(answer[0])*scale
        bgsize['y'] = int(answer[1])*scale

    except Exception as e:
        print(e)


def chooseColor():  # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    global bgcolor
    bgcolor = color_code[-1]


menubar = Menu(top)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
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

mode = Menu(menubar, tearoff=0)

mode.add_command(label="Color Mode (Single Image)")
mode.add_command(label="TTY Mode (Single image)")
mode.add_command(label="Color Mode (Animation)")
mode.add_command(label="TTY Mode (Animation)")

menubar.add_cascade(label="Mode", menu=mode)

background = Menu(menubar, tearoff=0)

background.add_command(label="Background Color", command=chooseColor)
background.add_command(label="Image Size (Pixels)", command=setSize)
background.add_command(label="Square to Pixel scale", command=setScale)

menubar.add_cascade(label="Options", menu=background)

halp = Menu(menubar, tearoff=0)
halp.add_command(label="About", command=showAbout)
menubar.add_cascade(label="Help", menu=halp)

top.attributes('-zoomed', True)
top.config(menu=menubar)
top.mainloop()
