#1 - Escreva um programa para encontrar a soma S = 3 + 6 + 9 + ……. + 333
s = 0
for x in range(3, 334, 3):
    s = s + x
    print('Soma = ', s)

#2 - Escreva um programa que leia 10 notas e informe a média dos alunos.
s = 0
for contador in range(1, 11):
    nota = float(input('Digite a nota ' + str(contador) + ": "))
    s = s + nota
    print('Media = ', s/10)

#3 - Escreva um programa que leia um número de 1 a 10,
# e mostre a tabuada desse número.
numero = int(input('Digite o numero para a tabuada: '))
for sequencia in range (1,11):
    print("{} x {} = {}".format(sequencia, numero, (sequencia*numero)))