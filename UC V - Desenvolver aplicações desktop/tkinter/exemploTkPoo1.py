from tkinter import *
#class Janela:
#    def __init__(self, instancia_de_Tk):
#        pass
#raiz = Tk()
#Janela(raiz)
#raiz.mainloop()

#======= OUUUUUU =========
class Janela(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="Olá")
        self.msg.pack()
        self.fechar = Button(self,text="Fechar", command=self.quit)
        self.fechar.pack()
        self.pack()

app = Janela()
mainloop()
