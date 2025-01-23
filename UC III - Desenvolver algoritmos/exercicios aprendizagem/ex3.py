#Escreva um programa que solicite ao usuário um número inteiro positivo N e calcule a soma de todos os números pares de 
#1 até N.

# Solicitar ao usuário um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializar a soma
soma_pares = 0

# Iterar de 1 até N
for i in range(1, n + 1):
    if i % 2 == 0:  # Verificar se o número é par
        soma_pares += i

# Exibir o resultado
print(f"A soma de todos os números pares de 1 até {n} é: {soma_pares}")
