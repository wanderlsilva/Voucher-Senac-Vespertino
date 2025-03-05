def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    return lista_unica[1]

print(segundo_maior([10,20,4,45,99,99]))
