from graphics import *
#Create graphical window
win = GraphWin("Let's Paint", 1000, 1000)
win.setBackground('light gray')

class ARectangle():
        def __init__(self, c1, c2):
            self.c1 = c1
            self.c2 = c2
    
        def drawing(self, w):
            self.s = Rectangle(self.c1, self.c2)
            self.s.draw(w)

        def color(self):
            key = win.getKey()
            if key == "w":
                self.s.setFill('white')
            elif key == "k":
                self.s.setFill('black')
            elif key == "b":
                self.s.setFill('blue')
            elif key == "r":
                self.s.setFill('red')
            elif key == "y":
                self.s.setFill('yellow')
            elif key == "n":
                self.s.setFill('brown')
            elif key == "g":
                self.s.setFill('green')
            elif key == "p":
                self.s.setFill('pink')
            pass

class ALine():
        def __init__(self, c1, c2):
            self.c1 = c1
            self.c2 = c2
            
        def drawing(self, w):
            self.l = Line(self.c1, self.c2)
            self.l.draw(w)
            
        def color(self):
            key = win.getKey()
            if key == "w":
                self.l.setOutline('white')
            elif key == "k":
                self.l.setOutline('black')
            elif key == "b":
                self.l.setOutline('blue')
            elif key == "r":
                self.l.setOutline('red')
            elif key == "y":
                self.l.setOutline('yellow')
            elif key == "n":
                self.l.setOutline('brown')
            elif key == "g":
                self.l.setOutline('green')
            elif key == "p":
                self.l.setOutline('pink')
            pass

class ACircle():
        def __init__(self, x1, y1, radius):
            self.x1 = x1
            self.y1 = y1
            self.radius = radius

        def drawing(self, w):
            self.c = Circle(Point(self.x1, self.y1), self.radius)
            self.c.draw(w)

        def color(self):
            key = win.getKey()
            if key == "w":
                self.c.setFill('white')
            elif key == "k":
                self.c.setFill('black')
            elif key == "b":
                self.c.setFill('blue')
            elif key == "r":
                self.c.setFill('red')
            elif key == "y":
                self.c.setFill('yellow')
            elif key == "n":
                self.c.setFill('brown')
            elif key == "g":
                self.c.setFill('green')
            elif key == "p":
                self.c.setFill('pink')
            pass

class APolygon():
        def __init__(self, c1, c2, c3):
            self.c1 = c1
            self.c2 = c2
            self.c3 = c3

        def drawing(self, w):
            self.p = Polygon(self.c1, self.c2, self.c3)
            self.p.draw(w)
            
        def color(self):
            key = win.getKey()
            if key == "w":
                self.p.setFill('white')
            elif key == "k":
                self.p.setFill('black')
            elif key == "b":
                self.p.setFill('blue')
            elif key == "r":
                self.p.setFill('red')
            elif key == "y":
                self.p.setFill('yellow')
            elif key == "n":
                self.p.setFill('brown')
            elif key == "g":
                self.p.setFill('green')
            elif key == "p":
                self.p.setFill('pink')
            pass

def main():
    # Instructions
    condition = True
    while condition:
        message1 = Text(Point(500, 30), 'Press l to draw a Line, s to draw a Rectangle, c to draw a Circle, and p to draw a Polygon')
        message1.draw(win)
        message2 = Text(Point(500,  45), 'After selecting the figure you wish to draw, use your mouse to click on the points where you wish to draw')
        message2.draw(win)
        message_c = Text(Point(500, 60), 'Then, press w for White, k for Black, b for Blue, r for Red, y for Yellow, n for Brown, g for Green, and p for pink')
        message_c.draw(win)

        # Options to select and color a figure
        option = win.getKey() 

        if option == "l":
            c1 = win.getMouse()
            c2 = win.getMouse()
            line = ALine(c1, c2)
            line.drawing(win)
            line.color()

        elif option == "s":
             c1 = win.getMouse()
             c2 = win.getMouse()
             rectangle = ARectangle(c1, c2)
             rectangle.drawing(win)
             rectangle.color()

        elif option == "c":
             c1 = win.getMouse()
             x1 = c1.getX()
             y1 = c1.getY()
             radi_m = Text(Point(500, 85), 'Enter the radius of the circle on your terminal and hit enter')
             radi_m.draw(win)
             radius = int(input('Enter the radius of the circle'))
             circle = ACircle(x1, y1, radius)
             circle.drawing(win)
             circle.color()
             radi_m.undraw()

        elif option == "p":
             c1 = win.getMouse()
             c2 = win.getMouse()
             c3 = win.getMouse()
             polygon = APolygon(c1, c2, c3)
             polygon.drawing(win)
             polygon.color()

        # Ask user if he wishes to finish drawing or continue
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