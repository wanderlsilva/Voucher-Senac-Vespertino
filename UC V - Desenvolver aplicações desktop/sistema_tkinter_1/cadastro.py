import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk #Exibir imagem no tkinter
import os
from login import *
import bcrypt


#Arquivos onde os usuarios serão salvos
ARQUIVOS_USUARIOS = "sistema_tkinter_1/bd/usuarios.txt"

def salvar_usuario(usuario, cpf, telefone, senha):
    hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
    with open(ARQUIVOS_USUARIOS, "a") as f:
        f.write(f"{usuario},{cpf},{telefone},{hash_senha}\n")

def verificar_usuario(cpf, senha):
    if not os.path.exists(ARQUIVOS_USUARIOS):
        return False
    with open(ARQUIVOS_USUARIOS, 'r') as f:
        for line in f:
            print(line)
            user,x ,y,  hash_pwd = line.strip().split(",")
            if x == cpf and bcrypt.checkpw(senha.encode(), hash_pwd.encode()):
                return True
    return False

class CadastroApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cadastro de Usuário")
        self.geometry("600x400")
        self.configure(bg="#FFFFFF")

        frame = tk.Frame(self, bg="black", padx=20, pady=20, relief="raised", borderwidth=2)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        try:
            imagem = Image.open("sistema_tkinter_1/img/cadastrar.png")
            imagem = imagem.resize((85, 85), Image.Resampling.LANCZOS)
            self.imagem_tk = ImageTk.PhotoImage(imagem)
            self.image_label = tk.Label(self, image=self.imagem_tk, bg="white")
            self.image_label.pack()
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        tk.Label(frame, text="Novo Usuário: ", bg="black", fg="white").pack()
        self.usuario_entry = tk.Entry(frame)
        self.usuario_entry.pack()

        tk.Label(frame, text="CPF: ", bg="black", fg="white").pack()
        self.cpf_entry = tk.Entry(frame)
        self.cpf_entry.pack()

        tk.Label(frame, text="Telefone: ", bg="black", fg="white").pack()
        self.telefone_entry = tk.Entry(frame)
        self.telefone_entry.pack()

        tk.Label(frame, text="Nova Senha: ", bg="black", fg="white").pack()
        self.senha_entry = tk.Entry(frame, show="*")
        self.senha_entry.pack()

        self.registrar_botao = tk.Button(frame, text="Cadastrar", bg="#4CAF50", fg="white", command=self.cadastrar)
        self.registrar_botao.pack()

        self.voltar_botao = tk.Button(frame, text="Voltar", bg="#FF0000", fg="white",  command=self.voltar)
        self.voltar_botao.pack()
    
    def cadastrar(self):
        usuario = self.usuario_entry.get()
        cpf = self.cpf_entry.get()
        telefone = self.telefone_entry.get()
        senha = self.senha_entry.get()

        if usuario and cpf and telefone and senha:
            salvar_usuario(usuario, cpf, telefone, senha)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def voltar(self):
        self.destroy() #Fecha a janela de cadastro
        self.master.deiconify() #Mostra a tela de login
