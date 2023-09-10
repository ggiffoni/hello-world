import datetime
from Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataabertura = datetime.datetime.today()
        self.extrato = Extrato()


    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}")

    def transferevalor(self, contadestino, valor):
        if self.saldo < valor:
            return "Nao existe saldo suficiente."
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
        return "Transferencia realizada."


def main():
    c1 = Conta(231206, 7684875795, "Giovanni Giffoni", 5500)
    c1.depositar(300)
    saque = c1.sacar(6000)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")

if __name__ == "__main__":
    main()


