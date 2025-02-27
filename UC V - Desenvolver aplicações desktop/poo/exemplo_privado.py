class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome #Atributo Publico
        self.idade = idade #Atributo Publico
        self.__nota = nota #Atributo Privado

    def get_nota(self):
        #Método getter para obter a nota do aluno.
        return self.__nota
    
    def set_nota(self, nova_nota):
        #Método setter para definir uma nova nota
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
            print(f"Nota atualizada para : {nova_nota}")
        else:
            print("Nota Inválida! A nota deve estar entre 0 a 10.")
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.__nota}")

aluno1 = Aluno("Carlos", 17, 8.5)
print(aluno1.get_nota())
aluno1.set_nota(6.5)
print(aluno1.get_nota())