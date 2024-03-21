import flet as ft
import pandas as pd

df = pd.read_csv('datos_todos.csv')

def getinfo(index):
    return print(df.iloc[index]['Color'])

def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    gv = ft.GridView(expand=True,runs_count=5, max_extent=400, child_aspect_ratio=0.9,spacing=5,run_spacing=5,)
    page.add(gv)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Buscar"),
            ft.NavigationDestination(icon=ft.icons.EXPLORE_OUTLINED,selected_icon=ft.icons.EXPLORE, label="Explorar"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Guardados",
            ),
        ],bgcolor=ft.colors.PINK_100,height=70,
    )

    for i in range(0, 5000):
        gv.controls.append(
            ft.Stack(
                [
                    ft.Container(content=ft.Image(src=df.iloc[i]['Imagenes'], width=250, height=300, fit=ft.ImageFit.FILL,
                                                   repeat=ft.ImageRepeat.NO_REPEAT, border_radius=15), 
                                 ink=True,
                                 ink_color=ft.colors.BLACK12,
                                 border_radius=30,
                                 on_click=lambda e, index=i: getinfo(index)),
                    ft.Text(f"{df.iloc[i]['Temporada']}",
                            color="Yellow",
                            size=25,
                            weight="bold",
                            top=1,text_align=ft.alignment.top_center)
                ]
            )
        )
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
