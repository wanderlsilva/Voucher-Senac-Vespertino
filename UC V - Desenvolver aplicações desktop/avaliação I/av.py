#Resolva a seguinte atividade avaliativa em python:
#O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada semestre. Os pontos são atribuídos da seguinte forma:
#•Se um cliente comprar 0 livros, ele ganhará 0 pontos.
#•Se um cliente comprar 1 livro, ele ganhará 5 pontos.
#•Se um cliente comprar 2 livros, ele ganhará 15 pontos.
#•Se um cliente comprar 3 livros, ele ganhará 30 pontos.
#•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
#Lista de brindes:
#De 20 à 30 pontos o cliente poderá escolher entre: Uma EcoBag OU Caneta personalizada
#De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira.
#Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank
#Obs: Os pontos são acumulativos, e contado a cada compra realizada pelo cliente. Ex: Se o cliente na semana 1 comprar 2 livros de uma única vez ele receberá 15 pontos, se na semana 2 ele comprar 1 único livro receberá 5 pontos totalizando 20 pontos em duas semamas.
#Crie um programa que leia o número de livros comprado por um usuário e exiba o número de pontos correspondentes e qual brinde ele poderá escolher.

def calcular_pontos(livros_comprados):
    if livros_comprados == 0:
        return 0
    elif livros_comprados == 1:
        return 5
    elif livros_comprados == 2:
        return 15
    elif livros_comprados == 3:
        return 30
    else:
        return 60

def verificar_brinde(pontos):
    if 20 <= pontos <= 30:
        return "EcoBag OU Caneta personalizada"
    elif 35 <= pontos <= 60:
        return "Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira"
    elif pontos > 65:
        return "2 livros (com valor máximo de R$100,00) OU Powerbank"
    else:
        return "Nenhum brinde disponível"

def main():
    pontos_acumulados = 0
    while True:
        try:
            livros = int(input("Quantos livros você comprou nesta compra? (Digite -1 para sair): "))
            if livros == -1:
                break
            if livros < 0:
                print("Número inválido. Digite um valor positivo.")
                continue
            
            pontos_ganhos = calcular_pontos(livros)
            pontos_acumulados += pontos_ganhos
            
            print(f"Você ganhou {pontos_ganhos} pontos nesta compra. Total de pontos acumulados: {pontos_acumulados}")
            print(f"Brinde disponível: {verificar_brinde(pontos_acumulados)}")
        
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    main()
