import mysql.connector
try:
    conexao = mysql.connector.Connect(
        host = "localhost",
        database = "farmacia",
        user = "root",
        password = ""
    )
    if conexao.is_connected():
        informacaobanco = conexao.get_server_info()
        print(f"Conectado ao servidor do banco de dados {informacaobanco}")
        print("Conexao OK")
        comandosql = conexao.cursor()
        comandosql.execute('select database();')
        nomebanco = comandosql.fetchone()
        print(f"Banco de dados acessado = {nomebanco}")
    else:
        print("Conexao não realizada com banco")
except Exception as erro:
    print(f"Erro: {erro}")