from conta import Conta

c1 = Conta('123-9', 'Wander', 100.0, 4000.0)
c1.deposita(100.0)
print("Titular : ", c1.titular)
print("Saldo : ", c1.saldo)

c2 = Conta('442-8', 'Maria', 200.0, 4000.0)
c2.deposita(200.0)
print("Titular : ", c2.titular)
print("Saldo : ", c2.saldo)

c3 = Conta('352-7', 'Carla', 300.0, 4000.0)
c3.deposita(300.0)
print("Titular : ", c3.titular)
print("Saldo : ", c3.saldo)