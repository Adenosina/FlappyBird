# Main program
# I use this graphics library as I am just learning python thanks to
# John Zelle book ("Python Programming: An introduction to computer science")
# As a comment, this game was intended to be a classic flappy bird
# that's why there are objects with those names. Nonetheless, it 
# ended up having a Star Wars features due to the recently release
# of Star Wars, The Last Jedi.

from graphics import *
from barrier import *
from stars import stars

finalcondition = True
while finalcondition:
    # Setting up the Graphical User Interface
    width, lenght = 1200, 800
    win = GraphWin("Flappy", width, lenght, autoflush=False)
    win.setBackground("black")
    x, y, dy, radium, gravity = 150, 100, 0, 30, 0.1
    barlist = []
    bardiff = 125
    newbarrier = 0
    score = 0
    speedbarrier = -5
    color = "purple"
    flappy = Circle(Point(x, y), radium) # The real object that represents 'flappy bird'
    flappy.setFill("black") # Hide this object which is aprox equal to the tie dimension
    tie = Image(Point(x, y), "tie1.gif") # What you do see in the game
    galaxy = stars(win)
    bar = barrier(win, color, bardiff)
    barlist.append(bar)
    scoreban = Text(Point(width / 1.1, lenght / 10), "SCORE: " + str(score))
    scoreban.setSize(24)
    scoreban.setStyle("bold")
    scoreban.setTextColor("white")
    introbanner1 = Text(Point(width / 2.0, lenght / 2.5), "Control your TIE using <j>")
    introbanner2 = Text(Point(width / 2.0, lenght / 2.0), "PRESS <S> to start the flight")

    for i in [flappy, tie, scoreban, introbanner1, introbanner2]:  # Draw it all
        i.draw(win)
        for j in [introbanner1, introbanner2]:
            j.setSize(24)
            j.setTextColor("yellow")

    Introcondition = win.getKey()
    while not Introcondition == "S":  # Introduction
        Introcondition = win.getKey()
    for i in [introbanner1, introbanner2]:
        i.undraw()


    def losingcondition(flappy, score):  # Lose condition
        """ Or TIE object gets a y-value not valid or it hits a barrier. """
        if flappy.getYcirc() > 800 or barlist[score].flappyimpact(flappy.getYcirc(), radium) \
                or flappy.getYcirc() < 0:
            return True


    while not losingcondition(flappy, score):  # Game itself
        if barlist[newbarrier].getXbar(1) < 450:
            bar = barrier(win, color, bardiff)
            barlist.append(bar)
            newbarrier += 1
        for barriers in barlist:
            barriers.movebar(speedbarrier)
        if 20 > score >= 10:
            bardiff = 115
            speedbarrier = -6
        elif 30 > score >= 20:
            speedbarrier = -7
            bardiff = 105
        elif 40 > score >= 30:
            bardiff = 95
        KeyPressed = win.checkKey()
        if KeyPressed == "j":
            dy -= 5
            dy *= 0.5
            if dy <= -7.5:
                dy = -7.5
        else:
            dy += gravity
        flappy.move(0, dy)
        tie.move(0, dy)
        if barlist[score].getXbar(2) < 140:
            score += 1
        scoreban.setText("SCORE: " + str(score))

    endbanner = Text(Point(width / 2, lenght / 2), "Press Q to quit and R to replay")
    endbanner.setSize(24)
    endbanner.setTextColor("white")
    endbanner.draw(win)

    Gamingcondition = win.getKey()
    while not Gamingcondition == "Q" or Gamingcondition == "R":
        Gamingcondition = win.getKey()
        if Gamingcondition == "R":
            win.close()
            break
        elif Gamingcondition == "Q":
            win.close()
            finalcondition = False
