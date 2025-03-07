import tkinter as tk
from tkinter import messagebox

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela de Login")

        #widgets
        self.usuario_label = tk.Label(self, text="Usuario")
        self.usuario_label.pack()

        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        self.senha_label = tk.Label(self, text="Senha")
        self.senha_label.pack()

        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack()

        self.login_botao = tk.Button(self, text="Login", command=login)
        self.login_botao.pack()
    
    def login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if usuario == "Admin" and senha == "123":
            messagebox.showinfo("Usuario", "Login realizado com sucesso.")
        else:
            messagebox.showerror('Usuario', 'Login ou Senha Incorreta!!!')

app = LoginApp()
app.mainloop()