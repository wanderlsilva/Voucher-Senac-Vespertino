# Crie um programa para gerenciar um pequeno cadastro de produtos. 
# Ele deve permitir que o usuário adicione produtos a um dicionário, onde a chave será o nome do produto 
# e o valor será o preço. Depois de adicionar os produtos, exiba todos os itens cadastrados e calcule o valor total.

# Criar um dicionário para armazenar os produtos
produtos = {}

# Loop para adicionar produtos ao dicionário
while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    preco = float(input(f"Digite o preço do produto '{nome}': "))
    produtos[nome] = preco

# Exibir os produtos cadastrados
print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

# Calcular e exibir o valor total
total = sum(produtos.values())
print(f"\nValor total dos produtos: R$ {total:.2f}")
