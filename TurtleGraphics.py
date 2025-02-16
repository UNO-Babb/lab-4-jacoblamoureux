#TurtleGraphics.py
#Name: Jacob Lamoureux
#Date: 2/16/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(fred, corner):
    drawSquare(fred, 100)
    
    if corner == 1:
        fred.begin_fill()
        drawSquare(fred, 50)
        fred.end_fill()
    elif corner == 2:
        fred.forward(50)
        fred.begin_fill()
        drawSquare(fred, 50)
        fred.end_fill()
    elif corner == 3:
        fred.right(90)
        fred.forward(50)
        fred.left(90)
        fred.begin_fill()
        drawSquare(fred, 50)
        fred.end_fill()
    elif corner == 4:
        fred.right(90)
        fred.forward(100)
        fred.left(90)
        fred.forward(50)
        fred.left(90)
        fred.begin_fill()
        drawSquare(fred, 50)
        fred.end_fill()
    
    
def squaresinSquares(jim, num):
    size = 20
    
    for n in range(num):
        
        drawSquare(jim, size)
        jim.penup()
        jim.backward(10)
        jim.left(90)
        jim.forward(10)
        jim.right(90)
        jim.pendown()
        
        size = size + 20
        
        
    
        

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)
    

    # fillCorner(myTurtle, 3) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresinSquares(myTurtle, 20) #draws 5 concentric squares
    # squaresinSquares(myTurtle, 3) #draws 3 concentric squares


main()
