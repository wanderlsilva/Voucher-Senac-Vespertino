# Escreva um programa que receba uma lista de números inteiros do usuário (separados por espaços), 
# remova os números duplicados, ordene a lista em ordem crescente e exiba o resultado.

# Solicitar uma lista de números do usuário
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converter a entrada em uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Remover duplicatas e ordenar a lista
numeros_unicos = sorted(list(set(numeros)))

# Exibir a lista final
print("Lista sem duplicatas e ordenada:", numeros_unicos)
