# Crie um programa que receba uma lista de números inteiros do usuário (separados por espaços), 
# converta a lista em uma tupla e retorne outra tupla contendo apenas os elementos que aparecem uma única vez.

# Solicitar uma lista de números do usuário
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converter a entrada em uma tupla de inteiros
numeros = tuple(map(int, entrada.split()))

# Encontrar os elementos que aparecem uma única vez
unicos = tuple(x for x in numeros if numeros.count(x) == 1)

# Exibir os resultados
print(f"Tupla original: {numeros}")
print(f"Elementos únicos na tupla: {unicos}")
