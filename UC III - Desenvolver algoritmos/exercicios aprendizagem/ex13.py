# Escreva um programa que crie uma matriz 2x3 (2 linhas e 3 colunas) com valores fornecidos pelo usuário 
# e calcule a soma de todos os elementos da matriz.

# Criar uma matriz 2x3
matriz = []

# Solicitar os valores do usuário
print("Digite os valores para uma matriz 2x3:")
for i in range(2):  # 2 linhas
    linha = []
    for j in range(3):  # 3 colunas
        valor = int(input(f"Digite o valor para a posição ({i},{j}): "))
        linha.append(valor)
    matriz.append(linha)

# Calcular a soma dos elementos
soma = 0
for linha in matriz:
    soma += sum(linha)

# Exibir a matriz e a soma
print("\nMatriz:")
for linha in matriz:
    print(linha)
print(f"Soma de todos os elementos: {soma}")

