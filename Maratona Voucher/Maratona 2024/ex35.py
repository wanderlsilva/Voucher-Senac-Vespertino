def contar_vogais(s):
    vogais ='aeiou'
    return sum(1 for letra in s.lower() if letra in vogais)

print(contar_vogais("Programacao"))