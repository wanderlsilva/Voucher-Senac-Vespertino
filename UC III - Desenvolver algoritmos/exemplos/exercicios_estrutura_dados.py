lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

#a) imprima o maior elemento
maiorValor = lista[0]
for index in range(0, len(lista)):
    if(maiorValor < lista[index]):
        maiorValor = lista[index]
print(maiorValor)

#b) imprima o menor elemento
menorValor = lista[0]
for index in range(0, len(lista)):
    if(menorValor > lista[index]):
        menorValor = lista[index]
print(menorValor)

#c) imprima os números pares
listaPares = []
for index in range(0, len(lista)):
    if( lista[index] % 2 == 0):
        listaPares.append(lista[index])
    print(listaPares)

#d) imprima o número de ocorrências do primeiro elemento da lista
ocorrenciasItem1 = 0
for index in range(0, len(lista)):
    if(lista[index] == lista[0]):
        ocorrenciasItem1 = ocorrenciasItem1 + 1
print(ocorrenciasItem1)

#e) imprima a média dos elementos
mediaElementos = 0
for index in range(0, len(lista)):
    mediaElementos =+ mediaElementos + lista[index]
mediaElementos = mediaElementos / len(lista)
print(mediaElementos)

#f) imprima a soma dos elementos de valor negativo
somaNegativos = 0
for index in range(0, len(lista)):
    if(lista[index] < 0):
        somaNegativos = somaNegativos + lista[index]
print(somaNegativos)