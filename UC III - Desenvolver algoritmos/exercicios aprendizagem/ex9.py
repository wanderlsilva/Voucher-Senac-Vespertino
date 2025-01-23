# Crie um programa que receba uma lista de números reais do usuário (separados por espaços), 
# calcule a média desses números e exiba os números que estão acima da média.

# Solicitar uma lista de números reais do usuário
entrada = input("Digite uma lista de números reais separados por espaço: ")

# Converter a entrada em uma lista de floats
numeros = list(map(float, entrada.split()))

# Calcular a média
media = sum(numeros) / len(numeros)

# Encontrar os números acima da média
acima_da_media = [num for num in numeros if num > media]

# Exibir a média e os números acima dela
print(f"A média dos números é: {media:.2f}")
print("Números acima da média:", acima_da_media)
