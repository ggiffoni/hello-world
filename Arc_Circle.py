import turtle
import math

t = turtle.Turtle()
'''
def arco(t, r, angulo):
    comprimento = 2 * math.pi * r * angulo / 360
    n = int(comprimento / 3) + 1
    passo_comprimento = comprimento / n
    passo_angulo = angulo / n

    for i in range(n):
        t.fd(passo_comprimento)
        t.lt(passo_angulo)

'''
# arco(t, 80, 160)

def polyline(t, n, comprimento, angulo):
    for i in range(n):
        t.fd(comprimento)
        t.lt(angulo)


def polygon(t, n , comprimento):
    angulo = 360.0 / n
    polyline(t, n, comprimento, angulo)


def arc(t, r, angulo):
    comprimento = 2 * math.pi * r * angulo / 360
    n = int(comprimento / 3) + 1
    passo_comprimento = comprimento / n
    passo_angulo = angulo / n
    polyline(t, n, passo_comprimento, passo_angulo)


def circulo(t, r):
    arc(t, r, 360)


circulo(t, 200)

turtle.mainloop()
