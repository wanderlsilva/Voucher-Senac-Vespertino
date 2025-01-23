import random
def forca():
    print('*****************')
    print('Bem vindo ao jogo da forca')
    print('*****************')

    arquivo = open('jogos/palavras.txt', 'r')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input('Qual letra ?')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
        else:
            erros += 1

        acertou = '_' not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)

    if(acertou):
        print('Ganhou!!!')
    else:
        print('Perdeu!!!')


    print('Fim de jogo!!!')