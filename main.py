#!/usr/bin/python3
import PySimpleGUI as sg
import webbrowser

# Globals
title = "Axolotl Studio"
version = 'Alpha 1.0'
msg = """Open Source Pixel Art and Animation.
Cross platform graphical pixel art and animation software.
Written in Python 3.
This is free and Open Source Software (MIT License)
    """
bgcolor = 'white'
bgsize = {'x': 100, 'y': 100}
scale = 10
canvas = 'nocanvas'
active_color = bgcolor

sg.theme('Topanga')
menu_def = [['File', ['New', ['Single Image (TTY)', 'Single Image (Color)', 'Animation (TTY)', 'Animation (Color)'], 'Open', 'Save', 'Export...',['To Image', 'To Video', 'To TTY Animation']]],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', ['About...', 'Offline Documentation', 'Online Documentation']]]

right_click_menu = ['Unused', [
    'Right', '!&Click', '&Menu', 'E&xit', 'Properties']]

layout = [[sg.Menu(menu_def)],
          [sg.Button(' ', button_color=('grey', 'black'), key='black'),
           sg.Button(' ', button_color=('grey', 'white'), key='white')],
          [sg.Button(' ', button_color=('grey', 'red'), key='red'),
           sg.Button(' ', button_color=('grey', 'blue'), key='blue')],
          [sg.Button(' ', button_color=('grey', 'green'), key='green'),
           sg.Button(' ', button_color=('grey', 'grey'), key='grey')],
          ]


window = sg.Window('Axolotl Studio', layout, no_titlebar=False,
                   resizable=True, size=(1000, 768))
window.Finalize()

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    colors = ('black', 'white', 'blue', 'red', 'green', 'grey')
    if event in colors:
        print('Color =>', event)
    if event == 'About...':
        sg.popup(title, version, msg,  grab_anywhere=True)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
