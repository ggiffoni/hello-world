def quatro_vezes(f):
    f()
    f()
    f()
    f()


def mais_menos():
    print("+", end="")
    print(4 * " -", end=" ")
    print("+", end="")
    print(4 * " -", end=" ")
    print("+")


def barras():
    x = 2 * ("|" + 9 * " ") + "|"
    print(x)


def tabela():
    mais_menos()
    quatro_vezes(barras)
    mais_menos()
    quatro_vezes(barras)
    mais_menos()

tabela()





