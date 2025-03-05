def transposta(matriz):
    return [list(row) for row in zip(*matriz)]

matriz = [ 
    [1,2,3],
    [4,5,6]
    ]
print(transposta(matriz))