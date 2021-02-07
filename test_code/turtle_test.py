
import turtle
import tkinter as tk


def do_stuff():
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)


def press():
    do_stuff()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("cyan")
    canvas = screen.getcanvas()
    button = tk.Button(canvas.master, text="Press me", command=press)
    canvas.create_window(-200, -200, window=button)
    my_lovely_turtle = turtle.Turtle(shape="turtle")
    turtle.done()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
	
import turtle
import tkinter as tk
 
 
def do_stuff():
    my_lovely_turtle.setpos(100,200)
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        
        my_lovely_turtle.right(120)
 
 
def press():
    do_stuff()
 
 
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("cyan")
    canvas = screen.getcanvas()
    button = tk.Button(canvas.master, text="Press me", command=press)
    canvas.create_window(-200, -200, window=button)
    my_lovely_turtle = turtle.Turtle(shape="turtle")
    turtle.done()