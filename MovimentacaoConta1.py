from Contas import Conta
conta1 = Conta(1, 123, "Joao", 0)
conta2 = Conta(3, 456, "Maria", 0)

conta1.depositar(1000)
conta1.transferevalor(conta2, 500)

print(f"Saldo da conta1: {conta1.saldo} \nSaldo da conta2: {conta2.saldo}")
