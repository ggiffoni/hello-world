from Veiculo import Veiculo

class Onibus(Veiculo):
    def capacidade_assentos(self, capacidade = 70):
        return super().capacidade_assentos(capacidade=70)


onibus1 = Onibus("Viacao 1001", 80, 15)

onibus1.imprimir()
onibus1.capacidade_assentos()