# Kody Scott
# Section-004
# 12/05/2024
# kodys@email.sc.edu
# Lab14: Drawing Pad

import turtle

# screen setup
win = turtle.Screen()
win.bgcolor("light green")

# creating the turtle/pencil
pencil = turtle.Turtle()
pencil.color("red")
pencil.speed(0)
pencil.turtlesize(1.5)
pencil.pensize(3)

# choosing a pencil color
pencil_color = "red"

# function thats fired when middle mouse button is clicked
def clear_drawing(x, y):
    pencil.clear()

# toggles red or blue when right button is clicked
def toggle_pencil_color(x, y):
    global pencil_color
    if pencil_color == "red":
        pencil_color = "blue"
    else:
        pencil_color = "red"
    pencil.color(pencil_color)

# dragging function
def follow_mouse(x, y):
    pencil.goto(x, y)


# keybinds
pencil.ondrag(follow_mouse)
win.onscreenclick(clear_drawing, btn=2)  # middle mouse click
win.onscreenclick(toggle_pencil_color, btn=3)  # right mouse click



