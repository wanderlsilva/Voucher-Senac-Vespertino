class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def emitir_som(self):
        print("O animal emitiu um som.")

    def exibir_dados(self):
        print(f"Nome: {self._nome}, idade: {self._idade} anos")

class Dog(Animal):
    def emitir_som(self):
        print(f"O dog {self._nome} latiu: Ruf, Ruf")

class Cat(Animal):
    def emitir_som(self):
        print(f"O cat {self._nome} miou: Meow, Meow")

dog1 = Dog("Rex", 3)
cat1 = Cat("Frajola", 2)

dog1.exibir_dados()
dog1.emitir_som()
print()
cat1.exibir_dados()
cat1.emitir_som()