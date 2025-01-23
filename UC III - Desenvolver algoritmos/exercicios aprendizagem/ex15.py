#O seguinte algoritmo foi escrito para encontrar o maior número em uma lista fornecida pelo usuário.
# No entanto, ele contém um erro que faz com que não funcione corretamente em todos os casos. 
# Analise o código, identifique o erro, explique o que está errado e corrija o algoritmo.

def encontrar_maior(lista):
    if not lista:
        return "A lista está vazia."
    #maior = 0 # Inicializa o maior como 0. Esse era o erro

    maior = lista[0]  # Inicializa o maior como 0
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

# Solicitar os números do usuário
entrada = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(int, entrada.split()))

# Chamar a função e exibir o resultado
maior_numero = encontrar_maior(numeros)
print(f"O maior número da lista é: {maior_numero}")
