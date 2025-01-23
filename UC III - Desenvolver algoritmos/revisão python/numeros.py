#1 - Escreva um programa que receba 2 valores do tipo inteiro x e y, 
# e calcule o valor de z: z = (𝑥²+ 𝑦²)/(𝑥−𝑦)²
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = (x**2 + y ** 2) / (x - y)**2
print('Z =', z)

#2 - Escreva um programa que receba o salário de um uncionário (float), 
# e retorne o resultado do novo salário com reajuste de 35%.
salario = float(input('Digite o salário atual: '))
novo_salario = salario * 1.35
print('Novo salário = R$ {}'.format(novo_salario))