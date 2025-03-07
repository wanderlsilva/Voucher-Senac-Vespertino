import flet as ft

def main(page: ft.Page):
    def on_click(e):
        page.add(ft.Text(f"Botão {e.control.text} Clicado!!!"))
    
    page.title = "Botão para clicar"

    botao = [ft.Button(text=f"Botão {i}", on_click=on_click) for i in range(5)]
    page.add(*botao)

ft.app(target=main)