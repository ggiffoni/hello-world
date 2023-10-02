from Contas import Conta

from ContaPoupanca import ContaPoupanca

class ContaRemuneradaPoupanca(Conta, ContaPoupanca):
    def __init__(self, taxaremuneracao, clientes, numero, saldo):
        Conta.__init__(self, clientes, numero, saldo)
        ContaPoupanca.__init__(self, taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao

        

