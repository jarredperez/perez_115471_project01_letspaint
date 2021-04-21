from graphics import *

def aRectangle(win):
    c1 = win.getMouse()
    c2 = win.getMouse()
    rect = Rectangle(c1, c2)
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
    rect.draw(win)
    pass

def aLine(win):
    c1 = win.getMouse()
    c2 = win.getMouse()
    l = Line(c1, c2)
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
    l.draw(win)
    pass

def aCircle(win):
    c1 = win.getMouse()
    c2 = win.getMouse()
    c3 = Entry(Point(500, 60), 3)
    circ = Circle((c1, c2), c3)  
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
    circ.draw(win)
    pass

def aPolygon(win):
    c1 = win.getMouse()
    c2 = win.getMouse()
    c3 = win.getMouse()
    poly = Polygon(c1, c2, c3)  
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
    poly.draw(win)
    pass

def main():
    #Create graphical window
    win = GraphWin("Let's Paint", 1000, 1000)
    win.setBackground('light gray')
    condition = True
    while condition:
        message = Text(Point(500, 30), 'Press l to draw a Line, s to draw a Rectangle, c to draw a Circle, and p to draw a Polygon')
        message.draw(win)
        message_c = Text(Point(500, 50), 'Press w for White, k for Black, b for Blue, r for Red, y for Yellow, and n for Brown')
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
        goodbye_m = Text(Point(500, 70), 'If you wish to continue drawing press 1, if you wish to close the program press esc')
        goodbye_m.draw(win)
        goodbye_k = win.getKey()
        if goodbye_k == "1":
             condition = True
        elif goodbye_k == "esc":
             win.close()
    
    pass

main()
 
