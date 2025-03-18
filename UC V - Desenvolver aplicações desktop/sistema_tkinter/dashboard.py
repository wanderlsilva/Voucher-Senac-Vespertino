import tkinter as tk # Importa a biblioteca Tkinter para criar I1nterface Gráfica
from tkinter import ttk #Importa o ttk para widgets mais modernos
from PIL import Image, ImageTk #Importa o Pillow para trabalhar com imagens nos botões

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__() # Inicializa a classe Tk
        #Configuração da Janela
        self.title("Dashboard") #Define o titulo da janela
        self.geometry("800x500") #Define o tamanho da janela
        self.configure(bg="#f4f4f4") #Define a cor de fundo da janela
        self.iconbitmap("sistema_tkinter/img/icon.ico") #Define um icone para a janela

        # Criando um Frame para o Menu Lateral (Sidebar)
        self.sidebar = tk.Frame(self, bg="#333", width=200, height=500) #Cria o frame da sidebar
        self.sidebar.pack(side="left", fill="y") #Posiciona a sidebar à esquerda e a estende verticalmente

        #Criando um Frame para o conteudo principal
        self.content_frame = tk.Frame(self, bg="white", width=600, height=500) #Cria o frame da área principal
        self.content_frame.pack(side="right", fill="both", expand=True) # Posiciona o frame à direita, ocupando o espaço disponivel

        #Criando o título do menu lateral
        self.logo = tk.Label(self.sidebar, text="DASHBOARD", bg="#333", fg="white", font=("Arial", 14, "bold"))
        self.logo.pack(pady=20)

        #Carregando imagens para os botoes do menu
        self.img_dashboard = ImageTk.PhotoImage(Image.open("sistema_tkinter/img/dashboard.png").resize((32,32)))
        self.img_relatorio = ImageTk.PhotoImage(Image.open("sistema_tkinter/img/relatorio.png").resize((32,32)))
        self.img_configuracao = ImageTk.PhotoImage(Image.open("sistema_tkinter/img/configuracao.png").resize((32,32)))

        #Criando Botoes do Menu Lateral com Icones
        self.create_sidebar_botao("Dashboard", self.img_dashboard, self.mostrar_dashboard)
        self.create_sidebar_botao("Relatório", self.img_relatorio, self.mostrar_relatorios)
        self.create_sidebar_botao("Configuração", self.img_configuracao, self.mostrar_configuracoes)

        self.mostrar_dashboard() #Exibe o dashboard inicial ao abrir o programa

    def create_sidebar_botao(self, text, image, command):
        #Cria um botão estilizado no menu lateral
        btn = tk.Button(
            self.sidebar, text=f" {text}", image=image, compound="left", #Define o texto e coloca a imagem à esquerda
            bg="#555", fg="white", font=("Arial", 12), anchor="w", #Define a cor do fundo, fonte e alinhamento à esquerda
            command=command, bd=0, padx=10 # Define a ação do botão e remove da borda
        )
        btn.pack(fill="x", pady=5) #Faz o botão ocupar toda a largura do menu  e adiciona o espaçamento vertical

    def limpar_tela(self):
        #Remove todos os widgets da area de conteudo antes de exibir outra tela
        for widget in self.content_frame.winfo_children():
            widget.destroy() # Remove cada widget dentro do frame de conteudo

    def mostrar_dashboard(self):
        #Exibe o widgets do Dashboard
        self.limpar_tela() #Limpa o conteudo atual da tela

        #Titulo da seção Dashboard
        titulo = tk.Label(self.content_frame, text="Dashboard", font=("Georgia", 16, "bold"), bg="white")
        titulo.pack(pady=20) # Adiciona um espaçamento vertical

        #Criando um frame para armazenar os cards informativos
        card_frame = tk.Frame(self.content_frame, bg="white")
        card_frame.pack()

        #Criando os Cards com informações do sistema
        self.criar_card(card_frame, "Usuários", "1500", "#3498db") #Card de Usuarios
        self.criar_card(card_frame, "Vendas", "R$ 12.200", "#2ecc71") #Card de Vendas
        self.criar_card(card_frame, "Relatórios", "25 gerados", "#e67e22") #Card de Relatórios
    
    def criar_card(self, parent, titulo, valor, cor):
        #Cria um card de informação colorido
        card = tk.Frame(parent, bg=cor, width=150, height=100, padx=10, pady=10) #Define o tamanho e a cor do card
        card.pack(side="left", padx=10, pady=10) #Posiciona os cards lado a lado com espaçamento

        #Adiciona o titulo e o valor dentro do card
        tk.Label(card, text=titulo, font=("Arial", 12, "bold"), bg=cor, fg="white").pack()
        tk.Label(card, text=valor, font=("Arial", 16), bg=cor, fg="white").pack()
    
    def mostrar_relatorios(self):
        #Exibe a area de Relatorios
        self.limpar_tela() #Limpa o conteudo da tela antes de exibir os relatorios
        titulo = tk.Label(self.content_frame, text="Relatórios", font=("Arial", 16, "bold"), bg="white")
        titulo.pack(pady=20) #Adiciona um espaçamento vertical

    def mostrar_configuracoes(self):
        #Exibe a area de Configurações
        self.limpar_tela() #Limpa o conteudo da tela antes de exibir os relatorios
        titulo = tk.Label(self.content_frame, text="Configurações", font=("Arial", 16, "bold"), bg="white")
        titulo.pack(pady=20) #Adiciona um espaçamento vertical

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()