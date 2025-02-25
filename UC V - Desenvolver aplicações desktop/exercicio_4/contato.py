class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def __str__(self):
        return f"{self.nome},{self.telefone}" #Formato para salvar no arquivo
    
    @staticmethod
    def from_string(string):
        nome, telefone = string.strip().split(',')
        return Contato(nome, telefone)

class Agenda:
    def __init__(self, arquivo="agenda.txt"):
        self.arquivo = arquivo
        self.contatos = self.carregar_contatos()

    def adicionar_contatos(self, nome, telefone):
        self.contatos.append(Contato(nome, telefone))
        self.salvar_contatos()
        print(f"Contato {nome} adicionado com sucesso!")

    def exibir_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            print("\nLista de contatos: ")
            for i, contato in enumerate(self.contatos, 1):
                print(f"{i}. Nome: {contato.nome}, Telefone: {contato.telefone}")
    
    def buscar_contato(self, nome):
        encontrados = [contato for contato in self.contatos if contato.nome.lower() == nome.lower()]
        if encontrados:
            for contato in encontrados:
                print(f"Encontrado: Nome: {contato.nome}, Telefone: {contato.telefone}")
        else:
            print(f"Nenhum contato encontrado com o nome: {nome}")
    
    def remover_contato(self, nome):
        self.contatos = [contato for contato in self.contatos if contato.nome.lower() != nome.lower()]
        self.salvar_contatos()
        print(f"Contato {nome} removido com sucesso!")
    
    def salvar_contatos(self):
        with open(self.arquivo, "w", encoding="utf-8") as file:
            for contato in self.contatos:
                file.write(str(contato) + "\n")
    
    def carregar_contatos(self):
        contatos = []
        try:
            with open(self.arquivo, "r", encoding="utf-8") as file:
                for linha in file:
                    contatos.append(Contato.from_string(linha))
        except FileNotFoundError:
            pass

        return contatos