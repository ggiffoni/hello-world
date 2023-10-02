from Contas import Conta
from Clientes import Cliente
from ContaEspecial import ContaEspecial

cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria", "Rua 2")
cliente3 = Cliente ("789","Joana", "Rua H")

conta1 = Conta([cliente1, cliente2], 1, 2000)
conta2 = ContaEspecial([cliente3],3,1000,2000)
conta2.depositar(100)
conta2.sacar(3200)

print(conta2.extrato.extrato(conta2.numero))
print(conta2.saldo)


