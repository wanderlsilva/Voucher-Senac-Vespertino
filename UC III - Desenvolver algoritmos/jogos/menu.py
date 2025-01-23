import forca
import adivinha_numero

print('------------------------------------')
print('********* MENU DE JOGOS ************')
print('------------------------------------')
print('1 - Adivinhar o Numero')
print('2 - Forca')
print('0 - Sair')
escolha = int(input('Qual jogo quer jogar? Digite o número: '))

if escolha == 1:
    adivinha_numero.adivinha()
elif escolha == 2:
    forca.forca()
elif escolha == 0:
    print('Saindooooo.....')
else:
    print('Opção inválida!!!')