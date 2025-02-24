from conta import Conta
from conta import Cliente

cliente_1 = Cliente("Wander", "Luiz", "111222333-44")
conta_1 = Conta("123-4", cliente_1, 300.0)
print("TItular", conta_1.titular.nome)
print("Saldo", conta_1.saldo)
