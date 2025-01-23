#Escreva um programa que receba três números inteiros do usuário e imprima o maior deles.

# Recebendo os três números do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Verificando qual é o maior número usando estruturas condicionais
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Imprimindo o maior número encontrado
print(f"O maior número digitado é: {maior}")
