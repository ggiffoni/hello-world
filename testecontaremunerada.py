from Clientes import Cliente
from Contas import Conta
from ContaPoupanca import ContaPoupanca
from ContaRemunerada import ContaRemuneradaPoupanca

cliente1 = Cliente("123","Joao","Rua X")
cliente2 = Cliente("456","Maria","Rua W")

contapoupanca1 = ContaPoupanca(0.1)
contaremunerada1 = ContaRemuneradaPoupanca(0.1,cliente1,5,1000)

print(contaremunerada1.remuneraConta())

print(contaremunerada1.saldo())