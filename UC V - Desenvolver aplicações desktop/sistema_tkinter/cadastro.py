import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk #Exibir imagem no tkinter
import os
from login import *

#Arquivos onde os usuarios serão salvos
ARQUIVOS_USUARIOS = "sistema_tkinter/bd/usuarios.txt"

def salvar_usuario(usuario, senha):
    with open(ARQUIVOS_USUARIOS, "a") as f:
        f.write(f"{usuario},{senha}\n")

def verificar_usuario(usuario, senha):
    if not os.path.exists(ARQUIVOS_USUARIOS):
        return False
    
    with open(ARQUIVOS_USUARIOS, 'r') as f:
        for line in f:
            user, password = line.strip().split(",")
            if user == usuario and password == senha:
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
            imagem = Image.open("sistema_tkinter/img/cadastrar.png")
            imagem = imagem.resize((85, 85), Image.Resampling.LANCZOS)
            self.imagem_tk = ImageTk.PhotoImage(imagem)
            self.image_label = tk.Label(self, image=self.imagem_tk, bg="white")
            self.image_label.pack()
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        tk.Label(frame, text="Novo Usuário: ", bg="black", fg="white").pack()
        self.usuario_entry = tk.Entry(frame)
        self.usuario_entry.pack()

        tk.Label(frame, text="Nova Senha: ", bg="black", fg="white").pack()
        self.senha_entry = tk.Entry(frame, show="*")
        self.senha_entry.pack()

        self.registrar_botao = tk.Button(frame, text="Cadastrar", bg="#4CAF50", fg="white", command=self.cadastrar)
        self.registrar_botao.pack()

        self.voltar_botao = tk.Button(frame, text="Voltar", bg="#FF0000", fg="white",  command=self.voltar)
        self.voltar_botao.pack()
    
    def cadastrar(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if usuario and senha:
            salvar_usuario(usuario, senha)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def voltar(self):
        self.destroy() #Fecha a janela de cadastro
        self.master.deiconify() #Mostra a tela de login
