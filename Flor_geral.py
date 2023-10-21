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
def curva_1(t, r, angulo):
    arc_ah(t, r, angulo)
    t.pu()
    arc_ah(t, r, angulo * 2)
    t.pd()
    arc_ah(t, r, angulo)
    arc_h(t, r, angulo)
    t.pu()
    arc_h(t, r, angulo * 2)
    t.pd()
    arc_h(t, r, angulo)


def curva_2(t, r, angulo):
    t.rt(90)
    arc_ah(t, r, angulo)
    t.pu()
    arc_ah(t, r, angulo * 2)
    t.pd()
    arc_ah(t, r, angulo)
    arc_h(t, r, angulo)
    t.pu()
    arc_h(t, r, angulo * 2)
    t.pd()
    arc_h(t, r, angulo)

arc_ah(t, 100, 90)
t.pu()
arc_ah(t,100,180)
t.pd()
arc_ah(t, 100, 90)

arc_h(t, 100, 90)
t.pu()
arc_h(t,100,180)
t.pd()
arc_h(t, 100, 90)

t.rt(90)

arc_ah(t, 100, 90)
t.pu()
arc_ah(t,100,180)
t.pd()
arc_ah(t, 100, 90)

arc_h(t, 100, 90)
t.pu()
arc_h(t,100,180)
t.pd()
arc_h(t, 100, 90)

#curva_1(t, 100, 90)
#curva_2(t, 100, 90)

def metade_curva_1(t, r, angulo):
    arc_ah(t, r, angulo)
    t.pu()
    arc_ah(t, r, angulo * 3)
    arc_h(t, r, angulo * 3)
    t.pd()
    arc_h(t, r, angulo)

def metade_curva_2(t, r, angulo):
    t.lt(90)
    t.pu()
    arc_ah(t, r, angulo * 3)
    t.pd()
    arc_ah(t, r, angulo)
    arc_h(t, r, angulo)
    t.pu()
    arc_h(t, r, angulo * 3)
    t.rt(90)

def bipetala(t, r, angulo):
    metade_curva_1(t, r, angulo)
    metade_curva_2(t, r, angulo)


def rotacionar(t, r, angulo, passo_angular, n):
    for i in range(n):
        bipetala(t, r, angulo)
        t.rt(passo_angular)
        
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


def rodar_petala(t, r, angulo, passo_angular, n):
    for i in range(n):
        petala(t, r, angulo)
        t.rt(passo_angular)


#metade_curva_1(t, 100, 90)
#metade_curva_2(t, 100, 90)
#bipetala(t, 100, 90)
#rotacionar(t, 100, 90, 60, 4)
#petala(t, 100, 90)

rodar_petala(t, 100, 90, 60, 6)

turtle.mainloop()