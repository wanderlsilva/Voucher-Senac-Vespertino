class Ponto: #Nomes de classes possui a primeira letra maiuscula
    #Método Construtor
    def __init__(self, coordenadaX, coordenadaY): #estão contidos todos os atributos deste objeto.
        self.x = coordenadaX #self.x recebe o valor do parametro coordenadaX
        self.y = coordenadaY #self.y recebe o valor do parametro coordenadaY
        #A palavra SELF é obrigatória ao se referir ao objeto em si dentro da classe.

    #Método
    def setX(self, novoX):
    #Este método SETA um novo valor para a posição x.
    #novoX: Este é o novo valor que se deseja atualizar ao ponto.
        self.x = novoX #A variavel self.x é atualizada

    def setY(self, novoY):
    #Este método SETA um novo valor para a posição y.
    #novoY: Este é o novo valor que se deseja atualizar ao ponto.
        self.y = novoY #A variavel self.y é atualizada