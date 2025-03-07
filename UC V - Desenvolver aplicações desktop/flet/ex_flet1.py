import flet as ft

def main(page: ft.Page):
    page.title = "Olá Flet"
    page.add(ft.Text("Olá Mundo!!!"))

ft.app(target=main)