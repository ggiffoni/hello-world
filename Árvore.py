from turtle import *

shape("turtle")

speed(0)

def arvore(tamanho, niveis, angulo):
    if niveis == 0:
        color("yellow")
        dot(tamanho / 2)
        color("black")
        return

    forward(tamanho)
    right(angulo)

    arvore(tamanho * 0.8, niveis -1, angulo)

    left(angulo * 2)

    arvore(tamanho * 0.8, niveis - 1, angulo)

    right(angulo)
    backward(tamanho)

left(90)
arvore(70, 7, 20)

mainloop()

