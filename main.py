import flet as ft

def main(page:ft.Page):
    page.title = "TemplatePOS"

    page.add(ft.Text("Welcome to TemplatePOS!"))

ft.app(target=main)