import random
def adivinha():
    print('*****************')
    print('Bem vindo ao jogo de Adivinhar o Numero')
    print('*****************')
    
    numero = random.randrange(0,100)
    total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute = int(input('Digite um numero: '))
        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero

        if acertou:
            print('Você acertou!!!')
            break
        elif maior:
            print('Você errou!!!, O seu chute foi maior que o numero.')
        elif menor:
            print('Você errou!!!, O seu chute foi menor que o numero.')

    print('Fim de Jogo!!!, o numero era {}'.format(numero))