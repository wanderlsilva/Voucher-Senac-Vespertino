from contato import *

def menu():
    agenda = Agenda()

    while True:
        print("\n AGENDA DE CONTATOS")
        print("1 - Adicionar Contato")
        print("2 - Exibir Contatos")
        print("3 - Buscar Contato")
        print("4 - Remover Contato")
        print("5 - Sair")
        opcao = input ("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            agenda.adicionar_contatos(nome, telefone)
        elif opcao == "2":
            agenda.exibir_contatos()
        elif opcao == "3":
            nome = input("Digite o nome para buscar: ")
            agenda.buscar_contato(nome)
        elif opcao == "4":
            nome = input("Digite um nome para remover: ")
            agenda.remover_contato(nome)
        elif opcao == "5":
            print("Saindo da agenda...")
            break
        else:
            print("Opção Inválida!")

menu()