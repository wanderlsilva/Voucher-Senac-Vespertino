#Sistema de cadastro de alunos
#Você deve criar uma classe chamada Aluno que possua os seguintes atributos:
#nome (string), idade (inteiro), nota (float)
#A classe deve ter os seguintes métodos:
#__init__: para inicializar os atributos.
#exibir_dados(): que imprime as informações do aluno.
#verificar_situacao(): que retorna "Aprovado" se a nota for maior ou igual a 7 e "Reprovado" caso contrário.
#Crie pelo menos dois objetos da classe Aluno e exiba os dados de cada um.
#Mostre se cada aluno está aprovado ou reprovado.
from aluno import Aluno

aluno1 = Aluno("Ana", 14, 6.0)
aluno2 = Aluno("José", 13, 8.4)

aluno1.exibir_dados()
print("Situação: ", aluno1.verificar_situacao())