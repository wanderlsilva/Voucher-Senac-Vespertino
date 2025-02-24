class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def exibir_dados(self):
        print("Nome: {} \n Idade: {} \n Nota: {}".format(self.nome, self.idade, self.nota))

    def verificar_situacao(self):
        return "Aprovado" if self.nota >= 7 else "Reprovado"