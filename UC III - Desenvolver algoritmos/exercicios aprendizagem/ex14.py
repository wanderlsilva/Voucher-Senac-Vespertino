# Crie um programa que gere e exiba uma matriz identidade de ordem N, onde N é fornecido pelo usuário. 
# A matriz identidade possui 1 na diagonal principal e 0 nos demais elementos.

# Solicitar o tamanho da matriz identidade
n = int(input("Digite a ordem da matriz identidade (N): "))

# Criar a matriz identidade
matriz_identidade = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz_identidade.append(linha)

# Exibir a matriz identidade
print("\nMatriz Identidade:")
for linha in matriz_identidade:
    print(linha)
