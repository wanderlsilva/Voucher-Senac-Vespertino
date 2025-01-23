#1 - Faça um programa que leia 2 notas de um aluno , calcule a média e imprima
# aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6)
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2)/2
print('Media = ', media)
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')
    
#2 - Refaça o exercício 1, identificando o conceito aprovado (média superior a 6),
# exame (média entre 4 e 6) ou reprovado (média inferior a 4)
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2)/2
print('Media = ', media)
if media >= 6:
    print('Aprovado')
elif media >= 4 and media < 6:
    print('Exame')
else:
    print('Reprovado')