import tkinter as tk
from tkinter import messagebox
import os

#Arquivos onde os usuarios serão salvos
ARQUIVOS_USUARIOS = "usuarios.txt"

def salvar_usuario(usuario, senha):
    with open(ARQUIVOS_USUARIOS, "a") as f:
        f.write(f"{usuario}, {senha}\n")

def verificar_usuario(usuario, senha):
    if not os.path.exists(ARQUIVOS_USUARIOS):
        return False
    with open(ARQUIVOS_USUARIOS, 'r') as f:
        for line in f:
            usuario, senha = line.strip().split(",")
            if usuario == usuario and senha == senha:
                return True
    return False

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela de Login")
        self.geometry("300x200")

        tk.Label(self, text="Usuário: ").pack()
        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        tk.Label(self, text="Senha: ").pack()
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack()

        self.login_botao = tk.Button(self, text="Login")
        self.login_botao.pack()

        self.registrar_botao = tk.Button(self, text="Cadastrar", command=self.abrir_tela_cadastro)
        self.registrar_botao.pack()
    
    def abrir_tela_cadastro(self):
        self.withdraw() #Esconder a tela de login
        CadastroApp(self)

class CadastroApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cadastro de Usuário")
        self.geometry("300x200")

        tk.Label(self, text="Novo Usuário: ").pack()
        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        tk.Label(self, text="Nova Senha: ").pack()
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack()

        self.registrar_botao = tk.Button(self, text="Cadastrar")
        self.registrar_botao.pack()

        self.voltar_botao = tk.Button(self, text="Voltar", command=self.voltar)
        self.voltar_botao.pack()

    def voltar(self):
        self.destroy() #Fecha a janela de cadastro
        self.master.deiconify() #Mostra a tela de login

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
