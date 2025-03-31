import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import PhotoImage


class DashboardAgenda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sis Agenda")
        self.geometry("800x500")
        self.configure(bg="#696969")

        self.sidebar = tk.Frame(self, bg="#F8F8FF", width=200, height=500)
        self.sidebar.pack(side="right", fill="y")

        self.content_frame = tk.Frame(self, bg="white", width=600, height=500) #Cria o frame da área principal
        self.content_frame.pack(side="right", fill="both", expand=True) # Posiciona o frame à direita, ocupando o espaço disponivel

        self.logo = tk.Label(self.sidebar, text="Agenda", bg="#F8F8FF", fg="black", font=("Bodoni", 16, "bold"))
        self.logo.pack(padx=40, pady=40)

        self.img_dashboard = ImageTk.PhotoImage(Image.open("sis_agenda/img/dashboard_agenda.png").resize((32,32)))
        self.create_sidebar_botao("Dashboard", self.img_dashboard, self.mostrar_dashboard)

        self.mostrar_dashboard()

    def create_sidebar_botao(self, text, image, command):
        #Cria um botão estilizado no menu lateral
        btn = tk.Button(
            self.sidebar, text=f" {text}", image=image, compound="left", #Define o texto e coloca a imagem à esquerda
            bg="#555", fg="white", font=("Arial", 12), anchor="w", #Define a cor do fundo, fonte e alinhamento à esquerda
            command=command, bd=0, padx=10 # Define a ação do botão e remove da borda
        )
        btn.pack(fill="x", pady=5) #Faz o botão ocupar toda a largura do menu  e adiciona o espaçamento vertical

    def mostrar_dashboard(self):
        #Exibe o widgets do Dashboard
#        self.limpar_tela() #Limpa o conteudo atual da tela

        #Titulo da seção Dashboard
        titulo = tk.Label(self.content_frame, text="Dashboard", font=("Georgia", 16, "bold"), bg="white")
        titulo.pack(pady=20) # Adiciona um espaçamento vertical

        #Criando um frame para armazenar os cards informativos
        card_frame = tk.Frame(self.content_frame, bg="white")
        card_frame.pack()

        tk.Label(self.content_frame, text="Usuário: ", bg="black", fg="white").pack()
     

if __name__ == "__main__":
    app = DashboardAgenda()
    app.mainloop()