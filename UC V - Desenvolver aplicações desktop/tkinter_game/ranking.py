import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
import random  # Importa o módulo random para gerar posições aleatórias
import json  # Importa json para salvar e carregar o ranking

# Função para mover o alvo aleatoriamente
def mover_alvo():
    """Move o alvo para uma nova posição aleatória no canvas."""
    global x, y  # Usa variáveis globais para posição
    x = random.randint(50, 350)  # Gera nova posição X aleatória
    y = random.randint(50, 350)  # Gera nova posição Y aleatória
    canvas.coords(alvo, x, y, x+50, y+50)  # Atualiza a posição do alvo

# Função para processar o clique do jogador
def clicar_alvo(event):
    """Verifica se o clique foi dentro do alvo e atualiza a pontuação."""
    global pontuacao  # Usa a variável global da pontuação
    if x <= event.x <= x+50 and y <= event.y <= y+50:  # Verifica se o clique acertou o alvo
        pontuacao += 1  # Incrementa a pontuação
        label_pontos.config(text=f"Pontuação: {pontuacao}")  # Atualiza a exibição da pontuação
        mover_alvo()  # Move o alvo para uma nova posição

# Função para salvar a pontuação no ranking
def salvar_ranking():
    """Salva a pontuação do jogador no ranking e exibe as melhores pontuações."""
    nome = entrada_nome.get().strip()  # Obtém o nome do jogador
    if not nome:
        nome = "Jogador Anônimo"  # Nome padrão caso o jogador não insira um nome
    
    # Carrega o ranking atual ou cria uma lista vazia se o arquivo não existir
    try:
        with open("ranking.json", "r") as arquivo:
            ranking = json.load(arquivo)
    except FileNotFoundError:
        ranking = []
    
    # Adiciona a nova pontuação ao ranking
    ranking.append({"nome": nome, "pontuacao": pontuacao})
    
    # Ordena o ranking do maior para o menor
    ranking = sorted(ranking, key=lambda k: k["pontuacao"], reverse=True)
    
    # Salva o ranking atualizado no arquivo JSON
    with open("ranking.json", "w") as arquivo:
        json.dump(ranking, arquivo, indent=4)
    
    # Exibe as 5 melhores pontuações
    texto_ranking = "Ranking:\n"
    for i, jogador in enumerate(ranking[:5]):  # Exibe os top 5 jogadores
        texto_ranking += f"{i+1}. {jogador['nome']} - {jogador['pontuacao']} pontos\n"
    label_ranking.config(text=texto_ranking)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Jogo com Ranking")
janela.geometry("400x500")

# Campo para entrada do nome do jogador
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=10)
entrada_nome.insert(0, "Digite seu nome")

# Criando o canvas para desenhar o alvo
canvas = tk.Canvas(janela, width=400, height=400, bg="white")
canvas.pack()

# Inicializando a posição do alvo
x = random.randint(50, 350)
y = random.randint(50, 350)
alvo = canvas.create_oval(x, y, x+50, y+50, fill="red")  # Cria um círculo como alvo

# Criando a label para exibir a pontuação
pontuacao = 0
label_pontos = tk.Label(janela, text=f"Pontuação: {pontuacao}", font=("Arial", 14))
label_pontos.pack()

# Criando botão para salvar pontuação no ranking
botao_salvar = tk.Button(janela, text="Salvar Pontuação", command=salvar_ranking)
botao_salvar.pack(pady=5)

# Criando a label para exibir o ranking
top5 = "Ranking:\n1. -\n2. -\n3. -\n4. -\n5. -"
label_ranking = tk.Label(janela, text=top5, font=("Arial", 12), justify="left")
label_ranking.pack()

# Associa o clique no canvas à função clicar_alvo
canvas.bind("<Button-1>", clicar_alvo)

janela.mainloop()  # Inicia o loop principal da interface gráfica
