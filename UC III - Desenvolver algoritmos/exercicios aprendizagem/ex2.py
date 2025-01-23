#Escreva um programa que receba três números que representam os lados de um triângulo e 
# determine se eles podem formar um triângulo e, em caso afirmativo, 
# classifique-o como equilátero, isósceles ou escaleno.

# Recebendo os três lados do triângulo do usuário
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

# Verificando se os lados podem formar um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Determinando o tipo de triângulo
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"Os lados formam um triângulo {tipo}.")
else:
    print("Os lados fornecidos não podem formar um triângulo.")
