import tkinter as tk
from tkinter import messagebox

def autenticacao():
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    #Verificar os dados
    if usuario == "Admin" and senha == "123":
        messagebox.showinfo("Usuario", "Login realizado com Sucesso.")
    else:
        messagebox.showerror("Usuario", "Login ou Senha incorreta!!!")

#Criando a janela
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("800x600")

#Criando o widgets
usuario_label = tk.Label(janela, text="Usuário: ")
usuario_label.pack()

usuario_entry = tk.Entry(janela)
usuario_entry.pack()

senha_label = tk.Label(janela, text="Senha: ")
senha_label.pack()

senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

login_botao = tk.Button(janela, text="Login", command=autenticacao)
login_botao.pack()

#Executando a janela
janela.mainloop()