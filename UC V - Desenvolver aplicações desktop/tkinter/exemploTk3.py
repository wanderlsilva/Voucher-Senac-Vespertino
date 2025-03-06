from tkinter import *
from tkinter.ttk import *

def exibeValor():
    mensagem['text']="Opção Escolhida: " +str(escolha.get())

window = Tk()
window.geometry("300x200+200+100")
window.title("Radius Button")

mensagem = Label(window, text="Opção Escolhida: Nenhuma", font="arial 20 bold")
mensagem.pack()

escolha = StringVar()

escolha1 = Radiobutton(window, text='Primeiro', value='Primeiro', variable=escolha)
escolha2 = Radiobutton(window, text='Segundo', value='Segundo', variable=escolha)
escolha3 = Radiobutton(window, text='Terceiro', value='Terceiro', variable=escolha)
escolha4 = Radiobutton(window, text='Quarto', value='Quarto', variable=escolha)
escolha5 = Radiobutton(window, text='Quinto', value='Quinto', variable=escolha)

escolha1.pack()
escolha2.pack()
escolha3.pack()
escolha4.pack()
escolha5.pack()

botao = Button(window, text="Clique Aqui", command=exibeValor)
botao.pack()

window.mainloop()