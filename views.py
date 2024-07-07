import flet as ft
from pages.home import Home

def views_handler(page: ft.Page):

  container_home = ft.Container(
    content=Home(page),
    expand=True,
  )

  return {
    '/':ft.View(
      route='/',
      controls=[
        container_home,
        ],
        bgcolor='#302369'
      )
  }