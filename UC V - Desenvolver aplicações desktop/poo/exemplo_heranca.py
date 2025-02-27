# Classe base (Superclasse)
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_dados(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano:{self.ano}")

    def ligar(self):
        print(f"O {self.modelo} está ligado.")

#Subclasse Carro herdando de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano) #chama o construtor da superclasse
        self.portas = portas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Portas: {self.portas}")
    
    def ligar(self):
        print(f"O carro {self.modelo} está ligado. Pronto para dirigir")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cilindradas: {self.cilindradas}")
    
    def ligar(self):
        print(f"A moto {self.modelo} está ligada. Capacete obrigatório")

#Criando objetos das subclasses
carro1 = Carro("Toyota", "Corolla", 2022, 4)
moto1 = Moto("Honda", "Cb=B 500", 2021, 500)

print("Dados do Carro:")
carro1.exibir_dados()
carro1.ligar()

print("\n Dados da Moto: ")
moto1.exibir_dados()
moto1.ligar()