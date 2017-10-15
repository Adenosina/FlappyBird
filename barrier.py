# Class that creates a barrier that moves along the x-coordenate.

from graphics import *
from random import *


class barrier:
    def __init__(self, win, color, bardiff):
        self.win = win
        self.randy1 = randrange(0, self.win.getHeight() / 2, 1)
        self.randy2 = randrange(-self.win.getHeight() / 2, self.win.getHeight() / 2, 1)
        self.y1 = self.randy1
        self.y2 = self.win.getHeight() / 1.5 + self.randy2
        while True:  # Random barrier generator
            self.randy1 = randrange(-self.win.getHeight() / 2, self.win.getHeight() / 2, 1)
            self.randy2 = randrange(-self.win.getHeight() / 2, self.win.getHeight() / 2, 1)
            self.y1 = self.win.getHeight() / 2.2 + self.randy1
            self.y2 = self.win.getHeight() / 1.7 + self.randy2
            if self.y1 < self.y2 and self.y1 > 200 and self.y2 < 600 \
                    and bardiff >= self.y2 - self.y1 >= 90:
                break

        self.y1list, self.y2list = [], []
        for i in range(0, int(self.y1 + 1)):
            self.y1list.append(i)
        for i in range(int(self.y1), int(self.win.getHeight() + 1)):
            self.y2list.append(i)

        self.p1 = Point(self.win.getWidth() / 1.1, 0)  # Up left
        self.p2 = Point(self.win.getWidth(), self.y1)  # Down right
        self.p3 = Point(self.win.getWidth() / 1.1, self.win.getHeight())  # Down left
        self.p4 = Point(self.win.getWidth(), self.y2)  # Up right
        self.Upbarrier = Rectangle(self.p1, self.p2)
        self.Downbarrier = Rectangle(self.p3, self.p4)
        for i in [self.Upbarrier, self.Downbarrier]:  # Draws rectangle
            i.setFill(color)
            i.draw(self.win)

    def movebar(self, xmov):
        self.Upbarrier.move(xmov, 0)
        self.Downbarrier.move(xmov, 0)

    def getXbar(self, whichpoint):
        upbarpoint1 = self.Upbarrier.getP1()
        upbarpoint2 = self.Upbarrier.getP2()
        if whichpoint == 1:
            return upbarpoint1.getX()
        elif whichpoint == 2:
            return upbarpoint2.getX()

    def flappyimpact(self, ycenter, radium):
        """ Returns True if the object has hit a barrier. """
        yvariationpos, yvariationneg, yflappyvalues, xlist = 0, 0, [], []
        for i in range(120, 181):
            xlist.append(i)
        upbarpoint1 = self.Upbarrier.getP1()
        upbarpoint2 = self.Upbarrier.getP2()  # Up rectangle UPDATE coordenates
        downbarpoint = self.Downbarrier.getP2()  # Down rectangle UPDATE coordenates
        if upbarpoint1.getX() <= 180 or downbarpoint.getX() <= 120:
            # If the barrier has reached the x-interval of the object.
            downcircle = (ycenter + radium)
            topcircle = (ycenter - radium)
            if topcircle <= upbarpoint2.getY() or downcircle >= downbarpoint.getY():
                # If the top or bottom of the circle hits the barrier.
                return True
