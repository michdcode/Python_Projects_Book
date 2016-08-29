import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
import fractions


class Spiro:
    """Create turtle that can draw multiple spirographs concurrently."""
    def __init__(self, xc, yc, col, R, r, l):
        self.t = turtle.Turtle()
        self.t.shape('arrow')
        self.step = 5
        self.drawing_complete = False
        self.setparams(xc, yc, col, R, r, l)
        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        """Sets initial parameters."""
        self.xc = xc
        self.yc = yc
        #convert radius of each circle
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        #calculate greatest common demoninator of each radius
        gcd_val = fractions.gcd(self.r, self.R)
        self.nRot = self.r//gcd_val
        self.k = r/float(R)
        self.t.color(*col)
        #store angle
        self.a = 0

    def restart(self):
        """Resets parameters."""
        self.drawing_complete = False
        self.t.showturtle()
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    def draw(self):
        """Draws the spirograph."""
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        self.t.hideturtle()

    def update(self):
        """Draws curve segment by segment to create animation."""
        if self.drawing_complete:
            return
        #increments current angle
        self.a += self.step
        R, k, l = self.R, self.k, self.l
        a = math.radians(self.a)
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        if self.a >= 360*self.nRot:
            self.drawing_complete = True
            self.t.hideturtle()

    def clear(self):
        self.t.clear()


class SpiroAnimator:
    """Animates spirograph."""
    def __init__(self, N):
        self.deltaT = 1
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        self.spiros = []
        for i in range(N):
            rparams = self.genRandomParams()
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
        turtle.ontimer(self.update, self.deltaT)

    def restart(self):
        """Loops through spiros, clears drawings, sets new params & restarts."""
        for spiro in self.spiros:
            spiro.clear()
            rparams = self.genRandomParams()
            spiro.setparams(*rparams)
            spiro.restart()

    def genRandomParams(self):
        """Creates random numbers as parameters for sprio objects for curves. """
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
               random.random(),
               random.random())
        return (xc, yc, col, R, r, l)

    def update(self):
        """Updates all spiros."""
        nComplete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawing_complete:
                nComplete += 1
        if nComplete == len(self.spiros):
            self.restart()
        turtle.ontimer(self.update, self.deltaT)

    def toggleTurtles(self):
        """Will show or hide arrow cursor."""
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()


def save_drawing():
        """Saves drawing as png file."""
        turtle.hideturtle()
        dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName = 'spiro-' + dateStr
        canvas = turtle.getcanvas()
        canvas.postscript(file=fileName + '.eps')
        img = Image.open(fileName + '.eps')
        img.save(fileName + '.png', 'png')
        turtle.showturtle()


def main():
    """Command line arguments."""
    descStr = """Draws spirographs using turtle module."""
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
                        help="The three arguments in sparams: R, r, l.")
    args = parser.parse_args()

    turtle.setup(width=0.8)
    turtle.shape('arrow')
    turtle.title("Spirographs!")
    turtle.onkey(save_drawing, "s")
    turtle.listen()
    turtle.hideturtle()

    if args.sparams:
        params = [float(x) for x in args.sparams]
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        spiroAnim = SpiroAnimator(4)
        turtle.onkey(spiroAnim.restart, "space")

    turtle.mainloop()

if __name__ == '__main__':
    main()
