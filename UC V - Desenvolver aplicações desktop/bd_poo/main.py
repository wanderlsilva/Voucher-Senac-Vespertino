import mysql.connector
from mysql.connector import Error

class BancoDeDados:
    def __init__(self, host, user, password, database):
        self.host = host    #localhost ou 127.0.0.1
        self.user = user    #root
        self.password = password    #""
        self.database = database    #loja

    def conectar(self):
        try:
            conexao = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            if conexao.is_connected():
                return conexao
        except Error as e:
            print(f"Erro ao conectar no Banco de Dados: {e}")
            return None
        
    def executar(self, query, valores=None):
        conexao = self.conectar()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(query, valores)
                conexao.commit()
                return cursor
            except Error as e:
                print(f"Erro ao executar a query: {e}")
            finally:
                conexao.close()
        return None
    
    def buscar(self, query, valores = None):
        conexao = self.conectar()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(query, valores)
                return cursor.fetchall()
            except Error as e:
                print(f"Erro ao buscar dados: {e}")
            finally:
                conexao.close()
        return []
    
class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.db = BancoDeDados("127.0.0.1", "root", "", "loja")

    def salvar(self):
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        valores = (self.nome, self.preco)
        self.db.executar(query, valores)

a = Produto("Mouse", 50.00)
a.salvar()