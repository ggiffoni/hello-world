import turtle
import math

t = turtle.Turtle()

def polyline_e(t, n, comprimento, angulo):
    for i in range(n):
        t.fd(comprimento)
        t.lt(angulo)


def arc_e(t, r, angulo):
    comprimento = 2 * math.pi * r * angulo / 360
    n = int(comprimento / 3) + 1
    passo_comprimento = comprimento / n
    passo_angulo = angulo / n
    polyline_e(t, n, passo_comprimento, passo_angulo)


def polyline_d(t, n, comprimento, angulo):
    for i in range(n):
        t.fd(comprimento)
        t.rt(angulo)


def arc_d(t, r, angulo):
    comprimento = 2 * math.pi * r * angulo / 360
    n = int(comprimento / 3) + 1
    passo_comprimento = comprimento / n
    passo_angulo = angulo / n
    polyline_d(t, n, passo_comprimento, passo_angulo)


#arc_e(t, 100, 360)
arc_e(t, 100, 90)
t.pu()
x = arc_e(t,100,180)
t.pd()
arc_e(t, 100, 90)

arc_d(t, 100, 90)
t.pu()
x = arc_d(t,100,180)
t.pd()
arc_d(t, 100, 90)

#arc_d(t, 100, 360)
t.rt(90)

arc_e(t, 100, 90)
t.pu()
x = arc_e(t,100,180)
t.pd()
arc_e(t, 100, 90)

arc_d(t, 100, 90)
t.pu()
x = arc_d(t,100,180)
t.pd()
arc_d(t, 100, 90)


turtle.mainloop()