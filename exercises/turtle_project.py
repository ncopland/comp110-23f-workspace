"""Turtle Project.

4 functions implemented 
Program contains a main functoin ()
Drew circles more than twice (lines 18 - 20) by calling the circle function 3 times with different specifications
Used a loop in both the hat and eye section of the program to simplify the code ()
Fill color changed in the hat function
Marker color changed in the eye function
"""


__author__ = "730659660"
 
from turtle import Turtle, done 

 
def main() -> None:
    """The entrypoint of my scene."""
    drawer: Turtle = Turtle()

    drawer.speed(0)

    circle(drawer, 100, 100, 100)
    circle(drawer, 150, 150, 60)
    circle(drawer, 200, 200, 40)
    draw_line(drawer, 210, 120, 120, 50)
    draw_line(drawer, 100, 120, 240, 50)
    draw_eyes(drawer, 180, 180, 10)
    draw_eyes(drawer, 220, 180, 10)
    draw_tophat(drawer, 180, 245, 40)

    done()


def circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle of the given width whose highest point is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 365:
        a_turtle.forward(radius / 60)
        a_turtle.right(1)
        i = i + 1


def draw_line(a_turtle: Turtle, x: float, y: float, angle: float, length: float) -> None:
    """Draw a line of the given width whose end point is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.right(angle)
    a_turtle.forward(length)


def draw_eyes(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Draws a section of a hexagon according to user specifications."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor("blue")
    i: int = 0
    while i < 3:
        a_turtle.forward(size)
        a_turtle.right(60)
        i = i + 1
    
    a_turtle.pencolor("black")


def draw_tophat(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square and a rectangle of the given width whose top-left corner is located at x, y. Also going for the try something fun points with functions fillcolor, begin_fill, and end_fill."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.fillcolor("red")
    a_turtle.begin_fill()

    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1

    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(180)
    a_turtle.left(90)
    a_turtle.forward(width / 3)
    a_turtle.left(90)
    a_turtle.forward(width / 6)
    a_turtle.left(90)
    a_turtle.forward(width / 3 + width + width / 3)
    a_turtle.left(90)
    a_turtle.forward(width / 6)
    a_turtle.left(90)
    a_turtle.forward(width / 3)

    a_turtle.end_fill()


if __name__ == "__main__":
    main()