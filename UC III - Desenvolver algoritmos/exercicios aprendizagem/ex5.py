# Escreva um programa que receba uma palavra do usuário e verifique se ela é um palíndromo. 
# Uma palavra é considerada um palíndromo se for lida da mesma forma de trás para frente (ignorando maiúsculas e minúsculas).

# Solicitar uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Transformar a palavra para minúsculas e verificar se é um palíndromo
if palavra.lower() == palavra.lower()[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
