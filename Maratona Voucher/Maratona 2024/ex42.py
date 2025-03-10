def string_longa(lista):
    return max(lista, key=len)

print(string_longa(["casa", "carro", "avião"]))