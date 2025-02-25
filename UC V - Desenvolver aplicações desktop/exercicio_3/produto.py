# Sistema de Produtos

#Crie uma classe Produto com os atributos:
#nome
#preco
#estoque

#E os métodos:
#adicionar_estoque(quantidade) → aumenta o estoque.
#vender(quantidade) → reduz o estoque se houver unidades suficientes.
#exibir_produto() → exibe as informações do produto.

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
        else:
            print("Estoque insuficiente!!!")

    def exibir_produto(self):
        print(f"Produto: {self.nome}, Preco: R$ {self.preco:.2f}, Estoque: {self.estoque}")

produto1 = Produto("Notebook", 3500, 10)
produto1.vender(2)
produto1.adicionar_estoque(5)
produto1.exibir_produto()