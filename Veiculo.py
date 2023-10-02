class Veiculo:
    def __init__(self, nome, velocidademaxima, kmlitro):
        self.nome = nome
        self.velocidademaxima = velocidademaxima
        self.kmlitro = kmlitro

    def capacidade_assentos(self, capacidade):
        print(f"A capacidade de assentos do veiculo {self.nome} e: {capacidade}")


    def imprimir(self):
        print(f"Nome = {self.nome}")
        print(f"Velocidade Maxima = {self.velocidademaxima}")
        print(f"Quilometros percorridos por litro = {self.kmlitro}")


modelo_carro = Veiculo("Fusca", 180, 10)
modelo_carro.imprimir()






