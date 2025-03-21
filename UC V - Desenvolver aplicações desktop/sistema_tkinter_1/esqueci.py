import tkinter as tk
from tkinter import messagebox
import bcrypt
import random
import os

#Arquivos onde os usuarios serão salvos
ARQUIVOS_USUARIOS = "sistema_tkinter_1/bd/usuarios.txt"

class EsqueciSenhaApp(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Esqueci a Senha")
        self.geometry("400x250")
        self.configure(bg="white")

        self.codigo_gerado = None
        self.usuario_atual = None

        tk.Label(self, text="Digite seu usuário:", bg="white").pack(pady=5)
        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack(pady=5)

        self.verificar_botao = tk.Button(self, text="Recuperar Senha", command=self.verificar_usuario)
        self.verificar_botao.pack(pady=10)

    def verificar_usuario(self):
        #Verifica se o usuário existe e gera um código de recuperação
        usuario = self.usuario_entry.get()

        if not os.path.exists(ARQUIVOS_USUARIOS):
            messagebox.showerror("Erro", "Nenhum usuário cadastrado.")
            return

        with open(ARQUIVOS_USUARIOS, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")  # [0] = usuário, [1] = senha_hash
                if usuario == dados[0]:  
                    self.usuario_atual = usuario
                    self.codigo_gerado = str(random.randint(1000, 9999))  # Código de 4 dígitos
                    messagebox.showinfo("Código Enviado", f"Seu código de recuperação é: {self.codigo_gerado}")
                    self.tela_nova_senha()
                    return
        
        messagebox.showerror("Erro", "Usuário não encontrado.")

    def tela_nova_senha(self):
        #Exibe a tela para digitar o código e cadastrar nova senha
        for widget in self.winfo_children():
            widget.destroy()  # Remove todos os widgets da tela anterior

        tk.Label(self, text="Digite o código enviado:", bg="white").pack(pady=5)
        self.codigo_entry = tk.Entry(self)
        self.codigo_entry.pack(pady=5)

        tk.Label(self, text="Nova senha:", bg="white").pack(pady=5)
        self.nova_senha_entry = tk.Entry(self, show="*")
        self.nova_senha_entry.pack(pady=5)

        self.confirmar_botao = tk.Button(self, text="Confirmar", command=self.atualizar_senha)
        self.confirmar_botao.pack(pady=10)

    def atualizar_senha(self):
       #Verifica o código e atualiza a senha no banco de dados
        codigo_digitado = self.codigo_entry.get()
        nova_senha = self.nova_senha_entry.get()

        if codigo_digitado != self.codigo_gerado:
            messagebox.showerror("Erro", "Código incorreto!")
            return

        if len(nova_senha) < 4:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 4 caracteres.")
            return

        # Criptografando a nova senha com bcrypt
        nova_senha_hash = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt()).decode()

        # Atualiza o arquivo de usuários
        linhas = []
        with open(ARQUIVOS_USUARIOS, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == self.usuario_atual:
                    dados[1] = nova_senha_hash  # Atualiza a senha hash
                linhas.append(",".join(dados))

        with open(ARQUIVOS_USUARIOS, "w") as arquivo:
            for linha in linhas:
                arquivo.write(linha + "\n")

        messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
        self.destroy()  # Fecha a janela

