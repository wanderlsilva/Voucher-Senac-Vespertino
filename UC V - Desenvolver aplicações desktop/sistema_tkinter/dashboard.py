import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #Configuração da Janela
        self.title("Dashboard")
        self.geometry("800x500")
        self.configure(bg="#f4f4f4")
        self.iconbitmap("sistema_tkinter/img/icon.ico")

        #Criando Frames
        self.sidebar = tk.Frame(self, bg="#333", width=200, height=500)
        self.sidebar.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self, bg="white", width=600, height=500)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.logo = tk.Label(self.sidebar, text="DASHBOARD", bg="#333", fg="white", font=("Arial", 14, "bold"))
        self.logo.pack(pady=20)

        self.img_dashboard = ImageTk.PhotoImage(Image.open("sistema_tkinter/img/dashboard.png").resize((32,32)))
        self.img_relatorio = ImageTk.PhotoImage(Image.open("sistema_tkinter/img/relatorio.png").resize((32,32)))
        self.img_configuracao = ImageTk.PhotoImage(Image.open("sistema_tkinter/img/configuracao.png").resize((32,32)))

        self.create_sidebar_botao("Dashboard", self.img_dashboard, self.mostrar_dashboard)
        #self.create_sidebar_botao("Relatório", self.img_relatorio, self.mostrar_relatorios)
        #self.create_sidebar_botao("Configuração", self.img_configuracao, self.mostrar_configuracoes)

        self.mostrar_dashboard()

    def mostrar_dashboard(self):
        #self.limpar_tela()

        titulo = tk.Label(self.content_frame, text="Dashboard", font=("Georgia", 16, "Bold"), bg="white")
        titulo.pack(pady=20)

        card_frame = tk.Frame(self.content_frame, bg="white")
        card_frame.pack()

        self.criar_card(card_frame, "Usuários", "1500", "#3498db")
        self.criar_card(card_frame, "Vendas", "R$ 12.200", "#2ecc71")
        self.criar_card(card_frame, "Relatórios", "25 gerados", "#e67e22")

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()