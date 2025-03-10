def soma_indices(lista):
    return sum(lista[i] for i in range(0, len(lista), 2))

print(soma_indices([1,2,3,4,5,6]))