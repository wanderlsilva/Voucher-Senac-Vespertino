def soma_digitos(n):
    return sum((int(digito) for digito in str(n)))

print(soma_digitos(12345))