from conta import Conta

c1 = Conta('123-9', 'Wander', 100.0)
c1.deposita(100.0)
print("Titular : ", c1.titular)
print("Saldo : ", c1.saldo)
print("Limite : ", c1.limite)

c2 = Conta('442-8', 'Maria', 200.0)
c2.deposita(200.0)
print("Titular : ", c2.titular)
print("Saldo : ", c2.saldo)
print("Limite : ", c2.limite)

c3 = Conta('352-7', 'Carla', 300.0)
c3.deposita(300.0)
print("Titular : ", c3.titular)
print("Saldo : ", c3.saldo)
print("Limite : ", c3.limite)

c1.transfere(c3, 50.0)
print("Titular", c1.titular)
print("Saldo", c1.saldo)
print("Titular", c3.titular)
print("Saldo", c3.saldo)