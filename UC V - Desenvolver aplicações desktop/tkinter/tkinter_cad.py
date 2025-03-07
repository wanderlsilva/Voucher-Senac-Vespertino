import tkinter as tk
from tkinter import messagebox
import os

#Arquivos onde os usuarios serão salvos
ARQUIVOS_USUARIOS = "usuarios.txt"

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

        self.registrar_botao = tk.Button(self, text="Cadastrar")
        self.registrar_botao.pack()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
