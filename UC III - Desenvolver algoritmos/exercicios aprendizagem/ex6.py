# Crie uma função chamada calcular_fatorial que receba um número inteiro positivo como parâmetro e 
# retorne o fatorial desse número. Utilize essa função em um programa que solicite um número do usuário 
# e exiba o fatorial calculado.

# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

# Programa principal
num = int(input("Digite um número inteiro positivo: "))
if num < 0:
    print("O número deve ser positivo!")
else:
    print(f"O fatorial de {num} é: {calcular_fatorial(num)}")
