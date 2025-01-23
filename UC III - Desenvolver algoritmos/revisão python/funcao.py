# 1 - Crie uma função para desenhar uma linha, usando o caractere ''__''. 
# O tamanho da linha deve ser definido na chamada da função.
def linha(n):
    for i in range(n):
        print(end='_')
    print(' ')

#linha(10)
# 2 - Crie uma função que receba como parâmetro uma lista com valores de
# qualquer tipo . A função deve imprimir todos os elementos da lista numerando-os
def imprime_lista(a):
    contador = 0
    for valor in range(a):
        contador = contador + 1
        print(contador, ' ) ', valor)

#imprime_lista(25)
# 3 - Crie uma função que receba como parâmetro uma lista com valores numéricos 
# e retorne a média desses valores.
def media_lista(x):
    somador = 0
    for valor in range(x):
        somador = somador + valor
    return somador/len(x)