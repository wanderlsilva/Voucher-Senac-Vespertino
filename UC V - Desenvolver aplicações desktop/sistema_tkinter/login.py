import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk #Exibir imagem no tkinter
from cadastro import *
from dashboard import *
from esqueci import *

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela de Login")
        self.geometry("600x400")
        self.configure(bg="#FFFFFF")

        frame = tk.Frame(self, bg="black", padx=20, pady=20, relief="raised", borderwidth=2)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        try:
            imagem = Image.open("sistema_tkinter/img/login.gif")
            imagem = imagem.resize((85, 85), Image.Resampling.LANCZOS)
            self.imagem_tk = ImageTk.PhotoImage(imagem)
            self.image_label = tk.Label(self, image=self.imagem_tk, bg="white")
            self.image_label.pack()
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        tk.Label(frame, text="Usuário: ", bg="black", fg="white").pack()
        self.usuario_entry = tk.Entry(frame)
        self.usuario_entry.pack()

        tk.Label(frame, text="Senha: ", bg="black", fg="white").pack()
        self.senha_entry = tk.Entry(frame, show="*")
        self.senha_entry.pack()

        self.show_senha = False
        self.toggle_botao = tk.Button(frame, text="👀", command=self.toggle_senha)
        self.toggle_botao.pack()

        self.login_botao = tk.Button(frame, text="Login", bg="#4CAF50", fg="white", command=self.login)
        self.login_botao.pack(pady=10)

        self.esqueci_senha_botao = tk.Button(frame, text="Esqueci a senha", fg="red", bg="white", command=self.abrir_esqueci_senha)
        self.esqueci_senha_botao.pack(pady=5)

        self.registrar_botao = tk.Button(frame, text="Cadastrar", bg="#008CBA", fg="white", command=self.abrir_tela_cadastro)
        self.registrar_botao.pack()

    def login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if verificar_usuario(usuario, senha):
            messagebox.showinfo("Login", 'Login Realizado com Sucesso!')
            self.destroy()  # Fecha a janela de login
            DashboardApp()  # Abre a dashboard
        else:
            messagebox.showerror("Erro", "Usuário ou Senha Incorreta!")

    def abrir_tela_cadastro(self):
        self.withdraw() #Esconder a tela de login
        CadastroApp(self) # Abre a tela de Cadastro

    def toggle_senha(self):
        if self.show_senha:
            self.senha_entry.config(show="*")
        else:
            self.senha_entry.config(show="")
        self.show_senha = not self.show_senha
    
    def abrir_esqueci_senha(self):
    #Abre a tela de recuperação de senha
        self.withdraw() #Esconder a tela de login
        EsqueciSenhaApp(self) # Abre a tela de esqueci senha
