from graphics import *
#Create graphical window
win = GraphWin("Let's Paint", 1000, 1000)
win.setBackground('light gray')

class ARectangle():
        def __init__(self, c1, c2):
            self.c1 = c1
            self.draw(win)
    
        def color(self):
            key = win.getKey()
            if key == "w":
                self.setFill('white')
            elif key == "k":
                self.setFill('black')
            elif key == "b":
                self.setFill('blue')
            elif key == "r":
                self.setFill('red')
            elif key == "y":
                self.setFill('yellow')
            elif key == "n":
                self.setFill('brown')
            elif key == "g":
                self.setFill('green')
            elif key == "p":
                self.setFill('pink')
            pass

class ALine():
        def __init__(self, c1, c2):
            self.c1 = c1
            self.c2 = c2
            

        def drawing(self, w):
            self.testing = Line(self.c1, self.c2)
            self.testing.draw(w)
            
        def color(self):
            key = win.getKey()
            if key == "w":
                self.testing.setOutline('white')
            elif key == "k":
                self.testing.setOutline('black')
            elif key == "b":
                self.testing.setOutline('blue')
            elif key == "r":
                self.testing.setOutline('red')
            elif key == "y":
                self.testing.setOutline('yellow')
            elif key == "n":
                self.testing.setOutline('brown')
            elif key == "g":
                self.testing.setOutline('green')
            elif key == "p":
                self.testing.setOutline('pink')
            pass

def ACircle(win):
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
    elif color1 == "p":
        circ.setFill('pink')
    radi_m.undraw()
    pass

class APolygon():
        def __init__(self, c1, c2, c3):
            self.Polygon(c1, c2, c3)
            self.draw(win)
    
        def color(self):
            key = win.getKey()
            if key == "w":
                self.setFill('white')
            elif key == "k":
                self.setFill('black')
            elif key == "b":
                self.setFill('blue')
            elif key == "r":
                self.setFill('red')
            elif key == "y":
                self.setFill('yellow')
            elif key == "n":
                self.setFill('brown')
            elif key == "g":
                self.setFill('green')
            elif key == "p":
                self.setFill('pink')
            pass

def main():

    condition = True
    while condition:
        message1 = Text(Point(500, 30), 'Press l to draw a Line, s to draw a Rectangle, c to draw a Circle, and p to draw a Polygon')
        message1.draw(win)
        message2 = Text(Point(500,  45), 'After selecting the figure you wish to draw, use your mouse to click on the points where you wish to draw')
        message2.draw(win)
        message_c = Text(Point(500, 60), 'Then, press w for White, k for Black, b for Blue, r for Red, y for Yellow, n for Brown, g for Green, and p for pink')
        message_c.draw(win)
        option = win.getKey() 
        if option == "l":
            c1 = win.getMouse()
            c2 = win.getMouse()
            line = ALine(c1, c2)
            line.drawing(win)
            line.color()
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


main()