# 1 - Considere a string A = "Um elefante incomoda muita gente" gente". 
# Que fatia corresponde a "elefante incomoda
a = "Um elefante incomoda muita gente"
print(a[3:20])

# 2 - Escreva um programa que solicite uma frase ao usuário e escreva a 
# frase toda em mai úscula e sem espaços em branco.
frase = input("Digite uma frase: ")
frase_sem_espaco = frase.replace(' ','')
frase_maiuscula = frase_sem_espaco.upper()
print(frase_maiuscula)