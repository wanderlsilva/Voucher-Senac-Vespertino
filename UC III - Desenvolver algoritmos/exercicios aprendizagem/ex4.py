# Um número é considerado perfeito se a soma de seus divisores (excluindo ele mesmo) for igual ao próprio número. Por exemplo,
#6 é perfeito porque 1 + 2 + 3 = 6
#Escreva um programa que solicite ao usuário um número inteiro positivo e determine se ele é perfeito.

# Solicitar ao usuário um número inteiro positivo
num = int(input("Digite um número inteiro positivo: "))

# Inicializar a soma dos divisores
soma_divisores = 0

# Encontrar os divisores do número
for i in range(1, num):  # Excluir o próprio número
    if num % i == 0:
        soma_divisores += i

# Verificar se o número é perfeito
if soma_divisores == num:
    print(f"{num} é um número perfeito!")
else:
    print(f"{num} não é um número perfeito.")
