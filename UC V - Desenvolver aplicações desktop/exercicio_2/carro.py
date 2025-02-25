class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade = max(0, self.velocidade - valor)

    def exibir_dados(self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} Km/h")

##### Testando a Classe Carro ###
carro1 = Carro("Fusca", 1980)
carro1.acelerar(50)
carro1.frear(20)
carro1.exibir_dados()