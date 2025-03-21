import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
import random  # Importa o módulo random para gerar posições aleatórias

# Função para mover o quadrado para uma nova posição aleatória
def mover_quadrado():
    """Atualiza a posição do quadrado na tela de forma aleatória."""
    global x, y  # Declara as variáveis globais para atualizar a posição
    x = random.randint(50, 350)  # Gera uma posição aleatória no eixo X dentro dos limites
    y = random.randint(50, 350)  # Gera uma posição aleatória no eixo Y dentro dos limites
    canvas.coords(quadrado, x, y, x+50, y+50)  # Atualiza a posição do quadrado no canvas

def clicar_quadrado(event):
    """Verifica se o jogador clicou dentro do quadrado e atualiza a pontuação."""
    global pontuacao  # Declara a variável global da pontuação
    if x <= event.x <= x+50 and y <= event.y <= y+50:  # Verifica se o clique ocorreu dentro do quadrado
        pontuacao += 1  # Incrementa a pontuação
        label_pontos.config(text=f"Pontuação: {pontuacao}")  # Atualiza a exibição da pontuação
        mover_quadrado()  # Move o quadrado para uma nova posição aleatória

# Configuração da janela principal
janela = tk.Tk()  # Inicializa a janela principal do Tkinter
janela.title("Acerte o Quadrado")  # Define o título da janela
janela.geometry("400x450")  # Define o tamanho da janela

# Criando o canvas para desenhar os elementos do jogo
canvas = tk.Canvas(janela, width=400, height=400, bg="white")  # Cria um canvas com fundo branco
canvas.pack()  # Adiciona o canvas à janela

# Inicializando a posição do quadrado
x = random.randint(50, 350)  # Posição inicial aleatória no eixo X

y = random.randint(50, 350)  # Posição inicial aleatória no eixo Y
quadrado = canvas.create_rectangle(x, y, x+50, y+50, fill="red")  # Desenha um quadrado vermelho

# Criando a label para exibir a pontuação
pontuacao = 0  # Inicializa a pontuação em zero
label_pontos = tk.Label(janela, text=f"Pontuação: {pontuacao}", font=("Arial", 14))  # Cria um rótulo para exibir a pontuação
label_pontos.pack()  # Adiciona a label à janela

# Associando o clique no canvas à função clicar_quadrado
canvas.bind("<Button-1>", clicar_quadrado)  # Liga o evento de clique do mouse à função clicar_quadrado

janela.mainloop()  # Inicia o loop principal da interface gráfica
