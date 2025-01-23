# Crie um programa que solicite ao usuário uma lista de números inteiros (separados por espaços), 
# converta essa lista em uma tupla, e depois calcule e exiba a soma e o produto de todos os elementos da tupla.

from functools import reduce

# Solicitar uma lista de números do usuário
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converter a entrada em uma tupla de inteiros
numeros = tuple(map(int, entrada.split()))

# Calcular a soma e o produto dos elementos da tupla
soma = sum(numeros)
produto = reduce(lambda x, y: x * y, numeros)

# Exibir os resultados
print(f"Tupla: {numeros}")
print(f"Soma dos elementos: {soma}")
print(f"Produto dos elementos: {produto}")
