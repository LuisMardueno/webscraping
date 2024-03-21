import flet as ft
import pandas as pd
df = pd.read_csv('datos_todos.csv')

def getinfo(index):
    print(f"Indice: {index}")
    return

def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 5
    page.update()

    page.add(ft.Text("Texto", color=ft.colors.BLACK))
    
    left_column = ft.Column(
        [ft.Text("THIS IS COL 1", color=ft.colors.RED_400)],
        scroll='Auto',
    )
    left_container = ft.Container(
        left_column,
        expand=True,
        margin=10,
        padding=10,
        bgcolor=ft.colors.LIGHT_GREEN_100,
        border_radius=10,
        alignment=ft.alignment.top_center,
    )
    right_column = ft.Column(
        [ft.Text("THIS IS COL 2", color=ft.colors.RED_400)],
        scroll='Auto',expand_loose=True
    )
    right_container = ft.Container(
        right_column,
        expand=True,
        margin=10,
        padding=10,
        bgcolor=ft.colors.LIGHT_GREEN_100,
        border_radius=10,
        alignment=ft.alignment.top_center,
    )
    row = ft.Row([left_container, right_container], expand=True)
    page.add(row)

    for i in range(0, 100):
        left_column.controls.append(
            ft.Container(content=ft.Image(src=df.iloc[i]['Imagenes'],width=400,height=500,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(10), ),
                                        ink=True,
                                        border_radius=10,
                                        on_click=lambda e: getinfo(i)),)

    for i in range(0, 100):
        right_column.controls.append( ft.Stack(
            [
                ft.Container(content=ft.Image(src=df.iloc[i+30]['Imagenes'],width=400,height=500,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(10), ),
                                        ink=True,
                                        border_radius=10,
                                        on_click=lambda e: getinfo(i)),
                ft.Text(f"{df.iloc[i+30]['Temporada']}",color="Black",size=30,weight="bold",)

            ]
        )
            
        )
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)