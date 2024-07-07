import flet as ft
from views import views_handler

def main(page: ft.Page):
    page.fonts = {'gagalin': "fonts/Gagalin-Gagalin-Regular.otf"}
    page.theme = ft.Theme(font_family='gagalin')
   
    def route_change(route):
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )
        page.update()

    page.on_route_change = route_change
    page.go('/')

ft.app(target=main, assets_dir='assets')