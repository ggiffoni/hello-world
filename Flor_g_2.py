import turtle
import math

t = turtle.Turtle()

def polyline_ah(t, n, comprimento, angulo):
    for i in range(n):
        t.fd(comprimento)
        t.lt(angulo)


def arc_ah(t, r, angulo):
    comprimento = 2 * math.pi * r * angulo / 360
    n = int(comprimento / 3) + 1
    passo_comprimento = comprimento / n
    passo_angulo = angulo / n
    polyline_ah(t, n, passo_comprimento, passo_angulo)


def polyline_h(t, n, comprimento, angulo):
    for i in range(n):
        t.fd(comprimento)
        t.rt(angulo)


def arc_h(t, r, angulo):
    comprimento = 2 * math.pi * r * angulo / 360
    n = int(comprimento / 3) + 1
    passo_comprimento = comprimento / n
    passo_angulo = angulo / n
    polyline_h(t, n, passo_comprimento, passo_angulo)
'''
def petala(t, r, angulo):
    arc_ah(t, r, angulo)
    t.pu()
    arc_ah(t, r, angulo * 3)
    t.pd()
    t.lt(90)
    arc_h(t, r, angulo)
    t.pu()
    arc_h(t, r, angulo * 3)
    t.pd()
    t.rt(90)
    
'''


def petala2(t, r, angulo):
    arc_ah(t, r, angulo)
    t.pu()
    t.setpos((0, 0))
    t.pd()
    arc_h(t, r, angulo)
    t.pu()
    t.setpos((0, 0))
    t.pd()


def flor(t, r, angulo, n):
    for i in range(n):
        petala2(t, r, angulo)
        t.rt(360 / n)


flor(t, 100, 90, 3)

#petala2(t, 100, 90)

turtle.mainloop()