# 1 – Dada a tabela a seguir, crie um dicionário que a represente:
#Lanchonete
#Produtos Preços R$
#Salgado  R$ 4.50
#Lanche   R$ 6.50
#Suco     R$ 3.00
#Refrigerante  R$ 3.50
#Doce     R$ 1.00
dic = {'Salgado':4.50, 'Lanche':6.50, 'Suco':3.00, 'Refrigerante':3.50, 'Doce':1.00}
print(dic)

#2 – Considere um dicionário com 5 nomes de alunos e suas notas. 
# Escreva um programa que calcule a média dessas notas.
sala = {'Ana':9.0, 'Beatriz':8.8, 'Carla':7.5, 'Daniela':7.0, 'Erica':6.5}
notas = sala.values()
media = sum(notas)/5
print('A média da sala é: ', media)