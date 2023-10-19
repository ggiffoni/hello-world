import turtle
import math

t = turtle.Turtle()
def polygon(t, n, length):

    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


#polygon(t, 30, 10)

def circle(t, r):
    circunferencia = 2 * math.pi * r
    n = 50
#   n = int(circunferencia / 3) + 1
    length = circunferencia / n
    polygon(t, n, length)


circle(t, 200)

