from graphics import *

def aRectangle(win):
    c1 = win.getMouse()
    c2 = win.getMouse()
    rect = Rectangle(c1, c2)
    rect.draw(win)
    color1 = win.getKey()
    if color1 == "w":
        rect.setFill('white')
    elif color1 == "k":
        rect.setFill('black')
    elif color1 == "b":
        rect.setFill('blue')
    elif color1 == "r":
        rect.setFill('red')
    elif color1 == "y":
        rect.setFill('yellow')
    elif color1 == "n":
        rect.setFill('brown')
    elif color1 == "g":
        rect.setFill('green')
    pass

def aLine(win):
    c1 = win.getMouse()
    c2 = win.getMouse()
    l = Line(c1, c2)
    l.draw(win)
    color1 = win.getKey()
    if color1 == "w":
        l.setOutline('white')
    elif color1 == "k":
        l.setOutline('black')
    elif color1 == "b":
        l.setOutline('blue')
    elif color1 == "r":
        l.setOutline('red')
    elif color1 == "y":
        l.setOutline('yellow')
    elif color1 == "n":
        l.setOutline('brown')
    elif color1 == "g":
        l.setFill('green')
    pass

def aCircle(win):
    c1 = win.getMouse()
    x1 = c1.getX()
    y1 = c1.getY()
    radi_m = Text(Point(500, 85), 'Enter the radius of the circle on your terminal and hit enter')
    radi_m.draw(win)
    radius = int(input('Enter the radius of the circle'))
    circ = Circle(Point(x1, y1), radius)
    circ.draw(win)
    color1 = win.getKey()
    if color1 == "w":   
        circ.setFill('white')
    elif color1 == "k":
        circ.setFill('black')
    elif color1 == "b":
        circ.setFill('blue')
    elif color1 == "r": 
        circ.setFill('red')
    elif color1 == "y":
        circ.setFill('yellow')
    elif color1 == "n":
        circ.setFill('brown')
    elif color1 == "g":
        circ.setFill('green')
    radi_m.undraw()
    pass

def aPolygon(win):
    c1 = win.getMouse()
    c2 = win.getMouse()
    c3 = win.getMouse()
    poly = Polygon(c1, c2, c3)  
    poly.draw(win)
    color1 = win.getKey()
    if color1 == "w":
        poly.setFill('white')
    elif color1 == "k":
        poly.setFill('black')
    elif color1 == "b":
        poly.setFill('blue')
    elif color1 == "r":
        poly.setFill('red')
    elif color1 == "y":
        poly.setFill('yellow')
    elif color1 == "n":
        poly.setFill('brown')
    elif color1 == "g":
        poly.setFill('green')
    pass

def main():
    #Create graphical window
    win = GraphWin("Let's Paint", 1000, 1000)
    win.setBackground('light gray')
    condition = True
    while condition:
        message1 = Text(Point(500, 30), 'Press l to draw a Line, s to draw a Rectangle, c to draw a Circle, and p to draw a Polygon')
        message1.draw(win)
        message2 = Text(Point(500,  45), 'After selecting the figure you wish to draw, use your mouse to click on the points where you wish to draw')
        message2.draw(win)
        message_c = Text(Point(500, 60), 'Then, press w for White, k for Black, b for Blue, r for Red, y for Yellow, n for Brown, and g for Green')
        message_c.draw(win)
        option = win.getKey() 
        if option == "l":
            aLine(win)
        elif option == "s":
            aRectangle(win)
        elif option == "c":
            aCircle(win)
        elif option == "p":
            aPolygon(win)
        goodbye_m = Text(Point(500, 75), 'After drawing each figure, if you wish to continue drawing press 1 and proceed to do the same steps, if you wish to close the program press 0')
        goodbye_m.draw(win)
        goodbye_k = win.getKey()
        if goodbye_k == "1":
             condition = True
        elif goodbye_k == "0":
             win.close()
        goodbye_m.undraw()
    pass

if __name__ == '__main__':
    main()

 
