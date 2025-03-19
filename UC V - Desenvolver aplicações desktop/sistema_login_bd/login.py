import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bcrypt

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login com MYSQL")
        self.root.geometry("300x250")

        tk.Label(root, text="Usuário: ").pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        tk.Label(root, text="Senha: ").pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        tk.Button(root, text="Login", command=self.verificar_login).pack()
        tk.Button(root, text="Registrar", command=self.registrar_usuario).pack()

        self.conectar_banco()

    def conectar_banco(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="farmacia"
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario VARCHAR(50) UNIQUE NOT NULL,
                    senha VARCHAR(255) NOT NULL
                ) 
            """
            )
            self.conn.commit()
        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro ao conectar no Banco de Dados: {e}")
    
    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if not usuario or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        try:
            self.cursor.execute("SELECT senha FROM usuarios WHERE usuario = %s", (usuario,))
            resultado = self.cursor.fetchone()
            if resultado and bcrypt.checkpw(senha.encode(), resultado[0].encode()):
                messagebox.showinfo("Sucesso", "Login realizado com sucesso!!!")
            else:
                messagebox.showerror("Erro","Usuario ou senha incorretos.")
        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro no login: {e}")
        
    def registrar_usuario(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if not usuario or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        
        hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

        try:
            self.cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)", (usuario, hash_senha))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Usuarios cadastrado com sucesso!!!")
        
        except mysql.connector.IntegrityError as e:
            messagebox.showerror("Erro", f"Usuario já existe.")
       
        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro no Registro: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()