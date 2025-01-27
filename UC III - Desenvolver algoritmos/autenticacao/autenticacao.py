import hashlib

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    with open("autenticacao/usuarios.txt", "a+") as arquivo:
        arquivo.seek(0)
        for linha in arquivo:
            dados = linha.strip().split(";")
            if dados[0] == usuario:
                print("Usuário já cadastrado!")
                return
            
    senha_criptografada = criptografar_senha(senha)
    with open("autenticacao/usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario};{senha_criptografada}\n")
    print("Usuário cadastrado com sucesso!")

def login_usuario():
    print('\n=== Login ===')
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    senha_criptografada = criptografar_senha(senha)

    try:
        with open("autenticacao/usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if dados[0] == usuario and dados[1] == senha_criptografada:
                    print("Login realizado com sucesso!")
                    return True
        print("Usuário ou senha incorretos!")
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda!")
    return False

def menu():
    while True:
        print("\n=== Sistema de Login ===")
        print("1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            if login_usuario():
                print("\n Bem vindo ao Sistema!")
                break
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()