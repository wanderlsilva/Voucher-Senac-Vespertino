class Ponto:
    def __init__(self, coordenadaX, coordenadaY):
        self.x = coordenadaX
        self.y = coordenadaY
    
    def setX(self, novoX):
        self.x = novoX

    def setY(self, novoY):
        self.y = novoY

ponto1 = Ponto(0,0)
ponto1.x = 1
ponto1.y = 1