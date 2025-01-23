#1 -Dada a lista L = [5, 7, 2, 9, 4, 1, 3] escreva um programa que 
# imprima as seguintes informações:
l = [5, 7, 2, 9, 4, 1, 3]
#a) tamanho da lista.
print('O tamanho da lista é: ', len(l))
#b) maior valor da lista.
print('O maior elemento da lista é: ', max(l))
#c) menor valor da lista.
print('O menor elemento da lista é: ', min(l))
#d) soma de todos os elementos da lista.
print('A soma dos elemento da lista é: ', sum(l))
#e) lista em ordem crescente
l.sort()
print('Lista em ordem crescente: ', l)
#f) lista em ordem decrescente.
l.reverse()
print('Lista em ordem decrescente: ', l)

#2 -  Gere uma lista contendo os múltiplos de 3 entre 1 e 50
l = list(range(3, 50, 3))
print(l)