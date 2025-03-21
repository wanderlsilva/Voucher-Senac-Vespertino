import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
import random  # Importa o módulo random para gerar posições aleatórias

# Configurações iniciais
tamanho_celula = 20  # Tamanho de cada célula da grade
largura = 400  # Largura do canvas
altura = 400  # Altura do canvas

def mover():
    """Move a cobra na direção atual e verifica colisões."""
    global direcao, cobra, comida, pontuacao
    
    # Obtém a posição da cabeça da cobra
    x, y = cobra[0]
    
    # Define a nova posição com base na direção
    if direcao == "cima":
        y -= tamanho_celula
    elif direcao == "baixo":
        y += tamanho_celula
    elif direcao == "esquerda":
        x -= tamanho_celula
    elif direcao == "direita":
        x += tamanho_celula
    
    # Verifica colisão com as bordas
    if x < 0 or x >= largura or y < 0 or y >= altura:
        game_over()
        return
    
    # Verifica colisão com o próprio corpo
    if (x, y) in cobra:
        game_over()
        return
    
    # Adiciona a nova posição à cobra
    cobra.insert(0, (x, y))
    
    # Verifica se a cobra comeu a comida
    if (x, y) == comida:
        pontuacao += 1  # Incrementa a pontuação
        label_pontos.config(text=f"Pontuação: {pontuacao}")
        nova_comida()  # Gera nova comida
    else:
        cobra.pop()  # Remove a última parte da cobra para manter o tamanho
    
    desenhar()
    janela.after(100, mover)  # Chama a função novamente após 100ms

def mudar_direcao(nova_direcao):
    """Altera a direção da cobra garantindo que não possa ir na direção oposta imediatamente."""
    global direcao
    if (direcao == "cima" and nova_direcao != "baixo") or \
       (direcao == "baixo" and nova_direcao != "cima") or \
       (direcao == "esquerda" and nova_direcao != "direita") or \
       (direcao == "direita" and nova_direcao != "esquerda"):
        direcao = nova_direcao

def nova_comida():
    """Gera uma nova comida em uma posição aleatória que não esteja ocupada pela cobra."""
    global comida
    while True:
        x = random.randint(0, (largura // tamanho_celula) - 1) * tamanho_celula
        y = random.randint(0, (altura // tamanho_celula) - 1) * tamanho_celula
        if (x, y) not in cobra:
            comida = (x, y)
            break

def desenhar():
    """Desenha a cobra e a comida no canvas."""
    canvas.delete("all")
    # Desenha a cobra
    for segmento in cobra:
        x, y = segmento
        canvas.create_rectangle(x, y, x + tamanho_celula, y + tamanho_celula, fill="green")
    # Desenha a comida
    x, y = comida
    canvas.create_oval(x, y, x + tamanho_celula, y + tamanho_celula, fill="red")

def game_over():
    """Exibe a mensagem de fim de jogo e reinicia o jogo."""
    canvas.delete("all")
    canvas.create_text(largura // 2, altura // 2, text="GAME OVER", font=("Arial", 24), fill="red")

def iniciar_jogo():
    """Reinicia todas as configurações do jogo."""
    global cobra, direcao, pontuacao
    cobra = [(100, 100)]  # Posição inicial da cobra
    direcao = "direita"  # Direção inicial
    pontuacao = 0  # Reinicia a pontuação
    label_pontos.config(text=f"Pontuação: {pontuacao}")
    nova_comida()
    mover()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Jogo da Cobrinha")
janela.geometry("400x450")

# Criando o canvas para o jogo
canvas = tk.Canvas(janela, width=largura, height=altura, bg="black")
canvas.pack()

# Criando a label de pontuação
pontuacao = 0
label_pontos = tk.Label(janela, text=f"Pontuação: {pontuacao}", font=("Arial", 14))
label_pontos.pack()

# Inicializando a cobra e a comida
cobra = [(100, 100)]
direcao = "direita"
nova_comida()

# Vinculando as teclas ao movimento
tela = janela.bind("<Up>", lambda event: mudar_direcao("cima"))
tela = janela.bind("<Down>", lambda event: mudar_direcao("baixo"))
tela = janela.bind("<Left>", lambda event: mudar_direcao("esquerda"))
tela = janela.bind("<Right>", lambda event: mudar_direcao("direita"))

# Botão para reiniciar o jogo
botao_restart = tk.Button(janela, text="Reiniciar", command=iniciar_jogo)
botao_restart.pack()

# Iniciar o jogo
iniciar_jogo()

janela.mainloop()  # Inicia o loop principal da interface gráfica
