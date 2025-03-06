from tkinter import * #Importando o pacote TKINTER
from tkinter.ttk import * 

#def aoClicar():
#    mensagem["text"] = "Texto: " + entrada.get()

def exibeValor():
    mensagem["text"] = "Valor: " +combo.get()

janela = Tk() #instaciamos a classe tk

#janela.geometry('800x600') #Modificar tamanho da janela
janela.geometry('800x600+100+50') #Modificar tamanho da janela MargemEsquerda + MargemTopo
#janela.attributes('-fullscreen', True) #Tela Cheia

janela.title("Nossa primeira janela") #Definindo o titulo da janela

#Criando ComboBox
combo = Combobox(janela)
combo['values'] = (1, 2, 3, 4, 5, "Olá")
combo.current(0) #Definindo o valor a ser exibido
combo.pack()

#Criando Botão e Modificando cor de fundo e da fonte
botao = Button(janela, text="Clique Aqui", command=exibeValor)
botao.pack() #Adicionamos o widget a janela

#Entrada de informações
#entrada = Entry(janela, font="arial 15 bold", state="disabled")
#entrada.pack()

#Font => Nome da Fonte, Tamanho da Fonte, Efeito da Fonte
mensagem = Label(janela, text="Olá Mundo", font="impact 20 bold") #Widget e texto que guarda a label

#Alterando o Texto
#texto["text"] = "Este texto sera exibido"
mensagem.pack() #Adicionamos o widget a janela

#entrada.focus() #Focar o cursor
janela.mainloop() #Permanece aberta enquanto o mainloop estiver ativo.