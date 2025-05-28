import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "sistemaeventos"
    )

def cadastrar_local():
    nome = input("Nome do local: ")
    endereco = input("Endereço: ")
    capacidade = input("Capacidade: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO local (nome, endereco, capacidade)" \
    "VALUES (%s, %s, %s)", (nome, endereco, capacidade))
    conn.commit()
    print("Local cadastrado com Sucesso!!!")
    conn.close()

def cadastrar_participante():
    nome = input("Nome do participante: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO participante (nome, cpf, email)" \
    "VALUES (%s, %s, %s)", (nome, cpf, email))
    conn.commit()
    print("Participante cadastrado com sucesso!!")
    conn.close()

def listar_eventos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_evento, nome, data  FROM evento")
    for (id_evento, nome, data) in cursor.fetchall():
        print(f"{id_evento}: {nome} em {data}")
    conn.close()

def inscrever_participante():
    listar_eventos()
    id_evento = int(input("Digite o ID do evento: "))
    id_participante = int(input("Digite o ID do participante: "))
    data_inscricao = input("Data de inscrição (YYYY-MM-DD): ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inscricao (id_evento, id_participante, data_inscricao)" \
    "VALUES (%s, %s, %s)", (id_evento, id_participante, data_inscricao))
    conn.commit()
    print("Inscrição realizada com sucesso!")
    conn.close()

def listar_inscricoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT P.nome, E.nome, I.data_inscricao FROM inscricao I" \
    "JOIN partipante P ON i.id_particpante = P.id_participante" \
    "JOIN evento E ON I.id_evento = E.id_evento")
    for (participante, evento, data) in cursor.fetchall():
        print(f"{participante} inscrito em {evento} na data {data}")
    conn.close()

def emitir_certificado():
    id_participante = int(input("ID do participante: "))
    id_evento = int(input("ID do evento: "))
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE certificado SET status = 'Emitido', data_emissao = CURDATE()" \
    "WHERE id_participante = %s AND id_evento = %s", (id_participante, id_evento))
    conn.commit()
    print("Certificado emitido com sucesso!!!")
    conn.close()
    
def menu():
    while True:
        print("----- Sistema de Eventos -----")
        print("1 - Cadastrar Local")
        print("2 - Cadastrar Participante")
        print("3 - Listar Eventos")
        print("4 - Inscrever Participante em Evento")
        print("5 - Listar Inscrições")
        print("Emitir Certificado")
        print("0 - Sair")
        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            cadastrar_local()
        elif opcao == 2:
            cadastrar_participante()
        elif opcao == 3:
            listar_eventos()
        elif opcao == 4:
            print("4")
        elif opcao == 5:
            print("5")
        elif opcao == 6:
            print("6")
        elif opcao == 0:
            print("Saindo...")
        else:
            print("Opção Inválida!!!")

if __name__ == "__main__":
    menu()