import numpy as np
import matplotlib.pyplot as plt


def funcao1(x, y):
    return 0.0, 0.16 * y


def funcao2(x, y):
    return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6


def funcao3(x, y):
    return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6


def funcao4(x, y):
    return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44


funcoes = [funcao1, funcao2, funcao3, funcao4]
pontos = 100000
x, y = 0, 0
lista_x = []
lista_y = []

for i in range(pontos):
    funcao = np.random.choice(funcoes, p=[0.01, 0.85, 0.07, 0.07])
    x, y = funcao(x, y)
    lista_x.append(x)
    lista_y.append(y)

plt.scatter(lista_x, lista_y, s=0.2, color="green")
plt.show()


