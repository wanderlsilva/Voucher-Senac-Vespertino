def inverte(s):
    palavras = s.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return ' '.join(palavras_invertidas)

print(inverte("Olá Mundo"))