def comparar_lista(lista1, lista2):
    return list(set(lista1) & set(lista2))

print(comparar_lista([1,2,3,4], [3,4,5,6]))