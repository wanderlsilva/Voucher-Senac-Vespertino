def velocidade(espaco, tempo):
    v = espaco/tempo
    return v
#    print('Velocidade: {} m/s'.format(v))

#velocidade(100,20)
resultado = velocidade(100,20)/20
#print(resultado)

def diz_oi():
    print("oiiiiii")

#diz_oi()

def dados(nome, idade=None):
#    print('nome: {}'.format(nome))
    if(idade is not None):
        print('nome: {} \nidade: {}'.format(nome, idade))
    else:
        print('nome: {} \nidade: não informada'.format(nome))

#dados('Wander')

def calculadora(x, y):
    return {'soma':x+y, 'subtração':x-y, 'multiplicação': x*y}

#print(calculadora(2,1))

def teste(arg, *args):
    print('primeiro argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))

#teste('python','é', 'muito', 'legal')

def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

minha_funcao(nome='python')