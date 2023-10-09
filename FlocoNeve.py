from turtle import *

#shape("turtle")

speed(0)

def lado_floco_neve(comprimento, niveis):
    if niveis == 0:
        forward(comprimento)
        return

    comprimento /= 3.0
    lado_floco_neve(comprimento, niveis - 1)
    left(60)
    lado_floco_neve(comprimento, niveis - 1)
    right(120)
    lado_floco_neve(comprimento, niveis - 1)
    left(60)
    lado_floco_neve(comprimento, niveis - 1)


#lado_floco_neve(200, 1)

#mainloop()


def floco_neve(lados, comprimento):
     for i in range(lados):
         lado_floco_neve(comprimento, lados)
         right(360 / lados)


floco_neve(3, 200)

mainloop()

