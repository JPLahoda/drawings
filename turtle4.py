import turtle
t = turtle.Turtle()
t.speed(100)

def drawSquare(t, squareSize):
    for i in range(4):
        t.forward(squareSize)
        t.rt(90)

def drawRow(t, length, squareSize):
    for i in range(length):
        drawSquare(t, squareSize)
        t.forward(squareSize)

def drawGrid(t, size, squareSize):
    for i in range(size):
        drawRow(t, size, squareSize)
        t.rt(180)
        t.forward(squareSize * size)
        t.lt(90)
        t.forward(squareSize)
        t.lt(90)

def drawSquareStairs(t, height, squareSize):
    for i in range(height,0,-1):
        t.pendown()
        drawRow(t, i, squareSize)
        t.rt(180)
        t.forward(squareSize * i)
        t.rt(90)
        t.penup()
        t.forward(squareSize)
        t.rt(90)

def drawNgon(t, numSides, sideLength):
    angle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.lt(angle)

def drawNgonSpiral(t, numSides, sideLength, numShapes):
    for i in range(numShapes):
        drawNgon(t, numSides, sideLength)
        t.rt(720 / 35)

drawNgonSpiral(t, 7, 50, 100)
