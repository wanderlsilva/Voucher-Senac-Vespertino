# Crie uma função chamada eh_primo que receba um número inteiro como parâmetro e retorne True se o número 
# for primo e False caso contrário. Use essa função em um programa que solicite um número do usuário e informe 
# se ele é primo.

# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Programa principal
num = int(input("Digite um número inteiro: "))
if eh_primo(num):
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
