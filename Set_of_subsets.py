class Solucao:
    def subconjuntos(self, nums):
        saida = [[]]
        for i in nums:
            saida += [lst + [i] for lst in saida]
        return saida




