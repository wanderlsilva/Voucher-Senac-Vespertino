def contar_caracter(s):
    contador = {}
    for char in s:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador

print(contar_caracter("abacaxi"))