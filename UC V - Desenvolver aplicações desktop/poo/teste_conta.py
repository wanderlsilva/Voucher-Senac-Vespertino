from conta import *

cliente_1 = Cliente('Maria', 'Silva', '111222333-44')
cliente_2 = Cliente("José", "Da Silva", "444555666-77")
conta_1 = Conta("123-4", cliente_1, 500.0)
conta_2 = Conta("234-5", cliente_2, 200.0)

conta_1.deposita(100.0)
conta_1.saca(50.0)
conta_1.transfere(conta_2, 200.0)
conta_1.extrato

conta_1.historico.imprime()
conta_2.historico.imprime()



