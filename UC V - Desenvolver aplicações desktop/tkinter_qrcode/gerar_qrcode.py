import tkinter as tk # Importa a biblioteca para criar interface gráfica
from tkinter import filedialog # Importa o módulo para abrir a janela de seleção de arquivo
import qrcode # Importa a biblioteca para gerar QR Codes
from PIL import Image, ImageTk # Importa o PIL para manipulação de imagens

def gerar_qrcode():
    texto = entrada_texto.get() # Captura o texto digitado
    if texto:
        qr = qrcode.QRCode(
            version = 1, # Tamanho do QR Code
            error_correction = qrcode.constants.ERROR_CORRECT_L, # Nivel de correção de erro
            box_size = 10, # Tamanho dos quadrados pretos do QR Code
            border = 4 # Largura da borda branca ao redor do QR Code
        )
        qr.add_data(texto) # Adiciona o texto ao QR Code
        qr.make(fit=True) # Gera o QR Code
        img = qr.make_image(fill='black', back_color='white') # Define as cores do QR Code

        img.thumbnail((200,200)) # Redimensiona a imagem para exibição na interface
        img_tk = ImageTk.PhotoImage(img) # Converte a imagem para exibição no Tkinter
        label_imagem.config(image=img_tk) # Atualiza a exibiçao da imagem
        label_imagem.image = img_tk # Mantém a referencia para evitar que a imagem seja apagada

        global imagem_gerada # Declara a variavel global para salvar a imagem posteriormente
        imagem_gerada = img

def salvar_qrcode():
    if imagem_gerada:  # Verifica se ha uma imagem gerada
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".png", # Define o formato padrao do arquivo
            filetypes=[("PNG Files", "*.png"),("ALL Files", "*.*") ] # Tipos de arquivos suportados
        )
        if arquivo: # Verifica se um nome de arquivo foi escolhido
            imagem_gerada.save(arquivo) # Salva a imagem no loval especificado

# Criação da Janela principal
janela = tk.Tk() # Inicializa a janela do tkinter
janela.title("Gerando QR Code") # Define o titulo da janela
janela.geometry("400x400") # Define o tamanho da janela

# Campo de entrada para o texto do QR Code
entrada_texto = tk.Entry(janela, width=40) # Cria um campo de entrada de texto
entrada_texto.pack(pady=10) # Adiciona o campo à janela com espaçamento

#Botão para gerar o QR Code
botao_gerar = tk.Button(janela, text="Gerar QR Code", command=gerar_qrcode) # Cria um botão para Gerar o QR Code
botao_gerar.pack(pady=5) # Adiciona o botão à janela com espaçamento

# Label para exibir a imagem do QR Code
label_imagem = tk.Label(janela) # Cria um rótulo parar exibir a imagem
label_imagem.pack(pady=10) # Adiciona o rótulo à janela

# Botão para salvar o QR Code gerado
botao_salvar = tk.Button(janela, text="Salvar QR Code", command=salvar_qrcode) # Cria um botão para salvar imagem
botao_salvar.pack(pady=5) # Adiciona o botão à janela com espaçamento

imagem_gerada = None # Inicializa a variavel global para armazenar a imagem do QR Code

janela.mainloop() # Inicia o loop principal da interface grafica