import flet as ft

def main(page: ft.Page):
    def on_click(e):
        page.add(ft.Text("Você clicou no botão"))
    
    page.title = "Tela Flet"
    page.add(ft.Button(text="Clica Aqui", on_click=on_click))

ft.app(target=main)